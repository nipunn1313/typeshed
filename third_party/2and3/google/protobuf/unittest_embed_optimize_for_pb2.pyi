# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.unittest_optimize_for_pb2 import (
    TestOptimizedForSize as google___protobuf___unittest_optimize_for_pb2___TestOptimizedForSize,
)

from typing import (
    Iterable as typing___Iterable,
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

class TestEmbedOptimizedForSize(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def optional_message(self) -> google___protobuf___unittest_optimize_for_pb2___TestOptimizedForSize: ...

    @property
    def repeated_message(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___unittest_optimize_for_pb2___TestOptimizedForSize]: ...

    def __init__(self,
        *,
        optional_message : typing___Optional[google___protobuf___unittest_optimize_for_pb2___TestOptimizedForSize] = None,
        repeated_message : typing___Optional[typing___Iterable[google___protobuf___unittest_optimize_for_pb2___TestOptimizedForSize]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"optional_message",b"optional_message"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"optional_message",b"optional_message",u"repeated_message",b"repeated_message"]) -> None: ...
type___TestEmbedOptimizedForSize = TestEmbedOptimizedForSize
