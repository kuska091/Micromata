r'''
# AWS::EventsV2 Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_eventsv2 as events
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EventsV2 construct libraries](https://constructs.dev/search?q=eventsv2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EventsV2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EventsV2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EventsV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EventsV2.html).

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
    import aws_cdk.interfaces.aws_eventsv2 as _aws_eventsv2_0250e2c5
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_eventsv2_0250e2c5 = _LazyImport("aws_cdk.interfaces.aws_eventsv2")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_eventsv2_0250e2c5.IEventBusRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnEventBus(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventBus",
):
    '''Resource type definition for AWS::EventsV2::EventBus, an Amazon EventBridge custom event bus that receives events and delivers them to matching subscribers.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventbus.html
    :cloudformationResource: AWS::EventsV2::EventBus
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eventsv2 as eventsv2
        
        cfn_event_bus = eventsv2.CfnEventBus(self, "MyCfnEventBus",
            name="name",
        
            # the properties below are optional
            description="description",
            encryption_configuration=eventsv2.CfnEventBus.EncryptionConfigurationProperty(
                kms_key_identifier="kmsKeyIdentifier"
            ),
            storage_configuration=eventsv2.CfnEventBus.StorageConfigurationProperty(
                retention_period_in_days=123
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
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventBus.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        storage_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventBus.StorageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EventsV2::EventBus``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the event bus. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'.
        :param description: A description of the event bus. Control characters and Unicode line separators are not allowed.
        :param encryption_configuration: Encryption configuration for an event bus.
        :param storage_configuration: Storage (retention) configuration for the event bus.
        :param tags: The tags assigned to the event bus.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__73208bd89f76ba584f028d6ce398bcd1482829e2c346de90b3b9d148e7d887b6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventBusProps(
            name=name,
            description=description,
            encryption_configuration=encryption_configuration,
            storage_configuration=storage_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForEventBus")
    @builtins.classmethod
    def arn_for_event_bus(
        cls,
        resource: "_aws_eventsv2_0250e2c5.IEventBusRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b6ca2b227989b44b021f48111b26f0fb74f7b544507dd3e2f3f7d65212dbd7bf)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForEventBus", [resource]))

    @jsii.member(jsii_name="isCfnEventBus")
    @builtins.classmethod
    def is_cfn_event_bus(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnEventBus.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__18ef461863115ad0e9cc454734c7d1ed3affb217d3f2feda0012bdec87b7503d)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnEventBus", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fe8d712056c76d4b6d0ed7a4600e3dbb29dcf3554ceb465b0fe466051bb6c0ef)
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
            type_hints = cached_type_hints(_typecheckingstub__4cf4c0b04ff6a847d12f9151602e9a66ca3517d75f34999ca923b18ae5540ac0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the event bus was created, as an ISO 8601 timestamp.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrEventBusArn")
    def attr_event_bus_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the event bus.

        :cloudformationAttribute: EventBusArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventBusArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''The time the event bus was last modified, as an ISO 8601 timestamp.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The lifecycle state of the event bus.

        The settled operational state is ACTIVE.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="eventBusRef")
    def event_bus_ref(self) -> "_aws_eventsv2_0250e2c5.EventBusReference":
        '''A reference to a EventBus resource.'''
        return typing.cast("_aws_eventsv2_0250e2c5.EventBusReference", jsii.get(self, "eventBusRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the event bus.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ee9ac8b436284a957f1d956f844335a38245bfa0d2c47f6508e873a0cac4a898)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the event bus.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7df16b6417ddf005f3950e2298297d1ebe2b6ed2c71861f56407ad1ec7b0ec1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.EncryptionConfigurationProperty"]]:
        '''Encryption configuration for an event bus.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7a1587ce163ec2a1690136eb81cc89ac5b130f01424c98fe9cffa19ac50c824c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageConfiguration")
    def storage_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.StorageConfigurationProperty"]]:
        '''Storage (retention) configuration for the event bus.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.StorageConfigurationProperty"]], jsii.get(self, "storageConfiguration"))

    @storage_configuration.setter
    def storage_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.StorageConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fc42052cd98bfe53e4c5706d2a05e99640f84231be21e82224d0c890800df8a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the event bus.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__88ed1fa75f370cb15d812650283f3363698cbbb3bff10bd187595246d9876fbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventBus.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_identifier": "kmsKeyIdentifier"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            kms_key_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Encryption configuration for an event bus.

            :param kms_key_identifier: The identifier of the AWS KMS customer managed key that the event bus uses to encrypt events. You can specify the key ARN, key ID, alias name, or alias ARN. If you do not specify a key, EventBridge uses an AWS owned key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventbus-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                encryption_configuration_property = eventsv2.CfnEventBus.EncryptionConfigurationProperty(
                    kms_key_identifier="kmsKeyIdentifier"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__539097163761e51929fa97f8446a4a012832593efa9592d1040cd91ab0e4daf7)
                check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_identifier is not None:
                self._values["kms_key_identifier"] = kms_key_identifier

        @builtins.property
        def kms_key_identifier(self) -> typing.Optional[builtins.str]:
            '''The identifier of the AWS KMS customer managed key that the event bus uses to encrypt events.

            You can specify the key ARN, key ID, alias name, or alias ARN. If you do not specify a key, EventBridge uses an AWS owned key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventbus-encryptionconfiguration.html#cfn-eventsv2-eventbus-encryptionconfiguration-kmskeyidentifier
            '''
            result = self._values.get("kms_key_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventBus.StorageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"retention_period_in_days": "retentionPeriodInDays"},
    )
    class StorageConfigurationProperty:
        def __init__(
            self,
            *,
            retention_period_in_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Storage (retention) configuration for the event bus.

            :param retention_period_in_days: The number of days events are retained on the event bus for replay, 1-365.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventbus-storageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                storage_configuration_property = eventsv2.CfnEventBus.StorageConfigurationProperty(
                    retention_period_in_days=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__5ace5f3dc47d717e1fe4bc56f1be7fa2773a2ad721e0d1e5df27b1aa0cf98659)
                check_type(argname="argument retention_period_in_days", value=retention_period_in_days, expected_type=type_hints["retention_period_in_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if retention_period_in_days is not None:
                self._values["retention_period_in_days"] = retention_period_in_days

        @builtins.property
        def retention_period_in_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days events are retained on the event bus for replay, 1-365.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventbus-storageconfiguration.html#cfn-eventsv2-eventbus-storageconfiguration-retentionperiodindays
            '''
            result = self._values.get("retention_period_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventBusProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "encryption_configuration": "encryptionConfiguration",
        "storage_configuration": "storageConfiguration",
        "tags": "tags",
    },
)
class CfnEventBusProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventBus.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        storage_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventBus.StorageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventBus``.

        :param name: The name of the event bus. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'.
        :param description: A description of the event bus. Control characters and Unicode line separators are not allowed.
        :param encryption_configuration: Encryption configuration for an event bus.
        :param storage_configuration: Storage (retention) configuration for the event bus.
        :param tags: The tags assigned to the event bus.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventbus.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eventsv2 as eventsv2
            
            cfn_event_bus_props = eventsv2.CfnEventBusProps(
                name="name",
            
                # the properties below are optional
                description="description",
                encryption_configuration=eventsv2.CfnEventBus.EncryptionConfigurationProperty(
                    kms_key_identifier="kmsKeyIdentifier"
                ),
                storage_configuration=eventsv2.CfnEventBus.StorageConfigurationProperty(
                    retention_period_in_days=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__78fdefbe04da2f08db27daec43937bf27dd1f25d496457662f45c552c033f709)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument storage_configuration", value=storage_configuration, expected_type=type_hints["storage_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if storage_configuration is not None:
            self._values["storage_configuration"] = storage_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the event bus.

        The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventbus.html#cfn-eventsv2-eventbus-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the event bus.

        Control characters and Unicode line separators are not allowed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventbus.html#cfn-eventsv2-eventbus-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.EncryptionConfigurationProperty"]]:
        '''Encryption configuration for an event bus.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventbus.html#cfn-eventsv2-eventbus-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.EncryptionConfigurationProperty"]], result)

    @builtins.property
    def storage_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.StorageConfigurationProperty"]]:
        '''Storage (retention) configuration for the event bus.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventbus.html#cfn-eventsv2-eventbus-storageconfiguration
        '''
        result = self._values.get("storage_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventBus.StorageConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the event bus.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventbus.html#cfn-eventsv2-eventbus-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventBusProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_eventsv2_0250e2c5.IEventSourceRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnEventSource(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventSource",
):
    '''Resource schema for AWS::EventsV2::EventSource.

    A managed event source that forwards AWS service events or partner events onto a custom event bus.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventsource.html
    :cloudformationResource: AWS::EventsV2::EventSource
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eventsv2 as eventsv2
        
        cfn_event_source = eventsv2.CfnEventSource(self, "MyCfnEventSource",
            configuration=eventsv2.CfnEventSource.EventSourceConfigurationProperty(
                aws_service_events_configuration=eventsv2.CfnEventSource.AwsServiceEventsConfigurationProperty(
                    aws_service="awsService",
        
                    # the properties below are optional
                    on_failure_configuration=eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                        arn="arn"
                    ),
                    pattern="pattern"
                ),
                partner_events_configuration=eventsv2.CfnEventSource.PartnerEventsConfigurationProperty(
                    partner_event_source_arn="partnerEventSourceArn",
        
                    # the properties below are optional
                    on_failure_configuration=eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                        arn="arn"
                    ),
                    partner_bus_kms_key_identifier="partnerBusKmsKeyIdentifier",
                    pattern="pattern"
                )
            ),
            event_bus_arn="eventBusArn",
            name="name",
        
            # the properties below are optional
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
        configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventSource.EventSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        event_bus_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EventsV2::EventSource``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: Event source configuration. Exactly one of the two variants must be set.
        :param event_bus_arn: The ARN of the custom event bus the event source forwards onto.
        :param name: The name of the event source. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'. Names cannot begin with the reserved aws. prefix.
        :param description: A description of the event source. Control characters and Unicode line separators are not allowed.
        :param tags: The tags assigned to the event source.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__19ea3c2714b4bbb1b5c119c2fab9bb5c845575f8931b3a89abe1991f798f928b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventSourceProps(
            configuration=configuration,
            event_bus_arn=event_bus_arn,
            name=name,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForEventSource")
    @builtins.classmethod
    def arn_for_event_source(
        cls,
        resource: "_aws_eventsv2_0250e2c5.IEventSourceRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c9194c78bb4c32f7d83b27233159f2ea9d9c434371018442411a5cad4b690250)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForEventSource", [resource]))

    @jsii.member(jsii_name="isCfnEventSource")
    @builtins.classmethod
    def is_cfn_event_source(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnEventSource.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__773f2f1226ca2c8cc12d87d026858d00d0c6aa6594d505e3f58a027e92ec1507)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnEventSource", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__72863d3a7247be261ec897a3e4ff4e32e657ba96be66bcd1ceafc6bbe2f27ff6)
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
            type_hints = cached_type_hints(_typecheckingstub__99d3b9477f1dd3faa028535c642f0fe38c7fcd4b8defae73474bf0c1efae5ed0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the event source was created, as an ISO 8601 timestamp.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrEventSourceArn")
    def attr_event_source_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the event source.

        Its resource segment has the form event-sourcev2///. The type segment is set by the service (aws.service for AWS service events, aws.partner for partner events) and is not part of the event source name. The id segment is a 25-character identifier generated by the service.

        :cloudformationAttribute: EventSourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventSourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''The time the event source was last modified, as an ISO 8601 timestamp.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrRevoked")
    def attr_revoked(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''Whether the event bus owner has revoked this event source.

        Revocation is permanent: a revoked event source cannot be updated, but it can be deleted.

        :cloudformationAttribute: Revoked
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrRevoked"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The lifecycle state of the event source: CREATING, ACTIVE, UPDATING, CREATE_FAILED, UPDATE_FAILED, DELETING, or DELETE_FAILED.

        Revocation by the event bus owner is reported by the Revoked property, not by the state.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="eventSourceRef")
    def event_source_ref(self) -> "_aws_eventsv2_0250e2c5.EventSourceReference":
        '''A reference to a EventSource resource.'''
        return typing.cast("_aws_eventsv2_0250e2c5.EventSourceReference", jsii.get(self, "eventSourceRef"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.EventSourceConfigurationProperty"]:
        '''Event source configuration.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.EventSourceConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.EventSourceConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9c0002932c84a252c296e10e872e5fa5abf135d0e4984dca9be5082e00c13e5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventBusArn")
    def event_bus_arn(self) -> builtins.str:
        '''The ARN of the custom event bus the event source forwards onto.'''
        return typing.cast(builtins.str, jsii.get(self, "eventBusArn"))

    @event_bus_arn.setter
    def event_bus_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8d564d56b64810b9021d7445571c5638763974b5383ed5587190ac200f4d573a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBusArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the event source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2d6c8780caa2a0ffb779a7016735274f6123fb5da20a53ba8a93448bb0787224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the event source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7bfe70eadeea68822e462ab5cf2a07af053d7db9970b9f203fd623a1d7ab9124)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the event source.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6f880032e0ea2a6bf89a92521abfc144ac2ee6a1f69595b51d0dcfea3769e3ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventSource.AwsServiceEventsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_service": "awsService",
            "on_failure_configuration": "onFailureConfiguration",
            "pattern": "pattern",
        },
    )
    class AwsServiceEventsConfigurationProperty:
        def __init__(
            self,
            *,
            aws_service: builtins.str,
            on_failure_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventSource.OnFailureConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            pattern: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Forward a single AWS service's events from the account's default event bus.

            :param aws_service: A single AWS service source identifier, for example aws.s3. Wildcards and lists are not allowed.
            :param on_failure_configuration: The destination for events that could not be forwarded by the managed forwarding target or, for partner event sources, the managed partner event bus. Arn is optional. An empty object removes a configured destination on update.
            :param pattern: A filter pattern, as a JSON string, that defines which events from the specified AWS service are forwarded to the event bus. Do not include source, account, or region as top-level fields. If you do not specify a pattern, all events from the service are forwarded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                aws_service_events_configuration_property = eventsv2.CfnEventSource.AwsServiceEventsConfigurationProperty(
                    aws_service="awsService",
                
                    # the properties below are optional
                    on_failure_configuration=eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                        arn="arn"
                    ),
                    pattern="pattern"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ddedc661fee98c57d3f869532a27aec50c8b6bdaff873088c95159c9866ef533)
                check_type(argname="argument aws_service", value=aws_service, expected_type=type_hints["aws_service"])
                check_type(argname="argument on_failure_configuration", value=on_failure_configuration, expected_type=type_hints["on_failure_configuration"])
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_service": aws_service,
            }
            if on_failure_configuration is not None:
                self._values["on_failure_configuration"] = on_failure_configuration
            if pattern is not None:
                self._values["pattern"] = pattern

        @builtins.property
        def aws_service(self) -> builtins.str:
            '''A single AWS service source identifier, for example aws.s3. Wildcards and lists are not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration.html#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-awsservice
            '''
            result = self._values.get("aws_service")
            assert result is not None, "Required property 'aws_service' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def on_failure_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.OnFailureConfigurationProperty"]]:
            '''The destination for events that could not be forwarded by the managed forwarding target or, for partner event sources, the managed partner event bus.

            Arn is optional. An empty object removes a configured destination on update.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration.html#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-onfailureconfiguration
            '''
            result = self._values.get("on_failure_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.OnFailureConfigurationProperty"]], result)

        @builtins.property
        def pattern(self) -> typing.Optional[builtins.str]:
            '''A filter pattern, as a JSON string, that defines which events from the specified AWS service are forwarded to the event bus.

            Do not include source, account, or region as top-level fields. If you do not specify a pattern, all events from the service are forwarded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration.html#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-pattern
            '''
            result = self._values.get("pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsServiceEventsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventSource.EventSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_service_events_configuration": "awsServiceEventsConfiguration",
            "partner_events_configuration": "partnerEventsConfiguration",
        },
    )
    class EventSourceConfigurationProperty:
        def __init__(
            self,
            *,
            aws_service_events_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventSource.AwsServiceEventsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            partner_events_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventSource.PartnerEventsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Event source configuration.

            Exactly one of the two variants must be set.

            :param aws_service_events_configuration: Forward a single AWS service's events from the account's default event bus.
            :param partner_events_configuration: Forward a partner event source's events through a managed partner event bus.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-eventsourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                event_source_configuration_property = eventsv2.CfnEventSource.EventSourceConfigurationProperty(
                    aws_service_events_configuration=eventsv2.CfnEventSource.AwsServiceEventsConfigurationProperty(
                        aws_service="awsService",
                
                        # the properties below are optional
                        on_failure_configuration=eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                            arn="arn"
                        ),
                        pattern="pattern"
                    ),
                    partner_events_configuration=eventsv2.CfnEventSource.PartnerEventsConfigurationProperty(
                        partner_event_source_arn="partnerEventSourceArn",
                
                        # the properties below are optional
                        on_failure_configuration=eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                            arn="arn"
                        ),
                        partner_bus_kms_key_identifier="partnerBusKmsKeyIdentifier",
                        pattern="pattern"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__db65cd2375229e5c755606bdc958c9a287941eba06fcaa2eaa39188dbbef67dc)
                check_type(argname="argument aws_service_events_configuration", value=aws_service_events_configuration, expected_type=type_hints["aws_service_events_configuration"])
                check_type(argname="argument partner_events_configuration", value=partner_events_configuration, expected_type=type_hints["partner_events_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_service_events_configuration is not None:
                self._values["aws_service_events_configuration"] = aws_service_events_configuration
            if partner_events_configuration is not None:
                self._values["partner_events_configuration"] = partner_events_configuration

        @builtins.property
        def aws_service_events_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.AwsServiceEventsConfigurationProperty"]]:
            '''Forward a single AWS service's events from the account's default event bus.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-eventsourceconfiguration.html#cfn-eventsv2-eventsource-eventsourceconfiguration-awsserviceeventsconfiguration
            '''
            result = self._values.get("aws_service_events_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.AwsServiceEventsConfigurationProperty"]], result)

        @builtins.property
        def partner_events_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.PartnerEventsConfigurationProperty"]]:
            '''Forward a partner event source's events through a managed partner event bus.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-eventsourceconfiguration.html#cfn-eventsv2-eventsource-eventsourceconfiguration-partnereventsconfiguration
            '''
            result = self._values.get("partner_events_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.PartnerEventsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventSource.OnFailureConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class OnFailureConfigurationProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''The destination for events that could not be forwarded by the managed forwarding target or, for partner event sources, the managed partner event bus.

            Arn is optional. An empty object removes a configured destination on update.

            :param arn: The ARN of the Amazon SQS standard queue that receives events that could not be forwarded. FIFO queues are not supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-onfailureconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                on_failure_configuration_property = eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1cefd71b3eb3dccdf506b40744a767b5c7a852681abc8dc62fb33c632fe4179c)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Amazon SQS standard queue that receives events that could not be forwarded.

            FIFO queues are not supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-onfailureconfiguration.html#cfn-eventsv2-eventsource-onfailureconfiguration-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnFailureConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventSource.PartnerEventsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "partner_event_source_arn": "partnerEventSourceArn",
            "on_failure_configuration": "onFailureConfiguration",
            "partner_bus_kms_key_identifier": "partnerBusKmsKeyIdentifier",
            "pattern": "pattern",
        },
    )
    class PartnerEventsConfigurationProperty:
        def __init__(
            self,
            *,
            partner_event_source_arn: builtins.str,
            on_failure_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventSource.OnFailureConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            partner_bus_kms_key_identifier: typing.Optional[builtins.str] = None,
            pattern: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Forward a partner event source's events through a managed partner event bus.

            :param partner_event_source_arn: The ARN of the partner event source to forward. The partner owns the event source, so the ARN's account segment is empty. Changing this property replaces the event source. Because Name and EventBusArn together identify an event source, and the replacement is created before the old resource is deleted, change Name in the same update.
            :param on_failure_configuration: The destination for events that could not be forwarded by the managed forwarding target or, for partner event sources, the managed partner event bus. Arn is optional. An empty object removes a configured destination on update.
            :param partner_bus_kms_key_identifier: The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt events on the managed partner event bus. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN. If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt events on the event bus.
            :param pattern: A filter pattern, as a JSON string, that defines which events from the specified partner event source are forwarded to the event bus. If you do not specify a pattern, all events from the partner event source are forwarded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-partnereventsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                partner_events_configuration_property = eventsv2.CfnEventSource.PartnerEventsConfigurationProperty(
                    partner_event_source_arn="partnerEventSourceArn",
                
                    # the properties below are optional
                    on_failure_configuration=eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                        arn="arn"
                    ),
                    partner_bus_kms_key_identifier="partnerBusKmsKeyIdentifier",
                    pattern="pattern"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__815d9cedb6ba6bf56a9403e4fa03859f4947792a8a7fb051a3e9b7e56de91e4b)
                check_type(argname="argument partner_event_source_arn", value=partner_event_source_arn, expected_type=type_hints["partner_event_source_arn"])
                check_type(argname="argument on_failure_configuration", value=on_failure_configuration, expected_type=type_hints["on_failure_configuration"])
                check_type(argname="argument partner_bus_kms_key_identifier", value=partner_bus_kms_key_identifier, expected_type=type_hints["partner_bus_kms_key_identifier"])
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "partner_event_source_arn": partner_event_source_arn,
            }
            if on_failure_configuration is not None:
                self._values["on_failure_configuration"] = on_failure_configuration
            if partner_bus_kms_key_identifier is not None:
                self._values["partner_bus_kms_key_identifier"] = partner_bus_kms_key_identifier
            if pattern is not None:
                self._values["pattern"] = pattern

        @builtins.property
        def partner_event_source_arn(self) -> builtins.str:
            '''The ARN of the partner event source to forward.

            The partner owns the event source, so the ARN's account segment is empty. Changing this property replaces the event source. Because Name and EventBusArn together identify an event source, and the replacement is created before the old resource is deleted, change Name in the same update.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-partnereventsconfiguration.html#cfn-eventsv2-eventsource-partnereventsconfiguration-partnereventsourcearn
            '''
            result = self._values.get("partner_event_source_arn")
            assert result is not None, "Required property 'partner_event_source_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def on_failure_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.OnFailureConfigurationProperty"]]:
            '''The destination for events that could not be forwarded by the managed forwarding target or, for partner event sources, the managed partner event bus.

            Arn is optional. An empty object removes a configured destination on update.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-partnereventsconfiguration.html#cfn-eventsv2-eventsource-partnereventsconfiguration-onfailureconfiguration
            '''
            result = self._values.get("on_failure_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.OnFailureConfigurationProperty"]], result)

        @builtins.property
        def partner_bus_kms_key_identifier(self) -> typing.Optional[builtins.str]:
            '''The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt events on the managed partner event bus.

            The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN. If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt events on the event bus.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-partnereventsconfiguration.html#cfn-eventsv2-eventsource-partnereventsconfiguration-partnerbuskmskeyidentifier
            '''
            result = self._values.get("partner_bus_kms_key_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pattern(self) -> typing.Optional[builtins.str]:
            '''A filter pattern, as a JSON string, that defines which events from the specified partner event source are forwarded to the event bus.

            If you do not specify a pattern, all events from the partner event source are forwarded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-eventsource-partnereventsconfiguration.html#cfn-eventsv2-eventsource-partnereventsconfiguration-pattern
            '''
            result = self._values.get("pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PartnerEventsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eventsv2.CfnEventSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "event_bus_arn": "eventBusArn",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnEventSourceProps:
    def __init__(
        self,
        *,
        configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventSource.EventSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        event_bus_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventSource``.

        :param configuration: Event source configuration. Exactly one of the two variants must be set.
        :param event_bus_arn: The ARN of the custom event bus the event source forwards onto.
        :param name: The name of the event source. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'. Names cannot begin with the reserved aws. prefix.
        :param description: A description of the event source. Control characters and Unicode line separators are not allowed.
        :param tags: The tags assigned to the event source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventsource.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eventsv2 as eventsv2
            
            cfn_event_source_props = eventsv2.CfnEventSourceProps(
                configuration=eventsv2.CfnEventSource.EventSourceConfigurationProperty(
                    aws_service_events_configuration=eventsv2.CfnEventSource.AwsServiceEventsConfigurationProperty(
                        aws_service="awsService",
            
                        # the properties below are optional
                        on_failure_configuration=eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                            arn="arn"
                        ),
                        pattern="pattern"
                    ),
                    partner_events_configuration=eventsv2.CfnEventSource.PartnerEventsConfigurationProperty(
                        partner_event_source_arn="partnerEventSourceArn",
            
                        # the properties below are optional
                        on_failure_configuration=eventsv2.CfnEventSource.OnFailureConfigurationProperty(
                            arn="arn"
                        ),
                        partner_bus_kms_key_identifier="partnerBusKmsKeyIdentifier",
                        pattern="pattern"
                    )
                ),
                event_bus_arn="eventBusArn",
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__35ed838f2373b14d074fe18d883bc57c6be6a876f0c0e40543f9fc58c428122a)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument event_bus_arn", value=event_bus_arn, expected_type=type_hints["event_bus_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "event_bus_arn": event_bus_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.EventSourceConfigurationProperty"]:
        '''Event source configuration.

        Exactly one of the two variants must be set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventsource.html#cfn-eventsv2-eventsource-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventSource.EventSourceConfigurationProperty"], result)

    @builtins.property
    def event_bus_arn(self) -> builtins.str:
        '''The ARN of the custom event bus the event source forwards onto.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventsource.html#cfn-eventsv2-eventsource-eventbusarn
        '''
        result = self._values.get("event_bus_arn")
        assert result is not None, "Required property 'event_bus_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the event source.

        The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'. Names cannot begin with the reserved aws. prefix.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventsource.html#cfn-eventsv2-eventsource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the event source.

        Control characters and Unicode line separators are not allowed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventsource.html#cfn-eventsv2-eventsource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the event source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-eventsource.html#cfn-eventsv2-eventsource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_eventsv2_0250e2c5.IResourcePolicyRef)
class CfnResourcePolicy(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eventsv2.CfnResourcePolicy",
):
    '''Resource type definition for AWS::EventsV2::ResourcePolicy, the resource policy of an Amazon EventBridge event bus.

    This manages only the resource policy named "default", which the bus owner writes. It does not manage the policy named "AWS_RAM", which AWS Resource Access Manager owns on behalf of the bus owner. If the bus already has a default policy, creating this resource fails. Deleting this resource removes all permissions granted by it. An explicit Deny in this policy takes precedence over an Allow in the "AWS_RAM" policy, so deleting this resource can widen access. Set DeletionPolicy: Retain if the policy carries a Deny that you rely on. Required permissions: events:PutResourcePolicy, events:GetResourcePolicy, and events:DeleteResourcePolicy. Listing resources of this type also requires events:ListEventBuses and events:ListResourcePolicies.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-resourcepolicy.html
    :cloudformationResource: AWS::EventsV2::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eventsv2 as eventsv2
        
        # policy_document: Any
        
        cfn_resource_policy = eventsv2.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            event_bus_arn="eventBusArn",
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        event_bus_arn: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''Create a new ``AWS::EventsV2::ResourcePolicy``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param event_bus_arn: The Amazon Resource Name (ARN) of the event bus whose resource policy this is. The bus must already exist. This resource does not create it.
        :param policy_document: The resource policy document, as a JSON object. The document can be up to 20 KB. This quota is adjustable. An empty object is not a valid policy. To remove the policy, delete this resource. The principals in the document must exist and be visible to the service when the policy is written. When you create a new IAM role or user, that principal might not be immediately visible to the service. You might need to enforce a delay before you include it in the document. For more information, see "Changes that I make are not always immediately visible" in the IAM User Guide. Declare Version. Write AWS account and role principals as ARNs rather than as account IDs. Write a single Action, Resource, or principal value as a scalar rather than as a one-element list. The service returns these forms as you wrote them. It normalizes other forms, and a normalized value can appear as drift. A stack update replaces the whole policy with this document, including any change made outside CloudFormation. For more information about event bus resource policies, see the Amazon EventBridge User Guide.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__300cddccc13b1d85bc424fda9f26893846f54c90eba86ea09b2a26250039795f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(
            event_bus_arn=event_bus_arn, policy_document=policy_document
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnResourcePolicy")
    @builtins.classmethod
    def is_cfn_resource_policy(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnResourcePolicy.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6a1d8a2f5f4b9aa404ff515bb13df7667b5ce396a65aa13988c137440c9c3319)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnResourcePolicy", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__297832e93744970db77ecbe5bc0ddcb28e3f6f912689cb8dc8bbf336ec42cd51)
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
            type_hints = cached_type_hints(_typecheckingstub__5dca0a59ed62e2c169717fa5440c7d942a86dab2f141f2663aaaae87bdbea993)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRevisionId")
    def attr_revision_id(self) -> builtins.str:
        '''The revision identifier the service assigned to the stored policy.

        The identifier changes on every successful write.

        :cloudformationAttribute: RevisionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRevisionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "_aws_eventsv2_0250e2c5.ResourcePolicyReference":
        '''A reference to a ResourcePolicy resource.'''
        return typing.cast("_aws_eventsv2_0250e2c5.ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

    @builtins.property
    @jsii.member(jsii_name="eventBusArn")
    def event_bus_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the event bus whose resource policy this is.'''
        return typing.cast(builtins.str, jsii.get(self, "eventBusArn"))

    @event_bus_arn.setter
    def event_bus_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ad236f15451341d60d13dd82d2e4d162f902f0bd8908b8b4858d3dbc5b8892cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBusArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The resource policy document, as a JSON object.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__72321d83da7c7a058cee5f887d58a2593886e141b1e3893abd2f0dee518d2df7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eventsv2.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"event_bus_arn": "eventBusArn", "policy_document": "policyDocument"},
)
class CfnResourcePolicyProps:
    def __init__(
        self,
        *,
        event_bus_arn: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param event_bus_arn: The Amazon Resource Name (ARN) of the event bus whose resource policy this is. The bus must already exist. This resource does not create it.
        :param policy_document: The resource policy document, as a JSON object. The document can be up to 20 KB. This quota is adjustable. An empty object is not a valid policy. To remove the policy, delete this resource. The principals in the document must exist and be visible to the service when the policy is written. When you create a new IAM role or user, that principal might not be immediately visible to the service. You might need to enforce a delay before you include it in the document. For more information, see "Changes that I make are not always immediately visible" in the IAM User Guide. Declare Version. Write AWS account and role principals as ARNs rather than as account IDs. Write a single Action, Resource, or principal value as a scalar rather than as a one-element list. The service returns these forms as you wrote them. It normalizes other forms, and a normalized value can appear as drift. A stack update replaces the whole policy with this document, including any change made outside CloudFormation. For more information about event bus resource policies, see the Amazon EventBridge User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eventsv2 as eventsv2
            
            # policy_document: Any
            
            cfn_resource_policy_props = eventsv2.CfnResourcePolicyProps(
                event_bus_arn="eventBusArn",
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3a0ef7aad9ea56efd1b9f9ff3e9ca252fccbe507f5e1b910ce0f646ae9f0bf38)
            check_type(argname="argument event_bus_arn", value=event_bus_arn, expected_type=type_hints["event_bus_arn"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bus_arn": event_bus_arn,
            "policy_document": policy_document,
        }

    @builtins.property
    def event_bus_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the event bus whose resource policy this is.

        The bus must already exist. This resource does not create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-resourcepolicy.html#cfn-eventsv2-resourcepolicy-eventbusarn
        '''
        result = self._values.get("event_bus_arn")
        assert result is not None, "Required property 'event_bus_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The resource policy document, as a JSON object.

        The document can be up to 20 KB. This quota is adjustable. An empty object is not a valid policy. To remove the policy, delete this resource. The principals in the document must exist and be visible to the service when the policy is written. When you create a new IAM role or user, that principal might not be immediately visible to the service. You might need to enforce a delay before you include it in the document. For more information, see "Changes that I make are not always immediately visible" in the IAM User Guide. Declare Version. Write AWS account and role principals as ARNs rather than as account IDs. Write a single Action, Resource, or principal value as a scalar rather than as a one-element list. The service returns these forms as you wrote them. It normalizes other forms, and a normalized value can appear as drift. A stack update replaces the whole policy with this document, including any change made outside CloudFormation. For more information about event bus resource policies, see the Amazon EventBridge User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-resourcepolicy.html#cfn-eventsv2-resourcepolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_eventsv2_0250e2c5.ISubscriberRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnSubscriber(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber",
):
    '''Resource type definition for AWS::EventsV2::Subscriber, an Amazon EventBridge subscription that delivers events from an event bus to a target.

    Canonical identity is the combination of bus, name, and target. Replacement uses delete_then_create.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html
    :cloudformationResource: AWS::EventsV2::Subscriber
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eventsv2 as eventsv2
        
        cfn_subscriber = eventsv2.CfnSubscriber(self, "MyCfnSubscriber",
            event_bus_arn="eventBusArn",
            name="name",
        
            # the properties below are optional
            batch_configuration=eventsv2.CfnSubscriber.BatchConfigurationProperty(
                max_batch_size=123,
                max_batch_window_in_seconds=123
            ),
            description="description",
            filter_configuration=eventsv2.CfnSubscriber.FilterConfigurationProperty(
                filters=[eventsv2.CfnSubscriber.FilterProperty(
                    pattern="pattern",
                    scope="scope"
                )],
        
                # the properties below are optional
                language="language"
            ),
            log_configuration=eventsv2.CfnSubscriber.LogConfigurationProperty(
                include_payload="includePayload",
                level="level"
            ),
            on_failure_configuration=eventsv2.CfnSubscriber.OnFailureConfigurationProperty(
                arn="arn"
            ),
            point_in_time_configuration=eventsv2.CfnSubscriber.PointInTimeConfigurationProperty(
                point_type="pointType",
        
                # the properties below are optional
                end_point=123,
                starting_point=123
            ),
            resume_position="resumePosition",
            retry_policy=eventsv2.CfnSubscriber.RetryPolicyProperty(
                max_event_age_in_seconds=123,
                max_retry_attempts=123,
                retry_strategy="retryStrategy"
            ),
            starting_position="startingPosition",
            state="state",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            transformer=eventsv2.CfnSubscriber.TransformerProperty(
                jsonata_configuration=eventsv2.CfnSubscriber.JsonataConfigurationProperty(
                    expression="expression"
                ),
                type="type"
            ),
            type="type"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        event_bus_arn: builtins.str,
        name: builtins.str,
        batch_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.BatchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        filter_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.FilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        on_failure_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.OnFailureConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        point_in_time_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.PointInTimeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        resume_position: typing.Optional[builtins.str] = None,
        retry_policy: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.RetryPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        starting_position: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        transformer: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.TransformerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::EventsV2::Subscriber``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param event_bus_arn: The ARN of the event bus this subscriber belongs to.
        :param name: The name of the subscriber. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'.
        :param batch_configuration: Configuration for batching events into a single delivery.
        :param description: A description of the subscriber. Control characters and Unicode line separators are not allowed.
        :param filter_configuration: Configuration for filtering which events are delivered to the target. An event must match every filter to be delivered.
        :param log_configuration: Delivery logging configuration.
        :param on_failure_configuration: The destination for events that could not be delivered.
        :param point_in_time_configuration: The point in time to start delivering events from, used when StartingPosition is POINT_IN_TIME.
        :param resume_position: Resume-time control, never returned by the service. Applied only when an update transitions State from STOPPED to RUNNING: LAST_PROCESSED (default) resumes from the last processed event, LATEST skips to the newest. Ignored on create and on any update that does not perform that transition.
        :param retry_policy: The retry policy for failed deliveries.
        :param starting_position: Where the subscriber starts reading events: LATEST starts from the newest events; POINT_IN_TIME starts from the point specified in PointInTimeConfiguration.
        :param state: The run state of the subscriber. Events are delivered only while the state is RUNNING. Setting the state to STOPPED pauses delivery. When an update sets a stopped subscriber back to RUNNING, ResumePosition controls where delivery resumes.
        :param tags: The tags assigned to the subscriber.
        :param transformer: Configuration for transforming events before delivery: the raw payload, the payload with its metadata envelope, or the output of a JSONata expression.
        :param type: The delivery ordering mode of the subscriber. FIFO delivers events in order within an event group; UNORDERED delivers without an ordering guarantee.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__05eeedb290d1b08bfcdffd50d6a079078b77f0cf13828494b2822574ca1fd9cd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriberProps(
            event_bus_arn=event_bus_arn,
            name=name,
            batch_configuration=batch_configuration,
            description=description,
            filter_configuration=filter_configuration,
            log_configuration=log_configuration,
            on_failure_configuration=on_failure_configuration,
            point_in_time_configuration=point_in_time_configuration,
            resume_position=resume_position,
            retry_policy=retry_policy,
            starting_position=starting_position,
            state=state,
            tags=tags,
            transformer=transformer,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSubscriber")
    @builtins.classmethod
    def arn_for_subscriber(
        cls,
        resource: "_aws_eventsv2_0250e2c5.ISubscriberRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__73ff9aac1bf58379ec1df238773d941b43e91faccc9251c33a4a4b800b17bbbd)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSubscriber", [resource]))

    @jsii.member(jsii_name="isCfnSubscriber")
    @builtins.classmethod
    def is_cfn_subscriber(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSubscriber.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__377f43b61bd91be8c6e944c7f6b95813e6f2ba02534fc94acd535f370caa3ebe)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSubscriber", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__155ca594f4a12614dcd639a0037d20cc622aebd08cb2efd23130d8dad0fd5900)
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
            type_hints = cached_type_hints(_typecheckingstub__38c14032b6049c2e80ab3ca2f3423cc2d7ba78d02d5b3c3e994d5cf49fde4ce9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBusName")
    def attr_bus_name(self) -> builtins.str:
        '''The name of the event bus this subscriber belongs to.

        This property is read-only.

        :cloudformationAttribute: BusName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBusName"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''Creation timestamp (ISO-8601), read-only.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''Last-modification timestamp (ISO-8601), read-only.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrSubscriberArn")
    def attr_subscriber_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the subscriber.

        :cloudformationAttribute: SubscriberArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSubscriberArn"))

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
    @jsii.member(jsii_name="subscriberRef")
    def subscriber_ref(self) -> "_aws_eventsv2_0250e2c5.SubscriberReference":
        '''A reference to a Subscriber resource.'''
        return typing.cast("_aws_eventsv2_0250e2c5.SubscriberReference", jsii.get(self, "subscriberRef"))

    @builtins.property
    @jsii.member(jsii_name="eventBusArn")
    def event_bus_arn(self) -> builtins.str:
        '''The ARN of the event bus this subscriber belongs to.'''
        return typing.cast(builtins.str, jsii.get(self, "eventBusArn"))

    @event_bus_arn.setter
    def event_bus_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3933a6bedc3ebda376667b88f5aff39872b63d4f4cc267377f0ce24146444149)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBusArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the subscriber.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__87904eb3d4c136da852fa2f79014380c4a8e213f434e3ca7df4a95969dbba534)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="batchConfiguration")
    def batch_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.BatchConfigurationProperty"]]:
        '''Configuration for batching events into a single delivery.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.BatchConfigurationProperty"]], jsii.get(self, "batchConfiguration"))

    @batch_configuration.setter
    def batch_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.BatchConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4e9053b06fb8b200688b5dedefd3ba0608cdc0faadf89ec23b8d5ae6a581297e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the subscriber.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1d72dec88e45963d45b13efedcf6c93e95289752c135f4912ba07db0e94bfb10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.FilterConfigurationProperty"]]:
        '''Configuration for filtering which events are delivered to the target.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.FilterConfigurationProperty"]], jsii.get(self, "filterConfiguration"))

    @filter_configuration.setter
    def filter_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.FilterConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6556d4defc8819b1d1fd5d44b772ba7336f8d8ac3f7199cd9243dd8626324d8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.LogConfigurationProperty"]]:
        '''Delivery logging configuration.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.LogConfigurationProperty"]], jsii.get(self, "logConfiguration"))

    @log_configuration.setter
    def log_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.LogConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3e436742c5ebe5420abdab660baf82f0d4727a9c0a1ad77992e1ec3bc27b005e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="onFailureConfiguration")
    def on_failure_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.OnFailureConfigurationProperty"]]:
        '''The destination for events that could not be delivered.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.OnFailureConfigurationProperty"]], jsii.get(self, "onFailureConfiguration"))

    @on_failure_configuration.setter
    def on_failure_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.OnFailureConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__346b06bebd51f3c10e212119be182d6411b38595d52f541084cbf66b6d6947c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onFailureConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pointInTimeConfiguration")
    def point_in_time_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.PointInTimeConfigurationProperty"]]:
        '''The point in time to start delivering events from, used when StartingPosition is POINT_IN_TIME.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.PointInTimeConfigurationProperty"]], jsii.get(self, "pointInTimeConfiguration"))

    @point_in_time_configuration.setter
    def point_in_time_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.PointInTimeConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3c3a4b0a55ccbc09e680639c37389e152fc2a68249d30b23fb7bf1f8502116d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pointInTimeConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resumePosition")
    def resume_position(self) -> typing.Optional[builtins.str]:
        '''Resume-time control, never returned by the service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resumePosition"))

    @resume_position.setter
    def resume_position(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3b1a6aa60908c077debd64afa6b695d61a4a0244544cfb3471664671dc39b01e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resumePosition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.RetryPolicyProperty"]]:
        '''The retry policy for failed deliveries.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.RetryPolicyProperty"]], jsii.get(self, "retryPolicy"))

    @retry_policy.setter
    def retry_policy(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.RetryPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b6288cda489031a5be2eb50bf47b6782e46ab8d4a9940cb162abd728b474a6f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="startingPosition")
    def starting_position(self) -> typing.Optional[builtins.str]:
        '''Where the subscriber starts reading events: LATEST starts from the newest events;'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startingPosition"))

    @starting_position.setter
    def starting_position(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7a8523d5487330fd3418214fa760d6b5418285dea76accbc0da7b6b896d7f44e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startingPosition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The run state of the subscriber.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__264763c09a5d9d05410adb39930dd8cc7700affba24348821eb71fdebfa1ce7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the subscriber.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a1897a8d64094bec408dc401b2f1a02aff6ed9c2611c6e9969c4fefbce7bcb4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="transformer")
    def transformer(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.TransformerProperty"]]:
        '''Configuration for transforming events before delivery: the raw payload, the payload with its metadata envelope, or the output of a JSONata expression.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.TransformerProperty"]], jsii.get(self, "transformer"))

    @transformer.setter
    def transformer(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.TransformerProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__82679293e1412208d25ea9d26d5f638b05de8132e6cd164ac54dc8ee77a5d173)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transformer", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The delivery ordering mode of the subscriber.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fce7acb5b15cca1bf03e0e113c94bc4f18e5a5a2ca2a44cc2d9439db48ab3865)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.BatchConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_batch_size": "maxBatchSize",
            "max_batch_window_in_seconds": "maxBatchWindowInSeconds",
        },
    )
    class BatchConfigurationProperty:
        def __init__(
            self,
            *,
            max_batch_size: typing.Optional[jsii.Number] = None,
            max_batch_window_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration for batching events into a single delivery.

            :param max_batch_size: The maximum number of events in a single batch delivered to the target. The maximum depends on the target: 500 for Kinesis Data Streams and Amazon Data Firehose, 100 for Lambda, Step Functions, and AWS::EventsV2::EventBus targets, 10 for Amazon SQS, Amazon SNS, and AWS::Events::EventBus targets, and 1 for API Gateway, API destinations, and universal service integration targets. The service rejects a value above the target's maximum. Fewer events may be delivered when the batch window elapses. When omitted, the default is 10 for Lambda and Step Functions targets and the target's maximum for other targets. The resolved value applied by the service is returned on read.
            :param max_batch_window_in_seconds: The maximum time in seconds to wait for a batch to fill before delivering it, 0-300. The default is 0 (no wait). The resolved value applied by the service is returned on read.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-batchconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                batch_configuration_property = eventsv2.CfnSubscriber.BatchConfigurationProperty(
                    max_batch_size=123,
                    max_batch_window_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__78ebab28e0ecf3e029da44f82211ec92cdb5275477fee878cc39d22c77ac41b7)
                check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
                check_type(argname="argument max_batch_window_in_seconds", value=max_batch_window_in_seconds, expected_type=type_hints["max_batch_window_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_batch_size is not None:
                self._values["max_batch_size"] = max_batch_size
            if max_batch_window_in_seconds is not None:
                self._values["max_batch_window_in_seconds"] = max_batch_window_in_seconds

        @builtins.property
        def max_batch_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of events in a single batch delivered to the target.

            The maximum depends on the target: 500 for Kinesis Data Streams and Amazon Data Firehose, 100 for Lambda, Step Functions, and AWS::EventsV2::EventBus targets, 10 for Amazon SQS, Amazon SNS, and AWS::Events::EventBus targets, and 1 for API Gateway, API destinations, and universal service integration targets. The service rejects a value above the target's maximum. Fewer events may be delivered when the batch window elapses. When omitted, the default is 10 for Lambda and Step Functions targets and the target's maximum for other targets. The resolved value applied by the service is returned on read.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-batchconfiguration.html#cfn-eventsv2-subscriber-batchconfiguration-maxbatchsize
            '''
            result = self._values.get("max_batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_batch_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum time in seconds to wait for a batch to fill before delivering it, 0-300.

            The default is 0 (no wait). The resolved value applied by the service is returned on read.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-batchconfiguration.html#cfn-eventsv2-subscriber-batchconfiguration-maxbatchwindowinseconds
            '''
            result = self._values.get("max_batch_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BatchConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.FilterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"filters": "filters", "language": "language"},
    )
    class FilterConfigurationProperty:
        def __init__(
            self,
            *,
            filters: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.FilterProperty", typing.Dict[builtins.str, typing.Any]]]]],
            language: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for filtering which events are delivered to the target.

            An event must match every filter to be delivered.

            :param filters: The list of filters, 1-50 entries. An event must match every filter to be delivered.
            :param language: The filter language. The default is EVENT_BRIDGE_PATTERN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-filterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                filter_configuration_property = eventsv2.CfnSubscriber.FilterConfigurationProperty(
                    filters=[eventsv2.CfnSubscriber.FilterProperty(
                        pattern="pattern",
                        scope="scope"
                    )],
                
                    # the properties below are optional
                    language="language"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8cfe785c69fb3ea413615ee6b0002cdef19fe4b9a6bee0cd4cea1ee5b4e58629)
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
                check_type(argname="argument language", value=language, expected_type=type_hints["language"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filters": filters,
            }
            if language is not None:
                self._values["language"] = language

        @builtins.property
        def filters(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.FilterProperty"]]]:
            '''The list of filters, 1-50 entries.

            An event must match every filter to be delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-filterconfiguration.html#cfn-eventsv2-subscriber-filterconfiguration-filters
            '''
            result = self._values.get("filters")
            assert result is not None, "Required property 'filters' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.FilterProperty"]]], result)

        @builtins.property
        def language(self) -> typing.Optional[builtins.str]:
            '''The filter language.

            The default is EVENT_BRIDGE_PATTERN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-filterconfiguration.html#cfn-eventsv2-subscriber-filterconfiguration-language
            '''
            result = self._values.get("language")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"pattern": "pattern", "scope": "scope"},
    )
    class FilterProperty:
        def __init__(self, *, pattern: builtins.str, scope: builtins.str) -> None:
            '''A single filter entry: an event pattern and the scope of the event it is evaluated against.

            :param pattern: The event pattern, as a JSON string.
            :param scope: Which part of the event the pattern is evaluated against: DATA (the event payload), METADATA (event metadata), or SYSTEM_METADATA (service-generated metadata).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                filter_property = eventsv2.CfnSubscriber.FilterProperty(
                    pattern="pattern",
                    scope="scope"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a3ae39dcc4ccfc03648459956f13aedf923af4dffa84a8b5c04c3fc5f4d456f6)
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pattern": pattern,
                "scope": scope,
            }

        @builtins.property
        def pattern(self) -> builtins.str:
            '''The event pattern, as a JSON string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-filter.html#cfn-eventsv2-subscriber-filter-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scope(self) -> builtins.str:
            '''Which part of the event the pattern is evaluated against: DATA (the event payload), METADATA (event metadata), or SYSTEM_METADATA (service-generated metadata).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-filter.html#cfn-eventsv2-subscriber-filter-scope
            '''
            result = self._values.get("scope")
            assert result is not None, "Required property 'scope' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.JsonataConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression"},
    )
    class JsonataConfigurationProperty:
        def __init__(self, *, expression: builtins.str) -> None:
            '''JSONata transform settings.

            :param expression: The JSONata expression that transforms the event, enclosed in {% %} delimiters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-jsonataconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                jsonata_configuration_property = eventsv2.CfnSubscriber.JsonataConfigurationProperty(
                    expression="expression"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1ca400a0ab75346e88b9e69aed85a9a5363867dbc4e204a1593eb5cf4945dc0e)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
            }

        @builtins.property
        def expression(self) -> builtins.str:
            '''The JSONata expression that transforms the event, enclosed in {% %} delimiters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-jsonataconfiguration.html#cfn-eventsv2-subscriber-jsonataconfiguration-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonataConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"include_payload": "includePayload", "level": "level"},
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            include_payload: typing.Optional[builtins.str] = None,
            level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Delivery logging configuration.

            :param include_payload: Whether the event payload is included in emitted log records: FULL includes it in every emitted record, and ON_ERROR_ONLY includes it only in error records. The default is ON_ERROR_ONLY.
            :param level: The minimum log level: OFF (no logging), ERROR, or INFO. Records below this level are not emitted. The default is OFF.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-logconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                log_configuration_property = eventsv2.CfnSubscriber.LogConfigurationProperty(
                    include_payload="includePayload",
                    level="level"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__07669a8451260ee22e83467eed3ec8c8861ed2d68743f71f8050204a25dc8777)
                check_type(argname="argument include_payload", value=include_payload, expected_type=type_hints["include_payload"])
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if include_payload is not None:
                self._values["include_payload"] = include_payload
            if level is not None:
                self._values["level"] = level

        @builtins.property
        def include_payload(self) -> typing.Optional[builtins.str]:
            '''Whether the event payload is included in emitted log records: FULL includes it in every emitted record, and ON_ERROR_ONLY includes it only in error records.

            The default is ON_ERROR_ONLY.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-logconfiguration.html#cfn-eventsv2-subscriber-logconfiguration-includepayload
            '''
            result = self._values.get("include_payload")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def level(self) -> typing.Optional[builtins.str]:
            '''The minimum log level: OFF (no logging), ERROR, or INFO.

            Records below this level are not emitted. The default is OFF.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-logconfiguration.html#cfn-eventsv2-subscriber-logconfiguration-level
            '''
            result = self._values.get("level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.OnFailureConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class OnFailureConfigurationProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''The destination for events that could not be delivered.

            :param arn: The ARN of the destination that receives events that could not be delivered. An Amazon SQS queue is the supported destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-onfailureconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                on_failure_configuration_property = eventsv2.CfnSubscriber.OnFailureConfigurationProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2d1247df9ae68773b28215db5ae6d8f861a7fdf78ea9d6d5fb570fae90e85960)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the destination that receives events that could not be delivered.

            An Amazon SQS queue is the supported destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-onfailureconfiguration.html#cfn-eventsv2-subscriber-onfailureconfiguration-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnFailureConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.PointInTimeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "point_type": "pointType",
            "end_point": "endPoint",
            "starting_point": "startingPoint",
        },
    )
    class PointInTimeConfigurationProperty:
        def __init__(
            self,
            *,
            point_type: builtins.str,
            end_point: typing.Optional[jsii.Number] = None,
            starting_point: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The point in time to start delivering events from, used when StartingPosition is POINT_IN_TIME.

            :param point_type: Where to start: HORIZON starts from the earliest available event; TIMESTAMP starts from the StartingPoint timestamp.
            :param end_point: An optional time to stop delivering events at, in seconds since the Unix epoch.
            :param starting_point: The time to start delivering events from, in seconds since the Unix epoch. Required when PointType is TIMESTAMP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-pointintimeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                point_in_time_configuration_property = eventsv2.CfnSubscriber.PointInTimeConfigurationProperty(
                    point_type="pointType",
                
                    # the properties below are optional
                    end_point=123,
                    starting_point=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__027c7b99544f89e813d0a1ebba0f8c7e93daee20af22aa7a5659a4fc8df1463c)
                check_type(argname="argument point_type", value=point_type, expected_type=type_hints["point_type"])
                check_type(argname="argument end_point", value=end_point, expected_type=type_hints["end_point"])
                check_type(argname="argument starting_point", value=starting_point, expected_type=type_hints["starting_point"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "point_type": point_type,
            }
            if end_point is not None:
                self._values["end_point"] = end_point
            if starting_point is not None:
                self._values["starting_point"] = starting_point

        @builtins.property
        def point_type(self) -> builtins.str:
            '''Where to start: HORIZON starts from the earliest available event;

            TIMESTAMP starts from the StartingPoint timestamp.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-pointintimeconfiguration.html#cfn-eventsv2-subscriber-pointintimeconfiguration-pointtype
            '''
            result = self._values.get("point_type")
            assert result is not None, "Required property 'point_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_point(self) -> typing.Optional[jsii.Number]:
            '''An optional time to stop delivering events at, in seconds since the Unix epoch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-pointintimeconfiguration.html#cfn-eventsv2-subscriber-pointintimeconfiguration-endpoint
            '''
            result = self._values.get("end_point")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def starting_point(self) -> typing.Optional[jsii.Number]:
            '''The time to start delivering events from, in seconds since the Unix epoch.

            Required when PointType is TIMESTAMP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-pointintimeconfiguration.html#cfn-eventsv2-subscriber-pointintimeconfiguration-startingpoint
            '''
            result = self._values.get("starting_point")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PointInTimeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.RetryPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_event_age_in_seconds": "maxEventAgeInSeconds",
            "max_retry_attempts": "maxRetryAttempts",
            "retry_strategy": "retryStrategy",
        },
    )
    class RetryPolicyProperty:
        def __init__(
            self,
            *,
            max_event_age_in_seconds: typing.Optional[jsii.Number] = None,
            max_retry_attempts: typing.Optional[jsii.Number] = None,
            retry_strategy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The retry policy for failed deliveries.

            :param max_event_age_in_seconds: The maximum age of an event in seconds, 60-86400 (24 hours). When an event reaches this age, retries stop; if OnFailureConfiguration is set, the event is delivered to that destination, otherwise it is dropped. The default is 300.
            :param max_retry_attempts: The maximum number of retry attempts, 0-185. When the attempts are exhausted, retries stop; if OnFailureConfiguration is set, the event is delivered to that destination, otherwise it is dropped. The default is 5.
            :param retry_strategy: Which errors are retried. ALL retries all errors. The default is ALL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-retrypolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                retry_policy_property = eventsv2.CfnSubscriber.RetryPolicyProperty(
                    max_event_age_in_seconds=123,
                    max_retry_attempts=123,
                    retry_strategy="retryStrategy"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__3c791dede7e793330db33b26fb73a7685e974fa9f4d5cf40ff32e11d7afa0d64)
                check_type(argname="argument max_event_age_in_seconds", value=max_event_age_in_seconds, expected_type=type_hints["max_event_age_in_seconds"])
                check_type(argname="argument max_retry_attempts", value=max_retry_attempts, expected_type=type_hints["max_retry_attempts"])
                check_type(argname="argument retry_strategy", value=retry_strategy, expected_type=type_hints["retry_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_event_age_in_seconds is not None:
                self._values["max_event_age_in_seconds"] = max_event_age_in_seconds
            if max_retry_attempts is not None:
                self._values["max_retry_attempts"] = max_retry_attempts
            if retry_strategy is not None:
                self._values["retry_strategy"] = retry_strategy

        @builtins.property
        def max_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum age of an event in seconds, 60-86400 (24 hours).

            When an event reaches this age, retries stop; if OnFailureConfiguration is set, the event is delivered to that destination, otherwise it is dropped. The default is 300.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-retrypolicy.html#cfn-eventsv2-subscriber-retrypolicy-maxeventageinseconds
            '''
            result = self._values.get("max_event_age_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_retry_attempts(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of retry attempts, 0-185.

            When the attempts are exhausted, retries stop; if OnFailureConfiguration is set, the event is delivered to that destination, otherwise it is dropped. The default is 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-retrypolicy.html#cfn-eventsv2-subscriber-retrypolicy-maxretryattempts
            '''
            result = self._values.get("max_retry_attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def retry_strategy(self) -> typing.Optional[builtins.str]:
            '''Which errors are retried.

            ALL retries all errors. The default is ALL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-retrypolicy.html#cfn-eventsv2-subscriber-retrypolicy-retrystrategy
            '''
            result = self._values.get("retry_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetryPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriber.TransformerProperty",
        jsii_struct_bases=[],
        name_mapping={"jsonata_configuration": "jsonataConfiguration", "type": "type"},
    )
    class TransformerProperty:
        def __init__(
            self,
            *,
            jsonata_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.JsonataConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for transforming events before delivery: the raw payload, the payload with its metadata envelope, or the output of a JSONata expression.

            :param jsonata_configuration: JSONata transform settings.
            :param type: The transform type: RAW delivers the event payload only; WITH_METADATA delivers the event with its metadata envelope; JSONATA delivers the output of the JSONata expression in JsonataConfiguration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-transformer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventsv2 as eventsv2
                
                transformer_property = eventsv2.CfnSubscriber.TransformerProperty(
                    jsonata_configuration=eventsv2.CfnSubscriber.JsonataConfigurationProperty(
                        expression="expression"
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__85b761ea193aa8b93943323815709941f390d000a8bfe4fb8cb6913aaffa6e4e)
                check_type(argname="argument jsonata_configuration", value=jsonata_configuration, expected_type=type_hints["jsonata_configuration"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if jsonata_configuration is not None:
                self._values["jsonata_configuration"] = jsonata_configuration
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def jsonata_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.JsonataConfigurationProperty"]]:
            '''JSONata transform settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-transformer.html#cfn-eventsv2-subscriber-transformer-jsonataconfiguration
            '''
            result = self._values.get("jsonata_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.JsonataConfigurationProperty"]], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The transform type: RAW delivers the event payload only;

            WITH_METADATA delivers the event with its metadata envelope; JSONATA delivers the output of the JSONata expression in JsonataConfiguration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventsv2-subscriber-transformer.html#cfn-eventsv2-subscriber-transformer-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eventsv2.CfnSubscriberProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_bus_arn": "eventBusArn",
        "name": "name",
        "batch_configuration": "batchConfiguration",
        "description": "description",
        "filter_configuration": "filterConfiguration",
        "log_configuration": "logConfiguration",
        "on_failure_configuration": "onFailureConfiguration",
        "point_in_time_configuration": "pointInTimeConfiguration",
        "resume_position": "resumePosition",
        "retry_policy": "retryPolicy",
        "starting_position": "startingPosition",
        "state": "state",
        "tags": "tags",
        "transformer": "transformer",
        "type": "type",
    },
)
class CfnSubscriberProps:
    def __init__(
        self,
        *,
        event_bus_arn: builtins.str,
        name: builtins.str,
        batch_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.BatchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        filter_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.FilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        on_failure_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.OnFailureConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        point_in_time_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.PointInTimeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        resume_position: typing.Optional[builtins.str] = None,
        retry_policy: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.RetryPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        starting_position: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        transformer: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSubscriber.TransformerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscriber``.

        :param event_bus_arn: The ARN of the event bus this subscriber belongs to.
        :param name: The name of the subscriber. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'.
        :param batch_configuration: Configuration for batching events into a single delivery.
        :param description: A description of the subscriber. Control characters and Unicode line separators are not allowed.
        :param filter_configuration: Configuration for filtering which events are delivered to the target. An event must match every filter to be delivered.
        :param log_configuration: Delivery logging configuration.
        :param on_failure_configuration: The destination for events that could not be delivered.
        :param point_in_time_configuration: The point in time to start delivering events from, used when StartingPosition is POINT_IN_TIME.
        :param resume_position: Resume-time control, never returned by the service. Applied only when an update transitions State from STOPPED to RUNNING: LAST_PROCESSED (default) resumes from the last processed event, LATEST skips to the newest. Ignored on create and on any update that does not perform that transition.
        :param retry_policy: The retry policy for failed deliveries.
        :param starting_position: Where the subscriber starts reading events: LATEST starts from the newest events; POINT_IN_TIME starts from the point specified in PointInTimeConfiguration.
        :param state: The run state of the subscriber. Events are delivered only while the state is RUNNING. Setting the state to STOPPED pauses delivery. When an update sets a stopped subscriber back to RUNNING, ResumePosition controls where delivery resumes.
        :param tags: The tags assigned to the subscriber.
        :param transformer: Configuration for transforming events before delivery: the raw payload, the payload with its metadata envelope, or the output of a JSONata expression.
        :param type: The delivery ordering mode of the subscriber. FIFO delivers events in order within an event group; UNORDERED delivers without an ordering guarantee.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eventsv2 as eventsv2
            
            cfn_subscriber_props = eventsv2.CfnSubscriberProps(
                event_bus_arn="eventBusArn",
                name="name",
            
                # the properties below are optional
                batch_configuration=eventsv2.CfnSubscriber.BatchConfigurationProperty(
                    max_batch_size=123,
                    max_batch_window_in_seconds=123
                ),
                description="description",
                filter_configuration=eventsv2.CfnSubscriber.FilterConfigurationProperty(
                    filters=[eventsv2.CfnSubscriber.FilterProperty(
                        pattern="pattern",
                        scope="scope"
                    )],
            
                    # the properties below are optional
                    language="language"
                ),
                log_configuration=eventsv2.CfnSubscriber.LogConfigurationProperty(
                    include_payload="includePayload",
                    level="level"
                ),
                on_failure_configuration=eventsv2.CfnSubscriber.OnFailureConfigurationProperty(
                    arn="arn"
                ),
                point_in_time_configuration=eventsv2.CfnSubscriber.PointInTimeConfigurationProperty(
                    point_type="pointType",
            
                    # the properties below are optional
                    end_point=123,
                    starting_point=123
                ),
                resume_position="resumePosition",
                retry_policy=eventsv2.CfnSubscriber.RetryPolicyProperty(
                    max_event_age_in_seconds=123,
                    max_retry_attempts=123,
                    retry_strategy="retryStrategy"
                ),
                starting_position="startingPosition",
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                transformer=eventsv2.CfnSubscriber.TransformerProperty(
                    jsonata_configuration=eventsv2.CfnSubscriber.JsonataConfigurationProperty(
                        expression="expression"
                    ),
                    type="type"
                ),
                type="type"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a6cd1086538e738cc299431ae14151034acd600e3de88c1196593f9161f2a519)
            check_type(argname="argument event_bus_arn", value=event_bus_arn, expected_type=type_hints["event_bus_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument batch_configuration", value=batch_configuration, expected_type=type_hints["batch_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument filter_configuration", value=filter_configuration, expected_type=type_hints["filter_configuration"])
            check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
            check_type(argname="argument on_failure_configuration", value=on_failure_configuration, expected_type=type_hints["on_failure_configuration"])
            check_type(argname="argument point_in_time_configuration", value=point_in_time_configuration, expected_type=type_hints["point_in_time_configuration"])
            check_type(argname="argument resume_position", value=resume_position, expected_type=type_hints["resume_position"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transformer", value=transformer, expected_type=type_hints["transformer"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bus_arn": event_bus_arn,
            "name": name,
        }
        if batch_configuration is not None:
            self._values["batch_configuration"] = batch_configuration
        if description is not None:
            self._values["description"] = description
        if filter_configuration is not None:
            self._values["filter_configuration"] = filter_configuration
        if log_configuration is not None:
            self._values["log_configuration"] = log_configuration
        if on_failure_configuration is not None:
            self._values["on_failure_configuration"] = on_failure_configuration
        if point_in_time_configuration is not None:
            self._values["point_in_time_configuration"] = point_in_time_configuration
        if resume_position is not None:
            self._values["resume_position"] = resume_position
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if starting_position is not None:
            self._values["starting_position"] = starting_position
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if transformer is not None:
            self._values["transformer"] = transformer
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def event_bus_arn(self) -> builtins.str:
        '''The ARN of the event bus this subscriber belongs to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-eventbusarn
        '''
        result = self._values.get("event_bus_arn")
        assert result is not None, "Required property 'event_bus_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the subscriber.

        The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.BatchConfigurationProperty"]]:
        '''Configuration for batching events into a single delivery.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-batchconfiguration
        '''
        result = self._values.get("batch_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.BatchConfigurationProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the subscriber.

        Control characters and Unicode line separators are not allowed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.FilterConfigurationProperty"]]:
        '''Configuration for filtering which events are delivered to the target.

        An event must match every filter to be delivered.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-filterconfiguration
        '''
        result = self._values.get("filter_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.FilterConfigurationProperty"]], result)

    @builtins.property
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.LogConfigurationProperty"]]:
        '''Delivery logging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-logconfiguration
        '''
        result = self._values.get("log_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.LogConfigurationProperty"]], result)

    @builtins.property
    def on_failure_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.OnFailureConfigurationProperty"]]:
        '''The destination for events that could not be delivered.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-onfailureconfiguration
        '''
        result = self._values.get("on_failure_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.OnFailureConfigurationProperty"]], result)

    @builtins.property
    def point_in_time_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.PointInTimeConfigurationProperty"]]:
        '''The point in time to start delivering events from, used when StartingPosition is POINT_IN_TIME.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-pointintimeconfiguration
        '''
        result = self._values.get("point_in_time_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.PointInTimeConfigurationProperty"]], result)

    @builtins.property
    def resume_position(self) -> typing.Optional[builtins.str]:
        '''Resume-time control, never returned by the service.

        Applied only when an update transitions State from STOPPED to RUNNING: LAST_PROCESSED (default) resumes from the last processed event, LATEST skips to the newest. Ignored on create and on any update that does not perform that transition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-resumeposition
        '''
        result = self._values.get("resume_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_policy(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.RetryPolicyProperty"]]:
        '''The retry policy for failed deliveries.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-retrypolicy
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.RetryPolicyProperty"]], result)

    @builtins.property
    def starting_position(self) -> typing.Optional[builtins.str]:
        '''Where the subscriber starts reading events: LATEST starts from the newest events;

        POINT_IN_TIME starts from the point specified in PointInTimeConfiguration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-startingposition
        '''
        result = self._values.get("starting_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The run state of the subscriber.

        Events are delivered only while the state is RUNNING. Setting the state to STOPPED pauses delivery. When an update sets a stopped subscriber back to RUNNING, ResumePosition controls where delivery resumes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the subscriber.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def transformer(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.TransformerProperty"]]:
        '''Configuration for transforming events before delivery: the raw payload, the payload with its metadata envelope, or the output of a JSONata expression.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-transformer
        '''
        result = self._values.get("transformer")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSubscriber.TransformerProperty"]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The delivery ordering mode of the subscriber.

        FIFO delivers events in order within an event group; UNORDERED delivers without an ordering guarantee.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventsv2-subscriber.html#cfn-eventsv2-subscriber-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEventBus",
    "CfnEventBusProps",
    "CfnEventSource",
    "CfnEventSourceProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CfnSubscriber",
    "CfnSubscriberProps",
]

publication.publish()

def _typecheckingstub__73208bd89f76ba584f028d6ce398bcd1482829e2c346de90b3b9d148e7d887b6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventBus.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    storage_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventBus.StorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6ca2b227989b44b021f48111b26f0fb74f7b544507dd3e2f3f7d65212dbd7bf(
    resource: _aws_eventsv2_0250e2c5.IEventBusRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ef461863115ad0e9cc454734c7d1ed3affb217d3f2feda0012bdec87b7503d(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe8d712056c76d4b6d0ed7a4600e3dbb29dcf3554ceb465b0fe466051bb6c0ef(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cf4c0b04ff6a847d12f9151602e9a66ca3517d75f34999ca923b18ae5540ac0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee9ac8b436284a957f1d956f844335a38245bfa0d2c47f6508e873a0cac4a898(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7df16b6417ddf005f3950e2298297d1ebe2b6ed2c71861f56407ad1ec7b0ec1c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1587ce163ec2a1690136eb81cc89ac5b130f01424c98fe9cffa19ac50c824c(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnEventBus.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc42052cd98bfe53e4c5706d2a05e99640f84231be21e82224d0c890800df8a3(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnEventBus.StorageConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ed1fa75f370cb15d812650283f3363698cbbb3bff10bd187595246d9876fbe(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__539097163761e51929fa97f8446a4a012832593efa9592d1040cd91ab0e4daf7(
    *,
    kms_key_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ace5f3dc47d717e1fe4bc56f1be7fa2773a2ad721e0d1e5df27b1aa0cf98659(
    *,
    retention_period_in_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78fdefbe04da2f08db27daec43937bf27dd1f25d496457662f45c552c033f709(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventBus.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    storage_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventBus.StorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19ea3c2714b4bbb1b5c119c2fab9bb5c845575f8931b3a89abe1991f798f928b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventSource.EventSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    event_bus_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9194c78bb4c32f7d83b27233159f2ea9d9c434371018442411a5cad4b690250(
    resource: _aws_eventsv2_0250e2c5.IEventSourceRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773f2f1226ca2c8cc12d87d026858d00d0c6aa6594d505e3f58a027e92ec1507(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72863d3a7247be261ec897a3e4ff4e32e657ba96be66bcd1ceafc6bbe2f27ff6(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99d3b9477f1dd3faa028535c642f0fe38c7fcd4b8defae73474bf0c1efae5ed0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c0002932c84a252c296e10e872e5fa5abf135d0e4984dca9be5082e00c13e5f(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnEventSource.EventSourceConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d564d56b64810b9021d7445571c5638763974b5383ed5587190ac200f4d573a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d6c8780caa2a0ffb779a7016735274f6123fb5da20a53ba8a93448bb0787224(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bfe70eadeea68822e462ab5cf2a07af053d7db9970b9f203fd623a1d7ab9124(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f880032e0ea2a6bf89a92521abfc144ac2ee6a1f69595b51d0dcfea3769e3ee(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddedc661fee98c57d3f869532a27aec50c8b6bdaff873088c95159c9866ef533(
    *,
    aws_service: builtins.str,
    on_failure_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventSource.OnFailureConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db65cd2375229e5c755606bdc958c9a287941eba06fcaa2eaa39188dbbef67dc(
    *,
    aws_service_events_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventSource.AwsServiceEventsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    partner_events_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventSource.PartnerEventsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cefd71b3eb3dccdf506b40744a767b5c7a852681abc8dc62fb33c632fe4179c(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__815d9cedb6ba6bf56a9403e4fa03859f4947792a8a7fb051a3e9b7e56de91e4b(
    *,
    partner_event_source_arn: builtins.str,
    on_failure_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventSource.OnFailureConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    partner_bus_kms_key_identifier: typing.Optional[builtins.str] = None,
    pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ed838f2373b14d074fe18d883bc57c6be6a876f0c0e40543f9fc58c428122a(
    *,
    configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventSource.EventSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    event_bus_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300cddccc13b1d85bc424fda9f26893846f54c90eba86ea09b2a26250039795f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    event_bus_arn: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a1d8a2f5f4b9aa404ff515bb13df7667b5ce396a65aa13988c137440c9c3319(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__297832e93744970db77ecbe5bc0ddcb28e3f6f912689cb8dc8bbf336ec42cd51(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dca0a59ed62e2c169717fa5440c7d942a86dab2f141f2663aaaae87bdbea993(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad236f15451341d60d13dd82d2e4d162f902f0bd8908b8b4858d3dbc5b8892cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72321d83da7c7a058cee5f887d58a2593886e141b1e3893abd2f0dee518d2df7(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0ef7aad9ea56efd1b9f9ff3e9ca252fccbe507f5e1b910ce0f646ae9f0bf38(
    *,
    event_bus_arn: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05eeedb290d1b08bfcdffd50d6a079078b77f0cf13828494b2822574ca1fd9cd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    event_bus_arn: builtins.str,
    name: builtins.str,
    batch_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.BatchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    filter_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    on_failure_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.OnFailureConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    point_in_time_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.PointInTimeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resume_position: typing.Optional[builtins.str] = None,
    retry_policy: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.RetryPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    starting_position: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    transformer: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.TransformerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ff9aac1bf58379ec1df238773d941b43e91faccc9251c33a4a4b800b17bbbd(
    resource: _aws_eventsv2_0250e2c5.ISubscriberRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__377f43b61bd91be8c6e944c7f6b95813e6f2ba02534fc94acd535f370caa3ebe(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155ca594f4a12614dcd639a0037d20cc622aebd08cb2efd23130d8dad0fd5900(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38c14032b6049c2e80ab3ca2f3423cc2d7ba78d02d5b3c3e994d5cf49fde4ce9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3933a6bedc3ebda376667b88f5aff39872b63d4f4cc267377f0ce24146444149(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87904eb3d4c136da852fa2f79014380c4a8e213f434e3ca7df4a95969dbba534(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e9053b06fb8b200688b5dedefd3ba0608cdc0faadf89ec23b8d5ae6a581297e(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSubscriber.BatchConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d72dec88e45963d45b13efedcf6c93e95289752c135f4912ba07db0e94bfb10(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6556d4defc8819b1d1fd5d44b772ba7336f8d8ac3f7199cd9243dd8626324d8a(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSubscriber.FilterConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e436742c5ebe5420abdab660baf82f0d4727a9c0a1ad77992e1ec3bc27b005e(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSubscriber.LogConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__346b06bebd51f3c10e212119be182d6411b38595d52f541084cbf66b6d6947c9(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSubscriber.OnFailureConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c3a4b0a55ccbc09e680639c37389e152fc2a68249d30b23fb7bf1f8502116d6(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSubscriber.PointInTimeConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b1a6aa60908c077debd64afa6b695d61a4a0244544cfb3471664671dc39b01e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6288cda489031a5be2eb50bf47b6782e46ab8d4a9940cb162abd728b474a6f8(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSubscriber.RetryPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a8523d5487330fd3418214fa760d6b5418285dea76accbc0da7b6b896d7f44e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264763c09a5d9d05410adb39930dd8cc7700affba24348821eb71fdebfa1ce7e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1897a8d64094bec408dc401b2f1a02aff6ed9c2611c6e9969c4fefbce7bcb4d(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82679293e1412208d25ea9d26d5f638b05de8132e6cd164ac54dc8ee77a5d173(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSubscriber.TransformerProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fce7acb5b15cca1bf03e0e113c94bc4f18e5a5a2ca2a44cc2d9439db48ab3865(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ebab28e0ecf3e029da44f82211ec92cdb5275477fee878cc39d22c77ac41b7(
    *,
    max_batch_size: typing.Optional[jsii.Number] = None,
    max_batch_window_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cfe785c69fb3ea413615ee6b0002cdef19fe4b9a6bee0cd4cea1ee5b4e58629(
    *,
    filters: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.FilterProperty, typing.Dict[builtins.str, typing.Any]]]]],
    language: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3ae39dcc4ccfc03648459956f13aedf923af4dffa84a8b5c04c3fc5f4d456f6(
    *,
    pattern: builtins.str,
    scope: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca400a0ab75346e88b9e69aed85a9a5363867dbc4e204a1593eb5cf4945dc0e(
    *,
    expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07669a8451260ee22e83467eed3ec8c8861ed2d68743f71f8050204a25dc8777(
    *,
    include_payload: typing.Optional[builtins.str] = None,
    level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d1247df9ae68773b28215db5ae6d8f861a7fdf78ea9d6d5fb570fae90e85960(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027c7b99544f89e813d0a1ebba0f8c7e93daee20af22aa7a5659a4fc8df1463c(
    *,
    point_type: builtins.str,
    end_point: typing.Optional[jsii.Number] = None,
    starting_point: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c791dede7e793330db33b26fb73a7685e974fa9f4d5cf40ff32e11d7afa0d64(
    *,
    max_event_age_in_seconds: typing.Optional[jsii.Number] = None,
    max_retry_attempts: typing.Optional[jsii.Number] = None,
    retry_strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b761ea193aa8b93943323815709941f390d000a8bfe4fb8cb6913aaffa6e4e(
    *,
    jsonata_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.JsonataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6cd1086538e738cc299431ae14151034acd600e3de88c1196593f9161f2a519(
    *,
    event_bus_arn: builtins.str,
    name: builtins.str,
    batch_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.BatchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    filter_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    on_failure_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.OnFailureConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    point_in_time_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.PointInTimeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resume_position: typing.Optional[builtins.str] = None,
    retry_policy: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.RetryPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    starting_position: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    transformer: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSubscriber.TransformerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
