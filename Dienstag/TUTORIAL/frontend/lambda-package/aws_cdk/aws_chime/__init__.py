r'''
# AWS::Chime Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_chime as chime
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Chime construct libraries](https://constructs.dev/search?q=chime)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Chime resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Chime.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Chime](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Chime.html).

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
    import aws_cdk.interfaces.aws_chime as _aws_chime_58870695
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_chime_58870695 = _LazyImport("aws_cdk.interfaces.aws_chime")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.IAppInstanceRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnAppInstance(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnAppInstance",
):
    '''Resource Type definition for AWS::Chime::AppInstance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstance.html
    :cloudformationResource: AWS::Chime::AppInstance
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_app_instance = chime.CfnAppInstance(self, "MyCfnAppInstance",
            name="name",
        
            # the properties below are optional
            metadata="metadata",
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
        metadata: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::AppInstance``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the AppInstance.
        :param metadata: The metadata of the AppInstance. Limited to a 1KB string in UTF-8.
        :param tags: Tags assigned to the AppInstance.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6d337d6c149cc789c0b6f05ba4ba90f831464295606b004354b7815daaed0c77)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppInstanceProps(name=name, metadata=metadata, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAppInstance")
    @builtins.classmethod
    def arn_for_app_instance(
        cls,
        resource: "_aws_chime_58870695.IAppInstanceRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4f74b0e7014ea5c23e28103a5fb5867813697fd8201279c330a3aa769bc126a1)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAppInstance", [resource]))

    @jsii.member(jsii_name="isCfnAppInstance")
    @builtins.classmethod
    def is_cfn_app_instance(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAppInstance.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c0a664656abafe2adc6e2a0a9db5e06dc33b5b3b6a0fa2a5ca0b61b7b95d0c32)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAppInstance", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__400a60274a57ac76d314b93fb263163beba6942cc730e90588d6f74e739f4eb0)
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
            type_hints = cached_type_hints(_typecheckingstub__9c4ccf5db0f869956272a9d89ee82b1cfb49e2aacbbc94b43a595151f8b37e60)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="appInstanceRef")
    def app_instance_ref(self) -> "_aws_chime_58870695.AppInstanceReference":
        '''A reference to a AppInstance resource.'''
        return typing.cast("_aws_chime_58870695.AppInstanceReference", jsii.get(self, "appInstanceRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAppInstanceArn")
    def attr_app_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) of the AppInstance.

        :cloudformationAttribute: AppInstanceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppInstanceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The time at which an AppInstance was created, as an ISO 8601 timestamp.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTimestamp")
    def attr_last_updated_timestamp(self) -> builtins.str:
        '''The time an AppInstance was last updated, as an ISO 8601 timestamp.

        :cloudformationAttribute: LastUpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTimestamp"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the AppInstance.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b72de3b84f85f89b400c53dced98e7828184761f13429f1028134b5727fe38e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[builtins.str]:
        '''The metadata of the AppInstance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a4d28a89759474ddf9cf296e1da1bbf9afe7e7c1413d9a4d175db15deaca419f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags assigned to the AppInstance.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dc357af54a794ca273668787f93dac3a63d2f85c8108d86aa56926b60d6aac5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.IAppInstanceBotRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnAppInstanceBot(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceBot",
):
    '''Resource Type definition for AWS::Chime::AppInstanceBot.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstancebot.html
    :cloudformationResource: AWS::Chime::AppInstanceBot
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_app_instance_bot = chime.CfnAppInstanceBot(self, "MyCfnAppInstanceBot",
            app_instance_arn="appInstanceArn",
            configuration=chime.CfnAppInstanceBot.ConfigurationProperty(
                lex=chime.CfnAppInstanceBot.LexConfigurationProperty(
                    lex_bot_alias_arn="lexBotAliasArn",
                    locale_id="localeId",
        
                    # the properties below are optional
                    invoked_by=chime.CfnAppInstanceBot.InvokedByProperty(
                        standard_messages="standardMessages",
                        targeted_messages="targetedMessages"
                    ),
                    responds_to="respondsTo",
                    welcome_intent="welcomeIntent"
                )
            ),
        
            # the properties below are optional
            metadata="metadata",
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
        app_instance_arn: builtins.str,
        configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAppInstanceBot.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        metadata: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::AppInstanceBot``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_instance_arn: The ARN of the AppInstance.
        :param configuration: A structure that contains configuration data.
        :param metadata: The metadata of the AppInstanceBot.
        :param name: The name of the AppInstanceBot.
        :param tags: The tags assigned to the AppInstanceBot.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fca75944f6ceb69180d3b0f352517267777aeee7ffaa12b2f1a465cf9b6a3e00)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppInstanceBotProps(
            app_instance_arn=app_instance_arn,
            configuration=configuration,
            metadata=metadata,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAppInstanceBot")
    @builtins.classmethod
    def arn_for_app_instance_bot(
        cls,
        resource: "_aws_chime_58870695.IAppInstanceBotRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__49c5faf3dcf2887594ff746db96b49d9757db79f86e9d6f358d9f275ee8c8210)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAppInstanceBot", [resource]))

    @jsii.member(jsii_name="isCfnAppInstanceBot")
    @builtins.classmethod
    def is_cfn_app_instance_bot(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAppInstanceBot.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0255372b69a195b0351367c082f9533519223c17e242b93716f61ed8e55dea62)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAppInstanceBot", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__427e24f474e9d78b560301eb631ab4ec523303c4565f63f29c83299fe5abafb1)
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
            type_hints = cached_type_hints(_typecheckingstub__d0f31284f1d604da54c34b53acb2ff3863b786fb7370f15d19da68df814cd8ad)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="appInstanceBotRef")
    def app_instance_bot_ref(self) -> "_aws_chime_58870695.AppInstanceBotReference":
        '''A reference to a AppInstanceBot resource.'''
        return typing.cast("_aws_chime_58870695.AppInstanceBotReference", jsii.get(self, "appInstanceBotRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAppInstanceBotArn")
    def attr_app_instance_bot_arn(self) -> builtins.str:
        '''The ARN of the AppInstanceBot.

        :cloudformationAttribute: AppInstanceBotArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppInstanceBotArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The time at which the AppInstanceBot was created, as an ISO 8601 timestamp.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTimestamp")
    def attr_last_updated_timestamp(self) -> builtins.str:
        '''The time at which the AppInstanceBot was last updated, as an ISO 8601 timestamp.

        :cloudformationAttribute: LastUpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTimestamp"))

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
    @jsii.member(jsii_name="appInstanceArn")
    def app_instance_arn(self) -> builtins.str:
        '''The ARN of the AppInstance.'''
        return typing.cast(builtins.str, jsii.get(self, "appInstanceArn"))

    @app_instance_arn.setter
    def app_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__13a53900f75f263ec868d4efe44340a9273169b155a8e54a68fe8cde3818baec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appInstanceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.ConfigurationProperty"]:
        '''A structure that contains configuration data.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.ConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.ConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d36a14f99ec95cd590d6c1757bb41c8b9235cf6b317fa73e6692074ed033195a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[builtins.str]:
        '''The metadata of the AppInstanceBot.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__45024baca15a880d713b7458c08c15471a9b4b4bc485fcaa496535c2d75a30a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AppInstanceBot.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__13ad6a83eab879d92eb2609e2f37735b3c2383bb2e7e24c6cefbec192e42c39e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the AppInstanceBot.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d87e45b7d9459784717058ca252a094c146e5656ea14d9da51f1cf05f4aa56d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceBot.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lex": "lex"},
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            lex: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAppInstanceBot.LexConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A structure that contains configuration data.

            :param lex: The configuration for an Amazon Lex V2 bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                configuration_property = chime.CfnAppInstanceBot.ConfigurationProperty(
                    lex=chime.CfnAppInstanceBot.LexConfigurationProperty(
                        lex_bot_alias_arn="lexBotAliasArn",
                        locale_id="localeId",
                
                        # the properties below are optional
                        invoked_by=chime.CfnAppInstanceBot.InvokedByProperty(
                            standard_messages="standardMessages",
                            targeted_messages="targetedMessages"
                        ),
                        responds_to="respondsTo",
                        welcome_intent="welcomeIntent"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__09ff343ee28319a719419e7819c467b339964da524abd8a8f50f44edd43b11a8)
                check_type(argname="argument lex", value=lex, expected_type=type_hints["lex"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lex": lex,
            }

        @builtins.property
        def lex(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.LexConfigurationProperty"]:
            '''The configuration for an Amazon Lex V2 bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-configuration.html#cfn-chime-appinstancebot-configuration-lex
            '''
            result = self._values.get("lex")
            assert result is not None, "Required property 'lex' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.LexConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceBot.InvokedByProperty",
        jsii_struct_bases=[],
        name_mapping={
            "standard_messages": "standardMessages",
            "targeted_messages": "targetedMessages",
        },
    )
    class InvokedByProperty:
        def __init__(
            self,
            *,
            standard_messages: builtins.str,
            targeted_messages: builtins.str,
        ) -> None:
            '''Specifies the type of message that triggers a bot.

            :param standard_messages: Sets standard messages as the bot trigger.
            :param targeted_messages: Sets targeted messages as the bot trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-invokedby.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                invoked_by_property = chime.CfnAppInstanceBot.InvokedByProperty(
                    standard_messages="standardMessages",
                    targeted_messages="targetedMessages"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e0a8291bb53d368f6b1012fdd17317226c377241787e7d74d9371e641c527be4)
                check_type(argname="argument standard_messages", value=standard_messages, expected_type=type_hints["standard_messages"])
                check_type(argname="argument targeted_messages", value=targeted_messages, expected_type=type_hints["targeted_messages"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "standard_messages": standard_messages,
                "targeted_messages": targeted_messages,
            }

        @builtins.property
        def standard_messages(self) -> builtins.str:
            '''Sets standard messages as the bot trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-invokedby.html#cfn-chime-appinstancebot-invokedby-standardmessages
            '''
            result = self._values.get("standard_messages")
            assert result is not None, "Required property 'standard_messages' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def targeted_messages(self) -> builtins.str:
            '''Sets targeted messages as the bot trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-invokedby.html#cfn-chime-appinstancebot-invokedby-targetedmessages
            '''
            result = self._values.get("targeted_messages")
            assert result is not None, "Required property 'targeted_messages' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InvokedByProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceBot.LexConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lex_bot_alias_arn": "lexBotAliasArn",
            "locale_id": "localeId",
            "invoked_by": "invokedBy",
            "responds_to": "respondsTo",
            "welcome_intent": "welcomeIntent",
        },
    )
    class LexConfigurationProperty:
        def __init__(
            self,
            *,
            lex_bot_alias_arn: builtins.str,
            locale_id: builtins.str,
            invoked_by: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAppInstanceBot.InvokedByProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            responds_to: typing.Optional[builtins.str] = None,
            welcome_intent: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for an Amazon Lex V2 bot.

            :param lex_bot_alias_arn: The ARN of the Amazon Lex V2 bot's alias.
            :param locale_id: Identifies the Amazon Lex V2 bot's language and locale.
            :param invoked_by: Specifies the type of message that triggers a bot.
            :param responds_to: Determines whether the Amazon Lex V2 bot responds to all standard messages. Control messages are not supported.
            :param welcome_intent: The name of the welcome intent configured in the Amazon Lex V2 bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-lexconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                lex_configuration_property = chime.CfnAppInstanceBot.LexConfigurationProperty(
                    lex_bot_alias_arn="lexBotAliasArn",
                    locale_id="localeId",
                
                    # the properties below are optional
                    invoked_by=chime.CfnAppInstanceBot.InvokedByProperty(
                        standard_messages="standardMessages",
                        targeted_messages="targetedMessages"
                    ),
                    responds_to="respondsTo",
                    welcome_intent="welcomeIntent"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__59e9097c00a1cff69d67ed6937aea0b11010ff23c371f50b9ae25d98378dbf55)
                check_type(argname="argument lex_bot_alias_arn", value=lex_bot_alias_arn, expected_type=type_hints["lex_bot_alias_arn"])
                check_type(argname="argument locale_id", value=locale_id, expected_type=type_hints["locale_id"])
                check_type(argname="argument invoked_by", value=invoked_by, expected_type=type_hints["invoked_by"])
                check_type(argname="argument responds_to", value=responds_to, expected_type=type_hints["responds_to"])
                check_type(argname="argument welcome_intent", value=welcome_intent, expected_type=type_hints["welcome_intent"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lex_bot_alias_arn": lex_bot_alias_arn,
                "locale_id": locale_id,
            }
            if invoked_by is not None:
                self._values["invoked_by"] = invoked_by
            if responds_to is not None:
                self._values["responds_to"] = responds_to
            if welcome_intent is not None:
                self._values["welcome_intent"] = welcome_intent

        @builtins.property
        def lex_bot_alias_arn(self) -> builtins.str:
            '''The ARN of the Amazon Lex V2 bot's alias.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-lexconfiguration.html#cfn-chime-appinstancebot-lexconfiguration-lexbotaliasarn
            '''
            result = self._values.get("lex_bot_alias_arn")
            assert result is not None, "Required property 'lex_bot_alias_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def locale_id(self) -> builtins.str:
            '''Identifies the Amazon Lex V2 bot's language and locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-lexconfiguration.html#cfn-chime-appinstancebot-lexconfiguration-localeid
            '''
            result = self._values.get("locale_id")
            assert result is not None, "Required property 'locale_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invoked_by(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.InvokedByProperty"]]:
            '''Specifies the type of message that triggers a bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-lexconfiguration.html#cfn-chime-appinstancebot-lexconfiguration-invokedby
            '''
            result = self._values.get("invoked_by")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.InvokedByProperty"]], result)

        @builtins.property
        def responds_to(self) -> typing.Optional[builtins.str]:
            '''Determines whether the Amazon Lex V2 bot responds to all standard messages.

            Control messages are not supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-lexconfiguration.html#cfn-chime-appinstancebot-lexconfiguration-respondsto
            '''
            result = self._values.get("responds_to")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def welcome_intent(self) -> typing.Optional[builtins.str]:
            '''The name of the welcome intent configured in the Amazon Lex V2 bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstancebot-lexconfiguration.html#cfn-chime-appinstancebot-lexconfiguration-welcomeintent
            '''
            result = self._values.get("welcome_intent")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LexConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceBotProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_instance_arn": "appInstanceArn",
        "configuration": "configuration",
        "metadata": "metadata",
        "name": "name",
        "tags": "tags",
    },
)
class CfnAppInstanceBotProps:
    def __init__(
        self,
        *,
        app_instance_arn: builtins.str,
        configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAppInstanceBot.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        metadata: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAppInstanceBot``.

        :param app_instance_arn: The ARN of the AppInstance.
        :param configuration: A structure that contains configuration data.
        :param metadata: The metadata of the AppInstanceBot.
        :param name: The name of the AppInstanceBot.
        :param tags: The tags assigned to the AppInstanceBot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstancebot.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_app_instance_bot_props = chime.CfnAppInstanceBotProps(
                app_instance_arn="appInstanceArn",
                configuration=chime.CfnAppInstanceBot.ConfigurationProperty(
                    lex=chime.CfnAppInstanceBot.LexConfigurationProperty(
                        lex_bot_alias_arn="lexBotAliasArn",
                        locale_id="localeId",
            
                        # the properties below are optional
                        invoked_by=chime.CfnAppInstanceBot.InvokedByProperty(
                            standard_messages="standardMessages",
                            targeted_messages="targetedMessages"
                        ),
                        responds_to="respondsTo",
                        welcome_intent="welcomeIntent"
                    )
                ),
            
                # the properties below are optional
                metadata="metadata",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d900ae3a9eb6a587e47f3e534920839a7bec4e3fc41d625d3e3b8eb9d31d4eae)
            check_type(argname="argument app_instance_arn", value=app_instance_arn, expected_type=type_hints["app_instance_arn"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_instance_arn": app_instance_arn,
            "configuration": configuration,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_instance_arn(self) -> builtins.str:
        '''The ARN of the AppInstance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstancebot.html#cfn-chime-appinstancebot-appinstancearn
        '''
        result = self._values.get("app_instance_arn")
        assert result is not None, "Required property 'app_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.ConfigurationProperty"]:
        '''A structure that contains configuration data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstancebot.html#cfn-chime-appinstancebot-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceBot.ConfigurationProperty"], result)

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''The metadata of the AppInstanceBot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstancebot.html#cfn-chime-appinstancebot-metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AppInstanceBot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstancebot.html#cfn-chime-appinstancebot-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the AppInstanceBot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstancebot.html#cfn-chime-appinstancebot-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppInstanceBotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "metadata": "metadata", "tags": "tags"},
)
class CfnAppInstanceProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        metadata: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAppInstance``.

        :param name: The name of the AppInstance.
        :param metadata: The metadata of the AppInstance. Limited to a 1KB string in UTF-8.
        :param tags: Tags assigned to the AppInstance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstance.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_app_instance_props = chime.CfnAppInstanceProps(
                name="name",
            
                # the properties below are optional
                metadata="metadata",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__551f6928f9d6a158547ebe3a9d4b368b45ad66d983bfb330b063b77c078ca90e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if metadata is not None:
            self._values["metadata"] = metadata
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the AppInstance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstance.html#cfn-chime-appinstance-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''The metadata of the AppInstance.

        Limited to a 1KB string in UTF-8.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstance.html#cfn-chime-appinstance-metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags assigned to the AppInstance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstance.html#cfn-chime-appinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.IAppInstanceUserRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnAppInstanceUser(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceUser",
):
    '''Resource Type definition for AWS::Chime::AppInstanceUser.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstanceuser.html
    :cloudformationResource: AWS::Chime::AppInstanceUser
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_app_instance_user = chime.CfnAppInstanceUser(self, "MyCfnAppInstanceUser",
            app_instance_arn="appInstanceArn",
            app_instance_user_id="appInstanceUserId",
        
            # the properties below are optional
            expiration_settings=chime.CfnAppInstanceUser.ExpirationSettingsProperty(
                expiration_criterion="expirationCriterion",
                expiration_days=123
            ),
            metadata="metadata",
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
        app_instance_arn: builtins.str,
        app_instance_user_id: builtins.str,
        expiration_settings: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAppInstanceUser.ExpirationSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        metadata: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::AppInstanceUser``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_instance_arn: 
        :param app_instance_user_id: 
        :param expiration_settings: 
        :param metadata: 
        :param name: 
        :param tags: 
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2085cb61a0928e322527b02fa835e93ae1473637b82fc400d98124c9f4ea85ef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppInstanceUserProps(
            app_instance_arn=app_instance_arn,
            app_instance_user_id=app_instance_user_id,
            expiration_settings=expiration_settings,
            metadata=metadata,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAppInstanceUser")
    @builtins.classmethod
    def arn_for_app_instance_user(
        cls,
        resource: "_aws_chime_58870695.IAppInstanceUserRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__834453efdb4b627060834867c4d4be14cef2b1616cd26510f95ad19700c58e71)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAppInstanceUser", [resource]))

    @jsii.member(jsii_name="isCfnAppInstanceUser")
    @builtins.classmethod
    def is_cfn_app_instance_user(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAppInstanceUser.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b8249e724ed1b8ced6af4d14e2e058e7d87c556d2f34822d2c13ef2eae05db6f)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAppInstanceUser", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__863252a597952f489269b67d81cb8b94673d4899994aee030ef3ab18f84474cf)
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
            type_hints = cached_type_hints(_typecheckingstub__2319035bf7a04fca46bccb72f782d57c44957ca4561f7cd63c521a103cb24570)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="appInstanceUserRef")
    def app_instance_user_ref(self) -> "_aws_chime_58870695.AppInstanceUserReference":
        '''A reference to a AppInstanceUser resource.'''
        return typing.cast("_aws_chime_58870695.AppInstanceUserReference", jsii.get(self, "appInstanceUserRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAppInstanceUserArn")
    def attr_app_instance_user_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AppInstanceUserArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppInstanceUserArn"))

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
    @jsii.member(jsii_name="appInstanceArn")
    def app_instance_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appInstanceArn"))

    @app_instance_arn.setter
    def app_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b20a22b966f7df8751e06019df44b290ea5ac0f00632c5f0800d1ac32bc198eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appInstanceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="appInstanceUserId")
    def app_instance_user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appInstanceUserId"))

    @app_instance_user_id.setter
    def app_instance_user_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cfdd12ef0fd7a56e531e08fb8f66900a90956c52b40bad7b1a5bc196cc3b9f45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appInstanceUserId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expirationSettings")
    def expiration_settings(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceUser.ExpirationSettingsProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceUser.ExpirationSettingsProperty"]], jsii.get(self, "expirationSettings"))

    @expiration_settings.setter
    def expiration_settings(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceUser.ExpirationSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__11df1f0a14380b6e64d70d38f2d2279aa0cad03492a1c3ea2c336851c1379cd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationSettings", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__503686b1a9877ef8aef136c790c2be6a495abcde2081aa874974aba213155b4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__94ed3eda3e56547fc67748fa6d649fea23db4fd56781e44025b0e46a5857c8a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9051ba4c8c7a02ae24d26117b6b0c144f5b530848f9f9411655d4461d5883b41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceUser.ExpirationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expiration_criterion": "expirationCriterion",
            "expiration_days": "expirationDays",
        },
    )
    class ExpirationSettingsProperty:
        def __init__(
            self,
            *,
            expiration_criterion: builtins.str,
            expiration_days: jsii.Number,
        ) -> None:
            '''
            :param expiration_criterion: 
            :param expiration_days: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstanceuser-expirationsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                expiration_settings_property = chime.CfnAppInstanceUser.ExpirationSettingsProperty(
                    expiration_criterion="expirationCriterion",
                    expiration_days=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e650d9ca25019153fe4e2391b149c6b4c2a2336449a5886a3b94f66bf8ccb812)
                check_type(argname="argument expiration_criterion", value=expiration_criterion, expected_type=type_hints["expiration_criterion"])
                check_type(argname="argument expiration_days", value=expiration_days, expected_type=type_hints["expiration_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expiration_criterion": expiration_criterion,
                "expiration_days": expiration_days,
            }

        @builtins.property
        def expiration_criterion(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstanceuser-expirationsettings.html#cfn-chime-appinstanceuser-expirationsettings-expirationcriterion
            '''
            result = self._values.get("expiration_criterion")
            assert result is not None, "Required property 'expiration_criterion' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def expiration_days(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-appinstanceuser-expirationsettings.html#cfn-chime-appinstanceuser-expirationsettings-expirationdays
            '''
            result = self._values.get("expiration_days")
            assert result is not None, "Required property 'expiration_days' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExpirationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnAppInstanceUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_instance_arn": "appInstanceArn",
        "app_instance_user_id": "appInstanceUserId",
        "expiration_settings": "expirationSettings",
        "metadata": "metadata",
        "name": "name",
        "tags": "tags",
    },
)
class CfnAppInstanceUserProps:
    def __init__(
        self,
        *,
        app_instance_arn: builtins.str,
        app_instance_user_id: builtins.str,
        expiration_settings: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnAppInstanceUser.ExpirationSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        metadata: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAppInstanceUser``.

        :param app_instance_arn: 
        :param app_instance_user_id: 
        :param expiration_settings: 
        :param metadata: 
        :param name: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstanceuser.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_app_instance_user_props = chime.CfnAppInstanceUserProps(
                app_instance_arn="appInstanceArn",
                app_instance_user_id="appInstanceUserId",
            
                # the properties below are optional
                expiration_settings=chime.CfnAppInstanceUser.ExpirationSettingsProperty(
                    expiration_criterion="expirationCriterion",
                    expiration_days=123
                ),
                metadata="metadata",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c191e7d70c48f14aeb5305a9541ebc0cb899fc4cc9efe9e64a380ae2098e7b6e)
            check_type(argname="argument app_instance_arn", value=app_instance_arn, expected_type=type_hints["app_instance_arn"])
            check_type(argname="argument app_instance_user_id", value=app_instance_user_id, expected_type=type_hints["app_instance_user_id"])
            check_type(argname="argument expiration_settings", value=expiration_settings, expected_type=type_hints["expiration_settings"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_instance_arn": app_instance_arn,
            "app_instance_user_id": app_instance_user_id,
        }
        if expiration_settings is not None:
            self._values["expiration_settings"] = expiration_settings
        if metadata is not None:
            self._values["metadata"] = metadata
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_instance_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstanceuser.html#cfn-chime-appinstanceuser-appinstancearn
        '''
        result = self._values.get("app_instance_arn")
        assert result is not None, "Required property 'app_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_instance_user_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstanceuser.html#cfn-chime-appinstanceuser-appinstanceuserid
        '''
        result = self._values.get("app_instance_user_id")
        assert result is not None, "Required property 'app_instance_user_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expiration_settings(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceUser.ExpirationSettingsProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstanceuser.html#cfn-chime-appinstanceuser-expirationsettings
        '''
        result = self._values.get("expiration_settings")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnAppInstanceUser.ExpirationSettingsProperty"]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstanceuser.html#cfn-chime-appinstanceuser-metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstanceuser.html#cfn-chime-appinstanceuser-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-appinstanceuser.html#cfn-chime-appinstanceuser-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppInstanceUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.IChannelRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnChannel(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnChannel",
):
    '''Creates a channel in an Amazon Chime SDK Messaging AppInstance.

    Members of a channel exchange messages within it. Every channel operation is performed on behalf of an AppInstanceUser or AppInstanceBot, whose ARN is supplied as ChimeBearer and forms part of the channel's CloudFormation identifier.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html
    :cloudformationResource: AWS::Chime::Channel
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_channel = chime.CfnChannel(self, "MyCfnChannel",
            app_instance_arn="appInstanceArn",
            chime_bearer="chimeBearer",
            name="name",
        
            # the properties below are optional
            channel_id="channelId",
            elastic_channel_configuration=chime.CfnChannel.ElasticChannelConfigurationProperty(
                maximum_sub_channels=123,
                minimum_membership_percentage=123,
                target_memberships_per_sub_channel=123
            ),
            expiration_settings=chime.CfnChannel.ExpirationSettingsProperty(
                expiration_criterion="expirationCriterion",
                expiration_days=123
            ),
            member_arns=["memberArns"],
            metadata="metadata",
            mode="mode",
            moderator_arns=["moderatorArns"],
            privacy="privacy",
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
        app_instance_arn: builtins.str,
        chime_bearer: builtins.str,
        name: builtins.str,
        channel_id: typing.Optional[builtins.str] = None,
        elastic_channel_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.ElasticChannelConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        expiration_settings: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.ExpirationSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        member_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        metadata: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        moderator_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        privacy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::Channel``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_instance_arn: The ARN of the AppInstance that contains the channel.
        :param chime_bearer: The ARN of the AppInstanceUser or AppInstanceBot that performs every operation on this channel. Whichever of the two creates a channel automatically becomes one of its moderators, so the same ARN can subsequently read, update and delete the channel.
        :param name: The name of the channel.
        :param channel_id: The ID of the channel. When omitted, the service generates a UUID.
        :param elastic_channel_configuration: The attributes required to configure and create an elastic channel. An elastic channel must use RESTRICTED mode, cannot be created with MemberArns, and is available only in some regions.
        :param expiration_settings: Settings that control the interval after which the channel is automatically deleted.
        :param member_arns: The ARNs of the AppInstanceUsers to add to the channel as members when it is created. Cannot be combined with ElasticChannelConfiguration.
        :param metadata: The metadata of the channel.
        :param mode: The channel mode. In an UNRESTRICTED channel, members can add themselves and other members; in a RESTRICTED channel, only administrators and moderators can add members. An elastic channel must be RESTRICTED.
        :param moderator_arns: The ARNs of the AppInstanceUsers to add to the channel as moderators when it is created.
        :param privacy: The channel's privacy level. A PUBLIC channel is discoverable by anyone in the AppInstance; a PRIVATE channel is not. Privacy cannot be changed after creation.
        :param tags: The tags for the channel.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a89763003c5889154da844ca3dad921cfa98c23c362a40a05e69b7812336097d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelProps(
            app_instance_arn=app_instance_arn,
            chime_bearer=chime_bearer,
            name=name,
            channel_id=channel_id,
            elastic_channel_configuration=elastic_channel_configuration,
            expiration_settings=expiration_settings,
            member_arns=member_arns,
            metadata=metadata,
            mode=mode,
            moderator_arns=moderator_arns,
            privacy=privacy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForChannel")
    @builtins.classmethod
    def arn_for_channel(
        cls,
        resource: "_aws_chime_58870695.IChannelRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c427c0278e1c98cd454086845e50069da70f9022ed5cdd80f053334831c2cbb7)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForChannel", [resource]))

    @jsii.member(jsii_name="isCfnChannel")
    @builtins.classmethod
    def is_cfn_channel(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnChannel.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aa4790ed4f040aa7c08ce37d765a2efe53b80721c32fd5b1bbda12dc3ae91a05)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnChannel", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__56cb1e61db1c45729b964df35b81c00ecbadeb1e6841d345c0dfdce81520f8f3)
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
            type_hints = cached_type_hints(_typecheckingstub__fe58cc1b62badb3a367bdac675a7be40061ccddeb1291043e6a89f46b1941a0b)
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
        '''The ARN of the channel.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrChannelFlowArn")
    def attr_channel_flow_arn(self) -> builtins.str:
        '''The ARN of the channel flow.

        :cloudformationAttribute: ChannelFlowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrChannelFlowArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''The AppInstanceUser or AppInstanceBot that created the channel.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The time at which the channel was created.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLastMessageTimestamp")
    def attr_last_message_timestamp(self) -> builtins.str:
        '''The time at which a member sent the last message in the channel.

        :cloudformationAttribute: LastMessageTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastMessageTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTimestamp")
    def attr_last_updated_timestamp(self) -> builtins.str:
        '''The time at which the channel was last updated.

        :cloudformationAttribute: LastUpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTimestamp"))

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
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "_aws_chime_58870695.ChannelReference":
        '''A reference to a Channel resource.'''
        return typing.cast("_aws_chime_58870695.ChannelReference", jsii.get(self, "channelRef"))

    @builtins.property
    @jsii.member(jsii_name="appInstanceArn")
    def app_instance_arn(self) -> builtins.str:
        '''The ARN of the AppInstance that contains the channel.'''
        return typing.cast(builtins.str, jsii.get(self, "appInstanceArn"))

    @app_instance_arn.setter
    def app_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e8f59d56a9dbf4b3806ff1912cf07850ffda9a4e9b55db675fece72d4dd31b0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appInstanceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="chimeBearer")
    def chime_bearer(self) -> builtins.str:
        '''The ARN of the AppInstanceUser or AppInstanceBot that performs every operation on this channel.'''
        return typing.cast(builtins.str, jsii.get(self, "chimeBearer"))

    @chime_bearer.setter
    def chime_bearer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8fd04eb030be5b81f943a19c35fdeaa7124f05290326272628749488abfbd429)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "chimeBearer", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the channel.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4d4a11111ed722fa1552e5357156422c544c2a4dd446be1ea345c98978081526)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="channelId")
    def channel_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelId"))

    @channel_id.setter
    def channel_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2899b697a3d0599c4e86d02b714e86b25a73faa81d81b0b5a8a2b846f90a193d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticChannelConfiguration")
    def elastic_channel_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ElasticChannelConfigurationProperty"]]:
        '''The attributes required to configure and create an elastic channel.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ElasticChannelConfigurationProperty"]], jsii.get(self, "elasticChannelConfiguration"))

    @elastic_channel_configuration.setter
    def elastic_channel_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ElasticChannelConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__702d50233a97086fe25c17623249cdf79a35a98fd0c2ff24fc4c4ff212b8c90d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticChannelConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expirationSettings")
    def expiration_settings(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ExpirationSettingsProperty"]]:
        '''Settings that control the interval after which the channel is automatically deleted.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ExpirationSettingsProperty"]], jsii.get(self, "expirationSettings"))

    @expiration_settings.setter
    def expiration_settings(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ExpirationSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cfa4426ad9d68b9d95e87acf17bd96807ddb690c4339e557b335d54201155053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationSettings", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memberArns")
    def member_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the AppInstanceUsers to add to the channel as members when it is created.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "memberArns"))

    @member_arns.setter
    def member_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7d78aaa655e8d98ed189cc1db70ccbc99177cf80d3892ff11d41097adfbd6764)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[builtins.str]:
        '''The metadata of the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d047bb8ce80e19c537d247457b6cc43cd31f25981080e85979a87b0c6d44eea3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> typing.Optional[builtins.str]:
        '''The channel mode.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__826ffe751bf3da6b2ef69e117e86116849fa30257fc6a0ba2d55e0eee456d8cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="moderatorArns")
    def moderator_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the AppInstanceUsers to add to the channel as moderators when it is created.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "moderatorArns"))

    @moderator_arns.setter
    def moderator_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7931948e641c85a29c91dc0f18a05368cce4d97845b3fe14bc39e397032efb1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "moderatorArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privacy")
    def privacy(self) -> typing.Optional[builtins.str]:
        '''The channel's privacy level.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privacy"))

    @privacy.setter
    def privacy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c1ef91b405bc43229f3ad9bb756d161a4b0db50cfd4360ae21ef7c55c52f5944)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privacy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the channel.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__22aa1755f5052e591b4cabb4cbc7f1e285d37bd5839a3720256c387127f5aeb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnChannel.ElasticChannelConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maximum_sub_channels": "maximumSubChannels",
            "minimum_membership_percentage": "minimumMembershipPercentage",
            "target_memberships_per_sub_channel": "targetMembershipsPerSubChannel",
        },
    )
    class ElasticChannelConfigurationProperty:
        def __init__(
            self,
            *,
            maximum_sub_channels: jsii.Number,
            minimum_membership_percentage: jsii.Number,
            target_memberships_per_sub_channel: jsii.Number,
        ) -> None:
            '''The attributes required to configure and create an elastic channel.

            An elastic channel must use RESTRICTED mode, cannot be created with MemberArns, and is available only in some regions.

            :param maximum_sub_channels: The maximum number of SubChannels allowed in the elastic channel.
            :param minimum_membership_percentage: The minimum allowed percentage of TargetMembershipsPerSubChannel users, used to balance members across SubChannels.
            :param target_memberships_per_sub_channel: The maximum number of members allowed in a SubChannel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-elasticchannelconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                elastic_channel_configuration_property = chime.CfnChannel.ElasticChannelConfigurationProperty(
                    maximum_sub_channels=123,
                    minimum_membership_percentage=123,
                    target_memberships_per_sub_channel=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__86e0f478c14d309a5588841538b8043223e8385c82a42bfb60c7a2bdb9d77a9a)
                check_type(argname="argument maximum_sub_channels", value=maximum_sub_channels, expected_type=type_hints["maximum_sub_channels"])
                check_type(argname="argument minimum_membership_percentage", value=minimum_membership_percentage, expected_type=type_hints["minimum_membership_percentage"])
                check_type(argname="argument target_memberships_per_sub_channel", value=target_memberships_per_sub_channel, expected_type=type_hints["target_memberships_per_sub_channel"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "maximum_sub_channels": maximum_sub_channels,
                "minimum_membership_percentage": minimum_membership_percentage,
                "target_memberships_per_sub_channel": target_memberships_per_sub_channel,
            }

        @builtins.property
        def maximum_sub_channels(self) -> jsii.Number:
            '''The maximum number of SubChannels allowed in the elastic channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-elasticchannelconfiguration.html#cfn-chime-channel-elasticchannelconfiguration-maximumsubchannels
            '''
            result = self._values.get("maximum_sub_channels")
            assert result is not None, "Required property 'maximum_sub_channels' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def minimum_membership_percentage(self) -> jsii.Number:
            '''The minimum allowed percentage of TargetMembershipsPerSubChannel users, used to balance members across SubChannels.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-elasticchannelconfiguration.html#cfn-chime-channel-elasticchannelconfiguration-minimummembershippercentage
            '''
            result = self._values.get("minimum_membership_percentage")
            assert result is not None, "Required property 'minimum_membership_percentage' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def target_memberships_per_sub_channel(self) -> jsii.Number:
            '''The maximum number of members allowed in a SubChannel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-elasticchannelconfiguration.html#cfn-chime-channel-elasticchannelconfiguration-targetmembershipspersubchannel
            '''
            result = self._values.get("target_memberships_per_sub_channel")
            assert result is not None, "Required property 'target_memberships_per_sub_channel' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticChannelConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnChannel.ExpirationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expiration_criterion": "expirationCriterion",
            "expiration_days": "expirationDays",
        },
    )
    class ExpirationSettingsProperty:
        def __init__(
            self,
            *,
            expiration_criterion: builtins.str,
            expiration_days: jsii.Number,
        ) -> None:
            '''Settings that control the interval after which the channel is automatically deleted.

            :param expiration_criterion: The condition the expiration period is measured from.
            :param expiration_days: The period in days after which the system automatically deletes the channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-expirationsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                expiration_settings_property = chime.CfnChannel.ExpirationSettingsProperty(
                    expiration_criterion="expirationCriterion",
                    expiration_days=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__61fc7651b450f23570f29d1017ecab7caa5c391d1b674257b21ed9b83c1c68f6)
                check_type(argname="argument expiration_criterion", value=expiration_criterion, expected_type=type_hints["expiration_criterion"])
                check_type(argname="argument expiration_days", value=expiration_days, expected_type=type_hints["expiration_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expiration_criterion": expiration_criterion,
                "expiration_days": expiration_days,
            }

        @builtins.property
        def expiration_criterion(self) -> builtins.str:
            '''The condition the expiration period is measured from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-expirationsettings.html#cfn-chime-channel-expirationsettings-expirationcriterion
            '''
            result = self._values.get("expiration_criterion")
            assert result is not None, "Required property 'expiration_criterion' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def expiration_days(self) -> jsii.Number:
            '''The period in days after which the system automatically deletes the channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-expirationsettings.html#cfn-chime-channel-expirationsettings-expirationdays
            '''
            result = self._values.get("expiration_days")
            assert result is not None, "Required property 'expiration_days' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExpirationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnChannel.IdentityProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "name": "name"},
    )
    class IdentityProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The AppInstanceUser or AppInstanceBot that created the channel.

            :param arn: The ARN in an identity.
            :param name: The name in an identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-identity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                identity_property = chime.CfnChannel.IdentityProperty(
                    arn="arn",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2bfa5f1d241cfa51cfb94fc2037ee9ab05fc2825441e3b064b5c3346d71baebc)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN in an identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-identity.html#cfn-chime-channel-identity-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name in an identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channel-identity.html#cfn-chime-channel-identity-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.IChannelFlowRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnChannelFlow(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnChannelFlow",
):
    '''Creates a channel flow in the Amazon Chime SDK Messaging service.

    A channel flow is a container for processors (Lambda functions) that perform actions on chat messages.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channelflow.html
    :cloudformationResource: AWS::Chime::ChannelFlow
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_channel_flow = chime.CfnChannelFlow(self, "MyCfnChannelFlow",
            app_instance_arn="appInstanceArn",
            name="name",
            processors=[chime.CfnChannelFlow.ProcessorProperty(
                configuration=chime.CfnChannelFlow.ProcessorConfigurationProperty(
                    lambda_=chime.CfnChannelFlow.LambdaConfigurationProperty(
                        invocation_type="invocationType",
                        resource_arn="resourceArn"
                    )
                ),
                execution_order=123,
                fallback_action="fallbackAction",
                name="name"
            )],
        
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
        app_instance_arn: builtins.str,
        name: builtins.str,
        processors: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannelFlow.ProcessorProperty", typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::ChannelFlow``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_instance_arn: The ARN of the app instance.
        :param name: The name of the channel flow.
        :param processors: Information about the processor Lambda functions.
        :param tags: The tags for the channel flow.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__553e37c55476a947075ca59056beea348820f4c9d0001731f2dc6df208e46aac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelFlowProps(
            app_instance_arn=app_instance_arn,
            name=name,
            processors=processors,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForChannelFlow")
    @builtins.classmethod
    def arn_for_channel_flow(
        cls,
        resource: "_aws_chime_58870695.IChannelFlowRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__215e52bbdaf64af19e7a78a4c16ecf1be25619c25b0f1f560edef98f17fd074f)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForChannelFlow", [resource]))

    @jsii.member(jsii_name="isCfnChannelFlow")
    @builtins.classmethod
    def is_cfn_channel_flow(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnChannelFlow.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7cd9c6e628c1ed57d7d45231f8fd40a59294a2cfe8e8086a494a43b0dfbcb348)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnChannelFlow", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__95d931527d027465cc783a90101afd59c6d28ac9549723ed78d381411c1f152c)
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
            type_hints = cached_type_hints(_typecheckingstub__c315bd571cdd659263f798212f27154c2c646ef9c193834f07a863a925933999)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAppInstanceId")
    def attr_app_instance_id(self) -> builtins.str:
        '''The ID of the app instance, extracted from the channel flow ARN.

        :cloudformationAttribute: AppInstanceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppInstanceId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the channel flow.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrChannelFlowId")
    def attr_channel_flow_id(self) -> builtins.str:
        '''The ID of the channel flow, extracted from the channel flow ARN.

        :cloudformationAttribute: ChannelFlowId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrChannelFlowId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The time at which the channel flow was created.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTimestamp")
    def attr_last_updated_timestamp(self) -> builtins.str:
        '''The time at which the channel flow was last updated.

        :cloudformationAttribute: LastUpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTimestamp"))

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
    @jsii.member(jsii_name="channelFlowRef")
    def channel_flow_ref(self) -> "_aws_chime_58870695.ChannelFlowReference":
        '''A reference to a ChannelFlow resource.'''
        return typing.cast("_aws_chime_58870695.ChannelFlowReference", jsii.get(self, "channelFlowRef"))

    @builtins.property
    @jsii.member(jsii_name="appInstanceArn")
    def app_instance_arn(self) -> builtins.str:
        '''The ARN of the app instance.'''
        return typing.cast(builtins.str, jsii.get(self, "appInstanceArn"))

    @app_instance_arn.setter
    def app_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2952f13ac0bef71a3fce903cbe1c25737bd7625917778a93a03dac2015fa2104)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appInstanceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the channel flow.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__411cc8fb86020950b5c9e5844fb80dccb3d2c00b763b9ab9a8f9b5cc719d9451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.ProcessorProperty"]]]:
        '''Information about the processor Lambda functions.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.ProcessorProperty"]]], jsii.get(self, "processors"))

    @processors.setter
    def processors(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.ProcessorProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__87728ae9e5da9fcebfef150b2b1326c7b3106255781f7f53de411ad39a29a508)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "processors", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the channel flow.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__56a722312beda48b0dba71e0a7247be1089c7db33dfb3f22b8eb02c0cea9adc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnChannelFlow.LambdaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "invocation_type": "invocationType",
            "resource_arn": "resourceArn",
        },
    )
    class LambdaConfigurationProperty:
        def __init__(
            self,
            *,
            invocation_type: builtins.str,
            resource_arn: builtins.str,
        ) -> None:
            '''Stores metadata about a Lambda processor.

            :param invocation_type: Controls how the Lambda function is invoked.
            :param resource_arn: The ARN of the Lambda message processing function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-lambdaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                lambda_configuration_property = chime.CfnChannelFlow.LambdaConfigurationProperty(
                    invocation_type="invocationType",
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__285ed0bc098587d57e9f94632c1cb3c1c76fff652d29fd8997a47c3b2cc1cc09)
                check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "invocation_type": invocation_type,
                "resource_arn": resource_arn,
            }

        @builtins.property
        def invocation_type(self) -> builtins.str:
            '''Controls how the Lambda function is invoked.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-lambdaconfiguration.html#cfn-chime-channelflow-lambdaconfiguration-invocationtype
            '''
            result = self._values.get("invocation_type")
            assert result is not None, "Required property 'invocation_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the Lambda message processing function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-lambdaconfiguration.html#cfn-chime-channelflow-lambdaconfiguration-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnChannelFlow.ProcessorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_": "lambda"},
    )
    class ProcessorConfigurationProperty:
        def __init__(
            self,
            *,
            lambda_: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannelFlow.LambdaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A processor's metadata.

            :param lambda_: Stores metadata about a Lambda processor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-processorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                processor_configuration_property = chime.CfnChannelFlow.ProcessorConfigurationProperty(
                    lambda_=chime.CfnChannelFlow.LambdaConfigurationProperty(
                        invocation_type="invocationType",
                        resource_arn="resourceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__9fdc1fc093fa01b9277bf2dd738d6f6237e1cce994cac73e6f7d4e62ab99ac5c)
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_": lambda_,
            }

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.LambdaConfigurationProperty"]:
            '''Stores metadata about a Lambda processor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-processorconfiguration.html#cfn-chime-channelflow-processorconfiguration-lambda
            '''
            result = self._values.get("lambda_")
            assert result is not None, "Required property 'lambda_' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.LambdaConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnChannelFlow.ProcessorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration": "configuration",
            "execution_order": "executionOrder",
            "fallback_action": "fallbackAction",
            "name": "name",
        },
    )
    class ProcessorProperty:
        def __init__(
            self,
            *,
            configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannelFlow.ProcessorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            execution_order: jsii.Number,
            fallback_action: builtins.str,
            name: builtins.str,
        ) -> None:
            '''Information about a processor in a channel flow.

            :param configuration: A processor's metadata.
            :param execution_order: The sequence in which processors run.
            :param fallback_action: Determines whether to continue or stop processing when communication with a processor fails.
            :param name: The name of the processor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-processor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                processor_property = chime.CfnChannelFlow.ProcessorProperty(
                    configuration=chime.CfnChannelFlow.ProcessorConfigurationProperty(
                        lambda_=chime.CfnChannelFlow.LambdaConfigurationProperty(
                            invocation_type="invocationType",
                            resource_arn="resourceArn"
                        )
                    ),
                    execution_order=123,
                    fallback_action="fallbackAction",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__be4dcd983ce00e19de1c1ec7124b3517157f895d6121f59f1ca204a7a59f7fc1)
                check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
                check_type(argname="argument execution_order", value=execution_order, expected_type=type_hints["execution_order"])
                check_type(argname="argument fallback_action", value=fallback_action, expected_type=type_hints["fallback_action"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration": configuration,
                "execution_order": execution_order,
                "fallback_action": fallback_action,
                "name": name,
            }

        @builtins.property
        def configuration(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.ProcessorConfigurationProperty"]:
            '''A processor's metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-processor.html#cfn-chime-channelflow-processor-configuration
            '''
            result = self._values.get("configuration")
            assert result is not None, "Required property 'configuration' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.ProcessorConfigurationProperty"], result)

        @builtins.property
        def execution_order(self) -> jsii.Number:
            '''The sequence in which processors run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-processor.html#cfn-chime-channelflow-processor-executionorder
            '''
            result = self._values.get("execution_order")
            assert result is not None, "Required property 'execution_order' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def fallback_action(self) -> builtins.str:
            '''Determines whether to continue or stop processing when communication with a processor fails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-processor.html#cfn-chime-channelflow-processor-fallbackaction
            '''
            result = self._values.get("fallback_action")
            assert result is not None, "Required property 'fallback_action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the processor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-channelflow-processor.html#cfn-chime-channelflow-processor-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnChannelFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_instance_arn": "appInstanceArn",
        "name": "name",
        "processors": "processors",
        "tags": "tags",
    },
)
class CfnChannelFlowProps:
    def __init__(
        self,
        *,
        app_instance_arn: builtins.str,
        name: builtins.str,
        processors: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannelFlow.ProcessorProperty", typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannelFlow``.

        :param app_instance_arn: The ARN of the app instance.
        :param name: The name of the channel flow.
        :param processors: Information about the processor Lambda functions.
        :param tags: The tags for the channel flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channelflow.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_channel_flow_props = chime.CfnChannelFlowProps(
                app_instance_arn="appInstanceArn",
                name="name",
                processors=[chime.CfnChannelFlow.ProcessorProperty(
                    configuration=chime.CfnChannelFlow.ProcessorConfigurationProperty(
                        lambda_=chime.CfnChannelFlow.LambdaConfigurationProperty(
                            invocation_type="invocationType",
                            resource_arn="resourceArn"
                        )
                    ),
                    execution_order=123,
                    fallback_action="fallbackAction",
                    name="name"
                )],
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__04fab589c36890507658f03e0daf5dda656b997e99d4f0f5d449cfb4324279d2)
            check_type(argname="argument app_instance_arn", value=app_instance_arn, expected_type=type_hints["app_instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_instance_arn": app_instance_arn,
            "name": name,
            "processors": processors,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_instance_arn(self) -> builtins.str:
        '''The ARN of the app instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channelflow.html#cfn-chime-channelflow-appinstancearn
        '''
        result = self._values.get("app_instance_arn")
        assert result is not None, "Required property 'app_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the channel flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channelflow.html#cfn-chime-channelflow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.ProcessorProperty"]]]:
        '''Information about the processor Lambda functions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channelflow.html#cfn-chime-channelflow-processors
        '''
        result = self._values.get("processors")
        assert result is not None, "Required property 'processors' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannelFlow.ProcessorProperty"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the channel flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channelflow.html#cfn-chime-channelflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_instance_arn": "appInstanceArn",
        "chime_bearer": "chimeBearer",
        "name": "name",
        "channel_id": "channelId",
        "elastic_channel_configuration": "elasticChannelConfiguration",
        "expiration_settings": "expirationSettings",
        "member_arns": "memberArns",
        "metadata": "metadata",
        "mode": "mode",
        "moderator_arns": "moderatorArns",
        "privacy": "privacy",
        "tags": "tags",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        app_instance_arn: builtins.str,
        chime_bearer: builtins.str,
        name: builtins.str,
        channel_id: typing.Optional[builtins.str] = None,
        elastic_channel_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.ElasticChannelConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        expiration_settings: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.ExpirationSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        member_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        metadata: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        moderator_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        privacy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannel``.

        :param app_instance_arn: The ARN of the AppInstance that contains the channel.
        :param chime_bearer: The ARN of the AppInstanceUser or AppInstanceBot that performs every operation on this channel. Whichever of the two creates a channel automatically becomes one of its moderators, so the same ARN can subsequently read, update and delete the channel.
        :param name: The name of the channel.
        :param channel_id: The ID of the channel. When omitted, the service generates a UUID.
        :param elastic_channel_configuration: The attributes required to configure and create an elastic channel. An elastic channel must use RESTRICTED mode, cannot be created with MemberArns, and is available only in some regions.
        :param expiration_settings: Settings that control the interval after which the channel is automatically deleted.
        :param member_arns: The ARNs of the AppInstanceUsers to add to the channel as members when it is created. Cannot be combined with ElasticChannelConfiguration.
        :param metadata: The metadata of the channel.
        :param mode: The channel mode. In an UNRESTRICTED channel, members can add themselves and other members; in a RESTRICTED channel, only administrators and moderators can add members. An elastic channel must be RESTRICTED.
        :param moderator_arns: The ARNs of the AppInstanceUsers to add to the channel as moderators when it is created.
        :param privacy: The channel's privacy level. A PUBLIC channel is discoverable by anyone in the AppInstance; a PRIVATE channel is not. Privacy cannot be changed after creation.
        :param tags: The tags for the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_channel_props = chime.CfnChannelProps(
                app_instance_arn="appInstanceArn",
                chime_bearer="chimeBearer",
                name="name",
            
                # the properties below are optional
                channel_id="channelId",
                elastic_channel_configuration=chime.CfnChannel.ElasticChannelConfigurationProperty(
                    maximum_sub_channels=123,
                    minimum_membership_percentage=123,
                    target_memberships_per_sub_channel=123
                ),
                expiration_settings=chime.CfnChannel.ExpirationSettingsProperty(
                    expiration_criterion="expirationCriterion",
                    expiration_days=123
                ),
                member_arns=["memberArns"],
                metadata="metadata",
                mode="mode",
                moderator_arns=["moderatorArns"],
                privacy="privacy",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1f68927a594352d4dfb82e54610caae5c2c52baa2dcf7cbb196f93b31a786fed)
            check_type(argname="argument app_instance_arn", value=app_instance_arn, expected_type=type_hints["app_instance_arn"])
            check_type(argname="argument chime_bearer", value=chime_bearer, expected_type=type_hints["chime_bearer"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
            check_type(argname="argument elastic_channel_configuration", value=elastic_channel_configuration, expected_type=type_hints["elastic_channel_configuration"])
            check_type(argname="argument expiration_settings", value=expiration_settings, expected_type=type_hints["expiration_settings"])
            check_type(argname="argument member_arns", value=member_arns, expected_type=type_hints["member_arns"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument moderator_arns", value=moderator_arns, expected_type=type_hints["moderator_arns"])
            check_type(argname="argument privacy", value=privacy, expected_type=type_hints["privacy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_instance_arn": app_instance_arn,
            "chime_bearer": chime_bearer,
            "name": name,
        }
        if channel_id is not None:
            self._values["channel_id"] = channel_id
        if elastic_channel_configuration is not None:
            self._values["elastic_channel_configuration"] = elastic_channel_configuration
        if expiration_settings is not None:
            self._values["expiration_settings"] = expiration_settings
        if member_arns is not None:
            self._values["member_arns"] = member_arns
        if metadata is not None:
            self._values["metadata"] = metadata
        if mode is not None:
            self._values["mode"] = mode
        if moderator_arns is not None:
            self._values["moderator_arns"] = moderator_arns
        if privacy is not None:
            self._values["privacy"] = privacy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_instance_arn(self) -> builtins.str:
        '''The ARN of the AppInstance that contains the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-appinstancearn
        '''
        result = self._values.get("app_instance_arn")
        assert result is not None, "Required property 'app_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def chime_bearer(self) -> builtins.str:
        '''The ARN of the AppInstanceUser or AppInstanceBot that performs every operation on this channel.

        Whichever of the two creates a channel automatically becomes one of its moderators, so the same ARN can subsequently read, update and delete the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-chimebearer
        '''
        result = self._values.get("chime_bearer")
        assert result is not None, "Required property 'chime_bearer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the channel.

        When omitted, the service generates a UUID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-channelid
        '''
        result = self._values.get("channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elastic_channel_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ElasticChannelConfigurationProperty"]]:
        '''The attributes required to configure and create an elastic channel.

        An elastic channel must use RESTRICTED mode, cannot be created with MemberArns, and is available only in some regions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-elasticchannelconfiguration
        '''
        result = self._values.get("elastic_channel_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ElasticChannelConfigurationProperty"]], result)

    @builtins.property
    def expiration_settings(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ExpirationSettingsProperty"]]:
        '''Settings that control the interval after which the channel is automatically deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-expirationsettings
        '''
        result = self._values.get("expiration_settings")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.ExpirationSettingsProperty"]], result)

    @builtins.property
    def member_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the AppInstanceUsers to add to the channel as members when it is created.

        Cannot be combined with ElasticChannelConfiguration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-memberarns
        '''
        result = self._values.get("member_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''The metadata of the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''The channel mode.

        In an UNRESTRICTED channel, members can add themselves and other members; in a RESTRICTED channel, only administrators and moderators can add members. An elastic channel must be RESTRICTED.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def moderator_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the AppInstanceUsers to add to the channel as moderators when it is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-moderatorarns
        '''
        result = self._values.get("moderator_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def privacy(self) -> typing.Optional[builtins.str]:
        '''The channel's privacy level.

        A PUBLIC channel is discoverable by anyone in the AppInstance; a PRIVATE channel is not. Privacy cannot be changed after creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-privacy
        '''
        result = self._values.get("privacy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-channel.html#cfn-chime-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.IMediaInsightsPipelineConfigurationRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnMediaInsightsPipelineConfiguration(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration",
):
    '''Resource Type definition for an Amazon Chime SDK Media Insights Pipeline Configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediainsightspipelineconfiguration.html
    :cloudformationResource: AWS::Chime::MediaInsightsPipelineConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_media_insights_pipeline_configuration = chime.CfnMediaInsightsPipelineConfiguration(self, "MyCfnMediaInsightsPipelineConfiguration",
            elements=[chime.CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty(
                type="type",
        
                # the properties below are optional
                amazon_transcribe_call_analytics_processor_configuration=chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty(
                    language_code="languageCode",
        
                    # the properties below are optional
                    call_analytics_stream_categories=["callAnalyticsStreamCategories"],
                    content_identification_type="contentIdentificationType",
                    content_redaction_type="contentRedactionType",
                    enable_partial_results_stabilization=False,
                    filter_partial_results=False,
                    language_model_name="languageModelName",
                    partial_results_stability="partialResultsStability",
                    pii_entity_types="piiEntityTypes",
                    post_call_analytics_settings=chime.CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty(
                        data_access_role_arn="dataAccessRoleArn",
                        output_location="outputLocation",
        
                        # the properties below are optional
                        content_redaction_output="contentRedactionOutput",
                        output_encryption_kms_key_id="outputEncryptionKmsKeyId"
                    ),
                    vocabulary_filter_method="vocabularyFilterMethod",
                    vocabulary_filter_name="vocabularyFilterName",
                    vocabulary_name="vocabularyName"
                ),
                amazon_transcribe_processor_configuration=chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty(
                    content_identification_type="contentIdentificationType",
                    content_redaction_type="contentRedactionType",
                    enable_partial_results_stabilization=False,
                    filter_partial_results=False,
                    identify_language=False,
                    identify_multiple_languages=False,
                    language_code="languageCode",
                    language_model_name="languageModelName",
                    language_options="languageOptions",
                    partial_results_stability="partialResultsStability",
                    pii_entity_types="piiEntityTypes",
                    preferred_language="preferredLanguage",
                    show_speaker_label=False,
                    vocabulary_filter_method="vocabularyFilterMethod",
                    vocabulary_filter_name="vocabularyFilterName",
                    vocabulary_filter_names="vocabularyFilterNames",
                    vocabulary_name="vocabularyName",
                    vocabulary_names="vocabularyNames"
                ),
                kinesis_data_stream_sink_configuration=chime.CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty(
                    insights_target="insightsTarget"
                ),
                s3_recording_sink_configuration=chime.CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty(
                    destination="destination",
                    recording_file_format="recordingFileFormat"
                )
            )],
            media_insights_pipeline_configuration_name="mediaInsightsPipelineConfigurationName",
            resource_access_role_arn="resourceAccessRoleArn",
        
            # the properties below are optional
            real_time_alert_configuration=chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty(
                disabled=False,
                rules=[chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty(
                    type="type",
        
                    # the properties below are optional
                    issue_detection_configuration=chime.CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty(
                        rule_name="ruleName"
                    ),
                    keyword_match_configuration=chime.CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty(
                        keywords=["keywords"],
                        rule_name="ruleName",
        
                        # the properties below are optional
                        negate=False
                    ),
                    sentiment_configuration=chime.CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty(
                        rule_name="ruleName",
                        sentiment_type="sentimentType",
                        time_period=123
                    )
                )]
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
        elements: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty", typing.Dict[builtins.str, typing.Any]]]]],
        media_insights_pipeline_configuration_name: builtins.str,
        resource_access_role_arn: builtins.str,
        real_time_alert_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::MediaInsightsPipelineConfiguration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param elements: The elements in the configuration.
        :param media_insights_pipeline_configuration_name: The name of the media insights pipeline configuration.
        :param resource_access_role_arn: The ARN of the role used by the service to access Amazon Web Services resources.
        :param real_time_alert_configuration: 
        :param tags: The tags associated with the configuration.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__889d6d992b8d7ecaa497b89b0969fdfa7fa839fcacf07f58726b49cf8f323d52)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMediaInsightsPipelineConfigurationProps(
            elements=elements,
            media_insights_pipeline_configuration_name=media_insights_pipeline_configuration_name,
            resource_access_role_arn=resource_access_role_arn,
            real_time_alert_configuration=real_time_alert_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForMediaInsightsPipelineConfiguration")
    @builtins.classmethod
    def arn_for_media_insights_pipeline_configuration(
        cls,
        resource: "_aws_chime_58870695.IMediaInsightsPipelineConfigurationRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d947022873d1e6882ae47a189d20b3d7f2aa53c157b7df911c6e8deb1b32e31a)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForMediaInsightsPipelineConfiguration", [resource]))

    @jsii.member(jsii_name="isCfnMediaInsightsPipelineConfiguration")
    @builtins.classmethod
    def is_cfn_media_insights_pipeline_configuration(
        cls,
        x: typing.Any,
    ) -> builtins.bool:
        '''Checks whether the given object is a CfnMediaInsightsPipelineConfiguration.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fc4a193dcd334a33221d899407a55bf4c92b7885da28e3b9f57712ac4e0b6bfd)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnMediaInsightsPipelineConfiguration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ffe32f64919fa553c3f22877220b9efb5fbcdcf2ad1ec025355c8a02c6f847c2)
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
            type_hints = cached_type_hints(_typecheckingstub__883a85ed849985e75e040b5f613e64f571f44974766f3824019aee35d3eecdfc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The time at which the configuration was created.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrMediaInsightsPipelineConfigurationArn")
    def attr_media_insights_pipeline_configuration_arn(self) -> builtins.str:
        '''The ARN of the configuration.

        :cloudformationAttribute: MediaInsightsPipelineConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMediaInsightsPipelineConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMediaInsightsPipelineConfigurationId")
    def attr_media_insights_pipeline_configuration_id(self) -> builtins.str:
        '''The unique identifier of the configuration.

        :cloudformationAttribute: MediaInsightsPipelineConfigurationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMediaInsightsPipelineConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''The time at which the configuration was last updated.

        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

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
    @jsii.member(jsii_name="mediaInsightsPipelineConfigurationRef")
    def media_insights_pipeline_configuration_ref(
        self,
    ) -> "_aws_chime_58870695.MediaInsightsPipelineConfigurationReference":
        '''A reference to a MediaInsightsPipelineConfiguration resource.'''
        return typing.cast("_aws_chime_58870695.MediaInsightsPipelineConfigurationReference", jsii.get(self, "mediaInsightsPipelineConfigurationRef"))

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty"]]]:
        '''The elements in the configuration.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty"]]], jsii.get(self, "elements"))

    @elements.setter
    def elements(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2c400f356cf18466a3dff483e35943c01e7e22de89435c0c061ebb9510b901ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elements", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mediaInsightsPipelineConfigurationName")
    def media_insights_pipeline_configuration_name(self) -> builtins.str:
        '''The name of the media insights pipeline configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "mediaInsightsPipelineConfigurationName"))

    @media_insights_pipeline_configuration_name.setter
    def media_insights_pipeline_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__703c89c9d6f653e3380e4187a1fddc6718e6cef2c715047ba16991465db1d4ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaInsightsPipelineConfigurationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceAccessRoleArn")
    def resource_access_role_arn(self) -> builtins.str:
        '''The ARN of the role used by the service to access Amazon Web Services resources.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceAccessRoleArn"))

    @resource_access_role_arn.setter
    def resource_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a5495e3e7636c99bb133b9fe920d64aee710982f4fd245f2c92bb8034ee192b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceAccessRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="realTimeAlertConfiguration")
    def real_time_alert_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty"]], jsii.get(self, "realTimeAlertConfiguration"))

    @real_time_alert_configuration.setter
    def real_time_alert_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a72716e62afe90194547497ab6f884c0ec05d923704b462976f68d92a5a76f2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "realTimeAlertConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags associated with the configuration.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__99fa72bce81eb4333c1c1c86d38e36204aef77b68b24d9f3a58023ffe14e0700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "language_code": "languageCode",
            "call_analytics_stream_categories": "callAnalyticsStreamCategories",
            "content_identification_type": "contentIdentificationType",
            "content_redaction_type": "contentRedactionType",
            "enable_partial_results_stabilization": "enablePartialResultsStabilization",
            "filter_partial_results": "filterPartialResults",
            "language_model_name": "languageModelName",
            "partial_results_stability": "partialResultsStability",
            "pii_entity_types": "piiEntityTypes",
            "post_call_analytics_settings": "postCallAnalyticsSettings",
            "vocabulary_filter_method": "vocabularyFilterMethod",
            "vocabulary_filter_name": "vocabularyFilterName",
            "vocabulary_name": "vocabularyName",
        },
    )
    class AmazonTranscribeCallAnalyticsProcessorConfigurationProperty:
        def __init__(
            self,
            *,
            language_code: builtins.str,
            call_analytics_stream_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
            content_identification_type: typing.Optional[builtins.str] = None,
            content_redaction_type: typing.Optional[builtins.str] = None,
            enable_partial_results_stabilization: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            filter_partial_results: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            language_model_name: typing.Optional[builtins.str] = None,
            partial_results_stability: typing.Optional[builtins.str] = None,
            pii_entity_types: typing.Optional[builtins.str] = None,
            post_call_analytics_settings: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            vocabulary_filter_method: typing.Optional[builtins.str] = None,
            vocabulary_filter_name: typing.Optional[builtins.str] = None,
            vocabulary_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param language_code: The language code in the configuration.
            :param call_analytics_stream_categories: The categories to send to the insights target.
            :param content_identification_type: Labels all PII identified in the transcript.
            :param content_redaction_type: Redacts all PII identified in the transcript.
            :param enable_partial_results_stabilization: Enables partial result stabilization.
            :param filter_partial_results: If true, partial results are filtered out.
            :param language_model_name: The name of the custom language model.
            :param partial_results_stability: The level of stability for partial results.
            :param pii_entity_types: The types of PII to redact.
            :param post_call_analytics_settings: 
            :param vocabulary_filter_method: The vocabulary filtering method.
            :param vocabulary_filter_name: The name of the custom vocabulary filter.
            :param vocabulary_name: The name of the custom vocabulary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                amazon_transcribe_call_analytics_processor_configuration_property = chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty(
                    language_code="languageCode",
                
                    # the properties below are optional
                    call_analytics_stream_categories=["callAnalyticsStreamCategories"],
                    content_identification_type="contentIdentificationType",
                    content_redaction_type="contentRedactionType",
                    enable_partial_results_stabilization=False,
                    filter_partial_results=False,
                    language_model_name="languageModelName",
                    partial_results_stability="partialResultsStability",
                    pii_entity_types="piiEntityTypes",
                    post_call_analytics_settings=chime.CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty(
                        data_access_role_arn="dataAccessRoleArn",
                        output_location="outputLocation",
                
                        # the properties below are optional
                        content_redaction_output="contentRedactionOutput",
                        output_encryption_kms_key_id="outputEncryptionKmsKeyId"
                    ),
                    vocabulary_filter_method="vocabularyFilterMethod",
                    vocabulary_filter_name="vocabularyFilterName",
                    vocabulary_name="vocabularyName"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__afcc5b2f060868f5e44a495cf81d3fbeeebe9d579aabcae3cc02c92e4f318015)
                check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
                check_type(argname="argument call_analytics_stream_categories", value=call_analytics_stream_categories, expected_type=type_hints["call_analytics_stream_categories"])
                check_type(argname="argument content_identification_type", value=content_identification_type, expected_type=type_hints["content_identification_type"])
                check_type(argname="argument content_redaction_type", value=content_redaction_type, expected_type=type_hints["content_redaction_type"])
                check_type(argname="argument enable_partial_results_stabilization", value=enable_partial_results_stabilization, expected_type=type_hints["enable_partial_results_stabilization"])
                check_type(argname="argument filter_partial_results", value=filter_partial_results, expected_type=type_hints["filter_partial_results"])
                check_type(argname="argument language_model_name", value=language_model_name, expected_type=type_hints["language_model_name"])
                check_type(argname="argument partial_results_stability", value=partial_results_stability, expected_type=type_hints["partial_results_stability"])
                check_type(argname="argument pii_entity_types", value=pii_entity_types, expected_type=type_hints["pii_entity_types"])
                check_type(argname="argument post_call_analytics_settings", value=post_call_analytics_settings, expected_type=type_hints["post_call_analytics_settings"])
                check_type(argname="argument vocabulary_filter_method", value=vocabulary_filter_method, expected_type=type_hints["vocabulary_filter_method"])
                check_type(argname="argument vocabulary_filter_name", value=vocabulary_filter_name, expected_type=type_hints["vocabulary_filter_name"])
                check_type(argname="argument vocabulary_name", value=vocabulary_name, expected_type=type_hints["vocabulary_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "language_code": language_code,
            }
            if call_analytics_stream_categories is not None:
                self._values["call_analytics_stream_categories"] = call_analytics_stream_categories
            if content_identification_type is not None:
                self._values["content_identification_type"] = content_identification_type
            if content_redaction_type is not None:
                self._values["content_redaction_type"] = content_redaction_type
            if enable_partial_results_stabilization is not None:
                self._values["enable_partial_results_stabilization"] = enable_partial_results_stabilization
            if filter_partial_results is not None:
                self._values["filter_partial_results"] = filter_partial_results
            if language_model_name is not None:
                self._values["language_model_name"] = language_model_name
            if partial_results_stability is not None:
                self._values["partial_results_stability"] = partial_results_stability
            if pii_entity_types is not None:
                self._values["pii_entity_types"] = pii_entity_types
            if post_call_analytics_settings is not None:
                self._values["post_call_analytics_settings"] = post_call_analytics_settings
            if vocabulary_filter_method is not None:
                self._values["vocabulary_filter_method"] = vocabulary_filter_method
            if vocabulary_filter_name is not None:
                self._values["vocabulary_filter_name"] = vocabulary_filter_name
            if vocabulary_name is not None:
                self._values["vocabulary_name"] = vocabulary_name

        @builtins.property
        def language_code(self) -> builtins.str:
            '''The language code in the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-languagecode
            '''
            result = self._values.get("language_code")
            assert result is not None, "Required property 'language_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def call_analytics_stream_categories(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The categories to send to the insights target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-callanalyticsstreamcategories
            '''
            result = self._values.get("call_analytics_stream_categories")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def content_identification_type(self) -> typing.Optional[builtins.str]:
            '''Labels all PII identified in the transcript.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-contentidentificationtype
            '''
            result = self._values.get("content_identification_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def content_redaction_type(self) -> typing.Optional[builtins.str]:
            '''Redacts all PII identified in the transcript.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-contentredactiontype
            '''
            result = self._values.get("content_redaction_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_partial_results_stabilization(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Enables partial result stabilization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-enablepartialresultsstabilization
            '''
            result = self._values.get("enable_partial_results_stabilization")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def filter_partial_results(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''If true, partial results are filtered out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-filterpartialresults
            '''
            result = self._values.get("filter_partial_results")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def language_model_name(self) -> typing.Optional[builtins.str]:
            '''The name of the custom language model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-languagemodelname
            '''
            result = self._values.get("language_model_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def partial_results_stability(self) -> typing.Optional[builtins.str]:
            '''The level of stability for partial results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-partialresultsstability
            '''
            result = self._values.get("partial_results_stability")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pii_entity_types(self) -> typing.Optional[builtins.str]:
            '''The types of PII to redact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-piientitytypes
            '''
            result = self._values.get("pii_entity_types")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def post_call_analytics_settings(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-postcallanalyticssettings
            '''
            result = self._values.get("post_call_analytics_settings")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty"]], result)

        @builtins.property
        def vocabulary_filter_method(self) -> typing.Optional[builtins.str]:
            '''The vocabulary filtering method.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-vocabularyfiltermethod
            '''
            result = self._values.get("vocabulary_filter_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vocabulary_filter_name(self) -> typing.Optional[builtins.str]:
            '''The name of the custom vocabulary filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-vocabularyfiltername
            '''
            result = self._values.get("vocabulary_filter_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vocabulary_name(self) -> typing.Optional[builtins.str]:
            '''The name of the custom vocabulary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribecallanalyticsprocessorconfiguration-vocabularyname
            '''
            result = self._values.get("vocabulary_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonTranscribeCallAnalyticsProcessorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content_identification_type": "contentIdentificationType",
            "content_redaction_type": "contentRedactionType",
            "enable_partial_results_stabilization": "enablePartialResultsStabilization",
            "filter_partial_results": "filterPartialResults",
            "identify_language": "identifyLanguage",
            "identify_multiple_languages": "identifyMultipleLanguages",
            "language_code": "languageCode",
            "language_model_name": "languageModelName",
            "language_options": "languageOptions",
            "partial_results_stability": "partialResultsStability",
            "pii_entity_types": "piiEntityTypes",
            "preferred_language": "preferredLanguage",
            "show_speaker_label": "showSpeakerLabel",
            "vocabulary_filter_method": "vocabularyFilterMethod",
            "vocabulary_filter_name": "vocabularyFilterName",
            "vocabulary_filter_names": "vocabularyFilterNames",
            "vocabulary_name": "vocabularyName",
            "vocabulary_names": "vocabularyNames",
        },
    )
    class AmazonTranscribeProcessorConfigurationProperty:
        def __init__(
            self,
            *,
            content_identification_type: typing.Optional[builtins.str] = None,
            content_redaction_type: typing.Optional[builtins.str] = None,
            enable_partial_results_stabilization: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            filter_partial_results: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            identify_language: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            identify_multiple_languages: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            language_code: typing.Optional[builtins.str] = None,
            language_model_name: typing.Optional[builtins.str] = None,
            language_options: typing.Optional[builtins.str] = None,
            partial_results_stability: typing.Optional[builtins.str] = None,
            pii_entity_types: typing.Optional[builtins.str] = None,
            preferred_language: typing.Optional[builtins.str] = None,
            show_speaker_label: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            vocabulary_filter_method: typing.Optional[builtins.str] = None,
            vocabulary_filter_name: typing.Optional[builtins.str] = None,
            vocabulary_filter_names: typing.Optional[builtins.str] = None,
            vocabulary_name: typing.Optional[builtins.str] = None,
            vocabulary_names: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param content_identification_type: Labels all PII identified in the transcript.
            :param content_redaction_type: Redacts all PII identified in the transcript.
            :param enable_partial_results_stabilization: Enables partial result stabilization.
            :param filter_partial_results: If true, partial results are filtered out.
            :param identify_language: Turns language identification on or off.
            :param identify_multiple_languages: Turns multiple language identification on or off.
            :param language_code: The language code.
            :param language_model_name: The name of the custom language model.
            :param language_options: The language options for transcription.
            :param partial_results_stability: The level of stability for partial results.
            :param pii_entity_types: The types of PII to redact.
            :param preferred_language: The preferred language for transcription.
            :param show_speaker_label: Enables speaker partitioning.
            :param vocabulary_filter_method: The vocabulary filtering method.
            :param vocabulary_filter_name: The name of the custom vocabulary filter.
            :param vocabulary_filter_names: The names of the custom vocabulary filters.
            :param vocabulary_name: The name of the custom vocabulary.
            :param vocabulary_names: The names of the custom vocabularies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                amazon_transcribe_processor_configuration_property = chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty(
                    content_identification_type="contentIdentificationType",
                    content_redaction_type="contentRedactionType",
                    enable_partial_results_stabilization=False,
                    filter_partial_results=False,
                    identify_language=False,
                    identify_multiple_languages=False,
                    language_code="languageCode",
                    language_model_name="languageModelName",
                    language_options="languageOptions",
                    partial_results_stability="partialResultsStability",
                    pii_entity_types="piiEntityTypes",
                    preferred_language="preferredLanguage",
                    show_speaker_label=False,
                    vocabulary_filter_method="vocabularyFilterMethod",
                    vocabulary_filter_name="vocabularyFilterName",
                    vocabulary_filter_names="vocabularyFilterNames",
                    vocabulary_name="vocabularyName",
                    vocabulary_names="vocabularyNames"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__55202693225010e49bacdad3bec7e625d84491c4df67d1192367340ff7385560)
                check_type(argname="argument content_identification_type", value=content_identification_type, expected_type=type_hints["content_identification_type"])
                check_type(argname="argument content_redaction_type", value=content_redaction_type, expected_type=type_hints["content_redaction_type"])
                check_type(argname="argument enable_partial_results_stabilization", value=enable_partial_results_stabilization, expected_type=type_hints["enable_partial_results_stabilization"])
                check_type(argname="argument filter_partial_results", value=filter_partial_results, expected_type=type_hints["filter_partial_results"])
                check_type(argname="argument identify_language", value=identify_language, expected_type=type_hints["identify_language"])
                check_type(argname="argument identify_multiple_languages", value=identify_multiple_languages, expected_type=type_hints["identify_multiple_languages"])
                check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
                check_type(argname="argument language_model_name", value=language_model_name, expected_type=type_hints["language_model_name"])
                check_type(argname="argument language_options", value=language_options, expected_type=type_hints["language_options"])
                check_type(argname="argument partial_results_stability", value=partial_results_stability, expected_type=type_hints["partial_results_stability"])
                check_type(argname="argument pii_entity_types", value=pii_entity_types, expected_type=type_hints["pii_entity_types"])
                check_type(argname="argument preferred_language", value=preferred_language, expected_type=type_hints["preferred_language"])
                check_type(argname="argument show_speaker_label", value=show_speaker_label, expected_type=type_hints["show_speaker_label"])
                check_type(argname="argument vocabulary_filter_method", value=vocabulary_filter_method, expected_type=type_hints["vocabulary_filter_method"])
                check_type(argname="argument vocabulary_filter_name", value=vocabulary_filter_name, expected_type=type_hints["vocabulary_filter_name"])
                check_type(argname="argument vocabulary_filter_names", value=vocabulary_filter_names, expected_type=type_hints["vocabulary_filter_names"])
                check_type(argname="argument vocabulary_name", value=vocabulary_name, expected_type=type_hints["vocabulary_name"])
                check_type(argname="argument vocabulary_names", value=vocabulary_names, expected_type=type_hints["vocabulary_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content_identification_type is not None:
                self._values["content_identification_type"] = content_identification_type
            if content_redaction_type is not None:
                self._values["content_redaction_type"] = content_redaction_type
            if enable_partial_results_stabilization is not None:
                self._values["enable_partial_results_stabilization"] = enable_partial_results_stabilization
            if filter_partial_results is not None:
                self._values["filter_partial_results"] = filter_partial_results
            if identify_language is not None:
                self._values["identify_language"] = identify_language
            if identify_multiple_languages is not None:
                self._values["identify_multiple_languages"] = identify_multiple_languages
            if language_code is not None:
                self._values["language_code"] = language_code
            if language_model_name is not None:
                self._values["language_model_name"] = language_model_name
            if language_options is not None:
                self._values["language_options"] = language_options
            if partial_results_stability is not None:
                self._values["partial_results_stability"] = partial_results_stability
            if pii_entity_types is not None:
                self._values["pii_entity_types"] = pii_entity_types
            if preferred_language is not None:
                self._values["preferred_language"] = preferred_language
            if show_speaker_label is not None:
                self._values["show_speaker_label"] = show_speaker_label
            if vocabulary_filter_method is not None:
                self._values["vocabulary_filter_method"] = vocabulary_filter_method
            if vocabulary_filter_name is not None:
                self._values["vocabulary_filter_name"] = vocabulary_filter_name
            if vocabulary_filter_names is not None:
                self._values["vocabulary_filter_names"] = vocabulary_filter_names
            if vocabulary_name is not None:
                self._values["vocabulary_name"] = vocabulary_name
            if vocabulary_names is not None:
                self._values["vocabulary_names"] = vocabulary_names

        @builtins.property
        def content_identification_type(self) -> typing.Optional[builtins.str]:
            '''Labels all PII identified in the transcript.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-contentidentificationtype
            '''
            result = self._values.get("content_identification_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def content_redaction_type(self) -> typing.Optional[builtins.str]:
            '''Redacts all PII identified in the transcript.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-contentredactiontype
            '''
            result = self._values.get("content_redaction_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_partial_results_stabilization(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Enables partial result stabilization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-enablepartialresultsstabilization
            '''
            result = self._values.get("enable_partial_results_stabilization")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def filter_partial_results(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''If true, partial results are filtered out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-filterpartialresults
            '''
            result = self._values.get("filter_partial_results")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def identify_language(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Turns language identification on or off.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-identifylanguage
            '''
            result = self._values.get("identify_language")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def identify_multiple_languages(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Turns multiple language identification on or off.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-identifymultiplelanguages
            '''
            result = self._values.get("identify_multiple_languages")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def language_code(self) -> typing.Optional[builtins.str]:
            '''The language code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-languagecode
            '''
            result = self._values.get("language_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language_model_name(self) -> typing.Optional[builtins.str]:
            '''The name of the custom language model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-languagemodelname
            '''
            result = self._values.get("language_model_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language_options(self) -> typing.Optional[builtins.str]:
            '''The language options for transcription.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-languageoptions
            '''
            result = self._values.get("language_options")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def partial_results_stability(self) -> typing.Optional[builtins.str]:
            '''The level of stability for partial results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-partialresultsstability
            '''
            result = self._values.get("partial_results_stability")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pii_entity_types(self) -> typing.Optional[builtins.str]:
            '''The types of PII to redact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-piientitytypes
            '''
            result = self._values.get("pii_entity_types")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preferred_language(self) -> typing.Optional[builtins.str]:
            '''The preferred language for transcription.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-preferredlanguage
            '''
            result = self._values.get("preferred_language")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def show_speaker_label(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Enables speaker partitioning.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-showspeakerlabel
            '''
            result = self._values.get("show_speaker_label")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def vocabulary_filter_method(self) -> typing.Optional[builtins.str]:
            '''The vocabulary filtering method.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-vocabularyfiltermethod
            '''
            result = self._values.get("vocabulary_filter_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vocabulary_filter_name(self) -> typing.Optional[builtins.str]:
            '''The name of the custom vocabulary filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-vocabularyfiltername
            '''
            result = self._values.get("vocabulary_filter_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vocabulary_filter_names(self) -> typing.Optional[builtins.str]:
            '''The names of the custom vocabulary filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-vocabularyfilternames
            '''
            result = self._values.get("vocabulary_filter_names")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vocabulary_name(self) -> typing.Optional[builtins.str]:
            '''The name of the custom vocabulary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-vocabularyname
            '''
            result = self._values.get("vocabulary_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vocabulary_names(self) -> typing.Optional[builtins.str]:
            '''The names of the custom vocabularies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-amazontranscribeprocessorconfiguration-vocabularynames
            '''
            result = self._values.get("vocabulary_names")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonTranscribeProcessorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"rule_name": "ruleName"},
    )
    class IssueDetectionConfigurationProperty:
        def __init__(self, *, rule_name: builtins.str) -> None:
            '''
            :param rule_name: The name of the issue detection rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-issuedetectionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                issue_detection_configuration_property = chime.CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty(
                    rule_name="ruleName"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ab8c7535ce89e3bcb112d465f75d85b0285fad63a58b8b26215f096155d80c62)
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_name": rule_name,
            }

        @builtins.property
        def rule_name(self) -> builtins.str:
            '''The name of the issue detection rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-issuedetectionconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-issuedetectionconfiguration-rulename
            '''
            result = self._values.get("rule_name")
            assert result is not None, "Required property 'rule_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IssueDetectionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "keywords": "keywords",
            "rule_name": "ruleName",
            "negate": "negate",
        },
    )
    class KeywordMatchConfigurationProperty:
        def __init__(
            self,
            *,
            keywords: typing.Sequence[builtins.str],
            rule_name: builtins.str,
            negate: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        ) -> None:
            '''
            :param keywords: The keywords or phrases to match.
            :param rule_name: The name of the keyword match rule.
            :param negate: Matches keywords on their presence or absence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-keywordmatchconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                keyword_match_configuration_property = chime.CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty(
                    keywords=["keywords"],
                    rule_name="ruleName",
                
                    # the properties below are optional
                    negate=False
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6a2dae732e141f2e4061d354a319ad3929393a26356474daf8eb6b533ae66cac)
                check_type(argname="argument keywords", value=keywords, expected_type=type_hints["keywords"])
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
                check_type(argname="argument negate", value=negate, expected_type=type_hints["negate"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "keywords": keywords,
                "rule_name": rule_name,
            }
            if negate is not None:
                self._values["negate"] = negate

        @builtins.property
        def keywords(self) -> typing.List[builtins.str]:
            '''The keywords or phrases to match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-keywordmatchconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-keywordmatchconfiguration-keywords
            '''
            result = self._values.get("keywords")
            assert result is not None, "Required property 'keywords' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def rule_name(self) -> builtins.str:
            '''The name of the keyword match rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-keywordmatchconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-keywordmatchconfiguration-rulename
            '''
            result = self._values.get("rule_name")
            assert result is not None, "Required property 'rule_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def negate(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Matches keywords on their presence or absence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-keywordmatchconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-keywordmatchconfiguration-negate
            '''
            result = self._values.get("negate")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeywordMatchConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"insights_target": "insightsTarget"},
    )
    class KinesisDataStreamSinkConfigurationProperty:
        def __init__(
            self,
            *,
            insights_target: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param insights_target: The ARN of the Kinesis Data Stream sink.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-kinesisdatastreamsinkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                kinesis_data_stream_sink_configuration_property = chime.CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty(
                    insights_target="insightsTarget"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0c7b26f7516e3f0c94b597c003af93479cb85b1b15e8dbdfdf2dfaa9fd033949)
                check_type(argname="argument insights_target", value=insights_target, expected_type=type_hints["insights_target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if insights_target is not None:
                self._values["insights_target"] = insights_target

        @builtins.property
        def insights_target(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Kinesis Data Stream sink.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-kinesisdatastreamsinkconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-kinesisdatastreamsinkconfiguration-insightstarget
            '''
            result = self._values.get("insights_target")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisDataStreamSinkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "amazon_transcribe_call_analytics_processor_configuration": "amazonTranscribeCallAnalyticsProcessorConfiguration",
            "amazon_transcribe_processor_configuration": "amazonTranscribeProcessorConfiguration",
            "kinesis_data_stream_sink_configuration": "kinesisDataStreamSinkConfiguration",
            "s3_recording_sink_configuration": "s3RecordingSinkConfiguration",
        },
    )
    class MediaInsightsPipelineConfigurationElementProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            amazon_transcribe_call_analytics_processor_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            amazon_transcribe_processor_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_data_stream_sink_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_recording_sink_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param type: The element type.
            :param amazon_transcribe_call_analytics_processor_configuration: 
            :param amazon_transcribe_processor_configuration: 
            :param kinesis_data_stream_sink_configuration: 
            :param s3_recording_sink_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                media_insights_pipeline_configuration_element_property = chime.CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty(
                    type="type",
                
                    # the properties below are optional
                    amazon_transcribe_call_analytics_processor_configuration=chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty(
                        language_code="languageCode",
                
                        # the properties below are optional
                        call_analytics_stream_categories=["callAnalyticsStreamCategories"],
                        content_identification_type="contentIdentificationType",
                        content_redaction_type="contentRedactionType",
                        enable_partial_results_stabilization=False,
                        filter_partial_results=False,
                        language_model_name="languageModelName",
                        partial_results_stability="partialResultsStability",
                        pii_entity_types="piiEntityTypes",
                        post_call_analytics_settings=chime.CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty(
                            data_access_role_arn="dataAccessRoleArn",
                            output_location="outputLocation",
                
                            # the properties below are optional
                            content_redaction_output="contentRedactionOutput",
                            output_encryption_kms_key_id="outputEncryptionKmsKeyId"
                        ),
                        vocabulary_filter_method="vocabularyFilterMethod",
                        vocabulary_filter_name="vocabularyFilterName",
                        vocabulary_name="vocabularyName"
                    ),
                    amazon_transcribe_processor_configuration=chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty(
                        content_identification_type="contentIdentificationType",
                        content_redaction_type="contentRedactionType",
                        enable_partial_results_stabilization=False,
                        filter_partial_results=False,
                        identify_language=False,
                        identify_multiple_languages=False,
                        language_code="languageCode",
                        language_model_name="languageModelName",
                        language_options="languageOptions",
                        partial_results_stability="partialResultsStability",
                        pii_entity_types="piiEntityTypes",
                        preferred_language="preferredLanguage",
                        show_speaker_label=False,
                        vocabulary_filter_method="vocabularyFilterMethod",
                        vocabulary_filter_name="vocabularyFilterName",
                        vocabulary_filter_names="vocabularyFilterNames",
                        vocabulary_name="vocabularyName",
                        vocabulary_names="vocabularyNames"
                    ),
                    kinesis_data_stream_sink_configuration=chime.CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty(
                        insights_target="insightsTarget"
                    ),
                    s3_recording_sink_configuration=chime.CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty(
                        destination="destination",
                        recording_file_format="recordingFileFormat"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__9ee2b917d23080d4fd427d093f10d15a4b47ba3f834e7d360f29dcc6254db811)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument amazon_transcribe_call_analytics_processor_configuration", value=amazon_transcribe_call_analytics_processor_configuration, expected_type=type_hints["amazon_transcribe_call_analytics_processor_configuration"])
                check_type(argname="argument amazon_transcribe_processor_configuration", value=amazon_transcribe_processor_configuration, expected_type=type_hints["amazon_transcribe_processor_configuration"])
                check_type(argname="argument kinesis_data_stream_sink_configuration", value=kinesis_data_stream_sink_configuration, expected_type=type_hints["kinesis_data_stream_sink_configuration"])
                check_type(argname="argument s3_recording_sink_configuration", value=s3_recording_sink_configuration, expected_type=type_hints["s3_recording_sink_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if amazon_transcribe_call_analytics_processor_configuration is not None:
                self._values["amazon_transcribe_call_analytics_processor_configuration"] = amazon_transcribe_call_analytics_processor_configuration
            if amazon_transcribe_processor_configuration is not None:
                self._values["amazon_transcribe_processor_configuration"] = amazon_transcribe_processor_configuration
            if kinesis_data_stream_sink_configuration is not None:
                self._values["kinesis_data_stream_sink_configuration"] = kinesis_data_stream_sink_configuration
            if s3_recording_sink_configuration is not None:
                self._values["s3_recording_sink_configuration"] = s3_recording_sink_configuration

        @builtins.property
        def type(self) -> builtins.str:
            '''The element type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement.html#cfn-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def amazon_transcribe_call_analytics_processor_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement.html#cfn-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement-amazontranscribecallanalyticsprocessorconfiguration
            '''
            result = self._values.get("amazon_transcribe_call_analytics_processor_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty"]], result)

        @builtins.property
        def amazon_transcribe_processor_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement.html#cfn-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement-amazontranscribeprocessorconfiguration
            '''
            result = self._values.get("amazon_transcribe_processor_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty"]], result)

        @builtins.property
        def kinesis_data_stream_sink_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement.html#cfn-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement-kinesisdatastreamsinkconfiguration
            '''
            result = self._values.get("kinesis_data_stream_sink_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty"]], result)

        @builtins.property
        def s3_recording_sink_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement.html#cfn-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationelement-s3recordingsinkconfiguration
            '''
            result = self._values.get("s3_recording_sink_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaInsightsPipelineConfigurationElementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_access_role_arn": "dataAccessRoleArn",
            "output_location": "outputLocation",
            "content_redaction_output": "contentRedactionOutput",
            "output_encryption_kms_key_id": "outputEncryptionKmsKeyId",
        },
    )
    class PostCallAnalyticsSettingsProperty:
        def __init__(
            self,
            *,
            data_access_role_arn: builtins.str,
            output_location: builtins.str,
            content_redaction_output: typing.Optional[builtins.str] = None,
            output_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_access_role_arn: The ARN of the role used by Transcribe to upload post-call analysis.
            :param output_location: The URL of the Amazon S3 bucket for post-call data.
            :param content_redaction_output: The content redaction output settings.
            :param output_encryption_kms_key_id: The ID of the KMS key used to encrypt the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-postcallanalyticssettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                post_call_analytics_settings_property = chime.CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty(
                    data_access_role_arn="dataAccessRoleArn",
                    output_location="outputLocation",
                
                    # the properties below are optional
                    content_redaction_output="contentRedactionOutput",
                    output_encryption_kms_key_id="outputEncryptionKmsKeyId"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__55dd53917f4d820371c3d2de6f1b1b305b775665440acf4e8b26628464786c06)
                check_type(argname="argument data_access_role_arn", value=data_access_role_arn, expected_type=type_hints["data_access_role_arn"])
                check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
                check_type(argname="argument content_redaction_output", value=content_redaction_output, expected_type=type_hints["content_redaction_output"])
                check_type(argname="argument output_encryption_kms_key_id", value=output_encryption_kms_key_id, expected_type=type_hints["output_encryption_kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_access_role_arn": data_access_role_arn,
                "output_location": output_location,
            }
            if content_redaction_output is not None:
                self._values["content_redaction_output"] = content_redaction_output
            if output_encryption_kms_key_id is not None:
                self._values["output_encryption_kms_key_id"] = output_encryption_kms_key_id

        @builtins.property
        def data_access_role_arn(self) -> builtins.str:
            '''The ARN of the role used by Transcribe to upload post-call analysis.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-postcallanalyticssettings.html#cfn-chime-mediainsightspipelineconfiguration-postcallanalyticssettings-dataaccessrolearn
            '''
            result = self._values.get("data_access_role_arn")
            assert result is not None, "Required property 'data_access_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output_location(self) -> builtins.str:
            '''The URL of the Amazon S3 bucket for post-call data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-postcallanalyticssettings.html#cfn-chime-mediainsightspipelineconfiguration-postcallanalyticssettings-outputlocation
            '''
            result = self._values.get("output_location")
            assert result is not None, "Required property 'output_location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def content_redaction_output(self) -> typing.Optional[builtins.str]:
            '''The content redaction output settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-postcallanalyticssettings.html#cfn-chime-mediainsightspipelineconfiguration-postcallanalyticssettings-contentredactionoutput
            '''
            result = self._values.get("content_redaction_output")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the KMS key used to encrypt the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-postcallanalyticssettings.html#cfn-chime-mediainsightspipelineconfiguration-postcallanalyticssettings-outputencryptionkmskeyid
            '''
            result = self._values.get("output_encryption_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PostCallAnalyticsSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"disabled": "disabled", "rules": "rules"},
    )
    class RealTimeAlertConfigurationProperty:
        def __init__(
            self,
            *,
            disabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            rules: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param disabled: Turns off real-time alerts.
            :param rules: The rules in the alert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-realtimealertconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                real_time_alert_configuration_property = chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty(
                    disabled=False,
                    rules=[chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty(
                        type="type",
                
                        # the properties below are optional
                        issue_detection_configuration=chime.CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty(
                            rule_name="ruleName"
                        ),
                        keyword_match_configuration=chime.CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty(
                            keywords=["keywords"],
                            rule_name="ruleName",
                
                            # the properties below are optional
                            negate=False
                        ),
                        sentiment_configuration=chime.CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty(
                            rule_name="ruleName",
                            sentiment_type="sentimentType",
                            time_period=123
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f58a5091b81af0969b48eb2cb8c038f94af7be3f100d23e47633ebcfa5075b09)
                check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if disabled is not None:
                self._values["disabled"] = disabled
            if rules is not None:
                self._values["rules"] = rules

        @builtins.property
        def disabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Turns off real-time alerts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-realtimealertconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-realtimealertconfiguration-disabled
            '''
            result = self._values.get("disabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def rules(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty"]]]]:
            '''The rules in the alert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-realtimealertconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-realtimealertconfiguration-rules
            '''
            result = self._values.get("rules")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RealTimeAlertConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "issue_detection_configuration": "issueDetectionConfiguration",
            "keyword_match_configuration": "keywordMatchConfiguration",
            "sentiment_configuration": "sentimentConfiguration",
        },
    )
    class RealTimeAlertRuleProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            issue_detection_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            keyword_match_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sentiment_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param type: The type of alert rule.
            :param issue_detection_configuration: 
            :param keyword_match_configuration: 
            :param sentiment_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-realtimealertrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                real_time_alert_rule_property = chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty(
                    type="type",
                
                    # the properties below are optional
                    issue_detection_configuration=chime.CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty(
                        rule_name="ruleName"
                    ),
                    keyword_match_configuration=chime.CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty(
                        keywords=["keywords"],
                        rule_name="ruleName",
                
                        # the properties below are optional
                        negate=False
                    ),
                    sentiment_configuration=chime.CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty(
                        rule_name="ruleName",
                        sentiment_type="sentimentType",
                        time_period=123
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__014418bc181569b08f625dde46ac0798963eb491d4ad04fc180d53234cb2164c)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument issue_detection_configuration", value=issue_detection_configuration, expected_type=type_hints["issue_detection_configuration"])
                check_type(argname="argument keyword_match_configuration", value=keyword_match_configuration, expected_type=type_hints["keyword_match_configuration"])
                check_type(argname="argument sentiment_configuration", value=sentiment_configuration, expected_type=type_hints["sentiment_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if issue_detection_configuration is not None:
                self._values["issue_detection_configuration"] = issue_detection_configuration
            if keyword_match_configuration is not None:
                self._values["keyword_match_configuration"] = keyword_match_configuration
            if sentiment_configuration is not None:
                self._values["sentiment_configuration"] = sentiment_configuration

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of alert rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-realtimealertrule.html#cfn-chime-mediainsightspipelineconfiguration-realtimealertrule-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def issue_detection_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-realtimealertrule.html#cfn-chime-mediainsightspipelineconfiguration-realtimealertrule-issuedetectionconfiguration
            '''
            result = self._values.get("issue_detection_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty"]], result)

        @builtins.property
        def keyword_match_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-realtimealertrule.html#cfn-chime-mediainsightspipelineconfiguration-realtimealertrule-keywordmatchconfiguration
            '''
            result = self._values.get("keyword_match_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty"]], result)

        @builtins.property
        def sentiment_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-realtimealertrule.html#cfn-chime-mediainsightspipelineconfiguration-realtimealertrule-sentimentconfiguration
            '''
            result = self._values.get("sentiment_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RealTimeAlertRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "recording_file_format": "recordingFileFormat",
        },
    )
    class S3RecordingSinkConfigurationProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
            recording_file_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination: The default URI of the Amazon S3 bucket.
            :param recording_file_format: The recording file format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-s3recordingsinkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                s3_recording_sink_configuration_property = chime.CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty(
                    destination="destination",
                    recording_file_format="recordingFileFormat"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__282a9f6918db78f8c2ba6791400feb36b9c506d6568b739ade819b651c917da5)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument recording_file_format", value=recording_file_format, expected_type=type_hints["recording_file_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if recording_file_format is not None:
                self._values["recording_file_format"] = recording_file_format

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            '''The default URI of the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-s3recordingsinkconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-s3recordingsinkconfiguration-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def recording_file_format(self) -> typing.Optional[builtins.str]:
            '''The recording file format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-s3recordingsinkconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-s3recordingsinkconfiguration-recordingfileformat
            '''
            result = self._values.get("recording_file_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3RecordingSinkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_name": "ruleName",
            "sentiment_type": "sentimentType",
            "time_period": "timePeriod",
        },
    )
    class SentimentConfigurationProperty:
        def __init__(
            self,
            *,
            rule_name: builtins.str,
            sentiment_type: builtins.str,
            time_period: jsii.Number,
        ) -> None:
            '''
            :param rule_name: The name of the sentiment rule.
            :param sentiment_type: The type of sentiment.
            :param time_period: The analysis interval in seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-sentimentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                sentiment_configuration_property = chime.CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty(
                    rule_name="ruleName",
                    sentiment_type="sentimentType",
                    time_period=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__433bc2f178f4e21ad76e84ccc78517a72d926ae25aba59dc382a92cb7e86654f)
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
                check_type(argname="argument sentiment_type", value=sentiment_type, expected_type=type_hints["sentiment_type"])
                check_type(argname="argument time_period", value=time_period, expected_type=type_hints["time_period"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_name": rule_name,
                "sentiment_type": sentiment_type,
                "time_period": time_period,
            }

        @builtins.property
        def rule_name(self) -> builtins.str:
            '''The name of the sentiment rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-sentimentconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-sentimentconfiguration-rulename
            '''
            result = self._values.get("rule_name")
            assert result is not None, "Required property 'rule_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sentiment_type(self) -> builtins.str:
            '''The type of sentiment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-sentimentconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-sentimentconfiguration-sentimenttype
            '''
            result = self._values.get("sentiment_type")
            assert result is not None, "Required property 'sentiment_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_period(self) -> jsii.Number:
            '''The analysis interval in seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediainsightspipelineconfiguration-sentimentconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-sentimentconfiguration-timeperiod
            '''
            result = self._values.get("time_period")
            assert result is not None, "Required property 'time_period' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SentimentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnMediaInsightsPipelineConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "elements": "elements",
        "media_insights_pipeline_configuration_name": "mediaInsightsPipelineConfigurationName",
        "resource_access_role_arn": "resourceAccessRoleArn",
        "real_time_alert_configuration": "realTimeAlertConfiguration",
        "tags": "tags",
    },
)
class CfnMediaInsightsPipelineConfigurationProps:
    def __init__(
        self,
        *,
        elements: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty", typing.Dict[builtins.str, typing.Any]]]]],
        media_insights_pipeline_configuration_name: builtins.str,
        resource_access_role_arn: builtins.str,
        real_time_alert_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMediaInsightsPipelineConfiguration``.

        :param elements: The elements in the configuration.
        :param media_insights_pipeline_configuration_name: The name of the media insights pipeline configuration.
        :param resource_access_role_arn: The ARN of the role used by the service to access Amazon Web Services resources.
        :param real_time_alert_configuration: 
        :param tags: The tags associated with the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediainsightspipelineconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_media_insights_pipeline_configuration_props = chime.CfnMediaInsightsPipelineConfigurationProps(
                elements=[chime.CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty(
                    type="type",
            
                    # the properties below are optional
                    amazon_transcribe_call_analytics_processor_configuration=chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty(
                        language_code="languageCode",
            
                        # the properties below are optional
                        call_analytics_stream_categories=["callAnalyticsStreamCategories"],
                        content_identification_type="contentIdentificationType",
                        content_redaction_type="contentRedactionType",
                        enable_partial_results_stabilization=False,
                        filter_partial_results=False,
                        language_model_name="languageModelName",
                        partial_results_stability="partialResultsStability",
                        pii_entity_types="piiEntityTypes",
                        post_call_analytics_settings=chime.CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty(
                            data_access_role_arn="dataAccessRoleArn",
                            output_location="outputLocation",
            
                            # the properties below are optional
                            content_redaction_output="contentRedactionOutput",
                            output_encryption_kms_key_id="outputEncryptionKmsKeyId"
                        ),
                        vocabulary_filter_method="vocabularyFilterMethod",
                        vocabulary_filter_name="vocabularyFilterName",
                        vocabulary_name="vocabularyName"
                    ),
                    amazon_transcribe_processor_configuration=chime.CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty(
                        content_identification_type="contentIdentificationType",
                        content_redaction_type="contentRedactionType",
                        enable_partial_results_stabilization=False,
                        filter_partial_results=False,
                        identify_language=False,
                        identify_multiple_languages=False,
                        language_code="languageCode",
                        language_model_name="languageModelName",
                        language_options="languageOptions",
                        partial_results_stability="partialResultsStability",
                        pii_entity_types="piiEntityTypes",
                        preferred_language="preferredLanguage",
                        show_speaker_label=False,
                        vocabulary_filter_method="vocabularyFilterMethod",
                        vocabulary_filter_name="vocabularyFilterName",
                        vocabulary_filter_names="vocabularyFilterNames",
                        vocabulary_name="vocabularyName",
                        vocabulary_names="vocabularyNames"
                    ),
                    kinesis_data_stream_sink_configuration=chime.CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty(
                        insights_target="insightsTarget"
                    ),
                    s3_recording_sink_configuration=chime.CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty(
                        destination="destination",
                        recording_file_format="recordingFileFormat"
                    )
                )],
                media_insights_pipeline_configuration_name="mediaInsightsPipelineConfigurationName",
                resource_access_role_arn="resourceAccessRoleArn",
            
                # the properties below are optional
                real_time_alert_configuration=chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty(
                    disabled=False,
                    rules=[chime.CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty(
                        type="type",
            
                        # the properties below are optional
                        issue_detection_configuration=chime.CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty(
                            rule_name="ruleName"
                        ),
                        keyword_match_configuration=chime.CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty(
                            keywords=["keywords"],
                            rule_name="ruleName",
            
                            # the properties below are optional
                            negate=False
                        ),
                        sentiment_configuration=chime.CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty(
                            rule_name="ruleName",
                            sentiment_type="sentimentType",
                            time_period=123
                        )
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c5edcf05aa706b7cb6499c317d5a3073fbd8b8e091f593c38e6cbbcd4e4b4835)
            check_type(argname="argument elements", value=elements, expected_type=type_hints["elements"])
            check_type(argname="argument media_insights_pipeline_configuration_name", value=media_insights_pipeline_configuration_name, expected_type=type_hints["media_insights_pipeline_configuration_name"])
            check_type(argname="argument resource_access_role_arn", value=resource_access_role_arn, expected_type=type_hints["resource_access_role_arn"])
            check_type(argname="argument real_time_alert_configuration", value=real_time_alert_configuration, expected_type=type_hints["real_time_alert_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "elements": elements,
            "media_insights_pipeline_configuration_name": media_insights_pipeline_configuration_name,
            "resource_access_role_arn": resource_access_role_arn,
        }
        if real_time_alert_configuration is not None:
            self._values["real_time_alert_configuration"] = real_time_alert_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def elements(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty"]]]:
        '''The elements in the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediainsightspipelineconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-elements
        '''
        result = self._values.get("elements")
        assert result is not None, "Required property 'elements' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty"]]], result)

    @builtins.property
    def media_insights_pipeline_configuration_name(self) -> builtins.str:
        '''The name of the media insights pipeline configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediainsightspipelineconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-mediainsightspipelineconfigurationname
        '''
        result = self._values.get("media_insights_pipeline_configuration_name")
        assert result is not None, "Required property 'media_insights_pipeline_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_access_role_arn(self) -> builtins.str:
        '''The ARN of the role used by the service to access Amazon Web Services resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediainsightspipelineconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-resourceaccessrolearn
        '''
        result = self._values.get("resource_access_role_arn")
        assert result is not None, "Required property 'resource_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def real_time_alert_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediainsightspipelineconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-realtimealertconfiguration
        '''
        result = self._values.get("real_time_alert_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags associated with the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediainsightspipelineconfiguration.html#cfn-chime-mediainsightspipelineconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMediaInsightsPipelineConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.IMediaPipelineKinesisVideoStreamPoolRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnMediaPipelineKinesisVideoStreamPool(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnMediaPipelineKinesisVideoStreamPool",
):
    '''Resource Type definition for an Amazon Chime SDK Media Pipeline Kinesis Video Stream Pool.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediapipelinekinesisvideostreampool.html
    :cloudformationResource: AWS::Chime::MediaPipelineKinesisVideoStreamPool
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_media_pipeline_kinesis_video_stream_pool = chime.CfnMediaPipelineKinesisVideoStreamPool(self, "MyCfnMediaPipelineKinesisVideoStreamPool",
            pool_name="poolName",
            stream_configuration=chime.CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty(
                region="region",
        
                # the properties below are optional
                data_retention_in_hours=123
            ),
        
            # the properties below are optional
            tags=[chime.CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty(
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
        pool_name: builtins.str,
        stream_configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::MediaPipelineKinesisVideoStreamPool``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param pool_name: The name of the Kinesis Video Stream Pool.
        :param stream_configuration: The configuration settings for the Kinesis video stream.
        :param tags: The tags associated with the Kinesis Video Stream Pool.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b336d9205da99d4437e13b57fe31566b7bcddbad8a4aca01118d6e9af2e64130)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMediaPipelineKinesisVideoStreamPoolProps(
            pool_name=pool_name, stream_configuration=stream_configuration, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForMediaPipelineKinesisVideoStreamPool")
    @builtins.classmethod
    def arn_for_media_pipeline_kinesis_video_stream_pool(
        cls,
        resource: "_aws_chime_58870695.IMediaPipelineKinesisVideoStreamPoolRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__32690cfe6167486a6bc73ee7a4e8b2d72cf2b71f8d044f85f72d01dafc98562b)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForMediaPipelineKinesisVideoStreamPool", [resource]))

    @jsii.member(jsii_name="isCfnMediaPipelineKinesisVideoStreamPool")
    @builtins.classmethod
    def is_cfn_media_pipeline_kinesis_video_stream_pool(
        cls,
        x: typing.Any,
    ) -> builtins.bool:
        '''Checks whether the given object is a CfnMediaPipelineKinesisVideoStreamPool.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__49dc319dea57d3c17dfa63f2944c37fff0d692bfb0acb6c6a6c8d4849a7fbcae)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnMediaPipelineKinesisVideoStreamPool", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5bb3bc86383838753d4e892b4d5b009b8a4bf3d69ae85b39d6d4a54445fbd219)
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
            type_hints = cached_type_hints(_typecheckingstub__023cb1dbceee8545cd0fb5816a4202d640695b79fc5f31581fab9f0ee4e134ec)
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
        '''The ARN of the Kinesis Video Stream Pool.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The time at which the Kinesis Video Stream Pool was created.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrPoolId")
    def attr_pool_id(self) -> builtins.str:
        '''The unique identifier of the Kinesis Video Stream Pool.

        :cloudformationAttribute: PoolId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPoolId"))

    @builtins.property
    @jsii.member(jsii_name="attrPoolStatus")
    def attr_pool_status(self) -> builtins.str:
        '''The status of the Kinesis Video Stream Pool.

        :cloudformationAttribute: PoolStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPoolStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''The time at which the Kinesis Video Stream Pool was last updated.

        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

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
    @jsii.member(jsii_name="mediaPipelineKinesisVideoStreamPoolRef")
    def media_pipeline_kinesis_video_stream_pool_ref(
        self,
    ) -> "_aws_chime_58870695.MediaPipelineKinesisVideoStreamPoolReference":
        '''A reference to a MediaPipelineKinesisVideoStreamPool resource.'''
        return typing.cast("_aws_chime_58870695.MediaPipelineKinesisVideoStreamPoolReference", jsii.get(self, "mediaPipelineKinesisVideoStreamPoolRef"))

    @builtins.property
    @jsii.member(jsii_name="poolName")
    def pool_name(self) -> builtins.str:
        '''The name of the Kinesis Video Stream Pool.'''
        return typing.cast(builtins.str, jsii.get(self, "poolName"))

    @pool_name.setter
    def pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f677f01464018d20d5c629d5a30dfe7b5a353a6f894cee558cd7a079815b3648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="streamConfiguration")
    def stream_configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty"]:
        '''The configuration settings for the Kinesis video stream.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty"], jsii.get(self, "streamConfiguration"))

    @stream_configuration.setter
    def stream_configuration(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4eef490c284885605bd4d9641f9a06d3eda73e2ce6d657b210b0a1f9a297ab7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(
        self,
    ) -> typing.Optional[typing.List["CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty"]]:
        '''The tags associated with the Kinesis Video Stream Pool.'''
        return typing.cast(typing.Optional[typing.List["CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__994c1e7aea782a4f5ac4c165542058880ff58e7435841b0f9687daa4baa0d0ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "data_retention_in_hours": "dataRetentionInHours",
        },
    )
    class StreamConfigurationProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            data_retention_in_hours: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The configuration settings for the Kinesis video stream.

            :param region: The AWS Region of the video stream.
            :param data_retention_in_hours: The amount of time that data is retained, in hours.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediapipelinekinesisvideostreampool-streamconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                stream_configuration_property = chime.CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty(
                    region="region",
                
                    # the properties below are optional
                    data_retention_in_hours=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__9180f89bf344bebe3717327b7e726cc5fc7402b806c845d0a7bec90af2aa71a6)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument data_retention_in_hours", value=data_retention_in_hours, expected_type=type_hints["data_retention_in_hours"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
            }
            if data_retention_in_hours is not None:
                self._values["data_retention_in_hours"] = data_retention_in_hours

        @builtins.property
        def region(self) -> builtins.str:
            '''The AWS Region of the video stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediapipelinekinesisvideostreampool-streamconfiguration.html#cfn-chime-mediapipelinekinesisvideostreampool-streamconfiguration-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_retention_in_hours(self) -> typing.Optional[jsii.Number]:
            '''The amount of time that data is retained, in hours.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediapipelinekinesisvideostreampool-streamconfiguration.html#cfn-chime-mediapipelinekinesisvideostreampool-streamconfiguration-dataretentioninhours
            '''
            result = self._values.get("data_retention_in_hours")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsItemsProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediapipelinekinesisvideostreampool-tagsitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                tags_items_property = chime.CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__720939a95a92fe53c15ba34c0f539667cb899205f38b3e1f0635deeb6d1ee34b)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediapipelinekinesisvideostreampool-tagsitems.html#cfn-chime-mediapipelinekinesisvideostreampool-tagsitems-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-mediapipelinekinesisvideostreampool-tagsitems.html#cfn-chime-mediapipelinekinesisvideostreampool-tagsitems-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnMediaPipelineKinesisVideoStreamPoolProps",
    jsii_struct_bases=[],
    name_mapping={
        "pool_name": "poolName",
        "stream_configuration": "streamConfiguration",
        "tags": "tags",
    },
)
class CfnMediaPipelineKinesisVideoStreamPoolProps:
    def __init__(
        self,
        *,
        pool_name: builtins.str,
        stream_configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMediaPipelineKinesisVideoStreamPool``.

        :param pool_name: The name of the Kinesis Video Stream Pool.
        :param stream_configuration: The configuration settings for the Kinesis video stream.
        :param tags: The tags associated with the Kinesis Video Stream Pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediapipelinekinesisvideostreampool.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_media_pipeline_kinesis_video_stream_pool_props = chime.CfnMediaPipelineKinesisVideoStreamPoolProps(
                pool_name="poolName",
                stream_configuration=chime.CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty(
                    region="region",
            
                    # the properties below are optional
                    data_retention_in_hours=123
                ),
            
                # the properties below are optional
                tags=[chime.CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0a4fb7dfa431fc097a5630ce4858b4dd3da0617dbc59442dd069b385683b9538)
            check_type(argname="argument pool_name", value=pool_name, expected_type=type_hints["pool_name"])
            check_type(argname="argument stream_configuration", value=stream_configuration, expected_type=type_hints["stream_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pool_name": pool_name,
            "stream_configuration": stream_configuration,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pool_name(self) -> builtins.str:
        '''The name of the Kinesis Video Stream Pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediapipelinekinesisvideostreampool.html#cfn-chime-mediapipelinekinesisvideostreampool-poolname
        '''
        result = self._values.get("pool_name")
        assert result is not None, "Required property 'pool_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty"]:
        '''The configuration settings for the Kinesis video stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediapipelinekinesisvideostreampool.html#cfn-chime-mediapipelinekinesisvideostreampool-streamconfiguration
        '''
        result = self._values.get("stream_configuration")
        assert result is not None, "Required property 'stream_configuration' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty"], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.List["CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty"]]:
        '''The tags associated with the Kinesis Video Stream Pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-mediapipelinekinesisvideostreampool.html#cfn-chime-mediapipelinekinesisvideostreampool-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMediaPipelineKinesisVideoStreamPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.ISipMediaApplicationRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnSipMediaApplication(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnSipMediaApplication",
):
    '''Resource Type definition for AWS::Chime::SipMediaApplication.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-sipmediaapplication.html
    :cloudformationResource: AWS::Chime::SipMediaApplication
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_sip_media_application = chime.CfnSipMediaApplication(self, "MyCfnSipMediaApplication",
            aws_region="awsRegion",
            endpoints=[chime.CfnSipMediaApplication.SipMediaApplicationEndpointProperty(
                lambda_arn="lambdaArn"
            )],
            name="name",
        
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
        aws_region: builtins.str,
        endpoints: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSipMediaApplication.SipMediaApplicationEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::SipMediaApplication``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param aws_region: The AWS Region in which the SIP media application is created.
        :param endpoints: List of endpoints (Lambda ARNs) specified for the SIP media application.
        :param name: The name of the SIP media application.
        :param tags: Tags assigned to the SIP media application.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__26eb8c1bc4a1f86978d3246e599a9aa699835a5d089fa644436e38af502db993)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSipMediaApplicationProps(
            aws_region=aws_region, endpoints=endpoints, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSipMediaApplication")
    @builtins.classmethod
    def arn_for_sip_media_application(
        cls,
        resource: "_aws_chime_58870695.ISipMediaApplicationRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ba0d683650689e2081014db2d6fb9a99607330603aeb24831e1b4435308282a6)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSipMediaApplication", [resource]))

    @jsii.member(jsii_name="isCfnSipMediaApplication")
    @builtins.classmethod
    def is_cfn_sip_media_application(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSipMediaApplication.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2be69fd45b5d6f37793e1a3c4568d5fefa809a190aa3b6d71debe22da918b05d)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSipMediaApplication", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__be1e3584a84de325a695edf5be77fbe8848ccb44a374d874697fb274c323ed00)
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
            type_hints = cached_type_hints(_typecheckingstub__3492a5dbb051d3de8df839802771567711dc67d94bf59796892bbc6bfb37fdf7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The SIP media application creation timestamp, in ISO 8601 format.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrSipMediaApplicationArn")
    def attr_sip_media_application_arn(self) -> builtins.str:
        '''The ARN of the SIP media application.

        :cloudformationAttribute: SipMediaApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSipMediaApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSipMediaApplicationId")
    def attr_sip_media_application_id(self) -> builtins.str:
        '''The SIP media application ID.

        :cloudformationAttribute: SipMediaApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSipMediaApplicationId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''The time at which the SIP media application was updated.

        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

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
    @jsii.member(jsii_name="sipMediaApplicationRef")
    def sip_media_application_ref(
        self,
    ) -> "_aws_chime_58870695.SipMediaApplicationReference":
        '''A reference to a SipMediaApplication resource.'''
        return typing.cast("_aws_chime_58870695.SipMediaApplicationReference", jsii.get(self, "sipMediaApplicationRef"))

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        '''The AWS Region in which the SIP media application is created.'''
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4a2351c8de98c40a4806a6c3430bda1438b5d8da90910f625bff87ae9672466c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="endpoints")
    def endpoints(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSipMediaApplication.SipMediaApplicationEndpointProperty"]]]:
        '''List of endpoints (Lambda ARNs) specified for the SIP media application.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSipMediaApplication.SipMediaApplicationEndpointProperty"]]], jsii.get(self, "endpoints"))

    @endpoints.setter
    def endpoints(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSipMediaApplication.SipMediaApplicationEndpointProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6d39849434edfc162ba7322548e8f937629a922e919e923822c0d77e54c9544f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoints", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the SIP media application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__637cbb29fb24b5f18d6dd14a0acb910eec6b79c40ed43346a0bfef34740a74a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags assigned to the SIP media application.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3e77d8effaf0cfae22ca3cab05ea8c172429af80efd993b6d6b08b6f7a6e033a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_chime.CfnSipMediaApplication.SipMediaApplicationEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_arn": "lambdaArn"},
    )
    class SipMediaApplicationEndpointProperty:
        def __init__(self, *, lambda_arn: builtins.str) -> None:
            '''
            :param lambda_arn: Valid Amazon Resource Name (ARN) of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-sipmediaapplication-sipmediaapplicationendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_chime as chime
                
                sip_media_application_endpoint_property = chime.CfnSipMediaApplication.SipMediaApplicationEndpointProperty(
                    lambda_arn="lambdaArn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a21df4d9a86ef098cfa2390c70577cdd058412ed46b6983f7ae3e8d0e64c9c53)
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_arn": lambda_arn,
            }

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''Valid Amazon Resource Name (ARN) of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-chime-sipmediaapplication-sipmediaapplicationendpoint.html#cfn-chime-sipmediaapplication-sipmediaapplicationendpoint-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SipMediaApplicationEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnSipMediaApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_region": "awsRegion",
        "endpoints": "endpoints",
        "name": "name",
        "tags": "tags",
    },
)
class CfnSipMediaApplicationProps:
    def __init__(
        self,
        *,
        aws_region: builtins.str,
        endpoints: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSipMediaApplication.SipMediaApplicationEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSipMediaApplication``.

        :param aws_region: The AWS Region in which the SIP media application is created.
        :param endpoints: List of endpoints (Lambda ARNs) specified for the SIP media application.
        :param name: The name of the SIP media application.
        :param tags: Tags assigned to the SIP media application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-sipmediaapplication.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_sip_media_application_props = chime.CfnSipMediaApplicationProps(
                aws_region="awsRegion",
                endpoints=[chime.CfnSipMediaApplication.SipMediaApplicationEndpointProperty(
                    lambda_arn="lambdaArn"
                )],
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4b2d633e5b779a6c367587f51d4100a3e0e2a07b261dd3f0daa879adca38fe54)
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            check_type(argname="argument endpoints", value=endpoints, expected_type=type_hints["endpoints"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_region": aws_region,
            "endpoints": endpoints,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def aws_region(self) -> builtins.str:
        '''The AWS Region in which the SIP media application is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-sipmediaapplication.html#cfn-chime-sipmediaapplication-awsregion
        '''
        result = self._values.get("aws_region")
        assert result is not None, "Required property 'aws_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoints(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSipMediaApplication.SipMediaApplicationEndpointProperty"]]]:
        '''List of endpoints (Lambda ARNs) specified for the SIP media application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-sipmediaapplication.html#cfn-chime-sipmediaapplication-endpoints
        '''
        result = self._values.get("endpoints")
        assert result is not None, "Required property 'endpoints' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSipMediaApplication.SipMediaApplicationEndpointProperty"]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the SIP media application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-sipmediaapplication.html#cfn-chime-sipmediaapplication-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags assigned to the SIP media application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-sipmediaapplication.html#cfn-chime-sipmediaapplication-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSipMediaApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_chime_58870695.IVoiceConnectorRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnVoiceConnector(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chime.CfnVoiceConnector",
):
    '''An Amazon Chime SDK Voice Connector configuration, including outbound host name and encryption settings.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-voiceconnector.html
    :cloudformationResource: AWS::Chime::VoiceConnector
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chime as chime
        
        cfn_voice_connector = chime.CfnVoiceConnector(self, "MyCfnVoiceConnector",
            name="name",
            require_encryption=False,
        
            # the properties below are optional
            aws_region="awsRegion",
            network_type="networkType",
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
        require_encryption: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
        aws_region: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Chime::VoiceConnector``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the Voice Connector.
        :param require_encryption: Enables or disables encryption for the Voice Connector.
        :param aws_region: The AWS Region in which the Voice Connector is created.
        :param network_type: The type of network for the Voice Connector.
        :param tags: The tags assigned to the Voice Connector.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__45a25fd89e9de3fb404a08691b4c7ee98e0f077a34dc286b1cfce7f532fc05a2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVoiceConnectorProps(
            name=name,
            require_encryption=require_encryption,
            aws_region=aws_region,
            network_type=network_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVoiceConnector")
    @builtins.classmethod
    def arn_for_voice_connector(
        cls,
        resource: "_aws_chime_58870695.IVoiceConnectorRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__665d280f8f7569acff61b157dc414017ab7f482e10a00950ec6899957eb17cdf)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVoiceConnector", [resource]))

    @jsii.member(jsii_name="isCfnVoiceConnector")
    @builtins.classmethod
    def is_cfn_voice_connector(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVoiceConnector.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e2ecc4f32023674befc0ccc9379b88b16aae99e14435795fce3c30cb902fae2c)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVoiceConnector", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d3977b7652d57b9a0da2fb652c70c5b8445222f780f87d4b34dff3b3a830124e)
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
            type_hints = cached_type_hints(_typecheckingstub__0191f5993b709064b78f286535ab05ebb6ffe17837ee9caec0239b04963c4e1e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The Voice Connector creation timestamp, in ISO 8601 format.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrOutboundHostName")
    def attr_outbound_host_name(self) -> builtins.str:
        '''The outbound host name for the Voice Connector.

        :cloudformationAttribute: OutboundHostName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOutboundHostName"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''The Voice Connector updated timestamp, in ISO 8601 format.

        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrVoiceConnectorArn")
    def attr_voice_connector_arn(self) -> builtins.str:
        '''The ARN of the Voice Connector.

        :cloudformationAttribute: VoiceConnectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVoiceConnectorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVoiceConnectorId")
    def attr_voice_connector_id(self) -> builtins.str:
        '''The Voice Connector ID.

        :cloudformationAttribute: VoiceConnectorId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVoiceConnectorId"))

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
    @jsii.member(jsii_name="voiceConnectorRef")
    def voice_connector_ref(self) -> "_aws_chime_58870695.VoiceConnectorReference":
        '''A reference to a VoiceConnector resource.'''
        return typing.cast("_aws_chime_58870695.VoiceConnectorReference", jsii.get(self, "voiceConnectorRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Voice Connector.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__787a84d7c3d4d36ba68b8e307c922a0ec73d2389a1a30a84ddc055d72d127ffa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requireEncryption")
    def require_encryption(
        self,
    ) -> typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]:
        '''Enables or disables encryption for the Voice Connector.'''
        return typing.cast(typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"], jsii.get(self, "requireEncryption"))

    @require_encryption.setter
    def require_encryption(
        self,
        value: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__74f77946a6da8b6b6475129ab1e18916bd7b6b0329c2b4d16869d6db6e4d5b4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireEncryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region in which the Voice Connector is created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9c3900dc2719e0dab876645a1db496658a0424323d8a7781cb0e0d33e57147d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkType")
    def network_type(self) -> typing.Optional[builtins.str]:
        '''The type of network for the Voice Connector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkType"))

    @network_type.setter
    def network_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ddaa871794b6518dc8bd6140a4ce963a409e289a5f48e907522ad7766dffa252)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the Voice Connector.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__035b14d74fc5c3eb7431fd43c26137270d2039024e8aed2254c225c80aee44b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chime.CfnVoiceConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "require_encryption": "requireEncryption",
        "aws_region": "awsRegion",
        "network_type": "networkType",
        "tags": "tags",
    },
)
class CfnVoiceConnectorProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        require_encryption: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
        aws_region: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVoiceConnector``.

        :param name: The name of the Voice Connector.
        :param require_encryption: Enables or disables encryption for the Voice Connector.
        :param aws_region: The AWS Region in which the Voice Connector is created.
        :param network_type: The type of network for the Voice Connector.
        :param tags: The tags assigned to the Voice Connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-voiceconnector.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chime as chime
            
            cfn_voice_connector_props = chime.CfnVoiceConnectorProps(
                name="name",
                require_encryption=False,
            
                # the properties below are optional
                aws_region="awsRegion",
                network_type="networkType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8ce9a6b502ef05469370c725a4e8275d6f0ef0b0d8135c1376f5871e55058375)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument require_encryption", value=require_encryption, expected_type=type_hints["require_encryption"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            check_type(argname="argument network_type", value=network_type, expected_type=type_hints["network_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "require_encryption": require_encryption,
        }
        if aws_region is not None:
            self._values["aws_region"] = aws_region
        if network_type is not None:
            self._values["network_type"] = network_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Voice Connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-voiceconnector.html#cfn-chime-voiceconnector-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def require_encryption(
        self,
    ) -> typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]:
        '''Enables or disables encryption for the Voice Connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-voiceconnector.html#cfn-chime-voiceconnector-requireencryption
        '''
        result = self._values.get("require_encryption")
        assert result is not None, "Required property 'require_encryption' is missing"
        return typing.cast(typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"], result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region in which the Voice Connector is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-voiceconnector.html#cfn-chime-voiceconnector-awsregion
        '''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_type(self) -> typing.Optional[builtins.str]:
        '''The type of network for the Voice Connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-voiceconnector.html#cfn-chime-voiceconnector-networktype
        '''
        result = self._values.get("network_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the Voice Connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chime-voiceconnector.html#cfn-chime-voiceconnector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVoiceConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAppInstance",
    "CfnAppInstanceBot",
    "CfnAppInstanceBotProps",
    "CfnAppInstanceProps",
    "CfnAppInstanceUser",
    "CfnAppInstanceUserProps",
    "CfnChannel",
    "CfnChannelFlow",
    "CfnChannelFlowProps",
    "CfnChannelProps",
    "CfnMediaInsightsPipelineConfiguration",
    "CfnMediaInsightsPipelineConfigurationProps",
    "CfnMediaPipelineKinesisVideoStreamPool",
    "CfnMediaPipelineKinesisVideoStreamPoolProps",
    "CfnSipMediaApplication",
    "CfnSipMediaApplicationProps",
    "CfnVoiceConnector",
    "CfnVoiceConnectorProps",
]

publication.publish()

def _typecheckingstub__6d337d6c149cc789c0b6f05ba4ba90f831464295606b004354b7815daaed0c77(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    metadata: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f74b0e7014ea5c23e28103a5fb5867813697fd8201279c330a3aa769bc126a1(
    resource: _aws_chime_58870695.IAppInstanceRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0a664656abafe2adc6e2a0a9db5e06dc33b5b3b6a0fa2a5ca0b61b7b95d0c32(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__400a60274a57ac76d314b93fb263163beba6942cc730e90588d6f74e739f4eb0(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c4ccf5db0f869956272a9d89ee82b1cfb49e2aacbbc94b43a595151f8b37e60(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b72de3b84f85f89b400c53dced98e7828184761f13429f1028134b5727fe38e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d28a89759474ddf9cf296e1da1bbf9afe7e7c1413d9a4d175db15deaca419f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc357af54a794ca273668787f93dac3a63d2f85c8108d86aa56926b60d6aac5a(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca75944f6ceb69180d3b0f352517267777aeee7ffaa12b2f1a465cf9b6a3e00(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_instance_arn: builtins.str,
    configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAppInstanceBot.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    metadata: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49c5faf3dcf2887594ff746db96b49d9757db79f86e9d6f358d9f275ee8c8210(
    resource: _aws_chime_58870695.IAppInstanceBotRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0255372b69a195b0351367c082f9533519223c17e242b93716f61ed8e55dea62(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427e24f474e9d78b560301eb631ab4ec523303c4565f63f29c83299fe5abafb1(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f31284f1d604da54c34b53acb2ff3863b786fb7370f15d19da68df814cd8ad(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a53900f75f263ec868d4efe44340a9273169b155a8e54a68fe8cde3818baec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d36a14f99ec95cd590d6c1757bb41c8b9235cf6b317fa73e6692074ed033195a(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnAppInstanceBot.ConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45024baca15a880d713b7458c08c15471a9b4b4bc485fcaa496535c2d75a30a8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ad6a83eab879d92eb2609e2f37735b3c2383bb2e7e24c6cefbec192e42c39e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d87e45b7d9459784717058ca252a094c146e5656ea14d9da51f1cf05f4aa56d4(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ff343ee28319a719419e7819c467b339964da524abd8a8f50f44edd43b11a8(
    *,
    lex: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAppInstanceBot.LexConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0a8291bb53d368f6b1012fdd17317226c377241787e7d74d9371e641c527be4(
    *,
    standard_messages: builtins.str,
    targeted_messages: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e9097c00a1cff69d67ed6937aea0b11010ff23c371f50b9ae25d98378dbf55(
    *,
    lex_bot_alias_arn: builtins.str,
    locale_id: builtins.str,
    invoked_by: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAppInstanceBot.InvokedByProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    responds_to: typing.Optional[builtins.str] = None,
    welcome_intent: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d900ae3a9eb6a587e47f3e534920839a7bec4e3fc41d625d3e3b8eb9d31d4eae(
    *,
    app_instance_arn: builtins.str,
    configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAppInstanceBot.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    metadata: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551f6928f9d6a158547ebe3a9d4b368b45ad66d983bfb330b063b77c078ca90e(
    *,
    name: builtins.str,
    metadata: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2085cb61a0928e322527b02fa835e93ae1473637b82fc400d98124c9f4ea85ef(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_instance_arn: builtins.str,
    app_instance_user_id: builtins.str,
    expiration_settings: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAppInstanceUser.ExpirationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metadata: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__834453efdb4b627060834867c4d4be14cef2b1616cd26510f95ad19700c58e71(
    resource: _aws_chime_58870695.IAppInstanceUserRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8249e724ed1b8ced6af4d14e2e058e7d87c556d2f34822d2c13ef2eae05db6f(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__863252a597952f489269b67d81cb8b94673d4899994aee030ef3ab18f84474cf(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2319035bf7a04fca46bccb72f782d57c44957ca4561f7cd63c521a103cb24570(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20a22b966f7df8751e06019df44b290ea5ac0f00632c5f0800d1ac32bc198eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfdd12ef0fd7a56e531e08fb8f66900a90956c52b40bad7b1a5bc196cc3b9f45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11df1f0a14380b6e64d70d38f2d2279aa0cad03492a1c3ea2c336851c1379cd8(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnAppInstanceUser.ExpirationSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__503686b1a9877ef8aef136c790c2be6a495abcde2081aa874974aba213155b4a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94ed3eda3e56547fc67748fa6d649fea23db4fd56781e44025b0e46a5857c8a5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9051ba4c8c7a02ae24d26117b6b0c144f5b530848f9f9411655d4461d5883b41(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e650d9ca25019153fe4e2391b149c6b4c2a2336449a5886a3b94f66bf8ccb812(
    *,
    expiration_criterion: builtins.str,
    expiration_days: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c191e7d70c48f14aeb5305a9541ebc0cb899fc4cc9efe9e64a380ae2098e7b6e(
    *,
    app_instance_arn: builtins.str,
    app_instance_user_id: builtins.str,
    expiration_settings: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnAppInstanceUser.ExpirationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metadata: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a89763003c5889154da844ca3dad921cfa98c23c362a40a05e69b7812336097d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_instance_arn: builtins.str,
    chime_bearer: builtins.str,
    name: builtins.str,
    channel_id: typing.Optional[builtins.str] = None,
    elastic_channel_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.ElasticChannelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    expiration_settings: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.ExpirationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    member_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    metadata: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    moderator_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    privacy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c427c0278e1c98cd454086845e50069da70f9022ed5cdd80f053334831c2cbb7(
    resource: _aws_chime_58870695.IChannelRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa4790ed4f040aa7c08ce37d765a2efe53b80721c32fd5b1bbda12dc3ae91a05(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56cb1e61db1c45729b964df35b81c00ecbadeb1e6841d345c0dfdce81520f8f3(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe58cc1b62badb3a367bdac675a7be40061ccddeb1291043e6a89f46b1941a0b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8f59d56a9dbf4b3806ff1912cf07850ffda9a4e9b55db675fece72d4dd31b0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd04eb030be5b81f943a19c35fdeaa7124f05290326272628749488abfbd429(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4a11111ed722fa1552e5357156422c544c2a4dd446be1ea345c98978081526(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2899b697a3d0599c4e86d02b714e86b25a73faa81d81b0b5a8a2b846f90a193d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702d50233a97086fe25c17623249cdf79a35a98fd0c2ff24fc4c4ff212b8c90d(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnChannel.ElasticChannelConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa4426ad9d68b9d95e87acf17bd96807ddb690c4339e557b335d54201155053(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnChannel.ExpirationSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d78aaa655e8d98ed189cc1db70ccbc99177cf80d3892ff11d41097adfbd6764(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d047bb8ce80e19c537d247457b6cc43cd31f25981080e85979a87b0c6d44eea3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__826ffe751bf3da6b2ef69e117e86116849fa30257fc6a0ba2d55e0eee456d8cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7931948e641c85a29c91dc0f18a05368cce4d97845b3fe14bc39e397032efb1d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ef91b405bc43229f3ad9bb756d161a4b0db50cfd4360ae21ef7c55c52f5944(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22aa1755f5052e591b4cabb4cbc7f1e285d37bd5839a3720256c387127f5aeb3(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e0f478c14d309a5588841538b8043223e8385c82a42bfb60c7a2bdb9d77a9a(
    *,
    maximum_sub_channels: jsii.Number,
    minimum_membership_percentage: jsii.Number,
    target_memberships_per_sub_channel: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61fc7651b450f23570f29d1017ecab7caa5c391d1b674257b21ed9b83c1c68f6(
    *,
    expiration_criterion: builtins.str,
    expiration_days: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bfa5f1d241cfa51cfb94fc2037ee9ab05fc2825441e3b064b5c3346d71baebc(
    *,
    arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__553e37c55476a947075ca59056beea348820f4c9d0001731f2dc6df208e46aac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_instance_arn: builtins.str,
    name: builtins.str,
    processors: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannelFlow.ProcessorProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__215e52bbdaf64af19e7a78a4c16ecf1be25619c25b0f1f560edef98f17fd074f(
    resource: _aws_chime_58870695.IChannelFlowRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cd9c6e628c1ed57d7d45231f8fd40a59294a2cfe8e8086a494a43b0dfbcb348(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d931527d027465cc783a90101afd59c6d28ac9549723ed78d381411c1f152c(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c315bd571cdd659263f798212f27154c2c646ef9c193834f07a863a925933999(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2952f13ac0bef71a3fce903cbe1c25737bd7625917778a93a03dac2015fa2104(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__411cc8fb86020950b5c9e5844fb80dccb3d2c00b763b9ab9a8f9b5cc719d9451(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87728ae9e5da9fcebfef150b2b1326c7b3106255781f7f53de411ad39a29a508(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnChannelFlow.ProcessorProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a722312beda48b0dba71e0a7247be1089c7db33dfb3f22b8eb02c0cea9adc2(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__285ed0bc098587d57e9f94632c1cb3c1c76fff652d29fd8997a47c3b2cc1cc09(
    *,
    invocation_type: builtins.str,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fdc1fc093fa01b9277bf2dd738d6f6237e1cce994cac73e6f7d4e62ab99ac5c(
    *,
    lambda_: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannelFlow.LambdaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be4dcd983ce00e19de1c1ec7124b3517157f895d6121f59f1ca204a7a59f7fc1(
    *,
    configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannelFlow.ProcessorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    execution_order: jsii.Number,
    fallback_action: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04fab589c36890507658f03e0daf5dda656b997e99d4f0f5d449cfb4324279d2(
    *,
    app_instance_arn: builtins.str,
    name: builtins.str,
    processors: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannelFlow.ProcessorProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f68927a594352d4dfb82e54610caae5c2c52baa2dcf7cbb196f93b31a786fed(
    *,
    app_instance_arn: builtins.str,
    chime_bearer: builtins.str,
    name: builtins.str,
    channel_id: typing.Optional[builtins.str] = None,
    elastic_channel_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.ElasticChannelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    expiration_settings: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.ExpirationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    member_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    metadata: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    moderator_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    privacy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889d6d992b8d7ecaa497b89b0969fdfa7fa839fcacf07f58726b49cf8f323d52(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    elements: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty, typing.Dict[builtins.str, typing.Any]]]]],
    media_insights_pipeline_configuration_name: builtins.str,
    resource_access_role_arn: builtins.str,
    real_time_alert_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d947022873d1e6882ae47a189d20b3d7f2aa53c157b7df911c6e8deb1b32e31a(
    resource: _aws_chime_58870695.IMediaInsightsPipelineConfigurationRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc4a193dcd334a33221d899407a55bf4c92b7885da28e3b9f57712ac4e0b6bfd(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffe32f64919fa553c3f22877220b9efb5fbcdcf2ad1ec025355c8a02c6f847c2(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883a85ed849985e75e040b5f613e64f571f44974766f3824019aee35d3eecdfc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c400f356cf18466a3dff483e35943c01e7e22de89435c0c061ebb9510b901ef(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703c89c9d6f653e3380e4187a1fddc6718e6cef2c715047ba16991465db1d4ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5495e3e7636c99bb133b9fe920d64aee710982f4fd245f2c92bb8034ee192b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72716e62afe90194547497ab6f884c0ec05d923704b462976f68d92a5a76f2a(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fa72bce81eb4333c1c1c86d38e36204aef77b68b24d9f3a58023ffe14e0700(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcc5b2f060868f5e44a495cf81d3fbeeebe9d579aabcae3cc02c92e4f318015(
    *,
    language_code: builtins.str,
    call_analytics_stream_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    content_identification_type: typing.Optional[builtins.str] = None,
    content_redaction_type: typing.Optional[builtins.str] = None,
    enable_partial_results_stabilization: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    filter_partial_results: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    language_model_name: typing.Optional[builtins.str] = None,
    partial_results_stability: typing.Optional[builtins.str] = None,
    pii_entity_types: typing.Optional[builtins.str] = None,
    post_call_analytics_settings: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.PostCallAnalyticsSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vocabulary_filter_method: typing.Optional[builtins.str] = None,
    vocabulary_filter_name: typing.Optional[builtins.str] = None,
    vocabulary_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55202693225010e49bacdad3bec7e625d84491c4df67d1192367340ff7385560(
    *,
    content_identification_type: typing.Optional[builtins.str] = None,
    content_redaction_type: typing.Optional[builtins.str] = None,
    enable_partial_results_stabilization: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    filter_partial_results: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    identify_language: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    identify_multiple_languages: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    language_code: typing.Optional[builtins.str] = None,
    language_model_name: typing.Optional[builtins.str] = None,
    language_options: typing.Optional[builtins.str] = None,
    partial_results_stability: typing.Optional[builtins.str] = None,
    pii_entity_types: typing.Optional[builtins.str] = None,
    preferred_language: typing.Optional[builtins.str] = None,
    show_speaker_label: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    vocabulary_filter_method: typing.Optional[builtins.str] = None,
    vocabulary_filter_name: typing.Optional[builtins.str] = None,
    vocabulary_filter_names: typing.Optional[builtins.str] = None,
    vocabulary_name: typing.Optional[builtins.str] = None,
    vocabulary_names: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab8c7535ce89e3bcb112d465f75d85b0285fad63a58b8b26215f096155d80c62(
    *,
    rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a2dae732e141f2e4061d354a319ad3929393a26356474daf8eb6b533ae66cac(
    *,
    keywords: typing.Sequence[builtins.str],
    rule_name: builtins.str,
    negate: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7b26f7516e3f0c94b597c003af93479cb85b1b15e8dbdfdf2dfaa9fd033949(
    *,
    insights_target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ee2b917d23080d4fd427d093f10d15a4b47ba3f834e7d360f29dcc6254db811(
    *,
    type: builtins.str,
    amazon_transcribe_call_analytics_processor_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.AmazonTranscribeCallAnalyticsProcessorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    amazon_transcribe_processor_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.AmazonTranscribeProcessorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_data_stream_sink_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.KinesisDataStreamSinkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_recording_sink_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.S3RecordingSinkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55dd53917f4d820371c3d2de6f1b1b305b775665440acf4e8b26628464786c06(
    *,
    data_access_role_arn: builtins.str,
    output_location: builtins.str,
    content_redaction_output: typing.Optional[builtins.str] = None,
    output_encryption_kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58a5091b81af0969b48eb2cb8c038f94af7be3f100d23e47633ebcfa5075b09(
    *,
    disabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    rules: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.RealTimeAlertRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014418bc181569b08f625dde46ac0798963eb491d4ad04fc180d53234cb2164c(
    *,
    type: builtins.str,
    issue_detection_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.IssueDetectionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    keyword_match_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.KeywordMatchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sentiment_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.SentimentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282a9f6918db78f8c2ba6791400feb36b9c506d6568b739ade819b651c917da5(
    *,
    destination: typing.Optional[builtins.str] = None,
    recording_file_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__433bc2f178f4e21ad76e84ccc78517a72d926ae25aba59dc382a92cb7e86654f(
    *,
    rule_name: builtins.str,
    sentiment_type: builtins.str,
    time_period: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5edcf05aa706b7cb6499c317d5a3073fbd8b8e091f593c38e6cbbcd4e4b4835(
    *,
    elements: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.MediaInsightsPipelineConfigurationElementProperty, typing.Dict[builtins.str, typing.Any]]]]],
    media_insights_pipeline_configuration_name: builtins.str,
    resource_access_role_arn: builtins.str,
    real_time_alert_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaInsightsPipelineConfiguration.RealTimeAlertConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b336d9205da99d4437e13b57fe31566b7bcddbad8a4aca01118d6e9af2e64130(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    pool_name: builtins.str,
    stream_configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32690cfe6167486a6bc73ee7a4e8b2d72cf2b71f8d044f85f72d01dafc98562b(
    resource: _aws_chime_58870695.IMediaPipelineKinesisVideoStreamPoolRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49dc319dea57d3c17dfa63f2944c37fff0d692bfb0acb6c6a6c8d4849a7fbcae(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb3bc86383838753d4e892b4d5b009b8a4bf3d69ae85b39d6d4a54445fbd219(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__023cb1dbceee8545cd0fb5816a4202d640695b79fc5f31581fab9f0ee4e134ec(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f677f01464018d20d5c629d5a30dfe7b5a353a6f894cee558cd7a079815b3648(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eef490c284885605bd4d9641f9a06d3eda73e2ce6d657b210b0a1f9a297ab7c(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994c1e7aea782a4f5ac4c165542058880ff58e7435841b0f9687daa4baa0d0ed(
    value: typing.Optional[typing.List[CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9180f89bf344bebe3717327b7e726cc5fc7402b806c845d0a7bec90af2aa71a6(
    *,
    region: builtins.str,
    data_retention_in_hours: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__720939a95a92fe53c15ba34c0f539667cb899205f38b3e1f0635deeb6d1ee34b(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a4fb7dfa431fc097a5630ce4858b4dd3da0617dbc59442dd069b385683b9538(
    *,
    pool_name: builtins.str,
    stream_configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMediaPipelineKinesisVideoStreamPool.StreamConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[CfnMediaPipelineKinesisVideoStreamPool.TagsItemsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26eb8c1bc4a1f86978d3246e599a9aa699835a5d089fa644436e38af502db993(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    aws_region: builtins.str,
    endpoints: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSipMediaApplication.SipMediaApplicationEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba0d683650689e2081014db2d6fb9a99607330603aeb24831e1b4435308282a6(
    resource: _aws_chime_58870695.ISipMediaApplicationRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2be69fd45b5d6f37793e1a3c4568d5fefa809a190aa3b6d71debe22da918b05d(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1e3584a84de325a695edf5be77fbe8848ccb44a374d874697fb274c323ed00(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3492a5dbb051d3de8df839802771567711dc67d94bf59796892bbc6bfb37fdf7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2351c8de98c40a4806a6c3430bda1438b5d8da90910f625bff87ae9672466c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d39849434edfc162ba7322548e8f937629a922e919e923822c0d77e54c9544f(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSipMediaApplication.SipMediaApplicationEndpointProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__637cbb29fb24b5f18d6dd14a0acb910eec6b79c40ed43346a0bfef34740a74a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e77d8effaf0cfae22ca3cab05ea8c172429af80efd993b6d6b08b6f7a6e033a(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a21df4d9a86ef098cfa2390c70577cdd058412ed46b6983f7ae3e8d0e64c9c53(
    *,
    lambda_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2d633e5b779a6c367587f51d4100a3e0e2a07b261dd3f0daa879adca38fe54(
    *,
    aws_region: builtins.str,
    endpoints: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSipMediaApplication.SipMediaApplicationEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a25fd89e9de3fb404a08691b4c7ee98e0f077a34dc286b1cfce7f532fc05a2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    require_encryption: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
    aws_region: typing.Optional[builtins.str] = None,
    network_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665d280f8f7569acff61b157dc414017ab7f482e10a00950ec6899957eb17cdf(
    resource: _aws_chime_58870695.IVoiceConnectorRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2ecc4f32023674befc0ccc9379b88b16aae99e14435795fce3c30cb902fae2c(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3977b7652d57b9a0da2fb652c70c5b8445222f780f87d4b34dff3b3a830124e(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0191f5993b709064b78f286535ab05ebb6ffe17837ee9caec0239b04963c4e1e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__787a84d7c3d4d36ba68b8e307c922a0ec73d2389a1a30a84ddc055d72d127ffa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f77946a6da8b6b6475129ab1e18916bd7b6b0329c2b4d16869d6db6e4d5b4f(
    value: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c3900dc2719e0dab876645a1db496658a0424323d8a7781cb0e0d33e57147d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddaa871794b6518dc8bd6140a4ce963a409e289a5f48e907522ad7766dffa252(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__035b14d74fc5c3eb7431fd43c26137270d2039024e8aed2254c225c80aee44b3(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce9a6b502ef05469370c725a4e8275d6f0ef0b0d8135c1376f5871e55058375(
    *,
    name: builtins.str,
    require_encryption: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
    aws_region: typing.Optional[builtins.str] = None,
    network_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
