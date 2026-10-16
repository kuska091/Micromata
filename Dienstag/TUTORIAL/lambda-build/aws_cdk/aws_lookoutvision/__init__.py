r'''
# AWS::LookoutVision Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_lookoutvision as lookoutvision
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LookoutVision construct libraries](https://constructs.dev/search?q=lookoutvision)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LookoutVision resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LookoutVision.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LookoutVision](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LookoutVision.html).

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
    import aws_cdk.interfaces.aws_lookoutvision as _aws_lookoutvision_d3e2cc05
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_lookoutvision_d3e2cc05 = _LazyImport("aws_cdk.interfaces.aws_lookoutvision")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_lookoutvision_d3e2cc05.IProjectRef)
class CfnProject(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lookoutvision.CfnProject",
):
    '''The ``AWS::LookoutVision::Project`` type creates an Amazon Lookout for Vision project.

    A project is a grouping of the resources needed to create and manage an Amazon Lookout for Vision model.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutvision-project.html
    :cloudformationResource: AWS::LookoutVision::Project
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lookoutvision as lookoutvision
        
        cfn_project = lookoutvision.CfnProject(self, "MyCfnProject",
            project_name="projectName"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        project_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::LookoutVision::Project``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param project_name: The name of the project.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ae1299eb5a9daafd09ff98ba3e3d4056e110dde110eef801bc1e296150ee6402)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(project_name=project_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForProject")
    @builtins.classmethod
    def arn_for_project(
        cls,
        resource: "_aws_lookoutvision_d3e2cc05.IProjectRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__749f23ba01f7fdc53827fbcb401d225323cb8f419099c89a9c4caf4a7b7b5090)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForProject", [resource]))

    @jsii.member(jsii_name="fromProjectArn")
    @builtins.classmethod
    def from_project_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_aws_lookoutvision_d3e2cc05.IProjectRef":
        '''Creates a new IProjectRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__84fff196233367990984dbde8dbe8aa8640b040153a13a4a883d4f0528c0f0ca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_aws_lookoutvision_d3e2cc05.IProjectRef", jsii.sinvoke(cls, "fromProjectArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromProjectName")
    @builtins.classmethod
    def from_project_name(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        project_name: builtins.str,
    ) -> "_aws_lookoutvision_d3e2cc05.IProjectRef":
        '''Creates a new IProjectRef from a projectName.

        :param scope: -
        :param id: -
        :param project_name: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__10d2b4dda47960ca6ee5e6df8c5e0d918819f580de3bd335e8522dea923180a2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
        return typing.cast("_aws_lookoutvision_d3e2cc05.IProjectRef", jsii.sinvoke(cls, "fromProjectName", [scope, id, project_name]))

    @jsii.member(jsii_name="isCfnProject")
    @builtins.classmethod
    def is_cfn_project(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnProject.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3e45bbfda2feb9cb819883025c071612a0b025c74b1cf57bd52a95248afffb6e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnProject", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__03b76078beb0180f06779d0a685dd8192d3a9f806bb489debf20ab767476c7b0)
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
            type_hints = cached_type_hints(_typecheckingstub__2d2835be554706a29b78410620f8f7eb59e8aafb9dde76f11633c087b0abf80e)
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
        '''Returns the Amazon Resource Name of the project.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "_aws_lookoutvision_d3e2cc05.ProjectReference":
        '''A reference to a Project resource.'''
        return typing.cast("_aws_lookoutvision_d3e2cc05.ProjectReference", jsii.get(self, "projectRef"))

    @builtins.property
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        '''The name of the project.'''
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e1f4170a767549b8248365a6b8ae0370362abd74419aadf2a50d24ecce2482cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectName", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lookoutvision.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={"project_name": "projectName"},
)
class CfnProjectProps:
    def __init__(self, *, project_name: builtins.str) -> None:
        '''Properties for defining a ``CfnProject``.

        :param project_name: The name of the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutvision-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lookoutvision as lookoutvision
            
            cfn_project_props = lookoutvision.CfnProjectProps(
                project_name="projectName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__30a54c5cb3bf96801bcf6422c9ea63dac484a231684d0a4383d059386e74ea5a)
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_name": project_name,
        }

    @builtins.property
    def project_name(self) -> builtins.str:
        '''The name of the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutvision-project.html#cfn-lookoutvision-project-projectname
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnProject",
    "CfnProjectProps",
]

publication.publish()

def _typecheckingstub__ae1299eb5a9daafd09ff98ba3e3d4056e110dde110eef801bc1e296150ee6402(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__749f23ba01f7fdc53827fbcb401d225323cb8f419099c89a9c4caf4a7b7b5090(
    resource: _aws_lookoutvision_d3e2cc05.IProjectRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84fff196233367990984dbde8dbe8aa8640b040153a13a4a883d4f0528c0f0ca(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10d2b4dda47960ca6ee5e6df8c5e0d918819f580de3bd335e8522dea923180a2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    project_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e45bbfda2feb9cb819883025c071612a0b025c74b1cf57bd52a95248afffb6e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b76078beb0180f06779d0a685dd8192d3a9f806bb489debf20ab767476c7b0(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d2835be554706a29b78410620f8f7eb59e8aafb9dde76f11633c087b0abf80e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f4170a767549b8248365a6b8ae0370362abd74419aadf2a50d24ecce2482cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a54c5cb3bf96801bcf6422c9ea63dac484a231684d0a4383d059386e74ea5a(
    *,
    project_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
