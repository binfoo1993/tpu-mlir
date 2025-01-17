//===----------------------------------------------------------------------===//
//
// Copyright (C) 2022 Sophgo Technologies Inc.  All rights reserved.
//
// TPU-MLIR is licensed under the 2-Clause BSD License except for the
// third-party components.
//
//===----------------------------------------------------------------------===//

#include "../Lowering.h"

using namespace tpu_mlir;
using namespace tpu_mlir::helper;
using namespace mlir;

void top::DivOp::lowering_int8_bm1684x(PatternRewriter &rewriter,
                                       bool asymmetric) {
  lowering_f32_bm1684x(rewriter);
}

void top::DivOp::lowering_f32_bm1684x(PatternRewriter &rewriter) {
  lowering_common_float<tpu::DivOp>(rewriter, getOperation());
}

void top::DivOp::lowering_bf16_bm1684x(PatternRewriter &rewriter) {
  lowering_common_float<tpu::DivOp, Float32Type>(rewriter, getOperation());
}

void top::DivOp::lowering_f16_bm1684x(PatternRewriter &rewriter) {
  lowering_common_float<tpu::DivOp, Float32Type>(rewriter, getOperation());
}

void top::DivOp::lowering_quant_bm1684x(PatternRewriter &rewriter) {
  lowering_common<tpu::DivOp>(rewriter, getOperation(), output().getType());
}
