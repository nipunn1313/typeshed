# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TestMessageSet(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___TestMessageSet = TestMessageSet

class TestMessageSetWireFormatContainer(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def message_set(self) -> type___TestMessageSet: ...

    def __init__(self,
        *,
        message_set : typing___Optional[type___TestMessageSet] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"message_set",b"message_set"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"message_set",b"message_set"]) -> None: ...
type___TestMessageSetWireFormatContainer = TestMessageSetWireFormatContainer
