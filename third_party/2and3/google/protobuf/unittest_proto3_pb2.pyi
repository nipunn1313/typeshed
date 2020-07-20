# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.unittest_import_pb2 import (
    ImportMessage as google___protobuf___unittest_import_pb2___ImportMessage,
)

from google.protobuf.unittest_import_public_pb2 import (
    PublicImportMessage as google___protobuf___unittest_import_public_pb2___PublicImportMessage,
)

from typing import (
    Iterable as typing___Iterable,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
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

ForeignEnumValue = typing___NewType('ForeignEnumValue', builtin___int)
type___ForeignEnumValue = ForeignEnumValue
ForeignEnum: _ForeignEnum
class _ForeignEnum(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ForeignEnumValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    FOREIGN_ZERO = typing___cast(ForeignEnumValue, 0)
    FOREIGN_FOO = typing___cast(ForeignEnumValue, 4)
    FOREIGN_BAR = typing___cast(ForeignEnumValue, 5)
    FOREIGN_BAZ = typing___cast(ForeignEnumValue, 6)
FOREIGN_ZERO = typing___cast(ForeignEnumValue, 0)
FOREIGN_FOO = typing___cast(ForeignEnumValue, 4)
FOREIGN_BAR = typing___cast(ForeignEnumValue, 5)
FOREIGN_BAZ = typing___cast(ForeignEnumValue, 6)
type___ForeignEnum = ForeignEnum

class TestAllTypes(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    NestedEnumValue = typing___NewType('NestedEnumValue', builtin___int)
    type___NestedEnumValue = NestedEnumValue
    NestedEnum: _NestedEnum
    class _NestedEnum(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[TestAllTypes.NestedEnumValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        ZERO = typing___cast(TestAllTypes.NestedEnumValue, 0)
        FOO = typing___cast(TestAllTypes.NestedEnumValue, 1)
        BAR = typing___cast(TestAllTypes.NestedEnumValue, 2)
        BAZ = typing___cast(TestAllTypes.NestedEnumValue, 3)
        NEG = typing___cast(TestAllTypes.NestedEnumValue, -1)
    ZERO = typing___cast(TestAllTypes.NestedEnumValue, 0)
    FOO = typing___cast(TestAllTypes.NestedEnumValue, 1)
    BAR = typing___cast(TestAllTypes.NestedEnumValue, 2)
    BAZ = typing___cast(TestAllTypes.NestedEnumValue, 3)
    NEG = typing___cast(TestAllTypes.NestedEnumValue, -1)
    type___NestedEnum = NestedEnum

    class NestedMessage(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        bb: builtin___int = ...

        def __init__(self,
            *,
            bb : typing___Optional[builtin___int] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"bb",b"bb"]) -> None: ...
    type___NestedMessage = NestedMessage

    optional_int32: builtin___int = ...
    optional_int64: builtin___int = ...
    optional_uint32: builtin___int = ...
    optional_uint64: builtin___int = ...
    optional_sint32: builtin___int = ...
    optional_sint64: builtin___int = ...
    optional_fixed32: builtin___int = ...
    optional_fixed64: builtin___int = ...
    optional_sfixed32: builtin___int = ...
    optional_sfixed64: builtin___int = ...
    optional_float: builtin___float = ...
    optional_double: builtin___float = ...
    optional_bool: builtin___bool = ...
    optional_string: typing___Text = ...
    optional_bytes: builtin___bytes = ...
    optional_nested_enum: type___TestAllTypes.NestedEnumValue = ...
    optional_foreign_enum: type___ForeignEnumValue = ...
    optional_string_piece: typing___Text = ...
    optional_cord: typing___Text = ...
    repeated_int32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_int64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_uint32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_uint64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_sint32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_sint64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_fixed32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_fixed64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_sfixed32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_sfixed64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_float: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    repeated_double: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    repeated_bool: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bool] = ...
    repeated_string: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    repeated_bytes: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes] = ...
    repeated_nested_enum: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___TestAllTypes.NestedEnumValue] = ...
    repeated_foreign_enum: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___ForeignEnumValue] = ...
    repeated_string_piece: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    repeated_cord: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    oneof_uint32: builtin___int = ...
    oneof_string: typing___Text = ...
    oneof_bytes: builtin___bytes = ...

    @property
    def optional_nested_message(self) -> type___TestAllTypes.NestedMessage: ...

    @property
    def optional_foreign_message(self) -> type___ForeignMessage: ...

    @property
    def optional_import_message(self) -> google___protobuf___unittest_import_pb2___ImportMessage: ...

    @property
    def optional_public_import_message(self) -> google___protobuf___unittest_import_public_pb2___PublicImportMessage: ...

    @property
    def optional_lazy_message(self) -> type___TestAllTypes.NestedMessage: ...

    @property
    def optional_lazy_import_message(self) -> google___protobuf___unittest_import_pb2___ImportMessage: ...

    @property
    def repeated_nested_message(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TestAllTypes.NestedMessage]: ...

    @property
    def repeated_foreign_message(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ForeignMessage]: ...

    @property
    def repeated_import_message(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___unittest_import_pb2___ImportMessage]: ...

    @property
    def repeated_lazy_message(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TestAllTypes.NestedMessage]: ...

    @property
    def oneof_nested_message(self) -> type___TestAllTypes.NestedMessage: ...

    def __init__(self,
        *,
        optional_int32 : typing___Optional[builtin___int] = None,
        optional_int64 : typing___Optional[builtin___int] = None,
        optional_uint32 : typing___Optional[builtin___int] = None,
        optional_uint64 : typing___Optional[builtin___int] = None,
        optional_sint32 : typing___Optional[builtin___int] = None,
        optional_sint64 : typing___Optional[builtin___int] = None,
        optional_fixed32 : typing___Optional[builtin___int] = None,
        optional_fixed64 : typing___Optional[builtin___int] = None,
        optional_sfixed32 : typing___Optional[builtin___int] = None,
        optional_sfixed64 : typing___Optional[builtin___int] = None,
        optional_float : typing___Optional[builtin___float] = None,
        optional_double : typing___Optional[builtin___float] = None,
        optional_bool : typing___Optional[builtin___bool] = None,
        optional_string : typing___Optional[typing___Text] = None,
        optional_bytes : typing___Optional[builtin___bytes] = None,
        optional_nested_message : typing___Optional[type___TestAllTypes.NestedMessage] = None,
        optional_foreign_message : typing___Optional[type___ForeignMessage] = None,
        optional_import_message : typing___Optional[google___protobuf___unittest_import_pb2___ImportMessage] = None,
        optional_nested_enum : typing___Optional[type___TestAllTypes.NestedEnumValue] = None,
        optional_foreign_enum : typing___Optional[type___ForeignEnumValue] = None,
        optional_string_piece : typing___Optional[typing___Text] = None,
        optional_cord : typing___Optional[typing___Text] = None,
        optional_public_import_message : typing___Optional[google___protobuf___unittest_import_public_pb2___PublicImportMessage] = None,
        optional_lazy_message : typing___Optional[type___TestAllTypes.NestedMessage] = None,
        optional_lazy_import_message : typing___Optional[google___protobuf___unittest_import_pb2___ImportMessage] = None,
        repeated_int32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_int64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_uint32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_uint64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_sint32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_sint64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_fixed32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_fixed64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_sfixed32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_sfixed64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_float : typing___Optional[typing___Iterable[builtin___float]] = None,
        repeated_double : typing___Optional[typing___Iterable[builtin___float]] = None,
        repeated_bool : typing___Optional[typing___Iterable[builtin___bool]] = None,
        repeated_string : typing___Optional[typing___Iterable[typing___Text]] = None,
        repeated_bytes : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        repeated_nested_message : typing___Optional[typing___Iterable[type___TestAllTypes.NestedMessage]] = None,
        repeated_foreign_message : typing___Optional[typing___Iterable[type___ForeignMessage]] = None,
        repeated_import_message : typing___Optional[typing___Iterable[google___protobuf___unittest_import_pb2___ImportMessage]] = None,
        repeated_nested_enum : typing___Optional[typing___Iterable[type___TestAllTypes.NestedEnumValue]] = None,
        repeated_foreign_enum : typing___Optional[typing___Iterable[type___ForeignEnumValue]] = None,
        repeated_string_piece : typing___Optional[typing___Iterable[typing___Text]] = None,
        repeated_cord : typing___Optional[typing___Iterable[typing___Text]] = None,
        repeated_lazy_message : typing___Optional[typing___Iterable[type___TestAllTypes.NestedMessage]] = None,
        oneof_uint32 : typing___Optional[builtin___int] = None,
        oneof_nested_message : typing___Optional[type___TestAllTypes.NestedMessage] = None,
        oneof_string : typing___Optional[typing___Text] = None,
        oneof_bytes : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"oneof_bytes",b"oneof_bytes",u"oneof_field",b"oneof_field",u"oneof_nested_message",b"oneof_nested_message",u"oneof_string",b"oneof_string",u"oneof_uint32",b"oneof_uint32",u"optional_foreign_message",b"optional_foreign_message",u"optional_import_message",b"optional_import_message",u"optional_lazy_import_message",b"optional_lazy_import_message",u"optional_lazy_message",b"optional_lazy_message",u"optional_nested_message",b"optional_nested_message",u"optional_public_import_message",b"optional_public_import_message"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"oneof_bytes",b"oneof_bytes",u"oneof_field",b"oneof_field",u"oneof_nested_message",b"oneof_nested_message",u"oneof_string",b"oneof_string",u"oneof_uint32",b"oneof_uint32",u"optional_bool",b"optional_bool",u"optional_bytes",b"optional_bytes",u"optional_cord",b"optional_cord",u"optional_double",b"optional_double",u"optional_fixed32",b"optional_fixed32",u"optional_fixed64",b"optional_fixed64",u"optional_float",b"optional_float",u"optional_foreign_enum",b"optional_foreign_enum",u"optional_foreign_message",b"optional_foreign_message",u"optional_import_message",b"optional_import_message",u"optional_int32",b"optional_int32",u"optional_int64",b"optional_int64",u"optional_lazy_import_message",b"optional_lazy_import_message",u"optional_lazy_message",b"optional_lazy_message",u"optional_nested_enum",b"optional_nested_enum",u"optional_nested_message",b"optional_nested_message",u"optional_public_import_message",b"optional_public_import_message",u"optional_sfixed32",b"optional_sfixed32",u"optional_sfixed64",b"optional_sfixed64",u"optional_sint32",b"optional_sint32",u"optional_sint64",b"optional_sint64",u"optional_string",b"optional_string",u"optional_string_piece",b"optional_string_piece",u"optional_uint32",b"optional_uint32",u"optional_uint64",b"optional_uint64",u"repeated_bool",b"repeated_bool",u"repeated_bytes",b"repeated_bytes",u"repeated_cord",b"repeated_cord",u"repeated_double",b"repeated_double",u"repeated_fixed32",b"repeated_fixed32",u"repeated_fixed64",b"repeated_fixed64",u"repeated_float",b"repeated_float",u"repeated_foreign_enum",b"repeated_foreign_enum",u"repeated_foreign_message",b"repeated_foreign_message",u"repeated_import_message",b"repeated_import_message",u"repeated_int32",b"repeated_int32",u"repeated_int64",b"repeated_int64",u"repeated_lazy_message",b"repeated_lazy_message",u"repeated_nested_enum",b"repeated_nested_enum",u"repeated_nested_message",b"repeated_nested_message",u"repeated_sfixed32",b"repeated_sfixed32",u"repeated_sfixed64",b"repeated_sfixed64",u"repeated_sint32",b"repeated_sint32",u"repeated_sint64",b"repeated_sint64",u"repeated_string",b"repeated_string",u"repeated_string_piece",b"repeated_string_piece",u"repeated_uint32",b"repeated_uint32",u"repeated_uint64",b"repeated_uint64"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"oneof_field",b"oneof_field"]) -> typing_extensions___Literal["oneof_uint32","oneof_nested_message","oneof_string","oneof_bytes"]: ...
