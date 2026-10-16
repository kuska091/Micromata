r'''
# AWS::DataExchange Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_dataexchange as dataexchange
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DataExchange construct libraries](https://constructs.dev/search?q=dataexchange)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DataExchange resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataExchange.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DataExchange](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataExchange.html).

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
    import aws_cdk.interfaces.aws_dataexchange as _aws_dataexchange_7cdcf7e6
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_dataexchange_7cdcf7e6 = _LazyImport("aws_cdk.interfaces.aws_dataexchange")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_dataexchange_7cdcf7e6.IDataSetRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnDataSet(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dataexchange.CfnDataSet",
):
    '''Definition of AWS::DataExchange::DataSet Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-dataset.html
    :cloudformationResource: AWS::DataExchange::DataSet
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dataexchange as dataexchange
        
        cfn_data_set = dataexchange.CfnDataSet(self, "MyCfnDataSet",
            asset_type="assetType",
            description="description",
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
        asset_type: builtins.str,
        description: builtins.str,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DataExchange::DataSet``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param asset_type: The type of asset that is added to a data set.
        :param description: A description for the data set.
        :param name: The name of the data set.
        :param tags: Tags for the data set.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a28579e0b5d792e18a73b4a7a6a53d3e87bb9f2ef8d642f855b0e59905197a9d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataSetProps(
            asset_type=asset_type, description=description, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDataSet")
    @builtins.classmethod
    def arn_for_data_set(
        cls,
        resource: "_aws_dataexchange_7cdcf7e6.IDataSetRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__949a098ef187fbd111ad95e815b82ec82f525a8b94a05f9b3f8def2012711d60)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDataSet", [resource]))

    @jsii.member(jsii_name="isCfnDataSet")
    @builtins.classmethod
    def is_cfn_data_set(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDataSet.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4a4fffde5cff33c8ac3ee62bfdd3e4be3c5ce316b97610c61e6f651973f687da)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDataSet", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e10294eba07830ac5b7e2f71017eccef104c6416e96f5665e1cd9ae45666d5ec)
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
            type_hints = cached_type_hints(_typecheckingstub__d991976313e4d2bf74ef0e74f4a20a3b1c237257c5b91eaa0fe2961365b756f3)
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
        '''The ARN for the data set.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the data set was created, in ISO 8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier for the data set.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrOrigin")
    def attr_origin(self) -> builtins.str:
        '''A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).

        :cloudformationAttribute: Origin
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOrigin"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The date and time that the data set was last updated, in ISO 8601 format.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="dataSetRef")
    def data_set_ref(self) -> "_aws_dataexchange_7cdcf7e6.DataSetReference":
        '''A reference to a DataSet resource.'''
        return typing.cast("_aws_dataexchange_7cdcf7e6.DataSetReference", jsii.get(self, "dataSetRef"))

    @builtins.property
    @jsii.member(jsii_name="assetType")
    def asset_type(self) -> builtins.str:
        '''The type of asset that is added to a data set.'''
        return typing.cast(builtins.str, jsii.get(self, "assetType"))

    @asset_type.setter
    def asset_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8ad50ba7f16d0aab02ed2f94e82f428d8eb2db6f33c7c76b56c3e3b5132850da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description for the data set.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7b1d99e273b036153036e40905f29974ba146ac2e8ea236f711c41cfd0576373)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the data set.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__31ac5f7226097bbf76b507334ed212b144769406f12d7834fb44609d064dae2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags for the data set.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8e82204d87f1853c063f5e710da8cabb8392aea08eef2ed8930b6acd0f51c391)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dataexchange.CfnDataSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "asset_type": "assetType",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnDataSetProps:
    def __init__(
        self,
        *,
        asset_type: builtins.str,
        description: builtins.str,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataSet``.

        :param asset_type: The type of asset that is added to a data set.
        :param description: A description for the data set.
        :param name: The name of the data set.
        :param tags: Tags for the data set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-dataset.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dataexchange as dataexchange
            
            cfn_data_set_props = dataexchange.CfnDataSetProps(
                asset_type="assetType",
                description="description",
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9c9088cac499341e75980fb2960ff5f751a7c0251338aa82eb734c076141da7b)
            check_type(argname="argument asset_type", value=asset_type, expected_type=type_hints["asset_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset_type": asset_type,
            "description": description,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def asset_type(self) -> builtins.str:
        '''The type of asset that is added to a data set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-dataset.html#cfn-dataexchange-dataset-assettype
        '''
        result = self._values.get("asset_type")
        assert result is not None, "Required property 'asset_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''A description for the data set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-dataset.html#cfn-dataexchange-dataset-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the data set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-dataset.html#cfn-dataexchange-dataset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags for the data set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-dataset.html#cfn-dataexchange-dataset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_dataexchange_7cdcf7e6.IEventActionRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnEventAction(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dataexchange.CfnEventAction",
):
    '''An event action is an AWS Data Exchange resource that automatically exports data set revisions to Amazon S3 when a revision is published.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-eventaction.html
    :cloudformationResource: AWS::DataExchange::EventAction
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dataexchange as dataexchange
        
        cfn_event_action = dataexchange.CfnEventAction(self, "MyCfnEventAction",
            action=dataexchange.CfnEventAction.ActionProperty(
                export_revision_to_s3=dataexchange.CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty(
                    revision_destination=dataexchange.CfnEventAction.AutoExportRevisionDestinationEntryProperty(
                        bucket="bucket",
        
                        # the properties below are optional
                        key_pattern="keyPattern"
                    ),
        
                    # the properties below are optional
                    encryption=dataexchange.CfnEventAction.ExportServerSideEncryptionProperty(
                        type="type",
        
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn"
                    )
                )
            ),
            event=dataexchange.CfnEventAction.EventProperty(
                revision_published=dataexchange.CfnEventAction.RevisionPublishedProperty(
                    data_set_id="dataSetId"
                )
            ),
        
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
        action: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventAction.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
        event: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventAction.EventProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DataExchange::EventAction``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action: What occurs after a certain event.
        :param event: What occurs to start an action.
        :param tags: The tags for the event action.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9338ea917a7b87d379ebb514898af4e17383c411595b1e392e4e117bd2c2b07d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventActionProps(action=action, event=event, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForEventAction")
    @builtins.classmethod
    def arn_for_event_action(
        cls,
        resource: "_aws_dataexchange_7cdcf7e6.IEventActionRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3389b720e6e950cbfc69f7f93256cb311dcd2f367df791ca293676cb90f1f28d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForEventAction", [resource]))

    @jsii.member(jsii_name="isCfnEventAction")
    @builtins.classmethod
    def is_cfn_event_action(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnEventAction.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__840f9729fce08039051185ff17b6e2543c68a09c49686679b6dad8f4016318f0)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnEventAction", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b88d9a6e0a19f8e7901e3c0905ae6be689c5f9b8ad85061f0ea5cb8c46f017da)
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
            type_hints = cached_type_hints(_typecheckingstub__fbadbbc3b743d0e543c75ebc0c6eea907e87015b69ba6f0e03cdf5030af2880f)
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
        '''The ARN for the event action.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the event action was created, in ISO 8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEventActionId")
    def attr_event_action_id(self) -> builtins.str:
        '''The unique identifier for the event action.

        :cloudformationAttribute: EventActionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventActionId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The date and time that the event action was last updated, in ISO 8601 format.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="eventActionRef")
    def event_action_ref(self) -> "_aws_dataexchange_7cdcf7e6.EventActionReference":
        '''A reference to a EventAction resource.'''
        return typing.cast("_aws_dataexchange_7cdcf7e6.EventActionReference", jsii.get(self, "eventActionRef"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.ActionProperty"]:
        '''What occurs after a certain event.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.ActionProperty"], jsii.get(self, "action"))

    @action.setter
    def action(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.ActionProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__36b6ad451c37e76fa6b001fbfd070eae686a1f2c56e91afe46bdd7e0fd4ae6f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="event")
    def event(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.EventProperty"]:
        '''What occurs to start an action.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.EventProperty"], jsii.get(self, "event"))

    @event.setter
    def event(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.EventProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8bd6e6cd70128f3dffcb2e2d66fe081a32c3d9701bd2f84dab6d249a859dac84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "event", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the event action.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__17694973311bcb5930306f0ac654a12367a4315755e7ff285dc317dbcc3e7adb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dataexchange.CfnEventAction.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"export_revision_to_s3": "exportRevisionToS3"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            export_revision_to_s3: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''What occurs after a certain event.

            :param export_revision_to_s3: Details of the operation to be performed by the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dataexchange as dataexchange
                
                action_property = dataexchange.CfnEventAction.ActionProperty(
                    export_revision_to_s3=dataexchange.CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty(
                        revision_destination=dataexchange.CfnEventAction.AutoExportRevisionDestinationEntryProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            key_pattern="keyPattern"
                        ),
                
                        # the properties below are optional
                        encryption=dataexchange.CfnEventAction.ExportServerSideEncryptionProperty(
                            type="type",
                
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8486d28986ea85ab73b71886583641bf71072313a44ac1bdc008c8444835aea1)
                check_type(argname="argument export_revision_to_s3", value=export_revision_to_s3, expected_type=type_hints["export_revision_to_s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if export_revision_to_s3 is not None:
                self._values["export_revision_to_s3"] = export_revision_to_s3

        @builtins.property
        def export_revision_to_s3(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty"]]:
            '''Details of the operation to be performed by the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-action.html#cfn-dataexchange-eventaction-action-exportrevisiontos3
            '''
            result = self._values.get("export_revision_to_s3")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dataexchange.CfnEventAction.AutoExportRevisionDestinationEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key_pattern": "keyPattern"},
    )
    class AutoExportRevisionDestinationEntryProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key_pattern: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A revision destination is the Amazon S3 bucket folder destination to where the export will be sent.

            :param bucket: The Amazon S3 bucket that is the destination for the event action.
            :param key_pattern: A string representing the pattern for generated names of the individual assets in the revision.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-autoexportrevisiondestinationentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dataexchange as dataexchange
                
                auto_export_revision_destination_entry_property = dataexchange.CfnEventAction.AutoExportRevisionDestinationEntryProperty(
                    bucket="bucket",
                
                    # the properties below are optional
                    key_pattern="keyPattern"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6a2631caf25675139fba654f5e400e3c52ed4f1edc0ceabe5dd769f225cd8a91)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key_pattern", value=key_pattern, expected_type=type_hints["key_pattern"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
            }
            if key_pattern is not None:
                self._values["key_pattern"] = key_pattern

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The Amazon S3 bucket that is the destination for the event action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-autoexportrevisiondestinationentry.html#cfn-dataexchange-eventaction-autoexportrevisiondestinationentry-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_pattern(self) -> typing.Optional[builtins.str]:
            '''A string representing the pattern for generated names of the individual assets in the revision.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-autoexportrevisiondestinationentry.html#cfn-dataexchange-eventaction-autoexportrevisiondestinationentry-keypattern
            '''
            result = self._values.get("key_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoExportRevisionDestinationEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dataexchange.CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "revision_destination": "revisionDestination",
            "encryption": "encryption",
        },
    )
    class AutoExportRevisionToS3RequestDetailsProperty:
        def __init__(
            self,
            *,
            revision_destination: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventAction.AutoExportRevisionDestinationEntryProperty", typing.Dict[builtins.str, typing.Any]]],
            encryption: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventAction.ExportServerSideEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Details of the operation to be performed by the job.

            :param revision_destination: A revision destination is the Amazon S3 bucket folder destination to where the export will be sent.
            :param encryption: Encryption configuration of the export job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-autoexportrevisiontos3requestdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dataexchange as dataexchange
                
                auto_export_revision_to_s3_request_details_property = dataexchange.CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty(
                    revision_destination=dataexchange.CfnEventAction.AutoExportRevisionDestinationEntryProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        key_pattern="keyPattern"
                    ),
                
                    # the properties below are optional
                    encryption=dataexchange.CfnEventAction.ExportServerSideEncryptionProperty(
                        type="type",
                
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d5fa27e6f9db08a8b12d2906352770d6b5356450954766a2f4a0c6dce7d6b0d8)
                check_type(argname="argument revision_destination", value=revision_destination, expected_type=type_hints["revision_destination"])
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "revision_destination": revision_destination,
            }
            if encryption is not None:
                self._values["encryption"] = encryption

        @builtins.property
        def revision_destination(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.AutoExportRevisionDestinationEntryProperty"]:
            '''A revision destination is the Amazon S3 bucket folder destination to where the export will be sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-autoexportrevisiontos3requestdetails.html#cfn-dataexchange-eventaction-autoexportrevisiontos3requestdetails-revisiondestination
            '''
            result = self._values.get("revision_destination")
            assert result is not None, "Required property 'revision_destination' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.AutoExportRevisionDestinationEntryProperty"], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.ExportServerSideEncryptionProperty"]]:
            '''Encryption configuration of the export job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-autoexportrevisiontos3requestdetails.html#cfn-dataexchange-eventaction-autoexportrevisiontos3requestdetails-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.ExportServerSideEncryptionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoExportRevisionToS3RequestDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dataexchange.CfnEventAction.EventProperty",
        jsii_struct_bases=[],
        name_mapping={"revision_published": "revisionPublished"},
    )
    class EventProperty:
        def __init__(
            self,
            *,
            revision_published: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventAction.RevisionPublishedProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''What occurs to start an action.

            :param revision_published: Information about the published revision.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-event.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dataexchange as dataexchange
                
                event_property = dataexchange.CfnEventAction.EventProperty(
                    revision_published=dataexchange.CfnEventAction.RevisionPublishedProperty(
                        data_set_id="dataSetId"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__63af77b4f6117936c8860391ac05b0552f2f0a4c740df919a337a8d167ddfce8)
                check_type(argname="argument revision_published", value=revision_published, expected_type=type_hints["revision_published"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if revision_published is not None:
                self._values["revision_published"] = revision_published

        @builtins.property
        def revision_published(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.RevisionPublishedProperty"]]:
            '''Information about the published revision.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-event.html#cfn-dataexchange-eventaction-event-revisionpublished
            '''
            result = self._values.get("revision_published")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.RevisionPublishedProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dataexchange.CfnEventAction.ExportServerSideEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "kms_key_arn": "kmsKeyArn"},
    )
    class ExportServerSideEncryptionProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Encryption configuration of the export job.

            :param type: The type of server side encryption used for encrypting the objects in Amazon S3.
            :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS KMS key you want to use to encrypt the Amazon S3 objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-exportserversideencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dataexchange as dataexchange
                
                export_server_side_encryption_property = dataexchange.CfnEventAction.ExportServerSideEncryptionProperty(
                    type="type",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d4a8f5bfb5ec664d2506621bacf5dfb4481e5334a1a12102ec987b49e7801ce2)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of server side encryption used for encrypting the objects in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-exportserversideencryption.html#cfn-dataexchange-eventaction-exportserversideencryption-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the AWS KMS key you want to use to encrypt the Amazon S3 objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-exportserversideencryption.html#cfn-dataexchange-eventaction-exportserversideencryption-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExportServerSideEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dataexchange.CfnEventAction.RevisionPublishedProperty",
        jsii_struct_bases=[],
        name_mapping={"data_set_id": "dataSetId"},
    )
    class RevisionPublishedProperty:
        def __init__(self, *, data_set_id: builtins.str) -> None:
            '''Information about the published revision.

            :param data_set_id: The data set ID of the published revision.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-revisionpublished.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dataexchange as dataexchange
                
                revision_published_property = dataexchange.CfnEventAction.RevisionPublishedProperty(
                    data_set_id="dataSetId"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__7b0bcc5ce6d77f5fae231a5ee1f80d1561ea840f460f1cc63716173076dda2e1)
                check_type(argname="argument data_set_id", value=data_set_id, expected_type=type_hints["data_set_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_set_id": data_set_id,
            }

        @builtins.property
        def data_set_id(self) -> builtins.str:
            '''The data set ID of the published revision.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dataexchange-eventaction-revisionpublished.html#cfn-dataexchange-eventaction-revisionpublished-datasetid
            '''
            result = self._values.get("data_set_id")
            assert result is not None, "Required property 'data_set_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RevisionPublishedProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dataexchange.CfnEventActionProps",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "event": "event", "tags": "tags"},
)
class CfnEventActionProps:
    def __init__(
        self,
        *,
        action: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventAction.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
        event: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEventAction.EventProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventAction``.

        :param action: What occurs after a certain event.
        :param event: What occurs to start an action.
        :param tags: The tags for the event action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-eventaction.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dataexchange as dataexchange
            
            cfn_event_action_props = dataexchange.CfnEventActionProps(
                action=dataexchange.CfnEventAction.ActionProperty(
                    export_revision_to_s3=dataexchange.CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty(
                        revision_destination=dataexchange.CfnEventAction.AutoExportRevisionDestinationEntryProperty(
                            bucket="bucket",
            
                            # the properties below are optional
                            key_pattern="keyPattern"
                        ),
            
                        # the properties below are optional
                        encryption=dataexchange.CfnEventAction.ExportServerSideEncryptionProperty(
                            type="type",
            
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        )
                    )
                ),
                event=dataexchange.CfnEventAction.EventProperty(
                    revision_published=dataexchange.CfnEventAction.RevisionPublishedProperty(
                        data_set_id="dataSetId"
                    )
                ),
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9da1bfa0e66b0f0ce0061f77a52099d8a1c2521f336cf0d7f2ec6bc86e14286b)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "event": event,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.ActionProperty"]:
        '''What occurs after a certain event.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-eventaction.html#cfn-dataexchange-eventaction-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.ActionProperty"], result)

    @builtins.property
    def event(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.EventProperty"]:
        '''What occurs to start an action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-eventaction.html#cfn-dataexchange-eventaction-event
        '''
        result = self._values.get("event")
        assert result is not None, "Required property 'event' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEventAction.EventProperty"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the event action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dataexchange-eventaction.html#cfn-dataexchange-eventaction-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataSet",
    "CfnDataSetProps",
    "CfnEventAction",
    "CfnEventActionProps",
]

publication.publish()

def _typecheckingstub__a28579e0b5d792e18a73b4a7a6a53d3e87bb9f2ef8d642f855b0e59905197a9d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    asset_type: builtins.str,
    description: builtins.str,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__949a098ef187fbd111ad95e815b82ec82f525a8b94a05f9b3f8def2012711d60(
    resource: _aws_dataexchange_7cdcf7e6.IDataSetRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4fffde5cff33c8ac3ee62bfdd3e4be3c5ce316b97610c61e6f651973f687da(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e10294eba07830ac5b7e2f71017eccef104c6416e96f5665e1cd9ae45666d5ec(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d991976313e4d2bf74ef0e74f4a20a3b1c237257c5b91eaa0fe2961365b756f3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad50ba7f16d0aab02ed2f94e82f428d8eb2db6f33c7c76b56c3e3b5132850da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1d99e273b036153036e40905f29974ba146ac2e8ea236f711c41cfd0576373(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31ac5f7226097bbf76b507334ed212b144769406f12d7834fb44609d064dae2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e82204d87f1853c063f5e710da8cabb8392aea08eef2ed8930b6acd0f51c391(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9088cac499341e75980fb2960ff5f751a7c0251338aa82eb734c076141da7b(
    *,
    asset_type: builtins.str,
    description: builtins.str,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9338ea917a7b87d379ebb514898af4e17383c411595b1e392e4e117bd2c2b07d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventAction.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    event: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventAction.EventProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3389b720e6e950cbfc69f7f93256cb311dcd2f367df791ca293676cb90f1f28d(
    resource: _aws_dataexchange_7cdcf7e6.IEventActionRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__840f9729fce08039051185ff17b6e2543c68a09c49686679b6dad8f4016318f0(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88d9a6e0a19f8e7901e3c0905ae6be689c5f9b8ad85061f0ea5cb8c46f017da(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbadbbc3b743d0e543c75ebc0c6eea907e87015b69ba6f0e03cdf5030af2880f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b6ad451c37e76fa6b001fbfd070eae686a1f2c56e91afe46bdd7e0fd4ae6f9(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnEventAction.ActionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd6e6cd70128f3dffcb2e2d66fe081a32c3d9701bd2f84dab6d249a859dac84(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnEventAction.EventProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17694973311bcb5930306f0ac654a12367a4315755e7ff285dc317dbcc3e7adb(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8486d28986ea85ab73b71886583641bf71072313a44ac1bdc008c8444835aea1(
    *,
    export_revision_to_s3: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventAction.AutoExportRevisionToS3RequestDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a2631caf25675139fba654f5e400e3c52ed4f1edc0ceabe5dd769f225cd8a91(
    *,
    bucket: builtins.str,
    key_pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5fa27e6f9db08a8b12d2906352770d6b5356450954766a2f4a0c6dce7d6b0d8(
    *,
    revision_destination: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventAction.AutoExportRevisionDestinationEntryProperty, typing.Dict[builtins.str, typing.Any]]],
    encryption: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventAction.ExportServerSideEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63af77b4f6117936c8860391ac05b0552f2f0a4c740df919a337a8d167ddfce8(
    *,
    revision_published: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventAction.RevisionPublishedProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4a8f5bfb5ec664d2506621bacf5dfb4481e5334a1a12102ec987b49e7801ce2(
    *,
    type: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0bcc5ce6d77f5fae231a5ee1f80d1561ea840f460f1cc63716173076dda2e1(
    *,
    data_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9da1bfa0e66b0f0ce0061f77a52099d8a1c2521f336cf0d7f2ec6bc86e14286b(
    *,
    action: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventAction.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    event: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEventAction.EventProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
