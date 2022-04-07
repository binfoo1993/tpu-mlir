//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
// Also available under a BSD-style license. See LICENSE.
//
//===----------------------------------------------------------------------===//

#include "sophgo/Dialect/Tpu/IR/TpuOps.h"
#include "sophgo/Interfaces/InferenceInterface.h"
#include "sophgo/Support/Dnnl/Conv.h"
#include "sophgo/Support/Dnnl/Pool.h"
#include "sophgo/Support/Dnnl/MatMul.h"
#include "sophgo/Support/Helper/Quant.h"

#include "mlir/IR/Builders.h"
#include "mlir/IR/BuiltinOps.h"
#include "mlir/IR/PatternMatch.h"
#include "mlir/IR/TypeUtilities.h"
#include "mlir/Support/LLVM.h"
#include "llvm/ADT/StringMap.h"
#include "llvm/Support/Casting.h"
#include "dnnl.hpp"

using namespace sophgo;
using namespace mlir;

template <typename T> static void relu(T *src, T *dst, size_t size, bool bint8 = false) {
#pragma omp parallel for schedule(static, omp_schedule(size))
  for (size_t i = 0; i < size; ++i) {
    dst[i] = src[i] > 0 ? src[i] : 0;
    if (bint8) {
      dst[i]  = dst[i]  > 255?255:dst[i] <0?0:dst[i];
    }
  }
}

LogicalResult tpu::ConvOp::init(InferenceParameter &p) {
  auto conv = new Conv();
  int64_t n, ic, ih, iw, oc, oh, ow, g, kh, kw, ins_h, ins_w, sh, sw, pt, pb,
      pl, pr, dh, dw;
  bool is_dw, with_bias, relu;
  parseParam(n, ic, ih, iw, oc, oh, ow, g, kh, kw, ins_h, ins_w, sh, sw, pt, pb,
             pl, pr, dh, dw, is_dw, with_bias, relu);

  memory::data_type idt, wdt, bdt, odt;
  idt = wdt = bdt = odt = memory::data_type::f32;
  if(input().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>()){
    idt = memory::data_type::s8;
  }
  if(filter().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedPerAxisType>() ||
    filter().getType().cast<RankedTensorType>().getElementType().isInteger(8)){
    wdt = memory::data_type::s8;
  }
  if(output().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>()) {
    odt = memory::data_type::s32;
  }
  auto bdtype = bias().getType().cast<RankedTensorType>().getElementType();
  if (with_bias && (bdtype.isInteger(16) || bdtype.isInteger(32))) {
    bdt = memory::data_type::s32;
  }

  /*auto module = Module::getModuleOp(this);
  if (Module::getChip(module) == Module::Chip::BM1686) {
    newValue = quantize_op.quantize_int8_bm1686();
  }*/

  int* p_rshift = nullptr;
  int* p_multipler = nullptr;
  std::vector<int> rshift_v;
  std::vector<int> multipler_v;
  bool per_channel = false;
  int size = multipler().hasValue()?multipler().getValue().size():0;
  if (size >1) {
    per_channel = true;
  }
  if (size > 0) {
    for (size_t i = 0; i < oc; i++) {
      rshift_v.push_back(rshift().getValue()[i].cast<IntegerAttr>().getInt());
      multipler_v.push_back(multipler().getValue()[i].cast<IntegerAttr>().getInt());
    }
    p_rshift = rshift_v.data();
    p_multipler = multipler_v.data();
  } else {
    rshift_v.push_back(rshift().getValue()[0].cast<IntegerAttr>().getInt());
    p_rshift = rshift_v.data();
  }

  conv->setup(p.inputs[0], p.inputs[1], p.inputs[2], p.outputs[0], n, ic, ih, //fixme p.inputs[2] maybe null???
              iw, oc, oh, ow, kh, kw, sh, sw, dh, dw, pt, pb, pl, pr, g, do_relu(), p_rshift, p_multipler, idt, wdt, bdt, odt, per_channel);
  p.handle = (void *)conv;
  return success();
}

void tpu::ConvOp::deinit(InferenceParameter &p) {
  if (p.handle != nullptr) {
    auto conv = (Conv *)p.handle;
    delete conv;
    p.handle = nullptr;
  }
}

LogicalResult tpu::ConvOp::inference(InferenceParameter &p) {
  if (p.handle == nullptr) {
    return failure();
  }
  auto conv = (Conv *)p.handle;
  conv->run();
  //llvm::errs() << "ConvOp inference:" << this->name() << "\n";
  for (int i = 0; i < 5; i++) {
    //printf("%d  %f x %d +%f = %f\n", i, p.inputs[0][i], (int8_t)p.inputs[1][i], p.inputs[2][i], p.outputs[0][i]);
  }
  return success();
}

