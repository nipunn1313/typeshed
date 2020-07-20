# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.any_pb2 import (
    Any as google___protobuf___any_pb2___Any,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TestField(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    a: builtin___int = ...
    b: builtin___int = ...
    c: builtin___int = ...
    rc: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...

    @property
    def m(self) -> type___TestField: ...

    def __init__(self,
        *,
        a : typing___Optional[builtin___int] = None,
        b : typing___Optional[builtin___int] = None,
        c : typing___Optional[builtin___int] = None,
        rc : typing___Optional[typing___Iterable[builtin___int]] = None,
        m : typing___Optional[type___TestField] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"a",b"a",u"b",b"b",u"c",b"c",u"m",b"m"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"a",b"a",u"b",b"b",u"c",b"c",u"m",b"m",u"rc",b"rc"]) -> None: ...
type___TestField = TestField

class TestDiffMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Item(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        a: builtin___int = ...
        b: typing___Text = ...
        ra: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
        rb: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

        @property
        def m(self) -> type___TestField: ...

        @property
        def rm(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TestField]: ...

        def __init__(self,
            *,
            a : typing___Optional[builtin___int] = None,
            b : typing___Optional[typing___Text] = None,
            ra : typing___Optional[typing___Iterable[builtin___int]] = None,
            rb : typing___Optional[typing___Iterable[typing___Text]] = None,
            m : typing___Optional[type___TestField] = None,
            rm : typing___Optional[typing___Iterable[type___TestField]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"a",b"a",u"b",b"b",u"m",b"m"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"a",b"a",u"b",b"b",u"m",b"m",u"ra",b"ra",u"rb",b"rb",u"rm",b"rm"]) -> None: ...
    type___Item = Item

    v: builtin___int = ...
    w: typing___Text = ...
    rv: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    rw: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    @property
    def item(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TestDiffMessage.Item]: ...

    @property
    def m(self) -> type___TestField: ...

    @property
    def rm(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TestField]: ...

    @property
    def rany(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___any_pb2___Any]: ...

    def __init__(self,
        *,
        item : typing___Optional[typing___Iterable[type___TestDiffMessage.Item]] = None,
        v : typing___Optional[builtin___int] = None,
        w : typing___Optional[typing___Text] = None,
        m : typing___Optional[type___TestField] = None,
        rv : typing___Optional[typing___Iterable[builtin___int]] = None,
        rw : typing___Optional[typing___Iterable[typing___Text]] = None,
        rm : typing___Optional[typing___Iterable[type___TestField]] = None,
        rany : typing___Optional[typing___Iterable[google___protobuf___any_pb2___Any]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"m",b"m",u"v",b"v",u"w",b"w"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"item",b"item",u"m",b"m",u"rany",b"rany",u"rm",b"rm",u"rv",b"rv",u"rw",b"rw",u"v",b"v",u"w",b"w"]) -> None: ...
type___TestDiffMessage = TestDiffMessage
