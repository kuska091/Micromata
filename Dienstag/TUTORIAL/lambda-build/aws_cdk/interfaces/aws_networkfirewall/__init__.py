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
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.ContainerAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"container_association_arn": "containerAssociationArn"},
)
class ContainerAssociationReference:
    def __init__(self, *, container_association_arn: builtins.str) -> None:
        '''A reference to a ContainerAssociation resource.

        :param container_association_arn: The ContainerAssociationArn of the ContainerAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkfirewall as interfaces_networkfirewall
            
            container_association_reference = interfaces_networkfirewall.ContainerAssociationReference(
                container_association_arn="containerAssociationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a60d64c9a952fad867dc88469e47c5a6221a5a4dd9ac3960dc6e263f100efe2e)
            check_type(argname="argument container_association_arn", value=container_association_arn, expected_type=type_hints["container_association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_association_arn": container_association_arn,
        }

    @builtins.property
    def container_association_arn(self) -> builtins.str:
        '''The ContainerAssociationArn of the ContainerAssociation resource.'''
        result = self._values.get("container_association_arn")
        assert result is not None, "Required property 'container_association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.FirewallPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"firewall_policy_arn": "firewallPolicyArn"},
)
class FirewallPolicyReference:
    def __init__(self, *, firewall_policy_arn: builtins.str) -> None:
        '''A reference to a FirewallPolicy resource.

        :param firewall_policy_arn: The FirewallPolicyArn of the FirewallPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkfirewall as interfaces_networkfirewall
            
            firewall_policy_reference = interfaces_networkfirewall.FirewallPolicyReference(
                firewall_policy_arn="firewallPolicyArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bc3a7ea8f865dd2ed15f63bf33b08bd8a433c4d9c685696775a3cef691b50192)
            check_type(argname="argument firewall_policy_arn", value=firewall_policy_arn, expected_type=type_hints["firewall_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_policy_arn": firewall_policy_arn,
        }

    @builtins.property
    def firewall_policy_arn(self) -> builtins.str:
        '''The FirewallPolicyArn of the FirewallPolicy resource.'''
        result = self._values.get("firewall_policy_arn")
        assert result is not None, "Required property 'firewall_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.FirewallReference",
    jsii_struct_bases=[],
    name_mapping={"firewall_arn": "firewallArn"},
)
class FirewallReference:
    def __init__(self, *, firewall_arn: builtins.str) -> None:
        '''A reference to a Firewall resource.

        :param firewall_arn: The FirewallArn of the Firewall resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkfirewall as interfaces_networkfirewall
            
            firewall_reference = interfaces_networkfirewall.FirewallReference(
                firewall_arn="firewallArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__09e2b2db10474a5b008d17f0c1f0194fb9be22a9cac3f103f27d8aeaa9c8adac)
            check_type(argname="argument firewall_arn", value=firewall_arn, expected_type=type_hints["firewall_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_arn": firewall_arn,
        }

    @builtins.property
    def firewall_arn(self) -> builtins.str:
        '''The FirewallArn of the Firewall resource.'''
        result = self._values.get("firewall_arn")
        assert result is not None, "Required property 'firewall_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.IContainerAssociationRef"
)
class IContainerAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContainerAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="containerAssociationRef")
    def container_association_ref(self) -> "ContainerAssociationReference":
        '''(experimental) A reference to a ContainerAssociation resource.

        :stability: experimental
        '''
        ...


class _IContainerAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContainerAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkfirewall.IContainerAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="containerAssociationRef")
    def container_association_ref(self) -> "ContainerAssociationReference":
        '''(experimental) A reference to a ContainerAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ContainerAssociationReference", jsii.get(self, "containerAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContainerAssociationRef).__jsii_proxy_class__ = lambda : _IContainerAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.IFirewallPolicyRef"
)
class IFirewallPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyRef")
    def firewall_policy_ref(self) -> "FirewallPolicyReference":
        '''(experimental) A reference to a FirewallPolicy resource.

        :stability: experimental
        '''
        ...


class _IFirewallPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkfirewall.IFirewallPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="firewallPolicyRef")
    def firewall_policy_ref(self) -> "FirewallPolicyReference":
        '''(experimental) A reference to a FirewallPolicy resource.

        :stability: experimental
        '''
        return typing.cast("FirewallPolicyReference", jsii.get(self, "firewallPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallPolicyRef).__jsii_proxy_class__ = lambda : _IFirewallPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.IFirewallRef")
class IFirewallRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Firewall.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="firewallRef")
    def firewall_ref(self) -> "FirewallReference":
        '''(experimental) A reference to a Firewall resource.

        :stability: experimental
        '''
        ...