LogicalResult tpu::ReluOp::inference(InferenceParameter &p) {
  auto num_elem = input().getType().cast<RankedTensorType>().getNumElements();
  relu(p.inputs[0], p.outputs[0], num_elem, \
    input().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>());
  return success();
}

LogicalResult tpu::AddOp::inference(InferenceParameter &p) {
  auto num_elem = output().getType().cast<RankedTensorType>().getNumElements();
  auto dtype = output().getType().cast<RankedTensorType>().getElementType();
  auto zp = dtype.cast<quant::UniformQuantizedType>().getZeroPoint();
#pragma omp parallel for schedule(static, omp_schedule(num_elem))
  for (int64_t i = 0; i < num_elem; i++) {
    p.outputs[0][i] = 0;
    int idx = 0;
    for (auto in : p.inputs) {
      if (in != nullptr) {
        int rshift = rshifts().getValue()[idx].cast<IntegerAttr>().getInt();
        int multiplier = (int8_t)coeff().getValue()[idx].cast<FloatAttr>().getValueAsDouble();
        p.outputs[0][i] += (int32_t)(in[i]*multiplier)>>rshift;
      }
      idx++;
    }

    if (do_relu()) { //relu输出
      p.outputs[0][i] = p.outputs[0][i] > 255?255:p.outputs[0][i]<0?0:p.outputs[0][i];
    } else {
      p.outputs[0][i] = p.outputs[0][i] > 127?127:p.outputs[0][i]<-128?-128:p.outputs[0][i];
    }
  }
  //llvm::errs() << "AddOp inference:" << this->name() << "\n";
  for (int i = 0; i < 5; i++) {
    //printf("%d, %f+%f = %f\n", i, p.inputs[0][i], p.inputs[1][i], p.outputs[0][i]);
  }
  return success();
}

LogicalResult tpu::MaxPoolOp::init(InferenceParameter &p) {
  auto pooling = new Pooling();
  int64_t n, c, ih, iw, oh, ow, kh, kw, sh, sw, pt, pb, pl, pr, pad_value;
  bool is_global, count_include_pad;
  memory::data_type dt = memory::data_type::f32;
  if(input().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>()){
    dt = memory::data_type::s8;
  }
  parseParam(n, c, ih, iw, oh, ow, kh, kw, sh, sw, pt, pb, pl, pr, pad_value,
             is_global, count_include_pad);
  pooling->setup(p.inputs[0], p.outputs[0], n, c, ih, iw, oh, ow, kh, kw, sh,
                 sw, pt, pb, pl, pr, false, count_include_pad, pad_value, dt);
  p.handle = (void *)pooling;
  return success();
}

void tpu::MaxPoolOp::deinit(InferenceParameter &p) {
  if (p.handle != nullptr) {
    auto pooling = (Pooling *)p.handle;
    delete pooling;
    p.handle = nullptr;
  }
  return;
}

LogicalResult tpu::MaxPoolOp::inference(InferenceParameter &p) {
  if (p.handle == nullptr) {
    return failure();
  }
  auto pooling = (Pooling *)p.handle;
  pooling->run();
  if (do_relu()) {
    size_t num_elem =
        output().getType().cast<RankedTensorType>().getNumElements();
    relu(p.outputs[0], p.outputs[0], num_elem, \
      input().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>());
  }
  return success();
}

LogicalResult tpu::AvgPoolOp::init(InferenceParameter &p) {
  auto pooling = new Pooling();
  int64_t n, c, ih, iw, oh, ow, kh, kw, sh, sw, pt, pb, pl, pr, pad_value;
  bool is_global, count_include_pad;
  memory::data_type dt = memory::data_type::f32;
  if(input().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>()){
    dt = memory::data_type::s8;
  }
  parseParam(n, c, ih, iw, oh, ow, kh, kw, sh, sw, pt, pb, pl, pr, pad_value,
             is_global, count_include_pad);
  pooling->setup(p.inputs[0], p.outputs[0], n, c, ih, iw, oh, ow, kh, kw, sh,
                 sw, pt, pb, pl, pr, true, count_include_pad, pad_value, dt);
  p.handle = (void *)pooling;
  return success();
}

