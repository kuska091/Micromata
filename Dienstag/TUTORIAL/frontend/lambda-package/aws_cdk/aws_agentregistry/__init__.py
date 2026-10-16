r'''
# AWS::AgentRegistry Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_agentregistry as agentregistry
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AgentRegistry construct libraries](https://constructs.dev/search?q=agentregistry)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AgentRegistry resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AgentRegistry.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AgentRegistry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AgentRegistry.html).

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
    import aws_cdk.interfaces.aws_agentregistry as _aws_agentregistry_506fb521
    import constructs as _constructs_77d1e7e8
else:

    _aws_agentregistry_506fb521 = _LazyImport("aws_cdk.interfaces.aws_agentregistry")
    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_agentregistry_506fb521.IRegistryRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnRegistry(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistry",
):
    '''Definition of AWS::AgentRegistry::Registry Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registry.html
    :cloudformationResource: AWS::AgentRegistry::Registry
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_agentregistry as agentregistry
        
        cfn_registry = agentregistry.CfnRegistry(self, "MyCfnRegistry",
            name="name",
        
            # the properties below are optional
            approval_configuration=agentregistry.CfnRegistry.ApprovalConfigurationProperty(
                auto_approval_rules=["autoApprovalRules"]
            ),
            authorizer_type="authorizerType",
            description="description",
            discovery_configuration=agentregistry.CfnRegistry.DiscoveryConfigurationProperty(
                authorizer_configuration=agentregistry.CfnRegistry.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=agentregistry.CfnRegistry.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
        
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"],
                        allowed_scopes=["allowedScopes"],
                        custom_claims=[agentregistry.CfnRegistry.CustomClaimValidationTypeProperty(
                            authorizing_claim_match_value=agentregistry.CfnRegistry.AuthorizingClaimMatchValueTypeProperty(
                                claim_match_operator="claimMatchOperator",
                                claim_match_value=agentregistry.CfnRegistry.ClaimMatchValueTypeProperty(
                                    match_value_string="matchValueString",
                                    match_value_string_list=["matchValueStringList"]
                                )
                            ),
                            inbound_token_claim_name="inboundTokenClaimName",
                            inbound_token_claim_value_type="inboundTokenClaimValueType"
                        )]
                    )
                )
            ),
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
        approval_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.ApprovalConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        authorizer_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        discovery_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.DiscoveryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AgentRegistry::Registry``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the registry.
        :param approval_configuration: Configuration for the registry's record approval workflow.
        :param authorizer_type: The type of authorizer that controls how consumers access the registry's search and MCP invoke operations.
        :param description: The description of the registry.
        :param discovery_configuration: Discovery configuration for the registry. Controls how consumers are authorized to search the registry and invoke its MCP endpoint.
        :param tags: Tags to assign to the registry.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c92eab34b9759c9076b623bf33eca391e46a29b4416fcb07c7b30302f1de95b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRegistryProps(
            name=name,
            approval_configuration=approval_configuration,
            authorizer_type=authorizer_type,
            description=description,
            discovery_configuration=discovery_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForRegistry")
    @builtins.classmethod
    def arn_for_registry(
        cls,
        resource: "_aws_agentregistry_506fb521.IRegistryRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f807826dcca746eb661237fe74624805a548d2fd0b2754b127a7abcba8e99d64)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForRegistry", [resource]))

    @jsii.member(jsii_name="isCfnRegistry")
    @builtins.classmethod
    def is_cfn_registry(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRegistry.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__106d6487e951bf82b880a23c87994f5240e375c0768d18c5da3364f8d8b9ad83)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRegistry", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3127ad756b133c6ac1a01fb8fb9fa2b74c8fe3ace3578175225748b3ee8dc129)
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
            type_hints = cached_type_hints(_typecheckingstub__0c4f19cc7543f61ed5fe2a8439cd07e7c70758818d19b0543fb92bb89c3fc01f)
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
        '''The timestamp when the registry was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrRegistryArn")
    def attr_registry_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the registry.

        :cloudformationAttribute: RegistryArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRegistryId")
    def attr_registry_id(self) -> builtins.str:
        '''The unique identifier of the registry.

        :cloudformationAttribute: RegistryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the registry.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the registry was last updated.

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
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "_aws_agentregistry_506fb521.RegistryReference":
        '''A reference to a Registry resource.'''
        return typing.cast("_aws_agentregistry_506fb521.RegistryReference", jsii.get(self, "registryRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the registry.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__44903752c8ad92a1a5b3bea748d118e360856827239ffb71ff515dbc7e372da7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="approvalConfiguration")
    def approval_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.ApprovalConfigurationProperty"]]:
        '''Configuration for the registry's record approval workflow.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.ApprovalConfigurationProperty"]], jsii.get(self, "approvalConfiguration"))

    @approval_configuration.setter
    def approval_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.ApprovalConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a82c9cc795b7a19f46589e380713aa8028087b53c881ad5cb72684fb914b42e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authorizerType")
    def authorizer_type(self) -> typing.Optional[builtins.str]:
        '''The type of authorizer that controls how consumers access the registry's search and MCP invoke operations.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerType"))

    @authorizer_type.setter
    def authorizer_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e5ae93a351cc6e0a318dbf92458f45de0b6b96efd086af7f4205c7e00dcd0f56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the registry.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3b008aa20d30be0120e5d8a8866b7968949e2929088e43770aa94ebee678edbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="discoveryConfiguration")
    def discovery_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.DiscoveryConfigurationProperty"]]:
        '''Discovery configuration for the registry.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.DiscoveryConfigurationProperty"]], jsii.get(self, "discoveryConfiguration"))

    @discovery_configuration.setter
    def discovery_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.DiscoveryConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5a1b96b5514172fb57ca62002ae3be655be2839d81eff8747ebaecd2ee280ce9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "discoveryConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to assign to the registry.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6f33b3edde8ee2055f274039c2177c20002d6e3d68800b02fd6a5690ffaa15d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistry.ApprovalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"auto_approval_rules": "autoApprovalRules"},
    )
    class ApprovalConfigurationProperty:
        def __init__(
            self,
            *,
            auto_approval_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration for the registry's record approval workflow.

            :param auto_approval_rules: The rules that determine which registry records are automatically approved on submission. When omitted or empty, submitted records require manual review.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-approvalconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                approval_configuration_property = agentregistry.CfnRegistry.ApprovalConfigurationProperty(
                    auto_approval_rules=["autoApprovalRules"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__bfda2e2da1494b1ec48d9472528d44ae0527e50e58d3c6145181a36d375c0f85)
                check_type(argname="argument auto_approval_rules", value=auto_approval_rules, expected_type=type_hints["auto_approval_rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_approval_rules is not None:
                self._values["auto_approval_rules"] = auto_approval_rules

        @builtins.property
        def auto_approval_rules(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The rules that determine which registry records are automatically approved on submission.

            When omitted or empty, submitted records require manual review.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-approvalconfiguration.html#cfn-agentregistry-registry-approvalconfiguration-autoapprovalrules
            '''
            result = self._values.get("auto_approval_rules")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApprovalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistry.AuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_jwt_authorizer": "customJwtAuthorizer"},
    )
    class AuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            custom_jwt_authorizer: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.CustomJWTAuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The authorizer configuration for the registry.

            This is a union - specify exactly one member.

            :param custom_jwt_authorizer: Configuration for a custom JWT authorizer that validates inbound bearer tokens against an OpenID Connect identity provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-authorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                authorizer_configuration_property = agentregistry.CfnRegistry.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=agentregistry.CfnRegistry.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
                
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"],
                        allowed_scopes=["allowedScopes"],
                        custom_claims=[agentregistry.CfnRegistry.CustomClaimValidationTypeProperty(
                            authorizing_claim_match_value=agentregistry.CfnRegistry.AuthorizingClaimMatchValueTypeProperty(
                                claim_match_operator="claimMatchOperator",
                                claim_match_value=agentregistry.CfnRegistry.ClaimMatchValueTypeProperty(
                                    match_value_string="matchValueString",
                                    match_value_string_list=["matchValueStringList"]
                                )
                            ),
                            inbound_token_claim_name="inboundTokenClaimName",
                            inbound_token_claim_value_type="inboundTokenClaimValueType"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ed2639db61d2e3af825f1a8f0f3500e04332e0af1dbd729a78477d4e8d1b9edf)
                check_type(argname="argument custom_jwt_authorizer", value=custom_jwt_authorizer, expected_type=type_hints["custom_jwt_authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_jwt_authorizer": custom_jwt_authorizer,
            }

        @builtins.property
        def custom_jwt_authorizer(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.CustomJWTAuthorizerConfigurationProperty"]:
            '''Configuration for a custom JWT authorizer that validates inbound bearer tokens against an OpenID Connect identity provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-authorizerconfiguration.html#cfn-agentregistry-registry-authorizerconfiguration-customjwtauthorizer
            '''
            result = self._values.get("custom_jwt_authorizer")
            assert result is not None, "Required property 'custom_jwt_authorizer' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.CustomJWTAuthorizerConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistry.AuthorizingClaimMatchValueTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "claim_match_operator": "claimMatchOperator",
            "claim_match_value": "claimMatchValue",
        },
    )
    class AuthorizingClaimMatchValueTypeProperty:
        def __init__(
            self,
            *,
            claim_match_operator: builtins.str,
            claim_match_value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.ClaimMatchValueTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The value and match operator used to authorize a claim during JWT validation.

            :param claim_match_operator: 
            :param claim_match_value: The expected value used to match a claim. Exactly one member is set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                authorizing_claim_match_value_type_property = agentregistry.CfnRegistry.AuthorizingClaimMatchValueTypeProperty(
                    claim_match_operator="claimMatchOperator",
                    claim_match_value=agentregistry.CfnRegistry.ClaimMatchValueTypeProperty(
                        match_value_string="matchValueString",
                        match_value_string_list=["matchValueStringList"]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__843a47c7ba9ad382abfec27c682df7bc4ecf3f899d64f8c791c2cd41dd2c198e)
                check_type(argname="argument claim_match_operator", value=claim_match_operator, expected_type=type_hints["claim_match_operator"])
                check_type(argname="argument claim_match_value", value=claim_match_value, expected_type=type_hints["claim_match_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "claim_match_operator": claim_match_operator,
                "claim_match_value": claim_match_value,
            }

        @builtins.property
        def claim_match_operator(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype.html#cfn-agentregistry-registry-authorizingclaimmatchvaluetype-claimmatchoperator
            '''
            result = self._values.get("claim_match_operator")
            assert result is not None, "Required property 'claim_match_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def claim_match_value(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.ClaimMatchValueTypeProperty"]:
            '''The expected value used to match a claim.

            Exactly one member is set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-authorizingclaimmatchvaluetype.html#cfn-agentregistry-registry-authorizingclaimmatchvaluetype-claimmatchvalue
            '''
            result = self._values.get("claim_match_value")
            assert result is not None, "Required property 'claim_match_value' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.ClaimMatchValueTypeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizingClaimMatchValueTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistry.ClaimMatchValueTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "match_value_string": "matchValueString",
            "match_value_string_list": "matchValueStringList",
        },
    )
    class ClaimMatchValueTypeProperty:
        def __init__(
            self,
            *,
            match_value_string: typing.Optional[builtins.str] = None,
            match_value_string_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The expected value used to match a claim.

            Exactly one member is set.

            :param match_value_string: 
            :param match_value_string_list: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-claimmatchvaluetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                claim_match_value_type_property = agentregistry.CfnRegistry.ClaimMatchValueTypeProperty(
                    match_value_string="matchValueString",
                    match_value_string_list=["matchValueStringList"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f658ef5b0d03da0e25be1ec309f8cbc63ad52710adbaf23f6f1ae2d5a44eeea8)
                check_type(argname="argument match_value_string", value=match_value_string, expected_type=type_hints["match_value_string"])
                check_type(argname="argument match_value_string_list", value=match_value_string_list, expected_type=type_hints["match_value_string_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if match_value_string is not None:
                self._values["match_value_string"] = match_value_string
            if match_value_string_list is not None:
                self._values["match_value_string_list"] = match_value_string_list

        @builtins.property
        def match_value_string(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-claimmatchvaluetype.html#cfn-agentregistry-registry-claimmatchvaluetype-matchvaluestring
            '''
            result = self._values.get("match_value_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def match_value_string_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-claimmatchvaluetype.html#cfn-agentregistry-registry-claimmatchvaluetype-matchvaluestringlist
            '''
            result = self._values.get("match_value_string_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClaimMatchValueTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistry.CustomClaimValidationTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorizing_claim_match_value": "authorizingClaimMatchValue",
            "inbound_token_claim_name": "inboundTokenClaimName",
            "inbound_token_claim_value_type": "inboundTokenClaimValueType",
        },
    )
    class CustomClaimValidationTypeProperty:
        def __init__(
            self,
            *,
            authorizing_claim_match_value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.AuthorizingClaimMatchValueTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            inbound_token_claim_name: builtins.str,
            inbound_token_claim_value_type: builtins.str,
        ) -> None:
            '''A validation rule applied to a single claim of an inbound JWT.

            :param authorizing_claim_match_value: The value and match operator used to authorize a claim during JWT validation.
            :param inbound_token_claim_name: 
            :param inbound_token_claim_value_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customclaimvalidationtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                custom_claim_validation_type_property = agentregistry.CfnRegistry.CustomClaimValidationTypeProperty(
                    authorizing_claim_match_value=agentregistry.CfnRegistry.AuthorizingClaimMatchValueTypeProperty(
                        claim_match_operator="claimMatchOperator",
                        claim_match_value=agentregistry.CfnRegistry.ClaimMatchValueTypeProperty(
                            match_value_string="matchValueString",
                            match_value_string_list=["matchValueStringList"]
                        )
                    ),
                    inbound_token_claim_name="inboundTokenClaimName",
                    inbound_token_claim_value_type="inboundTokenClaimValueType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__92c0bec14d64b642472f4ad606c21eb9001da8eee5764d82d0599db783c5b274)
                check_type(argname="argument authorizing_claim_match_value", value=authorizing_claim_match_value, expected_type=type_hints["authorizing_claim_match_value"])
                check_type(argname="argument inbound_token_claim_name", value=inbound_token_claim_name, expected_type=type_hints["inbound_token_claim_name"])
                check_type(argname="argument inbound_token_claim_value_type", value=inbound_token_claim_value_type, expected_type=type_hints["inbound_token_claim_value_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorizing_claim_match_value": authorizing_claim_match_value,
                "inbound_token_claim_name": inbound_token_claim_name,
                "inbound_token_claim_value_type": inbound_token_claim_value_type,
            }

        @builtins.property
        def authorizing_claim_match_value(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.AuthorizingClaimMatchValueTypeProperty"]:
            '''The value and match operator used to authorize a claim during JWT validation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customclaimvalidationtype.html#cfn-agentregistry-registry-customclaimvalidationtype-authorizingclaimmatchvalue
            '''
            result = self._values.get("authorizing_claim_match_value")
            assert result is not None, "Required property 'authorizing_claim_match_value' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.AuthorizingClaimMatchValueTypeProperty"], result)

        @builtins.property
        def inbound_token_claim_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customclaimvalidationtype.html#cfn-agentregistry-registry-customclaimvalidationtype-inboundtokenclaimname
            '''
            result = self._values.get("inbound_token_claim_name")
            assert result is not None, "Required property 'inbound_token_claim_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def inbound_token_claim_value_type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customclaimvalidationtype.html#cfn-agentregistry-registry-customclaimvalidationtype-inboundtokenclaimvaluetype
            '''
            result = self._values.get("inbound_token_claim_value_type")
            assert result is not None, "Required property 'inbound_token_claim_value_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomClaimValidationTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistry.CustomJWTAuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "discovery_url": "discoveryUrl",
            "allowed_audience": "allowedAudience",
            "allowed_clients": "allowedClients",
            "allowed_scopes": "allowedScopes",
            "custom_claims": "customClaims",
        },
    )
    class CustomJWTAuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            discovery_url: builtins.str,
            allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            custom_claims: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.CustomClaimValidationTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration for a custom JWT authorizer that validates inbound bearer tokens against an OpenID Connect identity provider.

            :param discovery_url: The OpenID Connect discovery URL used to retrieve the identity provider's metadata and signing keys.
            :param allowed_audience: The audience values accepted during JWT validation.
            :param allowed_clients: The client identifiers accepted during JWT validation.
            :param allowed_scopes: The scopes accepted during JWT validation.
            :param custom_claims: Additional custom claim validations applied to the inbound JWT.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customjwtauthorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                custom_jwt_authorizer_configuration_property = agentregistry.CfnRegistry.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
                
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"],
                    allowed_scopes=["allowedScopes"],
                    custom_claims=[agentregistry.CfnRegistry.CustomClaimValidationTypeProperty(
                        authorizing_claim_match_value=agentregistry.CfnRegistry.AuthorizingClaimMatchValueTypeProperty(
                            claim_match_operator="claimMatchOperator",
                            claim_match_value=agentregistry.CfnRegistry.ClaimMatchValueTypeProperty(
                                match_value_string="matchValueString",
                                match_value_string_list=["matchValueStringList"]
                            )
                        ),
                        inbound_token_claim_name="inboundTokenClaimName",
                        inbound_token_claim_value_type="inboundTokenClaimValueType"
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f7f05f2a0c04cca178fdec7101afb3c703940cffbf41f03ccc78bc9094aab209)
                check_type(argname="argument discovery_url", value=discovery_url, expected_type=type_hints["discovery_url"])
                check_type(argname="argument allowed_audience", value=allowed_audience, expected_type=type_hints["allowed_audience"])
                check_type(argname="argument allowed_clients", value=allowed_clients, expected_type=type_hints["allowed_clients"])
                check_type(argname="argument allowed_scopes", value=allowed_scopes, expected_type=type_hints["allowed_scopes"])
                check_type(argname="argument custom_claims", value=custom_claims, expected_type=type_hints["custom_claims"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "discovery_url": discovery_url,
            }
            if allowed_audience is not None:
                self._values["allowed_audience"] = allowed_audience
            if allowed_clients is not None:
                self._values["allowed_clients"] = allowed_clients
            if allowed_scopes is not None:
                self._values["allowed_scopes"] = allowed_scopes
            if custom_claims is not None:
                self._values["custom_claims"] = custom_claims

        @builtins.property
        def discovery_url(self) -> builtins.str:
            '''The OpenID Connect discovery URL used to retrieve the identity provider's metadata and signing keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customjwtauthorizerconfiguration.html#cfn-agentregistry-registry-customjwtauthorizerconfiguration-discoveryurl
            '''
            result = self._values.get("discovery_url")
            assert result is not None, "Required property 'discovery_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_audience(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The audience values accepted during JWT validation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customjwtauthorizerconfiguration.html#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedaudience
            '''
            result = self._values.get("allowed_audience")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_clients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The client identifiers accepted during JWT validation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customjwtauthorizerconfiguration.html#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedclients
            '''
            result = self._values.get("allowed_clients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The scopes accepted during JWT validation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customjwtauthorizerconfiguration.html#cfn-agentregistry-registry-customjwtauthorizerconfiguration-allowedscopes
            '''
            result = self._values.get("allowed_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def custom_claims(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.CustomClaimValidationTypeProperty"]]]]:
            '''Additional custom claim validations applied to the inbound JWT.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-customjwtauthorizerconfiguration.html#cfn-agentregistry-registry-customjwtauthorizerconfiguration-customclaims
            '''
            result = self._values.get("custom_claims")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.CustomClaimValidationTypeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomJWTAuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistry.DiscoveryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"authorizer_configuration": "authorizerConfiguration"},
    )
    class DiscoveryConfigurationProperty:
        def __init__(
            self,
            *,
            authorizer_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Discovery configuration for the registry.

            Controls how consumers are authorized to search the registry and invoke its MCP endpoint.

            :param authorizer_configuration: The authorizer configuration for the registry. This is a union - specify exactly one member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-discoveryconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                discovery_configuration_property = agentregistry.CfnRegistry.DiscoveryConfigurationProperty(
                    authorizer_configuration=agentregistry.CfnRegistry.AuthorizerConfigurationProperty(
                        custom_jwt_authorizer=agentregistry.CfnRegistry.CustomJWTAuthorizerConfigurationProperty(
                            discovery_url="discoveryUrl",
                
                            # the properties below are optional
                            allowed_audience=["allowedAudience"],
                            allowed_clients=["allowedClients"],
                            allowed_scopes=["allowedScopes"],
                            custom_claims=[agentregistry.CfnRegistry.CustomClaimValidationTypeProperty(
                                authorizing_claim_match_value=agentregistry.CfnRegistry.AuthorizingClaimMatchValueTypeProperty(
                                    claim_match_operator="claimMatchOperator",
                                    claim_match_value=agentregistry.CfnRegistry.ClaimMatchValueTypeProperty(
                                        match_value_string="matchValueString",
                                        match_value_string_list=["matchValueStringList"]
                                    )
                                ),
                                inbound_token_claim_name="inboundTokenClaimName",
                                inbound_token_claim_value_type="inboundTokenClaimValueType"
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0075ca34f0469a75f3909e5eaf6a881ca07aa3e497e1be371bc34bb156576420)
                check_type(argname="argument authorizer_configuration", value=authorizer_configuration, expected_type=type_hints["authorizer_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorizer_configuration is not None:
                self._values["authorizer_configuration"] = authorizer_configuration

        @builtins.property
        def authorizer_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.AuthorizerConfigurationProperty"]]:
            '''The authorizer configuration for the registry.

            This is a union - specify exactly one member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registry-discoveryconfiguration.html#cfn-agentregistry-registry-discoveryconfiguration-authorizerconfiguration
            '''
            result = self._values.get("authorizer_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.AuthorizerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DiscoveryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "approval_configuration": "approvalConfiguration",
        "authorizer_type": "authorizerType",
        "description": "description",
        "discovery_configuration": "discoveryConfiguration",
        "tags": "tags",
    },
)
class CfnRegistryProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        approval_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.ApprovalConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        authorizer_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        discovery_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistry.DiscoveryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRegistry``.

        :param name: The name of the registry.
        :param approval_configuration: Configuration for the registry's record approval workflow.
        :param authorizer_type: The type of authorizer that controls how consumers access the registry's search and MCP invoke operations.
        :param description: The description of the registry.
        :param discovery_configuration: Discovery configuration for the registry. Controls how consumers are authorized to search the registry and invoke its MCP endpoint.
        :param tags: Tags to assign to the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registry.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_agentregistry as agentregistry
            
            cfn_registry_props = agentregistry.CfnRegistryProps(
                name="name",
            
                # the properties below are optional
                approval_configuration=agentregistry.CfnRegistry.ApprovalConfigurationProperty(
                    auto_approval_rules=["autoApprovalRules"]
                ),
                authorizer_type="authorizerType",
                description="description",
                discovery_configuration=agentregistry.CfnRegistry.DiscoveryConfigurationProperty(
                    authorizer_configuration=agentregistry.CfnRegistry.AuthorizerConfigurationProperty(
                        custom_jwt_authorizer=agentregistry.CfnRegistry.CustomJWTAuthorizerConfigurationProperty(
                            discovery_url="discoveryUrl",
            
                            # the properties below are optional
                            allowed_audience=["allowedAudience"],
                            allowed_clients=["allowedClients"],
                            allowed_scopes=["allowedScopes"],
                            custom_claims=[agentregistry.CfnRegistry.CustomClaimValidationTypeProperty(
                                authorizing_claim_match_value=agentregistry.CfnRegistry.AuthorizingClaimMatchValueTypeProperty(
                                    claim_match_operator="claimMatchOperator",
                                    claim_match_value=agentregistry.CfnRegistry.ClaimMatchValueTypeProperty(
                                        match_value_string="matchValueString",
                                        match_value_string_list=["matchValueStringList"]
                                    )
                                ),
                                inbound_token_claim_name="inboundTokenClaimName",
                                inbound_token_claim_value_type="inboundTokenClaimValueType"
                            )]
                        )
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b98476a5662bfac6fbe3ddd43ef77bef00711e71c235f99e97057616ec96a16e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument approval_configuration", value=approval_configuration, expected_type=type_hints["approval_configuration"])
            check_type(argname="argument authorizer_type", value=authorizer_type, expected_type=type_hints["authorizer_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument discovery_configuration", value=discovery_configuration, expected_type=type_hints["discovery_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if approval_configuration is not None:
            self._values["approval_configuration"] = approval_configuration
        if authorizer_type is not None:
            self._values["authorizer_type"] = authorizer_type
        if description is not None:
            self._values["description"] = description
        if discovery_configuration is not None:
            self._values["discovery_configuration"] = discovery_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registry.html#cfn-agentregistry-registry-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def approval_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.ApprovalConfigurationProperty"]]:
        '''Configuration for the registry's record approval workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registry.html#cfn-agentregistry-registry-approvalconfiguration
        '''
        result = self._values.get("approval_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.ApprovalConfigurationProperty"]], result)

    @builtins.property
    def authorizer_type(self) -> typing.Optional[builtins.str]:
        '''The type of authorizer that controls how consumers access the registry's search and MCP invoke operations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registry.html#cfn-agentregistry-registry-authorizertype
        '''
        result = self._values.get("authorizer_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registry.html#cfn-agentregistry-registry-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def discovery_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.DiscoveryConfigurationProperty"]]:
        '''Discovery configuration for the registry.

        Controls how consumers are authorized to search the registry and invoke its MCP endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registry.html#cfn-agentregistry-registry-discoveryconfiguration
        '''
        result = self._values.get("discovery_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistry.DiscoveryConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to assign to the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registry.html#cfn-agentregistry-registry-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegistryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_agentregistry_506fb521.IRegistryRecordRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnRegistryRecord(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord",
):
    '''Definition of AWS::AgentRegistry::RegistryRecord Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html
    :cloudformationResource: AWS::AgentRegistry::RegistryRecord
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_agentregistry as agentregistry
        
        cfn_registry_record = agentregistry.CfnRegistryRecord(self, "MyCfnRegistryRecord",
            descriptors=agentregistry.CfnRegistryRecord.DescriptorsProperty(
                a2_a_agent_card=agentregistry.CfnRegistryRecord.A2aAgentCardDescriptorProperty(
                    data="data",
                    data_schema_version="dataSchemaVersion",
                    source=agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                            url="url",
        
                            # the properties below are optional
                            credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                                credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                    iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                        region="region",
                                        role_arn="roleArn",
                                        service="service"
                                    ),
                                    oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                        provider_arn="providerArn",
        
                                        # the properties below are optional
                                        custom_parameters={
                                            "custom_parameters_key": "customParameters"
                                        },
                                        grant_type="grantType",
                                        scopes=["scopes"]
                                    )
                                ),
                                credential_provider_type="credentialProviderType"
                            )]
                        )
                    )
                ),
                agent_skills_definition=agentregistry.CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty(
                    additional_data=agentregistry.CfnRegistryRecord.AgentSkillsAdditionalDataProperty(
                        skill_md=agentregistry.CfnRegistryRecord.AgentSkillsMdDescriptorProperty(
                            data="data",
                            data_schema_version="dataSchemaVersion",
                            source=agentregistry.CfnRegistryRecord.SkillMdSourceProperty(
                                from_url=agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty(
                                    url="url"
                                )
                            )
                        )
                    ),
                    data="data",
                    data_schema_version="dataSchemaVersion"
                ),
                agui=agentregistry.CfnRegistryRecord.AgUiDescriptorProperty(
                    source=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                            url="url"
                        )
                    )
                ),
                custom=agentregistry.CfnRegistryRecord.CustomDescriptorProperty(
                    data="data"
                ),
                http=agentregistry.CfnRegistryRecord.HttpDescriptorProperty(
                    source=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                            url="url"
                        )
                    )
                ),
                mcp_server=agentregistry.CfnRegistryRecord.McpServerDescriptorProperty(
                    additional_data=agentregistry.CfnRegistryRecord.McpServerAdditionalDataProperty(
                        tools=agentregistry.CfnRegistryRecord.McpToolsDescriptorProperty(
                            data="data",
                            data_schema_version="dataSchemaVersion"
                        )
                    ),
                    data="data",
                    data_schema_version="dataSchemaVersion",
                    source=agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                            url="url",
        
                            # the properties below are optional
                            credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                                credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                    iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                        region="region",
                                        role_arn="roleArn",
                                        service="service"
                                    ),
                                    oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                        provider_arn="providerArn",
        
                                        # the properties below are optional
                                        custom_parameters={
                                            "custom_parameters_key": "customParameters"
                                        },
                                        grant_type="grantType",
                                        scopes=["scopes"]
                                    )
                                ),
                                credential_provider_type="credentialProviderType"
                            )]
                        )
                    )
                )
            ),
            name="name",
            record_type="recordType",
        
            # the properties below are optional
            description="description",
            display_name="displayName",
            record_version="recordVersion",
            registry_id="registryId",
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
        descriptors: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.DescriptorsProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        record_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        record_version: typing.Optional[builtins.str] = None,
        registry_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AgentRegistry::RegistryRecord``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param descriptors: The typed set of descriptors for a registry record. Exactly one descriptor field is populated based on the record type.
        :param name: The name of the registry record.
        :param record_type: The type of the registry record.
        :param description: The description of the registry record.
        :param display_name: The human-readable display name of the registry record.
        :param record_version: The version of the registry record.
        :param registry_id: The identifier of the registry in which to create the record. You can specify either the registry ID or the registry Amazon Resource Name (ARN). Use the ARN form to reference a registry shared from another account via AWS Resource Access Manager (RAM).
        :param tags: Tags to assign to the registry record.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7ef8b3afdf0d8fa2a57531ae35ed0ed172ca12f519f3a312e79d540a72e88d74)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRegistryRecordProps(
            descriptors=descriptors,
            name=name,
            record_type=record_type,
            description=description,
            display_name=display_name,
            record_version=record_version,
            registry_id=registry_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnRegistryRecord")
    @builtins.classmethod
    def is_cfn_registry_record(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRegistryRecord.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__60ab8e8cef582bd2d3ec6bd5cfb86ddee72d7c1f0f0131b2b83652803af88d6d)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRegistryRecord", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a7361ed8164b5f3cdafa91a2686cb44699f14ff384f55aada32958b17ab5fa04)
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
            type_hints = cached_type_hints(_typecheckingstub__b8464f2d44da52e9636217c4cc94c48509e2de79509aec4ac8f0c9cc915064df)
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
        '''The timestamp when the registry record was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The identifier of the AWS account that created the registry record.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrRecordArn")
    def attr_record_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the registry record.

        :cloudformationAttribute: RecordArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRecordArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRecordId")
    def attr_record_id(self) -> builtins.str:
        '''The unique identifier of the registry record.

        :cloudformationAttribute: RecordId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRecordId"))

    @builtins.property
    @jsii.member(jsii_name="attrRegistryArn")
    def attr_registry_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the registry containing the record.

        :cloudformationAttribute: RegistryArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The lifecycle status of the registry record.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the registry record was last updated.

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
    @jsii.member(jsii_name="registryRecordRef")
    def registry_record_ref(
        self,
    ) -> "_aws_agentregistry_506fb521.RegistryRecordReference":
        '''A reference to a RegistryRecord resource.'''
        return typing.cast("_aws_agentregistry_506fb521.RegistryRecordReference", jsii.get(self, "registryRecordRef"))

    @builtins.property
    @jsii.member(jsii_name="descriptors")
    def descriptors(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorsProperty"]:
        '''The typed set of descriptors for a registry record.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorsProperty"], jsii.get(self, "descriptors"))

    @descriptors.setter
    def descriptors(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorsProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e20ed69c19154a1c1c82f76a8fa036f90acfa535493e48813acaf3af97ae1fef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "descriptors", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the registry record.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3dac661425718c0e01f8c2d9f0b486f0cf83ef80ab08988a82ad85f2797e2336)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordType")
    def record_type(self) -> builtins.str:
        '''The type of the registry record.'''
        return typing.cast(builtins.str, jsii.get(self, "recordType"))

    @record_type.setter
    def record_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ddafdbd3f82f53f2237ad280e72be884e39e4be52bec5ebb50731242e8bb189f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the registry record.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0c6a9aae0bf922e08911fd3846f325f960d7df0f0cbb9e1057371b443377e605)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The human-readable display name of the registry record.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4837f51052d31d643559b181dcf50bb6914aea97770549487a7166473d6d13df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordVersion")
    def record_version(self) -> typing.Optional[builtins.str]:
        '''The version of the registry record.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordVersion"))

    @record_version.setter
    def record_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c03f3fe0d25f7024efbcefface95c2d9aad0137a0613c75161e23fa68d4a24af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="registryId")
    def registry_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the registry in which to create the record.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryId"))

    @registry_id.setter
    def registry_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d4a1f651ea2d1dea12707fff754c90bddf57ff13a28d3826dea56199a5971c15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to assign to the registry record.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__59a039aa0fc4e16e0e8ba645515217334b8560454b55d3da7bfc7de67e70bc46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.A2aAgentCardDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data": "data",
            "data_schema_version": "dataSchemaVersion",
            "source": "source",
        },
    )
    class A2aAgentCardDescriptorProperty:
        def __init__(
            self,
            *,
            data: typing.Optional[builtins.str] = None,
            data_schema_version: typing.Optional[builtins.str] = None,
            source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.DescriptorSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The A2A agent card descriptor, populated when the record type is AGENT.

            :param data: Descriptor payload data.
            :param data_schema_version: Version of the descriptor type schema.
            :param source: The source configuration that defines where descriptor content is retrieved from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                a2a_agent_card_descriptor_property = agentregistry.CfnRegistryRecord.A2aAgentCardDescriptorProperty(
                    data="data",
                    data_schema_version="dataSchemaVersion",
                    source=agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                            url="url",
                
                            # the properties below are optional
                            credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                                credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                    iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                        region="region",
                                        role_arn="roleArn",
                                        service="service"
                                    ),
                                    oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                        provider_arn="providerArn",
                
                                        # the properties below are optional
                                        custom_parameters={
                                            "custom_parameters_key": "customParameters"
                                        },
                                        grant_type="grantType",
                                        scopes=["scopes"]
                                    )
                                ),
                                credential_provider_type="credentialProviderType"
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__afa9881107eac84791f3306a270cd236e769c8e820626a2d3fa82a0684e3afbf)
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
                check_type(argname="argument data_schema_version", value=data_schema_version, expected_type=type_hints["data_schema_version"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data is not None:
                self._values["data"] = data
            if data_schema_version is not None:
                self._values["data_schema_version"] = data_schema_version
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''Descriptor payload data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor.html#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_schema_version(self) -> typing.Optional[builtins.str]:
            '''Version of the descriptor type schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor.html#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-dataschemaversion
            '''
            result = self._values.get("data_schema_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorSourceProperty"]]:
            '''The source configuration that defines where descriptor content is retrieved from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-a2aagentcarddescriptor.html#cfn-agentregistry-registryrecord-a2aagentcarddescriptor-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "A2aAgentCardDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.AgUiDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class AgUiDescriptorProperty:
        def __init__(
            self,
            *,
            source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.SourceOnlyDescriptorSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The AG-UI (Agent-User Interaction) descriptor, populated for records detected from an AG-UI protocol source.

            This descriptor is source-only: its content is synchronized from the configured source URL rather than supplied inline.

            :param source: Source configuration for a source-only descriptor. Unlike mcpServer/a2aAgentCard sources, source-only descriptors do not support credential providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-aguidescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                ag_ui_descriptor_property = agentregistry.CfnRegistryRecord.AgUiDescriptorProperty(
                    source=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                            url="url"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f14707a1d412fb23aeac570107aa3e17f2d92f3d9d3a1b55108cabaa4ba9f75b)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def source(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SourceOnlyDescriptorSourceProperty"]]:
            '''Source configuration for a source-only descriptor.

            Unlike mcpServer/a2aAgentCard sources, source-only descriptors do not support credential providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-aguidescriptor.html#cfn-agentregistry-registryrecord-aguidescriptor-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SourceOnlyDescriptorSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgUiDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.AgentSkillsAdditionalDataProperty",
        jsii_struct_bases=[],
        name_mapping={"skill_md": "skillMd"},
    )
    class AgentSkillsAdditionalDataProperty:
        def __init__(
            self,
            *,
            skill_md: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.AgentSkillsMdDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Additional data associated with an agent skills definition descriptor.

            :param skill_md: Markdown-format descriptor containing an agent skills document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsadditionaldata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                agent_skills_additional_data_property = agentregistry.CfnRegistryRecord.AgentSkillsAdditionalDataProperty(
                    skill_md=agentregistry.CfnRegistryRecord.AgentSkillsMdDescriptorProperty(
                        data="data",
                        data_schema_version="dataSchemaVersion",
                        source=agentregistry.CfnRegistryRecord.SkillMdSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty(
                                url="url"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6c5606d1e396f4b94e586f5e54c97f90c7d135dc36043fbf5824a249d6a5edbc)
                check_type(argname="argument skill_md", value=skill_md, expected_type=type_hints["skill_md"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if skill_md is not None:
                self._values["skill_md"] = skill_md

        @builtins.property
        def skill_md(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.AgentSkillsMdDescriptorProperty"]]:
            '''Markdown-format descriptor containing an agent skills document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsadditionaldata.html#cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillmd
            '''
            result = self._values.get("skill_md")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.AgentSkillsMdDescriptorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgentSkillsAdditionalDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_data": "additionalData",
            "data": "data",
            "data_schema_version": "dataSchemaVersion",
        },
    )
    class AgentSkillsDefinitionDescriptorProperty:
        def __init__(
            self,
            *,
            additional_data: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.AgentSkillsAdditionalDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            data: typing.Optional[builtins.str] = None,
            data_schema_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The agent skills definition descriptor, populated when the record type is SKILL.

            :param additional_data: Additional data associated with an agent skills definition descriptor.
            :param data: Descriptor payload data.
            :param data_schema_version: Version of the descriptor type schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                agent_skills_definition_descriptor_property = agentregistry.CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty(
                    additional_data=agentregistry.CfnRegistryRecord.AgentSkillsAdditionalDataProperty(
                        skill_md=agentregistry.CfnRegistryRecord.AgentSkillsMdDescriptorProperty(
                            data="data",
                            data_schema_version="dataSchemaVersion",
                            source=agentregistry.CfnRegistryRecord.SkillMdSourceProperty(
                                from_url=agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty(
                                    url="url"
                                )
                            )
                        )
                    ),
                    data="data",
                    data_schema_version="dataSchemaVersion"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0160a59fef7e0857e54bf7c152ab962e16b7c1f1864025e6cac6c2aaf7a87b63)
                check_type(argname="argument additional_data", value=additional_data, expected_type=type_hints["additional_data"])
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
                check_type(argname="argument data_schema_version", value=data_schema_version, expected_type=type_hints["data_schema_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if additional_data is not None:
                self._values["additional_data"] = additional_data
            if data is not None:
                self._values["data"] = data
            if data_schema_version is not None:
                self._values["data_schema_version"] = data_schema_version

        @builtins.property
        def additional_data(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.AgentSkillsAdditionalDataProperty"]]:
            '''Additional data associated with an agent skills definition descriptor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor.html#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-additionaldata
            '''
            result = self._values.get("additional_data")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.AgentSkillsAdditionalDataProperty"]], result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''Descriptor payload data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor.html#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_schema_version(self) -> typing.Optional[builtins.str]:
            '''Version of the descriptor type schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor.html#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-dataschemaversion
            '''
            result = self._values.get("data_schema_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgentSkillsDefinitionDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.AgentSkillsMdDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data": "data",
            "data_schema_version": "dataSchemaVersion",
            "source": "source",
        },
    )
    class AgentSkillsMdDescriptorProperty:
        def __init__(
            self,
            *,
            data: typing.Optional[builtins.str] = None,
            data_schema_version: typing.Optional[builtins.str] = None,
            source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.SkillMdSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Markdown-format descriptor containing an agent skills document.

            :param data: Descriptor payload data.
            :param data_schema_version: Version of the descriptor type schema.
            :param source: Source configuration for a SkillMd document. Unlike MCP/A2A sources, SkillMd does not support credential providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsmddescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                agent_skills_md_descriptor_property = agentregistry.CfnRegistryRecord.AgentSkillsMdDescriptorProperty(
                    data="data",
                    data_schema_version="dataSchemaVersion",
                    source=agentregistry.CfnRegistryRecord.SkillMdSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty(
                            url="url"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1ae3cf7a8a04ae74aaedc504cd4c187cc310da85624594b69305579f742ff48a)
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
                check_type(argname="argument data_schema_version", value=data_schema_version, expected_type=type_hints["data_schema_version"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data is not None:
                self._values["data"] = data
            if data_schema_version is not None:
                self._values["data_schema_version"] = data_schema_version
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''Descriptor payload data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsmddescriptor.html#cfn-agentregistry-registryrecord-agentskillsmddescriptor-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_schema_version(self) -> typing.Optional[builtins.str]:
            '''Version of the descriptor type schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsmddescriptor.html#cfn-agentregistry-registryrecord-agentskillsmddescriptor-dataschemaversion
            '''
            result = self._values.get("data_schema_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SkillMdSourceProperty"]]:
            '''Source configuration for a SkillMd document.

            Unlike MCP/A2A sources, SkillMd does not support credential providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-agentskillsmddescriptor.html#cfn-agentregistry-registryrecord-agentskillsmddescriptor-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SkillMdSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgentSkillsMdDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.CustomDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={"data": "data"},
    )
    class CustomDescriptorProperty:
        def __init__(self, *, data: typing.Optional[builtins.str] = None) -> None:
            '''The custom descriptor, populated when the record type is CUSTOM.

            :param data: Descriptor payload data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-customdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                custom_descriptor_property = agentregistry.CfnRegistryRecord.CustomDescriptorProperty(
                    data="data"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a280d6b557483a5ec1b646e580daa3ea76882b95df89d04d9a1cf9ee65387c14)
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''Descriptor payload data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-customdescriptor.html#cfn-agentregistry-registryrecord-customdescriptor-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty",
        jsii_struct_bases=[],
        name_mapping={
            "url": "url",
            "credential_provider_configurations": "credentialProviderConfigurations",
        },
    )
    class DescriptorSourceFromUrlProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            credential_provider_configurations: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''URL-based descriptor source configuration, with credential provider configurations for authenticated URL retrieval.

            :param url: URL source for descriptor content.
            :param credential_provider_configurations: The credential providers used to authenticate when fetching descriptor content from the source URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptorsourcefromurl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                descriptor_source_from_url_property = agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                    url="url",
                
                    # the properties below are optional
                    credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                        credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                            iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                region="region",
                                role_arn="roleArn",
                                service="service"
                            ),
                            oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                provider_arn="providerArn",
                
                                # the properties below are optional
                                custom_parameters={
                                    "custom_parameters_key": "customParameters"
                                },
                                grant_type="grantType",
                                scopes=["scopes"]
                            )
                        ),
                        credential_provider_type="credentialProviderType"
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1eee7c83b8b212382d1a03795116c50adcb47836013c53d7d5d7261019cda6f5)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument credential_provider_configurations", value=credential_provider_configurations, expected_type=type_hints["credential_provider_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url": url,
            }
            if credential_provider_configurations is not None:
                self._values["credential_provider_configurations"] = credential_provider_configurations

        @builtins.property
        def url(self) -> builtins.str:
            '''URL source for descriptor content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptorsourcefromurl.html#cfn-agentregistry-registryrecord-descriptorsourcefromurl-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def credential_provider_configurations(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty"]]]]:
            '''The credential providers used to authenticate when fetching descriptor content from the source URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptorsourcefromurl.html#cfn-agentregistry-registryrecord-descriptorsourcefromurl-credentialproviderconfigurations
            '''
            result = self._values.get("credential_provider_configurations")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DescriptorSourceFromUrlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.DescriptorSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"from_url": "fromUrl"},
    )
    class DescriptorSourceProperty:
        def __init__(
            self,
            *,
            from_url: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.DescriptorSourceFromUrlProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source configuration that defines where descriptor content is retrieved from.

            :param from_url: URL-based descriptor source configuration, with credential provider configurations for authenticated URL retrieval.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptorsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                descriptor_source_property = agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                    from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                        url="url",
                
                        # the properties below are optional
                        credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                            credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                    region="region",
                                    role_arn="roleArn",
                                    service="service"
                                ),
                                oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                    provider_arn="providerArn",
                
                                    # the properties below are optional
                                    custom_parameters={
                                        "custom_parameters_key": "customParameters"
                                    },
                                    grant_type="grantType",
                                    scopes=["scopes"]
                                )
                            ),
                            credential_provider_type="credentialProviderType"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f2f403fe6cb0e29ee4e08fc2b21d38f5362b5ca167d2e899656eb31497fba395)
                check_type(argname="argument from_url", value=from_url, expected_type=type_hints["from_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if from_url is not None:
                self._values["from_url"] = from_url

        @builtins.property
        def from_url(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorSourceFromUrlProperty"]]:
            '''URL-based descriptor source configuration, with credential provider configurations for authenticated URL retrieval.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptorsource.html#cfn-agentregistry-registryrecord-descriptorsource-fromurl
            '''
            result = self._values.get("from_url")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorSourceFromUrlProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DescriptorSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.DescriptorsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "a2_a_agent_card": "a2AAgentCard",
            "agent_skills_definition": "agentSkillsDefinition",
            "agui": "agui",
            "custom": "custom",
            "http": "http",
            "mcp_server": "mcpServer",
        },
    )
    class DescriptorsProperty:
        def __init__(
            self,
            *,
            a2_a_agent_card: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.A2aAgentCardDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            agent_skills_definition: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            agui: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.AgUiDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.CustomDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            http: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.HttpDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.McpServerDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The typed set of descriptors for a registry record.

            Exactly one descriptor field is populated based on the record type.

            :param a2_a_agent_card: The A2A agent card descriptor, populated when the record type is AGENT.
            :param agent_skills_definition: The agent skills definition descriptor, populated when the record type is SKILL.
            :param agui: The AG-UI (Agent-User Interaction) descriptor, populated for records detected from an AG-UI protocol source. This descriptor is source-only: its content is synchronized from the configured source URL rather than supplied inline.
            :param custom: The custom descriptor, populated when the record type is CUSTOM.
            :param http: The HTTP descriptor, populated for records detected from an HTTP protocol source. This descriptor is source-only: its content is synchronized from the configured source URL rather than supplied inline.
            :param mcp_server: The MCP server descriptor, populated when the record type is MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptors.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                descriptors_property = agentregistry.CfnRegistryRecord.DescriptorsProperty(
                    a2_a_agent_card=agentregistry.CfnRegistryRecord.A2aAgentCardDescriptorProperty(
                        data="data",
                        data_schema_version="dataSchemaVersion",
                        source=agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                                url="url",
                
                                # the properties below are optional
                                credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                                    credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                        iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                            region="region",
                                            role_arn="roleArn",
                                            service="service"
                                        ),
                                        oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                            provider_arn="providerArn",
                
                                            # the properties below are optional
                                            custom_parameters={
                                                "custom_parameters_key": "customParameters"
                                            },
                                            grant_type="grantType",
                                            scopes=["scopes"]
                                        )
                                    ),
                                    credential_provider_type="credentialProviderType"
                                )]
                            )
                        )
                    ),
                    agent_skills_definition=agentregistry.CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty(
                        additional_data=agentregistry.CfnRegistryRecord.AgentSkillsAdditionalDataProperty(
                            skill_md=agentregistry.CfnRegistryRecord.AgentSkillsMdDescriptorProperty(
                                data="data",
                                data_schema_version="dataSchemaVersion",
                                source=agentregistry.CfnRegistryRecord.SkillMdSourceProperty(
                                    from_url=agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty(
                                        url="url"
                                    )
                                )
                            )
                        ),
                        data="data",
                        data_schema_version="dataSchemaVersion"
                    ),
                    agui=agentregistry.CfnRegistryRecord.AgUiDescriptorProperty(
                        source=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                                url="url"
                            )
                        )
                    ),
                    custom=agentregistry.CfnRegistryRecord.CustomDescriptorProperty(
                        data="data"
                    ),
                    http=agentregistry.CfnRegistryRecord.HttpDescriptorProperty(
                        source=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                                url="url"
                            )
                        )
                    ),
                    mcp_server=agentregistry.CfnRegistryRecord.McpServerDescriptorProperty(
                        additional_data=agentregistry.CfnRegistryRecord.McpServerAdditionalDataProperty(
                            tools=agentregistry.CfnRegistryRecord.McpToolsDescriptorProperty(
                                data="data",
                                data_schema_version="dataSchemaVersion"
                            )
                        ),
                        data="data",
                        data_schema_version="dataSchemaVersion",
                        source=agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                                url="url",
                
                                # the properties below are optional
                                credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                                    credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                        iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                            region="region",
                                            role_arn="roleArn",
                                            service="service"
                                        ),
                                        oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                            provider_arn="providerArn",
                
                                            # the properties below are optional
                                            custom_parameters={
                                                "custom_parameters_key": "customParameters"
                                            },
                                            grant_type="grantType",
                                            scopes=["scopes"]
                                        )
                                    ),
                                    credential_provider_type="credentialProviderType"
                                )]
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__eeaec09ea09830cf935441309df33f6f79c13bcf622fbbedf0296fbea3603915)
                check_type(argname="argument a2_a_agent_card", value=a2_a_agent_card, expected_type=type_hints["a2_a_agent_card"])
                check_type(argname="argument agent_skills_definition", value=agent_skills_definition, expected_type=type_hints["agent_skills_definition"])
                check_type(argname="argument agui", value=agui, expected_type=type_hints["agui"])
                check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
                check_type(argname="argument http", value=http, expected_type=type_hints["http"])
                check_type(argname="argument mcp_server", value=mcp_server, expected_type=type_hints["mcp_server"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if a2_a_agent_card is not None:
                self._values["a2_a_agent_card"] = a2_a_agent_card
            if agent_skills_definition is not None:
                self._values["agent_skills_definition"] = agent_skills_definition
            if agui is not None:
                self._values["agui"] = agui
            if custom is not None:
                self._values["custom"] = custom
            if http is not None:
                self._values["http"] = http
            if mcp_server is not None:
                self._values["mcp_server"] = mcp_server

        @builtins.property
        def a2_a_agent_card(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.A2aAgentCardDescriptorProperty"]]:
            '''The A2A agent card descriptor, populated when the record type is AGENT.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptors.html#cfn-agentregistry-registryrecord-descriptors-a2aagentcard
            '''
            result = self._values.get("a2_a_agent_card")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.A2aAgentCardDescriptorProperty"]], result)

        @builtins.property
        def agent_skills_definition(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty"]]:
            '''The agent skills definition descriptor, populated when the record type is SKILL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptors.html#cfn-agentregistry-registryrecord-descriptors-agentskillsdefinition
            '''
            result = self._values.get("agent_skills_definition")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty"]], result)

        @builtins.property
        def agui(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.AgUiDescriptorProperty"]]:
            '''The AG-UI (Agent-User Interaction) descriptor, populated for records detected from an AG-UI protocol source.

            This descriptor is source-only: its content is synchronized from the configured source URL rather than supplied inline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptors.html#cfn-agentregistry-registryrecord-descriptors-agui
            '''
            result = self._values.get("agui")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.AgUiDescriptorProperty"]], result)

        @builtins.property
        def custom(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.CustomDescriptorProperty"]]:
            '''The custom descriptor, populated when the record type is CUSTOM.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptors.html#cfn-agentregistry-registryrecord-descriptors-custom
            '''
            result = self._values.get("custom")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.CustomDescriptorProperty"]], result)

        @builtins.property
        def http(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.HttpDescriptorProperty"]]:
            '''The HTTP descriptor, populated for records detected from an HTTP protocol source.

            This descriptor is source-only: its content is synchronized from the configured source URL rather than supplied inline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptors.html#cfn-agentregistry-registryrecord-descriptors-http
            '''
            result = self._values.get("http")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.HttpDescriptorProperty"]], result)

        @builtins.property
        def mcp_server(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.McpServerDescriptorProperty"]]:
            '''The MCP server descriptor, populated when the record type is MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-descriptors.html#cfn-agentregistry-registryrecord-descriptors-mcpserver
            '''
            result = self._values.get("mcp_server")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.McpServerDescriptorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DescriptorsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.HttpDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class HttpDescriptorProperty:
        def __init__(
            self,
            *,
            source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.SourceOnlyDescriptorSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The HTTP descriptor, populated for records detected from an HTTP protocol source.

            This descriptor is source-only: its content is synchronized from the configured source URL rather than supplied inline.

            :param source: Source configuration for a source-only descriptor. Unlike mcpServer/a2aAgentCard sources, source-only descriptors do not support credential providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-httpdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                http_descriptor_property = agentregistry.CfnRegistryRecord.HttpDescriptorProperty(
                    source=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                            url="url"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__3f717a36df278a573d9cdd74a8f17f1cf8ff612b423008872eb5427cd0ba6127)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def source(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SourceOnlyDescriptorSourceProperty"]]:
            '''Source configuration for a source-only descriptor.

            Unlike mcpServer/a2aAgentCard sources, source-only descriptors do not support credential providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-httpdescriptor.html#cfn-agentregistry-registryrecord-httpdescriptor-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SourceOnlyDescriptorSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.McpServerAdditionalDataProperty",
        jsii_struct_bases=[],
        name_mapping={"tools": "tools"},
    )
    class McpServerAdditionalDataProperty:
        def __init__(
            self,
            *,
            tools: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.McpToolsDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Additional data associated with an MCP server descriptor.

            :param tools: The MCP tools descriptor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcpserveradditionaldata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                mcp_server_additional_data_property = agentregistry.CfnRegistryRecord.McpServerAdditionalDataProperty(
                    tools=agentregistry.CfnRegistryRecord.McpToolsDescriptorProperty(
                        data="data",
                        data_schema_version="dataSchemaVersion"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a15bd678a351885a69fa4329f56f9727663705b1e158cba98d48dc7d7106bc4b)
                check_type(argname="argument tools", value=tools, expected_type=type_hints["tools"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if tools is not None:
                self._values["tools"] = tools

        @builtins.property
        def tools(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.McpToolsDescriptorProperty"]]:
            '''The MCP tools descriptor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcpserveradditionaldata.html#cfn-agentregistry-registryrecord-mcpserveradditionaldata-tools
            '''
            result = self._values.get("tools")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.McpToolsDescriptorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "McpServerAdditionalDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.McpServerDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_data": "additionalData",
            "data": "data",
            "data_schema_version": "dataSchemaVersion",
            "source": "source",
        },
    )
    class McpServerDescriptorProperty:
        def __init__(
            self,
            *,
            additional_data: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.McpServerAdditionalDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            data: typing.Optional[builtins.str] = None,
            data_schema_version: typing.Optional[builtins.str] = None,
            source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.DescriptorSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The MCP server descriptor, populated when the record type is MCP.

            :param additional_data: Additional data associated with an MCP server descriptor.
            :param data: Descriptor payload data.
            :param data_schema_version: Version of the descriptor type schema.
            :param source: The source configuration that defines where descriptor content is retrieved from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcpserverdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                mcp_server_descriptor_property = agentregistry.CfnRegistryRecord.McpServerDescriptorProperty(
                    additional_data=agentregistry.CfnRegistryRecord.McpServerAdditionalDataProperty(
                        tools=agentregistry.CfnRegistryRecord.McpToolsDescriptorProperty(
                            data="data",
                            data_schema_version="dataSchemaVersion"
                        )
                    ),
                    data="data",
                    data_schema_version="dataSchemaVersion",
                    source=agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                        from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                            url="url",
                
                            # the properties below are optional
                            credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                                credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                    iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                        region="region",
                                        role_arn="roleArn",
                                        service="service"
                                    ),
                                    oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                        provider_arn="providerArn",
                
                                        # the properties below are optional
                                        custom_parameters={
                                            "custom_parameters_key": "customParameters"
                                        },
                                        grant_type="grantType",
                                        scopes=["scopes"]
                                    )
                                ),
                                credential_provider_type="credentialProviderType"
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0389199c51f09a874e22aad151a72b41a56b44af2343534906165854e9f5bfa8)
                check_type(argname="argument additional_data", value=additional_data, expected_type=type_hints["additional_data"])
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
                check_type(argname="argument data_schema_version", value=data_schema_version, expected_type=type_hints["data_schema_version"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if additional_data is not None:
                self._values["additional_data"] = additional_data
            if data is not None:
                self._values["data"] = data
            if data_schema_version is not None:
                self._values["data_schema_version"] = data_schema_version
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def additional_data(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.McpServerAdditionalDataProperty"]]:
            '''Additional data associated with an MCP server descriptor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcpserverdescriptor.html#cfn-agentregistry-registryrecord-mcpserverdescriptor-additionaldata
            '''
            result = self._values.get("additional_data")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.McpServerAdditionalDataProperty"]], result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''Descriptor payload data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcpserverdescriptor.html#cfn-agentregistry-registryrecord-mcpserverdescriptor-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_schema_version(self) -> typing.Optional[builtins.str]:
            '''Version of the descriptor type schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcpserverdescriptor.html#cfn-agentregistry-registryrecord-mcpserverdescriptor-dataschemaversion
            '''
            result = self._values.get("data_schema_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorSourceProperty"]]:
            '''The source configuration that defines where descriptor content is retrieved from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcpserverdescriptor.html#cfn-agentregistry-registryrecord-mcpserverdescriptor-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "McpServerDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.McpToolsDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={"data": "data", "data_schema_version": "dataSchemaVersion"},
    )
    class McpToolsDescriptorProperty:
        def __init__(
            self,
            *,
            data: typing.Optional[builtins.str] = None,
            data_schema_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The MCP tools descriptor.

            :param data: Descriptor payload data.
            :param data_schema_version: Version of the tools descriptor schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcptoolsdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                mcp_tools_descriptor_property = agentregistry.CfnRegistryRecord.McpToolsDescriptorProperty(
                    data="data",
                    data_schema_version="dataSchemaVersion"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e4c43b5694c40617ea835f766e48eb876d2434232d439bbcfa3583c35dce3c7e)
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
                check_type(argname="argument data_schema_version", value=data_schema_version, expected_type=type_hints["data_schema_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data is not None:
                self._values["data"] = data
            if data_schema_version is not None:
                self._values["data_schema_version"] = data_schema_version

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''Descriptor payload data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcptoolsdescriptor.html#cfn-agentregistry-registryrecord-mcptoolsdescriptor-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_schema_version(self) -> typing.Optional[builtins.str]:
            '''Version of the tools descriptor schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-mcptoolsdescriptor.html#cfn-agentregistry-registryrecord-mcptoolsdescriptor-dataschemaversion
            '''
            result = self._values.get("data_schema_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "McpToolsDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "credential_provider": "credentialProvider",
            "credential_provider_type": "credentialProviderType",
        },
    )
    class RegistryRecordCredentialProviderConfigurationProperty:
        def __init__(
            self,
            *,
            credential_provider: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty", typing.Dict[builtins.str, typing.Any]]],
            credential_provider_type: builtins.str,
        ) -> None:
            '''A credential provider configuration used for authenticated descriptor retrieval.

            :param credential_provider: The credential provider details. Specify exactly one member.
            :param credential_provider_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                registry_record_credential_provider_configuration_property = agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                    credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                        iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                            region="region",
                            role_arn="roleArn",
                            service="service"
                        ),
                        oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                            provider_arn="providerArn",
                
                            # the properties below are optional
                            custom_parameters={
                                "custom_parameters_key": "customParameters"
                            },
                            grant_type="grantType",
                            scopes=["scopes"]
                        )
                    ),
                    credential_provider_type="credentialProviderType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1a1b370274cb9cbf419b51f33da806996fb65f85fe96e8e23f2f24263a727b18)
                check_type(argname="argument credential_provider", value=credential_provider, expected_type=type_hints["credential_provider"])
                check_type(argname="argument credential_provider_type", value=credential_provider_type, expected_type=type_hints["credential_provider_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "credential_provider": credential_provider,
                "credential_provider_type": credential_provider_type,
            }

        @builtins.property
        def credential_provider(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty"]:
            '''The credential provider details.

            Specify exactly one member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration.html#cfn-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-credentialprovider
            '''
            result = self._values.get("credential_provider")
            assert result is not None, "Required property 'credential_provider' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty"], result)

        @builtins.property
        def credential_provider_type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration.html#cfn-agentregistry-registryrecord-registryrecordcredentialproviderconfiguration-credentialprovidertype
            '''
            result = self._values.get("credential_provider_type")
            assert result is not None, "Required property 'credential_provider_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistryRecordCredentialProviderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iam_credential_provider": "iamCredentialProvider",
            "oauth_credential_provider": "oauthCredentialProvider",
        },
    )
    class RegistryRecordCredentialProviderUnionProperty:
        def __init__(
            self,
            *,
            iam_credential_provider: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            oauth_credential_provider: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The credential provider details.

            Specify exactly one member.

            :param iam_credential_provider: IAM credential provider configuration.
            :param oauth_credential_provider: OAuth credential provider configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                registry_record_credential_provider_union_property = agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                    iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                        region="region",
                        role_arn="roleArn",
                        service="service"
                    ),
                    oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                        provider_arn="providerArn",
                
                        # the properties below are optional
                        custom_parameters={
                            "custom_parameters_key": "customParameters"
                        },
                        grant_type="grantType",
                        scopes=["scopes"]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__30d186a8bd943c6bb99ba85034150b39fba31212321b9807feaf41146dae30e0)
                check_type(argname="argument iam_credential_provider", value=iam_credential_provider, expected_type=type_hints["iam_credential_provider"])
                check_type(argname="argument oauth_credential_provider", value=oauth_credential_provider, expected_type=type_hints["oauth_credential_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam_credential_provider is not None:
                self._values["iam_credential_provider"] = iam_credential_provider
            if oauth_credential_provider is not None:
                self._values["oauth_credential_provider"] = oauth_credential_provider

        @builtins.property
        def iam_credential_provider(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty"]]:
            '''IAM credential provider configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion.html#cfn-agentregistry-registryrecord-registryrecordcredentialproviderunion-iamcredentialprovider
            '''
            result = self._values.get("iam_credential_provider")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty"]], result)

        @builtins.property
        def oauth_credential_provider(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty"]]:
            '''OAuth credential provider configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordcredentialproviderunion.html#cfn-agentregistry-registryrecord-registryrecordcredentialproviderunion-oauthcredentialprovider
            '''
            result = self._values.get("oauth_credential_provider")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistryRecordCredentialProviderUnionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"region": "region", "role_arn": "roleArn", "service": "service"},
    )
    class RegistryRecordIamCredentialProviderProperty:
        def __init__(
            self,
            *,
            region: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
            service: typing.Optional[builtins.str] = None,
        ) -> None:
            '''IAM credential provider configuration.

            :param region: The SigV4 signing region.
            :param role_arn: The ARN of the IAM role.
            :param service: The SigV4 signing service name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                registry_record_iam_credential_provider_property = agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                    region="region",
                    role_arn="roleArn",
                    service="service"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a7d07b2a807802353b7eb77ec11d3b9d013f20c4f5fc8ff0a28e4a3738925964)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if region is not None:
                self._values["region"] = region
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if service is not None:
                self._values["service"] = service

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The SigV4 signing region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider.html#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider.html#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service(self) -> typing.Optional[builtins.str]:
            '''The SigV4 signing service name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordiamcredentialprovider.html#cfn-agentregistry-registryrecord-registryrecordiamcredentialprovider-service
            '''
            result = self._values.get("service")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistryRecordIamCredentialProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provider_arn": "providerArn",
            "custom_parameters": "customParameters",
            "grant_type": "grantType",
            "scopes": "scopes",
        },
    )
    class RegistryRecordOAuthCredentialProviderProperty:
        def __init__(
            self,
            *,
            provider_arn: builtins.str,
            custom_parameters: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
            grant_type: typing.Optional[builtins.str] = None,
            scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''OAuth credential provider configuration.

            :param provider_arn: The ARN of the OAuth credential provider.
            :param custom_parameters: Additional custom parameters for the OAuth flow.
            :param grant_type: 
            :param scopes: OAuth scopes to request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                registry_record_o_auth_credential_provider_property = agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                    provider_arn="providerArn",
                
                    # the properties below are optional
                    custom_parameters={
                        "custom_parameters_key": "customParameters"
                    },
                    grant_type="grantType",
                    scopes=["scopes"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__9948428878b83b74af2f15ff81bda2ded5437f03db55af853481abb03b111854)
                check_type(argname="argument provider_arn", value=provider_arn, expected_type=type_hints["provider_arn"])
                check_type(argname="argument custom_parameters", value=custom_parameters, expected_type=type_hints["custom_parameters"])
                check_type(argname="argument grant_type", value=grant_type, expected_type=type_hints["grant_type"])
                check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "provider_arn": provider_arn,
            }
            if custom_parameters is not None:
                self._values["custom_parameters"] = custom_parameters
            if grant_type is not None:
                self._values["grant_type"] = grant_type
            if scopes is not None:
                self._values["scopes"] = scopes

        @builtins.property
        def provider_arn(self) -> builtins.str:
            '''The ARN of the OAuth credential provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider.html#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-providerarn
            '''
            result = self._values.get("provider_arn")
            assert result is not None, "Required property 'provider_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def custom_parameters(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''Additional custom parameters for the OAuth flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider.html#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-customparameters
            '''
            result = self._values.get("custom_parameters")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def grant_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider.html#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-granttype
            '''
            result = self._values.get("grant_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''OAuth scopes to request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-registryrecordoauthcredentialprovider.html#cfn-agentregistry-registryrecord-registryrecordoauthcredentialprovider-scopes
            '''
            result = self._values.get("scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistryRecordOAuthCredentialProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url"},
    )
    class SkillMdSourceFromUrlProperty:
        def __init__(self, *, url: builtins.str) -> None:
            '''URL-based source for SkillMd content (sync is skipped;

            content is provided inline via Data).

            :param url: URL source for the SkillMd document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-skillmdsourcefromurl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                skill_md_source_from_url_property = agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty(
                    url="url"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__36100a2c70034e7269ce98469d7c7e1a48722fe1c424f841ea0238adc9fda700)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url": url,
            }

        @builtins.property
        def url(self) -> builtins.str:
            '''URL source for the SkillMd document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-skillmdsourcefromurl.html#cfn-agentregistry-registryrecord-skillmdsourcefromurl-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SkillMdSourceFromUrlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.SkillMdSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"from_url": "fromUrl"},
    )
    class SkillMdSourceProperty:
        def __init__(
            self,
            *,
            from_url: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.SkillMdSourceFromUrlProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Source configuration for a SkillMd document.

            Unlike MCP/A2A sources, SkillMd does not support credential providers.

            :param from_url: URL-based source for SkillMd content (sync is skipped; content is provided inline via Data).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-skillmdsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                skill_md_source_property = agentregistry.CfnRegistryRecord.SkillMdSourceProperty(
                    from_url=agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty(
                        url="url"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__595c5cb5d6a3c5f7919222fc9acdb5b325682228947228957e5b1f08a4b28878)
                check_type(argname="argument from_url", value=from_url, expected_type=type_hints["from_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if from_url is not None:
                self._values["from_url"] = from_url

        @builtins.property
        def from_url(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SkillMdSourceFromUrlProperty"]]:
            '''URL-based source for SkillMd content (sync is skipped;

            content is provided inline via Data).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-skillmdsource.html#cfn-agentregistry-registryrecord-skillmdsource-fromurl
            '''
            result = self._values.get("from_url")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SkillMdSourceFromUrlProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SkillMdSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url"},
    )
    class SourceOnlyDescriptorSourceFromUrlProperty:
        def __init__(self, *, url: builtins.str) -> None:
            '''URL-based source configuration for a source-only descriptor.

            :param url: URL source for descriptor content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                source_only_descriptor_source_from_url_property = agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                    url="url"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__43e185e48b7d4ebd67afe06f1ef043348d1f6ae2ba84b65c33c6283c40dd8af3)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url": url,
            }

        @builtins.property
        def url(self) -> builtins.str:
            '''URL source for descriptor content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl.html#cfn-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceOnlyDescriptorSourceFromUrlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"from_url": "fromUrl"},
    )
    class SourceOnlyDescriptorSourceProperty:
        def __init__(
            self,
            *,
            from_url: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Source configuration for a source-only descriptor.

            Unlike mcpServer/a2aAgentCard sources, source-only descriptors do not support credential providers.

            :param from_url: URL-based source configuration for a source-only descriptor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_agentregistry as agentregistry
                
                source_only_descriptor_source_property = agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                    from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                        url="url"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__697de4a1d2bd7d5d400c4d0f9f2404a4e812bac51918f0531d571e46f1f07a12)
                check_type(argname="argument from_url", value=from_url, expected_type=type_hints["from_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if from_url is not None:
                self._values["from_url"] = from_url

        @builtins.property
        def from_url(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty"]]:
            '''URL-based source configuration for a source-only descriptor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource.html#cfn-agentregistry-registryrecord-sourceonlydescriptorsource-fromurl
            '''
            result = self._values.get("from_url")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceOnlyDescriptorSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_agentregistry.CfnRegistryRecordProps",
    jsii_struct_bases=[],
    name_mapping={
        "descriptors": "descriptors",
        "name": "name",
        "record_type": "recordType",
        "description": "description",
        "display_name": "displayName",
        "record_version": "recordVersion",
        "registry_id": "registryId",
        "tags": "tags",
    },
)
class CfnRegistryRecordProps:
    def __init__(
        self,
        *,
        descriptors: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnRegistryRecord.DescriptorsProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        record_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        record_version: typing.Optional[builtins.str] = None,
        registry_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRegistryRecord``.

        :param descriptors: The typed set of descriptors for a registry record. Exactly one descriptor field is populated based on the record type.
        :param name: The name of the registry record.
        :param record_type: The type of the registry record.
        :param description: The description of the registry record.
        :param display_name: The human-readable display name of the registry record.
        :param record_version: The version of the registry record.
        :param registry_id: The identifier of the registry in which to create the record. You can specify either the registry ID or the registry Amazon Resource Name (ARN). Use the ARN form to reference a registry shared from another account via AWS Resource Access Manager (RAM).
        :param tags: Tags to assign to the registry record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_agentregistry as agentregistry
            
            cfn_registry_record_props = agentregistry.CfnRegistryRecordProps(
                descriptors=agentregistry.CfnRegistryRecord.DescriptorsProperty(
                    a2_a_agent_card=agentregistry.CfnRegistryRecord.A2aAgentCardDescriptorProperty(
                        data="data",
                        data_schema_version="dataSchemaVersion",
                        source=agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                                url="url",
            
                                # the properties below are optional
                                credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                                    credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                        iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                            region="region",
                                            role_arn="roleArn",
                                            service="service"
                                        ),
                                        oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                            provider_arn="providerArn",
            
                                            # the properties below are optional
                                            custom_parameters={
                                                "custom_parameters_key": "customParameters"
                                            },
                                            grant_type="grantType",
                                            scopes=["scopes"]
                                        )
                                    ),
                                    credential_provider_type="credentialProviderType"
                                )]
                            )
                        )
                    ),
                    agent_skills_definition=agentregistry.CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty(
                        additional_data=agentregistry.CfnRegistryRecord.AgentSkillsAdditionalDataProperty(
                            skill_md=agentregistry.CfnRegistryRecord.AgentSkillsMdDescriptorProperty(
                                data="data",
                                data_schema_version="dataSchemaVersion",
                                source=agentregistry.CfnRegistryRecord.SkillMdSourceProperty(
                                    from_url=agentregistry.CfnRegistryRecord.SkillMdSourceFromUrlProperty(
                                        url="url"
                                    )
                                )
                            )
                        ),
                        data="data",
                        data_schema_version="dataSchemaVersion"
                    ),
                    agui=agentregistry.CfnRegistryRecord.AgUiDescriptorProperty(
                        source=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                                url="url"
                            )
                        )
                    ),
                    custom=agentregistry.CfnRegistryRecord.CustomDescriptorProperty(
                        data="data"
                    ),
                    http=agentregistry.CfnRegistryRecord.HttpDescriptorProperty(
                        source=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty(
                                url="url"
                            )
                        )
                    ),
                    mcp_server=agentregistry.CfnRegistryRecord.McpServerDescriptorProperty(
                        additional_data=agentregistry.CfnRegistryRecord.McpServerAdditionalDataProperty(
                            tools=agentregistry.CfnRegistryRecord.McpToolsDescriptorProperty(
                                data="data",
                                data_schema_version="dataSchemaVersion"
                            )
                        ),
                        data="data",
                        data_schema_version="dataSchemaVersion",
                        source=agentregistry.CfnRegistryRecord.DescriptorSourceProperty(
                            from_url=agentregistry.CfnRegistryRecord.DescriptorSourceFromUrlProperty(
                                url="url",
            
                                # the properties below are optional
                                credential_provider_configurations=[agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty(
                                    credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty(
                                        iam_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty(
                                            region="region",
                                            role_arn="roleArn",
                                            service="service"
                                        ),
                                        oauth_credential_provider=agentregistry.CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty(
                                            provider_arn="providerArn",
            
                                            # the properties below are optional
                                            custom_parameters={
                                                "custom_parameters_key": "customParameters"
                                            },
                                            grant_type="grantType",
                                            scopes=["scopes"]
                                        )
                                    ),
                                    credential_provider_type="credentialProviderType"
                                )]
                            )
                        )
                    )
                ),
                name="name",
                record_type="recordType",
            
                # the properties below are optional
                description="description",
                display_name="displayName",
                record_version="recordVersion",
                registry_id="registryId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__68bc3c29ea26d0372a7ccb8f399a09e4970aca187d9f42a8210b964653061c40)
            check_type(argname="argument descriptors", value=descriptors, expected_type=type_hints["descriptors"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument record_type", value=record_type, expected_type=type_hints["record_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument record_version", value=record_version, expected_type=type_hints["record_version"])
            check_type(argname="argument registry_id", value=registry_id, expected_type=type_hints["registry_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "descriptors": descriptors,
            "name": name,
            "record_type": record_type,
        }
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if record_version is not None:
            self._values["record_version"] = record_version
        if registry_id is not None:
            self._values["registry_id"] = registry_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def descriptors(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorsProperty"]:
        '''The typed set of descriptors for a registry record.

        Exactly one descriptor field is populated based on the record type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html#cfn-agentregistry-registryrecord-descriptors
        '''
        result = self._values.get("descriptors")
        assert result is not None, "Required property 'descriptors' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnRegistryRecord.DescriptorsProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the registry record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html#cfn-agentregistry-registryrecord-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_type(self) -> builtins.str:
        '''The type of the registry record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html#cfn-agentregistry-registryrecord-recordtype
        '''
        result = self._values.get("record_type")
        assert result is not None, "Required property 'record_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the registry record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html#cfn-agentregistry-registryrecord-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The human-readable display name of the registry record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html#cfn-agentregistry-registryrecord-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_version(self) -> typing.Optional[builtins.str]:
        '''The version of the registry record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html#cfn-agentregistry-registryrecord-recordversion
        '''
        result = self._values.get("record_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the registry in which to create the record.

        You can specify either the registry ID or the registry Amazon Resource Name (ARN). Use the ARN form to reference a registry shared from another account via AWS Resource Access Manager (RAM).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html#cfn-agentregistry-registryrecord-registryid
        '''
        result = self._values.get("registry_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to assign to the registry record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-agentregistry-registryrecord.html#cfn-agentregistry-registryrecord-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegistryRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRegistry",
    "CfnRegistryProps",
    "CfnRegistryRecord",
    "CfnRegistryRecordProps",
]

