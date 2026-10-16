r'''
# AWS::DRS Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_drs as drs
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DRS construct libraries](https://constructs.dev/search?q=drs)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DRS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DRS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DRS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DRS.html).

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
    import aws_cdk.interfaces.aws_drs as _aws_drs_f93ad3cc
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_drs_f93ad3cc = _LazyImport("aws_cdk.interfaces.aws_drs")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_drs_f93ad3cc.ILaunchConfigurationTemplateRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnLaunchConfigurationTemplate(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_drs.CfnLaunchConfigurationTemplate",
):
    '''Account level Launch Configuration Template for AWS Elastic Disaster Recovery.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html
    :cloudformationResource: AWS::DRS::LaunchConfigurationTemplate
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_drs as drs
        
        cfn_launch_configuration_template = drs.CfnLaunchConfigurationTemplate(self, "MyCfnLaunchConfigurationTemplate",
            copy_private_ip=False,
            copy_tags=False,
            export_bucket_arn="exportBucketArn",
            launch_disposition="launchDisposition",
            launch_into_source_instance=False,
            licensing=drs.CfnLaunchConfigurationTemplate.LicensingProperty(
                os_byol=False
            ),
            post_launch_enabled=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_instance_type_right_sizing_method="targetInstanceTypeRightSizingMethod"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        copy_private_ip: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        copy_tags: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        export_bucket_arn: typing.Optional[builtins.str] = None,
        launch_disposition: typing.Optional[builtins.str] = None,
        launch_into_source_instance: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        licensing: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLaunchConfigurationTemplate.LicensingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        post_launch_enabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        target_instance_type_right_sizing_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DRS::LaunchConfigurationTemplate``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param copy_private_ip: Copy private IP.
        :param copy_tags: Copy tags.
        :param export_bucket_arn: S3 bucket ARN to export Source Network templates.
        :param launch_disposition: Launch disposition.
        :param launch_into_source_instance: DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.
        :param licensing: Configuration of a machine's license.
        :param post_launch_enabled: Whether we want to activate post-launch actions.
        :param tags: A set of tags associated with the Launch Configuration Template.
        :param target_instance_type_right_sizing_method: Target instance type right-sizing method.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aa8ff51d4bc35cc1b9c10672fa5e444c0b4ae98dd54bb25556b71f1cc6ed1564)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLaunchConfigurationTemplateProps(
            copy_private_ip=copy_private_ip,
            copy_tags=copy_tags,
            export_bucket_arn=export_bucket_arn,
            launch_disposition=launch_disposition,
            launch_into_source_instance=launch_into_source_instance,
            licensing=licensing,
            post_launch_enabled=post_launch_enabled,
            tags=tags,
            target_instance_type_right_sizing_method=target_instance_type_right_sizing_method,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLaunchConfigurationTemplate")
    @builtins.classmethod
    def arn_for_launch_configuration_template(
        cls,
        resource: "_aws_drs_f93ad3cc.ILaunchConfigurationTemplateRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__20f5796515a0d18c918fd55a0efbe528b59b5708d8a3cba32faac50f9916707e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForLaunchConfigurationTemplate", [resource]))

    @jsii.member(jsii_name="isCfnLaunchConfigurationTemplate")
    @builtins.classmethod
    def is_cfn_launch_configuration_template(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnLaunchConfigurationTemplate.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__972657d6c5ffd08d47a8696faf43ebaf768d171eb41531d8a32cc6c3af7d468e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnLaunchConfigurationTemplate", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__09de5c948b603f3b90cdf308a6a00618bcc3ffab118bf1178b2c4c20ae6e4acf)
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
            type_hints = cached_type_hints(_typecheckingstub__1eb62626008db57a4ef674c9c182d76df959c65c27541cbb7852ed412122c9a6)
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
        '''ARN of the Launch Configuration Template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLaunchConfigurationTemplateId")
    def attr_launch_configuration_template_id(self) -> builtins.str:
        '''ID of the Launch Configuration Template.

        :cloudformationAttribute: LaunchConfigurationTemplateID
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLaunchConfigurationTemplateId"))

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
    @jsii.member(jsii_name="launchConfigurationTemplateRef")
    def launch_configuration_template_ref(
        self,
    ) -> "_aws_drs_f93ad3cc.LaunchConfigurationTemplateReference":
        '''A reference to a LaunchConfigurationTemplate resource.'''
        return typing.cast("_aws_drs_f93ad3cc.LaunchConfigurationTemplateReference", jsii.get(self, "launchConfigurationTemplateRef"))

    @builtins.property
    @jsii.member(jsii_name="copyPrivateIp")
    def copy_private_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Copy private IP.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "copyPrivateIp"))

    @copy_private_ip.setter
    def copy_private_ip(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a1aa7f1a07d1a658a87015c8b9a8b3cec51f6757e962ca458d987f235293f9d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyPrivateIp", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="copyTags")
    def copy_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Copy tags.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "copyTags"))

    @copy_tags.setter
    def copy_tags(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__70a6d8c93566902c86d567de0e0d0f62afc517a46150ca55b191d33b14d64d69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="exportBucketArn")
    def export_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''S3 bucket ARN to export Source Network templates.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exportBucketArn"))

    @export_bucket_arn.setter
    def export_bucket_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__efe75f9e3d80ebb7e330714aa7d29d4c99ec0a6255a9b565f8b5bfa234454b55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exportBucketArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="launchDisposition")
    def launch_disposition(self) -> typing.Optional[builtins.str]:
        '''Launch disposition.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchDisposition"))

    @launch_disposition.setter
    def launch_disposition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5ed2a8b92ba5fdafb1e79da16817441ccea9813f07696d10f22522258fb268e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchDisposition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="launchIntoSourceInstance")
    def launch_into_source_instance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "launchIntoSourceInstance"))

    @launch_into_source_instance.setter
    def launch_into_source_instance(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7df55d93dd7061ca6e2a1edb4af542742d4fbedb59faab33e05c85efce0f28c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchIntoSourceInstance", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licensing")
    def licensing(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLaunchConfigurationTemplate.LicensingProperty"]]:
        '''Configuration of a machine's license.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLaunchConfigurationTemplate.LicensingProperty"]], jsii.get(self, "licensing"))

    @licensing.setter
    def licensing(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLaunchConfigurationTemplate.LicensingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fb062602853e904726706b0c170040510ca9fd5ccedacf0b49a6e2705d90ff15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licensing", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="postLaunchEnabled")
    def post_launch_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether we want to activate post-launch actions.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "postLaunchEnabled"))

    @post_launch_enabled.setter
    def post_launch_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a52efad8e137262b5c482fe9732b6c7b038112ef59adf75aecc31fc9b91dade6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postLaunchEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A set of tags associated with the Launch Configuration Template.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ec54180f516d9cd81a76b12ec81f4c0234b54023f4ca1bbf2e3354739e569356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetInstanceTypeRightSizingMethod")
    def target_instance_type_right_sizing_method(self) -> typing.Optional[builtins.str]:
        '''Target instance type right-sizing method.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInstanceTypeRightSizingMethod"))

    @target_instance_type_right_sizing_method.setter
    def target_instance_type_right_sizing_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a349c2c41d641939164deb1bccab4953985727bc96b2b6356730f04e4b0de787)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetInstanceTypeRightSizingMethod", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_drs.CfnLaunchConfigurationTemplate.LicensingProperty",
        jsii_struct_bases=[],
        name_mapping={"os_byol": "osByol"},
    )
    class LicensingProperty:
        def __init__(
            self,
            *,
            os_byol: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        ) -> None:
            '''Configuration of a machine's license.

            :param os_byol: Whether to enable Bring your own license or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-drs-launchconfigurationtemplate-licensing.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_drs as drs
                
                licensing_property = drs.CfnLaunchConfigurationTemplate.LicensingProperty(
                    os_byol=False
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__54b8314b015d3d894a0a733f1f8ecb51b858a376e41a63929bd4b5fefb1b32f5)
                check_type(argname="argument os_byol", value=os_byol, expected_type=type_hints["os_byol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if os_byol is not None:
                self._values["os_byol"] = os_byol

        @builtins.property
        def os_byol(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether to enable Bring your own license or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-drs-launchconfigurationtemplate-licensing.html#cfn-drs-launchconfigurationtemplate-licensing-osbyol
            '''
            result = self._values.get("os_byol")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicensingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_drs.CfnLaunchConfigurationTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "copy_private_ip": "copyPrivateIp",
        "copy_tags": "copyTags",
        "export_bucket_arn": "exportBucketArn",
        "launch_disposition": "launchDisposition",
        "launch_into_source_instance": "launchIntoSourceInstance",
        "licensing": "licensing",
        "post_launch_enabled": "postLaunchEnabled",
        "tags": "tags",
        "target_instance_type_right_sizing_method": "targetInstanceTypeRightSizingMethod",
    },
)
class CfnLaunchConfigurationTemplateProps:
    def __init__(
        self,
        *,
        copy_private_ip: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        copy_tags: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        export_bucket_arn: typing.Optional[builtins.str] = None,
        launch_disposition: typing.Optional[builtins.str] = None,
        launch_into_source_instance: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        licensing: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLaunchConfigurationTemplate.LicensingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        post_launch_enabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        target_instance_type_right_sizing_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLaunchConfigurationTemplate``.

        :param copy_private_ip: Copy private IP.
        :param copy_tags: Copy tags.
        :param export_bucket_arn: S3 bucket ARN to export Source Network templates.
        :param launch_disposition: Launch disposition.
        :param launch_into_source_instance: DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.
        :param licensing: Configuration of a machine's license.
        :param post_launch_enabled: Whether we want to activate post-launch actions.
        :param tags: A set of tags associated with the Launch Configuration Template.
        :param target_instance_type_right_sizing_method: Target instance type right-sizing method.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_drs as drs
            
            cfn_launch_configuration_template_props = drs.CfnLaunchConfigurationTemplateProps(
                copy_private_ip=False,
                copy_tags=False,
                export_bucket_arn="exportBucketArn",
                launch_disposition="launchDisposition",
                launch_into_source_instance=False,
                licensing=drs.CfnLaunchConfigurationTemplate.LicensingProperty(
                    os_byol=False
                ),
                post_launch_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_instance_type_right_sizing_method="targetInstanceTypeRightSizingMethod"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dc6299d4436191a20483f05c03c88fc1c894497d78685edf856ee5c4d0e6a2d7)
            check_type(argname="argument copy_private_ip", value=copy_private_ip, expected_type=type_hints["copy_private_ip"])
            check_type(argname="argument copy_tags", value=copy_tags, expected_type=type_hints["copy_tags"])
            check_type(argname="argument export_bucket_arn", value=export_bucket_arn, expected_type=type_hints["export_bucket_arn"])
            check_type(argname="argument launch_disposition", value=launch_disposition, expected_type=type_hints["launch_disposition"])
            check_type(argname="argument launch_into_source_instance", value=launch_into_source_instance, expected_type=type_hints["launch_into_source_instance"])
            check_type(argname="argument licensing", value=licensing, expected_type=type_hints["licensing"])
            check_type(argname="argument post_launch_enabled", value=post_launch_enabled, expected_type=type_hints["post_launch_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_instance_type_right_sizing_method", value=target_instance_type_right_sizing_method, expected_type=type_hints["target_instance_type_right_sizing_method"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if copy_private_ip is not None:
            self._values["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            self._values["copy_tags"] = copy_tags
        if export_bucket_arn is not None:
            self._values["export_bucket_arn"] = export_bucket_arn
        if launch_disposition is not None:
            self._values["launch_disposition"] = launch_disposition
        if launch_into_source_instance is not None:
            self._values["launch_into_source_instance"] = launch_into_source_instance
        if licensing is not None:
            self._values["licensing"] = licensing
        if post_launch_enabled is not None:
            self._values["post_launch_enabled"] = post_launch_enabled
        if tags is not None:
            self._values["tags"] = tags
        if target_instance_type_right_sizing_method is not None:
            self._values["target_instance_type_right_sizing_method"] = target_instance_type_right_sizing_method

    @builtins.property
    def copy_private_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Copy private IP.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-copyprivateip
        '''
        result = self._values.get("copy_private_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def copy_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Copy tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-copytags
        '''
        result = self._values.get("copy_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def export_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''S3 bucket ARN to export Source Network templates.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-exportbucketarn
        '''
        result = self._values.get("export_bucket_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_disposition(self) -> typing.Optional[builtins.str]:
        '''Launch disposition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-launchdisposition
        '''
        result = self._values.get("launch_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_into_source_instance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-launchintosourceinstance
        '''
        result = self._values.get("launch_into_source_instance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def licensing(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLaunchConfigurationTemplate.LicensingProperty"]]:
        '''Configuration of a machine's license.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-licensing
        '''
        result = self._values.get("licensing")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLaunchConfigurationTemplate.LicensingProperty"]], result)

    @builtins.property
    def post_launch_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether we want to activate post-launch actions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-postlaunchenabled
        '''
        result = self._values.get("post_launch_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A set of tags associated with the Launch Configuration Template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def target_instance_type_right_sizing_method(self) -> typing.Optional[builtins.str]:
        '''Target instance type right-sizing method.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-launchconfigurationtemplate.html#cfn-drs-launchconfigurationtemplate-targetinstancetyperightsizingmethod
        '''
        result = self._values.get("target_instance_type_right_sizing_method")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchConfigurationTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_drs_f93ad3cc.IReplicationConfigurationTemplateRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnReplicationConfigurationTemplate(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_drs.CfnReplicationConfigurationTemplate",
):
    '''A replication configuration template for AWS Elastic Disaster Recovery Service.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html
    :cloudformationResource: AWS::DRS::ReplicationConfigurationTemplate
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_drs as drs
        
        cfn_replication_configuration_template = drs.CfnReplicationConfigurationTemplate(self, "MyCfnReplicationConfigurationTemplate",
            bandwidth_throttling=123,
            ebs_encryption="ebsEncryption",
            pit_policy=[drs.CfnReplicationConfigurationTemplate.PITPolicyRuleProperty(
                interval=123,
                retention_duration=123,
                units="units",
        
                # the properties below are optional
                enabled=False,
                rule_id=123
            )],
            replication_servers_security_groups_i_ds=["replicationServersSecurityGroupsIDs"],
            staging_area_subnet_id="stagingAreaSubnetId",
            staging_area_tags={
                "staging_area_tags_key": "stagingAreaTags"
            },
        
            # the properties below are optional
            associate_default_security_group=False,
            auto_replicate_new_disks=False,
            create_public_ip=False,
            data_plane_routing="dataPlaneRouting",
            default_large_staging_disk_type="defaultLargeStagingDiskType",
            ebs_encryption_key_arn="ebsEncryptionKeyArn",
            internet_protocol="internetProtocol",
            replication_server_instance_type="replicationServerInstanceType",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            use_dedicated_replication_server=False
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        bandwidth_throttling: jsii.Number,
        ebs_encryption: builtins.str,
        pit_policy: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnReplicationConfigurationTemplate.PITPolicyRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        replication_servers_security_groups_i_ds: typing.Sequence[builtins.str],
        staging_area_subnet_id: builtins.str,
        staging_area_tags: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]],
        associate_default_security_group: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        auto_replicate_new_disks: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        create_public_ip: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        data_plane_routing: typing.Optional[builtins.str] = None,
        default_large_staging_disk_type: typing.Optional[builtins.str] = None,
        ebs_encryption_key_arn: typing.Optional[builtins.str] = None,
        internet_protocol: typing.Optional[builtins.str] = None,
        replication_server_instance_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        use_dedicated_replication_server: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
    ) -> None:
        '''Create a new ``AWS::DRS::ReplicationConfigurationTemplate``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bandwidth_throttling: Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.
        :param ebs_encryption: The type of EBS encryption to be used during replication.
        :param pit_policy: The Point in time (PIT) policy to manage snapshots taken during replication.
        :param replication_servers_security_groups_i_ds: The security group IDs that will be used by the replication server.
        :param staging_area_subnet_id: The subnet to be used by the replication staging area.
        :param staging_area_tags: A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.
        :param associate_default_security_group: Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.
        :param auto_replicate_new_disks: Whether to allow the AWS replication agent to automatically replicate newly added disks.
        :param create_public_ip: Whether to create a Public IP for the Recovery Instance by default.
        :param data_plane_routing: The data plane routing mechanism that will be used for replication.
        :param default_large_staging_disk_type: The Staging Disk EBS volume type to be used during replication.
        :param ebs_encryption_key_arn: The ARN of the EBS encryption key to be used during replication.
        :param internet_protocol: Which version of the Internet Protocol to use for replication of data.
        :param replication_server_instance_type: The instance type to be used for the replication server.
        :param tags: A set of tags to be associated with the Replication Configuration Template resource.
        :param use_dedicated_replication_server: Whether to use a dedicated Replication Server in the replication staging area.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__473112b770609ad0a9ab2476be9e574caab7570c7e292a51ac8b977aa569dc47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationConfigurationTemplateProps(
            bandwidth_throttling=bandwidth_throttling,
            ebs_encryption=ebs_encryption,
            pit_policy=pit_policy,
            replication_servers_security_groups_i_ds=replication_servers_security_groups_i_ds,
            staging_area_subnet_id=staging_area_subnet_id,
            staging_area_tags=staging_area_tags,
            associate_default_security_group=associate_default_security_group,
            auto_replicate_new_disks=auto_replicate_new_disks,
            create_public_ip=create_public_ip,
            data_plane_routing=data_plane_routing,
            default_large_staging_disk_type=default_large_staging_disk_type,
            ebs_encryption_key_arn=ebs_encryption_key_arn,
            internet_protocol=internet_protocol,
            replication_server_instance_type=replication_server_instance_type,
            tags=tags,
            use_dedicated_replication_server=use_dedicated_replication_server,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForReplicationConfigurationTemplate")
    @builtins.classmethod
    def arn_for_replication_configuration_template(
        cls,
        resource: "_aws_drs_f93ad3cc.IReplicationConfigurationTemplateRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7962cd9d83d4e09ecf8a8e4bdea7359c8fdb40cc5225560a24180e3c3a1ad240)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForReplicationConfigurationTemplate", [resource]))

    @jsii.member(jsii_name="isCfnReplicationConfigurationTemplate")
    @builtins.classmethod
    def is_cfn_replication_configuration_template(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnReplicationConfigurationTemplate.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__550608fa3a3172089660f8457ed957fb440e34017cc36c53b4fd38fd5019380e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnReplicationConfigurationTemplate", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e7b24b2d010b2e7c4c00290c943f21a3eab4c125598996852e698194206b8a56)
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
            type_hints = cached_type_hints(_typecheckingstub__bb9ff3bc395de4ee2fbb52325e2238b684b37079f8eaab284b46c53f5b5df535)
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
        '''The Replication Configuration Template ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrReplicationConfigurationTemplateId")
    def attr_replication_configuration_template_id(self) -> builtins.str:
        '''The Replication Configuration Template ID.

        :cloudformationAttribute: ReplicationConfigurationTemplateID
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReplicationConfigurationTemplateId"))

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
    @jsii.member(jsii_name="replicationConfigurationTemplateRef")
    def replication_configuration_template_ref(
        self,
    ) -> "_aws_drs_f93ad3cc.ReplicationConfigurationTemplateReference":
        '''A reference to a ReplicationConfigurationTemplate resource.'''
        return typing.cast("_aws_drs_f93ad3cc.ReplicationConfigurationTemplateReference", jsii.get(self, "replicationConfigurationTemplateRef"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthThrottling")
    def bandwidth_throttling(self) -> jsii.Number:
        '''Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.'''
        return typing.cast(jsii.Number, jsii.get(self, "bandwidthThrottling"))

    @bandwidth_throttling.setter
    def bandwidth_throttling(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b2771b131538f8a0ebe915008c564d771e79ae3ccd1742ba753c2cbcfde97d3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bandwidthThrottling", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ebsEncryption")
    def ebs_encryption(self) -> builtins.str:
        '''The type of EBS encryption to be used during replication.'''
        return typing.cast(builtins.str, jsii.get(self, "ebsEncryption"))

    @ebs_encryption.setter
    def ebs_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a487b6ac7a6f86dfe81bfb188c8d9762af9d3352fa0428f1471b674abad276ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsEncryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pitPolicy")
    def pit_policy(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnReplicationConfigurationTemplate.PITPolicyRuleProperty"]]]:
        '''The Point in time (PIT) policy to manage snapshots taken during replication.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnReplicationConfigurationTemplate.PITPolicyRuleProperty"]]], jsii.get(self, "pitPolicy"))

    @pit_policy.setter
    def pit_policy(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnReplicationConfigurationTemplate.PITPolicyRuleProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fabe91d26be85e13652662acbb7fc44840088d2d9158d40712b711d7152142ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pitPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="replicationServersSecurityGroupsIDs")
    def replication_servers_security_groups_i_ds(self) -> typing.List[builtins.str]:
        '''The security group IDs that will be used by the replication server.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "replicationServersSecurityGroupsIDs"))

    @replication_servers_security_groups_i_ds.setter
    def replication_servers_security_groups_i_ds(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9be02c26637915104575b421959818e025112c195ff95e936b527a431d0e24c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationServersSecurityGroupsIDs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="stagingAreaSubnetId")
    def staging_area_subnet_id(self) -> builtins.str:
        '''The subnet to be used by the replication staging area.'''
        return typing.cast(builtins.str, jsii.get(self, "stagingAreaSubnetId"))

    @staging_area_subnet_id.setter
    def staging_area_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b0d2b6e81ffa85b31118810136e164f6d27e59b097fe95823dae0e0ca82b6d6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stagingAreaSubnetId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="stagingAreaTags")
    def staging_area_tags(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]:
        '''A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "stagingAreaTags"))

    @staging_area_tags.setter
    def staging_area_tags(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c85c233ee9fff3c9ecfcc6b7bd132ea02df3dcd7b523690f80f0df91bc59379e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stagingAreaTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="associateDefaultSecurityGroup")
    def associate_default_security_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "associateDefaultSecurityGroup"))

    @associate_default_security_group.setter
    def associate_default_security_group(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__de3d79ab7f3a6cde64547779dce9dbf13629e59c804725fba0cae3cb825a2362)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateDefaultSecurityGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="autoReplicateNewDisks")
    def auto_replicate_new_disks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether to allow the AWS replication agent to automatically replicate newly added disks.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "autoReplicateNewDisks"))

    @auto_replicate_new_disks.setter
    def auto_replicate_new_disks(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f54ecc218724e74c47ba388d0a2d78eacbb824a0c12d6c1aaf7eccf5de2ddbed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoReplicateNewDisks", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createPublicIp")
    def create_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether to create a Public IP for the Recovery Instance by default.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "createPublicIp"))

    @create_public_ip.setter
    def create_public_ip(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7d9b197519f754ed4649c8bb1029320b9e413fb33f26492341f5177f530693d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createPublicIp", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dataPlaneRouting")
    def data_plane_routing(self) -> typing.Optional[builtins.str]:
        '''The data plane routing mechanism that will be used for replication.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataPlaneRouting"))

    @data_plane_routing.setter
    def data_plane_routing(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e5e59213126ee2fbb44a702cf3dde0ed194bd589d9d519dbc623a9b3edafd89c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataPlaneRouting", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultLargeStagingDiskType")
    def default_large_staging_disk_type(self) -> typing.Optional[builtins.str]:
        '''The Staging Disk EBS volume type to be used during replication.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultLargeStagingDiskType"))

    @default_large_staging_disk_type.setter
    def default_large_staging_disk_type(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c60044ae2c2d990e651a341a660141eb36e227e5041cf75a6da9a228dc76e387)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLargeStagingDiskType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ebsEncryptionKeyArn")
    def ebs_encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the EBS encryption key to be used during replication.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ebsEncryptionKeyArn"))

    @ebs_encryption_key_arn.setter
    def ebs_encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__af024ca969e6e44efe7512dcc31d8ef8d657450205e6aeebf8ccaf0943ac6bc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsEncryptionKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internetProtocol")
    def internet_protocol(self) -> typing.Optional[builtins.str]:
        '''Which version of the Internet Protocol to use for replication of data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "internetProtocol"))

    @internet_protocol.setter
    def internet_protocol(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__25adbd9e8c8d0c865067a8a2665940ce412795b7960cccb6c9712eadf65053c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internetProtocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="replicationServerInstanceType")
    def replication_server_instance_type(self) -> typing.Optional[builtins.str]:
        '''The instance type to be used for the replication server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationServerInstanceType"))

    @replication_server_instance_type.setter
    def replication_server_instance_type(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5ed8d14cf1ff8a058ba157fdeb87f78910115da97723c8d62d57afe2f16b5e1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationServerInstanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A set of tags to be associated with the Replication Configuration Template resource.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__805ad609f1ae54e04a69d0e1e1b3930ada7debab6b96e7e2bb45b88df8fa3b6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="useDedicatedReplicationServer")
    def use_dedicated_replication_server(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether to use a dedicated Replication Server in the replication staging area.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "useDedicatedReplicationServer"))

    @use_dedicated_replication_server.setter
    def use_dedicated_replication_server(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fb775493208d51b336e1856d64842adc56e93ecc82df0d0e5fcae4d2ed2c5b0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useDedicatedReplicationServer", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_drs.CfnReplicationConfigurationTemplate.PITPolicyRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval": "interval",
            "retention_duration": "retentionDuration",
            "units": "units",
            "enabled": "enabled",
            "rule_id": "ruleId",
        },
    )
    class PITPolicyRuleProperty:
        def __init__(
            self,
            *,
            interval: jsii.Number,
            retention_duration: jsii.Number,
            units: builtins.str,
            enabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            rule_id: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param interval: How often, in the chosen units, a snapshot should be taken.
            :param retention_duration: The duration to retain a snapshot for, in the chosen units.
            :param units: The units used to measure the interval and retentionDuration.
            :param enabled: Whether this rule is enabled or not.
            :param rule_id: The ID of the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-drs-replicationconfigurationtemplate-pitpolicyrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_drs as drs
                
                p_it_policy_rule_property = drs.CfnReplicationConfigurationTemplate.PITPolicyRuleProperty(
                    interval=123,
                    retention_duration=123,
                    units="units",
                
                    # the properties below are optional
                    enabled=False,
                    rule_id=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e6a85a1a88e6d9ac089d2f77eb4004b81cfc83f4cbd867234ce7708b0fa59d38)
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument retention_duration", value=retention_duration, expected_type=type_hints["retention_duration"])
                check_type(argname="argument units", value=units, expected_type=type_hints["units"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interval": interval,
                "retention_duration": retention_duration,
                "units": units,
            }
            if enabled is not None:
                self._values["enabled"] = enabled
            if rule_id is not None:
                self._values["rule_id"] = rule_id

        @builtins.property
        def interval(self) -> jsii.Number:
            '''How often, in the chosen units, a snapshot should be taken.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-drs-replicationconfigurationtemplate-pitpolicyrule.html#cfn-drs-replicationconfigurationtemplate-pitpolicyrule-interval
            '''
            result = self._values.get("interval")
            assert result is not None, "Required property 'interval' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def retention_duration(self) -> jsii.Number:
            '''The duration to retain a snapshot for, in the chosen units.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-drs-replicationconfigurationtemplate-pitpolicyrule.html#cfn-drs-replicationconfigurationtemplate-pitpolicyrule-retentionduration
            '''
            result = self._values.get("retention_duration")
            assert result is not None, "Required property 'retention_duration' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def units(self) -> builtins.str:
            '''The units used to measure the interval and retentionDuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-drs-replicationconfigurationtemplate-pitpolicyrule.html#cfn-drs-replicationconfigurationtemplate-pitpolicyrule-units
            '''
            result = self._values.get("units")
            assert result is not None, "Required property 'units' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether this rule is enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-drs-replicationconfigurationtemplate-pitpolicyrule.html#cfn-drs-replicationconfigurationtemplate-pitpolicyrule-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def rule_id(self) -> typing.Optional[jsii.Number]:
            '''The ID of the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-drs-replicationconfigurationtemplate-pitpolicyrule.html#cfn-drs-replicationconfigurationtemplate-pitpolicyrule-ruleid
            '''
            result = self._values.get("rule_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PITPolicyRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_drs.CfnReplicationConfigurationTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "bandwidth_throttling": "bandwidthThrottling",
        "ebs_encryption": "ebsEncryption",
        "pit_policy": "pitPolicy",
        "replication_servers_security_groups_i_ds": "replicationServersSecurityGroupsIDs",
        "staging_area_subnet_id": "stagingAreaSubnetId",
        "staging_area_tags": "stagingAreaTags",
        "associate_default_security_group": "associateDefaultSecurityGroup",
        "auto_replicate_new_disks": "autoReplicateNewDisks",
        "create_public_ip": "createPublicIp",
        "data_plane_routing": "dataPlaneRouting",
        "default_large_staging_disk_type": "defaultLargeStagingDiskType",
        "ebs_encryption_key_arn": "ebsEncryptionKeyArn",
        "internet_protocol": "internetProtocol",
        "replication_server_instance_type": "replicationServerInstanceType",
        "tags": "tags",
        "use_dedicated_replication_server": "useDedicatedReplicationServer",
    },
)
class CfnReplicationConfigurationTemplateProps:
    def __init__(
        self,
        *,
        bandwidth_throttling: jsii.Number,
        ebs_encryption: builtins.str,
        pit_policy: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnReplicationConfigurationTemplate.PITPolicyRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        replication_servers_security_groups_i_ds: typing.Sequence[builtins.str],
        staging_area_subnet_id: builtins.str,
        staging_area_tags: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]],
        associate_default_security_group: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        auto_replicate_new_disks: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        create_public_ip: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        data_plane_routing: typing.Optional[builtins.str] = None,
        default_large_staging_disk_type: typing.Optional[builtins.str] = None,
        ebs_encryption_key_arn: typing.Optional[builtins.str] = None,
        internet_protocol: typing.Optional[builtins.str] = None,
        replication_server_instance_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        use_dedicated_replication_server: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationConfigurationTemplate``.

        :param bandwidth_throttling: Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.
        :param ebs_encryption: The type of EBS encryption to be used during replication.
        :param pit_policy: The Point in time (PIT) policy to manage snapshots taken during replication.
        :param replication_servers_security_groups_i_ds: The security group IDs that will be used by the replication server.
        :param staging_area_subnet_id: The subnet to be used by the replication staging area.
        :param staging_area_tags: A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.
        :param associate_default_security_group: Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.
        :param auto_replicate_new_disks: Whether to allow the AWS replication agent to automatically replicate newly added disks.
        :param create_public_ip: Whether to create a Public IP for the Recovery Instance by default.
        :param data_plane_routing: The data plane routing mechanism that will be used for replication.
        :param default_large_staging_disk_type: The Staging Disk EBS volume type to be used during replication.
        :param ebs_encryption_key_arn: The ARN of the EBS encryption key to be used during replication.
        :param internet_protocol: Which version of the Internet Protocol to use for replication of data.
        :param replication_server_instance_type: The instance type to be used for the replication server.
        :param tags: A set of tags to be associated with the Replication Configuration Template resource.
        :param use_dedicated_replication_server: Whether to use a dedicated Replication Server in the replication staging area.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_drs as drs
            
            cfn_replication_configuration_template_props = drs.CfnReplicationConfigurationTemplateProps(
                bandwidth_throttling=123,
                ebs_encryption="ebsEncryption",
                pit_policy=[drs.CfnReplicationConfigurationTemplate.PITPolicyRuleProperty(
                    interval=123,
                    retention_duration=123,
                    units="units",
            
                    # the properties below are optional
                    enabled=False,
                    rule_id=123
                )],
                replication_servers_security_groups_i_ds=["replicationServersSecurityGroupsIDs"],
                staging_area_subnet_id="stagingAreaSubnetId",
                staging_area_tags={
                    "staging_area_tags_key": "stagingAreaTags"
                },
            
                # the properties below are optional
                associate_default_security_group=False,
                auto_replicate_new_disks=False,
                create_public_ip=False,
                data_plane_routing="dataPlaneRouting",
                default_large_staging_disk_type="defaultLargeStagingDiskType",
                ebs_encryption_key_arn="ebsEncryptionKeyArn",
                internet_protocol="internetProtocol",
                replication_server_instance_type="replicationServerInstanceType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                use_dedicated_replication_server=False
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__19672dd8995cea3ad6193da6f5d08724ecb4624987058d9989d62ee598bec899)
            check_type(argname="argument bandwidth_throttling", value=bandwidth_throttling, expected_type=type_hints["bandwidth_throttling"])
            check_type(argname="argument ebs_encryption", value=ebs_encryption, expected_type=type_hints["ebs_encryption"])
            check_type(argname="argument pit_policy", value=pit_policy, expected_type=type_hints["pit_policy"])
            check_type(argname="argument replication_servers_security_groups_i_ds", value=replication_servers_security_groups_i_ds, expected_type=type_hints["replication_servers_security_groups_i_ds"])
            check_type(argname="argument staging_area_subnet_id", value=staging_area_subnet_id, expected_type=type_hints["staging_area_subnet_id"])
            check_type(argname="argument staging_area_tags", value=staging_area_tags, expected_type=type_hints["staging_area_tags"])
            check_type(argname="argument associate_default_security_group", value=associate_default_security_group, expected_type=type_hints["associate_default_security_group"])
            check_type(argname="argument auto_replicate_new_disks", value=auto_replicate_new_disks, expected_type=type_hints["auto_replicate_new_disks"])
            check_type(argname="argument create_public_ip", value=create_public_ip, expected_type=type_hints["create_public_ip"])
            check_type(argname="argument data_plane_routing", value=data_plane_routing, expected_type=type_hints["data_plane_routing"])
            check_type(argname="argument default_large_staging_disk_type", value=default_large_staging_disk_type, expected_type=type_hints["default_large_staging_disk_type"])
            check_type(argname="argument ebs_encryption_key_arn", value=ebs_encryption_key_arn, expected_type=type_hints["ebs_encryption_key_arn"])
            check_type(argname="argument internet_protocol", value=internet_protocol, expected_type=type_hints["internet_protocol"])
            check_type(argname="argument replication_server_instance_type", value=replication_server_instance_type, expected_type=type_hints["replication_server_instance_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument use_dedicated_replication_server", value=use_dedicated_replication_server, expected_type=type_hints["use_dedicated_replication_server"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bandwidth_throttling": bandwidth_throttling,
            "ebs_encryption": ebs_encryption,
            "pit_policy": pit_policy,
            "replication_servers_security_groups_i_ds": replication_servers_security_groups_i_ds,
            "staging_area_subnet_id": staging_area_subnet_id,
            "staging_area_tags": staging_area_tags,
        }
        if associate_default_security_group is not None:
            self._values["associate_default_security_group"] = associate_default_security_group
        if auto_replicate_new_disks is not None:
            self._values["auto_replicate_new_disks"] = auto_replicate_new_disks
        if create_public_ip is not None:
            self._values["create_public_ip"] = create_public_ip
        if data_plane_routing is not None:
            self._values["data_plane_routing"] = data_plane_routing
        if default_large_staging_disk_type is not None:
            self._values["default_large_staging_disk_type"] = default_large_staging_disk_type
        if ebs_encryption_key_arn is not None:
            self._values["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if internet_protocol is not None:
            self._values["internet_protocol"] = internet_protocol
        if replication_server_instance_type is not None:
            self._values["replication_server_instance_type"] = replication_server_instance_type
        if tags is not None:
            self._values["tags"] = tags
        if use_dedicated_replication_server is not None:
            self._values["use_dedicated_replication_server"] = use_dedicated_replication_server

    @builtins.property
    def bandwidth_throttling(self) -> jsii.Number:
        '''Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-bandwidththrottling
        '''
        result = self._values.get("bandwidth_throttling")
        assert result is not None, "Required property 'bandwidth_throttling' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def ebs_encryption(self) -> builtins.str:
        '''The type of EBS encryption to be used during replication.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-ebsencryption
        '''
        result = self._values.get("ebs_encryption")
        assert result is not None, "Required property 'ebs_encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pit_policy(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnReplicationConfigurationTemplate.PITPolicyRuleProperty"]]]:
        '''The Point in time (PIT) policy to manage snapshots taken during replication.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-pitpolicy
        '''
        result = self._values.get("pit_policy")
        assert result is not None, "Required property 'pit_policy' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnReplicationConfigurationTemplate.PITPolicyRuleProperty"]]], result)

    @builtins.property
    def replication_servers_security_groups_i_ds(self) -> typing.List[builtins.str]:
        '''The security group IDs that will be used by the replication server.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-replicationserverssecuritygroupsids
        '''
        result = self._values.get("replication_servers_security_groups_i_ds")
        assert result is not None, "Required property 'replication_servers_security_groups_i_ds' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def staging_area_subnet_id(self) -> builtins.str:
        '''The subnet to be used by the replication staging area.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-stagingareasubnetid
        '''
        result = self._values.get("staging_area_subnet_id")
        assert result is not None, "Required property 'staging_area_subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def staging_area_tags(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]:
        '''A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-stagingareatags
        '''
        result = self._values.get("staging_area_tags")
        assert result is not None, "Required property 'staging_area_tags' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def associate_default_security_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-associatedefaultsecuritygroup
        '''
        result = self._values.get("associate_default_security_group")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def auto_replicate_new_disks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether to allow the AWS replication agent to automatically replicate newly added disks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-autoreplicatenewdisks
        '''
        result = self._values.get("auto_replicate_new_disks")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def create_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether to create a Public IP for the Recovery Instance by default.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-createpublicip
        '''
        result = self._values.get("create_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def data_plane_routing(self) -> typing.Optional[builtins.str]:
        '''The data plane routing mechanism that will be used for replication.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-dataplanerouting
        '''
        result = self._values.get("data_plane_routing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_large_staging_disk_type(self) -> typing.Optional[builtins.str]:
        '''The Staging Disk EBS volume type to be used during replication.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-defaultlargestagingdisktype
        '''
        result = self._values.get("default_large_staging_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the EBS encryption key to be used during replication.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-ebsencryptionkeyarn
        '''
        result = self._values.get("ebs_encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internet_protocol(self) -> typing.Optional[builtins.str]:
        '''Which version of the Internet Protocol to use for replication of data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-internetprotocol
        '''
        result = self._values.get("internet_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_server_instance_type(self) -> typing.Optional[builtins.str]:
        '''The instance type to be used for the replication server.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-replicationserverinstancetype
        '''
        result = self._values.get("replication_server_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A set of tags to be associated with the Replication Configuration Template resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def use_dedicated_replication_server(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether to use a dedicated Replication Server in the replication staging area.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-replicationconfigurationtemplate.html#cfn-drs-replicationconfigurationtemplate-usededicatedreplicationserver
        '''
        result = self._values.get("use_dedicated_replication_server")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationConfigurationTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_drs_f93ad3cc.ISourceNetworkRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnSourceNetwork(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_drs.CfnSourceNetwork",
):
    '''A Source Network resource represents a VPC that is protected by AWS Elastic Disaster Recovery.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-sourcenetwork.html
    :cloudformationResource: AWS::DRS::SourceNetwork
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_drs as drs
        
        cfn_source_network = drs.CfnSourceNetwork(self, "MyCfnSourceNetwork",
            origin_account_id="originAccountId",
            origin_region="originRegion",
            vpc_id="vpcId",
        
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
        origin_account_id: builtins.str,
        origin_region: builtins.str,
        vpc_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DRS::SourceNetwork``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param origin_account_id: The account ID containing the VPC to protect.
        :param origin_region: The region containing the VPC to protect.
        :param vpc_id: The VPC ID to protect.
        :param tags: A set of tags associated with the Source Network.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d97ad57f2522dd0411c6b55ae55d73d746b282dc5d1e831e927a90539c24fd9a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSourceNetworkProps(
            origin_account_id=origin_account_id,
            origin_region=origin_region,
            vpc_id=vpc_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSourceNetwork")
    @builtins.classmethod
    def arn_for_source_network(
        cls,
        resource: "_aws_drs_f93ad3cc.ISourceNetworkRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c05fc634112ac58c78160fc830d41e79942f87c8e226f9bca445eea84d55aec3)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSourceNetwork", [resource]))

    @jsii.member(jsii_name="isCfnSourceNetwork")
    @builtins.classmethod
    def is_cfn_source_network(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSourceNetwork.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__617565c2120521824646c6e53646bdc8869c274398d52eef3fe38c5d33c46c15)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSourceNetwork", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6f77637dd897a244a753e0003c12a01dde9b56b7d772f5cd19fae616409a67b6)
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
            type_hints = cached_type_hints(_typecheckingstub__c7c6ec2fe694506d506546a55e76ad6c986ed9d2bbb34f7cb114c4cbec12022d)
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
        '''The ARN of the Source Network.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceNetworkId")
    def attr_source_network_id(self) -> builtins.str:
        '''The ID of the Source Network.

        :cloudformationAttribute: SourceNetworkID
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceNetworkId"))

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
    @jsii.member(jsii_name="sourceNetworkRef")
    def source_network_ref(self) -> "_aws_drs_f93ad3cc.SourceNetworkReference":
        '''A reference to a SourceNetwork resource.'''
        return typing.cast("_aws_drs_f93ad3cc.SourceNetworkReference", jsii.get(self, "sourceNetworkRef"))

    @builtins.property
    @jsii.member(jsii_name="originAccountId")
    def origin_account_id(self) -> builtins.str:
        '''The account ID containing the VPC to protect.'''
        return typing.cast(builtins.str, jsii.get(self, "originAccountId"))

    @origin_account_id.setter
    def origin_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c72d6d69d5d8da72514116ae9d75a13c86212f82245dc854ea2f277bb8f94fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originAccountId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="originRegion")
    def origin_region(self) -> builtins.str:
        '''The region containing the VPC to protect.'''
        return typing.cast(builtins.str, jsii.get(self, "originRegion"))

    @origin_region.setter
    def origin_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__68976ddfc0bd35d074c8413345f3cd461035cf818143a1e1e739b68adacfa4fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The VPC ID to protect.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ec5656c25085a2061c8f8578569bf7dab822eb4a6fd4f07d214e1b9cf6b77da5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A set of tags associated with the Source Network.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4f459ea64bac22a86b151bf3be9ffe44eb2341eeec168d352034f5a234ae3f32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_drs.CfnSourceNetworkProps",
    jsii_struct_bases=[],
    name_mapping={
        "origin_account_id": "originAccountId",
        "origin_region": "originRegion",
        "vpc_id": "vpcId",
        "tags": "tags",
    },
)
class CfnSourceNetworkProps:
    def __init__(
        self,
        *,
        origin_account_id: builtins.str,
        origin_region: builtins.str,
        vpc_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSourceNetwork``.

        :param origin_account_id: The account ID containing the VPC to protect.
        :param origin_region: The region containing the VPC to protect.
        :param vpc_id: The VPC ID to protect.
        :param tags: A set of tags associated with the Source Network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-sourcenetwork.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_drs as drs
            
            cfn_source_network_props = drs.CfnSourceNetworkProps(
                origin_account_id="originAccountId",
                origin_region="originRegion",
                vpc_id="vpcId",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f60a1e02b93ca008ca4dd333cf7c4cc38ea03fd8d1bf4b81057a2ce8902533bb)
            check_type(argname="argument origin_account_id", value=origin_account_id, expected_type=type_hints["origin_account_id"])
            check_type(argname="argument origin_region", value=origin_region, expected_type=type_hints["origin_region"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "origin_account_id": origin_account_id,
            "origin_region": origin_region,
            "vpc_id": vpc_id,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def origin_account_id(self) -> builtins.str:
        '''The account ID containing the VPC to protect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-sourcenetwork.html#cfn-drs-sourcenetwork-originaccountid
        '''
        result = self._values.get("origin_account_id")
        assert result is not None, "Required property 'origin_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_region(self) -> builtins.str:
        '''The region containing the VPC to protect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-sourcenetwork.html#cfn-drs-sourcenetwork-originregion
        '''
        result = self._values.get("origin_region")
        assert result is not None, "Required property 'origin_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VPC ID to protect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-sourcenetwork.html#cfn-drs-sourcenetwork-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A set of tags associated with the Source Network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-drs-sourcenetwork.html#cfn-drs-sourcenetwork-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSourceNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLaunchConfigurationTemplate",
    "CfnLaunchConfigurationTemplateProps",
    "CfnReplicationConfigurationTemplate",
    "CfnReplicationConfigurationTemplateProps",
    "CfnSourceNetwork",
    "CfnSourceNetworkProps",
]

publication.publish()

def _typecheckingstub__aa8ff51d4bc35cc1b9c10672fa5e444c0b4ae98dd54bb25556b71f1cc6ed1564(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    copy_private_ip: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    export_bucket_arn: typing.Optional[builtins.str] = None,
    launch_disposition: typing.Optional[builtins.str] = None,
    launch_into_source_instance: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    licensing: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLaunchConfigurationTemplate.LicensingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    post_launch_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_instance_type_right_sizing_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f5796515a0d18c918fd55a0efbe528b59b5708d8a3cba32faac50f9916707e(
    resource: _aws_drs_f93ad3cc.ILaunchConfigurationTemplateRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972657d6c5ffd08d47a8696faf43ebaf768d171eb41531d8a32cc6c3af7d468e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09de5c948b603f3b90cdf308a6a00618bcc3ffab118bf1178b2c4c20ae6e4acf(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb62626008db57a4ef674c9c182d76df959c65c27541cbb7852ed412122c9a6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1aa7f1a07d1a658a87015c8b9a8b3cec51f6757e962ca458d987f235293f9d8(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a6d8c93566902c86d567de0e0d0f62afc517a46150ca55b191d33b14d64d69(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe75f9e3d80ebb7e330714aa7d29d4c99ec0a6255a9b565f8b5bfa234454b55(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed2a8b92ba5fdafb1e79da16817441ccea9813f07696d10f22522258fb268e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7df55d93dd7061ca6e2a1edb4af542742d4fbedb59faab33e05c85efce0f28c5(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb062602853e904726706b0c170040510ca9fd5ccedacf0b49a6e2705d90ff15(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLaunchConfigurationTemplate.LicensingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a52efad8e137262b5c482fe9732b6c7b038112ef59adf75aecc31fc9b91dade6(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec54180f516d9cd81a76b12ec81f4c0234b54023f4ca1bbf2e3354739e569356(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a349c2c41d641939164deb1bccab4953985727bc96b2b6356730f04e4b0de787(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b8314b015d3d894a0a733f1f8ecb51b858a376e41a63929bd4b5fefb1b32f5(
    *,
    os_byol: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6299d4436191a20483f05c03c88fc1c894497d78685edf856ee5c4d0e6a2d7(
    *,
    copy_private_ip: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    export_bucket_arn: typing.Optional[builtins.str] = None,
    launch_disposition: typing.Optional[builtins.str] = None,
    launch_into_source_instance: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    licensing: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLaunchConfigurationTemplate.LicensingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    post_launch_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_instance_type_right_sizing_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473112b770609ad0a9ab2476be9e574caab7570c7e292a51ac8b977aa569dc47(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bandwidth_throttling: jsii.Number,
    ebs_encryption: builtins.str,
    pit_policy: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnReplicationConfigurationTemplate.PITPolicyRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    replication_servers_security_groups_i_ds: typing.Sequence[builtins.str],
    staging_area_subnet_id: builtins.str,
    staging_area_tags: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]],
    associate_default_security_group: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    auto_replicate_new_disks: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    create_public_ip: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    data_plane_routing: typing.Optional[builtins.str] = None,
    default_large_staging_disk_type: typing.Optional[builtins.str] = None,
    ebs_encryption_key_arn: typing.Optional[builtins.str] = None,
    internet_protocol: typing.Optional[builtins.str] = None,
    replication_server_instance_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_dedicated_replication_server: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7962cd9d83d4e09ecf8a8e4bdea7359c8fdb40cc5225560a24180e3c3a1ad240(
    resource: _aws_drs_f93ad3cc.IReplicationConfigurationTemplateRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__550608fa3a3172089660f8457ed957fb440e34017cc36c53b4fd38fd5019380e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b24b2d010b2e7c4c00290c943f21a3eab4c125598996852e698194206b8a56(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb9ff3bc395de4ee2fbb52325e2238b684b37079f8eaab284b46c53f5b5df535(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2771b131538f8a0ebe915008c564d771e79ae3ccd1742ba753c2cbcfde97d3e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a487b6ac7a6f86dfe81bfb188c8d9762af9d3352fa0428f1471b674abad276ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fabe91d26be85e13652662acbb7fc44840088d2d9158d40712b711d7152142ec(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnReplicationConfigurationTemplate.PITPolicyRuleProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be02c26637915104575b421959818e025112c195ff95e936b527a431d0e24c6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d2b6e81ffa85b31118810136e164f6d27e59b097fe95823dae0e0ca82b6d6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c85c233ee9fff3c9ecfcc6b7bd132ea02df3dcd7b523690f80f0df91bc59379e(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de3d79ab7f3a6cde64547779dce9dbf13629e59c804725fba0cae3cb825a2362(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f54ecc218724e74c47ba388d0a2d78eacbb824a0c12d6c1aaf7eccf5de2ddbed(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9b197519f754ed4649c8bb1029320b9e413fb33f26492341f5177f530693d9(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e59213126ee2fbb44a702cf3dde0ed194bd589d9d519dbc623a9b3edafd89c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60044ae2c2d990e651a341a660141eb36e227e5041cf75a6da9a228dc76e387(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af024ca969e6e44efe7512dcc31d8ef8d657450205e6aeebf8ccaf0943ac6bc1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25adbd9e8c8d0c865067a8a2665940ce412795b7960cccb6c9712eadf65053c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed8d14cf1ff8a058ba157fdeb87f78910115da97723c8d62d57afe2f16b5e1c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__805ad609f1ae54e04a69d0e1e1b3930ada7debab6b96e7e2bb45b88df8fa3b6b(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb775493208d51b336e1856d64842adc56e93ecc82df0d0e5fcae4d2ed2c5b0d(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a85a1a88e6d9ac089d2f77eb4004b81cfc83f4cbd867234ce7708b0fa59d38(
    *,
    interval: jsii.Number,
    retention_duration: jsii.Number,
    units: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    rule_id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19672dd8995cea3ad6193da6f5d08724ecb4624987058d9989d62ee598bec899(
    *,
    bandwidth_throttling: jsii.Number,
    ebs_encryption: builtins.str,
    pit_policy: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnReplicationConfigurationTemplate.PITPolicyRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    replication_servers_security_groups_i_ds: typing.Sequence[builtins.str],
    staging_area_subnet_id: builtins.str,
    staging_area_tags: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]],
    associate_default_security_group: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    auto_replicate_new_disks: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    create_public_ip: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    data_plane_routing: typing.Optional[builtins.str] = None,
    default_large_staging_disk_type: typing.Optional[builtins.str] = None,
    ebs_encryption_key_arn: typing.Optional[builtins.str] = None,
    internet_protocol: typing.Optional[builtins.str] = None,
    replication_server_instance_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_dedicated_replication_server: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d97ad57f2522dd0411c6b55ae55d73d746b282dc5d1e831e927a90539c24fd9a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    origin_account_id: builtins.str,
    origin_region: builtins.str,
    vpc_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c05fc634112ac58c78160fc830d41e79942f87c8e226f9bca445eea84d55aec3(
    resource: _aws_drs_f93ad3cc.ISourceNetworkRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__617565c2120521824646c6e53646bdc8869c274398d52eef3fe38c5d33c46c15(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f77637dd897a244a753e0003c12a01dde9b56b7d772f5cd19fae616409a67b6(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c6ec2fe694506d506546a55e76ad6c986ed9d2bbb34f7cb114c4cbec12022d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c72d6d69d5d8da72514116ae9d75a13c86212f82245dc854ea2f277bb8f94fba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68976ddfc0bd35d074c8413345f3cd461035cf818143a1e1e739b68adacfa4fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5656c25085a2061c8f8578569bf7dab822eb4a6fd4f07d214e1b9cf6b77da5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f459ea64bac22a86b151bf3be9ffe44eb2341eeec168d352034f5a234ae3f32(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f60a1e02b93ca008ca4dd333cf7c4cc38ea03fd8d1bf4b81057a2ce8902533bb(
    *,
    origin_account_id: builtins.str,
    origin_region: builtins.str,
    vpc_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
