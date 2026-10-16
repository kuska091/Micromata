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
    jsii_type="aws-cdk-lib.interfaces.aws_mgn.ConnectorReference",
    jsii_struct_bases=[],
    name_mapping={"connector_arn": "connectorArn"},
)
class ConnectorReference:
    def __init__(self, *, connector_arn: builtins.str) -> None:
        '''A reference to a Connector resource.

        :param connector_arn: The Arn of the Connector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mgn as interfaces_mgn
            
            connector_reference = interfaces_mgn.ConnectorReference(
                connector_arn="connectorArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__473ef89909abcba7dfb3bc946d38f201fafd6bff9e343478d713690f6d871c3a)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The Arn of the Connector resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mgn.IConnectorRef")
class IConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        ...


class _IConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mgn.IConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorReference", jsii.get(self, "connectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorRef).__jsii_proxy_class__ = lambda : _IConnectorRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mgn.ILaunchConfigurationTemplateRef"
)
class ILaunchConfigurationTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchConfigurationTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchConfigurationTemplateRef")
    def launch_configuration_template_ref(
        self,
    ) -> "LaunchConfigurationTemplateReference":
        '''(experimental) A reference to a LaunchConfigurationTemplate resource.

        :stability: experimental
        '''
        ...


class _ILaunchConfigurationTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchConfigurationTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mgn.ILaunchConfigurationTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="launchConfigurationTemplateRef")
    def launch_configuration_template_ref(
        self,
    ) -> "LaunchConfigurationTemplateReference":
        '''(experimental) A reference to a LaunchConfigurationTemplate resource.

        :stability: experimental
        '''
        return typing.cast("LaunchConfigurationTemplateReference", jsii.get(self, "launchConfigurationTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILaunchConfigurationTemplateRef).__jsii_proxy_class__ = lambda : _ILaunchConfigurationTemplateRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mgn.INetworkMigrationDefinitionRef"
)
class INetworkMigrationDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkMigrationDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkMigrationDefinitionRef")
    def network_migration_definition_ref(self) -> "NetworkMigrationDefinitionReference":
        '''(experimental) A reference to a NetworkMigrationDefinition resource.

        :stability: experimental
        '''
        ...


class _INetworkMigrationDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkMigrationDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mgn.INetworkMigrationDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="networkMigrationDefinitionRef")
    def network_migration_definition_ref(self) -> "NetworkMigrationDefinitionReference":
        '''(experimental) A reference to a NetworkMigrationDefinition resource.

        :stability: experimental
        '''
        return typing.cast("NetworkMigrationDefinitionReference", jsii.get(self, "networkMigrationDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkMigrationDefinitionRef).__jsii_proxy_class__ = lambda : _INetworkMigrationDefinitionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mgn.LaunchConfigurationTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "launch_configuration_template_arn": "launchConfigurationTemplateArn",
    },
)
class LaunchConfigurationTemplateReference:
    def __init__(self, *, launch_configuration_template_arn: builtins.str) -> None:
        '''A reference to a LaunchConfigurationTemplate resource.

        :param launch_configuration_template_arn: The Arn of the LaunchConfigurationTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mgn as interfaces_mgn
            
            launch_configuration_template_reference = interfaces_mgn.LaunchConfigurationTemplateReference(
                launch_configuration_template_arn="launchConfigurationTemplateArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d8193c0ab8601ec2d351fcac429e131de1d8d2859cc6a341e1edf201036b5e12)
            check_type(argname="argument launch_configuration_template_arn", value=launch_configuration_template_arn, expected_type=type_hints["launch_configuration_template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_configuration_template_arn": launch_configuration_template_arn,
        }

    @builtins.property
    def launch_configuration_template_arn(self) -> builtins.str:
        '''The Arn of the LaunchConfigurationTemplate resource.'''
        result = self._values.get("launch_configuration_template_arn")
        assert result is not None, "Required property 'launch_configuration_template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchConfigurationTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mgn.NetworkMigrationDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"network_migration_definition_arn": "networkMigrationDefinitionArn"},
)
class NetworkMigrationDefinitionReference:
    def __init__(self, *, network_migration_definition_arn: builtins.str) -> None:
        '''A reference to a NetworkMigrationDefinition resource.

        :param network_migration_definition_arn: The Arn of the NetworkMigrationDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mgn as interfaces_mgn
            
            network_migration_definition_reference = interfaces_mgn.NetworkMigrationDefinitionReference(
                network_migration_definition_arn="networkMigrationDefinitionArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__59e2537a75d064c98d466c307a81aefe9272b9c2a9920f50a99ae1df911a2cb9)
            check_type(argname="argument network_migration_definition_arn", value=network_migration_definition_arn, expected_type=type_hints["network_migration_definition_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_migration_definition_arn": network_migration_definition_arn,
        }

    @builtins.property
    def network_migration_definition_arn(self) -> builtins.str:
        '''The Arn of the NetworkMigrationDefinition resource.'''
        result = self._values.get("network_migration_definition_arn")
        assert result is not None, "Required property 'network_migration_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkMigrationDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectorReference",
    "IConnectorRef",
    "ILaunchConfigurationTemplateRef",
    "INetworkMigrationDefinitionRef",
    "LaunchConfigurationTemplateReference",
    "NetworkMigrationDefinitionReference",
]

publication.publish()

def _typecheckingstub__473ef89909abcba7dfb3bc946d38f201fafd6bff9e343478d713690f6d871c3a(
    *,
    connector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8193c0ab8601ec2d351fcac429e131de1d8d2859cc6a341e1edf201036b5e12(
    *,
    launch_configuration_template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e2537a75d064c98d466c307a81aefe9272b9c2a9920f50a99ae1df911a2cb9(
    *,
    network_migration_definition_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectorRef, ILaunchConfigurationTemplateRef, INetworkMigrationDefinitionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
