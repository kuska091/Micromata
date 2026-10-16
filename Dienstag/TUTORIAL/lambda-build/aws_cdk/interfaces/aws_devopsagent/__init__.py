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
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.AgentSpaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "agent_space_arn": "agentSpaceArn",
        "agent_space_id": "agentSpaceId",
    },
)
class AgentSpaceReference:
    def __init__(
        self,
        *,
        agent_space_arn: builtins.str,
        agent_space_id: builtins.str,
    ) -> None:
        '''A reference to a AgentSpace resource.

        :param agent_space_arn: The ARN of the AgentSpace resource.
        :param agent_space_id: The AgentSpaceId of the AgentSpace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            agent_space_reference = interfaces_devopsagent.AgentSpaceReference(
                agent_space_arn="agentSpaceArn",
                agent_space_id="agentSpaceId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__243d248446cd635e4d580c7e821c36a9651420cfff39e507c6e56843c8dfb804)
            check_type(argname="argument agent_space_arn", value=agent_space_arn, expected_type=type_hints["agent_space_arn"])
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_arn": agent_space_arn,
            "agent_space_id": agent_space_id,
        }

    @builtins.property
    def agent_space_arn(self) -> builtins.str:
        '''The ARN of the AgentSpace resource.'''
        result = self._values.get("agent_space_arn")
        assert result is not None, "Required property 'agent_space_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the AgentSpace resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentSpaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.AssetReference",
    jsii_struct_bases=[],
    name_mapping={
        "agent_space_id": "agentSpaceId",
        "asset_arn": "assetArn",
        "asset_id": "assetId",
    },
)
class AssetReference:
    def __init__(
        self,
        *,
        agent_space_id: builtins.str,
        asset_arn: builtins.str,
        asset_id: builtins.str,
    ) -> None:
        '''A reference to a Asset resource.

        :param agent_space_id: The AgentSpaceId of the Asset resource.
        :param asset_arn: The ARN of the Asset resource.
        :param asset_id: The AssetId of the Asset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            asset_reference = interfaces_devopsagent.AssetReference(
                agent_space_id="agentSpaceId",
                asset_arn="assetArn",
                asset_id="assetId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5e07ae93fd4597600bcf048453225278461c377da1857624454c2c72c898a881)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
            check_type(argname="argument asset_arn", value=asset_arn, expected_type=type_hints["asset_arn"])
            check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
            "asset_arn": asset_arn,
            "asset_id": asset_id,
        }

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the Asset resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_arn(self) -> builtins.str:
        '''The ARN of the Asset resource.'''
        result = self._values.get("asset_arn")
        assert result is not None, "Required property 'asset_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_id(self) -> builtins.str:
        '''The AssetId of the Asset resource.'''
        result = self._values.get("asset_id")
        assert result is not None, "Required property 'asset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.AssociationReference",
    jsii_struct_bases=[],
    name_mapping={"agent_space_id": "agentSpaceId", "association_id": "associationId"},
)
class AssociationReference:
    def __init__(
        self,
        *,
        agent_space_id: builtins.str,
        association_id: builtins.str,
    ) -> None:
        '''A reference to a Association resource.

        :param agent_space_id: The AgentSpaceId of the Association resource.
        :param association_id: The AssociationId of the Association resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            association_reference = interfaces_devopsagent.AssociationReference(
                agent_space_id="agentSpaceId",
                association_id="associationId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__02318c63b2a10c35692903fce2e2a91bd6e6b83485fb019a8dd7f1e3e1a7d952)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
            "association_id": association_id,
        }

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the Association resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the Association resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.IAgentSpaceRef")
class IAgentSpaceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentSpace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "AgentSpaceReference":
        '''(experimental) A reference to a AgentSpace resource.

        :stability: experimental
        '''
        ...


class _IAgentSpaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentSpace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.IAgentSpaceRef"

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "AgentSpaceReference":
        '''(experimental) A reference to a AgentSpace resource.

        :stability: experimental
        '''
        return typing.cast("AgentSpaceReference", jsii.get(self, "agentSpaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentSpaceRef).__jsii_proxy_class__ = lambda : _IAgentSpaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.IAssetRef")
class IAssetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Asset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assetRef")
    def asset_ref(self) -> "AssetReference":
        '''(experimental) A reference to a Asset resource.

        :stability: experimental
        '''
        ...


class _IAssetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Asset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.IAssetRef"

    @builtins.property
    @jsii.member(jsii_name="assetRef")
    def asset_ref(self) -> "AssetReference":
        '''(experimental) A reference to a Asset resource.

        :stability: experimental
        '''
        return typing.cast("AssetReference", jsii.get(self, "assetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssetRef).__jsii_proxy_class__ = lambda : _IAssetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.IAssociationRef")
class IAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Association.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="associationRef")
    def association_ref(self) -> "AssociationReference":
        '''(experimental) A reference to a Association resource.

        :stability: experimental
        '''
        ...


class _IAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Association.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.IAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="associationRef")
    def association_ref(self) -> "AssociationReference":
        '''(experimental) A reference to a Association resource.

        :stability: experimental
        '''
        return typing.cast("AssociationReference", jsii.get(self, "associationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssociationRef).__jsii_proxy_class__ = lambda : _IAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.IPrivateConnectionRef"
)
class IPrivateConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PrivateConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="privateConnectionRef")
    def private_connection_ref(self) -> "PrivateConnectionReference":
        '''(experimental) A reference to a PrivateConnection resource.

        :stability: experimental
        '''
        ...


class _IPrivateConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PrivateConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.IPrivateConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="privateConnectionRef")
    def private_connection_ref(self) -> "PrivateConnectionReference":
        '''(experimental) A reference to a PrivateConnection resource.

        :stability: experimental
        '''
        return typing.cast("PrivateConnectionReference", jsii.get(self, "privateConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrivateConnectionRef).__jsii_proxy_class__ = lambda : _IPrivateConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.IServiceRef")
class IServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        ...


class _IServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.IServiceRef"

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        return typing.cast("ServiceReference", jsii.get(self, "serviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceRef).__jsii_proxy_class__ = lambda : _IServiceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.ITriggerRef")
class ITriggerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Trigger.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="triggerRef")
    def trigger_ref(self) -> "TriggerReference":
        '''(experimental) A reference to a Trigger resource.

        :stability: experimental
        '''
        ...


class _ITriggerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Trigger.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.ITriggerRef"

    @builtins.property
    @jsii.member(jsii_name="triggerRef")
    def trigger_ref(self) -> "TriggerReference":
        '''(experimental) A reference to a Trigger resource.

        :stability: experimental
        '''
        return typing.cast("TriggerReference", jsii.get(self, "triggerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITriggerRef).__jsii_proxy_class__ = lambda : _ITriggerRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.PrivateConnectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "private_connection_arn": "privateConnectionArn",
        "private_connection_name": "privateConnectionName",
    },
)
class PrivateConnectionReference:
    def __init__(
        self,
        *,
        private_connection_arn: builtins.str,
        private_connection_name: builtins.str,
    ) -> None:
        '''A reference to a PrivateConnection resource.

        :param private_connection_arn: The ARN of the PrivateConnection resource.
        :param private_connection_name: The Name of the PrivateConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            private_connection_reference = interfaces_devopsagent.PrivateConnectionReference(
                private_connection_arn="privateConnectionArn",
                private_connection_name="privateConnectionName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2def640e7c2b099f513cf363f4461e9d56d50feb02228dac70b092330aafb258)
            check_type(argname="argument private_connection_arn", value=private_connection_arn, expected_type=type_hints["private_connection_arn"])
            check_type(argname="argument private_connection_name", value=private_connection_name, expected_type=type_hints["private_connection_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "private_connection_arn": private_connection_arn,
            "private_connection_name": private_connection_name,
        }

    @builtins.property
    def private_connection_arn(self) -> builtins.str:
        '''The ARN of the PrivateConnection resource.'''
        result = self._values.get("private_connection_arn")
        assert result is not None, "Required property 'private_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_connection_name(self) -> builtins.str:
        '''The Name of the PrivateConnection resource.'''
        result = self._values.get("private_connection_name")
        assert result is not None, "Required property 'private_connection_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.ServiceReference",
    jsii_struct_bases=[],
    name_mapping={"service_arn": "serviceArn", "service_id": "serviceId"},
)
class ServiceReference:
    def __init__(self, *, service_arn: builtins.str, service_id: builtins.str) -> None:
        '''A reference to a Service resource.

        :param service_arn: The ARN of the Service resource.
        :param service_id: The ServiceId of the Service resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            service_reference = interfaces_devopsagent.ServiceReference(
                service_arn="serviceArn",
                service_id="serviceId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__07ccf3b3910b4e346e3aafaa8df25d00cb1ad66f67f835fb8c05b14d4cf5ce22)
            check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_arn": service_arn,
            "service_id": service_id,
        }

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''The ARN of the Service resource.'''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_id(self) -> builtins.str:
        '''The ServiceId of the Service resource.'''
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.TriggerReference",
    jsii_struct_bases=[],
    name_mapping={
        "agent_space_id": "agentSpaceId",
        "trigger_arn": "triggerArn",
        "trigger_id": "triggerId",
    },
)
class TriggerReference:
    def __init__(
        self,
        *,
        agent_space_id: builtins.str,
        trigger_arn: builtins.str,
        trigger_id: builtins.str,
    ) -> None:
        '''A reference to a Trigger resource.

        :param agent_space_id: The AgentSpaceId of the Trigger resource.
        :param trigger_arn: The ARN of the Trigger resource.
        :param trigger_id: The TriggerId of the Trigger resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            trigger_reference = interfaces_devopsagent.TriggerReference(
                agent_space_id="agentSpaceId",
                trigger_arn="triggerArn",
                trigger_id="triggerId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b2334c3b3f5d85bb6bbe5d5d6389c0b340214fd4e5d54bdb8336c1e2fbe619d8)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
            check_type(argname="argument trigger_arn", value=trigger_arn, expected_type=type_hints["trigger_arn"])
            check_type(argname="argument trigger_id", value=trigger_id, expected_type=type_hints["trigger_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
            "trigger_arn": trigger_arn,
            "trigger_id": trigger_id,
        }

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the Trigger resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trigger_arn(self) -> builtins.str:
        '''The ARN of the Trigger resource.'''
        result = self._values.get("trigger_arn")
        assert result is not None, "Required property 'trigger_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trigger_id(self) -> builtins.str:
        '''The TriggerId of the Trigger resource.'''
        result = self._values.get("trigger_id")
        assert result is not None, "Required property 'trigger_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AgentSpaceReference",
    "AssetReference",
    "AssociationReference",
    "IAgentSpaceRef",
    "IAssetRef",
    "IAssociationRef",
    "IPrivateConnectionRef",
    "IServiceRef",
    "ITriggerRef",
    "PrivateConnectionReference",
    "ServiceReference",
    "TriggerReference",
]

publication.publish()

def _typecheckingstub__243d248446cd635e4d580c7e821c36a9651420cfff39e507c6e56843c8dfb804(
    *,
    agent_space_arn: builtins.str,
    agent_space_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e07ae93fd4597600bcf048453225278461c377da1857624454c2c72c898a881(
    *,
    agent_space_id: builtins.str,
    asset_arn: builtins.str,
    asset_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02318c63b2a10c35692903fce2e2a91bd6e6b83485fb019a8dd7f1e3e1a7d952(
    *,
    agent_space_id: builtins.str,
    association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2def640e7c2b099f513cf363f4461e9d56d50feb02228dac70b092330aafb258(
    *,
    private_connection_arn: builtins.str,
    private_connection_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ccf3b3910b4e346e3aafaa8df25d00cb1ad66f67f835fb8c05b14d4cf5ce22(
    *,
    service_arn: builtins.str,
    service_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2334c3b3f5d85bb6bbe5d5d6389c0b340214fd4e5d54bdb8336c1e2fbe619d8(
    *,
    agent_space_id: builtins.str,
    trigger_arn: builtins.str,
    trigger_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgentSpaceRef, IAssetRef, IAssociationRef, IPrivateConnectionRef, IServiceRef, ITriggerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
