r'''
# AWS::AccountAccess Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_accountaccess as accountaccess
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AccountAccess construct libraries](https://constructs.dev/search?q=accountaccess)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AccountAccess resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AccountAccess.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AccountAccess](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AccountAccess.html).

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
    import aws_cdk.interfaces.aws_accountaccess as _aws_accountaccess_faac6759
    import constructs as _constructs_77d1e7e8
else:

    _aws_accountaccess_faac6759 = _LazyImport("aws_cdk.interfaces.aws_accountaccess")
    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_accountaccess_faac6759.IApplicationRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnApplication(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_accountaccess.CfnApplication",
):
    '''Resource Type definition for AWS::AccountAccess::Application specifying an application for account access.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accountaccess-application.html
    :cloudformationResource: AWS::AccountAccess::Application
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_accountaccess as accountaccess
        
        cfn_application = accountaccess.CfnApplication(self, "MyCfnApplication",
            identity_source=accountaccess.CfnApplication.IdentitySourceProperty(
                identity_center=accountaccess.CfnApplication.IdentityCenterProperty(
                    instance_arn="instanceArn",
        
                    # the properties below are optional
                    application_arn="applicationArn"
                )
            ),
        
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
        identity_source: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnApplication.IdentitySourceProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AccountAccess::Application``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param identity_source: 
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__73f8306cb0446154a656b9352a94fa609e62d6f4fea69075d1eb8d89c3ac4a14)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(identity_source=identity_source, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForApplication")
    @builtins.classmethod
    def arn_for_application(
        cls,
        resource: "_aws_accountaccess_faac6759.IApplicationRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a4bdb7effa46d80e5f80e73ae010a2532e4ef859c788d9d48d059f7e97a79841)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForApplication", [resource]))

    @jsii.member(jsii_name="isCfnApplication")
    @builtins.classmethod
    def is_cfn_application(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnApplication.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1493a2fb28c7dd43c0e890e1ae1256ccaf4db6be6bcc1c561a541531e027cf7e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnApplication", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__49270eda86db2677290e426f6aba06bfe38acc4345aa166d53e9904885513abf)
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
            type_hints = cached_type_hints(_typecheckingstub__55bc264e005a4e321d459426a9a4868e61c16fa9ad72718b057e7530150a58e5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "_aws_accountaccess_faac6759.ApplicationReference":
        '''A reference to a Application resource.'''
        return typing.cast("_aws_accountaccess_faac6759.ApplicationReference", jsii.get(self, "applicationRef"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationArn")
    def attr_application_arn(self) -> builtins.str:
        '''The ARN of the application.

        :cloudformationAttribute: ApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the application was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentitySourceIdentityCenterApplicationArn")
    def attr_identity_source_identity_center_application_arn(self) -> builtins.str:
        '''The ARN of the associated Identity Center application.

        :cloudformationAttribute: IdentitySource.IdentityCenter.ApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentitySourceIdentityCenterApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the application.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTenantId")
    def attr_tenant_id(self) -> builtins.str:
        '''The tenant ID of the application.

        :cloudformationAttribute: TenantId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTenantId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the application was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="identitySource")
    def identity_source(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnApplication.IdentitySourceProperty"]:
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnApplication.IdentitySourceProperty"], jsii.get(self, "identitySource"))

    @identity_source.setter
    def identity_source(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnApplication.IdentitySourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__88f3ebd2c52381656a5da764f2e0c95fe3d92356f1f4701aa43d1258221ca4fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identitySource", value) # pyright: ignore[reportArgumentType]

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
            type_hints = cached_type_hints(_typecheckingstub__b391672f08db62f459bf7d90ac7d5eded75fcc1909fb440c1773742b0486e52a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accountaccess.CfnApplication.IdentityCenterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_arn": "instanceArn",
            "application_arn": "applicationArn",
        },
    )
    class IdentityCenterProperty:
        def __init__(
            self,
            *,
            instance_arn: builtins.str,
            application_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_arn: The ARN of the Identity Center instance.
            :param application_arn: The ARN of the associated Identity Center application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-application-identitycenter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accountaccess as accountaccess
                
                identity_center_property = accountaccess.CfnApplication.IdentityCenterProperty(
                    instance_arn="instanceArn",
                
                    # the properties below are optional
                    application_arn="applicationArn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__7c483dea091bb4d7c572e4950789ba596ced54cb8784fec4ea10586b9abf2338)
                check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
                check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_arn": instance_arn,
            }
            if application_arn is not None:
                self._values["application_arn"] = application_arn

        @builtins.property
        def instance_arn(self) -> builtins.str:
            '''The ARN of the Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-application-identitycenter.html#cfn-accountaccess-application-identitycenter-instancearn
            '''
            result = self._values.get("instance_arn")
            assert result is not None, "Required property 'instance_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def application_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the associated Identity Center application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-application-identitycenter.html#cfn-accountaccess-application-identitycenter-applicationarn
            '''
            result = self._values.get("application_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityCenterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accountaccess.CfnApplication.IdentitySourceProperty",
        jsii_struct_bases=[],
        name_mapping={"identity_center": "identityCenter"},
    )
    class IdentitySourceProperty:
        def __init__(
            self,
            *,
            identity_center: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnApplication.IdentityCenterProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param identity_center: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-application-identitysource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accountaccess as accountaccess
                
                identity_source_property = accountaccess.CfnApplication.IdentitySourceProperty(
                    identity_center=accountaccess.CfnApplication.IdentityCenterProperty(
                        instance_arn="instanceArn",
                
                        # the properties below are optional
                        application_arn="applicationArn"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__319b031310b3b581332f1f5f92378bdffd6e03f475aebf0a06cf36ba3ada76e7)
                check_type(argname="argument identity_center", value=identity_center, expected_type=type_hints["identity_center"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "identity_center": identity_center,
            }

        @builtins.property
        def identity_center(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnApplication.IdentityCenterProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-application-identitysource.html#cfn-accountaccess-application-identitysource-identitycenter
            '''
            result = self._values.get("identity_center")
            assert result is not None, "Required property 'identity_center' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnApplication.IdentityCenterProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentitySourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_accountaccess.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={"identity_source": "identitySource", "tags": "tags"},
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        identity_source: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnApplication.IdentitySourceProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param identity_source: 
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accountaccess-application.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_accountaccess as accountaccess
            
            cfn_application_props = accountaccess.CfnApplicationProps(
                identity_source=accountaccess.CfnApplication.IdentitySourceProperty(
                    identity_center=accountaccess.CfnApplication.IdentityCenterProperty(
                        instance_arn="instanceArn",
            
                        # the properties below are optional
                        application_arn="applicationArn"
                    )
                ),
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8ad46efd33b0a77c38cead74dbbab11994a5410435cf1e918cb7ffc03353a5b1)
            check_type(argname="argument identity_source", value=identity_source, expected_type=type_hints["identity_source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_source": identity_source,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def identity_source(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnApplication.IdentitySourceProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accountaccess-application.html#cfn-accountaccess-application-identitysource
        '''
        result = self._values.get("identity_source")
        assert result is not None, "Required property 'identity_source' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnApplication.IdentitySourceProperty"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accountaccess-application.html#cfn-accountaccess-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_accountaccess_faac6759.IEntitlementRef)
class CfnEntitlement(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_accountaccess.CfnEntitlement",
):
    '''Resource Type definition for AWS::AccountAccess::Entitlement specifying an entitlement for account access.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accountaccess-entitlement.html
    :cloudformationResource: AWS::AccountAccess::Entitlement
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_accountaccess as accountaccess
        
        cfn_entitlement = accountaccess.CfnEntitlement(self, "MyCfnEntitlement",
            application_arn="applicationArn",
            entitlement=accountaccess.CfnEntitlement.EntitlementProperty(
                principal_role=accountaccess.CfnEntitlement.PrincipalRoleEntitlementProperty(
                    principal=accountaccess.CfnEntitlement.PrincipalProperty(
                        identity_center=accountaccess.CfnEntitlement.IdentityCenterPrincipalProperty(
                            group_id="groupId",
                            user_id="userId"
                        )
                    ),
                    role_arn="roleArn",
        
                    # the properties below are optional
                    account="account"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        application_arn: builtins.str,
        entitlement: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEntitlement.EntitlementProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::AccountAccess::Entitlement``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_arn: The ARN of the application.
        :param entitlement: 
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7abc411fa3021845dbb6d66eeedf1b84bfb531d8297dab912cfaabc175eac381)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEntitlementProps(
            application_arn=application_arn, entitlement=entitlement
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnEntitlement")
    @builtins.classmethod
    def is_cfn_entitlement(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnEntitlement.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e7855a7b5676d0c54c95a7de0c505212ace8e6923fc5361275111080c1d58695)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnEntitlement", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cd2564cf31ae8d23429d0021939e581294f3ba89028183898d8817674412788c)
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
            type_hints = cached_type_hints(_typecheckingstub__5b8c94b53f422be8d3b0be0962182d302742e372dacf6f2b047d4a662105bb12)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the entitlement was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEntitlementId")
    def attr_entitlement_id(self) -> builtins.str:
        '''The ID of the entitlement.

        :cloudformationAttribute: EntitlementId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEntitlementId"))

    @builtins.property
    @jsii.member(jsii_name="attrEntitlementPrincipalRoleAccount")
    def attr_entitlement_principal_role_account(self) -> builtins.str:
        '''The AWS account ID.

        :cloudformationAttribute: Entitlement.PrincipalRole.Account
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEntitlementPrincipalRoleAccount"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="entitlementRef")
    def entitlement_ref(self) -> "_aws_accountaccess_faac6759.EntitlementReference":
        '''A reference to a Entitlement resource.'''
        return typing.cast("_aws_accountaccess_faac6759.EntitlementReference", jsii.get(self, "entitlementRef"))

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''The ARN of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @application_arn.setter
    def application_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__034730d5688d92e52ff5b9b6fbe38251f6dc81e9d536249e931010d50adb335f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="entitlement")
    def entitlement(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.EntitlementProperty"]:
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.EntitlementProperty"], jsii.get(self, "entitlement"))

    @entitlement.setter
    def entitlement(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.EntitlementProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5ef955b4664a76db4f2fc500ba939a410c2fe5138f11b0300017bce25e6a1690)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entitlement", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accountaccess.CfnEntitlement.EntitlementProperty",
        jsii_struct_bases=[],
        name_mapping={"principal_role": "principalRole"},
    )
    class EntitlementProperty:
        def __init__(
            self,
            *,
            principal_role: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEntitlement.PrincipalRoleEntitlementProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param principal_role: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-entitlement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accountaccess as accountaccess
                
                entitlement_property = accountaccess.CfnEntitlement.EntitlementProperty(
                    principal_role=accountaccess.CfnEntitlement.PrincipalRoleEntitlementProperty(
                        principal=accountaccess.CfnEntitlement.PrincipalProperty(
                            identity_center=accountaccess.CfnEntitlement.IdentityCenterPrincipalProperty(
                                group_id="groupId",
                                user_id="userId"
                            )
                        ),
                        role_arn="roleArn",
                
                        # the properties below are optional
                        account="account"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2b0b212fa55758f0b2cdec81c3bdda5b4cc9031efba4417ec6f37585283bd4a6)
                check_type(argname="argument principal_role", value=principal_role, expected_type=type_hints["principal_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "principal_role": principal_role,
            }

        @builtins.property
        def principal_role(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.PrincipalRoleEntitlementProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-entitlement.html#cfn-accountaccess-entitlement-entitlement-principalrole
            '''
            result = self._values.get("principal_role")
            assert result is not None, "Required property 'principal_role' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.PrincipalRoleEntitlementProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntitlementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accountaccess.CfnEntitlement.IdentityCenterPrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"group_id": "groupId", "user_id": "userId"},
    )
    class IdentityCenterPrincipalProperty:
        def __init__(
            self,
            *,
            group_id: typing.Optional[builtins.str] = None,
            user_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param group_id: The ID of the group.
            :param user_id: The ID of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-identitycenterprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accountaccess as accountaccess
                
                identity_center_principal_property = accountaccess.CfnEntitlement.IdentityCenterPrincipalProperty(
                    group_id="groupId",
                    user_id="userId"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__9e0cc32a7adad1f25f7fa7f662ef46d03107ab93b8fc75ccd56f2a4cf9451957)
                check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
                check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if group_id is not None:
                self._values["group_id"] = group_id
            if user_id is not None:
                self._values["user_id"] = user_id

        @builtins.property
        def group_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-identitycenterprincipal.html#cfn-accountaccess-entitlement-identitycenterprincipal-groupid
            '''
            result = self._values.get("group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-identitycenterprincipal.html#cfn-accountaccess-entitlement-identitycenterprincipal-userid
            '''
            result = self._values.get("user_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityCenterPrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accountaccess.CfnEntitlement.PrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"identity_center": "identityCenter"},
    )
    class PrincipalProperty:
        def __init__(
            self,
            *,
            identity_center: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEntitlement.IdentityCenterPrincipalProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param identity_center: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-principal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accountaccess as accountaccess
                
                principal_property = accountaccess.CfnEntitlement.PrincipalProperty(
                    identity_center=accountaccess.CfnEntitlement.IdentityCenterPrincipalProperty(
                        group_id="groupId",
                        user_id="userId"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__c8bcfbd31c7647f468f8fc5f0a57dc123ccf0d77ee14450446c7c81c9b5a8ff2)
                check_type(argname="argument identity_center", value=identity_center, expected_type=type_hints["identity_center"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "identity_center": identity_center,
            }

        @builtins.property
        def identity_center(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.IdentityCenterPrincipalProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-principal.html#cfn-accountaccess-entitlement-principal-identitycenter
            '''
            result = self._values.get("identity_center")
            assert result is not None, "Required property 'identity_center' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.IdentityCenterPrincipalProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accountaccess.CfnEntitlement.PrincipalRoleEntitlementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "principal": "principal",
            "role_arn": "roleArn",
            "account": "account",
        },
    )
    class PrincipalRoleEntitlementProperty:
        def __init__(
            self,
            *,
            principal: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEntitlement.PrincipalProperty", typing.Dict[builtins.str, typing.Any]]],
            role_arn: builtins.str,
            account: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param principal: 
            :param role_arn: The ARN of the IAM role.
            :param account: The AWS account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-principalroleentitlement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accountaccess as accountaccess
                
                principal_role_entitlement_property = accountaccess.CfnEntitlement.PrincipalRoleEntitlementProperty(
                    principal=accountaccess.CfnEntitlement.PrincipalProperty(
                        identity_center=accountaccess.CfnEntitlement.IdentityCenterPrincipalProperty(
                            group_id="groupId",
                            user_id="userId"
                        )
                    ),
                    role_arn="roleArn",
                
                    # the properties below are optional
                    account="account"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__55d61dbf9add78068b0b74eb5a03c306303bc3ca8d9e362e53cc32c0c05a46ee)
                check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "principal": principal,
                "role_arn": role_arn,
            }
            if account is not None:
                self._values["account"] = account

        @builtins.property
        def principal(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.PrincipalProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-principalroleentitlement.html#cfn-accountaccess-entitlement-principalroleentitlement-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.PrincipalProperty"], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-principalroleentitlement.html#cfn-accountaccess-entitlement-principalroleentitlement-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account(self) -> typing.Optional[builtins.str]:
            '''The AWS account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accountaccess-entitlement-principalroleentitlement.html#cfn-accountaccess-entitlement-principalroleentitlement-account
            '''
            result = self._values.get("account")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrincipalRoleEntitlementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_accountaccess.CfnEntitlementProps",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn", "entitlement": "entitlement"},
)
class CfnEntitlementProps:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        entitlement: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEntitlement.EntitlementProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnEntitlement``.

        :param application_arn: The ARN of the application.
        :param entitlement: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accountaccess-entitlement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_accountaccess as accountaccess
            
            cfn_entitlement_props = accountaccess.CfnEntitlementProps(
                application_arn="applicationArn",
                entitlement=accountaccess.CfnEntitlement.EntitlementProperty(
                    principal_role=accountaccess.CfnEntitlement.PrincipalRoleEntitlementProperty(
                        principal=accountaccess.CfnEntitlement.PrincipalProperty(
                            identity_center=accountaccess.CfnEntitlement.IdentityCenterPrincipalProperty(
                                group_id="groupId",
                                user_id="userId"
                            )
                        ),
                        role_arn="roleArn",
            
                        # the properties below are optional
                        account="account"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b6f09b9966ffe427841dfbf69bf22fc3fdc351c2717c0a39f83ad32791ca1527)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument entitlement", value=entitlement, expected_type=type_hints["entitlement"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "entitlement": entitlement,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ARN of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accountaccess-entitlement.html#cfn-accountaccess-entitlement-applicationarn
        '''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entitlement(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.EntitlementProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accountaccess-entitlement.html#cfn-accountaccess-entitlement-entitlement
        '''
        result = self._values.get("entitlement")
        assert result is not None, "Required property 'entitlement' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEntitlement.EntitlementProperty"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEntitlementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnEntitlement",
    "CfnEntitlementProps",
]

publication.publish()

def _typecheckingstub__73f8306cb0446154a656b9352a94fa609e62d6f4fea69075d1eb8d89c3ac4a14(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identity_source: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnApplication.IdentitySourceProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4bdb7effa46d80e5f80e73ae010a2532e4ef859c788d9d48d059f7e97a79841(
    resource: _aws_accountaccess_faac6759.IApplicationRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1493a2fb28c7dd43c0e890e1ae1256ccaf4db6be6bcc1c561a541531e027cf7e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49270eda86db2677290e426f6aba06bfe38acc4345aa166d53e9904885513abf(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55bc264e005a4e321d459426a9a4868e61c16fa9ad72718b057e7530150a58e5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f3ebd2c52381656a5da764f2e0c95fe3d92356f1f4701aa43d1258221ca4fa(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnApplication.IdentitySourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b391672f08db62f459bf7d90ac7d5eded75fcc1909fb440c1773742b0486e52a(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c483dea091bb4d7c572e4950789ba596ced54cb8784fec4ea10586b9abf2338(
    *,
    instance_arn: builtins.str,
    application_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__319b031310b3b581332f1f5f92378bdffd6e03f475aebf0a06cf36ba3ada76e7(
    *,
    identity_center: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnApplication.IdentityCenterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad46efd33b0a77c38cead74dbbab11994a5410435cf1e918cb7ffc03353a5b1(
    *,
    identity_source: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnApplication.IdentitySourceProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7abc411fa3021845dbb6d66eeedf1b84bfb531d8297dab912cfaabc175eac381(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_arn: builtins.str,
    entitlement: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEntitlement.EntitlementProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7855a7b5676d0c54c95a7de0c505212ace8e6923fc5361275111080c1d58695(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd2564cf31ae8d23429d0021939e581294f3ba89028183898d8817674412788c(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b8c94b53f422be8d3b0be0962182d302742e372dacf6f2b047d4a662105bb12(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034730d5688d92e52ff5b9b6fbe38251f6dc81e9d536249e931010d50adb335f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ef955b4664a76db4f2fc500ba939a410c2fe5138f11b0300017bce25e6a1690(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnEntitlement.EntitlementProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0b212fa55758f0b2cdec81c3bdda5b4cc9031efba4417ec6f37585283bd4a6(
    *,
    principal_role: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEntitlement.PrincipalRoleEntitlementProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e0cc32a7adad1f25f7fa7f662ef46d03107ab93b8fc75ccd56f2a4cf9451957(
    *,
    group_id: typing.Optional[builtins.str] = None,
    user_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8bcfbd31c7647f468f8fc5f0a57dc123ccf0d77ee14450446c7c81c9b5a8ff2(
    *,
    identity_center: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEntitlement.IdentityCenterPrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d61dbf9add78068b0b74eb5a03c306303bc3ca8d9e362e53cc32c0c05a46ee(
    *,
    principal: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEntitlement.PrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    account: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6f09b9966ffe427841dfbf69bf22fc3fdc351c2717c0a39f83ad32791ca1527(
    *,
    application_arn: builtins.str,
    entitlement: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEntitlement.EntitlementProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass
