r'''
# AWS::BcmPricingCalculator Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_bcmpricingcalculator as bcmpricingcalculator
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for BcmPricingCalculator construct libraries](https://constructs.dev/search?q=bcmpricingcalculator)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::BcmPricingCalculator resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BcmPricingCalculator.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::BcmPricingCalculator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BcmPricingCalculator.html).

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
    import aws_cdk.interfaces.aws_bcmpricingcalculator as _aws_bcmpricingcalculator_e6bc1cfa
    import constructs as _constructs_77d1e7e8
else:

    _aws_bcmpricingcalculator_e6bc1cfa = _LazyImport("aws_cdk.interfaces.aws_bcmpricingcalculator")
    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_bcmpricingcalculator_e6bc1cfa.IBillScenarioRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnBillScenario(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bcmpricingcalculator.CfnBillScenario",
):
    '''Resource Type definition for AWS::BcmPricingCalculator::BillScenario.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-billscenario.html
    :cloudformationResource: AWS::BcmPricingCalculator::BillScenario
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bcmpricingcalculator as bcmpricingcalculator
        
        cfn_bill_scenario = bcmpricingcalculator.CfnBillScenario(self, "MyCfnBillScenario",
            cost_category_group_sharing_preference_arn="costCategoryGroupSharingPreferenceArn",
            expires_at="expiresAt",
            group_sharing_preference="groupSharingPreference",
            name="name",
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
        cost_category_group_sharing_preference_arn: typing.Optional[builtins.str] = None,
        expires_at: typing.Optional[builtins.str] = None,
        group_sharing_preference: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::BcmPricingCalculator::BillScenario``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cost_category_group_sharing_preference_arn: The ARN of the cost category group sharing preference.
        :param expires_at: The timestamp when the bill scenario expires.
        :param group_sharing_preference: 
        :param name: The name of the bill scenario.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3a715e57ee3488b858266784f2bf4dd323fc5058e2331b29290293c29b387383)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBillScenarioProps(
            cost_category_group_sharing_preference_arn=cost_category_group_sharing_preference_arn,
            expires_at=expires_at,
            group_sharing_preference=group_sharing_preference,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForBillScenario")
    @builtins.classmethod
    def arn_for_bill_scenario(
        cls,
        resource: "_aws_bcmpricingcalculator_e6bc1cfa.IBillScenarioRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2732129e44a99d55050dfbed34a9f38e1eb4fa9a62b314e2f559a8d67f60095d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForBillScenario", [resource]))

    @jsii.member(jsii_name="isCfnBillScenario")
    @builtins.classmethod
    def is_cfn_bill_scenario(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnBillScenario.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__249f1dae497e55e121a7a7718aaefbbc48b8dd80550ff13614e9411e9b87127b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnBillScenario", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a7e1511f4ce71d044dcc2550cd3c14c42f2a6c0bc058d55f1257d19ae7298f6d)
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
            type_hints = cached_type_hints(_typecheckingstub__96a9d63a44f0c8c0f8dd784809900509009bca4bb49bd1e54160652d0866882d)
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
        '''The Amazon Resource Name (ARN) of the bill scenario.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBillInterval")
    def attr_bill_interval(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''
        :cloudformationAttribute: BillInterval
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrBillInterval"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the bill scenario was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureMessage")
    def attr_failure_message(self) -> builtins.str:
        '''The failure message if the bill scenario failed.

        :cloudformationAttribute: FailureMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the bill scenario.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="billScenarioRef")
    def bill_scenario_ref(
        self,
    ) -> "_aws_bcmpricingcalculator_e6bc1cfa.BillScenarioReference":
        '''A reference to a BillScenario resource.'''
        return typing.cast("_aws_bcmpricingcalculator_e6bc1cfa.BillScenarioReference", jsii.get(self, "billScenarioRef"))

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
    @jsii.member(jsii_name="costCategoryGroupSharingPreferenceArn")
    def cost_category_group_sharing_preference_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The ARN of the cost category group sharing preference.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "costCategoryGroupSharingPreferenceArn"))

    @cost_category_group_sharing_preference_arn.setter
    def cost_category_group_sharing_preference_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7bf3540920aef609fd784758cc78a57071379f8e33487aba585b73f53fd7d325)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "costCategoryGroupSharingPreferenceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expiresAt")
    def expires_at(self) -> typing.Optional[builtins.str]:
        '''The timestamp when the bill scenario expires.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiresAt"))

    @expires_at.setter
    def expires_at(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dff93d6d267606ad02a704874ff370ba50deb5b4ab342cc600e1160dd83420a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiresAt", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="groupSharingPreference")
    def group_sharing_preference(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupSharingPreference"))

    @group_sharing_preference.setter
    def group_sharing_preference(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bc81d5e2e2d17a621eaf96acee8bc5fbd376e291918203d39dcaecb8087bec15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupSharingPreference", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the bill scenario.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e4d2e14c1d683567ef229b10c3a4911341522e85bf7bee462d88696628fcc799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

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
            type_hints = cached_type_hints(_typecheckingstub__de6aaaf59fe930cc42db783bf03cc917082dc87230a98ef306fb78a8d02503d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bcmpricingcalculator.CfnBillScenario.BillIntervalProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class BillIntervalProperty:
        def __init__(
            self,
            *,
            end: typing.Optional[builtins.str] = None,
            start: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param end: 
            :param start: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmpricingcalculator-billscenario-billinterval.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bcmpricingcalculator as bcmpricingcalculator
                
                bill_interval_property = bcmpricingcalculator.CfnBillScenario.BillIntervalProperty(
                    end="end",
                    start="start"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__7e8f9d1edf439beb0c409540f07e32ff1d804605774b081953779fee271dd9cc)
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
                check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if end is not None:
                self._values["end"] = end
            if start is not None:
                self._values["start"] = start

        @builtins.property
        def end(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmpricingcalculator-billscenario-billinterval.html#cfn-bcmpricingcalculator-billscenario-billinterval-end
            '''
            result = self._values.get("end")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmpricingcalculator-billscenario-billinterval.html#cfn-bcmpricingcalculator-billscenario-billinterval-start
            '''
            result = self._values.get("start")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BillIntervalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bcmpricingcalculator.CfnBillScenarioProps",
    jsii_struct_bases=[],
    name_mapping={
        "cost_category_group_sharing_preference_arn": "costCategoryGroupSharingPreferenceArn",
        "expires_at": "expiresAt",
        "group_sharing_preference": "groupSharingPreference",
        "name": "name",
        "tags": "tags",
    },
)
class CfnBillScenarioProps:
    def __init__(
        self,
        *,
        cost_category_group_sharing_preference_arn: typing.Optional[builtins.str] = None,
        expires_at: typing.Optional[builtins.str] = None,
        group_sharing_preference: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBillScenario``.

        :param cost_category_group_sharing_preference_arn: The ARN of the cost category group sharing preference.
        :param expires_at: The timestamp when the bill scenario expires.
        :param group_sharing_preference: 
        :param name: The name of the bill scenario.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-billscenario.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bcmpricingcalculator as bcmpricingcalculator
            
            cfn_bill_scenario_props = bcmpricingcalculator.CfnBillScenarioProps(
                cost_category_group_sharing_preference_arn="costCategoryGroupSharingPreferenceArn",
                expires_at="expiresAt",
                group_sharing_preference="groupSharingPreference",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b426afea34841e5ec59e769c91a06d18ba9dfe38ebfb6971ce30a57c28977756)
            check_type(argname="argument cost_category_group_sharing_preference_arn", value=cost_category_group_sharing_preference_arn, expected_type=type_hints["cost_category_group_sharing_preference_arn"])
            check_type(argname="argument expires_at", value=expires_at, expected_type=type_hints["expires_at"])
            check_type(argname="argument group_sharing_preference", value=group_sharing_preference, expected_type=type_hints["group_sharing_preference"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cost_category_group_sharing_preference_arn is not None:
            self._values["cost_category_group_sharing_preference_arn"] = cost_category_group_sharing_preference_arn
        if expires_at is not None:
            self._values["expires_at"] = expires_at
        if group_sharing_preference is not None:
            self._values["group_sharing_preference"] = group_sharing_preference
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cost_category_group_sharing_preference_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The ARN of the cost category group sharing preference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-billscenario.html#cfn-bcmpricingcalculator-billscenario-costcategorygroupsharingpreferencearn
        '''
        result = self._values.get("cost_category_group_sharing_preference_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires_at(self) -> typing.Optional[builtins.str]:
        '''The timestamp when the bill scenario expires.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-billscenario.html#cfn-bcmpricingcalculator-billscenario-expiresat
        '''
        result = self._values.get("expires_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_sharing_preference(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-billscenario.html#cfn-bcmpricingcalculator-billscenario-groupsharingpreference
        '''
        result = self._values.get("group_sharing_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the bill scenario.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-billscenario.html#cfn-bcmpricingcalculator-billscenario-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-billscenario.html#cfn-bcmpricingcalculator-billscenario-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBillScenarioProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_bcmpricingcalculator_e6bc1cfa.IWorkloadEstimateRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnWorkloadEstimate(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bcmpricingcalculator.CfnWorkloadEstimate",
):
    '''Resource Type definition for AWS::BcmPricingCalculator::WorkloadEstimate.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-workloadestimate.html
    :cloudformationResource: AWS::BcmPricingCalculator::WorkloadEstimate
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bcmpricingcalculator as bcmpricingcalculator
        
        cfn_workload_estimate = bcmpricingcalculator.CfnWorkloadEstimate(self, "MyCfnWorkloadEstimate",
            name="name",
        
            # the properties below are optional
            expires_at="expiresAt",
            rate_type="rateType",
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
        expires_at: typing.Optional[builtins.str] = None,
        rate_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::BcmPricingCalculator::WorkloadEstimate``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the workload estimate.
        :param expires_at: The timestamp when the workload estimate will expire.
        :param rate_type: 
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__92036423d3ec5b4529f9b808e3a4a7816df37c45a7e1d98dfa6c3c4abcfb8ebd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkloadEstimateProps(
            name=name, expires_at=expires_at, rate_type=rate_type, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForWorkloadEstimate")
    @builtins.classmethod
    def arn_for_workload_estimate(
        cls,
        resource: "_aws_bcmpricingcalculator_e6bc1cfa.IWorkloadEstimateRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__30cfab48400c1dcb57984dc13b21524918f48f04ae124b378d3ff93518a1585c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForWorkloadEstimate", [resource]))

    @jsii.member(jsii_name="isCfnWorkloadEstimate")
    @builtins.classmethod
    def is_cfn_workload_estimate(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnWorkloadEstimate.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e3976a72cd722dbd991d75ecdaf85c845b098ff82ee2b85bcbdda1a9264de5f1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnWorkloadEstimate", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f000a317c47f380c2de3e718e3021794b66ddf88e6f4c3d8421f31a3007d1fe7)
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
            type_hints = cached_type_hints(_typecheckingstub__ba41e9b41ce51ff376a003fc7ff1a4dafc86d78126ba5c193f066e389fb225e5)
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
        '''The Amazon Resource Name (ARN) of the workload estimate.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCostCurrency")
    def attr_cost_currency(self) -> builtins.str:
        '''
        :cloudformationAttribute: CostCurrency
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCostCurrency"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the workload estimate was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureMessage")
    def attr_failure_message(self) -> builtins.str:
        '''An error message if the workload estimate failed.

        :cloudformationAttribute: FailureMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the workload estimate.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRateTimestamp")
    def attr_rate_timestamp(self) -> builtins.str:
        '''The timestamp of the pricing rates used for the estimate.

        :cloudformationAttribute: RateTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRateTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTotalCost")
    def attr_total_cost(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''The total estimated cost for the workload.

        :cloudformationAttribute: TotalCost
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrTotalCost"))

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
    @jsii.member(jsii_name="workloadEstimateRef")
    def workload_estimate_ref(
        self,
    ) -> "_aws_bcmpricingcalculator_e6bc1cfa.WorkloadEstimateReference":
        '''A reference to a WorkloadEstimate resource.'''
        return typing.cast("_aws_bcmpricingcalculator_e6bc1cfa.WorkloadEstimateReference", jsii.get(self, "workloadEstimateRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the workload estimate.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__59f13a6252d58cb6047ed165f6d24bc9cf8521351bde547d37b381c37f308c3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expiresAt")
    def expires_at(self) -> typing.Optional[builtins.str]:
        '''The timestamp when the workload estimate will expire.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiresAt"))

    @expires_at.setter
    def expires_at(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d31d84eac8ea1df7c753c48cd729c0ae972f2accfb4fb8acc5650d2362819f31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiresAt", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rateType")
    def rate_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rateType"))

    @rate_type.setter
    def rate_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__23d3cd9a6c7d022cd679d83390beddfca5b9780b3770a5ca4016753f84278238)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rateType", value) # pyright: ignore[reportArgumentType]

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
            type_hints = cached_type_hints(_typecheckingstub__db03ce5004a515ba66b4544fc29808f1528568433792946038cd614cc34b7dc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bcmpricingcalculator.CfnWorkloadEstimateProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "expires_at": "expiresAt",
        "rate_type": "rateType",
        "tags": "tags",
    },
)
class CfnWorkloadEstimateProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        expires_at: typing.Optional[builtins.str] = None,
        rate_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkloadEstimate``.

        :param name: The name of the workload estimate.
        :param expires_at: The timestamp when the workload estimate will expire.
        :param rate_type: 
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-workloadestimate.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bcmpricingcalculator as bcmpricingcalculator
            
            cfn_workload_estimate_props = bcmpricingcalculator.CfnWorkloadEstimateProps(
                name="name",
            
                # the properties below are optional
                expires_at="expiresAt",
                rate_type="rateType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__695117b87eadc6ed0100075c49d76c6143eaad10b2a8264850bb798dc5c44492)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument expires_at", value=expires_at, expected_type=type_hints["expires_at"])
            check_type(argname="argument rate_type", value=rate_type, expected_type=type_hints["rate_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if expires_at is not None:
            self._values["expires_at"] = expires_at
        if rate_type is not None:
            self._values["rate_type"] = rate_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the workload estimate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-workloadestimate.html#cfn-bcmpricingcalculator-workloadestimate-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expires_at(self) -> typing.Optional[builtins.str]:
        '''The timestamp when the workload estimate will expire.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-workloadestimate.html#cfn-bcmpricingcalculator-workloadestimate-expiresat
        '''
        result = self._values.get("expires_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rate_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-workloadestimate.html#cfn-bcmpricingcalculator-workloadestimate-ratetype
        '''
        result = self._values.get("rate_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmpricingcalculator-workloadestimate.html#cfn-bcmpricingcalculator-workloadestimate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkloadEstimateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBillScenario",
    "CfnBillScenarioProps",
    "CfnWorkloadEstimate",
    "CfnWorkloadEstimateProps",
]

publication.publish()

def _typecheckingstub__3a715e57ee3488b858266784f2bf4dd323fc5058e2331b29290293c29b387383(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cost_category_group_sharing_preference_arn: typing.Optional[builtins.str] = None,
    expires_at: typing.Optional[builtins.str] = None,
    group_sharing_preference: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2732129e44a99d55050dfbed34a9f38e1eb4fa9a62b314e2f559a8d67f60095d(
    resource: _aws_bcmpricingcalculator_e6bc1cfa.IBillScenarioRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__249f1dae497e55e121a7a7718aaefbbc48b8dd80550ff13614e9411e9b87127b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e1511f4ce71d044dcc2550cd3c14c42f2a6c0bc058d55f1257d19ae7298f6d(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96a9d63a44f0c8c0f8dd784809900509009bca4bb49bd1e54160652d0866882d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bf3540920aef609fd784758cc78a57071379f8e33487aba585b73f53fd7d325(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff93d6d267606ad02a704874ff370ba50deb5b4ab342cc600e1160dd83420a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc81d5e2e2d17a621eaf96acee8bc5fbd376e291918203d39dcaecb8087bec15(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4d2e14c1d683567ef229b10c3a4911341522e85bf7bee462d88696628fcc799(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6aaaf59fe930cc42db783bf03cc917082dc87230a98ef306fb78a8d02503d4(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e8f9d1edf439beb0c409540f07e32ff1d804605774b081953779fee271dd9cc(
    *,
    end: typing.Optional[builtins.str] = None,
    start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b426afea34841e5ec59e769c91a06d18ba9dfe38ebfb6971ce30a57c28977756(
    *,
    cost_category_group_sharing_preference_arn: typing.Optional[builtins.str] = None,
    expires_at: typing.Optional[builtins.str] = None,
    group_sharing_preference: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92036423d3ec5b4529f9b808e3a4a7816df37c45a7e1d98dfa6c3c4abcfb8ebd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    expires_at: typing.Optional[builtins.str] = None,
    rate_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30cfab48400c1dcb57984dc13b21524918f48f04ae124b378d3ff93518a1585c(
    resource: _aws_bcmpricingcalculator_e6bc1cfa.IWorkloadEstimateRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3976a72cd722dbd991d75ecdaf85c845b098ff82ee2b85bcbdda1a9264de5f1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f000a317c47f380c2de3e718e3021794b66ddf88e6f4c3d8421f31a3007d1fe7(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba41e9b41ce51ff376a003fc7ff1a4dafc86d78126ba5c193f066e389fb225e5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f13a6252d58cb6047ed165f6d24bc9cf8521351bde547d37b381c37f308c3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31d84eac8ea1df7c753c48cd729c0ae972f2accfb4fb8acc5650d2362819f31(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23d3cd9a6c7d022cd679d83390beddfca5b9780b3770a5ca4016753f84278238(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db03ce5004a515ba66b4544fc29808f1528568433792946038cd614cc34b7dc8(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__695117b87eadc6ed0100075c49d76c6143eaad10b2a8264850bb798dc5c44492(
    *,
    name: builtins.str,
    expires_at: typing.Optional[builtins.str] = None,
    rate_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