type___TestAllTypes = TestAllTypes

class TestPackedTypes(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    packed_int32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_int64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_uint32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_uint64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_sint32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_sint64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_fixed32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_fixed64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_sfixed32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_sfixed64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    packed_float: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    packed_double: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    packed_bool: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bool] = ...
    packed_enum: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___ForeignEnumValue] = ...

    def __init__(self,
        *,
        packed_int32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_int64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_uint32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_uint64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_sint32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_sint64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_fixed32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_fixed64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_sfixed32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_sfixed64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        packed_float : typing___Optional[typing___Iterable[builtin___float]] = None,
        packed_double : typing___Optional[typing___Iterable[builtin___float]] = None,
        packed_bool : typing___Optional[typing___Iterable[builtin___bool]] = None,
        packed_enum : typing___Optional[typing___Iterable[type___ForeignEnumValue]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"packed_bool",b"packed_bool",u"packed_double",b"packed_double",u"packed_enum",b"packed_enum",u"packed_fixed32",b"packed_fixed32",u"packed_fixed64",b"packed_fixed64",u"packed_float",b"packed_float",u"packed_int32",b"packed_int32",u"packed_int64",b"packed_int64",u"packed_sfixed32",b"packed_sfixed32",u"packed_sfixed64",b"packed_sfixed64",u"packed_sint32",b"packed_sint32",u"packed_sint64",b"packed_sint64",u"packed_uint32",b"packed_uint32",u"packed_uint64",b"packed_uint64"]) -> None: ...
