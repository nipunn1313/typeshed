# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
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

ImportEnumValue = typing___NewType('ImportEnumValue', builtin___int)
type___ImportEnumValue = ImportEnumValue
ImportEnum: _ImportEnum
class _ImportEnum(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ImportEnumValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    IMPORT_FOO = typing___cast(ImportEnumValue, 7)
    IMPORT_BAR = typing___cast(ImportEnumValue, 8)
    IMPORT_BAZ = typing___cast(ImportEnumValue, 9)
IMPORT_FOO = typing___cast(ImportEnumValue, 7)
IMPORT_BAR = typing___cast(ImportEnumValue, 8)
IMPORT_BAZ = typing___cast(ImportEnumValue, 9)
type___ImportEnum = ImportEnum

ImportEnumForMapValue = typing___NewType('ImportEnumForMapValue', builtin___int)
type___ImportEnumForMapValue = ImportEnumForMapValue
ImportEnumForMap: _ImportEnumForMap
class _ImportEnumForMap(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ImportEnumForMapValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    UNKNOWN = typing___cast(ImportEnumForMapValue, 0)
    FOO = typing___cast(ImportEnumForMapValue, 1)
    BAR = typing___cast(ImportEnumForMapValue, 2)
UNKNOWN = typing___cast(ImportEnumForMapValue, 0)
FOO = typing___cast(ImportEnumForMapValue, 1)
BAR = typing___cast(ImportEnumForMapValue, 2)
type___ImportEnumForMap = ImportEnumForMap

class ImportMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    d: builtin___int = ...

    def __init__(self,
        *,
        d : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"d",b"d"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"d",b"d"]) -> None: ...
type___ImportMessage = ImportMessage
