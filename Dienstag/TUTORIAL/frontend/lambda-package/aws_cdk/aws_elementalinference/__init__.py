r'''
# AWS::ElementalInference Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_elementalinference as elementalinference
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ElementalInference construct libraries](https://constructs.dev/search?q=elementalinference)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ElementalInference resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElementalInference.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ElementalInference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElementalInference.html).

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
    import aws_cdk.interfaces.aws_elementalinference as _aws_elementalinference_0f509120
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_elementalinference_0f509120 = _LazyImport("aws_cdk.interfaces.aws_elementalinference")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_elementalinference_0f509120.IDictionaryRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnDictionary(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elementalinference.CfnDictionary",
):
    '''Represents a custom dictionary for improving transcription accuracy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-dictionary.html
    :cloudformationResource: AWS::ElementalInference::Dictionary
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elementalinference as elementalinference
        
        cfn_dictionary = elementalinference.CfnDictionary(self, "MyCfnDictionary",
            language="language",
            name="name",
        
            # the properties below are optional
            entries="entries",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        language: builtins.str,
        name: builtins.str,
        entries: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ElementalInference::Dictionary``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param language: 
        :param name: 
        :param entries: 
        :param tags: 
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cb19e43a3823c0464788a8740b3a376bab8d792ca01b04cc7e8fd8caa98dce96)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDictionaryProps(
            language=language, name=name, entries=entries, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDictionary")
    @builtins.classmethod
    def arn_for_dictionary(
        cls,
        resource: "_aws_elementalinference_0f509120.IDictionaryRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__575acbdb404cc2fc60fd5541030f7f0171f8e072ea75445534f662d0bd18482f)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDictionary", [resource]))

    @jsii.member(jsii_name="isCfnDictionary")
    @builtins.classmethod
    def is_cfn_dictionary(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDictionary.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8c2833a44823385bc7675ecd9aff06abcc6b05fcacafbd76825b2a5cc5c91f75)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDictionary", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__64aba6c2e1ef5c8be2086d73065ee8b49157f97877b42f1f8dcebb4d728db012)
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
            type_hints = cached_type_hints(_typecheckingstub__278c4875549a5c5aecd91efca14bd1c6418d961ab0338aba324ebf3077809653)
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
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
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
    @jsii.member(jsii_name="dictionaryRef")
    def dictionary_ref(self) -> "_aws_elementalinference_0f509120.DictionaryReference":
        '''A reference to a Dictionary resource.'''
        return typing.cast("_aws_elementalinference_0f509120.DictionaryReference", jsii.get(self, "dictionaryRef"))

    @builtins.property
    @jsii.member(jsii_name="language")
    def language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "language"))

    @language.setter
    def language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__734e92c7f956c44d94fbc188e912c8b37a4e3616c1c59d03a685a23692428d05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "language", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__81d9bc21fc4dcf609fe6775bdc94be054fdd976c3ece189115b57d2f538ec9f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="entries")
    def entries(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entries"))

    @entries.setter
    def entries(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5a05e5736995207c2d2fc9a3d6e3e7b2590ae8ed1a7702ac2df1b9fba7241ebc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entries", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e397dca2baffe3ec040dd8bd16563c7bef34ae645c8bb604730b3420086d5898)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elementalinference.CfnDictionaryProps",
    jsii_struct_bases=[],
    name_mapping={
        "language": "language",
        "name": "name",
        "entries": "entries",
        "tags": "tags",
    },
)
class CfnDictionaryProps:
    def __init__(
        self,
        *,
        language: builtins.str,
        name: builtins.str,
        entries: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDictionary``.

        :param language: 
        :param name: 
        :param entries: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-dictionary.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elementalinference as elementalinference
            
            cfn_dictionary_props = elementalinference.CfnDictionaryProps(
                language="language",
                name="name",
            
                # the properties below are optional
                entries="entries",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9dd37114d271fae76e5cb86f97d7d3bb0ff7eaef406d3683fdc566d5fa38e81e)
            check_type(argname="argument language", value=language, expected_type=type_hints["language"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "language": language,
            "name": name,
        }
        if entries is not None:
            self._values["entries"] = entries
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def language(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-dictionary.html#cfn-elementalinference-dictionary-language
        '''
        result = self._values.get("language")
        assert result is not None, "Required property 'language' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-dictionary.html#cfn-elementalinference-dictionary-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entries(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-dictionary.html#cfn-elementalinference-dictionary-entries
        '''
        result = self._values.get("entries")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-dictionary.html#cfn-elementalinference-dictionary-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDictionaryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_elementalinference_0f509120.IFeedRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnFeed(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed",
):
    '''Represents a feed that receives media for inference processing.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html
    :cloudformationResource: AWS::ElementalInference::Feed
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elementalinference as elementalinference
        
        cfn_feed = elementalinference.CfnFeed(self, "MyCfnFeed",
            name="name",
            outputs=[elementalinference.CfnFeed.GetOutputProperty(
                name="name",
                output_config=elementalinference.CfnFeed.OutputConfigProperty(
                    clipping=elementalinference.CfnFeed.ClippingConfigProperty(
                        callback_metadata="callbackMetadata",
                        data_source_configuration=elementalinference.CfnFeed.DataSourceConfigurationProperty(
                            fixture_id="fixtureId"
                        )
                    ),
                    cropping=elementalinference.CfnFeed.CroppingConfigProperty(
                        template_groups=[elementalinference.CfnFeed.TemplateGroupProperty(
                            name="name",
                            template_uris=["templateUris"]
                        )]
                    ),
                    subtitling=elementalinference.CfnFeed.SubtitlingConfigProperty(
                        language="language",
        
                        # the properties below are optional
                        aspect_ratio=elementalinference.CfnFeed.AspectRatioProperty(
                            height=123,
                            width=123
                        ),
                        dictionary="dictionary",
                        profanity_filter="profanityFilter"
                    )
                ),
                status="status",
        
                # the properties below are optional
                description="description"
            )],
        
            # the properties below are optional
            access_role_arn="accessRoleArn",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        outputs: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.GetOutputProperty", typing.Dict[builtins.str, typing.Any]]]]],
        access_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ElementalInference::Feed``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: 
        :param outputs: 
        :param access_role_arn: 
        :param tags: 
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__086c1fcdd22f4573bbf9e5858e698d4a67c6e5f5679291a457c0399ac83d35d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFeedProps(
            name=name, outputs=outputs, access_role_arn=access_role_arn, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForFeed")
    @builtins.classmethod
    def arn_for_feed(
        cls,
        resource: "_aws_elementalinference_0f509120.IFeedRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f0e3705d6c009d3ad14dba82dc352718235a5afb9e6f07c2dfec5360885f5b8f)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForFeed", [resource]))

    @jsii.member(jsii_name="isCfnFeed")
    @builtins.classmethod
    def is_cfn_feed(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFeed.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9717524a84639953c97d1079ee02198d0c70203475e0a48c5a4ff3f60d192471)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFeed", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a16b23304f2dde726d178cff21ddda9392321b31d4d71b68e4b79cc737bc01da)
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
            type_hints = cached_type_hints(_typecheckingstub__0cc422f59d4b34fb0f9a25421f746cad0611bf7d1f39c981e4e55506b7df2ef3)
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
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDataEndpoints")
    def attr_data_endpoints(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: DataEndpoints
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDataEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
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
    @jsii.member(jsii_name="feedRef")
    def feed_ref(self) -> "_aws_elementalinference_0f509120.FeedReference":
        '''A reference to a Feed resource.'''
        return typing.cast("_aws_elementalinference_0f509120.FeedReference", jsii.get(self, "feedRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d75eaca9c34446747fb20283badafe891b40a3fba2ee34a519fcaf304f16dd07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.GetOutputProperty"]]]:
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.GetOutputProperty"]]], jsii.get(self, "outputs"))

    @outputs.setter
    def outputs(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.GetOutputProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b5c56fe45498c7c2ef7666681ed87b6d6305ad4ea8b27076706113d35691a314)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="accessRoleArn")
    def access_role_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessRoleArn"))

    @access_role_arn.setter
    def access_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0cec7d77ff0c70d567b933bae195ed89ba736dcd21743aa3f9078e59dde626a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e9e0bc362d8a7be8bdb4db49c0fb751ca65a9bf66da03ffdc2fb00af3e5efb90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.AspectRatioProperty",
        jsii_struct_bases=[],
        name_mapping={"height": "height", "width": "width"},
    )
    class AspectRatioProperty:
        def __init__(self, *, height: jsii.Number, width: jsii.Number) -> None:
            '''
            :param height: 
            :param width: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-aspectratio.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                aspect_ratio_property = elementalinference.CfnFeed.AspectRatioProperty(
                    height=123,
                    width=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__792d393b28a32ab459f4a4c4e6d800f3397b80f9a65080813eac36da35b36641)
                check_type(argname="argument height", value=height, expected_type=type_hints["height"])
                check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "height": height,
                "width": width,
            }

        @builtins.property
        def height(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-aspectratio.html#cfn-elementalinference-feed-aspectratio-height
            '''
            result = self._values.get("height")
            assert result is not None, "Required property 'height' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def width(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-aspectratio.html#cfn-elementalinference-feed-aspectratio-width
            '''
            result = self._values.get("width")
            assert result is not None, "Required property 'width' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AspectRatioProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.ClippingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "callback_metadata": "callbackMetadata",
            "data_source_configuration": "dataSourceConfiguration",
        },
    )
    class ClippingConfigProperty:
        def __init__(
            self,
            *,
            callback_metadata: typing.Optional[builtins.str] = None,
            data_source_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.DataSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param callback_metadata: 
            :param data_source_configuration: Identifies the fixture whose event data Elemental Inference maps onto the clipping metadata for an output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-clippingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                clipping_config_property = elementalinference.CfnFeed.ClippingConfigProperty(
                    callback_metadata="callbackMetadata",
                    data_source_configuration=elementalinference.CfnFeed.DataSourceConfigurationProperty(
                        fixture_id="fixtureId"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e6a4ba370813bfb444bc9ceafafb712ea485e1284fa02f399aac4531d0015262)
                check_type(argname="argument callback_metadata", value=callback_metadata, expected_type=type_hints["callback_metadata"])
                check_type(argname="argument data_source_configuration", value=data_source_configuration, expected_type=type_hints["data_source_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if callback_metadata is not None:
                self._values["callback_metadata"] = callback_metadata
            if data_source_configuration is not None:
                self._values["data_source_configuration"] = data_source_configuration

        @builtins.property
        def callback_metadata(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-clippingconfig.html#cfn-elementalinference-feed-clippingconfig-callbackmetadata
            '''
            result = self._values.get("callback_metadata")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_source_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.DataSourceConfigurationProperty"]]:
            '''Identifies the fixture whose event data Elemental Inference maps onto the clipping metadata for an output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-clippingconfig.html#cfn-elementalinference-feed-clippingconfig-datasourceconfiguration
            '''
            result = self._values.get("data_source_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.DataSourceConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClippingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.CroppingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"template_groups": "templateGroups"},
    )
    class CroppingConfigProperty:
        def __init__(
            self,
            *,
            template_groups: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.TemplateGroupProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param template_groups: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-croppingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                cropping_config_property = elementalinference.CfnFeed.CroppingConfigProperty(
                    template_groups=[elementalinference.CfnFeed.TemplateGroupProperty(
                        name="name",
                        template_uris=["templateUris"]
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__5cc4f807794b7274bf9c514b2958efe7c8139433e1d50c19a8687aa8e989ed76)
                check_type(argname="argument template_groups", value=template_groups, expected_type=type_hints["template_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if template_groups is not None:
                self._values["template_groups"] = template_groups

        @builtins.property
        def template_groups(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.TemplateGroupProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-croppingconfig.html#cfn-elementalinference-feed-croppingconfig-templategroups
            '''
            result = self._values.get("template_groups")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.TemplateGroupProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CroppingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.DataSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"fixture_id": "fixtureId"},
    )
    class DataSourceConfigurationProperty:
        def __init__(self, *, fixture_id: builtins.str) -> None:
            '''Identifies the fixture whose event data Elemental Inference maps onto the clipping metadata for an output.

            :param fixture_id: The ID of the fixture whose event data you want Elemental Inference to map onto this clipping output. To obtain this ID, use the SearchFixtures operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-datasourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                data_source_configuration_property = elementalinference.CfnFeed.DataSourceConfigurationProperty(
                    fixture_id="fixtureId"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__5da212fff1917d5ffbc0367ac3d7f565a9127ab3eef7843d80bf316f6bd74350)
                check_type(argname="argument fixture_id", value=fixture_id, expected_type=type_hints["fixture_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fixture_id": fixture_id,
            }

        @builtins.property
        def fixture_id(self) -> builtins.str:
            '''The ID of the fixture whose event data you want Elemental Inference to map onto this clipping output.

            To obtain this ID, use the SearchFixtures operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-datasourceconfiguration.html#cfn-elementalinference-feed-datasourceconfiguration-fixtureid
            '''
            result = self._values.get("fixture_id")
            assert result is not None, "Required property 'fixture_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.GetOutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "output_config": "outputConfig",
            "status": "status",
            "description": "description",
        },
    )
    class GetOutputProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            output_config: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.OutputConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            status: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: 
            :param output_config: 
            :param status: 
            :param description: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                get_output_property = elementalinference.CfnFeed.GetOutputProperty(
                    name="name",
                    output_config=elementalinference.CfnFeed.OutputConfigProperty(
                        clipping=elementalinference.CfnFeed.ClippingConfigProperty(
                            callback_metadata="callbackMetadata",
                            data_source_configuration=elementalinference.CfnFeed.DataSourceConfigurationProperty(
                                fixture_id="fixtureId"
                            )
                        ),
                        cropping=elementalinference.CfnFeed.CroppingConfigProperty(
                            template_groups=[elementalinference.CfnFeed.TemplateGroupProperty(
                                name="name",
                                template_uris=["templateUris"]
                            )]
                        ),
                        subtitling=elementalinference.CfnFeed.SubtitlingConfigProperty(
                            language="language",
                
                            # the properties below are optional
                            aspect_ratio=elementalinference.CfnFeed.AspectRatioProperty(
                                height=123,
                                width=123
                            ),
                            dictionary="dictionary",
                            profanity_filter="profanityFilter"
                        )
                    ),
                    status="status",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d7c0accadaf3abd8820d59ff8ea7b283716805039f5029d7aafb4b9c614a96cb)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument output_config", value=output_config, expected_type=type_hints["output_config"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "output_config": output_config,
                "status": status,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html#cfn-elementalinference-feed-getoutput-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output_config(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.OutputConfigProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html#cfn-elementalinference-feed-getoutput-outputconfig
            '''
            result = self._values.get("output_config")
            assert result is not None, "Required property 'output_config' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.OutputConfigProperty"], result)

        @builtins.property
        def status(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html#cfn-elementalinference-feed-getoutput-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html#cfn-elementalinference-feed-getoutput-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GetOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.OutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "clipping": "clipping",
            "cropping": "cropping",
            "subtitling": "subtitling",
        },
    )
    class OutputConfigProperty:
        def __init__(
            self,
            *,
            clipping: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.ClippingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cropping: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.CroppingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            subtitling: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.SubtitlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param clipping: 
            :param cropping: 
            :param subtitling: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-outputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                output_config_property = elementalinference.CfnFeed.OutputConfigProperty(
                    clipping=elementalinference.CfnFeed.ClippingConfigProperty(
                        callback_metadata="callbackMetadata",
                        data_source_configuration=elementalinference.CfnFeed.DataSourceConfigurationProperty(
                            fixture_id="fixtureId"
                        )
                    ),
                    cropping=elementalinference.CfnFeed.CroppingConfigProperty(
                        template_groups=[elementalinference.CfnFeed.TemplateGroupProperty(
                            name="name",
                            template_uris=["templateUris"]
                        )]
                    ),
                    subtitling=elementalinference.CfnFeed.SubtitlingConfigProperty(
                        language="language",
                
                        # the properties below are optional
                        aspect_ratio=elementalinference.CfnFeed.AspectRatioProperty(
                            height=123,
                            width=123
                        ),
                        dictionary="dictionary",
                        profanity_filter="profanityFilter"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2903ddb4ce42c6a1ffd01fed7c6276e891d4bc19ee8d5416c7af548c5968e928)
                check_type(argname="argument clipping", value=clipping, expected_type=type_hints["clipping"])
                check_type(argname="argument cropping", value=cropping, expected_type=type_hints["cropping"])
                check_type(argname="argument subtitling", value=subtitling, expected_type=type_hints["subtitling"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if clipping is not None:
                self._values["clipping"] = clipping
            if cropping is not None:
                self._values["cropping"] = cropping
            if subtitling is not None:
                self._values["subtitling"] = subtitling

        @builtins.property
        def clipping(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.ClippingConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-outputconfig.html#cfn-elementalinference-feed-outputconfig-clipping
            '''
            result = self._values.get("clipping")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.ClippingConfigProperty"]], result)

        @builtins.property
        def cropping(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.CroppingConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-outputconfig.html#cfn-elementalinference-feed-outputconfig-cropping
            '''
            result = self._values.get("cropping")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.CroppingConfigProperty"]], result)

        @builtins.property
        def subtitling(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.SubtitlingConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-outputconfig.html#cfn-elementalinference-feed-outputconfig-subtitling
            '''
            result = self._values.get("subtitling")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.SubtitlingConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.SubtitlingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "language": "language",
            "aspect_ratio": "aspectRatio",
            "dictionary": "dictionary",
            "profanity_filter": "profanityFilter",
        },
    )
    class SubtitlingConfigProperty:
        def __init__(
            self,
            *,
            language: builtins.str,
            aspect_ratio: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.AspectRatioProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dictionary: typing.Optional[builtins.str] = None,
            profanity_filter: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param language: 
            :param aspect_ratio: 
            :param dictionary: 
            :param profanity_filter: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-subtitlingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                subtitling_config_property = elementalinference.CfnFeed.SubtitlingConfigProperty(
                    language="language",
                
                    # the properties below are optional
                    aspect_ratio=elementalinference.CfnFeed.AspectRatioProperty(
                        height=123,
                        width=123
                    ),
                    dictionary="dictionary",
                    profanity_filter="profanityFilter"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__055a064b675d2d5bd0b0c8c5622cbbab95267c2ca5e1f1c134ef928ededc9560)
                check_type(argname="argument language", value=language, expected_type=type_hints["language"])
                check_type(argname="argument aspect_ratio", value=aspect_ratio, expected_type=type_hints["aspect_ratio"])
                check_type(argname="argument dictionary", value=dictionary, expected_type=type_hints["dictionary"])
                check_type(argname="argument profanity_filter", value=profanity_filter, expected_type=type_hints["profanity_filter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "language": language,
            }
            if aspect_ratio is not None:
                self._values["aspect_ratio"] = aspect_ratio
            if dictionary is not None:
                self._values["dictionary"] = dictionary
            if profanity_filter is not None:
                self._values["profanity_filter"] = profanity_filter

        @builtins.property
        def language(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-subtitlingconfig.html#cfn-elementalinference-feed-subtitlingconfig-language
            '''
            result = self._values.get("language")
            assert result is not None, "Required property 'language' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aspect_ratio(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.AspectRatioProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-subtitlingconfig.html#cfn-elementalinference-feed-subtitlingconfig-aspectratio
            '''
            result = self._values.get("aspect_ratio")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.AspectRatioProperty"]], result)

        @builtins.property
        def dictionary(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-subtitlingconfig.html#cfn-elementalinference-feed-subtitlingconfig-dictionary
            '''
            result = self._values.get("dictionary")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def profanity_filter(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-subtitlingconfig.html#cfn-elementalinference-feed-subtitlingconfig-profanityfilter
            '''
            result = self._values.get("profanity_filter")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubtitlingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.TemplateGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "template_uris": "templateUris"},
    )
    class TemplateGroupProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            template_uris: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param name: 
            :param template_uris: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-templategroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                template_group_property = elementalinference.CfnFeed.TemplateGroupProperty(
                    name="name",
                    template_uris=["templateUris"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6c0d96861e696386c42a9d2e4b9b5a7e1c0f4fc381aed2107adf35e37a7be787)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument template_uris", value=template_uris, expected_type=type_hints["template_uris"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "template_uris": template_uris,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-templategroup.html#cfn-elementalinference-feed-templategroup-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def template_uris(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-templategroup.html#cfn-elementalinference-feed-templategroup-templateuris
            '''
            result = self._values.get("template_uris")
            assert result is not None, "Required property 'template_uris' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeedProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "outputs": "outputs",
        "access_role_arn": "accessRoleArn",
        "tags": "tags",
    },
)
class CfnFeedProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        outputs: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFeed.GetOutputProperty", typing.Dict[builtins.str, typing.Any]]]]],
        access_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFeed``.

        :param name: 
        :param outputs: 
        :param access_role_arn: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elementalinference as elementalinference
            
            cfn_feed_props = elementalinference.CfnFeedProps(
                name="name",
                outputs=[elementalinference.CfnFeed.GetOutputProperty(
                    name="name",
                    output_config=elementalinference.CfnFeed.OutputConfigProperty(
                        clipping=elementalinference.CfnFeed.ClippingConfigProperty(
                            callback_metadata="callbackMetadata",
                            data_source_configuration=elementalinference.CfnFeed.DataSourceConfigurationProperty(
                                fixture_id="fixtureId"
                            )
                        ),
                        cropping=elementalinference.CfnFeed.CroppingConfigProperty(
                            template_groups=[elementalinference.CfnFeed.TemplateGroupProperty(
                                name="name",
                                template_uris=["templateUris"]
                            )]
                        ),
                        subtitling=elementalinference.CfnFeed.SubtitlingConfigProperty(
                            language="language",
            
                            # the properties below are optional
                            aspect_ratio=elementalinference.CfnFeed.AspectRatioProperty(
                                height=123,
                                width=123
                            ),
                            dictionary="dictionary",
                            profanity_filter="profanityFilter"
                        )
                    ),
                    status="status",
            
                    # the properties below are optional
                    description="description"
                )],
            
                # the properties below are optional
                access_role_arn="accessRoleArn",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b20c116466754eabef3c4516fae5bfe05f1720d03f7fdf1d8e53dfff7e268dd1)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument access_role_arn", value=access_role_arn, expected_type=type_hints["access_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "outputs": outputs,
        }
        if access_role_arn is not None:
            self._values["access_role_arn"] = access_role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html#cfn-elementalinference-feed-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.GetOutputProperty"]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html#cfn-elementalinference-feed-outputs
        '''
        result = self._values.get("outputs")
        assert result is not None, "Required property 'outputs' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFeed.GetOutputProperty"]]], result)

    @builtins.property
    def access_role_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html#cfn-elementalinference-feed-accessrolearn
        '''
        result = self._values.get("access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html#cfn-elementalinference-feed-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFeedProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDictionary",
    "CfnDictionaryProps",
    "CfnFeed",
    "CfnFeedProps",
]

publication.publish()

def _typecheckingstub__cb19e43a3823c0464788a8740b3a376bab8d792ca01b04cc7e8fd8caa98dce96(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    language: builtins.str,
    name: builtins.str,
    entries: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575acbdb404cc2fc60fd5541030f7f0171f8e072ea75445534f662d0bd18482f(
    resource: _aws_elementalinference_0f509120.IDictionaryRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c2833a44823385bc7675ecd9aff06abcc6b05fcacafbd76825b2a5cc5c91f75(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64aba6c2e1ef5c8be2086d73065ee8b49157f97877b42f1f8dcebb4d728db012(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__278c4875549a5c5aecd91efca14bd1c6418d961ab0338aba324ebf3077809653(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__734e92c7f956c44d94fbc188e912c8b37a4e3616c1c59d03a685a23692428d05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d9bc21fc4dcf609fe6775bdc94be054fdd976c3ece189115b57d2f538ec9f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a05e5736995207c2d2fc9a3d6e3e7b2590ae8ed1a7702ac2df1b9fba7241ebc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e397dca2baffe3ec040dd8bd16563c7bef34ae645c8bb604730b3420086d5898(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dd37114d271fae76e5cb86f97d7d3bb0ff7eaef406d3683fdc566d5fa38e81e(
    *,
    language: builtins.str,
    name: builtins.str,
    entries: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086c1fcdd22f4573bbf9e5858e698d4a67c6e5f5679291a457c0399ac83d35d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    outputs: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.GetOutputProperty, typing.Dict[builtins.str, typing.Any]]]]],
    access_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e3705d6c009d3ad14dba82dc352718235a5afb9e6f07c2dfec5360885f5b8f(
    resource: _aws_elementalinference_0f509120.IFeedRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9717524a84639953c97d1079ee02198d0c70203475e0a48c5a4ff3f60d192471(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16b23304f2dde726d178cff21ddda9392321b31d4d71b68e4b79cc737bc01da(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc422f59d4b34fb0f9a25421f746cad0611bf7d1f39c981e4e55506b7df2ef3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d75eaca9c34446747fb20283badafe891b40a3fba2ee34a519fcaf304f16dd07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5c56fe45498c7c2ef7666681ed87b6d6305ad4ea8b27076706113d35691a314(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnFeed.GetOutputProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cec7d77ff0c70d567b933bae195ed89ba736dcd21743aa3f9078e59dde626a6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e0bc362d8a7be8bdb4db49c0fb751ca65a9bf66da03ffdc2fb00af3e5efb90(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__792d393b28a32ab459f4a4c4e6d800f3397b80f9a65080813eac36da35b36641(
    *,
    height: jsii.Number,
    width: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a4ba370813bfb444bc9ceafafb712ea485e1284fa02f399aac4531d0015262(
    *,
    callback_metadata: typing.Optional[builtins.str] = None,
    data_source_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.DataSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cc4f807794b7274bf9c514b2958efe7c8139433e1d50c19a8687aa8e989ed76(
    *,
    template_groups: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.TemplateGroupProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5da212fff1917d5ffbc0367ac3d7f565a9127ab3eef7843d80bf316f6bd74350(
    *,
    fixture_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c0accadaf3abd8820d59ff8ea7b283716805039f5029d7aafb4b9c614a96cb(
    *,
    name: builtins.str,
    output_config: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.OutputConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    status: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2903ddb4ce42c6a1ffd01fed7c6276e891d4bc19ee8d5416c7af548c5968e928(
    *,
    clipping: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.ClippingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cropping: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.CroppingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    subtitling: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.SubtitlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__055a064b675d2d5bd0b0c8c5622cbbab95267c2ca5e1f1c134ef928ededc9560(
    *,
    language: builtins.str,
    aspect_ratio: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.AspectRatioProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dictionary: typing.Optional[builtins.str] = None,
    profanity_filter: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c0d96861e696386c42a9d2e4b9b5a7e1c0f4fc381aed2107adf35e37a7be787(
    *,
    name: builtins.str,
    template_uris: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20c116466754eabef3c4516fae5bfe05f1720d03f7fdf1d8e53dfff7e268dd1(
    *,
    name: builtins.str,
    outputs: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFeed.GetOutputProperty, typing.Dict[builtins.str, typing.Any]]]]],
    access_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