type___TestPackedTypes = TestPackedTypes

class TestUnpackedTypes(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    repeated_int32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_int64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_uint32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_uint64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_sint32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_sint64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_fixed32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_fixed64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_sfixed32: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_sfixed64: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    repeated_float: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    repeated_double: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float] = ...
    repeated_bool: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bool] = ...
    repeated_nested_enum: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___TestAllTypes.NestedEnumValue] = ...

    def __init__(self,
        *,
        repeated_int32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_int64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_uint32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_uint64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_sint32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_sint64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_fixed32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_fixed64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_sfixed32 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_sfixed64 : typing___Optional[typing___Iterable[builtin___int]] = None,
        repeated_float : typing___Optional[typing___Iterable[builtin___float]] = None,
        repeated_double : typing___Optional[typing___Iterable[builtin___float]] = None,
        repeated_bool : typing___Optional[typing___Iterable[builtin___bool]] = None,
        repeated_nested_enum : typing___Optional[typing___Iterable[type___TestAllTypes.NestedEnumValue]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"repeated_bool",b"repeated_bool",u"repeated_double",b"repeated_double",u"repeated_fixed32",b"repeated_fixed32",u"repeated_fixed64",b"repeated_fixed64",u"repeated_float",b"repeated_float",u"repeated_int32",b"repeated_int32",u"repeated_int64",b"repeated_int64",u"repeated_nested_enum",b"repeated_nested_enum",u"repeated_sfixed32",b"repeated_sfixed32",u"repeated_sfixed64",b"repeated_sfixed64",u"repeated_sint32",b"repeated_sint32",u"repeated_sint64",b"repeated_sint64",u"repeated_uint32",b"repeated_uint32",u"repeated_uint64",b"repeated_uint64"]) -> None: ...
