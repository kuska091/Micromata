r'''
# AWS::Wickr Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_wickr as wickr
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Wickr construct libraries](https://constructs.dev/search?q=wickr)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Wickr resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Wickr.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Wickr](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Wickr.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
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


from .._jsii import *

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
    import aws_cdk.interfaces.aws_wickr as _aws_wickr_2f0d0a41
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_wickr_2f0d0a41 = _LazyImport("aws_cdk.interfaces.aws_wickr")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_wickr_2f0d0a41.INetworkRef)
class CfnNetwork(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wickr.CfnNetwork",
):
    '''Resource Type definition for AWS::Wickr::Network.

    Creates and manages an AWS Wickr network for secure enterprise communications.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wickr-network.html
    :cloudformationResource: AWS::Wickr::Network
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wickr as wickr
        
        cfn_network = wickr.CfnNetwork(self, "MyCfnNetwork",
            access_level="accessLevel",
            network_name="networkName"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        access_level: builtins.str,
        network_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::Wickr::Network``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_level: The access level of the network, which determines available features and capabilities.
        :param network_name: The name of the network. Must be between 1 and 20 characters.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__81c0bc9ea699dce9f5955ed4c79822438d39e5e001dd13620148fe44248575d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNetworkProps(access_level=access_level, network_name=network_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForNetwork")
    @builtins.classmethod
    def arn_for_network(
        cls,
        resource: "_aws_wickr_2f0d0a41.INetworkRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cc9f30433f5eea603da1346e5527bd4b330d01ce0f08e8862cfbae4687475b09)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForNetwork", [resource]))

    @jsii.member(jsii_name="isCfnNetwork")
    @builtins.classmethod
    def is_cfn_network(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnNetwork.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d60d79658de52d7f60d9cbe3de5497035ef8578a035f10776ca14e16ec67c6a1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnNetwork", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__47fdca42395f3ffae246ec14b16a3a49825313fb629d194c04f4f4cdb2e345b6)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6e1e6bf5eb07b9e40c31a1ee03cdcfc51c022cd79e6c88bd85b1ac239ca2f086)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''The AWS account ID that owns the network.

        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrMigrationState")
    def attr_migration_state(self) -> jsii.Number:
        '''The SSO redirect URI migration state.

        Values: 0 (not started), 1 (in progress), or 2 (completed).

        :cloudformationAttribute: MigrationState
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMigrationState"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkArn")
    def attr_network_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the network.

        :cloudformationAttribute: NetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkId")
    def attr_network_id(self) -> builtins.str:
        '''The unique identifier of the network.

        :cloudformationAttribute: NetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNetworkId"))

    @builtins.property
    @jsii.member(jsii_name="attrStanding")
    def attr_standing(self) -> jsii.Number:
        '''The current standing or status of the network.

        :cloudformationAttribute: Standing
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrStanding"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="networkRef")
    def network_ref(self) -> "_aws_wickr_2f0d0a41.NetworkReference":
        '''A reference to a Network resource.'''
        return typing.cast("_aws_wickr_2f0d0a41.NetworkReference", jsii.get(self, "networkRef"))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        '''The access level of the network, which determines available features and capabilities.'''
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @access_level.setter
    def access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a9fa6de10c28ffaeb93ba1a2ffb9c416468dda7fb409d2373750881dd7c37655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkName")
    def network_name(self) -> builtins.str:
        '''The name of the network.'''
        return typing.cast(builtins.str, jsii.get(self, "networkName"))

    @network_name.setter
    def network_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c2387b6134a0da373f84425bce0f8f21e6c4d8c3560eedcad94770d521aa934c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkName", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wickr.CfnNetworkProps",
    jsii_struct_bases=[],
    name_mapping={"access_level": "accessLevel", "network_name": "networkName"},
)
class CfnNetworkProps:
    def __init__(
        self,
        *,
        access_level: builtins.str,
        network_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnNetwork``.

        :param access_level: The access level of the network, which determines available features and capabilities.
        :param network_name: The name of the network. Must be between 1 and 20 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wickr-network.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wickr as wickr
            
            cfn_network_props = wickr.CfnNetworkProps(
                access_level="accessLevel",
                network_name="networkName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a67678649fc2c36d8aca9f3f8e35fc5af9fb7fc6aaea5094fbfc22ae3ff0b5cc)
            check_type(argname="argument access_level", value=access_level, expected_type=type_hints["access_level"])
            check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_level": access_level,
            "network_name": network_name,
        }

    @builtins.property
    def access_level(self) -> builtins.str:
        '''The access level of the network, which determines available features and capabilities.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wickr-network.html#cfn-wickr-network-accesslevel
        '''
        result = self._values.get("access_level")
        assert result is not None, "Required property 'access_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_name(self) -> builtins.str:
        '''The name of the network.

        Must be between 1 and 20 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wickr-network.html#cfn-wickr-network-networkname
        '''
        result = self._values.get("network_name")
        assert result is not None, "Required property 'network_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNetwork",
    "CfnNetworkProps",
]

publication.publish()

def _typecheckingstub__81c0bc9ea699dce9f5955ed4c79822438d39e5e001dd13620148fe44248575d2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_level: builtins.str,
    network_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9f30433f5eea603da1346e5527bd4b330d01ce0f08e8862cfbae4687475b09(
    resource: _aws_wickr_2f0d0a41.INetworkRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d60d79658de52d7f60d9cbe3de5497035ef8578a035f10776ca14e16ec67c6a1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47fdca42395f3ffae246ec14b16a3a49825313fb629d194c04f4f4cdb2e345b6(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1e6bf5eb07b9e40c31a1ee03cdcfc51c022cd79e6c88bd85b1ac239ca2f086(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9fa6de10c28ffaeb93ba1a2ffb9c416468dda7fb409d2373750881dd7c37655(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2387b6134a0da373f84425bce0f8f21e6c4d8c3560eedcad94770d521aa934c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a67678649fc2c36d8aca9f3f8e35fc5af9fb7fc6aaea5094fbfc22ae3ff0b5cc(
    *,
    access_level: builtins.str,
    network_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
