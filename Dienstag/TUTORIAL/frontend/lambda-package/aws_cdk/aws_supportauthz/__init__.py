r'''
# AWS::SupportAuthZ Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_supportauthz as supportauthz
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SupportAuthZ construct libraries](https://constructs.dev/search?q=supportauthz)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SupportAuthZ resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SupportAuthZ.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SupportAuthZ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SupportAuthZ.html).

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
    import aws_cdk.interfaces.aws_supportauthz as _aws_supportauthz_427c65b5
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_supportauthz_427c65b5 = _LazyImport("aws_cdk.interfaces.aws_supportauthz")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_supportauthz_427c65b5.ISupportPermitRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnSupportPermit(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_supportauthz.CfnSupportPermit",
):
    '''Resource Type definition for AWS::SupportAuthZ::SupportPermit.

    Represents a support permit that grants AWS support time-bounded access to one or more resources for a set of actions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportauthz-supportpermit.html
    :cloudformationResource: AWS::SupportAuthZ::SupportPermit
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_supportauthz as supportauthz
        
        # all_actions: Any
        # all_resources_in_region: Any
        
        cfn_support_permit = supportauthz.CfnSupportPermit(self, "MyCfnSupportPermit",
            name="name",
            permit=supportauthz.CfnSupportPermit.PermitProperty(
                actions=supportauthz.CfnSupportPermit.ActionSetProperty(
                    actions=["actions"],
                    all_actions=all_actions
                ),
                resources=supportauthz.CfnSupportPermit.ResourceSetProperty(
                    all_resources_in_region=all_resources_in_region,
                    resources=["resources"]
                ),
        
                # the properties below are optional
                conditions=[supportauthz.CfnSupportPermit.ConditionProperty(
                    allow_after="allowAfter",
                    allow_before="allowBefore"
                )]
            ),
            signing_key_info=supportauthz.CfnSupportPermit.SigningKeyInfoProperty(
                kms_key="kmsKey"
            ),
        
            # the properties below are optional
            description="description",
            support_case_display_id="supportCaseDisplayId",
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
        permit: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSupportPermit.PermitProperty", typing.Dict[builtins.str, typing.Any]]],
        signing_key_info: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSupportPermit.SigningKeyInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        support_case_display_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SupportAuthZ::SupportPermit``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the support permit.
        :param permit: The grant definition: which actions on which resources, optionally constrained by time conditions.
        :param signing_key_info: The signing key used by the permit. Exactly one key type must be provided.
        :param description: An optional description of the support permit.
        :param support_case_display_id: The support case display identifier associated with the permit. When provided, the permit is linked to the specified AWS Support case.
        :param tags: A list of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ec448e30162aa795bda6905724deae8fbaaf1cac28be1d52e07d5d3757b8cdb5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSupportPermitProps(
            name=name,
            permit=permit,
            signing_key_info=signing_key_info,
            description=description,
            support_case_display_id=support_case_display_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSupportPermit")
    @builtins.classmethod
    def arn_for_support_permit(
        cls,
        resource: "_aws_supportauthz_427c65b5.ISupportPermitRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fa4e06ac785572e67efb43098025fb8832591438cceafabf81ab88ed9ad74b41)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSupportPermit", [resource]))

    @jsii.member(jsii_name="isCfnSupportPermit")
    @builtins.classmethod
    def is_cfn_support_permit(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSupportPermit.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d3592b9a0e7cff50274e2edbb69df0b7425447c4eccc94a952af99aefb71aa97)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSupportPermit", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8e974922c098b3565f04612dba5fb672bd4d97f2bdf538d51a842fb8302e7729)
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
            type_hints = cached_type_hints(_typecheckingstub__3565f87a285aafe9df6c2de15ebf075c6a3d3ba84ff03e66032a70104c919334)
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
        '''The Amazon Resource Name (ARN) of the support permit.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the support permit was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrPermitId")
    def attr_permit_id(self) -> builtins.str:
        '''The service-generated identifier of the support permit (the resource segment of the ARN).

        :cloudformationAttribute: PermitId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPermitId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the support permit.

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
    @jsii.member(jsii_name="supportPermitRef")
    def support_permit_ref(self) -> "_aws_supportauthz_427c65b5.SupportPermitReference":
        '''A reference to a SupportPermit resource.'''
        return typing.cast("_aws_supportauthz_427c65b5.SupportPermitReference", jsii.get(self, "supportPermitRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the support permit.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3ecf34640baa88a0c688553f45ff85f6c9133336b5c104c2202bf41da43529d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="permit")
    def permit(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.PermitProperty"]:
        '''The grant definition: which actions on which resources, optionally constrained by time conditions.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.PermitProperty"], jsii.get(self, "permit"))

    @permit.setter
    def permit(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.PermitProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ca368feaa23a5a0edc68fd81bf11edc70525605a17855d5fe7c0b2e1b65100ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permit", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="signingKeyInfo")
    def signing_key_info(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.SigningKeyInfoProperty"]:
        '''The signing key used by the permit.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.SigningKeyInfoProperty"], jsii.get(self, "signingKeyInfo"))

    @signing_key_info.setter
    def signing_key_info(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.SigningKeyInfoProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6a29af1ed3320518500efc84f1c2364f599991ddd68cb2042bbc84d3babc93db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingKeyInfo", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the support permit.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__263f09655a8beee93ac084b1622ba49c4df91e847cc45110f5f5e3da93814915)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="supportCaseDisplayId")
    def support_case_display_id(self) -> typing.Optional[builtins.str]:
        '''The support case display identifier associated with the permit.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportCaseDisplayId"))

    @support_case_display_id.setter
    def support_case_display_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2b3b9494e41da98a35c532a93104f6e87bca622485af7449b900d4c8c2125008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportCaseDisplayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ccba66f00d9eed5f8ad911f379fa0c30c26196e0ac5eb502cfacd2275b4ff209)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_supportauthz.CfnSupportPermit.ActionSetProperty",
        jsii_struct_bases=[],
        name_mapping={"actions": "actions", "all_actions": "allActions"},
    )
    class ActionSetProperty:
        def __init__(
            self,
            *,
            actions: typing.Optional[typing.Sequence[builtins.str]] = None,
            all_actions: typing.Any = None,
        ) -> None:
            '''The set of actions a support permit grants.

            Exactly one of AllActions or Actions must be provided.

            :param actions: An explicit list of actions to grant.
            :param all_actions: Grants all actions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-actionset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_supportauthz as supportauthz
                
                # all_actions: Any
                
                action_set_property = supportauthz.CfnSupportPermit.ActionSetProperty(
                    actions=["actions"],
                    all_actions=all_actions
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6bba2d3b930cb14c1db885aad0df5da015c81d1c77f55da05848acae90a810c4)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument all_actions", value=all_actions, expected_type=type_hints["all_actions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if actions is not None:
                self._values["actions"] = actions
            if all_actions is not None:
                self._values["all_actions"] = all_actions

        @builtins.property
        def actions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An explicit list of actions to grant.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-actionset.html#cfn-supportauthz-supportpermit-actionset-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def all_actions(self) -> typing.Any:
            '''Grants all actions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-actionset.html#cfn-supportauthz-supportpermit-actionset-allactions
            '''
            result = self._values.get("all_actions")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_supportauthz.CfnSupportPermit.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"allow_after": "allowAfter", "allow_before": "allowBefore"},
    )
    class ConditionProperty:
        def __init__(
            self,
            *,
            allow_after: typing.Optional[builtins.str] = None,
            allow_before: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A time-bound condition controlling when the permit is active.

            Exactly one of AllowAfter or AllowBefore must be provided.

            :param allow_after: The permit is active only after this time.
            :param allow_before: The permit is active only before this time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-condition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_supportauthz as supportauthz
                
                condition_property = supportauthz.CfnSupportPermit.ConditionProperty(
                    allow_after="allowAfter",
                    allow_before="allowBefore"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__49f84aa3f3fb6d0acdec7462e05afd23e0ebd8d96a65da271fe44d67e42a0f4c)
                check_type(argname="argument allow_after", value=allow_after, expected_type=type_hints["allow_after"])
                check_type(argname="argument allow_before", value=allow_before, expected_type=type_hints["allow_before"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_after is not None:
                self._values["allow_after"] = allow_after
            if allow_before is not None:
                self._values["allow_before"] = allow_before

        @builtins.property
        def allow_after(self) -> typing.Optional[builtins.str]:
            '''The permit is active only after this time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-condition.html#cfn-supportauthz-supportpermit-condition-allowafter
            '''
            result = self._values.get("allow_after")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def allow_before(self) -> typing.Optional[builtins.str]:
            '''The permit is active only before this time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-condition.html#cfn-supportauthz-supportpermit-condition-allowbefore
            '''
            result = self._values.get("allow_before")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_supportauthz.CfnSupportPermit.PermitProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "resources": "resources",
            "conditions": "conditions",
        },
    )
    class PermitProperty:
        def __init__(
            self,
            *,
            actions: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSupportPermit.ActionSetProperty", typing.Dict[builtins.str, typing.Any]]],
            resources: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSupportPermit.ResourceSetProperty", typing.Dict[builtins.str, typing.Any]]],
            conditions: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSupportPermit.ConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The grant definition: which actions on which resources, optionally constrained by time conditions.

            :param actions: The set of actions a support permit grants. Exactly one of AllActions or Actions must be provided.
            :param resources: The set of resources a support permit applies to. Exactly one of AllResourcesInRegion or Resources must be provided.
            :param conditions: Optional time-bound conditions (at most two).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-permit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_supportauthz as supportauthz
                
                # all_actions: Any
                # all_resources_in_region: Any
                
                permit_property = supportauthz.CfnSupportPermit.PermitProperty(
                    actions=supportauthz.CfnSupportPermit.ActionSetProperty(
                        actions=["actions"],
                        all_actions=all_actions
                    ),
                    resources=supportauthz.CfnSupportPermit.ResourceSetProperty(
                        all_resources_in_region=all_resources_in_region,
                        resources=["resources"]
                    ),
                
                    # the properties below are optional
                    conditions=[supportauthz.CfnSupportPermit.ConditionProperty(
                        allow_after="allowAfter",
                        allow_before="allowBefore"
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__07fc0c74c05a1702ef2558f2d8fceee5530e975a5eccfcb387a4ff647a19e727)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "actions": actions,
                "resources": resources,
            }
            if conditions is not None:
                self._values["conditions"] = conditions

        @builtins.property
        def actions(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.ActionSetProperty"]:
            '''The set of actions a support permit grants.

            Exactly one of AllActions or Actions must be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-permit.html#cfn-supportauthz-supportpermit-permit-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.ActionSetProperty"], result)

        @builtins.property
        def resources(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.ResourceSetProperty"]:
            '''The set of resources a support permit applies to.

            Exactly one of AllResourcesInRegion or Resources must be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-permit.html#cfn-supportauthz-supportpermit-permit-resources
            '''
            result = self._values.get("resources")
            assert result is not None, "Required property 'resources' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.ResourceSetProperty"], result)

        @builtins.property
        def conditions(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.ConditionProperty"]]]]:
            '''Optional time-bound conditions (at most two).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-permit.html#cfn-supportauthz-supportpermit-permit-conditions
            '''
            result = self._values.get("conditions")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.ConditionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PermitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_supportauthz.CfnSupportPermit.ResourceSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_resources_in_region": "allResourcesInRegion",
            "resources": "resources",
        },
    )
    class ResourceSetProperty:
        def __init__(
            self,
            *,
            all_resources_in_region: typing.Any = None,
            resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The set of resources a support permit applies to.

            Exactly one of AllResourcesInRegion or Resources must be provided.

            :param all_resources_in_region: Applies to all resources in the region.
            :param resources: An explicit list of resource ARNs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-resourceset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_supportauthz as supportauthz
                
                # all_resources_in_region: Any
                
                resource_set_property = supportauthz.CfnSupportPermit.ResourceSetProperty(
                    all_resources_in_region=all_resources_in_region,
                    resources=["resources"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1fb412672212cad2a6fee22010f36da7655de7d4b3fc49607dcc07c9a96bf26a)
                check_type(argname="argument all_resources_in_region", value=all_resources_in_region, expected_type=type_hints["all_resources_in_region"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if all_resources_in_region is not None:
                self._values["all_resources_in_region"] = all_resources_in_region
            if resources is not None:
                self._values["resources"] = resources

        @builtins.property
        def all_resources_in_region(self) -> typing.Any:
            '''Applies to all resources in the region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-resourceset.html#cfn-supportauthz-supportpermit-resourceset-allresourcesinregion
            '''
            result = self._values.get("all_resources_in_region")
            return typing.cast(typing.Any, result)

        @builtins.property
        def resources(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An explicit list of resource ARNs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-resourceset.html#cfn-supportauthz-supportpermit-resourceset-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_supportauthz.CfnSupportPermit.SigningKeyInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key": "kmsKey"},
    )
    class SigningKeyInfoProperty:
        def __init__(self, *, kms_key: builtins.str) -> None:
            '''The signing key used by the permit.

            Exactly one key type must be provided.

            :param kms_key: The ARN of the KMS key used to sign permit grants.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-signingkeyinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_supportauthz as supportauthz
                
                signing_key_info_property = supportauthz.CfnSupportPermit.SigningKeyInfoProperty(
                    kms_key="kmsKey"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__feb6393cdb2caec24090a62d6a925deb7c71535387ea697b5ca080f22e9f892b)
                check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kms_key": kms_key,
            }

        @builtins.property
        def kms_key(self) -> builtins.str:
            '''The ARN of the KMS key used to sign permit grants.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-supportauthz-supportpermit-signingkeyinfo.html#cfn-supportauthz-supportpermit-signingkeyinfo-kmskey
            '''
            result = self._values.get("kms_key")
            assert result is not None, "Required property 'kms_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SigningKeyInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_supportauthz.CfnSupportPermitProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "permit": "permit",
        "signing_key_info": "signingKeyInfo",
        "description": "description",
        "support_case_display_id": "supportCaseDisplayId",
        "tags": "tags",
    },
)
class CfnSupportPermitProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        permit: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSupportPermit.PermitProperty", typing.Dict[builtins.str, typing.Any]]],
        signing_key_info: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSupportPermit.SigningKeyInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        support_case_display_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSupportPermit``.

        :param name: The name of the support permit.
        :param permit: The grant definition: which actions on which resources, optionally constrained by time conditions.
        :param signing_key_info: The signing key used by the permit. Exactly one key type must be provided.
        :param description: An optional description of the support permit.
        :param support_case_display_id: The support case display identifier associated with the permit. When provided, the permit is linked to the specified AWS Support case.
        :param tags: A list of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportauthz-supportpermit.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_supportauthz as supportauthz
            
            # all_actions: Any
            # all_resources_in_region: Any
            
            cfn_support_permit_props = supportauthz.CfnSupportPermitProps(
                name="name",
                permit=supportauthz.CfnSupportPermit.PermitProperty(
                    actions=supportauthz.CfnSupportPermit.ActionSetProperty(
                        actions=["actions"],
                        all_actions=all_actions
                    ),
                    resources=supportauthz.CfnSupportPermit.ResourceSetProperty(
                        all_resources_in_region=all_resources_in_region,
                        resources=["resources"]
                    ),
            
                    # the properties below are optional
                    conditions=[supportauthz.CfnSupportPermit.ConditionProperty(
                        allow_after="allowAfter",
                        allow_before="allowBefore"
                    )]
                ),
                signing_key_info=supportauthz.CfnSupportPermit.SigningKeyInfoProperty(
                    kms_key="kmsKey"
                ),
            
                # the properties below are optional
                description="description",
                support_case_display_id="supportCaseDisplayId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9fb940014554d0ff5f05059787c9ec691d31108f1f02811321d760882ab10652)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument permit", value=permit, expected_type=type_hints["permit"])
            check_type(argname="argument signing_key_info", value=signing_key_info, expected_type=type_hints["signing_key_info"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument support_case_display_id", value=support_case_display_id, expected_type=type_hints["support_case_display_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "permit": permit,
            "signing_key_info": signing_key_info,
        }
        if description is not None:
            self._values["description"] = description
        if support_case_display_id is not None:
            self._values["support_case_display_id"] = support_case_display_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the support permit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportauthz-supportpermit.html#cfn-supportauthz-supportpermit-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permit(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.PermitProperty"]:
        '''The grant definition: which actions on which resources, optionally constrained by time conditions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportauthz-supportpermit.html#cfn-supportauthz-supportpermit-permit
        '''
        result = self._values.get("permit")
        assert result is not None, "Required property 'permit' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.PermitProperty"], result)

    @builtins.property
    def signing_key_info(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.SigningKeyInfoProperty"]:
        '''The signing key used by the permit.

        Exactly one key type must be provided.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportauthz-supportpermit.html#cfn-supportauthz-supportpermit-signingkeyinfo
        '''
        result = self._values.get("signing_key_info")
        assert result is not None, "Required property 'signing_key_info' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSupportPermit.SigningKeyInfoProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the support permit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportauthz-supportpermit.html#cfn-supportauthz-supportpermit-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def support_case_display_id(self) -> typing.Optional[builtins.str]:
        '''The support case display identifier associated with the permit.

        When provided, the permit is linked to the specified AWS Support case.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportauthz-supportpermit.html#cfn-supportauthz-supportpermit-supportcasedisplayid
        '''
        result = self._values.get("support_case_display_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportauthz-supportpermit.html#cfn-supportauthz-supportpermit-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSupportPermitProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSupportPermit",
    "CfnSupportPermitProps",
]

publication.publish()

def _typecheckingstub__ec448e30162aa795bda6905724deae8fbaaf1cac28be1d52e07d5d3757b8cdb5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    permit: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSupportPermit.PermitProperty, typing.Dict[builtins.str, typing.Any]]],
    signing_key_info: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSupportPermit.SigningKeyInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    support_case_display_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa4e06ac785572e67efb43098025fb8832591438cceafabf81ab88ed9ad74b41(
    resource: _aws_supportauthz_427c65b5.ISupportPermitRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3592b9a0e7cff50274e2edbb69df0b7425447c4eccc94a952af99aefb71aa97(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e974922c098b3565f04612dba5fb672bd4d97f2bdf538d51a842fb8302e7729(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3565f87a285aafe9df6c2de15ebf075c6a3d3ba84ff03e66032a70104c919334(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ecf34640baa88a0c688553f45ff85f6c9133336b5c104c2202bf41da43529d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca368feaa23a5a0edc68fd81bf11edc70525605a17855d5fe7c0b2e1b65100ff(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSupportPermit.PermitProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a29af1ed3320518500efc84f1c2364f599991ddd68cb2042bbc84d3babc93db(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSupportPermit.SigningKeyInfoProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__263f09655a8beee93ac084b1622ba49c4df91e847cc45110f5f5e3da93814915(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3b9494e41da98a35c532a93104f6e87bca622485af7449b900d4c8c2125008(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccba66f00d9eed5f8ad911f379fa0c30c26196e0ac5eb502cfacd2275b4ff209(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bba2d3b930cb14c1db885aad0df5da015c81d1c77f55da05848acae90a810c4(
    *,
    actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    all_actions: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49f84aa3f3fb6d0acdec7462e05afd23e0ebd8d96a65da271fe44d67e42a0f4c(
    *,
    allow_after: typing.Optional[builtins.str] = None,
    allow_before: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fc0c74c05a1702ef2558f2d8fceee5530e975a5eccfcb387a4ff647a19e727(
    *,
    actions: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSupportPermit.ActionSetProperty, typing.Dict[builtins.str, typing.Any]]],
    resources: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSupportPermit.ResourceSetProperty, typing.Dict[builtins.str, typing.Any]]],
    conditions: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSupportPermit.ConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fb412672212cad2a6fee22010f36da7655de7d4b3fc49607dcc07c9a96bf26a(
    *,
    all_resources_in_region: typing.Any = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb6393cdb2caec24090a62d6a925deb7c71535387ea697b5ca080f22e9f892b(
    *,
    kms_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb940014554d0ff5f05059787c9ec691d31108f1f02811321d760882ab10652(
    *,
    name: builtins.str,
    permit: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSupportPermit.PermitProperty, typing.Dict[builtins.str, typing.Any]]],
    signing_key_info: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSupportPermit.SigningKeyInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    support_case_display_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
