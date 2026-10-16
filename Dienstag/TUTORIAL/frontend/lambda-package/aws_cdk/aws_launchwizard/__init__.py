r'''
# AWS::LaunchWizard Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_launchwizard as launchwizard
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LaunchWizard construct libraries](https://constructs.dev/search?q=launchwizard)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LaunchWizard resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LaunchWizard.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LaunchWizard](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LaunchWizard.html).

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
    import aws_cdk.interfaces.aws_launchwizard as _aws_launchwizard_9b12b495
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_launchwizard_9b12b495 = _LazyImport("aws_cdk.interfaces.aws_launchwizard")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_launchwizard_9b12b495.IDeploymentRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnDeployment(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_launchwizard.CfnDeployment",
):
    '''Creates a deployment for the given workload.

    Deployments created by this operation are not available in the Launch Wizard console to use the ``Clone deployment`` action on.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html
    :cloudformationResource: AWS::LaunchWizard::Deployment
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_launchwizard as launchwizard
        
        cfn_deployment = launchwizard.CfnDeployment(self, "MyCfnDeployment",
            deployment_pattern_name="deploymentPatternName",
            name="name",
            workload_name="workloadName",
        
            # the properties below are optional
            specifications={
                "specifications_key": "specifications"
            },
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
        deployment_pattern_name: builtins.str,
        name: builtins.str,
        workload_name: builtins.str,
        specifications: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::LaunchWizard::Deployment``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param deployment_pattern_name: The name of the deployment pattern.
        :param name: The name of the deployment.
        :param workload_name: The name of the workload.
        :param specifications: The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see `SAP deployment specifications <https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html>`_ . To retrieve the specifications required to create a deployment for other workloads, use the ```GetWorkloadDeploymentPattern`` <https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html>`_ operation.
        :param tags: Information about the tags attached to a deployment.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fe77ed4e81ab71d948f0b03ed5f8780bcc2f324a23805bc45e7eef5f9137ded1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentProps(
            deployment_pattern_name=deployment_pattern_name,
            name=name,
            workload_name=workload_name,
            specifications=specifications,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDeployment")
    @builtins.classmethod
    def arn_for_deployment(
        cls,
        resource: "_aws_launchwizard_9b12b495.IDeploymentRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__568a48adc369ee7d93157209ab196d4f495c58158a475e203141da4dce6b7146)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDeployment", [resource]))

    @jsii.member(jsii_name="isCfnDeployment")
    @builtins.classmethod
    def is_cfn_deployment(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDeployment.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__90de14867b6d31f72487da50ba5b54d98d91d9be5ff80c8429f04142ed7fb886)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDeployment", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d7f3e6794e1a2bf9096acd5b62e08b5fc91decb983d7f694ca0d44580c781e51)
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
            type_hints = cached_type_hints(_typecheckingstub__fcfcdfea35cf6cb8ac79e3e1ec3fcf3c8fe447be5f525eff497dbc69d38de67b)
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
        '''The Amazon Resource Name (ARN) of the deployment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time the deployment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDeletedAt")
    def attr_deleted_at(self) -> builtins.str:
        '''The time the deployment was deleted.

        :cloudformationAttribute: DeletedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeletedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDeploymentId")
    def attr_deployment_id(self) -> builtins.str:
        '''The ID of the deployment.

        :cloudformationAttribute: DeploymentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeploymentId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceGroup")
    def attr_resource_group(self) -> builtins.str:
        '''The resource group of the deployment.

        :cloudformationAttribute: ResourceGroup
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceGroup"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the deployment.

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
    @jsii.member(jsii_name="deploymentRef")
    def deployment_ref(self) -> "_aws_launchwizard_9b12b495.DeploymentReference":
        '''A reference to a Deployment resource.'''
        return typing.cast("_aws_launchwizard_9b12b495.DeploymentReference", jsii.get(self, "deploymentRef"))

    @builtins.property
    @jsii.member(jsii_name="deploymentPatternName")
    def deployment_pattern_name(self) -> builtins.str:
        '''The name of the deployment pattern.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentPatternName"))

    @deployment_pattern_name.setter
    def deployment_pattern_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__04c6045841669ffb1a4272a23741926c40913ef41f644914958b8ffb8b0820be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentPatternName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the deployment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c0094e37b81e5d8f0b6e42001fe8da7cf6d149317e4ef32b73e5cef5a82aee61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workloadName")
    def workload_name(self) -> builtins.str:
        '''The name of the workload.'''
        return typing.cast(builtins.str, jsii.get(self, "workloadName"))

    @workload_name.setter
    def workload_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4ddbc17d8abf4c6daba412028f139c421c42d9da86f2e5b12d5b5a149a84c309)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workloadName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="specifications")
    def specifications(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
        '''The settings specified for the deployment.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "specifications"))

    @specifications.setter
    def specifications(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6343321573b3c3c84666431fb123811dbd97cb11a86c65d6c6d7d4c669c25d86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "specifications", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Information about the tags attached to a deployment.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__057665c8ffa5f5cdaedcf0301e727d15ee8b0244807853f59c72aadbb741357d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_launchwizard.CfnDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_pattern_name": "deploymentPatternName",
        "name": "name",
        "workload_name": "workloadName",
        "specifications": "specifications",
        "tags": "tags",
    },
)
class CfnDeploymentProps:
    def __init__(
        self,
        *,
        deployment_pattern_name: builtins.str,
        name: builtins.str,
        workload_name: builtins.str,
        specifications: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeployment``.

        :param deployment_pattern_name: The name of the deployment pattern.
        :param name: The name of the deployment.
        :param workload_name: The name of the workload.
        :param specifications: The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see `SAP deployment specifications <https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html>`_ . To retrieve the specifications required to create a deployment for other workloads, use the ```GetWorkloadDeploymentPattern`` <https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html>`_ operation.
        :param tags: Information about the tags attached to a deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_launchwizard as launchwizard
            
            cfn_deployment_props = launchwizard.CfnDeploymentProps(
                deployment_pattern_name="deploymentPatternName",
                name="name",
                workload_name="workloadName",
            
                # the properties below are optional
                specifications={
                    "specifications_key": "specifications"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a6e25238aa51033c6bfd52d31380bf8d8789e604e540fcfff33c0df8b15dcdcf)
            check_type(argname="argument deployment_pattern_name", value=deployment_pattern_name, expected_type=type_hints["deployment_pattern_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument workload_name", value=workload_name, expected_type=type_hints["workload_name"])
            check_type(argname="argument specifications", value=specifications, expected_type=type_hints["specifications"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_pattern_name": deployment_pattern_name,
            "name": name,
            "workload_name": workload_name,
        }
        if specifications is not None:
            self._values["specifications"] = specifications
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def deployment_pattern_name(self) -> builtins.str:
        '''The name of the deployment pattern.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-deploymentpatternname
        '''
        result = self._values.get("deployment_pattern_name")
        assert result is not None, "Required property 'deployment_pattern_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workload_name(self) -> builtins.str:
        '''The name of the workload.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-workloadname
        '''
        result = self._values.get("workload_name")
        assert result is not None, "Required property 'workload_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def specifications(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
        '''The settings specified for the deployment.

        These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see `SAP deployment specifications <https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html>`_ . To retrieve the specifications required to create a deployment for other workloads, use the ```GetWorkloadDeploymentPattern`` <https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html>`_ operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-specifications
        '''
        result = self._values.get("specifications")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Information about the tags attached to a deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDeployment",
    "CfnDeploymentProps",
]

publication.publish()

def _typecheckingstub__fe77ed4e81ab71d948f0b03ed5f8780bcc2f324a23805bc45e7eef5f9137ded1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deployment_pattern_name: builtins.str,
    name: builtins.str,
    workload_name: builtins.str,
    specifications: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__568a48adc369ee7d93157209ab196d4f495c58158a475e203141da4dce6b7146(
    resource: _aws_launchwizard_9b12b495.IDeploymentRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90de14867b6d31f72487da50ba5b54d98d91d9be5ff80c8429f04142ed7fb886(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f3e6794e1a2bf9096acd5b62e08b5fc91decb983d7f694ca0d44580c781e51(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcfcdfea35cf6cb8ac79e3e1ec3fcf3c8fe447be5f525eff497dbc69d38de67b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04c6045841669ffb1a4272a23741926c40913ef41f644914958b8ffb8b0820be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0094e37b81e5d8f0b6e42001fe8da7cf6d149317e4ef32b73e5cef5a82aee61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ddbc17d8abf4c6daba412028f139c421c42d9da86f2e5b12d5b5a149a84c309(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6343321573b3c3c84666431fb123811dbd97cb11a86c65d6c6d7d4c669c25d86(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057665c8ffa5f5cdaedcf0301e727d15ee8b0244807853f59c72aadbb741357d(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6e25238aa51033c6bfd52d31380bf8d8789e604e540fcfff33c0df8b15dcdcf(
    *,
    deployment_pattern_name: builtins.str,
    name: builtins.str,
    workload_name: builtins.str,
    specifications: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
