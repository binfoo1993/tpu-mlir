
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _math_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "math"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AbsOp(_ods_ir.OpView):
  OPERATION_NAME = "math.abs"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class Atan2Op(_ods_ir.OpView):
  OPERATION_NAME = "math.atan2"

  _ODS_REGIONS = (0, True)

  def __init__(self, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AtanOp(_ods_ir.OpView):
  OPERATION_NAME = "math.atan"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CeilOp(_ods_ir.OpView):
  OPERATION_NAME = "math.ceil"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CopySignOp(_ods_ir.OpView):
  OPERATION_NAME = "math.copysign"

  _ODS_REGIONS = (0, True)

  def __init__(self, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CosOp(_ods_ir.OpView):
  OPERATION_NAME = "math.cos"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CountLeadingZerosOp(_ods_ir.OpView):
  OPERATION_NAME = "math.ctlz"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CountTrailingZerosOp(_ods_ir.OpView):
  OPERATION_NAME = "math.cttz"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CtPopOp(_ods_ir.OpView):
  OPERATION_NAME = "math.ctpop"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ErfOp(_ods_ir.OpView):
  OPERATION_NAME = "math.erf"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class Exp2Op(_ods_ir.OpView):
  OPERATION_NAME = "math.exp2"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ExpM1Op(_ods_ir.OpView):
  OPERATION_NAME = "math.expm1"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ExpOp(_ods_ir.OpView):
  OPERATION_NAME = "math.exp"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FloorOp(_ods_ir.OpView):
  OPERATION_NAME = "math.floor"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class FmaOp(_ods_ir.OpView):
  OPERATION_NAME = "math.fma"

  _ODS_REGIONS = (0, True)

  def __init__(self, a, b, c, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(a))
    operands.append(_get_op_result_or_value(b))
    operands.append(_get_op_result_or_value(c))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def a(self):
    return self.operation.operands[0]

  @builtins.property
  def b(self):
    return self.operation.operands[1]

  @builtins.property
  def c(self):
    return self.operation.operands[2]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class Log10Op(_ods_ir.OpView):
  OPERATION_NAME = "math.log10"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class Log1pOp(_ods_ir.OpView):
  OPERATION_NAME = "math.log1p"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class Log2Op(_ods_ir.OpView):
  OPERATION_NAME = "math.log2"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class LogOp(_ods_ir.OpView):
  OPERATION_NAME = "math.log"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class PowFOp(_ods_ir.OpView):
  OPERATION_NAME = "math.powf"

  _ODS_REGIONS = (0, True)

  def __init__(self, lhs, rhs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(lhs))
    operands.append(_get_op_result_or_value(rhs))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def lhs(self):
    return self.operation.operands[0]

  @builtins.property
  def rhs(self):
    return self.operation.operands[1]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class RsqrtOp(_ods_ir.OpView):
  OPERATION_NAME = "math.rsqrt"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SinOp(_ods_ir.OpView):
  OPERATION_NAME = "math.sin"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SqrtOp(_ods_ir.OpView):
  OPERATION_NAME = "math.sqrt"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class TanhOp(_ods_ir.OpView):
  OPERATION_NAME = "math.tanh"

  _ODS_REGIONS = (0, True)

  def __init__(self, operand, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(operand))
    results.extend([operands[0].type] * 1)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def operand(self):
    return self.operation.operands[0]

  @builtins.property
  def result(self):
    return self.operation.results[0]