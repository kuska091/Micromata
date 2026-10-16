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


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codeconnections.ConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"connection_arn": "connectionArn"},
)
class ConnectionReference:
    def __init__(self, *, connection_arn: builtins.str) -> None:
        '''A reference to a Connection resource.

        :param connection_arn: The ConnectionArn of the Connection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codeconnections as interfaces_codeconnections
            
            connection_reference = interfaces_codeconnections.ConnectionReference(
                connection_arn="connectionArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__32e0a1f51a1af2deb607f1a2c1b7b7ea71617b002e04bbe9b16a3f34414d70ed)
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_arn": connection_arn,
        }

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The ConnectionArn of the Connection resource.'''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codeconnections.HostReference",
    jsii_struct_bases=[],
    name_mapping={"host_arn": "hostArn"},
)
class HostReference:
    def __init__(self, *, host_arn: builtins.str) -> None:
        '''A reference to a Host resource.

        :param host_arn: The HostArn of the Host resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codeconnections as interfaces_codeconnections
            
            host_reference = interfaces_codeconnections.HostReference(
                host_arn="hostArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0661c0c05abbfc479561ceeb2ccffd2df84ce58d5d0c9719897d559f51df5305)
            check_type(argname="argument host_arn", value=host_arn, expected_type=type_hints["host_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host_arn": host_arn,
        }

    @builtins.property
    def host_arn(self) -> builtins.str:
        '''The HostArn of the Host resource.'''
        result = self._values.get("host_arn")
        assert result is not None, "Required property 'host_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codeconnections.IConnectionRef")
class IConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        ...


class _IConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codeconnections.IConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionReference", jsii.get(self, "connectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionRef).__jsii_proxy_class__ = lambda : _IConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codeconnections.IHostRef")
class IHostRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Host.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hostRef")
    def host_ref(self) -> "HostReference":
        '''(experimental) A reference to a Host resource.

        :stability: experimental
        '''
        ...


class _IHostRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Host.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codeconnections.IHostRef"

    @builtins.property
    @jsii.member(jsii_name="hostRef")
    def host_ref(self) -> "HostReference":
        '''(experimental) A reference to a Host resource.

        :stability: experimental
        '''
        return typing.cast("HostReference", jsii.get(self, "hostRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHostRef).__jsii_proxy_class__ = lambda : _IHostRefProxy


__all__ = [
    "ConnectionReference",
    "HostReference",
    "IConnectionRef",
    "IHostRef",
]

publication.publish()

def _typecheckingstub__32e0a1f51a1af2deb607f1a2c1b7b7ea71617b002e04bbe9b16a3f34414d70ed(
    *,
    connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0661c0c05abbfc479561ceeb2ccffd2df84ce58d5d0c9719897d559f51df5305(
    *,
    host_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectionRef, IHostRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