void tpu::AvgPoolOp::deinit(InferenceParameter &p) {
  if (p.handle != nullptr) {
    auto pooling = (Pooling *)p.handle;
    delete pooling;
    p.handle = nullptr;
  }
  return;
}

LogicalResult tpu::AvgPoolOp::inference(InferenceParameter &p) {
  if (p.handle == nullptr) {
    return failure();
  }
  auto pooling = (Pooling *)p.handle;
  pooling->run();
  if (do_relu()) {
    size_t num_elem =
        output().getType().cast<RankedTensorType>().getNumElements();
    relu(p.outputs[0], p.outputs[0], num_elem, \
      input().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>());
  }
  //llvm::errs() << "AvgPoolOp inference:" << this->name() << "\n";
  for (int i = 0; i < 5; i++) {
    //printf("%d  %f -> %f\n", i, p.inputs[0][i], p.outputs[0][i]);
  }
  return success();
}

LogicalResult tpu::ReshapeOp::inference(InferenceParameter &p) {
  auto num_elem = output().getType().cast<RankedTensorType>().getNumElements();
#pragma omp parallel for schedule(static, omp_schedule(num_elem))
  for (int64_t i = 0; i < num_elem; i++) {
    p.outputs[0][i] = p.inputs[0][i];
  }
  return success();
}

LogicalResult tpu::MatMulOp::init(InferenceParameter &p) {
  auto matmul = new MatMul();
  int64_t batch, M, K, N;
  bool with_bias;
  parseParam(batch, M, K, N, with_bias);
  memory::data_type ldt, rdt, bdt, odt;
  ldt = rdt = bdt = odt = memory::data_type::f32;
  if(input().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>()){
    ldt = memory::data_type::s8;
  }
  if(right().getType().cast<RankedTensorType>().getElementType().isInteger(8)){
    rdt = memory::data_type::s8;
  }
  if(output().getType().cast<RankedTensorType>().getElementType().isa<quant::UniformQuantizedType>()) {
    odt = memory::data_type::s32;
  }
  if (with_bias && bias().getType().cast<RankedTensorType>().getElementType().isInteger(16)) {
    bdt = memory::data_type::s32;
  }

  matmul->setup(p.inputs[0], p.inputs[1], p.inputs[2], p.outputs[0], batch, M,
                K, N, do_relu(), rshift(), multipler(), ldt, rdt, bdt, odt);
  p.handle = (void *)matmul;
  return success();
}

void tpu::MatMulOp::deinit(InferenceParameter &p) {
  if (p.handle != nullptr) {
    auto matmul = (MatMul *)p.handle;
    delete matmul;
    p.handle = nullptr;
  }
  return;
}

LogicalResult tpu::MatMulOp::inference(InferenceParameter &p) {
  if (p.handle == nullptr) {
    return failure();
  }
  auto matmul = (MatMul *)p.handle;
  matmul->run();
  //llvm::errs() << "MatMulOp inference:" << this->name() << "\n";
  for (int i = 0; i < 5; i++) {
    //printf("%d  %f x %d +%f = %f\n", i, p.inputs[0][i], (int8_t)p.inputs[1][i], p.inputs[2][i], p.outputs[0][i]);
  }
  return success();
}

LogicalResult tpu::CastOp::inference(InferenceParameter &p) {
  auto num_elem = output().getType().cast<RankedTensorType>().getNumElements();
  auto dtype = output().getType().cast<RankedTensorType>().getElementType();
  if (dtype.isa<quant::UniformQuantizedType>()) {
    auto scale = dtype.cast<quant::UniformQuantizedType>().getScale();
    llvm::errs() << "CastOp fp32 to int8 scale:" << scale <<"\n";
#pragma omp parallel for schedule(static, omp_schedule(num_elem))
    for (size_t i = 0; i < num_elem; i++) {
      p.outputs[0][i] = (int8_t)(p.inputs[0][i]/scale);
      //if (i < 5) printf("CastOp: %f/%f -> %f\n", p.inputs[0][i], scale, p.outputs[0][i]);
    }
  } else if (dtype.isa<mlir::Float32Type>()) {
    auto type = input().getType().cast<RankedTensorType>();
    auto uniform_type = type.getElementType().cast<quant::UniformQuantizedType>();
    auto scale = uniform_type.getScale();
    llvm::errs() << "CastOp int8 to fp32 scale:" << scale <<"\n";
#pragma omp parallel for schedule(static, omp_schedule(num_elem))
    for (size_t i = 0; i < num_elem; i++) {
      p.outputs[0][i] = scale*p.inputs[0][i];
    }
  }
  return success();
}