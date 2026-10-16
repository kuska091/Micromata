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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkflowmonitor.IMonitorRef")
class IMonitorRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Monitor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="monitorRef")
    def monitor_ref(self) -> "MonitorReference":
        '''(experimental) A reference to a Monitor resource.

        :stability: experimental
        '''
        ...


class _IMonitorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Monitor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkflowmonitor.IMonitorRef"

    @builtins.property
    @jsii.member(jsii_name="monitorRef")
    def monitor_ref(self) -> "MonitorReference":
        '''(experimental) A reference to a Monitor resource.

        :stability: experimental
        '''
        return typing.cast("MonitorReference", jsii.get(self, "monitorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMonitorRef).__jsii_proxy_class__ = lambda : _IMonitorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkflowmonitor.IScopeRef")
class IScopeRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Scope.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scopeRef")
    def scope_ref(self) -> "ScopeReference":
        '''(experimental) A reference to a Scope resource.

        :stability: experimental
        '''
        ...


class _IScopeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Scope.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkflowmonitor.IScopeRef"

    @builtins.property
    @jsii.member(jsii_name="scopeRef")
    def scope_ref(self) -> "ScopeReference":
        '''(experimental) A reference to a Scope resource.

        :stability: experimental
        '''
        return typing.cast("ScopeReference", jsii.get(self, "scopeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScopeRef).__jsii_proxy_class__ = lambda : _IScopeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkflowmonitor.MonitorReference",
    jsii_struct_bases=[],
    name_mapping={"monitor_arn": "monitorArn"},
)
class MonitorReference:
    def __init__(self, *, monitor_arn: builtins.str) -> None:
        '''A reference to a Monitor resource.

        :param monitor_arn: The Arn of the Monitor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkflowmonitor as interfaces_networkflowmonitor
            
            monitor_reference = interfaces_networkflowmonitor.MonitorReference(
                monitor_arn="monitorArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bcb231cbb8ab3f5669321265603497bf17a1c1db515387055b28647594ef67a0)
            check_type(argname="argument monitor_arn", value=monitor_arn, expected_type=type_hints["monitor_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitor_arn": monitor_arn,
        }

    @builtins.property
    def monitor_arn(self) -> builtins.str:
        '''The Arn of the Monitor resource.'''
        result = self._values.get("monitor_arn")
        assert result is not None, "Required property 'monitor_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkflowmonitor.ScopeReference",
    jsii_struct_bases=[],
    name_mapping={"scope_arn": "scopeArn"},
)
class ScopeReference:
    def __init__(self, *, scope_arn: builtins.str) -> None:
        '''A reference to a Scope resource.

        :param scope_arn: The ScopeArn of the Scope resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkflowmonitor as interfaces_networkflowmonitor
            
            scope_reference = interfaces_networkflowmonitor.ScopeReference(
                scope_arn="scopeArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9c8782c40d1bcacc31000a4e8357207afdf1629f7d1e379147c5a190c7a7c06e)
            check_type(argname="argument scope_arn", value=scope_arn, expected_type=type_hints["scope_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scope_arn": scope_arn,
        }

    @builtins.property
    def scope_arn(self) -> builtins.str:
        '''The ScopeArn of the Scope resource.'''
        result = self._values.get("scope_arn")
        assert result is not None, "Required property 'scope_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScopeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IMonitorRef",
    "IScopeRef",
    "MonitorReference",
    "ScopeReference",
]

publication.publish()

def _typecheckingstub__bcb231cbb8ab3f5669321265603497bf17a1c1db515387055b28647594ef67a0(
    *,
    monitor_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8782c40d1bcacc31000a4e8357207afdf1629f7d1e379147c5a190c7a7c06e(
    *,
    scope_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IMonitorRef, IScopeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
