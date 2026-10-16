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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsecuretunneling.ITunnelRef")
class ITunnelRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Tunnel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tunnelRef")
    def tunnel_ref(self) -> "TunnelReference":
        '''(experimental) A reference to a Tunnel resource.

        :stability: experimental
        '''
        ...


class _ITunnelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Tunnel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsecuretunneling.ITunnelRef"

    @builtins.property
    @jsii.member(jsii_name="tunnelRef")
    def tunnel_ref(self) -> "TunnelReference":
        '''(experimental) A reference to a Tunnel resource.

        :stability: experimental
        '''
        return typing.cast("TunnelReference", jsii.get(self, "tunnelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITunnelRef).__jsii_proxy_class__ = lambda : _ITunnelRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotsecuretunneling.TunnelReference",
    jsii_struct_bases=[],
    name_mapping={"tunnel_arn": "tunnelArn"},
)
class TunnelReference:
    def __init__(self, *, tunnel_arn: builtins.str) -> None:
        '''A reference to a Tunnel resource.

        :param tunnel_arn: The TunnelArn of the Tunnel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsecuretunneling as interfaces_iotsecuretunneling
            
            tunnel_reference = interfaces_iotsecuretunneling.TunnelReference(
                tunnel_arn="tunnelArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d9ad18277deb807f22c84407a7ce089409cab368f915e4c16c0f9cd744ee8e10)
            check_type(argname="argument tunnel_arn", value=tunnel_arn, expected_type=type_hints["tunnel_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tunnel_arn": tunnel_arn,
        }

    @builtins.property
    def tunnel_arn(self) -> builtins.str:
        '''The TunnelArn of the Tunnel resource.'''
        result = self._values.get("tunnel_arn")
        assert result is not None, "Required property 'tunnel_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TunnelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ITunnelRef",
    "TunnelReference",
]

publication.publish()

def _typecheckingstub__d9ad18277deb807f22c84407a7ce089409cab368f915e4c16c0f9cd744ee8e10(
    *,
    tunnel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ITunnelRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
