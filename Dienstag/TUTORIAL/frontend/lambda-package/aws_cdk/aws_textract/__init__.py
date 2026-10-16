r'''
# AWS::Textract Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_textract as textract
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Textract construct libraries](https://constructs.dev/search?q=textract)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Textract resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Textract.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Textract](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Textract.html).

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
    import aws_cdk.interfaces.aws_textract as _aws_textract_57016ef5
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_textract_57016ef5 = _LazyImport("aws_cdk.interfaces.aws_textract")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_textract_57016ef5.IAdapterRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnAdapter(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_textract.CfnAdapter",
):
    '''The AWS::Textract::Adapter resource creates an Amazon Textract adapter, which can be fine-tuned for enhanced performance on user-provided documents.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-textract-adapter.html
    :cloudformationResource: AWS::Textract::Adapter
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_textract as textract
        
        cfn_adapter = textract.CfnAdapter(self, "MyCfnAdapter",
            adapter_name="adapterName",
            feature_types=["featureTypes"],
        
            # the properties below are optional
            auto_update="autoUpdate",
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
        adapter_name: builtins.str,
        feature_types: typing.Sequence[builtins.str],
        auto_update: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Textract::Adapter``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param adapter_name: The name to be assigned to the adapter being created.
        :param feature_types: The type of feature that the adapter is being trained on. Currently, supported feature types are: QUERIES
        :param auto_update: Controls whether or not the adapter should automatically update.
        :param description: The description to be assigned to the adapter being created.
        :param tags: A list of tags to be added to the adapter.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__555f33b4aad2e420ef9286245345e979caff74e1e0aceacbf51327f9834fb61a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAdapterProps(
            adapter_name=adapter_name,
            feature_types=feature_types,
            auto_update=auto_update,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAdapter")
    @builtins.classmethod
    def arn_for_adapter(
        cls,
        resource: "_aws_textract_57016ef5.IAdapterRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b1ae8a77fa4d2c88e87cf44241930124ce4c53c0ca73615fe0ae9f1f8e7afec6)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAdapter", [resource]))

    @jsii.member(jsii_name="isCfnAdapter")
    @builtins.classmethod
    def is_cfn_adapter(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAdapter.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f00c3e712bf4dc730d0bd04de4e302211a803b7761428ed312e60ff05f9e3ffb)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAdapter", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c21046e584df63b93e670e418b3cc1c057937c2ee21a67eccd0728ae29b20a34)
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
            type_hints = cached_type_hints(_typecheckingstub__9c10f26f0f43422aacba582208443d077c03e6a97f933cecda8e0fd72d1ef245)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="adapterRef")
    def adapter_ref(self) -> "_aws_textract_57016ef5.AdapterReference":
        '''A reference to a Adapter resource.'''
        return typing.cast("_aws_textract_57016ef5.AdapterReference", jsii.get(self, "adapterRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAdapterId")
    def attr_adapter_id(self) -> builtins.str:
        '''A unique identifier for the adapter resource.

        :cloudformationAttribute: AdapterId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAdapterId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the adapter.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The date and time that the adapter was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

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
    @jsii.member(jsii_name="adapterName")
    def adapter_name(self) -> builtins.str:
        '''The name to be assigned to the adapter being created.'''
        return typing.cast(builtins.str, jsii.get(self, "adapterName"))

    @adapter_name.setter
    def adapter_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__886799141ec01d9ea2256cdd67c42848de7514b954cbc32a9a45142e19239c70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adapterName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="featureTypes")
    def feature_types(self) -> typing.List[builtins.str]:
        '''The type of feature that the adapter is being trained on.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "featureTypes"))

    @feature_types.setter
    def feature_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__30f67f376a5f036b73076099b32edec76b4a3e394b4b7e6ffa024728429f2ded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "featureTypes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="autoUpdate")
    def auto_update(self) -> typing.Optional[builtins.str]:
        '''Controls whether or not the adapter should automatically update.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoUpdate"))

    @auto_update.setter
    def auto_update(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__92784ab97d9f6b538830e8b8c6e734b14585910aed4e3b92082a8ca10a868078)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpdate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to be assigned to the adapter being created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c194f2a4e32c6be061592ea92cc999e7aae364cb78e15a7e0a130d3d25d37ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of tags to be added to the adapter.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d8c908c24c1c9cac33f554e9c732d8ca205501a6b08d9e40758143fe0f056096)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_textract.CfnAdapterProps",
    jsii_struct_bases=[],
    name_mapping={
        "adapter_name": "adapterName",
        "feature_types": "featureTypes",
        "auto_update": "autoUpdate",
        "description": "description",
        "tags": "tags",
    },
)
class CfnAdapterProps:
    def __init__(
        self,
        *,
        adapter_name: builtins.str,
        feature_types: typing.Sequence[builtins.str],
        auto_update: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAdapter``.

        :param adapter_name: The name to be assigned to the adapter being created.
        :param feature_types: The type of feature that the adapter is being trained on. Currently, supported feature types are: QUERIES
        :param auto_update: Controls whether or not the adapter should automatically update.
        :param description: The description to be assigned to the adapter being created.
        :param tags: A list of tags to be added to the adapter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-textract-adapter.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_textract as textract
            
            cfn_adapter_props = textract.CfnAdapterProps(
                adapter_name="adapterName",
                feature_types=["featureTypes"],
            
                # the properties below are optional
                auto_update="autoUpdate",
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1f4d32a5e348a57106397cb1043cf755c90945ad2972f38f3cdba1b054dfa49f)
            check_type(argname="argument adapter_name", value=adapter_name, expected_type=type_hints["adapter_name"])
            check_type(argname="argument feature_types", value=feature_types, expected_type=type_hints["feature_types"])
            check_type(argname="argument auto_update", value=auto_update, expected_type=type_hints["auto_update"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "adapter_name": adapter_name,
            "feature_types": feature_types,
        }
        if auto_update is not None:
            self._values["auto_update"] = auto_update
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def adapter_name(self) -> builtins.str:
        '''The name to be assigned to the adapter being created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-textract-adapter.html#cfn-textract-adapter-adaptername
        '''
        result = self._values.get("adapter_name")
        assert result is not None, "Required property 'adapter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def feature_types(self) -> typing.List[builtins.str]:
        '''The type of feature that the adapter is being trained on.

        Currently, supported feature types are: QUERIES

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-textract-adapter.html#cfn-textract-adapter-featuretypes
        '''
        result = self._values.get("feature_types")
        assert result is not None, "Required property 'feature_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def auto_update(self) -> typing.Optional[builtins.str]:
        '''Controls whether or not the adapter should automatically update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-textract-adapter.html#cfn-textract-adapter-autoupdate
        '''
        result = self._values.get("auto_update")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to be assigned to the adapter being created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-textract-adapter.html#cfn-textract-adapter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of tags to be added to the adapter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-textract-adapter.html#cfn-textract-adapter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAdapterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAdapter",
    "CfnAdapterProps",
]

publication.publish()

def _typecheckingstub__555f33b4aad2e420ef9286245345e979caff74e1e0aceacbf51327f9834fb61a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    adapter_name: builtins.str,
    feature_types: typing.Sequence[builtins.str],
    auto_update: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ae8a77fa4d2c88e87cf44241930124ce4c53c0ca73615fe0ae9f1f8e7afec6(
    resource: _aws_textract_57016ef5.IAdapterRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f00c3e712bf4dc730d0bd04de4e302211a803b7761428ed312e60ff05f9e3ffb(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c21046e584df63b93e670e418b3cc1c057937c2ee21a67eccd0728ae29b20a34(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c10f26f0f43422aacba582208443d077c03e6a97f933cecda8e0fd72d1ef245(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__886799141ec01d9ea2256cdd67c42848de7514b954cbc32a9a45142e19239c70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f67f376a5f036b73076099b32edec76b4a3e394b4b7e6ffa024728429f2ded(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92784ab97d9f6b538830e8b8c6e734b14585910aed4e3b92082a8ca10a868078(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c194f2a4e32c6be061592ea92cc999e7aae364cb78e15a7e0a130d3d25d37ff1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c908c24c1c9cac33f554e9c732d8ca205501a6b08d9e40758143fe0f056096(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f4d32a5e348a57106397cb1043cf755c90945ad2972f38f3cdba1b054dfa49f(
    *,
    adapter_name: builtins.str,
    feature_types: typing.Sequence[builtins.str],
    auto_update: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
