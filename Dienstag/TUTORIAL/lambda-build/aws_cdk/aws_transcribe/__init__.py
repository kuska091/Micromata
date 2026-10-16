r'''
# AWS::Transcribe Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_transcribe as transcribe
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Transcribe construct libraries](https://constructs.dev/search?q=transcribe)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Transcribe resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Transcribe.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Transcribe](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Transcribe.html).

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
    import aws_cdk.interfaces.aws_transcribe as _aws_transcribe_5ed72ef1
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_transcribe_5ed72ef1 = _LazyImport("aws_cdk.interfaces.aws_transcribe")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_transcribe_5ed72ef1.ICallAnalyticsCategoryRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnCallAnalyticsCategory(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategory",
):
    '''Resource type definition for AWS::Transcribe::CallAnalyticsCategory.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-callanalyticscategory.html
    :cloudformationResource: AWS::Transcribe::CallAnalyticsCategory
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transcribe as transcribe
        
        cfn_call_analytics_category = transcribe.CfnCallAnalyticsCategory(self, "MyCfnCallAnalyticsCategory",
            category_name="categoryName",
            rules=[transcribe.CfnCallAnalyticsCategory.RuleProperty(
                interruption_filter=transcribe.CfnCallAnalyticsCategory.InterruptionFilterProperty(
                    absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                        end_time=123,
                        first=123,
                        last=123,
                        start_time=123
                    ),
                    negate=False,
                    participant_role="participantRole",
                    relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                        end_percentage=123,
                        first=123,
                        last=123,
                        start_percentage=123
                    ),
                    threshold=123
                ),
                non_talk_time_filter=transcribe.CfnCallAnalyticsCategory.NonTalkTimeFilterProperty(
                    absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                        end_time=123,
                        first=123,
                        last=123,
                        start_time=123
                    ),
                    negate=False,
                    relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                        end_percentage=123,
                        first=123,
                        last=123,
                        start_percentage=123
                    ),
                    threshold=123
                ),
                sentiment_filter=transcribe.CfnCallAnalyticsCategory.SentimentFilterProperty(
                    sentiments=["sentiments"],
        
                    # the properties below are optional
                    absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                        end_time=123,
                        first=123,
                        last=123,
                        start_time=123
                    ),
                    negate=False,
                    participant_role="participantRole",
                    relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                        end_percentage=123,
                        first=123,
                        last=123,
                        start_percentage=123
                    )
                ),
                transcript_filter=transcribe.CfnCallAnalyticsCategory.TranscriptFilterProperty(
                    targets=["targets"],
                    transcript_filter_type="transcriptFilterType",
        
                    # the properties below are optional
                    absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                        end_time=123,
                        first=123,
                        last=123,
                        start_time=123
                    ),
                    negate=False,
                    participant_role="participantRole",
                    relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                        end_percentage=123,
                        first=123,
                        last=123,
                        start_percentage=123
                    )
                )
            )],
        
            # the properties below are optional
            input_type="inputType",
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
        category_name: builtins.str,
        rules: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        input_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Transcribe::CallAnalyticsCategory``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param category_name: A unique name, chosen by you, for your Call Analytics category.
        :param rules: Rules define a Call Analytics category.
        :param input_type: The input type associated with the specified category.
        :param tags: Tags associated with the Call Analytics category.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c054cf749f051b84a6a814fff3e3c75987682766e5a8ff88bc2cf4dffd41a48a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCallAnalyticsCategoryProps(
            category_name=category_name, rules=rules, input_type=input_type, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForCallAnalyticsCategory")
    @builtins.classmethod
    def arn_for_call_analytics_category(
        cls,
        resource: "_aws_transcribe_5ed72ef1.ICallAnalyticsCategoryRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4d8571a53687a8b6533cb284a2f98ed8feed66ee602c8f7f36ddcb16c9e88ef8)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForCallAnalyticsCategory", [resource]))

    @jsii.member(jsii_name="isCfnCallAnalyticsCategory")
    @builtins.classmethod
    def is_cfn_call_analytics_category(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnCallAnalyticsCategory.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__94b1ac3d028d43d60d3c298fc55864255b44820f4bd60d6937ec5e842b8fc6a9)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnCallAnalyticsCategory", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__632d59371f38094a22db12c913e32ade7052ca38e8bfeb1799c31dff0f69fecf)
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
            type_hints = cached_type_hints(_typecheckingstub__fba6dad15065e4454fe009dd4311676ae9d12d5c1f9a4b13ab55bacf68719cc5)
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
        '''The Amazon Resource Name (ARN) of the Call Analytics category.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateTime")
    def attr_create_time(self) -> builtins.str:
        '''The date and time the Call Analytics category was created.

        :cloudformationAttribute: CreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdateTime")
    def attr_last_update_time(self) -> builtins.str:
        '''The date and time the Call Analytics category was last updated.

        :cloudformationAttribute: LastUpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="callAnalyticsCategoryRef")
    def call_analytics_category_ref(
        self,
    ) -> "_aws_transcribe_5ed72ef1.CallAnalyticsCategoryReference":
        '''A reference to a CallAnalyticsCategory resource.'''
        return typing.cast("_aws_transcribe_5ed72ef1.CallAnalyticsCategoryReference", jsii.get(self, "callAnalyticsCategoryRef"))

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
    @jsii.member(jsii_name="categoryName")
    def category_name(self) -> builtins.str:
        '''A unique name, chosen by you, for your Call Analytics category.'''
        return typing.cast(builtins.str, jsii.get(self, "categoryName"))

    @category_name.setter
    def category_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7a74a59fcc2ea39f9e98156d83686b31507d8a735ff5369691de802f24304af5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RuleProperty"]]]:
        '''Rules define a Call Analytics category.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RuleProperty"]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RuleProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7f6165ae0d3e465b4ad5f4d8fd7a9d9de61baabcdaafe835737fdee1a822ced4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="inputType")
    def input_type(self) -> typing.Optional[builtins.str]:
        '''The input type associated with the specified category.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputType"))

    @input_type.setter
    def input_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__74f5685f60a622014fa6122c6f25ad3a7470136f979faec970d763d99bc2408a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags associated with the Call Analytics category.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a263451f5e03dfbf9d0d8c77fc4bfdadcf134a226b833cb4a830522cc00ee43e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_time": "endTime",
            "first": "first",
            "last": "last",
            "start_time": "startTime",
        },
    )
    class AbsoluteTimeRangeProperty:
        def __init__(
            self,
            *,
            end_time: typing.Optional[jsii.Number] = None,
            first: typing.Optional[jsii.Number] = None,
            last: typing.Optional[jsii.Number] = None,
            start_time: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param end_time: 
            :param first: 
            :param last: 
            :param start_time: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-absolutetimerange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transcribe as transcribe
                
                absolute_time_range_property = transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                    end_time=123,
                    first=123,
                    last=123,
                    start_time=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e7a1199eebacc06a7c7c01b5682035bb1ef19fc0885a4c52790ccb6259d14737)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument first", value=first, expected_type=type_hints["first"])
                check_type(argname="argument last", value=last, expected_type=type_hints["last"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if end_time is not None:
                self._values["end_time"] = end_time
            if first is not None:
                self._values["first"] = first
            if last is not None:
                self._values["last"] = last
            if start_time is not None:
                self._values["start_time"] = start_time

        @builtins.property
        def end_time(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-absolutetimerange.html#cfn-transcribe-callanalyticscategory-absolutetimerange-endtime
            '''
            result = self._values.get("end_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def first(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-absolutetimerange.html#cfn-transcribe-callanalyticscategory-absolutetimerange-first
            '''
            result = self._values.get("first")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def last(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-absolutetimerange.html#cfn-transcribe-callanalyticscategory-absolutetimerange-last
            '''
            result = self._values.get("last")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def start_time(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-absolutetimerange.html#cfn-transcribe-callanalyticscategory-absolutetimerange-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbsoluteTimeRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategory.InterruptionFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "absolute_time_range": "absoluteTimeRange",
            "negate": "negate",
            "participant_role": "participantRole",
            "relative_time_range": "relativeTimeRange",
            "threshold": "threshold",
        },
    )
    class InterruptionFilterProperty:
        def __init__(
            self,
            *,
            absolute_time_range: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            negate: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            participant_role: typing.Optional[builtins.str] = None,
            relative_time_range: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.RelativeTimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param absolute_time_range: 
            :param negate: 
            :param participant_role: 
            :param relative_time_range: 
            :param threshold: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-interruptionfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transcribe as transcribe
                
                interruption_filter_property = transcribe.CfnCallAnalyticsCategory.InterruptionFilterProperty(
                    absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                        end_time=123,
                        first=123,
                        last=123,
                        start_time=123
                    ),
                    negate=False,
                    participant_role="participantRole",
                    relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                        end_percentage=123,
                        first=123,
                        last=123,
                        start_percentage=123
                    ),
                    threshold=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ea488fa9096c7f2e3ef622f1d73b5a173a2194fffa1f5ca0b386163b72d5b04c)
                check_type(argname="argument absolute_time_range", value=absolute_time_range, expected_type=type_hints["absolute_time_range"])
                check_type(argname="argument negate", value=negate, expected_type=type_hints["negate"])
                check_type(argname="argument participant_role", value=participant_role, expected_type=type_hints["participant_role"])
                check_type(argname="argument relative_time_range", value=relative_time_range, expected_type=type_hints["relative_time_range"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if absolute_time_range is not None:
                self._values["absolute_time_range"] = absolute_time_range
            if negate is not None:
                self._values["negate"] = negate
            if participant_role is not None:
                self._values["participant_role"] = participant_role
            if relative_time_range is not None:
                self._values["relative_time_range"] = relative_time_range
            if threshold is not None:
                self._values["threshold"] = threshold

        @builtins.property
        def absolute_time_range(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-interruptionfilter.html#cfn-transcribe-callanalyticscategory-interruptionfilter-absolutetimerange
            '''
            result = self._values.get("absolute_time_range")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty"]], result)

        @builtins.property
        def negate(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-interruptionfilter.html#cfn-transcribe-callanalyticscategory-interruptionfilter-negate
            '''
            result = self._values.get("negate")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def participant_role(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-interruptionfilter.html#cfn-transcribe-callanalyticscategory-interruptionfilter-participantrole
            '''
            result = self._values.get("participant_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def relative_time_range(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RelativeTimeRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-interruptionfilter.html#cfn-transcribe-callanalyticscategory-interruptionfilter-relativetimerange
            '''
            result = self._values.get("relative_time_range")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RelativeTimeRangeProperty"]], result)

        @builtins.property
        def threshold(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-interruptionfilter.html#cfn-transcribe-callanalyticscategory-interruptionfilter-threshold
            '''
            result = self._values.get("threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InterruptionFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategory.NonTalkTimeFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "absolute_time_range": "absoluteTimeRange",
            "negate": "negate",
            "relative_time_range": "relativeTimeRange",
            "threshold": "threshold",
        },
    )
    class NonTalkTimeFilterProperty:
        def __init__(
            self,
            *,
            absolute_time_range: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            negate: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            relative_time_range: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.RelativeTimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param absolute_time_range: 
            :param negate: 
            :param relative_time_range: 
            :param threshold: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-nontalktimefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transcribe as transcribe
                
                non_talk_time_filter_property = transcribe.CfnCallAnalyticsCategory.NonTalkTimeFilterProperty(
                    absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                        end_time=123,
                        first=123,
                        last=123,
                        start_time=123
                    ),
                    negate=False,
                    relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                        end_percentage=123,
                        first=123,
                        last=123,
                        start_percentage=123
                    ),
                    threshold=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__4f379146ac2727dde356ebe55d516a7c00c98768f78def996a2209eadb627524)
                check_type(argname="argument absolute_time_range", value=absolute_time_range, expected_type=type_hints["absolute_time_range"])
                check_type(argname="argument negate", value=negate, expected_type=type_hints["negate"])
                check_type(argname="argument relative_time_range", value=relative_time_range, expected_type=type_hints["relative_time_range"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if absolute_time_range is not None:
                self._values["absolute_time_range"] = absolute_time_range
            if negate is not None:
                self._values["negate"] = negate
            if relative_time_range is not None:
                self._values["relative_time_range"] = relative_time_range
            if threshold is not None:
                self._values["threshold"] = threshold

        @builtins.property
        def absolute_time_range(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-nontalktimefilter.html#cfn-transcribe-callanalyticscategory-nontalktimefilter-absolutetimerange
            '''
            result = self._values.get("absolute_time_range")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty"]], result)

        @builtins.property
        def negate(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-nontalktimefilter.html#cfn-transcribe-callanalyticscategory-nontalktimefilter-negate
            '''
            result = self._values.get("negate")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def relative_time_range(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RelativeTimeRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-nontalktimefilter.html#cfn-transcribe-callanalyticscategory-nontalktimefilter-relativetimerange
            '''
            result = self._values.get("relative_time_range")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RelativeTimeRangeProperty"]], result)

        @builtins.property
        def threshold(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-nontalktimefilter.html#cfn-transcribe-callanalyticscategory-nontalktimefilter-threshold
            '''
            result = self._values.get("threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NonTalkTimeFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_percentage": "endPercentage",
            "first": "first",
            "last": "last",
            "start_percentage": "startPercentage",
        },
    )
    class RelativeTimeRangeProperty:
        def __init__(
            self,
            *,
            end_percentage: typing.Optional[jsii.Number] = None,
            first: typing.Optional[jsii.Number] = None,
            last: typing.Optional[jsii.Number] = None,
            start_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param end_percentage: 
            :param first: 
            :param last: 
            :param start_percentage: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-relativetimerange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transcribe as transcribe
                
                relative_time_range_property = transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                    end_percentage=123,
                    first=123,
                    last=123,
                    start_percentage=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__bef6c2924461044181326d0c2452b7e50f4bdf5ee831c15eefbebfc891c438ca)
                check_type(argname="argument end_percentage", value=end_percentage, expected_type=type_hints["end_percentage"])
                check_type(argname="argument first", value=first, expected_type=type_hints["first"])
                check_type(argname="argument last", value=last, expected_type=type_hints["last"])
                check_type(argname="argument start_percentage", value=start_percentage, expected_type=type_hints["start_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if end_percentage is not None:
                self._values["end_percentage"] = end_percentage
            if first is not None:
                self._values["first"] = first
            if last is not None:
                self._values["last"] = last
            if start_percentage is not None:
                self._values["start_percentage"] = start_percentage

        @builtins.property
        def end_percentage(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-relativetimerange.html#cfn-transcribe-callanalyticscategory-relativetimerange-endpercentage
            '''
            result = self._values.get("end_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def first(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-relativetimerange.html#cfn-transcribe-callanalyticscategory-relativetimerange-first
            '''
            result = self._values.get("first")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def last(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-relativetimerange.html#cfn-transcribe-callanalyticscategory-relativetimerange-last
            '''
            result = self._values.get("last")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def start_percentage(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-relativetimerange.html#cfn-transcribe-callanalyticscategory-relativetimerange-startpercentage
            '''
            result = self._values.get("start_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelativeTimeRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategory.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interruption_filter": "interruptionFilter",
            "non_talk_time_filter": "nonTalkTimeFilter",
            "sentiment_filter": "sentimentFilter",
            "transcript_filter": "transcriptFilter",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            interruption_filter: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.InterruptionFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            non_talk_time_filter: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.NonTalkTimeFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sentiment_filter: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.SentimentFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            transcript_filter: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.TranscriptFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param interruption_filter: 
            :param non_talk_time_filter: 
            :param sentiment_filter: 
            :param transcript_filter: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transcribe as transcribe
                
                rule_property = transcribe.CfnCallAnalyticsCategory.RuleProperty(
                    interruption_filter=transcribe.CfnCallAnalyticsCategory.InterruptionFilterProperty(
                        absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                            end_time=123,
                            first=123,
                            last=123,
                            start_time=123
                        ),
                        negate=False,
                        participant_role="participantRole",
                        relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                            end_percentage=123,
                            first=123,
                            last=123,
                            start_percentage=123
                        ),
                        threshold=123
                    ),
                    non_talk_time_filter=transcribe.CfnCallAnalyticsCategory.NonTalkTimeFilterProperty(
                        absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                            end_time=123,
                            first=123,
                            last=123,
                            start_time=123
                        ),
                        negate=False,
                        relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                            end_percentage=123,
                            first=123,
                            last=123,
                            start_percentage=123
                        ),
                        threshold=123
                    ),
                    sentiment_filter=transcribe.CfnCallAnalyticsCategory.SentimentFilterProperty(
                        sentiments=["sentiments"],
                
                        # the properties below are optional
                        absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                            end_time=123,
                            first=123,
                            last=123,
                            start_time=123
                        ),
                        negate=False,
                        participant_role="participantRole",
                        relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                            end_percentage=123,
                            first=123,
                            last=123,
                            start_percentage=123
                        )
                    ),
                    transcript_filter=transcribe.CfnCallAnalyticsCategory.TranscriptFilterProperty(
                        targets=["targets"],
                        transcript_filter_type="transcriptFilterType",
                
                        # the properties below are optional
                        absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                            end_time=123,
                            first=123,
                            last=123,
                            start_time=123
                        ),
                        negate=False,
                        participant_role="participantRole",
                        relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                            end_percentage=123,
                            first=123,
                            last=123,
                            start_percentage=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0f8d6b50b53d11d790fab9cbc3d94c72ebb820cc2f073c02b770896cc31558b2)
                check_type(argname="argument interruption_filter", value=interruption_filter, expected_type=type_hints["interruption_filter"])
                check_type(argname="argument non_talk_time_filter", value=non_talk_time_filter, expected_type=type_hints["non_talk_time_filter"])
                check_type(argname="argument sentiment_filter", value=sentiment_filter, expected_type=type_hints["sentiment_filter"])
                check_type(argname="argument transcript_filter", value=transcript_filter, expected_type=type_hints["transcript_filter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interruption_filter is not None:
                self._values["interruption_filter"] = interruption_filter
            if non_talk_time_filter is not None:
                self._values["non_talk_time_filter"] = non_talk_time_filter
            if sentiment_filter is not None:
                self._values["sentiment_filter"] = sentiment_filter
            if transcript_filter is not None:
                self._values["transcript_filter"] = transcript_filter

        @builtins.property
        def interruption_filter(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.InterruptionFilterProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-rule.html#cfn-transcribe-callanalyticscategory-rule-interruptionfilter
            '''
            result = self._values.get("interruption_filter")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.InterruptionFilterProperty"]], result)

        @builtins.property
        def non_talk_time_filter(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.NonTalkTimeFilterProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-rule.html#cfn-transcribe-callanalyticscategory-rule-nontalktimefilter
            '''
            result = self._values.get("non_talk_time_filter")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.NonTalkTimeFilterProperty"]], result)

        @builtins.property
        def sentiment_filter(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.SentimentFilterProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-rule.html#cfn-transcribe-callanalyticscategory-rule-sentimentfilter
            '''
            result = self._values.get("sentiment_filter")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.SentimentFilterProperty"]], result)

        @builtins.property
        def transcript_filter(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.TranscriptFilterProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-rule.html#cfn-transcribe-callanalyticscategory-rule-transcriptfilter
            '''
            result = self._values.get("transcript_filter")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.TranscriptFilterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategory.SentimentFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sentiments": "sentiments",
            "absolute_time_range": "absoluteTimeRange",
            "negate": "negate",
            "participant_role": "participantRole",
            "relative_time_range": "relativeTimeRange",
        },
    )
    class SentimentFilterProperty:
        def __init__(
            self,
            *,
            sentiments: typing.Sequence[builtins.str],
            absolute_time_range: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            negate: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            participant_role: typing.Optional[builtins.str] = None,
            relative_time_range: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.RelativeTimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param sentiments: 
            :param absolute_time_range: 
            :param negate: 
            :param participant_role: 
            :param relative_time_range: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-sentimentfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transcribe as transcribe
                
                sentiment_filter_property = transcribe.CfnCallAnalyticsCategory.SentimentFilterProperty(
                    sentiments=["sentiments"],
                
                    # the properties below are optional
                    absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                        end_time=123,
                        first=123,
                        last=123,
                        start_time=123
                    ),
                    negate=False,
                    participant_role="participantRole",
                    relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                        end_percentage=123,
                        first=123,
                        last=123,
                        start_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8de1687e0b020f3e94a81f75165eb33089cabc3f9e1b09518670ff829e9bc775)
                check_type(argname="argument sentiments", value=sentiments, expected_type=type_hints["sentiments"])
                check_type(argname="argument absolute_time_range", value=absolute_time_range, expected_type=type_hints["absolute_time_range"])
                check_type(argname="argument negate", value=negate, expected_type=type_hints["negate"])
                check_type(argname="argument participant_role", value=participant_role, expected_type=type_hints["participant_role"])
                check_type(argname="argument relative_time_range", value=relative_time_range, expected_type=type_hints["relative_time_range"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sentiments": sentiments,
            }
            if absolute_time_range is not None:
                self._values["absolute_time_range"] = absolute_time_range
            if negate is not None:
                self._values["negate"] = negate
            if participant_role is not None:
                self._values["participant_role"] = participant_role
            if relative_time_range is not None:
                self._values["relative_time_range"] = relative_time_range

        @builtins.property
        def sentiments(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-sentimentfilter.html#cfn-transcribe-callanalyticscategory-sentimentfilter-sentiments
            '''
            result = self._values.get("sentiments")
            assert result is not None, "Required property 'sentiments' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def absolute_time_range(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-sentimentfilter.html#cfn-transcribe-callanalyticscategory-sentimentfilter-absolutetimerange
            '''
            result = self._values.get("absolute_time_range")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty"]], result)

        @builtins.property
        def negate(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-sentimentfilter.html#cfn-transcribe-callanalyticscategory-sentimentfilter-negate
            '''
            result = self._values.get("negate")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def participant_role(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-sentimentfilter.html#cfn-transcribe-callanalyticscategory-sentimentfilter-participantrole
            '''
            result = self._values.get("participant_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def relative_time_range(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RelativeTimeRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-sentimentfilter.html#cfn-transcribe-callanalyticscategory-sentimentfilter-relativetimerange
            '''
            result = self._values.get("relative_time_range")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RelativeTimeRangeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SentimentFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategory.TranscriptFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "targets": "targets",
            "transcript_filter_type": "transcriptFilterType",
            "absolute_time_range": "absoluteTimeRange",
            "negate": "negate",
            "participant_role": "participantRole",
            "relative_time_range": "relativeTimeRange",
        },
    )
    class TranscriptFilterProperty:
        def __init__(
            self,
            *,
            targets: typing.Sequence[builtins.str],
            transcript_filter_type: builtins.str,
            absolute_time_range: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            negate: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            participant_role: typing.Optional[builtins.str] = None,
            relative_time_range: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.RelativeTimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param targets: 
            :param transcript_filter_type: 
            :param absolute_time_range: 
            :param negate: 
            :param participant_role: 
            :param relative_time_range: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-transcriptfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transcribe as transcribe
                
                transcript_filter_property = transcribe.CfnCallAnalyticsCategory.TranscriptFilterProperty(
                    targets=["targets"],
                    transcript_filter_type="transcriptFilterType",
                
                    # the properties below are optional
                    absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                        end_time=123,
                        first=123,
                        last=123,
                        start_time=123
                    ),
                    negate=False,
                    participant_role="participantRole",
                    relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                        end_percentage=123,
                        first=123,
                        last=123,
                        start_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__3c158825c38df89d326ed5a53474d62c23127b4738bcfe1886d5f1e57dd00211)
                check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
                check_type(argname="argument transcript_filter_type", value=transcript_filter_type, expected_type=type_hints["transcript_filter_type"])
                check_type(argname="argument absolute_time_range", value=absolute_time_range, expected_type=type_hints["absolute_time_range"])
                check_type(argname="argument negate", value=negate, expected_type=type_hints["negate"])
                check_type(argname="argument participant_role", value=participant_role, expected_type=type_hints["participant_role"])
                check_type(argname="argument relative_time_range", value=relative_time_range, expected_type=type_hints["relative_time_range"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "targets": targets,
                "transcript_filter_type": transcript_filter_type,
            }
            if absolute_time_range is not None:
                self._values["absolute_time_range"] = absolute_time_range
            if negate is not None:
                self._values["negate"] = negate
            if participant_role is not None:
                self._values["participant_role"] = participant_role
            if relative_time_range is not None:
                self._values["relative_time_range"] = relative_time_range

        @builtins.property
        def targets(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-transcriptfilter.html#cfn-transcribe-callanalyticscategory-transcriptfilter-targets
            '''
            result = self._values.get("targets")
            assert result is not None, "Required property 'targets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def transcript_filter_type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-transcriptfilter.html#cfn-transcribe-callanalyticscategory-transcriptfilter-transcriptfiltertype
            '''
            result = self._values.get("transcript_filter_type")
            assert result is not None, "Required property 'transcript_filter_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def absolute_time_range(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-transcriptfilter.html#cfn-transcribe-callanalyticscategory-transcriptfilter-absolutetimerange
            '''
            result = self._values.get("absolute_time_range")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty"]], result)

        @builtins.property
        def negate(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-transcriptfilter.html#cfn-transcribe-callanalyticscategory-transcriptfilter-negate
            '''
            result = self._values.get("negate")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def participant_role(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-transcriptfilter.html#cfn-transcribe-callanalyticscategory-transcriptfilter-participantrole
            '''
            result = self._values.get("participant_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def relative_time_range(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RelativeTimeRangeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transcribe-callanalyticscategory-transcriptfilter.html#cfn-transcribe-callanalyticscategory-transcriptfilter-relativetimerange
            '''
            result = self._values.get("relative_time_range")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RelativeTimeRangeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TranscriptFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transcribe.CfnCallAnalyticsCategoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "category_name": "categoryName",
        "rules": "rules",
        "input_type": "inputType",
        "tags": "tags",
    },
)
class CfnCallAnalyticsCategoryProps:
    def __init__(
        self,
        *,
        category_name: builtins.str,
        rules: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCallAnalyticsCategory.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        input_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCallAnalyticsCategory``.

        :param category_name: A unique name, chosen by you, for your Call Analytics category.
        :param rules: Rules define a Call Analytics category.
        :param input_type: The input type associated with the specified category.
        :param tags: Tags associated with the Call Analytics category.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-callanalyticscategory.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transcribe as transcribe
            
            cfn_call_analytics_category_props = transcribe.CfnCallAnalyticsCategoryProps(
                category_name="categoryName",
                rules=[transcribe.CfnCallAnalyticsCategory.RuleProperty(
                    interruption_filter=transcribe.CfnCallAnalyticsCategory.InterruptionFilterProperty(
                        absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                            end_time=123,
                            first=123,
                            last=123,
                            start_time=123
                        ),
                        negate=False,
                        participant_role="participantRole",
                        relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                            end_percentage=123,
                            first=123,
                            last=123,
                            start_percentage=123
                        ),
                        threshold=123
                    ),
                    non_talk_time_filter=transcribe.CfnCallAnalyticsCategory.NonTalkTimeFilterProperty(
                        absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                            end_time=123,
                            first=123,
                            last=123,
                            start_time=123
                        ),
                        negate=False,
                        relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                            end_percentage=123,
                            first=123,
                            last=123,
                            start_percentage=123
                        ),
                        threshold=123
                    ),
                    sentiment_filter=transcribe.CfnCallAnalyticsCategory.SentimentFilterProperty(
                        sentiments=["sentiments"],
            
                        # the properties below are optional
                        absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                            end_time=123,
                            first=123,
                            last=123,
                            start_time=123
                        ),
                        negate=False,
                        participant_role="participantRole",
                        relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                            end_percentage=123,
                            first=123,
                            last=123,
                            start_percentage=123
                        )
                    ),
                    transcript_filter=transcribe.CfnCallAnalyticsCategory.TranscriptFilterProperty(
                        targets=["targets"],
                        transcript_filter_type="transcriptFilterType",
            
                        # the properties below are optional
                        absolute_time_range=transcribe.CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty(
                            end_time=123,
                            first=123,
                            last=123,
                            start_time=123
                        ),
                        negate=False,
                        participant_role="participantRole",
                        relative_time_range=transcribe.CfnCallAnalyticsCategory.RelativeTimeRangeProperty(
                            end_percentage=123,
                            first=123,
                            last=123,
                            start_percentage=123
                        )
                    )
                )],
            
                # the properties below are optional
                input_type="inputType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e7d119aaa8c30f6f9551e7aa3e3b762678b68daf86bd57643eb1d55ca2177b57)
            check_type(argname="argument category_name", value=category_name, expected_type=type_hints["category_name"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument input_type", value=input_type, expected_type=type_hints["input_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "category_name": category_name,
            "rules": rules,
        }
        if input_type is not None:
            self._values["input_type"] = input_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def category_name(self) -> builtins.str:
        '''A unique name, chosen by you, for your Call Analytics category.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-callanalyticscategory.html#cfn-transcribe-callanalyticscategory-categoryname
        '''
        result = self._values.get("category_name")
        assert result is not None, "Required property 'category_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RuleProperty"]]]:
        '''Rules define a Call Analytics category.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-callanalyticscategory.html#cfn-transcribe-callanalyticscategory-rules
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCallAnalyticsCategory.RuleProperty"]]], result)

    @builtins.property
    def input_type(self) -> typing.Optional[builtins.str]:
        '''The input type associated with the specified category.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-callanalyticscategory.html#cfn-transcribe-callanalyticscategory-inputtype
        '''
        result = self._values.get("input_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags associated with the Call Analytics category.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-callanalyticscategory.html#cfn-transcribe-callanalyticscategory-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCallAnalyticsCategoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_transcribe_5ed72ef1.IMedicalVocabularyRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnMedicalVocabulary(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transcribe.CfnMedicalVocabulary",
):
    '''Resource type definition for AWS::Transcribe::MedicalVocabulary.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-medicalvocabulary.html
    :cloudformationResource: AWS::Transcribe::MedicalVocabulary
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transcribe as transcribe
        
        cfn_medical_vocabulary = transcribe.CfnMedicalVocabulary(self, "MyCfnMedicalVocabulary",
            language_code="languageCode",
            vocabulary_name="vocabularyName",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vocabulary_file_uri="vocabularyFileUri"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        language_code: builtins.str,
        vocabulary_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vocabulary_file_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Transcribe::MedicalVocabulary``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param language_code: The language code of the vocabulary entries.
        :param vocabulary_name: The name of the medical vocabulary.
        :param tags: Tags associated with the medical vocabulary.
        :param vocabulary_file_uri: The Amazon S3 location of the text file that contains the medical vocabulary.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7776e2578a82c3d9c1922b43061249cbf50b611576a5817358b4841492ffbe23)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMedicalVocabularyProps(
            language_code=language_code,
            vocabulary_name=vocabulary_name,
            tags=tags,
            vocabulary_file_uri=vocabulary_file_uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForMedicalVocabulary")
    @builtins.classmethod
    def arn_for_medical_vocabulary(
        cls,
        resource: "_aws_transcribe_5ed72ef1.IMedicalVocabularyRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8e55c18063a6f1adb65c58874168ebf45bf99bb427f3f8f57bb8daf22fa637da)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForMedicalVocabulary", [resource]))

    @jsii.member(jsii_name="isCfnMedicalVocabulary")
    @builtins.classmethod
    def is_cfn_medical_vocabulary(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnMedicalVocabulary.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9d139f162b485c9372d2bc1765c3ab0514142739393b560d7aaafbb791295e54)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnMedicalVocabulary", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__caf5a98bdc672c1897a663c442f057251d33f57b0380f3239e6c9f95f9114df8)
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
            type_hints = cached_type_hints(_typecheckingstub__a4619ae7b917994bfcecb38cd0a10ca5ac2a3a8224a1a6856a88a179e67b7ddd)
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
        '''The Amazon Resource Name (ARN) of the medical vocabulary.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="medicalVocabularyRef")
    def medical_vocabulary_ref(
        self,
    ) -> "_aws_transcribe_5ed72ef1.MedicalVocabularyReference":
        '''A reference to a MedicalVocabulary resource.'''
        return typing.cast("_aws_transcribe_5ed72ef1.MedicalVocabularyReference", jsii.get(self, "medicalVocabularyRef"))

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        '''The language code of the vocabulary entries.'''
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__93d1569c8a62ae9ec7f30675183e5eb1dbdf44d0aa1262cc1a475c9d5e6ebaa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vocabularyName")
    def vocabulary_name(self) -> builtins.str:
        '''The name of the medical vocabulary.'''
        return typing.cast(builtins.str, jsii.get(self, "vocabularyName"))

    @vocabulary_name.setter
    def vocabulary_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__155f9768d7dfdd9e73091b14b64e3dfb9afaf1b5d83051d49cb9fead15fb3988)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vocabularyName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags associated with the medical vocabulary.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__12e3765bf8e096fb326923ede62eae98218db4a245f6b40b6c23137f29a9e9eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vocabularyFileUri")
    def vocabulary_file_uri(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 location of the text file that contains the medical vocabulary.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vocabularyFileUri"))

    @vocabulary_file_uri.setter
    def vocabulary_file_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ffd2b16a7bf8da4f3299e4e2559161526cebd37488425989f26b7bd3b2f86c07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vocabularyFileUri", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transcribe.CfnMedicalVocabularyProps",
    jsii_struct_bases=[],
    name_mapping={
        "language_code": "languageCode",
        "vocabulary_name": "vocabularyName",
        "tags": "tags",
        "vocabulary_file_uri": "vocabularyFileUri",
    },
)
class CfnMedicalVocabularyProps:
    def __init__(
        self,
        *,
        language_code: builtins.str,
        vocabulary_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vocabulary_file_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMedicalVocabulary``.

        :param language_code: The language code of the vocabulary entries.
        :param vocabulary_name: The name of the medical vocabulary.
        :param tags: Tags associated with the medical vocabulary.
        :param vocabulary_file_uri: The Amazon S3 location of the text file that contains the medical vocabulary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-medicalvocabulary.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transcribe as transcribe
            
            cfn_medical_vocabulary_props = transcribe.CfnMedicalVocabularyProps(
                language_code="languageCode",
                vocabulary_name="vocabularyName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vocabulary_file_uri="vocabularyFileUri"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__af80b22fc13d87a9875f4a8dbf0fbd8903e8fa91dcf247d5f2192eab00287ba6)
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument vocabulary_name", value=vocabulary_name, expected_type=type_hints["vocabulary_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vocabulary_file_uri", value=vocabulary_file_uri, expected_type=type_hints["vocabulary_file_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "language_code": language_code,
            "vocabulary_name": vocabulary_name,
        }
        if tags is not None:
            self._values["tags"] = tags
        if vocabulary_file_uri is not None:
            self._values["vocabulary_file_uri"] = vocabulary_file_uri

    @builtins.property
    def language_code(self) -> builtins.str:
        '''The language code of the vocabulary entries.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-medicalvocabulary.html#cfn-transcribe-medicalvocabulary-languagecode
        '''
        result = self._values.get("language_code")
        assert result is not None, "Required property 'language_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vocabulary_name(self) -> builtins.str:
        '''The name of the medical vocabulary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-medicalvocabulary.html#cfn-transcribe-medicalvocabulary-vocabularyname
        '''
        result = self._values.get("vocabulary_name")
        assert result is not None, "Required property 'vocabulary_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags associated with the medical vocabulary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-medicalvocabulary.html#cfn-transcribe-medicalvocabulary-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def vocabulary_file_uri(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 location of the text file that contains the medical vocabulary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-medicalvocabulary.html#cfn-transcribe-medicalvocabulary-vocabularyfileuri
        '''
        result = self._values.get("vocabulary_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMedicalVocabularyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_transcribe_5ed72ef1.IVocabularyRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnVocabulary(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transcribe.CfnVocabulary",
):
    '''Creates a custom vocabulary that you can use to improve the transcription accuracy of domain-specific words and phrases.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabulary.html
    :cloudformationResource: AWS::Transcribe::Vocabulary
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transcribe as transcribe
        
        cfn_vocabulary = transcribe.CfnVocabulary(self, "MyCfnVocabulary",
            language_code="languageCode",
            vocabulary_name="vocabularyName",
        
            # the properties below are optional
            data_access_role_arn="dataAccessRoleArn",
            phrases=["phrases"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vocabulary_file_uri="vocabularyFileUri"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        language_code: builtins.str,
        vocabulary_name: builtins.str,
        data_access_role_arn: typing.Optional[builtins.str] = None,
        phrases: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vocabulary_file_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Transcribe::Vocabulary``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param language_code: The language code that represents the language of the entries in your custom vocabulary. Each custom vocabulary must contain terms in only one language.
        :param vocabulary_name: A unique name, chosen by you, for your custom vocabulary. This name is case sensitive, cannot contain spaces, and must be unique within an AWS account.
        :param data_access_role_arn: The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input file.
        :param phrases: Use this parameter if you want to create your custom vocabulary by including all desired terms, as comma-separated values, within your request. You cannot use this parameter together with VocabularyFileUri.
        :param tags: Adds one or more custom tags, each in the form of a key:value pair, to the custom vocabulary.
        :param vocabulary_file_uri: The Amazon S3 location of the text file that contains your custom vocabulary. You cannot use this parameter together with Phrases.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8cd2b601bd5916e82ff98dc9def499623f8f7fd6873d2e0127676134d4a11d1e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVocabularyProps(
            language_code=language_code,
            vocabulary_name=vocabulary_name,
            data_access_role_arn=data_access_role_arn,
            phrases=phrases,
            tags=tags,
            vocabulary_file_uri=vocabulary_file_uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVocabulary")
    @builtins.classmethod
    def arn_for_vocabulary(
        cls,
        resource: "_aws_transcribe_5ed72ef1.IVocabularyRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__351883d766a65bd807d44824d0ad25d28aba4285361142fd1f43c5ec9074361d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVocabulary", [resource]))

    @jsii.member(jsii_name="isCfnVocabulary")
    @builtins.classmethod
    def is_cfn_vocabulary(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVocabulary.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0f46a514fb1bf01c95de95ef8e6964e66be8ad2523ae7498b91051513c1eaf0a)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVocabulary", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8f0437d44a9571dc47e9623c6679012b4688339532b67abda23a3a7ce0406694)
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
            type_hints = cached_type_hints(_typecheckingstub__19769c9ee59d11ef827f65092d13b64c582ae68b96ba11c84770eb5540404855)
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
        '''The Amazon Resource Name (ARN) of the custom vocabulary.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''The date and time the specified custom vocabulary was last modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrVocabularyState")
    def attr_vocabulary_state(self) -> builtins.str:
        '''The processing state of your custom vocabulary.

        If the state is READY, you can use the custom vocabulary in a StartTranscriptionJob request.

        :cloudformationAttribute: VocabularyState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVocabularyState"))

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
    @jsii.member(jsii_name="vocabularyRef")
    def vocabulary_ref(self) -> "_aws_transcribe_5ed72ef1.VocabularyReference":
        '''A reference to a Vocabulary resource.'''
        return typing.cast("_aws_transcribe_5ed72ef1.VocabularyReference", jsii.get(self, "vocabularyRef"))

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        '''The language code that represents the language of the entries in your custom vocabulary.'''
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b9c241fbb212fca3136cdb41f4c86a36889decb1b9e2d45613bf5f80d97aeb08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vocabularyName")
    def vocabulary_name(self) -> builtins.str:
        '''A unique name, chosen by you, for your custom vocabulary.'''
        return typing.cast(builtins.str, jsii.get(self, "vocabularyName"))

    @vocabulary_name.setter
    def vocabulary_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7ba2c8f4602a07232a809477edc6567e5f286e803383a24dee8b41679c6b9346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vocabularyName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dataAccessRoleArn")
    def data_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input file.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataAccessRoleArn"))

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0364624f1743dcee3e9f2992d4566cc24703ee250bb9ae22ed26f3539a131368)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataAccessRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="phrases")
    def phrases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Use this parameter if you want to create your custom vocabulary by including all desired terms, as comma-separated values, within your request.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "phrases"))

    @phrases.setter
    def phrases(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ea7aa54669942067a3e7cd4b7f12d85f35d6bf6dc08c0874a471cc3103d2ad1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phrases", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Adds one or more custom tags, each in the form of a key:value pair, to the custom vocabulary.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5899b6e320bc8d6d4075f904972e59283de674747dc42da93e78019fc63849aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vocabularyFileUri")
    def vocabulary_file_uri(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 location of the text file that contains your custom vocabulary.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vocabularyFileUri"))

    @vocabulary_file_uri.setter
    def vocabulary_file_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7366039e3e7adc2e526bf6e87f2dd5151c0164d1170323981b75e85f4c6d83d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vocabularyFileUri", value) # pyright: ignore[reportArgumentType]


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_transcribe_5ed72ef1.IVocabularyFilterRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnVocabularyFilter(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transcribe.CfnVocabularyFilter",
):
    '''Creates a custom vocabulary filter that you can use to mask, delete, or flag specific words from your transcript.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabularyfilter.html
    :cloudformationResource: AWS::Transcribe::VocabularyFilter
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transcribe as transcribe
        
        cfn_vocabulary_filter = transcribe.CfnVocabularyFilter(self, "MyCfnVocabularyFilter",
            language_code="languageCode",
            vocabulary_filter_name="vocabularyFilterName",
        
            # the properties below are optional
            data_access_role_arn="dataAccessRoleArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vocabulary_filter_file_uri="vocabularyFilterFileUri",
            words=["words"]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        language_code: builtins.str,
        vocabulary_filter_name: builtins.str,
        data_access_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vocabulary_filter_file_uri: typing.Optional[builtins.str] = None,
        words: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Transcribe::VocabularyFilter``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param language_code: The language code that represents the language of the entries in your vocabulary filter.
        :param vocabulary_filter_name: A unique name, chosen by you, for your custom vocabulary filter.
        :param data_access_role_arn: The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files.
        :param tags: Tags associated with the vocabulary filter.
        :param vocabulary_filter_file_uri: The Amazon S3 location of the text file that contains your custom vocabulary filter terms.
        :param words: Use this parameter if you want to create your custom vocabulary filter by including all desired terms, as comma-separated values, within your request.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4f379d43d1fb010196b1b7a0b7e190146a43a7817c4380b2a03c12a999b04403)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVocabularyFilterProps(
            language_code=language_code,
            vocabulary_filter_name=vocabulary_filter_name,
            data_access_role_arn=data_access_role_arn,
            tags=tags,
            vocabulary_filter_file_uri=vocabulary_filter_file_uri,
            words=words,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVocabularyFilter")
    @builtins.classmethod
    def arn_for_vocabulary_filter(
        cls,
        resource: "_aws_transcribe_5ed72ef1.IVocabularyFilterRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3d0d5fdd990c1e6f1f1578a57f2b1e07615e187c424de0cdb38c99ece36033ef)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVocabularyFilter", [resource]))

    @jsii.member(jsii_name="isCfnVocabularyFilter")
    @builtins.classmethod
    def is_cfn_vocabulary_filter(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVocabularyFilter.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b0842abbe55306ec5ea964df044d6068a3c93f961b8887d1ef9ab244365b53f9)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVocabularyFilter", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7e830e28f80376a22cc4875f2b2300dbc631c5e21a8ae0f3c1bd24ae3571e971)
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
            type_hints = cached_type_hints(_typecheckingstub__c5fffa3ebb60cbba9b4e3ded20ec86764ef3468786e2e8168b68abbe2f0d217a)
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
        '''The Amazon Resource Name (ARN) of the vocabulary filter.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="vocabularyFilterRef")
    def vocabulary_filter_ref(
        self,
    ) -> "_aws_transcribe_5ed72ef1.VocabularyFilterReference":
        '''A reference to a VocabularyFilter resource.'''
        return typing.cast("_aws_transcribe_5ed72ef1.VocabularyFilterReference", jsii.get(self, "vocabularyFilterRef"))

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        '''The language code that represents the language of the entries in your vocabulary filter.'''
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__02de5607a020110473f71afee0afc19fa4d720c960821f6356e48a84d39652d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vocabularyFilterName")
    def vocabulary_filter_name(self) -> builtins.str:
        '''A unique name, chosen by you, for your custom vocabulary filter.'''
        return typing.cast(builtins.str, jsii.get(self, "vocabularyFilterName"))

    @vocabulary_filter_name.setter
    def vocabulary_filter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d4fd94c77da23e798b90215596efbf7d11955e5a50f658c75bdbda30e6f96924)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vocabularyFilterName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dataAccessRoleArn")
    def data_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataAccessRoleArn"))

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__23780790450e1c427f7c6e5f873fd7e2b15f7d8b507361ef12a5cc0d96a0d21a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataAccessRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags associated with the vocabulary filter.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__070bdd4161a53bdf7e27d3f41aa541151e5854ddbe9052abd9361fb6a8d67cb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vocabularyFilterFileUri")
    def vocabulary_filter_file_uri(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 location of the text file that contains your custom vocabulary filter terms.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vocabularyFilterFileUri"))

    @vocabulary_filter_file_uri.setter
    def vocabulary_filter_file_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bc1f52ba1318d8b74f111bca20754506fbde302f7929088130e8e1bc376e0c99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vocabularyFilterFileUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="words")
    def words(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Use this parameter if you want to create your custom vocabulary filter by including all desired terms, as comma-separated values, within your request.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "words"))

    @words.setter
    def words(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4c5fccbb27376565b530d579ac68343c535ef849918794d84bfb1b41241d5003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "words", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transcribe.CfnVocabularyFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "language_code": "languageCode",
        "vocabulary_filter_name": "vocabularyFilterName",
        "data_access_role_arn": "dataAccessRoleArn",
        "tags": "tags",
        "vocabulary_filter_file_uri": "vocabularyFilterFileUri",
        "words": "words",
    },
)
class CfnVocabularyFilterProps:
    def __init__(
        self,
        *,
        language_code: builtins.str,
        vocabulary_filter_name: builtins.str,
        data_access_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vocabulary_filter_file_uri: typing.Optional[builtins.str] = None,
        words: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVocabularyFilter``.

        :param language_code: The language code that represents the language of the entries in your vocabulary filter.
        :param vocabulary_filter_name: A unique name, chosen by you, for your custom vocabulary filter.
        :param data_access_role_arn: The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files.
        :param tags: Tags associated with the vocabulary filter.
        :param vocabulary_filter_file_uri: The Amazon S3 location of the text file that contains your custom vocabulary filter terms.
        :param words: Use this parameter if you want to create your custom vocabulary filter by including all desired terms, as comma-separated values, within your request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabularyfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transcribe as transcribe
            
            cfn_vocabulary_filter_props = transcribe.CfnVocabularyFilterProps(
                language_code="languageCode",
                vocabulary_filter_name="vocabularyFilterName",
            
                # the properties below are optional
                data_access_role_arn="dataAccessRoleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vocabulary_filter_file_uri="vocabularyFilterFileUri",
                words=["words"]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2cdb6bfa5f45a15ed27722517b6b7c36595415a65bd62ee987f46cf27184b4b2)
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument vocabulary_filter_name", value=vocabulary_filter_name, expected_type=type_hints["vocabulary_filter_name"])
            check_type(argname="argument data_access_role_arn", value=data_access_role_arn, expected_type=type_hints["data_access_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vocabulary_filter_file_uri", value=vocabulary_filter_file_uri, expected_type=type_hints["vocabulary_filter_file_uri"])
            check_type(argname="argument words", value=words, expected_type=type_hints["words"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "language_code": language_code,
            "vocabulary_filter_name": vocabulary_filter_name,
        }
        if data_access_role_arn is not None:
            self._values["data_access_role_arn"] = data_access_role_arn
        if tags is not None:
            self._values["tags"] = tags
        if vocabulary_filter_file_uri is not None:
            self._values["vocabulary_filter_file_uri"] = vocabulary_filter_file_uri
        if words is not None:
            self._values["words"] = words

    @builtins.property
    def language_code(self) -> builtins.str:
        '''The language code that represents the language of the entries in your vocabulary filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabularyfilter.html#cfn-transcribe-vocabularyfilter-languagecode
        '''
        result = self._values.get("language_code")
        assert result is not None, "Required property 'language_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vocabulary_filter_name(self) -> builtins.str:
        '''A unique name, chosen by you, for your custom vocabulary filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabularyfilter.html#cfn-transcribe-vocabularyfilter-vocabularyfiltername
        '''
        result = self._values.get("vocabulary_filter_name")
        assert result is not None, "Required property 'vocabulary_filter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabularyfilter.html#cfn-transcribe-vocabularyfilter-dataaccessrolearn
        '''
        result = self._values.get("data_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags associated with the vocabulary filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabularyfilter.html#cfn-transcribe-vocabularyfilter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def vocabulary_filter_file_uri(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 location of the text file that contains your custom vocabulary filter terms.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabularyfilter.html#cfn-transcribe-vocabularyfilter-vocabularyfilterfileuri
        '''
        result = self._values.get("vocabulary_filter_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def words(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Use this parameter if you want to create your custom vocabulary filter by including all desired terms, as comma-separated values, within your request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabularyfilter.html#cfn-transcribe-vocabularyfilter-words
        '''
        result = self._values.get("words")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVocabularyFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transcribe.CfnVocabularyProps",
    jsii_struct_bases=[],
    name_mapping={
        "language_code": "languageCode",
        "vocabulary_name": "vocabularyName",
        "data_access_role_arn": "dataAccessRoleArn",
        "phrases": "phrases",
        "tags": "tags",
        "vocabulary_file_uri": "vocabularyFileUri",
    },
)
class CfnVocabularyProps:
    def __init__(
        self,
        *,
        language_code: builtins.str,
        vocabulary_name: builtins.str,
        data_access_role_arn: typing.Optional[builtins.str] = None,
        phrases: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vocabulary_file_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVocabulary``.

        :param language_code: The language code that represents the language of the entries in your custom vocabulary. Each custom vocabulary must contain terms in only one language.
        :param vocabulary_name: A unique name, chosen by you, for your custom vocabulary. This name is case sensitive, cannot contain spaces, and must be unique within an AWS account.
        :param data_access_role_arn: The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input file.
        :param phrases: Use this parameter if you want to create your custom vocabulary by including all desired terms, as comma-separated values, within your request. You cannot use this parameter together with VocabularyFileUri.
        :param tags: Adds one or more custom tags, each in the form of a key:value pair, to the custom vocabulary.
        :param vocabulary_file_uri: The Amazon S3 location of the text file that contains your custom vocabulary. You cannot use this parameter together with Phrases.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabulary.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transcribe as transcribe
            
            cfn_vocabulary_props = transcribe.CfnVocabularyProps(
                language_code="languageCode",
                vocabulary_name="vocabularyName",
            
                # the properties below are optional
                data_access_role_arn="dataAccessRoleArn",
                phrases=["phrases"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vocabulary_file_uri="vocabularyFileUri"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__00f00526eca9ca9edaa78f01c6bcd98168165bdf34269d516402f78c5c11569f)
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument vocabulary_name", value=vocabulary_name, expected_type=type_hints["vocabulary_name"])
            check_type(argname="argument data_access_role_arn", value=data_access_role_arn, expected_type=type_hints["data_access_role_arn"])
            check_type(argname="argument phrases", value=phrases, expected_type=type_hints["phrases"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vocabulary_file_uri", value=vocabulary_file_uri, expected_type=type_hints["vocabulary_file_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "language_code": language_code,
            "vocabulary_name": vocabulary_name,
        }
        if data_access_role_arn is not None:
            self._values["data_access_role_arn"] = data_access_role_arn
        if phrases is not None:
            self._values["phrases"] = phrases
        if tags is not None:
            self._values["tags"] = tags
        if vocabulary_file_uri is not None:
            self._values["vocabulary_file_uri"] = vocabulary_file_uri

    @builtins.property
    def language_code(self) -> builtins.str:
        '''The language code that represents the language of the entries in your custom vocabulary.

        Each custom vocabulary must contain terms in only one language.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabulary.html#cfn-transcribe-vocabulary-languagecode
        '''
        result = self._values.get("language_code")
        assert result is not None, "Required property 'language_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vocabulary_name(self) -> builtins.str:
        '''A unique name, chosen by you, for your custom vocabulary.

        This name is case sensitive, cannot contain spaces, and must be unique within an AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabulary.html#cfn-transcribe-vocabulary-vocabularyname
        '''
        result = self._values.get("vocabulary_name")
        assert result is not None, "Required property 'vocabulary_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input file.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabulary.html#cfn-transcribe-vocabulary-dataaccessrolearn
        '''
        result = self._values.get("data_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phrases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Use this parameter if you want to create your custom vocabulary by including all desired terms, as comma-separated values, within your request.

        You cannot use this parameter together with VocabularyFileUri.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabulary.html#cfn-transcribe-vocabulary-phrases
        '''
        result = self._values.get("phrases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Adds one or more custom tags, each in the form of a key:value pair, to the custom vocabulary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabulary.html#cfn-transcribe-vocabulary-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def vocabulary_file_uri(self) -> typing.Optional[builtins.str]:
        '''The Amazon S3 location of the text file that contains your custom vocabulary.

        You cannot use this parameter together with Phrases.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transcribe-vocabulary.html#cfn-transcribe-vocabulary-vocabularyfileuri
        '''
        result = self._values.get("vocabulary_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVocabularyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCallAnalyticsCategory",
    "CfnCallAnalyticsCategoryProps",
    "CfnMedicalVocabulary",
    "CfnMedicalVocabularyProps",
    "CfnVocabulary",
    "CfnVocabularyFilter",
    "CfnVocabularyFilterProps",
    "CfnVocabularyProps",
]

publication.publish()

def _typecheckingstub__c054cf749f051b84a6a814fff3e3c75987682766e5a8ff88bc2cf4dffd41a48a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    category_name: builtins.str,
    rules: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    input_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d8571a53687a8b6533cb284a2f98ed8feed66ee602c8f7f36ddcb16c9e88ef8(
    resource: _aws_transcribe_5ed72ef1.ICallAnalyticsCategoryRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b1ac3d028d43d60d3c298fc55864255b44820f4bd60d6937ec5e842b8fc6a9(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__632d59371f38094a22db12c913e32ade7052ca38e8bfeb1799c31dff0f69fecf(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fba6dad15065e4454fe009dd4311676ae9d12d5c1f9a4b13ab55bacf68719cc5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a74a59fcc2ea39f9e98156d83686b31507d8a735ff5369691de802f24304af5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f6165ae0d3e465b4ad5f4d8fd7a9d9de61baabcdaafe835737fdee1a822ced4(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnCallAnalyticsCategory.RuleProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f5685f60a622014fa6122c6f25ad3a7470136f979faec970d763d99bc2408a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a263451f5e03dfbf9d0d8c77fc4bfdadcf134a226b833cb4a830522cc00ee43e(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a1199eebacc06a7c7c01b5682035bb1ef19fc0885a4c52790ccb6259d14737(
    *,
    end_time: typing.Optional[jsii.Number] = None,
    first: typing.Optional[jsii.Number] = None,
    last: typing.Optional[jsii.Number] = None,
    start_time: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea488fa9096c7f2e3ef622f1d73b5a173a2194fffa1f5ca0b386163b72d5b04c(
    *,
    absolute_time_range: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    participant_role: typing.Optional[builtins.str] = None,
    relative_time_range: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.RelativeTimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f379146ac2727dde356ebe55d516a7c00c98768f78def996a2209eadb627524(
    *,
    absolute_time_range: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    relative_time_range: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.RelativeTimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bef6c2924461044181326d0c2452b7e50f4bdf5ee831c15eefbebfc891c438ca(
    *,
    end_percentage: typing.Optional[jsii.Number] = None,
    first: typing.Optional[jsii.Number] = None,
    last: typing.Optional[jsii.Number] = None,
    start_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f8d6b50b53d11d790fab9cbc3d94c72ebb820cc2f073c02b770896cc31558b2(
    *,
    interruption_filter: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.InterruptionFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    non_talk_time_filter: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.NonTalkTimeFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sentiment_filter: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.SentimentFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    transcript_filter: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.TranscriptFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de1687e0b020f3e94a81f75165eb33089cabc3f9e1b09518670ff829e9bc775(
    *,
    sentiments: typing.Sequence[builtins.str],
    absolute_time_range: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    participant_role: typing.Optional[builtins.str] = None,
    relative_time_range: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.RelativeTimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c158825c38df89d326ed5a53474d62c23127b4738bcfe1886d5f1e57dd00211(
    *,
    targets: typing.Sequence[builtins.str],
    transcript_filter_type: builtins.str,
    absolute_time_range: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.AbsoluteTimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    negate: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    participant_role: typing.Optional[builtins.str] = None,
    relative_time_range: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.RelativeTimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7d119aaa8c30f6f9551e7aa3e3b762678b68daf86bd57643eb1d55ca2177b57(
    *,
    category_name: builtins.str,
    rules: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCallAnalyticsCategory.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    input_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7776e2578a82c3d9c1922b43061249cbf50b611576a5817358b4841492ffbe23(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    language_code: builtins.str,
    vocabulary_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vocabulary_file_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e55c18063a6f1adb65c58874168ebf45bf99bb427f3f8f57bb8daf22fa637da(
    resource: _aws_transcribe_5ed72ef1.IMedicalVocabularyRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d139f162b485c9372d2bc1765c3ab0514142739393b560d7aaafbb791295e54(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf5a98bdc672c1897a663c442f057251d33f57b0380f3239e6c9f95f9114df8(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4619ae7b917994bfcecb38cd0a10ca5ac2a3a8224a1a6856a88a179e67b7ddd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d1569c8a62ae9ec7f30675183e5eb1dbdf44d0aa1262cc1a475c9d5e6ebaa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155f9768d7dfdd9e73091b14b64e3dfb9afaf1b5d83051d49cb9fead15fb3988(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12e3765bf8e096fb326923ede62eae98218db4a245f6b40b6c23137f29a9e9eb(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffd2b16a7bf8da4f3299e4e2559161526cebd37488425989f26b7bd3b2f86c07(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af80b22fc13d87a9875f4a8dbf0fbd8903e8fa91dcf247d5f2192eab00287ba6(
    *,
    language_code: builtins.str,
    vocabulary_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vocabulary_file_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd2b601bd5916e82ff98dc9def499623f8f7fd6873d2e0127676134d4a11d1e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    language_code: builtins.str,
    vocabulary_name: builtins.str,
    data_access_role_arn: typing.Optional[builtins.str] = None,
    phrases: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vocabulary_file_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351883d766a65bd807d44824d0ad25d28aba4285361142fd1f43c5ec9074361d(
    resource: _aws_transcribe_5ed72ef1.IVocabularyRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f46a514fb1bf01c95de95ef8e6964e66be8ad2523ae7498b91051513c1eaf0a(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f0437d44a9571dc47e9623c6679012b4688339532b67abda23a3a7ce0406694(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19769c9ee59d11ef827f65092d13b64c582ae68b96ba11c84770eb5540404855(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c241fbb212fca3136cdb41f4c86a36889decb1b9e2d45613bf5f80d97aeb08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ba2c8f4602a07232a809477edc6567e5f286e803383a24dee8b41679c6b9346(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0364624f1743dcee3e9f2992d4566cc24703ee250bb9ae22ed26f3539a131368(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea7aa54669942067a3e7cd4b7f12d85f35d6bf6dc08c0874a471cc3103d2ad1f(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5899b6e320bc8d6d4075f904972e59283de674747dc42da93e78019fc63849aa(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7366039e3e7adc2e526bf6e87f2dd5151c0164d1170323981b75e85f4c6d83d4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f379d43d1fb010196b1b7a0b7e190146a43a7817c4380b2a03c12a999b04403(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    language_code: builtins.str,
    vocabulary_filter_name: builtins.str,
    data_access_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vocabulary_filter_file_uri: typing.Optional[builtins.str] = None,
    words: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0d5fdd990c1e6f1f1578a57f2b1e07615e187c424de0cdb38c99ece36033ef(
    resource: _aws_transcribe_5ed72ef1.IVocabularyFilterRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0842abbe55306ec5ea964df044d6068a3c93f961b8887d1ef9ab244365b53f9(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e830e28f80376a22cc4875f2b2300dbc631c5e21a8ae0f3c1bd24ae3571e971(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5fffa3ebb60cbba9b4e3ded20ec86764ef3468786e2e8168b68abbe2f0d217a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02de5607a020110473f71afee0afc19fa4d720c960821f6356e48a84d39652d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4fd94c77da23e798b90215596efbf7d11955e5a50f658c75bdbda30e6f96924(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23780790450e1c427f7c6e5f873fd7e2b15f7d8b507361ef12a5cc0d96a0d21a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__070bdd4161a53bdf7e27d3f41aa541151e5854ddbe9052abd9361fb6a8d67cb7(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc1f52ba1318d8b74f111bca20754506fbde302f7929088130e8e1bc376e0c99(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c5fccbb27376565b530d579ac68343c535ef849918794d84bfb1b41241d5003(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cdb6bfa5f45a15ed27722517b6b7c36595415a65bd62ee987f46cf27184b4b2(
    *,
    language_code: builtins.str,
    vocabulary_filter_name: builtins.str,
    data_access_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vocabulary_filter_file_uri: typing.Optional[builtins.str] = None,
    words: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f00526eca9ca9edaa78f01c6bcd98168165bdf34269d516402f78c5c11569f(
    *,
    language_code: builtins.str,
    vocabulary_name: builtins.str,
    data_access_role_arn: typing.Optional[builtins.str] = None,
    phrases: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vocabulary_file_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
