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
    jsii_type="aws-cdk-lib.interfaces.aws_rum.AppMonitorReference",
    jsii_struct_bases=[],
    name_mapping={"app_monitor_name": "appMonitorName"},
)
class AppMonitorReference:
    def __init__(self, *, app_monitor_name: builtins.str) -> None:
        '''A reference to a AppMonitor resource.

        :param app_monitor_name: The Name of the AppMonitor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rum as interfaces_rum
            
            app_monitor_reference = interfaces_rum.AppMonitorReference(
                app_monitor_name="appMonitorName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c7f81b289ca8180436c458b4c11d3fbea4385e54821e2ec6fe90be718eddaad8)
            check_type(argname="argument app_monitor_name", value=app_monitor_name, expected_type=type_hints["app_monitor_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_monitor_name": app_monitor_name,
        }

    @builtins.property
    def app_monitor_name(self) -> builtins.str:
        '''The Name of the AppMonitor resource.'''
        result = self._values.get("app_monitor_name")
        assert result is not None, "Required property 'app_monitor_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppMonitorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rum.IAppMonitorRef")
class IAppMonitorRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AppMonitor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appMonitorRef")
    def app_monitor_ref(self) -> "AppMonitorReference":
        '''(experimental) A reference to a AppMonitor resource.

        :stability: experimental
        '''
        ...


class _IAppMonitorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AppMonitor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rum.IAppMonitorRef"

    @builtins.property
    @jsii.member(jsii_name="appMonitorRef")
    def app_monitor_ref(self) -> "AppMonitorReference":
        '''(experimental) A reference to a AppMonitor resource.

        :stability: experimental
        '''
        return typing.cast("AppMonitorReference", jsii.get(self, "appMonitorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppMonitorRef).__jsii_proxy_class__ = lambda : _IAppMonitorRefProxy


__all__ = [
    "AppMonitorReference",
    "IAppMonitorRef",
]

publication.publish()

def _typecheckingstub__c7f81b289ca8180436c458b4c11d3fbea4385e54821e2ec6fe90be718eddaad8(
    *,
    app_monitor_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAppMonitorRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
