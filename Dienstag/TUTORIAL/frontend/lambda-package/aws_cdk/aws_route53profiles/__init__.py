r'''
# AWS::Route53Profiles Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_route53profiles as route53profiles
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Route53Profiles construct libraries](https://constructs.dev/search?q=route53profiles)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Route53Profiles resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53Profiles.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Route53Profiles](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53Profiles.html).

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
    import aws_cdk.interfaces.aws_route53profiles as _aws_route53profiles_a8d26590
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_route53profiles_a8d26590 = _LazyImport("aws_cdk.interfaces.aws_route53profiles")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_route53profiles_a8d26590.IProfileRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnProfile(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53profiles.CfnProfile",
):
    '''A complex type that includes settings for a Route 53 Profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profile.html
    :cloudformationResource: AWS::Route53Profiles::Profile
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53profiles as route53profiles
        
        cfn_profile = route53profiles.CfnProfile(self, "MyCfnProfile",
            name="name",
        
            # the properties below are optional
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
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Profiles::Profile``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Name of the Profile.
        :param tags: A list of the tag keys and values that you want to associate with the profile.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a4c1f071f0e4e35c37cfd1564e9529ed7a07645071498a571c8b23339ff2d0f7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfileProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForProfile")
    @builtins.classmethod
    def arn_for_profile(
        cls,
        resource: "_aws_route53profiles_a8d26590.IProfileRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__52d54ba2d1176fe354d89d52b39e659b4317922ef40399e50a28ef571c08a11a)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForProfile", [resource]))

    @jsii.member(jsii_name="isCfnProfile")
    @builtins.classmethod
    def is_cfn_profile(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnProfile.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f240c456b0ef89337a45530fe5186e008465ad9d2ba878dbe60754c1a2fdd6f3)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnProfile", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d5dcbb042b2caccabe90d7a337f5dc8312ca20d29d0852b9ab08eb0a6f17ff01)
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
            type_hints = cached_type_hints(_typecheckingstub__bb8df6de20d928e5402eda0ff608d08e265257e361ef9679c54c70c7280b0fbd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Profile.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrClientToken")
    def attr_client_token(self) -> builtins.str:
        '''The ``ClientToken`` value that was assigned when the Profile was created.

        :cloudformationAttribute: ClientToken
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClientToken"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''ID of the Profile.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrShareStatus")
    def attr_share_status(self) -> builtins.str:
        '''Sharing status for the Profile.

        :cloudformationAttribute: ShareStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrShareStatus"))

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
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "_aws_route53profiles_a8d26590.ProfileReference":
        '''A reference to a Profile resource.'''
        return typing.cast("_aws_route53profiles_a8d26590.ProfileReference", jsii.get(self, "profileRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the Profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__60c46cc6c474c2912204fbc2c30bcdffdbbdb2e3c9dff0f7fa71ef743ec74297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of the tag keys and values that you want to associate with the profile.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1c969507a00c93e8a8b7637d952f3cf0cff3a4955296198e407c611f9eebfc0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_route53profiles_a8d26590.IProfileAssociationRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnProfileAssociation(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53profiles.CfnProfileAssociation",
):
    '''An association between a Route 53 Profile and a VPC.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileassociation.html
    :cloudformationResource: AWS::Route53Profiles::ProfileAssociation
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53profiles as route53profiles
        
        cfn_profile_association = route53profiles.CfnProfileAssociation(self, "MyCfnProfileAssociation",
            name="name",
            profile_id="profileId",
            resource_id="resourceId",
        
            # the properties below are optional
            arn="arn",
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
        name: builtins.str,
        profile_id: builtins.str,
        resource_id: builtins.str,
        arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Profiles::ProfileAssociation``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Name of the Profile association.
        :param profile_id: ID of the Profile. Update to this property requires update to the ``ResourceId`` property as well, because you can only associate one Profile per VPC. For more information, see `Route 53 Profiles <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html>`_ .
        :param resource_id: The ID of the VPC.
        :param arn: The Amazon Resource Name (ARN) of the profile association to a VPC.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0f887f11535feca537003f68699ddb6bbfe324f08f570e51e9d9c9660153c8b3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfileAssociationProps(
            name=name,
            profile_id=profile_id,
            resource_id=resource_id,
            arn=arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForProfileAssociation")
    @builtins.classmethod
    def arn_for_profile_association(
        cls,
        resource: "_aws_route53profiles_a8d26590.IProfileAssociationRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__938910c4b8db6f31cc8d5214d7502e776878f36ee324f42f6c2cba85052d2f1c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForProfileAssociation", [resource]))

    @jsii.member(jsii_name="isCfnProfileAssociation")
    @builtins.classmethod
    def is_cfn_profile_association(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnProfileAssociation.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2e798a18b5db3cbff5dfcac2850c00796298044699b13f59565e116a24253fb6)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnProfileAssociation", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a944f9ef0cfcf0fedb5df0ffe2f7bae6eec8447235dc0f66f3dfa3b25e60e3b9)
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
            type_hints = cached_type_hints(_typecheckingstub__50ffe6397875ccdece80bc20c899a7fcc00061247e1f0ac593e27500d9567541)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''ID of the Profile association.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="profileAssociationRef")
    def profile_association_ref(
        self,
    ) -> "_aws_route53profiles_a8d26590.ProfileAssociationReference":
        '''A reference to a ProfileAssociation resource.'''
        return typing.cast("_aws_route53profiles_a8d26590.ProfileAssociationReference", jsii.get(self, "profileAssociationRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the Profile association.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a511bbd7a0cc2d9194919b70e7bd0cfbef6d6560cf67f6c9eab367017a85e4e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        '''ID of the Profile.'''
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a560cfea07af2b59f29df43a85e3e9e48a2195cff87eec5bf9d7e3269fdc21a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        '''The ID of the VPC.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b16839b4164b84f692a7f82a0354b6f96cfb9c31b01ef9fadf50bb166bc7aff8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the profile association to a VPC.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3529d03e90e5a43e1281f5b497a4dd92b53f8b81d07a3ae7e158075cd7c2cdd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__931a5eb93acc9ea331b6c7a804aa50f9c8645e820b985c1e8c3b0338897b0758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53profiles.CfnProfileAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "profile_id": "profileId",
        "resource_id": "resourceId",
        "arn": "arn",
        "tags": "tags",
    },
)
class CfnProfileAssociationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        profile_id: builtins.str,
        resource_id: builtins.str,
        arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfileAssociation``.

        :param name: Name of the Profile association.
        :param profile_id: ID of the Profile. Update to this property requires update to the ``ResourceId`` property as well, because you can only associate one Profile per VPC. For more information, see `Route 53 Profiles <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html>`_ .
        :param resource_id: The ID of the VPC.
        :param arn: The Amazon Resource Name (ARN) of the profile association to a VPC.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53profiles as route53profiles
            
            cfn_profile_association_props = route53profiles.CfnProfileAssociationProps(
                name="name",
                profile_id="profileId",
                resource_id="resourceId",
            
                # the properties below are optional
                arn="arn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6a57a1fdd8721b32a07e564698e95375e4dc721f518a60463fd94e82877d73cf)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "profile_id": profile_id,
            "resource_id": resource_id,
        }
        if arn is not None:
            self._values["arn"] = arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the Profile association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileassociation.html#cfn-route53profiles-profileassociation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''ID of the Profile.

        Update to this property requires update to the ``ResourceId`` property as well, because you can only associate one Profile per VPC. For more information, see `Route 53 Profiles <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileassociation.html#cfn-route53profiles-profileassociation-profileid
        '''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The ID of the VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileassociation.html#cfn-route53profiles-profileassociation-resourceid
        '''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the profile association to a VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileassociation.html#cfn-route53profiles-profileassociation-arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileassociation.html#cfn-route53profiles-profileassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfileAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53profiles.CfnProfileProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnProfileProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfile``.

        :param name: Name of the Profile.
        :param tags: A list of the tag keys and values that you want to associate with the profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profile.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53profiles as route53profiles
            
            cfn_profile_props = route53profiles.CfnProfileProps(
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e302a4191c8b64aaaf85fdd1a3f3fb3c5393f25dfb085d717713b0dec0579b17)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the Profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profile.html#cfn-route53profiles-profile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of the tag keys and values that you want to associate with the profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profile.html#cfn-route53profiles-profile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_route53profiles_a8d26590.IProfileResourceAssociationRef)
class CfnProfileResourceAssociation(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53profiles.CfnProfileResourceAssociation",
):
    '''The association between a Route 53 Profile and resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileresourceassociation.html
    :cloudformationResource: AWS::Route53Profiles::ProfileResourceAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53profiles as route53profiles
        
        cfn_profile_resource_association = route53profiles.CfnProfileResourceAssociation(self, "MyCfnProfileResourceAssociation",
            name="name",
            profile_id="profileId",
            resource_arn="resourceArn",
        
            # the properties below are optional
            resource_properties="resourceProperties"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        profile_id: builtins.str,
        resource_arn: builtins.str,
        resource_properties: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Profiles::ProfileResourceAssociation``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Name of the Profile resource association.
        :param profile_id: Profile ID of the Profile that the resources are associated with.
        :param resource_arn: The Amazon Resource Name (ARN) of the resource association.
        :param resource_properties: If the DNS resource is a DNS Firewall rule group, this indicates the priority.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__654d8dd5618d66fa0625633f46d77099c9357744b521399d4e1e34d078669be8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfileResourceAssociationProps(
            name=name,
            profile_id=profile_id,
            resource_arn=resource_arn,
            resource_properties=resource_properties,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnProfileResourceAssociation")
    @builtins.classmethod
    def is_cfn_profile_resource_association(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnProfileResourceAssociation.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__37fcb433f8de289098c361613c249270f0dd465cfab322e101f233a531d453b1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnProfileResourceAssociation", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3152dee296caf378c70d9e7a562602ce5afefc68fd0990082249d596614cc5ed)
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
            type_hints = cached_type_hints(_typecheckingstub__17e0106dd2d03ba5f1e680218ffab0ec9ddb5f8f6e58d8e7ff7c75620d1e7f4e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''ID of the Profile resource association.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceType")
    def attr_resource_type(self) -> builtins.str:
        '''Resource type, such as a private hosted zone, interface VPC endpoint, or DNS Firewall rule group.

        :cloudformationAttribute: ResourceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="profileResourceAssociationRef")
    def profile_resource_association_ref(
        self,
    ) -> "_aws_route53profiles_a8d26590.ProfileResourceAssociationReference":
        '''A reference to a ProfileResourceAssociation resource.'''
        return typing.cast("_aws_route53profiles_a8d26590.ProfileResourceAssociationReference", jsii.get(self, "profileResourceAssociationRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the Profile resource association.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ca42427a0339ee0fa3a5e112a6fde9357eab47e700da806e76bb149f9f48a8b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        '''Profile ID of the Profile that the resources are associated with.'''
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__de62b5427237d19fe1dafa8c04952f10c662591ae4d715acb190b5db908ce662)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource association.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__75c7389edcf1d691cba068236e58e8d39cb4b56660cd71d39a86bbd9b2656087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceProperties")
    def resource_properties(self) -> typing.Optional[builtins.str]:
        '''If the DNS resource is a DNS Firewall rule group, this indicates the priority.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceProperties"))

    @resource_properties.setter
    def resource_properties(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ef034a5fa94b59c1205f90a0df217e7fe4b64926828487662c4de8f7785c165e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceProperties", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53profiles.CfnProfileResourceAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "profile_id": "profileId",
        "resource_arn": "resourceArn",
        "resource_properties": "resourceProperties",
    },
)
class CfnProfileResourceAssociationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        profile_id: builtins.str,
        resource_arn: builtins.str,
        resource_properties: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfileResourceAssociation``.

        :param name: Name of the Profile resource association.
        :param profile_id: Profile ID of the Profile that the resources are associated with.
        :param resource_arn: The Amazon Resource Name (ARN) of the resource association.
        :param resource_properties: If the DNS resource is a DNS Firewall rule group, this indicates the priority.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileresourceassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53profiles as route53profiles
            
            cfn_profile_resource_association_props = route53profiles.CfnProfileResourceAssociationProps(
                name="name",
                profile_id="profileId",
                resource_arn="resourceArn",
            
                # the properties below are optional
                resource_properties="resourceProperties"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5dc49398d34bd8989f72c7417ca7f6a94e871e24c58ac82a6f3fc4e5df4de248)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument resource_properties", value=resource_properties, expected_type=type_hints["resource_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "profile_id": profile_id,
            "resource_arn": resource_arn,
        }
        if resource_properties is not None:
            self._values["resource_properties"] = resource_properties

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the Profile resource association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileresourceassociation.html#cfn-route53profiles-profileresourceassociation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''Profile ID of the Profile that the resources are associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileresourceassociation.html#cfn-route53profiles-profileresourceassociation-profileid
        '''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileresourceassociation.html#cfn-route53profiles-profileresourceassociation-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_properties(self) -> typing.Optional[builtins.str]:
        '''If the DNS resource is a DNS Firewall rule group, this indicates the priority.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53profiles-profileresourceassociation.html#cfn-route53profiles-profileresourceassociation-resourceproperties
        '''
        result = self._values.get("resource_properties")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfileResourceAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnProfile",
    "CfnProfileAssociation",
    "CfnProfileAssociationProps",
    "CfnProfileProps",
    "CfnProfileResourceAssociation",
    "CfnProfileResourceAssociationProps",
]

publication.publish()

def _typecheckingstub__a4c1f071f0e4e35c37cfd1564e9529ed7a07645071498a571c8b23339ff2d0f7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52d54ba2d1176fe354d89d52b39e659b4317922ef40399e50a28ef571c08a11a(
    resource: _aws_route53profiles_a8d26590.IProfileRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f240c456b0ef89337a45530fe5186e008465ad9d2ba878dbe60754c1a2fdd6f3(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5dcbb042b2caccabe90d7a337f5dc8312ca20d29d0852b9ab08eb0a6f17ff01(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb8df6de20d928e5402eda0ff608d08e265257e361ef9679c54c70c7280b0fbd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60c46cc6c474c2912204fbc2c30bcdffdbbdb2e3c9dff0f7fa71ef743ec74297(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c969507a00c93e8a8b7637d952f3cf0cff3a4955296198e407c611f9eebfc0c(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f887f11535feca537003f68699ddb6bbfe324f08f570e51e9d9c9660153c8b3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    profile_id: builtins.str,
    resource_id: builtins.str,
    arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__938910c4b8db6f31cc8d5214d7502e776878f36ee324f42f6c2cba85052d2f1c(
    resource: _aws_route53profiles_a8d26590.IProfileAssociationRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e798a18b5db3cbff5dfcac2850c00796298044699b13f59565e116a24253fb6(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a944f9ef0cfcf0fedb5df0ffe2f7bae6eec8447235dc0f66f3dfa3b25e60e3b9(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ffe6397875ccdece80bc20c899a7fcc00061247e1f0ac593e27500d9567541(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a511bbd7a0cc2d9194919b70e7bd0cfbef6d6560cf67f6c9eab367017a85e4e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a560cfea07af2b59f29df43a85e3e9e48a2195cff87eec5bf9d7e3269fdc21a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b16839b4164b84f692a7f82a0354b6f96cfb9c31b01ef9fadf50bb166bc7aff8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3529d03e90e5a43e1281f5b497a4dd92b53f8b81d07a3ae7e158075cd7c2cdd6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931a5eb93acc9ea331b6c7a804aa50f9c8645e820b985c1e8c3b0338897b0758(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a57a1fdd8721b32a07e564698e95375e4dc721f518a60463fd94e82877d73cf(
    *,
    name: builtins.str,
    profile_id: builtins.str,
    resource_id: builtins.str,
    arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e302a4191c8b64aaaf85fdd1a3f3fb3c5393f25dfb085d717713b0dec0579b17(
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__654d8dd5618d66fa0625633f46d77099c9357744b521399d4e1e34d078669be8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    profile_id: builtins.str,
    resource_arn: builtins.str,
    resource_properties: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37fcb433f8de289098c361613c249270f0dd465cfab322e101f233a531d453b1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3152dee296caf378c70d9e7a562602ce5afefc68fd0990082249d596614cc5ed(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17e0106dd2d03ba5f1e680218ffab0ec9ddb5f8f6e58d8e7ff7c75620d1e7f4e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca42427a0339ee0fa3a5e112a6fde9357eab47e700da806e76bb149f9f48a8b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de62b5427237d19fe1dafa8c04952f10c662591ae4d715acb190b5db908ce662(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75c7389edcf1d691cba068236e58e8d39cb4b56660cd71d39a86bbd9b2656087(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef034a5fa94b59c1205f90a0df217e7fe4b64926828487662c4de8f7785c165e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc49398d34bd8989f72c7417ca7f6a94e871e24c58ac82a6f3fc4e5df4de248(
    *,
    name: builtins.str,
    profile_id: builtins.str,
    resource_arn: builtins.str,
    resource_properties: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