type___TestUnpackedTypes = TestUnpackedTypes

class NestedTestAllTypes(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def child(self) -> type___NestedTestAllTypes: ...

    @property
    def payload(self) -> type___TestAllTypes: ...

    def __init__(self,
        *,
        child : typing___Optional[type___NestedTestAllTypes] = None,
        payload : typing___Optional[type___TestAllTypes] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"child",b"child",u"payload",b"payload"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"child",b"child",u"payload",b"payload"]) -> None: ...
type___NestedTestAllTypes = NestedTestAllTypes

class ForeignMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    c: builtin___int = ...

    def __init__(self,
        *,
        c : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"c",b"c"]) -> None: ...
type___ForeignMessage = ForeignMessage

class TestEmptyMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___TestEmptyMessage = TestEmptyMessage

class TestMessageWithDummy(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    dummy: builtin___bool = ...

    def __init__(self,
        *,
        dummy : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dummy",b"dummy"]) -> None: ...
type___TestMessageWithDummy = TestMessageWithDummy

class TestOneof2(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    NestedEnumValue = typing___NewType('NestedEnumValue', builtin___int)
    type___NestedEnumValue = NestedEnumValue
    NestedEnum: _NestedEnum
    class _NestedEnum(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[TestOneof2.NestedEnumValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNKNOWN = typing___cast(TestOneof2.NestedEnumValue, 0)
        FOO = typing___cast(TestOneof2.NestedEnumValue, 1)
        BAR = typing___cast(TestOneof2.NestedEnumValue, 2)
        BAZ = typing___cast(TestOneof2.NestedEnumValue, 3)
    UNKNOWN = typing___cast(TestOneof2.NestedEnumValue, 0)
    FOO = typing___cast(TestOneof2.NestedEnumValue, 1)
    BAR = typing___cast(TestOneof2.NestedEnumValue, 2)
    BAZ = typing___cast(TestOneof2.NestedEnumValue, 3)
    type___NestedEnum = NestedEnum

    foo_enum: type___TestOneof2.NestedEnumValue = ...

    def __init__(self,
        *,
        foo_enum : typing___Optional[type___TestOneof2.NestedEnumValue] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"foo",b"foo",u"foo_enum",b"foo_enum"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"foo",b"foo",u"foo_enum",b"foo_enum"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"foo",b"foo"]) -> typing_extensions___Literal["foo_enum"]: ...
type___TestOneof2 = TestOneof2
