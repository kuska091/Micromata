r'''
# AWS::HealthAgent Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_healthagent as healthagent
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for HealthAgent construct libraries](https://constructs.dev/search?q=healthagent)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::HealthAgent resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_HealthAgent.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::HealthAgent](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_HealthAgent.html).

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
    import aws_cdk.interfaces.aws_healthagent as _aws_healthagent_b1b32d42
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_healthagent_b1b32d42 = _LazyImport("aws_cdk.interfaces.aws_healthagent")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_healthagent_b1b32d42.IDomainRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnDomain(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_healthagent.CfnDomain",
):
    '''Resource Type definition for AWS::HealthAgent::Domain.

    Creates and manages a HealthAgent Domain resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthagent-domain.html
    :cloudformationResource: AWS::HealthAgent::Domain
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_healthagent as healthagent
        
        cfn_domain = healthagent.CfnDomain(self, "MyCfnDomain",
            name="name",
        
            # the properties below are optional
            tags=[healthagent.CfnDomain.TagsItemsProperty(
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
        tags: typing.Optional[typing.Sequence[typing.Union["CfnDomain.TagsItemsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::HealthAgent::Domain``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the Domain.
        :param tags: Tags associated with the Domain.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dda8fd2580c7da6b8c30bc0cdbd0a85315dc0f254e20f90879049e46ff06280a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDomain")
    @builtins.classmethod
    def arn_for_domain(
        cls,
        resource: "_aws_healthagent_b1b32d42.IDomainRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__eace2ef79e9e23ae48d62ab145c2d8149570fda4f5c11a4e94652b584bc75c22)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDomain", [resource]))

    @jsii.member(jsii_name="isCfnDomain")
    @builtins.classmethod
    def is_cfn_domain(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDomain.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e3f03f35ec82d6381f3261c0d66879b8f41433687c85d113352ac27f7b732876)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDomain", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c9ea375973ed7fde2500bb0489df133ce34fad0ec2ef7a6b19e53b0d6853d2af)
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
            type_hints = cached_type_hints(_typecheckingstub__bbef48ac3841e4a876a3a427e7652aa431c9f9173643a2d368cafdb4eea70797)
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
        '''The Amazon Resource Name (ARN) of the Domain.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the Domain was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The unique identifier of the Domain.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEncryptionContext")
    def attr_encryption_context(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''Encryption context for the Domain.

        :cloudformationAttribute: EncryptionContext
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrEncryptionContext"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the Domain.

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
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "_aws_healthagent_b1b32d42.DomainReference":
        '''A reference to a Domain resource.'''
        return typing.cast("_aws_healthagent_b1b32d42.DomainReference", jsii.get(self, "domainRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Domain.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dd1b1558229fe92b5444f9b0c8605d0604d32ce632fe2f210f79d91f46894fed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnDomain.TagsItemsProperty"]]:
        '''Tags associated with the Domain.'''
        return typing.cast(typing.Optional[typing.List["CfnDomain.TagsItemsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnDomain.TagsItemsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1c650db4443cca1a9d3bb1a55984179f35f6a3fde7c531ce503f6c1db016a365)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthagent.CfnDomain.EncryptionContextProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_type": "encryptionType"},
    )
    class EncryptionContextProperty:
        def __init__(self, *, encryption_type: builtins.str) -> None:
            '''Encryption context for the Domain.

            :param encryption_type: The type of encryption key used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthagent-domain-encryptioncontext.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthagent as healthagent
                
                encryption_context_property = healthagent.CfnDomain.EncryptionContextProperty(
                    encryption_type="encryptionType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__15a640c5a3fc1ef056261c9949cd5766a5498241097b52d595506f5bc10d8eb2)
                check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_type": encryption_type,
            }

        @builtins.property
        def encryption_type(self) -> builtins.str:
            '''The type of encryption key used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthagent-domain-encryptioncontext.html#cfn-healthagent-domain-encryptioncontext-encryptiontype
            '''
            result = self._values.get("encryption_type")
            assert result is not None, "Required property 'encryption_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionContextProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthagent.CfnDomain.TagsItemsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsItemsProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthagent-domain-tagsitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthagent as healthagent
                
                tags_items_property = healthagent.CfnDomain.TagsItemsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6d94f5e40524ac18cd7abdacdaa890b79edeaa401caef04a8e9978eb82b545d0)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthagent-domain-tagsitems.html#cfn-healthagent-domain-tagsitems-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthagent-domain-tagsitems.html#cfn-healthagent-domain-tagsitems-value
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
    jsii_type="aws-cdk-lib.aws_healthagent.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnDomain.TagsItemsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param name: The name of the Domain.
        :param tags: Tags associated with the Domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthagent-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_healthagent as healthagent
            
            cfn_domain_props = healthagent.CfnDomainProps(
                name="name",
            
                # the properties below are optional
                tags=[healthagent.CfnDomain.TagsItemsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__411c16580f33f19190430ae9bc002c0db4445947fa92377fd377d9ed142b19d0)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthagent-domain.html#cfn-healthagent-domain-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnDomain.TagsItemsProperty"]]:
        '''Tags associated with the Domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthagent-domain.html#cfn-healthagent-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["CfnDomain.TagsItemsProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDomain",
    "CfnDomainProps",
]

publication.publish()

def _typecheckingstub__dda8fd2580c7da6b8c30bc0cdbd0a85315dc0f254e20f90879049e46ff06280a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDomain.TagsItemsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eace2ef79e9e23ae48d62ab145c2d8149570fda4f5c11a4e94652b584bc75c22(
    resource: _aws_healthagent_b1b32d42.IDomainRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f03f35ec82d6381f3261c0d66879b8f41433687c85d113352ac27f7b732876(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9ea375973ed7fde2500bb0489df133ce34fad0ec2ef7a6b19e53b0d6853d2af(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbef48ac3841e4a876a3a427e7652aa431c9f9173643a2d368cafdb4eea70797(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd1b1558229fe92b5444f9b0c8605d0604d32ce632fe2f210f79d91f46894fed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c650db4443cca1a9d3bb1a55984179f35f6a3fde7c531ce503f6c1db016a365(
    value: typing.Optional[typing.List[CfnDomain.TagsItemsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a640c5a3fc1ef056261c9949cd5766a5498241097b52d595506f5bc10d8eb2(
    *,
    encryption_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d94f5e40524ac18cd7abdacdaa890b79edeaa401caef04a8e9978eb82b545d0(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__411c16580f33f19190430ae9bc002c0db4445947fa92377fd377d9ed142b19d0(
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDomain.TagsItemsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
