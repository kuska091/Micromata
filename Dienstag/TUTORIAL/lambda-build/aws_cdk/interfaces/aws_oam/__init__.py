from __future__ import annotations

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from jsii._type_checking import cached_type_hints, check_type


from ..._jsii import *

class _LazyImport:
    def __init__(self, module_name: str) -> None:
        self._module_name = module_name
        self._module: typing.Any = None
    def __getattr__(self, name: str) -> typing.Any:
        if self._module is None:
            import importlib
            self._module = importlib.import_module(self._module_name)
        return getattr(self._module, name)

if typing.TYPE_CHECKING:

    import aws_cdk.interfaces as _interfaces_8ca7e747
    import constructs as _constructs_77d1e7e8
else:

    _constructs_77d1e7e8 = _LazyImport("constructs")
    _interfaces_8ca7e747 = _LazyImport("aws_cdk.interfaces")


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_oam.ILinkRef")
class ILinkRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Link.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="linkRef")
    def link_ref(self) -> "LinkReference":
        '''(experimental) A reference to a Link resource.

        :stability: experimental
        '''
        ...


class _ILinkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Link.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_oam.ILinkRef"

    @builtins.property
    @jsii.member(jsii_name="linkRef")
    def link_ref(self) -> "LinkReference":
        '''(experimental) A reference to a Link resource.

        :stability: experimental
        '''
        return typing.cast("LinkReference", jsii.get(self, "linkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILinkRef).__jsii_proxy_class__ = lambda : _ILinkRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_oam.ISinkRef")
class ISinkRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Sink.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sinkRef")
    def sink_ref(self) -> "SinkReference":
        '''(experimental) A reference to a Sink resource.

        :stability: experimental
        '''
        ...


class _ISinkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Sink.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_oam.ISinkRef"

    @builtins.property
    @jsii.member(jsii_name="sinkRef")
    def sink_ref(self) -> "SinkReference":
        '''(experimental) A reference to a Sink resource.

        :stability: experimental
        '''
        return typing.cast("SinkReference", jsii.get(self, "sinkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISinkRef).__jsii_proxy_class__ = lambda : _ISinkRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_oam.LinkReference",
    jsii_struct_bases=[],
    name_mapping={"link_arn": "linkArn"},
)
class LinkReference:
    def __init__(self, *, link_arn: builtins.str) -> None:
        '''A reference to a Link resource.

        :param link_arn: The Arn of the Link resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_oam as interfaces_oam
            
            link_reference = interfaces_oam.LinkReference(
                link_arn="linkArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__451e971dd16b398f25ba453f515a2d334483c2e1def719cc662f17881d810f45)
            check_type(argname="argument link_arn", value=link_arn, expected_type=type_hints["link_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "link_arn": link_arn,
        }

    @builtins.property
    def link_arn(self) -> builtins.str:
        '''The Arn of the Link resource.'''
        result = self._values.get("link_arn")
        assert result is not None, "Required property 'link_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_oam.SinkReference",
    jsii_struct_bases=[],
    name_mapping={"sink_arn": "sinkArn"},
)
class SinkReference:
    def __init__(self, *, sink_arn: builtins.str) -> None:
        '''A reference to a Sink resource.

        :param sink_arn: The Arn of the Sink resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_oam as interfaces_oam
            
            sink_reference = interfaces_oam.SinkReference(
                sink_arn="sinkArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ffd6d3b9466ddafe0064dc558ca102b98e6d4c5de0b747d1c6f5009eb2c7f81f)
            check_type(argname="argument sink_arn", value=sink_arn, expected_type=type_hints["sink_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sink_arn": sink_arn,
        }

    @builtins.property
    def sink_arn(self) -> builtins.str:
        '''The Arn of the Sink resource.'''
        result = self._values.get("sink_arn")
        assert result is not None, "Required property 'sink_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SinkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ILinkRef",
    "ISinkRef",
    "LinkReference",
    "SinkReference",
]

publication.publish()

def _typecheckingstub__451e971dd16b398f25ba453f515a2d334483c2e1def719cc662f17881d810f45(
    *,
    link_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffd6d3b9466ddafe0064dc558ca102b98e6d4c5de0b747d1c6f5009eb2c7f81f(
    *,
    sink_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ILinkRef, ISinkRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
