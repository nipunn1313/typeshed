# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    NewType as typing___NewType,
    cast as typing___cast,
)


builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

LazyEnumValue = typing___NewType('LazyEnumValue', builtin___int)
type___LazyEnumValue = LazyEnumValue
LazyEnum: _LazyEnum
class _LazyEnum(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[LazyEnumValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    LAZY_ENUM_0 = typing___cast(LazyEnumValue, 0)
    LAZY_ENUM_1 = typing___cast(LazyEnumValue, 1)
LAZY_ENUM_0 = typing___cast(LazyEnumValue, 0)
LAZY_ENUM_1 = typing___cast(LazyEnumValue, 1)
type___LazyEnum = LazyEnum
