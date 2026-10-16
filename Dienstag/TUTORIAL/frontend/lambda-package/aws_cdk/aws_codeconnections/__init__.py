r'''
# AWS::CodeConnections Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_codeconnections as codeconnections
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CodeConnections construct libraries](https://constructs.dev/search?q=codeconnections)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CodeConnections resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeConnections.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CodeConnections](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeConnections.html).

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
    import aws_cdk.interfaces.aws_codeconnections as _aws_codeconnections_a8ecd32b
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_codeconnections_a8ecd32b = _LazyImport("aws_cdk.interfaces.aws_codeconnections")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_codeconnections_a8ecd32b.IConnectionRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnConnection(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codeconnections.CfnConnection",
):
    '''A resource that is used to connect third-party source providers with services like CodePipeline.

    Note: A connection created through CloudFormation , the CLI, or the SDK is in ``PENDING`` status by default. You can make its status ``AVAILABLE`` by updating the connection in the console.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.html
    :cloudformationResource: AWS::CodeConnections::Connection
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codeconnections as codeconnections
        
        cfn_connection = codeconnections.CfnConnection(self, "MyCfnConnection",
            connection_name="connectionName",
        
            # the properties below are optional
            host_arn="hostArn",
            provider_type="providerType",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        connection_name: builtins.str,
        host_arn: typing.Optional[builtins.str] = None,
        provider_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::CodeConnections::Connection``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connection_name: The name of the connection. Connection names must be unique in an AWS account .
        :param host_arn: The Amazon Resource Name (ARN) of the host associated with the connection.
        :param provider_type: The name of the external provider where your third-party code repository is configured.
        :param tags: Specifies the tags applied to a connection.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__da00c1ce515c51afa7843809dadd2cb48a76e0e91dd2a8096cc430768e89a815)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectionProps(
            connection_name=connection_name,
            host_arn=host_arn,
            provider_type=provider_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForConnection")
    @builtins.classmethod
    def arn_for_connection(
        cls,
        resource: "_aws_codeconnections_a8ecd32b.IConnectionRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f0ebbeeb1a7e2051887bff67db79721fdc6e69076719f3a98c63ec4924102c1b)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForConnection", [resource]))

    @jsii.member(jsii_name="isCfnConnection")
    @builtins.classmethod
    def is_cfn_connection(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnConnection.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9da098eb0ec1eadf1e6c8e2874d960931a10c48234cfa2f71152fac89bc28721)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnConnection", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__78744497e1b5bae3f2ea20b9d3496e178855aef0e29d2de71777b026a6d27a1a)
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
            type_hints = cached_type_hints(_typecheckingstub__440f5e3662e5ab05ab71cf41aafae8bf45c3a11a457c7bbc13517a3eb9e7278e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionArn")
    def attr_connection_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connection.

        The ARN is used as the connection reference when the connection is shared between AWS services .
        .. epigraph::

           The ARN is never reused if the connection is deleted.

        :cloudformationAttribute: ConnectionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionStatus")
    def attr_connection_status(self) -> builtins.str:
        '''The current status of the connection.

        :cloudformationAttribute: ConnectionStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The identifier of the external provider where your third-party code repository is configured.

        For Bitbucket, this is the account ID of the owner of the Bitbucket repository.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "_aws_codeconnections_a8ecd32b.ConnectionReference":
        '''A reference to a Connection resource.'''
        return typing.cast("_aws_codeconnections_a8ecd32b.ConnectionReference", jsii.get(self, "connectionRef"))

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        '''The name of the connection.'''
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7d759fec9e0861542e9267cd70eacda49ebbb2a1399fb2f36364a2a01d38cdc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostArn")
    def host_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the host associated with the connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostArn"))

    @host_arn.setter
    def host_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6c6c22c4d5132fe518d2a74aed1b6d9c89f7a2fbb163195a459d8af8791cf1c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="providerType")
    def provider_type(self) -> typing.Optional[builtins.str]:
        '''The name of the external provider where your third-party code repository is configured.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerType"))

    @provider_type.setter
    def provider_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2ec396e84dc4ee92669ed87aa685780cf9af74b974c8d0d7f12b0c1196dc17d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Specifies the tags applied to a connection.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cd277a1214d747c2b8b1a0998909d0fe0edc54719c5d7b8ae3621585dbf60405)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codeconnections.CfnConnectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "connection_name": "connectionName",
        "host_arn": "hostArn",
        "provider_type": "providerType",
        "tags": "tags",
    },
)
class CfnConnectionProps:
    def __init__(
        self,
        *,
        connection_name: builtins.str,
        host_arn: typing.Optional[builtins.str] = None,
        provider_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnection``.

        :param connection_name: The name of the connection. Connection names must be unique in an AWS account .
        :param host_arn: The Amazon Resource Name (ARN) of the host associated with the connection.
        :param provider_type: The name of the external provider where your third-party code repository is configured.
        :param tags: Specifies the tags applied to a connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codeconnections as codeconnections
            
            cfn_connection_props = codeconnections.CfnConnectionProps(
                connection_name="connectionName",
            
                # the properties below are optional
                host_arn="hostArn",
                provider_type="providerType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4ac62d1262e0fc9d7647548096d4e83c0367271b1f1be70c2119c14ec99b3dde)
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument host_arn", value=host_arn, expected_type=type_hints["host_arn"])
            check_type(argname="argument provider_type", value=provider_type, expected_type=type_hints["provider_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_name": connection_name,
        }
        if host_arn is not None:
            self._values["host_arn"] = host_arn
        if provider_type is not None:
            self._values["provider_type"] = provider_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''The name of the connection.

        Connection names must be unique in an AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.html#cfn-codeconnections-connection-connectionname
        '''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the host associated with the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.html#cfn-codeconnections-connection-hostarn
        '''
        result = self._values.get("host_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_type(self) -> typing.Optional[builtins.str]:
        '''The name of the external provider where your third-party code repository is configured.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.html#cfn-codeconnections-connection-providertype
        '''
        result = self._values.get("provider_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Specifies the tags applied to a connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-connection.html#cfn-codeconnections-connection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_codeconnections_a8ecd32b.IHostRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnHost(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codeconnections.CfnHost",
):
    '''A resource that represents the infrastructure where a third-party provider is installed.

    You create one host for all connections to that provider.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-host.html
    :cloudformationResource: AWS::CodeConnections::Host
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codeconnections as codeconnections
        
        cfn_host = codeconnections.CfnHost(self, "MyCfnHost",
            name="name",
            provider_endpoint="providerEndpoint",
            provider_type="providerType",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_configuration=codeconnections.CfnHost.VpcConfigurationProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId",
        
                # the properties below are optional
                tls_certificate="tlsCertificate"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        provider_endpoint: builtins.str,
        provider_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnHost.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::CodeConnections::Host``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the host.
        :param provider_endpoint: The endpoint of the infrastructure where your provider type is installed.
        :param provider_type: The name of the installed provider to be associated with your connection.
        :param tags: Tags to apply to the host.
        :param vpc_configuration: The VPC configuration provisioned for the host.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__955548f1a83434bfe589e9465d3ab38c3c5f90d595957f0eb3ef54787a04f285)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHostProps(
            name=name,
            provider_endpoint=provider_endpoint,
            provider_type=provider_type,
            tags=tags,
            vpc_configuration=vpc_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForHost")
    @builtins.classmethod
    def arn_for_host(
        cls,
        resource: "_aws_codeconnections_a8ecd32b.IHostRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0492aff78c45a9849781a5145a2b63a75cedeb364faba0296cd5bfcdefa53e55)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForHost", [resource]))

    @jsii.member(jsii_name="isCfnHost")
    @builtins.classmethod
    def is_cfn_host(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnHost.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e09acbbff41515e4490dded19b0ddabbb1cdb04a48b03aceb6682ab76df622f7)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnHost", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c45b5f878984505d2aeba188062b1e8f8e1eca11e0724100a66dac60afca8216)
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
            type_hints = cached_type_hints(_typecheckingstub__452af0397c9fbd5f363dc2634e782d06ff8f2f0afccd9e8f0c46f65678743e14)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrHostArn")
    def attr_host_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the host.

        :cloudformationAttribute: HostArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostArn"))

    @builtins.property
    @jsii.member(jsii_name="attrHostId")
    def attr_host_id(self) -> builtins.str:
        '''The server-generated unique identifier for the host.

        :cloudformationAttribute: HostId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the host.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="hostRef")
    def host_ref(self) -> "_aws_codeconnections_a8ecd32b.HostReference":
        '''A reference to a Host resource.'''
        return typing.cast("_aws_codeconnections_a8ecd32b.HostReference", jsii.get(self, "hostRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the host.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__678966c1f3caebbcde15336278f21fc87bf5d68238732993317db86fb321ebff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="providerEndpoint")
    def provider_endpoint(self) -> builtins.str:
        '''The endpoint of the infrastructure where your provider type is installed.'''
        return typing.cast(builtins.str, jsii.get(self, "providerEndpoint"))

    @provider_endpoint.setter
    def provider_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5175881a75564bdfb981168592d63f0fcdbd1168ea713126172f952adf7fe746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerEndpoint", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="providerType")
    def provider_type(self) -> builtins.str:
        '''The name of the installed provider to be associated with your connection.'''
        return typing.cast(builtins.str, jsii.get(self, "providerType"))

    @provider_type.setter
    def provider_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e9b3edf4c4c8471028dd998530b46a885509ab3141208eeb91011d9bae314610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to apply to the host.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d888addd54ad753cc084483b45bf5d0a97682ff702b90d2a91c2ceaaadb625f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnHost.VpcConfigurationProperty"]]:
        '''The VPC configuration provisioned for the host.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnHost.VpcConfigurationProperty"]], jsii.get(self, "vpcConfiguration"))

    @vpc_configuration.setter
    def vpc_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnHost.VpcConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b8184046a577db6ff901740449c6a521de0eda15f52c5465b0c80a37fb0a544f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codeconnections.CfnHost.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
            "vpc_id": "vpcId",
            "tls_certificate": "tlsCertificate",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
            tls_certificate: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The VPC configuration provisioned for the host.

            :param security_group_ids: The ID of the security group or security groups associated with the Amazon VPC.
            :param subnet_ids: The ID of the subnet or subnets associated with the Amazon VPC.
            :param vpc_id: The ID of the Amazon VPC connected to the infrastructure where your provider type is installed.
            :param tls_certificate: The value of the Transport Layer Security (TLS) certificate associated with the infrastructure where your provider type is installed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeconnections-host-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codeconnections as codeconnections
                
                vpc_configuration_property = codeconnections.CfnHost.VpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId",
                
                    # the properties below are optional
                    tls_certificate="tlsCertificate"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__9952b7aab3d4882aa0bf265afa825ea9b776d4a6956aea96ad2b585de9be50f5)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
                check_type(argname="argument tls_certificate", value=tls_certificate, expected_type=type_hints["tls_certificate"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }
            if tls_certificate is not None:
                self._values["tls_certificate"] = tls_certificate

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The ID of the security group or security groups associated with the Amazon VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeconnections-host-vpcconfiguration.html#cfn-codeconnections-host-vpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The ID of the subnet or subnets associated with the Amazon VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeconnections-host-vpcconfiguration.html#cfn-codeconnections-host-vpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''The ID of the Amazon VPC connected to the infrastructure where your provider type is installed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeconnections-host-vpcconfiguration.html#cfn-codeconnections-host-vpcconfiguration-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tls_certificate(self) -> typing.Optional[builtins.str]:
            '''The value of the Transport Layer Security (TLS) certificate associated with the infrastructure where your provider type is installed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeconnections-host-vpcconfiguration.html#cfn-codeconnections-host-vpcconfiguration-tlscertificate
            '''
            result = self._values.get("tls_certificate")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codeconnections.CfnHostProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "provider_endpoint": "providerEndpoint",
        "provider_type": "providerType",
        "tags": "tags",
        "vpc_configuration": "vpcConfiguration",
    },
)
class CfnHostProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        provider_endpoint: builtins.str,
        provider_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnHost.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnHost``.

        :param name: The name of the host.
        :param provider_endpoint: The endpoint of the infrastructure where your provider type is installed.
        :param provider_type: The name of the installed provider to be associated with your connection.
        :param tags: Tags to apply to the host.
        :param vpc_configuration: The VPC configuration provisioned for the host.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-host.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codeconnections as codeconnections
            
            cfn_host_props = codeconnections.CfnHostProps(
                name="name",
                provider_endpoint="providerEndpoint",
                provider_type="providerType",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_configuration=codeconnections.CfnHost.VpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId",
            
                    # the properties below are optional
                    tls_certificate="tlsCertificate"
                )
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9f84ea6586678bf17fc941a6bb2712401c1fee06b478e44253c3551e1514b12c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument provider_endpoint", value=provider_endpoint, expected_type=type_hints["provider_endpoint"])
            check_type(argname="argument provider_type", value=provider_type, expected_type=type_hints["provider_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "provider_endpoint": provider_endpoint,
            "provider_type": provider_type,
        }
        if tags is not None:
            self._values["tags"] = tags
        if vpc_configuration is not None:
            self._values["vpc_configuration"] = vpc_configuration

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the host.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-host.html#cfn-codeconnections-host-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider_endpoint(self) -> builtins.str:
        '''The endpoint of the infrastructure where your provider type is installed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-host.html#cfn-codeconnections-host-providerendpoint
        '''
        result = self._values.get("provider_endpoint")
        assert result is not None, "Required property 'provider_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider_type(self) -> builtins.str:
        '''The name of the installed provider to be associated with your connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-host.html#cfn-codeconnections-host-providertype
        '''
        result = self._values.get("provider_type")
        assert result is not None, "Required property 'provider_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to apply to the host.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-host.html#cfn-codeconnections-host-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def vpc_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnHost.VpcConfigurationProperty"]]:
        '''The VPC configuration provisioned for the host.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeconnections-host.html#cfn-codeconnections-host-vpcconfiguration
        '''
        result = self._values.get("vpc_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnHost.VpcConfigurationProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHostProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnection",
    "CfnConnectionProps",
    "CfnHost",
    "CfnHostProps",
]

publication.publish()

def _typecheckingstub__da00c1ce515c51afa7843809dadd2cb48a76e0e91dd2a8096cc430768e89a815(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connection_name: builtins.str,
    host_arn: typing.Optional[builtins.str] = None,
    provider_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ebbeeb1a7e2051887bff67db79721fdc6e69076719f3a98c63ec4924102c1b(
    resource: _aws_codeconnections_a8ecd32b.IConnectionRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9da098eb0ec1eadf1e6c8e2874d960931a10c48234cfa2f71152fac89bc28721(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78744497e1b5bae3f2ea20b9d3496e178855aef0e29d2de71777b026a6d27a1a(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__440f5e3662e5ab05ab71cf41aafae8bf45c3a11a457c7bbc13517a3eb9e7278e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d759fec9e0861542e9267cd70eacda49ebbb2a1399fb2f36364a2a01d38cdc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c6c22c4d5132fe518d2a74aed1b6d9c89f7a2fbb163195a459d8af8791cf1c9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec396e84dc4ee92669ed87aa685780cf9af74b974c8d0d7f12b0c1196dc17d6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd277a1214d747c2b8b1a0998909d0fe0edc54719c5d7b8ae3621585dbf60405(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac62d1262e0fc9d7647548096d4e83c0367271b1f1be70c2119c14ec99b3dde(
    *,
    connection_name: builtins.str,
    host_arn: typing.Optional[builtins.str] = None,
    provider_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955548f1a83434bfe589e9465d3ab38c3c5f90d595957f0eb3ef54787a04f285(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    provider_endpoint: builtins.str,
    provider_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnHost.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0492aff78c45a9849781a5145a2b63a75cedeb364faba0296cd5bfcdefa53e55(
    resource: _aws_codeconnections_a8ecd32b.IHostRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e09acbbff41515e4490dded19b0ddabbb1cdb04a48b03aceb6682ab76df622f7(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45b5f878984505d2aeba188062b1e8f8e1eca11e0724100a66dac60afca8216(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__452af0397c9fbd5f363dc2634e782d06ff8f2f0afccd9e8f0c46f65678743e14(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678966c1f3caebbcde15336278f21fc87bf5d68238732993317db86fb321ebff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5175881a75564bdfb981168592d63f0fcdbd1168ea713126172f952adf7fe746(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b3edf4c4c8471028dd998530b46a885509ab3141208eeb91011d9bae314610(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d888addd54ad753cc084483b45bf5d0a97682ff702b90d2a91c2ceaaadb625f2(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8184046a577db6ff901740449c6a521de0eda15f52c5465b0c80a37fb0a544f(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnHost.VpcConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9952b7aab3d4882aa0bf265afa825ea9b776d4a6956aea96ad2b585de9be50f5(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    tls_certificate: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f84ea6586678bf17fc941a6bb2712401c1fee06b478e44253c3551e1514b12c(
    *,
    name: builtins.str,
    provider_endpoint: builtins.str,
    provider_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnHost.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