class _IFirewallRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Firewall.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkfirewall.IFirewallRef"

    @builtins.property
    @jsii.member(jsii_name="firewallRef")
    def firewall_ref(self) -> "FirewallReference":
        '''(experimental) A reference to a Firewall resource.

        :stability: experimental
        '''
        return typing.cast("FirewallReference", jsii.get(self, "firewallRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallRef).__jsii_proxy_class__ = lambda : _IFirewallRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.ILoggingConfigurationRef"
)
class ILoggingConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LoggingConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loggingConfigurationRef")
    def logging_configuration_ref(self) -> "LoggingConfigurationReference":
        '''(experimental) A reference to a LoggingConfiguration resource.

        :stability: experimental
        '''
        ...


class _ILoggingConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LoggingConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkfirewall.ILoggingConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="loggingConfigurationRef")
    def logging_configuration_ref(self) -> "LoggingConfigurationReference":
        '''(experimental) A reference to a LoggingConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("LoggingConfigurationReference", jsii.get(self, "loggingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoggingConfigurationRef).__jsii_proxy_class__ = lambda : _ILoggingConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.IRuleGroupRef")
class IRuleGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RuleGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ruleGroupRef")
    def rule_group_ref(self) -> "RuleGroupReference":
        '''(experimental) A reference to a RuleGroup resource.

        :stability: experimental
        '''
        ...


class _IRuleGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RuleGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkfirewall.IRuleGroupRef"

    @builtins.property
    @jsii.member(jsii_name="ruleGroupRef")
    def rule_group_ref(self) -> "RuleGroupReference":
        '''(experimental) A reference to a RuleGroup resource.

        :stability: experimental
        '''
        return typing.cast("RuleGroupReference", jsii.get(self, "ruleGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuleGroupRef).__jsii_proxy_class__ = lambda : _IRuleGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.ITLSInspectionConfigurationRef"
)
class ITLSInspectionConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TLSInspectionConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tlsInspectionConfigurationRef")
    def tls_inspection_configuration_ref(self) -> "TLSInspectionConfigurationReference":
        '''(experimental) A reference to a TLSInspectionConfiguration resource.

        :stability: experimental
        '''
        ...


class _ITLSInspectionConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TLSInspectionConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkfirewall.ITLSInspectionConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="tlsInspectionConfigurationRef")
    def tls_inspection_configuration_ref(self) -> "TLSInspectionConfigurationReference":
        '''(experimental) A reference to a TLSInspectionConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("TLSInspectionConfigurationReference", jsii.get(self, "tlsInspectionConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITLSInspectionConfigurationRef).__jsii_proxy_class__ = lambda : _ITLSInspectionConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.IVpcEndpointAssociationRef"
)
class IVpcEndpointAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VpcEndpointAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointAssociationRef")
    def vpc_endpoint_association_ref(self) -> "VpcEndpointAssociationReference":
        '''(experimental) A reference to a VpcEndpointAssociation resource.

        :stability: experimental
        '''
        ...


class _IVpcEndpointAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VpcEndpointAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkfirewall.IVpcEndpointAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointAssociationRef")
    def vpc_endpoint_association_ref(self) -> "VpcEndpointAssociationReference":
        '''(experimental) A reference to a VpcEndpointAssociation resource.

        :stability: experimental
        '''
        return typing.cast("VpcEndpointAssociationReference", jsii.get(self, "vpcEndpointAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpcEndpointAssociationRef).__jsii_proxy_class__ = lambda : _IVpcEndpointAssociationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.LoggingConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"firewall_arn": "firewallArn"},
)
class LoggingConfigurationReference:
    def __init__(self, *, firewall_arn: builtins.str) -> None:
        '''A reference to a LoggingConfiguration resource.

        :param firewall_arn: The FirewallArn of the LoggingConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkfirewall as interfaces_networkfirewall
            
            logging_configuration_reference = interfaces_networkfirewall.LoggingConfigurationReference(
                firewall_arn="firewallArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0b2e130cb897e29769cd8caa5fb2ee61cdad746ee08d5418a84eab440466be4e)
            check_type(argname="argument firewall_arn", value=firewall_arn, expected_type=type_hints["firewall_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_arn": firewall_arn,
        }

    @builtins.property
    def firewall_arn(self) -> builtins.str:
        '''The FirewallArn of the LoggingConfiguration resource.'''
        result = self._values.get("firewall_arn")
        assert result is not None, "Required property 'firewall_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.RuleGroupReference",
    jsii_struct_bases=[],
    name_mapping={"rule_group_arn": "ruleGroupArn"},
)
class RuleGroupReference:
    def __init__(self, *, rule_group_arn: builtins.str) -> None:
        '''A reference to a RuleGroup resource.

        :param rule_group_arn: The RuleGroupArn of the RuleGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkfirewall as interfaces_networkfirewall
            
            rule_group_reference = interfaces_networkfirewall.RuleGroupReference(
                rule_group_arn="ruleGroupArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d924df4cd658e7ea028419c44239556d79164c2bd3c007c6240c5426dbf3b2f9)
            check_type(argname="argument rule_group_arn", value=rule_group_arn, expected_type=type_hints["rule_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_group_arn": rule_group_arn,
        }

    @builtins.property
    def rule_group_arn(self) -> builtins.str:
        '''The RuleGroupArn of the RuleGroup resource.'''
        result = self._values.get("rule_group_arn")
        assert result is not None, "Required property 'rule_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.TLSInspectionConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"tls_inspection_configuration_arn": "tlsInspectionConfigurationArn"},
)
class TLSInspectionConfigurationReference:
    def __init__(self, *, tls_inspection_configuration_arn: builtins.str) -> None:
        '''A reference to a TLSInspectionConfiguration resource.

        :param tls_inspection_configuration_arn: The TLSInspectionConfigurationArn of the TLSInspectionConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkfirewall as interfaces_networkfirewall
            
            t_ls_inspection_configuration_reference = interfaces_networkfirewall.TLSInspectionConfigurationReference(
                tls_inspection_configuration_arn="tlsInspectionConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__521256213abf6e999a8897786d1d0c9c581d7ef53e65f40d696ecb8a0db106c8)
            check_type(argname="argument tls_inspection_configuration_arn", value=tls_inspection_configuration_arn, expected_type=type_hints["tls_inspection_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tls_inspection_configuration_arn": tls_inspection_configuration_arn,
        }

    @builtins.property
    def tls_inspection_configuration_arn(self) -> builtins.str:
        '''The TLSInspectionConfigurationArn of the TLSInspectionConfiguration resource.'''
        result = self._values.get("tls_inspection_configuration_arn")
        assert result is not None, "Required property 'tls_inspection_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TLSInspectionConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkfirewall.VpcEndpointAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_endpoint_association_arn": "vpcEndpointAssociationArn"},
)
class VpcEndpointAssociationReference:
    def __init__(self, *, vpc_endpoint_association_arn: builtins.str) -> None:
        '''A reference to a VpcEndpointAssociation resource.

        :param vpc_endpoint_association_arn: The VpcEndpointAssociationArn of the VpcEndpointAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkfirewall as interfaces_networkfirewall
            
            vpc_endpoint_association_reference = interfaces_networkfirewall.VpcEndpointAssociationReference(
                vpc_endpoint_association_arn="vpcEndpointAssociationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__685dfbe589915ae995a2001ac169f17fe768f12601dbc55650b6a3da2e7b12b9)
            check_type(argname="argument vpc_endpoint_association_arn", value=vpc_endpoint_association_arn, expected_type=type_hints["vpc_endpoint_association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_endpoint_association_arn": vpc_endpoint_association_arn,
        }

    @builtins.property
    def vpc_endpoint_association_arn(self) -> builtins.str:
        '''The VpcEndpointAssociationArn of the VpcEndpointAssociation resource.'''
        result = self._values.get("vpc_endpoint_association_arn")
        assert result is not None, "Required property 'vpc_endpoint_association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcEndpointAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ContainerAssociationReference",
    "FirewallPolicyReference",
    "FirewallReference",
    "IContainerAssociationRef",
    "IFirewallPolicyRef",
    "IFirewallRef",
    "ILoggingConfigurationRef",
    "IRuleGroupRef",
    "ITLSInspectionConfigurationRef",
    "IVpcEndpointAssociationRef",
    "LoggingConfigurationReference",
    "RuleGroupReference",
    "TLSInspectionConfigurationReference",
    "VpcEndpointAssociationReference",
]

publication.publish()

def _typecheckingstub__a60d64c9a952fad867dc88469e47c5a6221a5a4dd9ac3960dc6e263f100efe2e(
    *,
    container_association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3a7ea8f865dd2ed15f63bf33b08bd8a433c4d9c685696775a3cef691b50192(
    *,
    firewall_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e2b2db10474a5b008d17f0c1f0194fb9be22a9cac3f103f27d8aeaa9c8adac(
    *,
    firewall_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2e130cb897e29769cd8caa5fb2ee61cdad746ee08d5418a84eab440466be4e(
    *,
    firewall_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d924df4cd658e7ea028419c44239556d79164c2bd3c007c6240c5426dbf3b2f9(
    *,
    rule_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521256213abf6e999a8897786d1d0c9c581d7ef53e65f40d696ecb8a0db106c8(
    *,
    tls_inspection_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__685dfbe589915ae995a2001ac169f17fe768f12601dbc55650b6a3da2e7b12b9(
    *,
    vpc_endpoint_association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IContainerAssociationRef, IFirewallPolicyRef, IFirewallRef, ILoggingConfigurationRef, IRuleGroupRef, ITLSInspectionConfigurationRef, IVpcEndpointAssociationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
