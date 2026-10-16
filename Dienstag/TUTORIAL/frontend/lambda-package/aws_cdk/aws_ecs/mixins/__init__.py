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

    import aws_cdk as _aws_cdk_0cae9daa
    import aws_cdk.aws_ecs as _aws_ecs_19c7ccd1
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_ecs_19c7ccd1 = _LazyImport("aws_cdk.aws_ecs")
    _constructs_77d1e7e8 = _LazyImport("constructs")


class ClusterSettings(
    _aws_cdk_0cae9daa.Mixin,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecs.mixins.ClusterSettings",
):
    '''Applies one or more cluster settings to an ECS cluster.

    If a setting with the same name already exists, its value is replaced.

    :exampleMetadata: infused

    Example::

        ecs.CfnCluster(self, "Cluster").with(ecs.mixins.ClusterSettings([name="containerInsights", value="enhanced"]))
    '''

    def __init__(
        self,
        settings: typing.Sequence[typing.Union["_aws_ecs_19c7ccd1.CfnCluster.ClusterSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param settings: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__330f6d3486223a52f5a9301c591ff3cfe4883f1d51f8ce905443a08bb36647d5)
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        jsii.create(self.__class__, self, [settings])

    @jsii.member(jsii_name="applyTo")
    def apply_to(self, cluster: "_constructs_77d1e7e8.IConstruct") -> None:
        '''Applies the mixin functionality to the target construct.

        :param cluster: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__eb87ac656b0fc6c6c1f39c76c38e76a9578388765834a1eb500892a5ea99995d)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        return typing.cast(None, jsii.invoke(self, "applyTo", [cluster]))

    @jsii.member(jsii_name="supports")
    def supports(self, construct: "_constructs_77d1e7e8.IConstruct") -> builtins.bool:
        '''Determines whether this mixin can be applied to the given construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__248294cdc37e84b78b4b04f9c8084680fbe83e1bb5e8432efc1cc19b1d8e9d29)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "supports", [construct]))


__all__ = [
    "ClusterSettings",
]

publication.publish()

def _typecheckingstub__330f6d3486223a52f5a9301c591ff3cfe4883f1d51f8ce905443a08bb36647d5(
    settings: typing.Sequence[typing.Union[_aws_ecs_19c7ccd1.CfnCluster.ClusterSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb87ac656b0fc6c6c1f39c76c38e76a9578388765834a1eb500892a5ea99995d(
    cluster: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__248294cdc37e84b78b4b04f9c8084680fbe83e1bb5e8432efc1cc19b1d8e9d29(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass
