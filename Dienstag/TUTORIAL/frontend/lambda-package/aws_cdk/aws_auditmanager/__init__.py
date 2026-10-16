r'''
# AWS::AuditManager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_auditmanager as auditmanager
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AuditManager construct libraries](https://constructs.dev/search?q=auditmanager)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AuditManager resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AuditManager.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AuditManager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AuditManager.html).

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
    import aws_cdk.interfaces.aws_auditmanager as _aws_auditmanager_104d0a27
    import constructs as _constructs_77d1e7e8
else:

    _aws_auditmanager_104d0a27 = _LazyImport("aws_cdk.interfaces.aws_auditmanager")
    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_auditmanager_104d0a27.IAssessmentRef, _aws_cdk_0cae9daa.ITaggable)
class CfnAssessment(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessment",
):
    '''The ``AWS::AuditManager::Assessment`` resource is an Audit Manager resource type that defines the scope of audit evidence collected by Audit Manager .

    An Audit Manager assessment is an implementation of an Audit Manager framework.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html
    :cloudformationResource: AWS::AuditManager::Assessment
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_auditmanager as auditmanager
        
        cfn_assessment = auditmanager.CfnAssessment(self, "MyCfnAssessment",
            assessment_reports_destination=auditmanager.CfnAssessment.AssessmentReportsDestinationProperty(
                destination="destination",
                destination_type="destinationType"
            ),
            aws_account=auditmanager.CfnAssessment.AWSAccountProperty(
                email_address="emailAddress",
                id="id",
                name="name"
            ),
            delegations=[auditmanager.CfnAssessment.DelegationProperty(
                assessment_id="assessmentId",
                assessment_name="assessmentName",
                comment="comment",
                control_set_id="controlSetId",
                created_by="createdBy",
                creation_time=123,
                id="id",
                last_updated=123,
                role_arn="roleArn",
                role_type="roleType",
                status="status"
            )],
            description="description",
            framework_id="frameworkId",
            name="name",
            roles=[auditmanager.CfnAssessment.RoleProperty(
                role_arn="roleArn",
                role_type="roleType"
            )],
            scope=auditmanager.CfnAssessment.ScopeProperty(
                aws_accounts=[auditmanager.CfnAssessment.AWSAccountProperty(
                    email_address="emailAddress",
                    id="id",
                    name="name"
                )],
                aws_services=[auditmanager.CfnAssessment.AWSServiceProperty(
                    service_name="serviceName"
                )]
            ),
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope_: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        assessment_reports_destination: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.AssessmentReportsDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        aws_account: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.AWSAccountProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        delegations: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.DelegationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        framework_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.RoleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        scope: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.ScopeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AuditManager::Assessment``.

        :param scope_: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assessment_reports_destination: The destination that evidence reports are stored in for the assessment.
        :param aws_account: The AWS account that's associated with the assessment.
        :param delegations: The delegations that are associated with the assessment.
        :param description: The description of the assessment.
        :param framework_id: The unique identifier for the framework.
        :param name: The name of the assessment.
        :param roles: The roles that are associated with the assessment.
        :param scope: The wrapper of AWS accounts and services that are in scope for the assessment.
        :param status: The overall status of the assessment. When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` . After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .
        :param tags: The tags that are associated with the assessment.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__92bc07048cc88ff5fa41ca724a6b42a6ae66b35846d9ddafe90b7f4869459869)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssessmentProps(
            assessment_reports_destination=assessment_reports_destination,
            aws_account=aws_account,
            delegations=delegations,
            description=description,
            framework_id=framework_id,
            name=name,
            roles=roles,
            scope=scope,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.member(jsii_name="arnForAssessment")
    @builtins.classmethod
    def arn_for_assessment(
        cls,
        resource: "_aws_auditmanager_104d0a27.IAssessmentRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6c373e86f7061e512a57c2b840038c0c4ba3756e288c2444a46302b913d96fa7)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAssessment", [resource]))

    @jsii.member(jsii_name="fromAssessmentArn")
    @builtins.classmethod
    def from_assessment_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_aws_auditmanager_104d0a27.IAssessmentRef":
        '''Creates a new IAssessmentRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__53998ced82653765b84ddead2a4dff0ff2e45ab68892348e05eacca82bb124dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_aws_auditmanager_104d0a27.IAssessmentRef", jsii.sinvoke(cls, "fromAssessmentArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromAssessmentId")
    @builtins.classmethod
    def from_assessment_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        assessment_id: builtins.str,
    ) -> "_aws_auditmanager_104d0a27.IAssessmentRef":
        '''Creates a new IAssessmentRef from a assessmentId.

        :param scope: -
        :param id: -
        :param assessment_id: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__43eb8aeb11f425b57f8a93b31b847effe83f1e71d092fac1c67aa18396a4326f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument assessment_id", value=assessment_id, expected_type=type_hints["assessment_id"])
        return typing.cast("_aws_auditmanager_104d0a27.IAssessmentRef", jsii.sinvoke(cls, "fromAssessmentId", [scope, id, assessment_id]))

    @jsii.member(jsii_name="isCfnAssessment")
    @builtins.classmethod
    def is_cfn_assessment(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAssessment.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8d188bb015bdf2a874f15ae42351d0799b8abb50a5518190fbdd1333eb7d91e5)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAssessment", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__03e38c1f5231f872be6e5945b84145421d5aa9adad701fbe2da3ed8f537a8bf5)
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
            type_hints = cached_type_hints(_typecheckingstub__dd626e1ad6a0d5f107717ac4ca323d1b906b9108351e5594b9d302c1bae69154)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="assessmentRef")
    def assessment_ref(self) -> "_aws_auditmanager_104d0a27.AssessmentReference":
        '''A reference to a Assessment resource.'''
        return typing.cast("_aws_auditmanager_104d0a27.AssessmentReference", jsii.get(self, "assessmentRef"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the assessment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssessmentId")
    def attr_assessment_id(self) -> builtins.str:
        '''The unique identifier for the assessment.

        :cloudformationAttribute: AssessmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssessmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''Specifies when the assessment was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="assessmentReportsDestination")
    def assessment_reports_destination(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AssessmentReportsDestinationProperty"]]:
        '''The destination that evidence reports are stored in for the assessment.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AssessmentReportsDestinationProperty"]], jsii.get(self, "assessmentReportsDestination"))

    @assessment_reports_destination.setter
    def assessment_reports_destination(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AssessmentReportsDestinationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__00a9fcbfa3098ead8f6f1c39b628055baa8f3551041af9549614bef9d0eec479)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assessmentReportsDestination", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="awsAccount")
    def aws_account(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSAccountProperty"]]:
        '''The AWS account that's associated with the assessment.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSAccountProperty"]], jsii.get(self, "awsAccount"))

    @aws_account.setter
    def aws_account(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSAccountProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d4c9a5d085476d4a7f266e7e7925abc970275daaa2a8ab2752994ba1b1d56a7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="delegations")
    def delegations(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.DelegationProperty"]]]]:
        '''The delegations that are associated with the assessment.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.DelegationProperty"]]]], jsii.get(self, "delegations"))

    @delegations.setter
    def delegations(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.DelegationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__15a841dd635da320c870cbc6ccc893b259bee63a4c1cb3d0d5eb5b4eca87c91f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delegations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assessment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2c3a46125d908b0d8f6065ca7a0882de2fe6c538075a768d5c402884e4f2eded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="frameworkId")
    def framework_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for the framework.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkId"))

    @framework_id.setter
    def framework_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9e3765e6f7654ba597ca3ac6ee42c2eff6328a62c804aa79f5d73df28f4ca70a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the assessment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bddf3ba2ff3de348646c5261f9513f444c4dc05ebd31add93de54e003450e152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.RoleProperty"]]]]:
        '''The roles that are associated with the assessment.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.RoleProperty"]]]], jsii.get(self, "roles"))

    @roles.setter
    def roles(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.RoleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c91699b8b6b6ac6c9b455c5e5ae26c34f37550e436c81f8d9eab91fa5d5aae69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.ScopeProperty"]]:
        '''The wrapper of AWS accounts and services that are in scope for the assessment.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.ScopeProperty"]], jsii.get(self, "scope"))

    @scope.setter
    def scope(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.ScopeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__688a1871cd0766d0092bc2d7f3e18ec40b291fa378ec7291d28d66562fb8ab3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The overall status of the assessment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__740df134275bcc7cb35bd7422ee6421511835cfee5e0bfe601f9659dc9936edb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags that are associated with the assessment.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6ee30b6045910d84a8fae367b39720413cefcdd3486c52a43fc7339254c547e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessment.AWSAccountProperty",
        jsii_struct_bases=[],
        name_mapping={"email_address": "emailAddress", "id": "id", "name": "name"},
    )
    class AWSAccountProperty:
        def __init__(
            self,
            *,
            email_address: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWSAccount`` property type specifies the wrapper of the AWS account details, such as account ID, email address, and so on.

            :param email_address: The email address that's associated with the AWS account .
            :param id: The identifier for the AWS account .
            :param name: The name of the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_auditmanager as auditmanager
                
                a_ws_account_property = auditmanager.CfnAssessment.AWSAccountProperty(
                    email_address="emailAddress",
                    id="id",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__4f7b167f5d0d3e87b47b374fa360cd63ca43512f6941baaff8c85f7da884d337)
                check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email_address is not None:
                self._values["email_address"] = email_address
            if id is not None:
                self._values["id"] = id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def email_address(self) -> typing.Optional[builtins.str]:
            '''The email address that's associated with the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-emailaddress
            '''
            result = self._values.get("email_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AWSAccountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessment.AWSServiceProperty",
        jsii_struct_bases=[],
        name_mapping={"service_name": "serviceName"},
    )
    class AWSServiceProperty:
        def __init__(
            self,
            *,
            service_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWSService`` property type specifies an AWS service such as Amazon S3 , AWS CloudTrail , and so on.

            :param service_name: The name of the AWS service .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_auditmanager as auditmanager
                
                a_ws_service_property = auditmanager.CfnAssessment.AWSServiceProperty(
                    service_name="serviceName"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0fab7f0ba2096e4c65ed9aaad93bc90c679e144aa2e9f6d6ce11f068aa44cf49)
                check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if service_name is not None:
                self._values["service_name"] = service_name

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            '''The name of the AWS service .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html#cfn-auditmanager-assessment-awsservice-servicename
            '''
            result = self._values.get("service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AWSServiceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessment.AssessmentReportsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "destination_type": "destinationType",
        },
    )
    class AssessmentReportsDestinationProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
            destination_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AssessmentReportsDestination`` property type specifies the location in which AWS Audit Manager saves assessment reports for the given assessment.

            :param destination: The destination bucket where Audit Manager stores assessment reports.
            :param destination_type: The destination type, such as Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_auditmanager as auditmanager
                
                assessment_reports_destination_property = auditmanager.CfnAssessment.AssessmentReportsDestinationProperty(
                    destination="destination",
                    destination_type="destinationType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2c7f539a3c8f0db3468c968e44bd2431f6fb6ab31cbd6d142b3b970fe575d84f)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if destination_type is not None:
                self._values["destination_type"] = destination_type

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            '''The destination bucket where Audit Manager stores assessment reports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html#cfn-auditmanager-assessment-assessmentreportsdestination-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_type(self) -> typing.Optional[builtins.str]:
            '''The destination type, such as Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html#cfn-auditmanager-assessment-assessmentreportsdestination-destinationtype
            '''
            result = self._values.get("destination_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssessmentReportsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessment.DelegationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "assessment_id": "assessmentId",
            "assessment_name": "assessmentName",
            "comment": "comment",
            "control_set_id": "controlSetId",
            "created_by": "createdBy",
            "creation_time": "creationTime",
            "id": "id",
            "last_updated": "lastUpdated",
            "role_arn": "roleArn",
            "role_type": "roleType",
            "status": "status",
        },
    )
    class DelegationProperty:
        def __init__(
            self,
            *,
            assessment_id: typing.Optional[builtins.str] = None,
            assessment_name: typing.Optional[builtins.str] = None,
            comment: typing.Optional[builtins.str] = None,
            control_set_id: typing.Optional[builtins.str] = None,
            created_by: typing.Optional[builtins.str] = None,
            creation_time: typing.Optional[jsii.Number] = None,
            id: typing.Optional[builtins.str] = None,
            last_updated: typing.Optional[jsii.Number] = None,
            role_arn: typing.Optional[builtins.str] = None,
            role_type: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``Delegation`` property type specifies the assignment of a control set to a delegate for review.

            :param assessment_id: The identifier for the assessment that's associated with the delegation.
            :param assessment_name: The name of the assessment that's associated with the delegation.
            :param comment: The comment that's related to the delegation.
            :param control_set_id: The identifier for the control set that's associated with the delegation.
            :param created_by: The user or role that created the delegation. *Minimum* : ``1`` *Maximum* : ``100`` *Pattern* : ``^[a-zA-Z0-9-_()\\\\[\\\\]\\\\s]+$``
            :param creation_time: Specifies when the delegation was created.
            :param id: The unique identifier for the delegation.
            :param last_updated: Specifies when the delegation was last updated.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role.
            :param role_type: The type of customer persona. .. epigraph:: In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .
            :param status: The status of the delegation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_auditmanager as auditmanager
                
                delegation_property = auditmanager.CfnAssessment.DelegationProperty(
                    assessment_id="assessmentId",
                    assessment_name="assessmentName",
                    comment="comment",
                    control_set_id="controlSetId",
                    created_by="createdBy",
                    creation_time=123,
                    id="id",
                    last_updated=123,
                    role_arn="roleArn",
                    role_type="roleType",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__60cb5c0bcb9b4cce0c1ca2b06175feea6ad552567c139d59de4c612ba279b1f0)
                check_type(argname="argument assessment_id", value=assessment_id, expected_type=type_hints["assessment_id"])
                check_type(argname="argument assessment_name", value=assessment_name, expected_type=type_hints["assessment_name"])
                check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
                check_type(argname="argument control_set_id", value=control_set_id, expected_type=type_hints["control_set_id"])
                check_type(argname="argument created_by", value=created_by, expected_type=type_hints["created_by"])
                check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument last_updated", value=last_updated, expected_type=type_hints["last_updated"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument role_type", value=role_type, expected_type=type_hints["role_type"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if assessment_id is not None:
                self._values["assessment_id"] = assessment_id
            if assessment_name is not None:
                self._values["assessment_name"] = assessment_name
            if comment is not None:
                self._values["comment"] = comment
            if control_set_id is not None:
                self._values["control_set_id"] = control_set_id
            if created_by is not None:
                self._values["created_by"] = created_by
            if creation_time is not None:
                self._values["creation_time"] = creation_time
            if id is not None:
                self._values["id"] = id
            if last_updated is not None:
                self._values["last_updated"] = last_updated
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if role_type is not None:
                self._values["role_type"] = role_type
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def assessment_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the assessment that's associated with the delegation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-assessmentid
            '''
            result = self._values.get("assessment_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def assessment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the assessment that's associated with the delegation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-assessmentname
            '''
            result = self._values.get("assessment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            '''The comment that's related to the delegation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-comment
            '''
            result = self._values.get("comment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def control_set_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the control set that's associated with the delegation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-controlsetid
            '''
            result = self._values.get("control_set_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_by(self) -> typing.Optional[builtins.str]:
            '''The user or role that created the delegation.

            *Minimum* : ``1``

            *Maximum* : ``100``

            *Pattern* : ``^[a-zA-Z0-9-_()\\\\[\\\\]\\\\s]+$``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-createdby
            '''
            result = self._values.get("created_by")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def creation_time(self) -> typing.Optional[jsii.Number]:
            '''Specifies when the delegation was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-creationtime
            '''
            result = self._values.get("creation_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for the delegation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_updated(self) -> typing.Optional[jsii.Number]:
            '''Specifies when the delegation was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-lastupdated
            '''
            result = self._values.get("last_updated")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_type(self) -> typing.Optional[builtins.str]:
            '''The type of customer persona.

            .. epigraph::

               In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` .

               In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` .

               In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-roletype
            '''
            result = self._values.get("role_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the delegation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DelegationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessment.RoleProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "role_type": "roleType"},
    )
    class RoleProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            role_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``Role`` property type specifies the wrapper that contains AWS Audit Manager role information, such as the role type and IAM Amazon Resource Name (ARN).

            :param role_arn: The Amazon Resource Name (ARN) of the IAM role.
            :param role_type: The type of customer persona. .. epigraph:: In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_auditmanager as auditmanager
                
                role_property = auditmanager.CfnAssessment.RoleProperty(
                    role_arn="roleArn",
                    role_type="roleType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6122f7bde5ea2efe470ba306cc1eb0fe229ae0c1b9a31abd502b087e5a7c0b1a)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument role_type", value=role_type, expected_type=type_hints["role_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if role_type is not None:
                self._values["role_type"] = role_type

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html#cfn-auditmanager-assessment-role-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_type(self) -> typing.Optional[builtins.str]:
            '''The type of customer persona.

            .. epigraph::

               In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` .

               In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` .

               In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html#cfn-auditmanager-assessment-role-roletype
            '''
            result = self._values.get("role_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessment.ScopeProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_accounts": "awsAccounts", "aws_services": "awsServices"},
    )
    class ScopeProperty:
        def __init__(
            self,
            *,
            aws_accounts: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.AWSAccountProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            aws_services: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.AWSServiceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``Scope`` property type specifies the wrapper that contains the AWS accounts and services that are in scope for the assessment.

            :param aws_accounts: The AWS accounts that are included in the scope of the assessment.
            :param aws_services: The AWS services that are included in the scope of the assessment. .. epigraph:: This API parameter is no longer supported. If you use this parameter to specify one or more AWS services , Audit Manager ignores this input. Instead, the value for ``awsServices`` will show as empty.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_auditmanager as auditmanager
                
                scope_property = auditmanager.CfnAssessment.ScopeProperty(
                    aws_accounts=[auditmanager.CfnAssessment.AWSAccountProperty(
                        email_address="emailAddress",
                        id="id",
                        name="name"
                    )],
                    aws_services=[auditmanager.CfnAssessment.AWSServiceProperty(
                        service_name="serviceName"
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__05fcd83833b2ad06bd1bbfa294b9e1cfa8cbd4951ac7be53a7318918671273e4)
                check_type(argname="argument aws_accounts", value=aws_accounts, expected_type=type_hints["aws_accounts"])
                check_type(argname="argument aws_services", value=aws_services, expected_type=type_hints["aws_services"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_accounts is not None:
                self._values["aws_accounts"] = aws_accounts
            if aws_services is not None:
                self._values["aws_services"] = aws_services

        @builtins.property
        def aws_accounts(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSAccountProperty"]]]]:
            '''The AWS accounts that are included in the scope of the assessment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html#cfn-auditmanager-assessment-scope-awsaccounts
            '''
            result = self._values.get("aws_accounts")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSAccountProperty"]]]], result)

        @builtins.property
        def aws_services(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSServiceProperty"]]]]:
            '''The AWS services that are included in the scope of the assessment.

            .. epigraph::

               This API parameter is no longer supported. If you use this parameter to specify one or more AWS services , Audit Manager ignores this input. Instead, the value for ``awsServices`` will show as empty.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html#cfn-auditmanager-assessment-scope-awsservices
            '''
            result = self._values.get("aws_services")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSServiceProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScopeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_auditmanager_104d0a27.IAssessmentFrameworkRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnAssessmentFramework(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessmentFramework",
):
    '''Creates a custom framework in AWS Audit Manager.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessmentframework.html
    :cloudformationResource: AWS::AuditManager::AssessmentFramework
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_auditmanager as auditmanager
        
        cfn_assessment_framework = auditmanager.CfnAssessmentFramework(self, "MyCfnAssessmentFramework",
            control_sets=[auditmanager.CfnAssessmentFramework.ControlSetProperty(
                controls=[auditmanager.CfnAssessmentFramework.ControlSetControlProperty(
                    id="id"
                )],
                name="name"
            )],
            name="name",
        
            # the properties below are optional
            compliance_type="complianceType",
            description="description",
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
        control_sets: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessmentFramework.ControlSetProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        compliance_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AuditManager::AssessmentFramework``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param control_sets: The control sets that are associated with the framework.
        :param name: The name of the framework.
        :param compliance_type: The compliance type that the framework supports, such as CIS or HIPAA.
        :param description: The description of the framework.
        :param tags: The tags associated with the framework.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1238a7c7f997fc97830516d2d0e575345411edc6eace16d37e76453e51eb6113)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssessmentFrameworkProps(
            control_sets=control_sets,
            name=name,
            compliance_type=compliance_type,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAssessmentFramework")
    @builtins.classmethod
    def arn_for_assessment_framework(
        cls,
        resource: "_aws_auditmanager_104d0a27.IAssessmentFrameworkRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8a7418fea1c7c65bfb4a13254311609906ecc6b0de26699ce39621aa47c912a9)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAssessmentFramework", [resource]))

    @jsii.member(jsii_name="isCfnAssessmentFramework")
    @builtins.classmethod
    def is_cfn_assessment_framework(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAssessmentFramework.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fc5c0a85fa3581033d83034e0c21866ff83f4f72c034b51e6ff7349a73e9cebc)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAssessmentFramework", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__41cecd75886781ba608b6e1ba28350af7a3119659c49c756a5cc27f398dbc2ef)
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
            type_hints = cached_type_hints(_typecheckingstub__b741ddc3e6f0b8b8371d88e9af2f01105aec47284644d438ba8773f341a62a32)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="assessmentFrameworkRef")
    def assessment_framework_ref(
        self,
    ) -> "_aws_auditmanager_104d0a27.AssessmentFrameworkReference":
        '''A reference to a AssessmentFramework resource.'''
        return typing.cast("_aws_auditmanager_104d0a27.AssessmentFrameworkReference", jsii.get(self, "assessmentFrameworkRef"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the framework.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time when the framework was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The user or role that created the framework.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrFrameworkId")
    def attr_framework_id(self) -> builtins.str:
        '''The unique identifier for the framework.

        :cloudformationAttribute: FrameworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFrameworkId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time when the framework was most recently updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedBy")
    def attr_last_updated_by(self) -> builtins.str:
        '''The user or role that most recently updated the framework.

        :cloudformationAttribute: LastUpdatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The framework type, such as a standard framework or a custom framework.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

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
    @jsii.member(jsii_name="controlSets")
    def control_sets(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessmentFramework.ControlSetProperty"]]]:
        '''The control sets that are associated with the framework.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessmentFramework.ControlSetProperty"]]], jsii.get(self, "controlSets"))

    @control_sets.setter
    def control_sets(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessmentFramework.ControlSetProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b012fe7006c2e4be392fe167796061f9c5fe30972564e1f0fd01039c3c98afe6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "controlSets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the framework.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__08b095c3ba4a4d5a56a58b779a44cbede3a9436705695e691fc8a2c29e00b0b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="complianceType")
    def compliance_type(self) -> typing.Optional[builtins.str]:
        '''The compliance type that the framework supports, such as CIS or HIPAA.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceType"))

    @compliance_type.setter
    def compliance_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2ff254a9dfe767e44703ddf2aedde7c5ded65f5710a3dbb18c1fe931c14f1bb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "complianceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the framework.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__628b6b1c53ea797a988273286273c6b081736073253d75ce680ba8e38a1449d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags associated with the framework.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a3426d895ed1da5fcd852aeb51db469aa99e2fbf9120c57efd6b7e2b6648e12e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessmentFramework.ControlSetControlProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class ControlSetControlProperty:
        def __init__(self, *, id: builtins.str) -> None:
            '''A reference to an existing control by ID.

            :param id: The unique identifier of the control.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessmentframework-controlsetcontrol.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_auditmanager as auditmanager
                
                control_set_control_property = auditmanager.CfnAssessmentFramework.ControlSetControlProperty(
                    id="id"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__fbc97ca4808d77aa0afd095af34642b4728425747c34d23e13c04fd90bd3f7ff)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The unique identifier of the control.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessmentframework-controlsetcontrol.html#cfn-auditmanager-assessmentframework-controlsetcontrol-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ControlSetControlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessmentFramework.ControlSetProperty",
        jsii_struct_bases=[],
        name_mapping={"controls": "controls", "name": "name"},
    )
    class ControlSetProperty:
        def __init__(
            self,
            *,
            controls: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessmentFramework.ControlSetControlProperty", typing.Dict[builtins.str, typing.Any]]]]],
            name: builtins.str,
        ) -> None:
            '''A control set entity that represents a collection of controls in Audit Manager.

            :param controls: The list of controls within the control set.
            :param name: The name of the control set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessmentframework-controlset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_auditmanager as auditmanager
                
                control_set_property = auditmanager.CfnAssessmentFramework.ControlSetProperty(
                    controls=[auditmanager.CfnAssessmentFramework.ControlSetControlProperty(
                        id="id"
                    )],
                    name="name"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__3e2d224aba0b37af95b037821f3b28b16980a6c7adcecffc4371cf11d2de6793)
                check_type(argname="argument controls", value=controls, expected_type=type_hints["controls"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "controls": controls,
                "name": name,
            }

        @builtins.property
        def controls(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessmentFramework.ControlSetControlProperty"]]]:
            '''The list of controls within the control set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessmentframework-controlset.html#cfn-auditmanager-assessmentframework-controlset-controls
            '''
            result = self._values.get("controls")
            assert result is not None, "Required property 'controls' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessmentFramework.ControlSetControlProperty"]]], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the control set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessmentframework-controlset.html#cfn-auditmanager-assessmentframework-controlset-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ControlSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessmentFrameworkProps",
    jsii_struct_bases=[],
    name_mapping={
        "control_sets": "controlSets",
        "name": "name",
        "compliance_type": "complianceType",
        "description": "description",
        "tags": "tags",
    },
)
class CfnAssessmentFrameworkProps:
    def __init__(
        self,
        *,
        control_sets: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessmentFramework.ControlSetProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        compliance_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssessmentFramework``.

        :param control_sets: The control sets that are associated with the framework.
        :param name: The name of the framework.
        :param compliance_type: The compliance type that the framework supports, such as CIS or HIPAA.
        :param description: The description of the framework.
        :param tags: The tags associated with the framework.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessmentframework.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_auditmanager as auditmanager
            
            cfn_assessment_framework_props = auditmanager.CfnAssessmentFrameworkProps(
                control_sets=[auditmanager.CfnAssessmentFramework.ControlSetProperty(
                    controls=[auditmanager.CfnAssessmentFramework.ControlSetControlProperty(
                        id="id"
                    )],
                    name="name"
                )],
                name="name",
            
                # the properties below are optional
                compliance_type="complianceType",
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d5ec8716a5409f59c614fa67763a2ac1aab33d2d63771c02587c3b753a1caf16)
            check_type(argname="argument control_sets", value=control_sets, expected_type=type_hints["control_sets"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument compliance_type", value=compliance_type, expected_type=type_hints["compliance_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "control_sets": control_sets,
            "name": name,
        }
        if compliance_type is not None:
            self._values["compliance_type"] = compliance_type
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def control_sets(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessmentFramework.ControlSetProperty"]]]:
        '''The control sets that are associated with the framework.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessmentframework.html#cfn-auditmanager-assessmentframework-controlsets
        '''
        result = self._values.get("control_sets")
        assert result is not None, "Required property 'control_sets' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessmentFramework.ControlSetProperty"]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the framework.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessmentframework.html#cfn-auditmanager-assessmentframework-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compliance_type(self) -> typing.Optional[builtins.str]:
        '''The compliance type that the framework supports, such as CIS or HIPAA.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessmentframework.html#cfn-auditmanager-assessmentframework-compliancetype
        '''
        result = self._values.get("compliance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the framework.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessmentframework.html#cfn-auditmanager-assessmentframework-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags associated with the framework.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessmentframework.html#cfn-auditmanager-assessmentframework-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssessmentFrameworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_auditmanager.CfnAssessmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "assessment_reports_destination": "assessmentReportsDestination",
        "aws_account": "awsAccount",
        "delegations": "delegations",
        "description": "description",
        "framework_id": "frameworkId",
        "name": "name",
        "roles": "roles",
        "scope": "scope",
        "status": "status",
        "tags": "tags",
    },
)
class CfnAssessmentProps:
    def __init__(
        self,
        *,
        assessment_reports_destination: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.AssessmentReportsDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        aws_account: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.AWSAccountProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        delegations: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.DelegationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        framework_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.RoleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        scope: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAssessment.ScopeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssessment``.

        :param assessment_reports_destination: The destination that evidence reports are stored in for the assessment.
        :param aws_account: The AWS account that's associated with the assessment.
        :param delegations: The delegations that are associated with the assessment.
        :param description: The description of the assessment.
        :param framework_id: The unique identifier for the framework.
        :param name: The name of the assessment.
        :param roles: The roles that are associated with the assessment.
        :param scope: The wrapper of AWS accounts and services that are in scope for the assessment.
        :param status: The overall status of the assessment. When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` . After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .
        :param tags: The tags that are associated with the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_auditmanager as auditmanager
            
            cfn_assessment_props = auditmanager.CfnAssessmentProps(
                assessment_reports_destination=auditmanager.CfnAssessment.AssessmentReportsDestinationProperty(
                    destination="destination",
                    destination_type="destinationType"
                ),
                aws_account=auditmanager.CfnAssessment.AWSAccountProperty(
                    email_address="emailAddress",
                    id="id",
                    name="name"
                ),
                delegations=[auditmanager.CfnAssessment.DelegationProperty(
                    assessment_id="assessmentId",
                    assessment_name="assessmentName",
                    comment="comment",
                    control_set_id="controlSetId",
                    created_by="createdBy",
                    creation_time=123,
                    id="id",
                    last_updated=123,
                    role_arn="roleArn",
                    role_type="roleType",
                    status="status"
                )],
                description="description",
                framework_id="frameworkId",
                name="name",
                roles=[auditmanager.CfnAssessment.RoleProperty(
                    role_arn="roleArn",
                    role_type="roleType"
                )],
                scope=auditmanager.CfnAssessment.ScopeProperty(
                    aws_accounts=[auditmanager.CfnAssessment.AWSAccountProperty(
                        email_address="emailAddress",
                        id="id",
                        name="name"
                    )],
                    aws_services=[auditmanager.CfnAssessment.AWSServiceProperty(
                        service_name="serviceName"
                    )]
                ),
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2850511e546d810588bf13d31b8000ce88bdb15623b9e2fb6677d33dba4aa4c5)
            check_type(argname="argument assessment_reports_destination", value=assessment_reports_destination, expected_type=type_hints["assessment_reports_destination"])
            check_type(argname="argument aws_account", value=aws_account, expected_type=type_hints["aws_account"])
            check_type(argname="argument delegations", value=delegations, expected_type=type_hints["delegations"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument framework_id", value=framework_id, expected_type=type_hints["framework_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assessment_reports_destination is not None:
            self._values["assessment_reports_destination"] = assessment_reports_destination
        if aws_account is not None:
            self._values["aws_account"] = aws_account
        if delegations is not None:
            self._values["delegations"] = delegations
        if description is not None:
            self._values["description"] = description
        if framework_id is not None:
            self._values["framework_id"] = framework_id
        if name is not None:
            self._values["name"] = name
        if roles is not None:
            self._values["roles"] = roles
        if scope is not None:
            self._values["scope"] = scope
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assessment_reports_destination(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AssessmentReportsDestinationProperty"]]:
        '''The destination that evidence reports are stored in for the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-assessmentreportsdestination
        '''
        result = self._values.get("assessment_reports_destination")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AssessmentReportsDestinationProperty"]], result)

    @builtins.property
    def aws_account(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSAccountProperty"]]:
        '''The AWS account that's associated with the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-awsaccount
        '''
        result = self._values.get("aws_account")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.AWSAccountProperty"]], result)

    @builtins.property
    def delegations(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.DelegationProperty"]]]]:
        '''The delegations that are associated with the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-delegations
        '''
        result = self._values.get("delegations")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.DelegationProperty"]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def framework_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for the framework.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-frameworkid
        '''
        result = self._values.get("framework_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.RoleProperty"]]]]:
        '''The roles that are associated with the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.RoleProperty"]]]], result)

    @builtins.property
    def scope(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.ScopeProperty"]]:
        '''The wrapper of AWS accounts and services that are in scope for the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-scope
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAssessment.ScopeProperty"]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The overall status of the assessment.

        When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` .

        After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags that are associated with the assessment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssessmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssessment",
    "CfnAssessmentFramework",
    "CfnAssessmentFrameworkProps",
    "CfnAssessmentProps",
]

publication.publish()

def _typecheckingstub__92bc07048cc88ff5fa41ca724a6b42a6ae66b35846d9ddafe90b7f4869459869(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assessment_reports_destination: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.AssessmentReportsDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    aws_account: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.AWSAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delegations: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.DelegationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    framework_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.RoleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    scope: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c373e86f7061e512a57c2b840038c0c4ba3756e288c2444a46302b913d96fa7(
    resource: _aws_auditmanager_104d0a27.IAssessmentRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53998ced82653765b84ddead2a4dff0ff2e45ab68892348e05eacca82bb124dc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43eb8aeb11f425b57f8a93b31b847effe83f1e71d092fac1c67aa18396a4326f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    assessment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d188bb015bdf2a874f15ae42351d0799b8abb50a5518190fbdd1333eb7d91e5(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e38c1f5231f872be6e5945b84145421d5aa9adad701fbe2da3ed8f537a8bf5(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd626e1ad6a0d5f107717ac4ca323d1b906b9108351e5594b9d302c1bae69154(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a9fcbfa3098ead8f6f1c39b628055baa8f3551041af9549614bef9d0eec479(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnAssessment.AssessmentReportsDestinationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c9a5d085476d4a7f266e7e7925abc970275daaa2a8ab2752994ba1b1d56a7f(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnAssessment.AWSAccountProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a841dd635da320c870cbc6ccc893b259bee63a4c1cb3d0d5eb5b4eca87c91f(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnAssessment.DelegationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c3a46125d908b0d8f6065ca7a0882de2fe6c538075a768d5c402884e4f2eded(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e3765e6f7654ba597ca3ac6ee42c2eff6328a62c804aa79f5d73df28f4ca70a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bddf3ba2ff3de348646c5261f9513f444c4dc05ebd31add93de54e003450e152(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c91699b8b6b6ac6c9b455c5e5ae26c34f37550e436c81f8d9eab91fa5d5aae69(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnAssessment.RoleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__688a1871cd0766d0092bc2d7f3e18ec40b291fa378ec7291d28d66562fb8ab3e(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnAssessment.ScopeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740df134275bcc7cb35bd7422ee6421511835cfee5e0bfe601f9659dc9936edb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee30b6045910d84a8fae367b39720413cefcdd3486c52a43fc7339254c547e0(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7b167f5d0d3e87b47b374fa360cd63ca43512f6941baaff8c85f7da884d337(
    *,
    email_address: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fab7f0ba2096e4c65ed9aaad93bc90c679e144aa2e9f6d6ce11f068aa44cf49(
    *,
    service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7f539a3c8f0db3468c968e44bd2431f6fb6ab31cbd6d142b3b970fe575d84f(
    *,
    destination: typing.Optional[builtins.str] = None,
    destination_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60cb5c0bcb9b4cce0c1ca2b06175feea6ad552567c139d59de4c612ba279b1f0(
    *,
    assessment_id: typing.Optional[builtins.str] = None,
    assessment_name: typing.Optional[builtins.str] = None,
    comment: typing.Optional[builtins.str] = None,
    control_set_id: typing.Optional[builtins.str] = None,
    created_by: typing.Optional[builtins.str] = None,
    creation_time: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    last_updated: typing.Optional[jsii.Number] = None,
    role_arn: typing.Optional[builtins.str] = None,
    role_type: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6122f7bde5ea2efe470ba306cc1eb0fe229ae0c1b9a31abd502b087e5a7c0b1a(
    *,
    role_arn: typing.Optional[builtins.str] = None,
    role_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05fcd83833b2ad06bd1bbfa294b9e1cfa8cbd4951ac7be53a7318918671273e4(
    *,
    aws_accounts: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.AWSAccountProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    aws_services: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.AWSServiceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1238a7c7f997fc97830516d2d0e575345411edc6eace16d37e76453e51eb6113(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    control_sets: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessmentFramework.ControlSetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    compliance_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a7418fea1c7c65bfb4a13254311609906ecc6b0de26699ce39621aa47c912a9(
    resource: _aws_auditmanager_104d0a27.IAssessmentFrameworkRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5c0a85fa3581033d83034e0c21866ff83f4f72c034b51e6ff7349a73e9cebc(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41cecd75886781ba608b6e1ba28350af7a3119659c49c756a5cc27f398dbc2ef(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b741ddc3e6f0b8b8371d88e9af2f01105aec47284644d438ba8773f341a62a32(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b012fe7006c2e4be392fe167796061f9c5fe30972564e1f0fd01039c3c98afe6(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnAssessmentFramework.ControlSetProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08b095c3ba4a4d5a56a58b779a44cbede3a9436705695e691fc8a2c29e00b0b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff254a9dfe767e44703ddf2aedde7c5ded65f5710a3dbb18c1fe931c14f1bb7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__628b6b1c53ea797a988273286273c6b081736073253d75ce680ba8e38a1449d3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3426d895ed1da5fcd852aeb51db469aa99e2fbf9120c57efd6b7e2b6648e12e(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbc97ca4808d77aa0afd095af34642b4728425747c34d23e13c04fd90bd3f7ff(
    *,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2d224aba0b37af95b037821f3b28b16980a6c7adcecffc4371cf11d2de6793(
    *,
    controls: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessmentFramework.ControlSetControlProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5ec8716a5409f59c614fa67763a2ac1aab33d2d63771c02587c3b753a1caf16(
    *,
    control_sets: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessmentFramework.ControlSetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    compliance_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2850511e546d810588bf13d31b8000ce88bdb15623b9e2fb6677d33dba4aa4c5(
    *,
    assessment_reports_destination: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.AssessmentReportsDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    aws_account: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.AWSAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delegations: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.DelegationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    framework_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.RoleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    scope: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAssessment.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
