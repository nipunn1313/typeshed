# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    NewType as typing___NewType,
    Optional as typing___Optional,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

MyEnumValue = typing___NewType('MyEnumValue', builtin___int)
type___MyEnumValue = MyEnumValue
MyEnum: _MyEnum
class _MyEnum(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MyEnumValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    FOO = typing___cast(MyEnumValue, 0)
    BAR = typing___cast(MyEnumValue, 1)
    BAZ = typing___cast(MyEnumValue, 2)
FOO = typing___cast(MyEnumValue, 0)
BAR = typing___cast(MyEnumValue, 1)
BAZ = typing___cast(MyEnumValue, 2)
type___MyEnum = MyEnum

MyEnumPlusExtraValue = typing___NewType('MyEnumPlusExtraValue', builtin___int)
type___MyEnumPlusExtraValue = MyEnumPlusExtraValue
MyEnumPlusExtra: _MyEnumPlusExtra
class _MyEnumPlusExtra(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[MyEnumPlusExtraValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    E_FOO = typing___cast(MyEnumPlusExtraValue, 0)
    E_BAR = typing___cast(MyEnumPlusExtraValue, 1)
    E_BAZ = typing___cast(MyEnumPlusExtraValue, 2)
    E_EXTRA = typing___cast(MyEnumPlusExtraValue, 3)
E_FOO = typing___cast(MyEnumPlusExtraValue, 0)
E_BAR = typing___cast(MyEnumPlusExtraValue, 1)
E_BAZ = typing___cast(MyEnumPlusExtraValue, 2)
E_EXTRA = typing___cast(MyEnumPlusExtraValue, 3)
type___MyEnumPlusExtra = MyEnumPlusExtra

class MyMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    e: type___MyEnumValue = ...
    repeated_e: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___MyEnumValue] = ...
    repeated_packed_e: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___MyEnumValue] = ...
    repeated_packed_unexpected_e: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___MyEnumPlusExtraValue] = ...
    oneof_e_1: type___MyEnumValue = ...
    oneof_e_2: type___MyEnumValue = ...

    def __init__(self,
        *,
        e : typing___Optional[type___MyEnumValue] = None,
        repeated_e : typing___Optional[typing___Iterable[type___MyEnumValue]] = None,
        repeated_packed_e : typing___Optional[typing___Iterable[type___MyEnumValue]] = None,
        repeated_packed_unexpected_e : typing___Optional[typing___Iterable[type___MyEnumPlusExtraValue]] = None,
        oneof_e_1 : typing___Optional[type___MyEnumValue] = None,
        oneof_e_2 : typing___Optional[type___MyEnumValue] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"o",b"o",u"oneof_e_1",b"oneof_e_1",u"oneof_e_2",b"oneof_e_2"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"e",b"e",u"o",b"o",u"oneof_e_1",b"oneof_e_1",u"oneof_e_2",b"oneof_e_2",u"repeated_e",b"repeated_e",u"repeated_packed_e",b"repeated_packed_e",u"repeated_packed_unexpected_e",b"repeated_packed_unexpected_e"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"o",b"o"]) -> typing_extensions___Literal["oneof_e_1","oneof_e_2"]: ...
type___MyMessage = MyMessage

class MyMessagePlusExtra(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    e: type___MyEnumPlusExtraValue = ...
    repeated_e: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___MyEnumPlusExtraValue] = ...
    repeated_packed_e: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___MyEnumPlusExtraValue] = ...
    repeated_packed_unexpected_e: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___MyEnumPlusExtraValue] = ...
    oneof_e_1: type___MyEnumPlusExtraValue = ...
    oneof_e_2: type___MyEnumPlusExtraValue = ...

    def __init__(self,
        *,
        e : typing___Optional[type___MyEnumPlusExtraValue] = None,
        repeated_e : typing___Optional[typing___Iterable[type___MyEnumPlusExtraValue]] = None,
        repeated_packed_e : typing___Optional[typing___Iterable[type___MyEnumPlusExtraValue]] = None,
        repeated_packed_unexpected_e : typing___Optional[typing___Iterable[type___MyEnumPlusExtraValue]] = None,
        oneof_e_1 : typing___Optional[type___MyEnumPlusExtraValue] = None,
        oneof_e_2 : typing___Optional[type___MyEnumPlusExtraValue] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"o",b"o",u"oneof_e_1",b"oneof_e_1",u"oneof_e_2",b"oneof_e_2"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"e",b"e",u"o",b"o",u"oneof_e_1",b"oneof_e_1",u"oneof_e_2",b"oneof_e_2",u"repeated_e",b"repeated_e",u"repeated_packed_e",b"repeated_packed_e",u"repeated_packed_unexpected_e",b"repeated_packed_unexpected_e"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"o",b"o"]) -> typing_extensions___Literal["oneof_e_1","oneof_e_2"]: ...
type___MyMessagePlusExtra = MyMessagePlusExtra
