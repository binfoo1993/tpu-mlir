//===----------------------------------------------------------------------===//
//
// Copyright (C) 2022 Sophgo Technologies Inc.  All rights reserved.
//
// TPU-MLIR is licensed under the 2-Clause BSD License except for the
// third-party components.
//
//===----------------------------------------------------------------------===//

#include "../Lowering.h"

using namespace mlir;
using namespace tpu_mlir;
using namespace tpu_mlir::helper;

void top::SqueezeOp::lowering_int8_bm1684x(PatternRewriter &rewriter,
                                           bool asymmetric) {
  lowering_common_int8<tpu::SqueezeOp>(rewriter, getOperation(), asymmetric);
}

void top::SqueezeOp::lowering_f32_bm1684x(PatternRewriter &rewriter) {
  lowering_common_float<tpu::SqueezeOp>(rewriter, getOperation());
}

void top::SqueezeOp::lowering_bf16_bm1684x(PatternRewriter &rewriter) {
  lowering_common_float<tpu::SqueezeOp, BFloat16Type>(rewriter, getOperation());
}

void top::SqueezeOp::lowering_f16_bm1684x(PatternRewriter &rewriter) {
  lowering_common_float<tpu::SqueezeOp, Float16Type>(rewriter, getOperation());
}

void top::SqueezeOp::lowering_quant_bm1684x(PatternRewriter &rewriter) {
  lowering_common<tpu::SqueezeOp>(rewriter, getOperation(), output().getType());
}