publication.publish()

def _typecheckingstub__c92eab34b9759c9076b623bf33eca391e46a29b4416fcb07c7b30302f1de95b4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    approval_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.ApprovalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    authorizer_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    discovery_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.DiscoveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f807826dcca746eb661237fe74624805a548d2fd0b2754b127a7abcba8e99d64(
    resource: _aws_agentregistry_506fb521.IRegistryRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__106d6487e951bf82b880a23c87994f5240e375c0768d18c5da3364f8d8b9ad83(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3127ad756b133c6ac1a01fb8fb9fa2b74c8fe3ace3578175225748b3ee8dc129(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4f19cc7543f61ed5fe2a8439cd07e7c70758818d19b0543fb92bb89c3fc01f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44903752c8ad92a1a5b3bea748d118e360856827239ffb71ff515dbc7e372da7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82c9cc795b7a19f46589e380713aa8028087b53c881ad5cb72684fb914b42e5(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnRegistry.ApprovalConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ae93a351cc6e0a318dbf92458f45de0b6b96efd086af7f4205c7e00dcd0f56(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b008aa20d30be0120e5d8a8866b7968949e2929088e43770aa94ebee678edbc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a1b96b5514172fb57ca62002ae3be655be2839d81eff8747ebaecd2ee280ce9(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnRegistry.DiscoveryConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f33b3edde8ee2055f274039c2177c20002d6e3d68800b02fd6a5690ffaa15d2(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfda2e2da1494b1ec48d9472528d44ae0527e50e58d3c6145181a36d375c0f85(
    *,
    auto_approval_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed2639db61d2e3af825f1a8f0f3500e04332e0af1dbd729a78477d4e8d1b9edf(
    *,
    custom_jwt_authorizer: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.CustomJWTAuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843a47c7ba9ad382abfec27c682df7bc4ecf3f899d64f8c791c2cd41dd2c198e(
    *,
    claim_match_operator: builtins.str,
    claim_match_value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.ClaimMatchValueTypeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f658ef5b0d03da0e25be1ec309f8cbc63ad52710adbaf23f6f1ae2d5a44eeea8(
    *,
    match_value_string: typing.Optional[builtins.str] = None,
    match_value_string_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c0bec14d64b642472f4ad606c21eb9001da8eee5764d82d0599db783c5b274(
    *,
    authorizing_claim_match_value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.AuthorizingClaimMatchValueTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    inbound_token_claim_name: builtins.str,
    inbound_token_claim_value_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f05f2a0c04cca178fdec7101afb3c703940cffbf41f03ccc78bc9094aab209(
    *,
    discovery_url: builtins.str,
    allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_claims: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.CustomClaimValidationTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0075ca34f0469a75f3909e5eaf6a881ca07aa3e497e1be371bc34bb156576420(
    *,
    authorizer_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b98476a5662bfac6fbe3ddd43ef77bef00711e71c235f99e97057616ec96a16e(
    *,
    name: builtins.str,
    approval_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.ApprovalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    authorizer_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    discovery_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistry.DiscoveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef8b3afdf0d8fa2a57531ae35ed0ed172ca12f519f3a312e79d540a72e88d74(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    descriptors: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.DescriptorsProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    record_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    record_version: typing.Optional[builtins.str] = None,
    registry_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ab8e8cef582bd2d3ec6bd5cfb86ddee72d7c1f0f0131b2b83652803af88d6d(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7361ed8164b5f3cdafa91a2686cb44699f14ff384f55aada32958b17ab5fa04(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8464f2d44da52e9636217c4cc94c48509e2de79509aec4ac8f0c9cc915064df(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e20ed69c19154a1c1c82f76a8fa036f90acfa535493e48813acaf3af97ae1fef(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnRegistryRecord.DescriptorsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dac661425718c0e01f8c2d9f0b486f0cf83ef80ab08988a82ad85f2797e2336(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddafdbd3f82f53f2237ad280e72be884e39e4be52bec5ebb50731242e8bb189f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c6a9aae0bf922e08911fd3846f325f960d7df0f0cbb9e1057371b443377e605(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4837f51052d31d643559b181dcf50bb6914aea97770549487a7166473d6d13df(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c03f3fe0d25f7024efbcefface95c2d9aad0137a0613c75161e23fa68d4a24af(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4a1f651ea2d1dea12707fff754c90bddf57ff13a28d3826dea56199a5971c15(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a039aa0fc4e16e0e8ba645515217334b8560454b55d3da7bfc7de67e70bc46(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa9881107eac84791f3306a270cd236e769c8e820626a2d3fa82a0684e3afbf(
    *,
    data: typing.Optional[builtins.str] = None,
    data_schema_version: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.DescriptorSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14707a1d412fb23aeac570107aa3e17f2d92f3d9d3a1b55108cabaa4ba9f75b(
    *,
    source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.SourceOnlyDescriptorSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c5606d1e396f4b94e586f5e54c97f90c7d135dc36043fbf5824a249d6a5edbc(
    *,
    skill_md: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.AgentSkillsMdDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0160a59fef7e0857e54bf7c152ab962e16b7c1f1864025e6cac6c2aaf7a87b63(
    *,
    additional_data: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.AgentSkillsAdditionalDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data: typing.Optional[builtins.str] = None,
    data_schema_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ae3cf7a8a04ae74aaedc504cd4c187cc310da85624594b69305579f742ff48a(
    *,
    data: typing.Optional[builtins.str] = None,
    data_schema_version: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.SkillMdSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a280d6b557483a5ec1b646e580daa3ea76882b95df89d04d9a1cf9ee65387c14(
    *,
    data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eee7c83b8b212382d1a03795116c50adcb47836013c53d7d5d7261019cda6f5(
    *,
    url: builtins.str,
    credential_provider_configurations: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.RegistryRecordCredentialProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f403fe6cb0e29ee4e08fc2b21d38f5362b5ca167d2e899656eb31497fba395(
    *,
    from_url: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.DescriptorSourceFromUrlProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeaec09ea09830cf935441309df33f6f79c13bcf622fbbedf0296fbea3603915(
    *,
    a2_a_agent_card: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.A2aAgentCardDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    agent_skills_definition: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.AgentSkillsDefinitionDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    agui: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.AgUiDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.CustomDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.HttpDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.McpServerDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f717a36df278a573d9cdd74a8f17f1cf8ff612b423008872eb5427cd0ba6127(
    *,
    source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.SourceOnlyDescriptorSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a15bd678a351885a69fa4329f56f9727663705b1e158cba98d48dc7d7106bc4b(
    *,
    tools: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.McpToolsDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0389199c51f09a874e22aad151a72b41a56b44af2343534906165854e9f5bfa8(
    *,
    additional_data: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.McpServerAdditionalDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data: typing.Optional[builtins.str] = None,
    data_schema_version: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.DescriptorSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4c43b5694c40617ea835f766e48eb876d2434232d439bbcfa3583c35dce3c7e(
    *,
    data: typing.Optional[builtins.str] = None,
    data_schema_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1b370274cb9cbf419b51f33da806996fb65f85fe96e8e23f2f24263a727b18(
    *,
    credential_provider: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.RegistryRecordCredentialProviderUnionProperty, typing.Dict[builtins.str, typing.Any]]],
    credential_provider_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d186a8bd943c6bb99ba85034150b39fba31212321b9807feaf41146dae30e0(
    *,
    iam_credential_provider: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.RegistryRecordIamCredentialProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    oauth_credential_provider: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.RegistryRecordOAuthCredentialProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d07b2a807802353b7eb77ec11d3b9d013f20c4f5fc8ff0a28e4a3738925964(
    *,
    region: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    service: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9948428878b83b74af2f15ff81bda2ded5437f03db55af853481abb03b111854(
    *,
    provider_arn: builtins.str,
    custom_parameters: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    grant_type: typing.Optional[builtins.str] = None,
    scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36100a2c70034e7269ce98469d7c7e1a48722fe1c424f841ea0238adc9fda700(
    *,
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595c5cb5d6a3c5f7919222fc9acdb5b325682228947228957e5b1f08a4b28878(
    *,
    from_url: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.SkillMdSourceFromUrlProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43e185e48b7d4ebd67afe06f1ef043348d1f6ae2ba84b65c33c6283c40dd8af3(
    *,
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697de4a1d2bd7d5d400c4d0f9f2404a4e812bac51918f0531d571e46f1f07a12(
    *,
    from_url: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.SourceOnlyDescriptorSourceFromUrlProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68bc3c29ea26d0372a7ccb8f399a09e4970aca187d9f42a8210b964653061c40(
    *,
    descriptors: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnRegistryRecord.DescriptorsProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    record_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    record_version: typing.Optional[builtins.str] = None,
    registry_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
