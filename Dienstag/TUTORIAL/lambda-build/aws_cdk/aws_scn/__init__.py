r'''
# AWS::SCN Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_scn as scn
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SCN construct libraries](https://constructs.dev/search?q=scn)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SCN resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SCN.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SCN](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SCN.html).

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
    import aws_cdk.interfaces.aws_scn as _aws_scn_c02cfff3
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_scn_c02cfff3 = _LazyImport("aws_cdk.interfaces.aws_scn")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_scn_c02cfff3.IDataIntegrationFlowRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnDataIntegrationFlow(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow",
):
    '''Represents an AWS Supply Chain data integration flow.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataintegrationflow.html
    :cloudformationResource: AWS::SCN::DataIntegrationFlow
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_scn as scn
        
        cfn_data_integration_flow = scn.CfnDataIntegrationFlow(self, "MyCfnDataIntegrationFlow",
            instance_id="instanceId",
            name="name",
            sources=[scn.CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty(
                source_name="sourceName",
                source_type="sourceType",
        
                # the properties below are optional
                dataset_source=scn.CfnDataIntegrationFlow.DatasetSourceConfigurationProperty(
                    dataset_identifier="datasetIdentifier",
        
                    # the properties below are optional
                    options=scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                        dedupe_records=False,
                        dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                            type="type",
        
                            # the properties below are optional
                            field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                                fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                    name="name",
                                    sort_order="sortOrder"
                                )]
                            )
                        ),
                        load_type="loadType"
                    )
                ),
                s3_source=scn.CfnDataIntegrationFlow.S3SourceConfigurationProperty(
                    bucket_name="bucketName",
                    prefix="prefix",
        
                    # the properties below are optional
                    options=scn.CfnDataIntegrationFlow.S3OptionsProperty(
                        file_type="fileType"
                    )
                )
            )],
            target=scn.CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty(
                target_type="targetType",
        
                # the properties below are optional
                dataset_target=scn.CfnDataIntegrationFlow.DatasetTargetConfigurationProperty(
                    dataset_identifier="datasetIdentifier",
        
                    # the properties below are optional
                    options=scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                        dedupe_records=False,
                        dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                            type="type",
        
                            # the properties below are optional
                            field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                                fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                    name="name",
                                    sort_order="sortOrder"
                                )]
                            )
                        ),
                        load_type="loadType"
                    )
                )
            ),
            transformation=scn.CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty(
                transformation_type="transformationType",
        
                # the properties below are optional
                sql_transformation=scn.CfnDataIntegrationFlow.SqlTransformationConfigurationProperty(
                    query="query"
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
        instance_id: builtins.str,
        name: builtins.str,
        sources: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        target: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty", typing.Dict[builtins.str, typing.Any]]],
        transformation: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SCN::DataIntegrationFlow``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_id: The Amazon Web Services Supply Chain instance identifier.
        :param name: The name of the DataIntegrationFlow.
        :param sources: The source configurations for the DataIntegrationFlow.
        :param target: The DataIntegrationFlow target parameters.
        :param transformation: The DataIntegrationFlow transformation parameters.
        :param tags: The tags for the DataIntegrationFlow.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c861bd22c83042fae89a369505911a23b7b3a123d711242c38ce48ba21bbadd8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataIntegrationFlowProps(
            instance_id=instance_id,
            name=name,
            sources=sources,
            target=target,
            transformation=transformation,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDataIntegrationFlow")
    @builtins.classmethod
    def arn_for_data_integration_flow(
        cls,
        resource: "_aws_scn_c02cfff3.IDataIntegrationFlowRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__89f4136f3e2e1a912bb6594d91b516e21e0008cbb3b8c5c638f7c5b667ba3d85)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDataIntegrationFlow", [resource]))

    @jsii.member(jsii_name="isCfnDataIntegrationFlow")
    @builtins.classmethod
    def is_cfn_data_integration_flow(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDataIntegrationFlow.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6fcbeefa7d23d57d359a9b7911e18e16d7f55ed900029b80499b8ce93f450069)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDataIntegrationFlow", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c2fbc3edc6e854b7914849bf32a083198be059da49b8867a9f87294419cbf8cb)
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
            type_hints = cached_type_hints(_typecheckingstub__41b1d6114f9df421afeda92936e8421c67b03fe9126b7a506b3f01b3360cfe0c)
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
        '''The Amazon Resource Name (ARN) of the DataIntegrationFlow.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''The creation time of the DataIntegrationFlow.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''The last modified time of the DataIntegrationFlow.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

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
    @jsii.member(jsii_name="dataIntegrationFlowRef")
    def data_integration_flow_ref(
        self,
    ) -> "_aws_scn_c02cfff3.DataIntegrationFlowReference":
        '''A reference to a DataIntegrationFlow resource.'''
        return typing.cast("_aws_scn_c02cfff3.DataIntegrationFlowReference", jsii.get(self, "dataIntegrationFlowRef"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Amazon Web Services Supply Chain instance identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__de0acbd95c506da8bc3016915b20dbb875bcfd23301e1fe85e499ab5fd0a867d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the DataIntegrationFlow.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__eae3b43b763a82d3c4e65e16cee6f8ff1aa3cb6f1857e6afec8d53fa14bf8a9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty"]]]:
        '''The source configurations for the DataIntegrationFlow.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty"]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bc36d52be1d6ea8db516074239c41cd6b31cbac111e39faf24f1f099d6e83053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty"]:
        '''The DataIntegrationFlow target parameters.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty"], jsii.get(self, "target"))

    @target.setter
    def target(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6693bf50c5128fa82109f4d91d8c6869d3f947548f5b46592e4d0b0e94834fd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="transformation")
    def transformation(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty"]:
        '''The DataIntegrationFlow transformation parameters.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty"], jsii.get(self, "transformation"))

    @transformation.setter
    def transformation(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b4236450b032246d6a39b497a1363689422f70bf1b306c48720aeddab4db0072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transformation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the DataIntegrationFlow.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a131009bc141a31f64f6ff524630ae9a45fd63fb375764a1cf60bd320454d932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_name": "sourceName",
            "source_type": "sourceType",
            "dataset_source": "datasetSource",
            "s3_source": "s3Source",
        },
    )
    class DataIntegrationFlowSourceProperty:
        def __init__(
            self,
            *,
            source_name: builtins.str,
            source_type: builtins.str,
            dataset_source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DatasetSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.S3SourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The DataIntegrationFlow source parameters.

            :param source_name: The source name that can be used as table alias in SQL transformation query.
            :param source_type: The source type.
            :param dataset_source: The dataset source configuration parameters.
            :param s3_source: The S3 source configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                data_integration_flow_source_property = scn.CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty(
                    source_name="sourceName",
                    source_type="sourceType",
                
                    # the properties below are optional
                    dataset_source=scn.CfnDataIntegrationFlow.DatasetSourceConfigurationProperty(
                        dataset_identifier="datasetIdentifier",
                
                        # the properties below are optional
                        options=scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                            dedupe_records=False,
                            dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                                type="type",
                
                                # the properties below are optional
                                field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                                    fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                        name="name",
                                        sort_order="sortOrder"
                                    )]
                                )
                            ),
                            load_type="loadType"
                        )
                    ),
                    s3_source=scn.CfnDataIntegrationFlow.S3SourceConfigurationProperty(
                        bucket_name="bucketName",
                        prefix="prefix",
                
                        # the properties below are optional
                        options=scn.CfnDataIntegrationFlow.S3OptionsProperty(
                            file_type="fileType"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__648f395366f0dad4e3dc96cf1c9ee97dc59335ee195740237c6288818e844383)
                check_type(argname="argument source_name", value=source_name, expected_type=type_hints["source_name"])
                check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
                check_type(argname="argument dataset_source", value=dataset_source, expected_type=type_hints["dataset_source"])
                check_type(argname="argument s3_source", value=s3_source, expected_type=type_hints["s3_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_name": source_name,
                "source_type": source_type,
            }
            if dataset_source is not None:
                self._values["dataset_source"] = dataset_source
            if s3_source is not None:
                self._values["s3_source"] = s3_source

        @builtins.property
        def source_name(self) -> builtins.str:
            '''The source name that can be used as table alias in SQL transformation query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowsource.html#cfn-scn-dataintegrationflow-dataintegrationflowsource-sourcename
            '''
            result = self._values.get("source_name")
            assert result is not None, "Required property 'source_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_type(self) -> builtins.str:
            '''The source type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowsource.html#cfn-scn-dataintegrationflow-dataintegrationflowsource-sourcetype
            '''
            result = self._values.get("source_type")
            assert result is not None, "Required property 'source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dataset_source(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DatasetSourceConfigurationProperty"]]:
            '''The dataset source configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowsource.html#cfn-scn-dataintegrationflow-dataintegrationflowsource-datasetsource
            '''
            result = self._values.get("dataset_source")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DatasetSourceConfigurationProperty"]], result)

        @builtins.property
        def s3_source(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.S3SourceConfigurationProperty"]]:
            '''The S3 source configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowsource.html#cfn-scn-dataintegrationflow-dataintegrationflowsource-s3source
            '''
            result = self._values.get("s3_source")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.S3SourceConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataIntegrationFlowSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"target_type": "targetType", "dataset_target": "datasetTarget"},
    )
    class DataIntegrationFlowTargetProperty:
        def __init__(
            self,
            *,
            target_type: builtins.str,
            dataset_target: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DatasetTargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The DataIntegrationFlow target parameters.

            :param target_type: The target type.
            :param dataset_target: The dataset target configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowtarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                data_integration_flow_target_property = scn.CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty(
                    target_type="targetType",
                
                    # the properties below are optional
                    dataset_target=scn.CfnDataIntegrationFlow.DatasetTargetConfigurationProperty(
                        dataset_identifier="datasetIdentifier",
                
                        # the properties below are optional
                        options=scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                            dedupe_records=False,
                            dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                                type="type",
                
                                # the properties below are optional
                                field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                                    fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                        name="name",
                                        sort_order="sortOrder"
                                    )]
                                )
                            ),
                            load_type="loadType"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__05ff02c354716ca33f6945b309f9d38bdaa9d52b60ecabaa4b1d6d6b5ba6b051)
                check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
                check_type(argname="argument dataset_target", value=dataset_target, expected_type=type_hints["dataset_target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_type": target_type,
            }
            if dataset_target is not None:
                self._values["dataset_target"] = dataset_target

        @builtins.property
        def target_type(self) -> builtins.str:
            '''The target type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowtarget.html#cfn-scn-dataintegrationflow-dataintegrationflowtarget-targettype
            '''
            result = self._values.get("target_type")
            assert result is not None, "Required property 'target_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dataset_target(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DatasetTargetConfigurationProperty"]]:
            '''The dataset target configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowtarget.html#cfn-scn-dataintegrationflow-dataintegrationflowtarget-datasettarget
            '''
            result = self._values.get("dataset_target")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DatasetTargetConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataIntegrationFlowTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "transformation_type": "transformationType",
            "sql_transformation": "sqlTransformation",
        },
    )
    class DataIntegrationFlowTransformationProperty:
        def __init__(
            self,
            *,
            transformation_type: builtins.str,
            sql_transformation: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.SqlTransformationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The DataIntegrationFlow transformation parameters.

            :param transformation_type: The transformation type.
            :param sql_transformation: The SQL transformation configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowtransformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                data_integration_flow_transformation_property = scn.CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty(
                    transformation_type="transformationType",
                
                    # the properties below are optional
                    sql_transformation=scn.CfnDataIntegrationFlow.SqlTransformationConfigurationProperty(
                        query="query"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d83e465d4b6300c044f3926d7e392917fa342d35e29c06f7631290aafa863f18)
                check_type(argname="argument transformation_type", value=transformation_type, expected_type=type_hints["transformation_type"])
                check_type(argname="argument sql_transformation", value=sql_transformation, expected_type=type_hints["sql_transformation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "transformation_type": transformation_type,
            }
            if sql_transformation is not None:
                self._values["sql_transformation"] = sql_transformation

        @builtins.property
        def transformation_type(self) -> builtins.str:
            '''The transformation type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowtransformation.html#cfn-scn-dataintegrationflow-dataintegrationflowtransformation-transformationtype
            '''
            result = self._values.get("transformation_type")
            assert result is not None, "Required property 'transformation_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_transformation(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.SqlTransformationConfigurationProperty"]]:
            '''The SQL transformation configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dataintegrationflowtransformation.html#cfn-scn-dataintegrationflow-dataintegrationflowtransformation-sqltransformation
            '''
            result = self._values.get("sql_transformation")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.SqlTransformationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataIntegrationFlowTransformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.DatasetOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dedupe_records": "dedupeRecords",
            "dedupe_strategy": "dedupeStrategy",
            "load_type": "loadType",
        },
    )
    class DatasetOptionsProperty:
        def __init__(
            self,
            *,
            dedupe_records: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            dedupe_strategy: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DedupeStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            load_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The dataset options.

            :param dedupe_records: The option to perform deduplication on data records sharing same primary key values.
            :param dedupe_strategy: The deduplication strategy.
            :param load_type: The load type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasetoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                dataset_options_property = scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                    dedupe_records=False,
                    dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                        type="type",
                
                        # the properties below are optional
                        field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                            fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                name="name",
                                sort_order="sortOrder"
                            )]
                        )
                    ),
                    load_type="loadType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__b502239a24d0f57334572ea93dfa918bb458005651afee46f541afcf841c51a9)
                check_type(argname="argument dedupe_records", value=dedupe_records, expected_type=type_hints["dedupe_records"])
                check_type(argname="argument dedupe_strategy", value=dedupe_strategy, expected_type=type_hints["dedupe_strategy"])
                check_type(argname="argument load_type", value=load_type, expected_type=type_hints["load_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dedupe_records is not None:
                self._values["dedupe_records"] = dedupe_records
            if dedupe_strategy is not None:
                self._values["dedupe_strategy"] = dedupe_strategy
            if load_type is not None:
                self._values["load_type"] = load_type

        @builtins.property
        def dedupe_records(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''The option to perform deduplication on data records sharing same primary key values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasetoptions.html#cfn-scn-dataintegrationflow-datasetoptions-deduperecords
            '''
            result = self._values.get("dedupe_records")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def dedupe_strategy(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DedupeStrategyProperty"]]:
            '''The deduplication strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasetoptions.html#cfn-scn-dataintegrationflow-datasetoptions-dedupestrategy
            '''
            result = self._values.get("dedupe_strategy")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DedupeStrategyProperty"]], result)

        @builtins.property
        def load_type(self) -> typing.Optional[builtins.str]:
            '''The load type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasetoptions.html#cfn-scn-dataintegrationflow-datasetoptions-loadtype
            '''
            result = self._values.get("load_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.DatasetSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"dataset_identifier": "datasetIdentifier", "options": "options"},
    )
    class DatasetSourceConfigurationProperty:
        def __init__(
            self,
            *,
            dataset_identifier: builtins.str,
            options: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DatasetOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The dataset source configuration parameters.

            :param dataset_identifier: The ARN of the dataset.
            :param options: The dataset options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasetsourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                dataset_source_configuration_property = scn.CfnDataIntegrationFlow.DatasetSourceConfigurationProperty(
                    dataset_identifier="datasetIdentifier",
                
                    # the properties below are optional
                    options=scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                        dedupe_records=False,
                        dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                            type="type",
                
                            # the properties below are optional
                            field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                                fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                    name="name",
                                    sort_order="sortOrder"
                                )]
                            )
                        ),
                        load_type="loadType"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__73acee648d866db276f1215d3e3abe59b183892fdf7725e7001efa105456b35c)
                check_type(argname="argument dataset_identifier", value=dataset_identifier, expected_type=type_hints["dataset_identifier"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dataset_identifier": dataset_identifier,
            }
            if options is not None:
                self._values["options"] = options

        @builtins.property
        def dataset_identifier(self) -> builtins.str:
            '''The ARN of the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasetsourceconfiguration.html#cfn-scn-dataintegrationflow-datasetsourceconfiguration-datasetidentifier
            '''
            result = self._values.get("dataset_identifier")
            assert result is not None, "Required property 'dataset_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def options(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DatasetOptionsProperty"]]:
            '''The dataset options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasetsourceconfiguration.html#cfn-scn-dataintegrationflow-datasetsourceconfiguration-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DatasetOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.DatasetTargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"dataset_identifier": "datasetIdentifier", "options": "options"},
    )
    class DatasetTargetConfigurationProperty:
        def __init__(
            self,
            *,
            dataset_identifier: builtins.str,
            options: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DatasetOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The dataset target configuration parameters.

            :param dataset_identifier: The dataset ARN.
            :param options: The dataset options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasettargetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                dataset_target_configuration_property = scn.CfnDataIntegrationFlow.DatasetTargetConfigurationProperty(
                    dataset_identifier="datasetIdentifier",
                
                    # the properties below are optional
                    options=scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                        dedupe_records=False,
                        dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                            type="type",
                
                            # the properties below are optional
                            field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                                fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                    name="name",
                                    sort_order="sortOrder"
                                )]
                            )
                        ),
                        load_type="loadType"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__dea2d4d4cbb0c76586b0384ea662560b4279e840ec1043b1077aa0b72a708c29)
                check_type(argname="argument dataset_identifier", value=dataset_identifier, expected_type=type_hints["dataset_identifier"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dataset_identifier": dataset_identifier,
            }
            if options is not None:
                self._values["options"] = options

        @builtins.property
        def dataset_identifier(self) -> builtins.str:
            '''The dataset ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasettargetconfiguration.html#cfn-scn-dataintegrationflow-datasettargetconfiguration-datasetidentifier
            '''
            result = self._values.get("dataset_identifier")
            assert result is not None, "Required property 'dataset_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def options(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DatasetOptionsProperty"]]:
            '''The dataset options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-datasettargetconfiguration.html#cfn-scn-dataintegrationflow-datasettargetconfiguration-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DatasetOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetTargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.DedupeStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "field_priority": "fieldPriority"},
    )
    class DedupeStrategyProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            field_priority: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The deduplication strategy.

            :param type: The deduplication strategy type.
            :param field_priority: The field priority deduplication strategy configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dedupestrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                dedupe_strategy_property = scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                    type="type",
                
                    # the properties below are optional
                    field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                        fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                            name="name",
                            sort_order="sortOrder"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__63141d07eb182efc74aeadc49cbfc1e3077f448727186c5de53d7d8f065e7ce8)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument field_priority", value=field_priority, expected_type=type_hints["field_priority"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if field_priority is not None:
                self._values["field_priority"] = field_priority

        @builtins.property
        def type(self) -> builtins.str:
            '''The deduplication strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dedupestrategy.html#cfn-scn-dataintegrationflow-dedupestrategy-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field_priority(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty"]]:
            '''The field priority deduplication strategy configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-dedupestrategy.html#cfn-scn-dataintegrationflow-dedupestrategy-fieldpriority
            '''
            result = self._values.get("field_priority")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DedupeStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sort_order": "sortOrder"},
    )
    class FieldPriorityDedupeFieldProperty:
        def __init__(self, *, name: builtins.str, sort_order: builtins.str) -> None:
            '''A deduplication field.

            :param name: The name of the deduplication field.
            :param sort_order: The sort order.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-fieldprioritydedupefield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                field_priority_dedupe_field_property = scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                    name="name",
                    sort_order="sortOrder"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__4a32f65228bcb8164a32555a13ae818c2bcadd29d8fc6d26f503b6bdb59201f7)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sort_order", value=sort_order, expected_type=type_hints["sort_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "sort_order": sort_order,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the deduplication field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-fieldprioritydedupefield.html#cfn-scn-dataintegrationflow-fieldprioritydedupefield-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sort_order(self) -> builtins.str:
            '''The sort order.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-fieldprioritydedupefield.html#cfn-scn-dataintegrationflow-fieldprioritydedupefield-sortorder
            '''
            result = self._values.get("sort_order")
            assert result is not None, "Required property 'sort_order' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldPriorityDedupeFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"fields": "fields"},
    )
    class FieldPriorityDedupeStrategyConfigurationProperty:
        def __init__(
            self,
            *,
            fields: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The field priority deduplication strategy configuration.

            :param fields: The list of field names and their sort order for deduplication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-fieldprioritydedupestrategyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                field_priority_dedupe_strategy_configuration_property = scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                    fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                        name="name",
                        sort_order="sortOrder"
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0631ea44a54ce68d8fd71d130cbcd0d149a84cc4d0f8965f581c4fe3407a4582)
                check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fields": fields,
            }

        @builtins.property
        def fields(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty"]]]:
            '''The list of field names and their sort order for deduplication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-fieldprioritydedupestrategyconfiguration.html#cfn-scn-dataintegrationflow-fieldprioritydedupestrategyconfiguration-fields
            '''
            result = self._values.get("fields")
            assert result is not None, "Required property 'fields' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldPriorityDedupeStrategyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.S3OptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"file_type": "fileType"},
    )
    class S3OptionsProperty:
        def __init__(self, *, file_type: typing.Optional[builtins.str] = None) -> None:
            '''The Amazon S3 options.

            :param file_type: The file type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-s3options.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                s3_options_property = scn.CfnDataIntegrationFlow.S3OptionsProperty(
                    file_type="fileType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1668a565befa3528bebb3ef0ee60214d64f05046453c504eb03161a2f163838d)
                check_type(argname="argument file_type", value=file_type, expected_type=type_hints["file_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if file_type is not None:
                self._values["file_type"] = file_type

        @builtins.property
        def file_type(self) -> typing.Optional[builtins.str]:
            '''The file type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-s3options.html#cfn-scn-dataintegrationflow-s3options-filetype
            '''
            result = self._values.get("file_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.S3SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "prefix": "prefix",
            "options": "options",
        },
    )
    class S3SourceConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            prefix: builtins.str,
            options: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.S3OptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The S3 source configuration parameters.

            :param bucket_name: The S3 bucket name.
            :param prefix: The S3 prefix.
            :param options: The Amazon S3 options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-s3sourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                s3_source_configuration_property = scn.CfnDataIntegrationFlow.S3SourceConfigurationProperty(
                    bucket_name="bucketName",
                    prefix="prefix",
                
                    # the properties below are optional
                    options=scn.CfnDataIntegrationFlow.S3OptionsProperty(
                        file_type="fileType"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0bd4807f12c06202a291824e00f8f757e98fd0f51a2279ef1fd6b09d10542e51)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "prefix": prefix,
            }
            if options is not None:
                self._values["options"] = options

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-s3sourceconfiguration.html#cfn-scn-dataintegrationflow-s3sourceconfiguration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prefix(self) -> builtins.str:
            '''The S3 prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-s3sourceconfiguration.html#cfn-scn-dataintegrationflow-s3sourceconfiguration-prefix
            '''
            result = self._values.get("prefix")
            assert result is not None, "Required property 'prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def options(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.S3OptionsProperty"]]:
            '''The Amazon S3 options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-s3sourceconfiguration.html#cfn-scn-dataintegrationflow-s3sourceconfiguration-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.S3OptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlow.SqlTransformationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"query": "query"},
    )
    class SqlTransformationConfigurationProperty:
        def __init__(self, *, query: builtins.str) -> None:
            '''The SQL transformation configuration parameters.

            :param query: The transformation SQL query body based on SparkSQL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-sqltransformationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                sql_transformation_configuration_property = scn.CfnDataIntegrationFlow.SqlTransformationConfigurationProperty(
                    query="query"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1747a906c0431f5e984168eda35be39a55cd30cd402837f456f378b16c522307)
                check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "query": query,
            }

        @builtins.property
        def query(self) -> builtins.str:
            '''The transformation SQL query body based on SparkSQL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataintegrationflow-sqltransformationconfiguration.html#cfn-scn-dataintegrationflow-sqltransformationconfiguration-query
            '''
            result = self._values.get("query")
            assert result is not None, "Required property 'query' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqlTransformationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scn.CfnDataIntegrationFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_id": "instanceId",
        "name": "name",
        "sources": "sources",
        "target": "target",
        "transformation": "transformation",
        "tags": "tags",
    },
)
class CfnDataIntegrationFlowProps:
    def __init__(
        self,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        sources: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        target: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty", typing.Dict[builtins.str, typing.Any]]],
        transformation: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataIntegrationFlow``.

        :param instance_id: The Amazon Web Services Supply Chain instance identifier.
        :param name: The name of the DataIntegrationFlow.
        :param sources: The source configurations for the DataIntegrationFlow.
        :param target: The DataIntegrationFlow target parameters.
        :param transformation: The DataIntegrationFlow transformation parameters.
        :param tags: The tags for the DataIntegrationFlow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataintegrationflow.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scn as scn
            
            cfn_data_integration_flow_props = scn.CfnDataIntegrationFlowProps(
                instance_id="instanceId",
                name="name",
                sources=[scn.CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty(
                    source_name="sourceName",
                    source_type="sourceType",
            
                    # the properties below are optional
                    dataset_source=scn.CfnDataIntegrationFlow.DatasetSourceConfigurationProperty(
                        dataset_identifier="datasetIdentifier",
            
                        # the properties below are optional
                        options=scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                            dedupe_records=False,
                            dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                                type="type",
            
                                # the properties below are optional
                                field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                                    fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                        name="name",
                                        sort_order="sortOrder"
                                    )]
                                )
                            ),
                            load_type="loadType"
                        )
                    ),
                    s3_source=scn.CfnDataIntegrationFlow.S3SourceConfigurationProperty(
                        bucket_name="bucketName",
                        prefix="prefix",
            
                        # the properties below are optional
                        options=scn.CfnDataIntegrationFlow.S3OptionsProperty(
                            file_type="fileType"
                        )
                    )
                )],
                target=scn.CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty(
                    target_type="targetType",
            
                    # the properties below are optional
                    dataset_target=scn.CfnDataIntegrationFlow.DatasetTargetConfigurationProperty(
                        dataset_identifier="datasetIdentifier",
            
                        # the properties below are optional
                        options=scn.CfnDataIntegrationFlow.DatasetOptionsProperty(
                            dedupe_records=False,
                            dedupe_strategy=scn.CfnDataIntegrationFlow.DedupeStrategyProperty(
                                type="type",
            
                                # the properties below are optional
                                field_priority=scn.CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty(
                                    fields=[scn.CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty(
                                        name="name",
                                        sort_order="sortOrder"
                                    )]
                                )
                            ),
                            load_type="loadType"
                        )
                    )
                ),
                transformation=scn.CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty(
                    transformation_type="transformationType",
            
                    # the properties below are optional
                    sql_transformation=scn.CfnDataIntegrationFlow.SqlTransformationConfigurationProperty(
                        query="query"
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
            type_hints = cached_type_hints(_typecheckingstub__0841ed65c1206011f80abde77695fa169572cf446013fe89b53878125c152de8)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument transformation", value=transformation, expected_type=type_hints["transformation"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
            "sources": sources,
            "target": target,
            "transformation": transformation,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The Amazon Web Services Supply Chain instance identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataintegrationflow.html#cfn-scn-dataintegrationflow-instanceid
        '''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the DataIntegrationFlow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataintegrationflow.html#cfn-scn-dataintegrationflow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty"]]]:
        '''The source configurations for the DataIntegrationFlow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataintegrationflow.html#cfn-scn-dataintegrationflow-sources
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty"]]], result)

    @builtins.property
    def target(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty"]:
        '''The DataIntegrationFlow target parameters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataintegrationflow.html#cfn-scn-dataintegrationflow-target
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty"], result)

    @builtins.property
    def transformation(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty"]:
        '''The DataIntegrationFlow transformation parameters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataintegrationflow.html#cfn-scn-dataintegrationflow-transformation
        '''
        result = self._values.get("transformation")
        assert result is not None, "Required property 'transformation' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the DataIntegrationFlow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataintegrationflow.html#cfn-scn-dataintegrationflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataIntegrationFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_scn_c02cfff3.IDatasetRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnDataset(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scn.CfnDataset",
):
    '''Represents an AWS Supply Chain data lake dataset.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html
    :cloudformationResource: AWS::SCN::Dataset
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_scn as scn
        
        cfn_dataset = scn.CfnDataset(self, "MyCfnDataset",
            instance_id="instanceId",
            name="name",
            namespace="namespace",
        
            # the properties below are optional
            description="description",
            partition_spec=scn.CfnDataset.PartitionSpecProperty(
                fields=[scn.CfnDataset.DataLakeDatasetPartitionFieldProperty(
                    name="name",
                    transform=scn.CfnDataset.TransformProperty(
                        type="type"
                    )
                )]
            ),
            schema=scn.CfnDataset.SchemaProperty(
                fields=[scn.CfnDataset.DataLakeDatasetSchemaFieldProperty(
                    is_required=False,
                    name="name",
                    type="type"
                )],
                name="name",
        
                # the properties below are optional
                primary_keys=[scn.CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty(
                    name="name"
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
        instance_id: builtins.str,
        name: builtins.str,
        namespace: builtins.str,
        description: typing.Optional[builtins.str] = None,
        partition_spec: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataset.PartitionSpecProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schema: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataset.SchemaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SCN::Dataset``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_id: The Amazon Web Services Supply Chain instance identifier.
        :param name: The name of the dataset.
        :param namespace: The namespace of the dataset.
        :param description: The description of the dataset.
        :param partition_spec: The partition specification of the dataset.
        :param schema: The schema of the dataset.
        :param tags: The tags for the dataset.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__190557729091c09211becb4695232c6b7ee875f32e7b38ba31b9f53825686eda)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetProps(
            instance_id=instance_id,
            name=name,
            namespace=namespace,
            description=description,
            partition_spec=partition_spec,
            schema=schema,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDataset")
    @builtins.classmethod
    def arn_for_dataset(cls, resource: "_aws_scn_c02cfff3.IDatasetRef") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7a159fa5cc85a26e1772dd130543169a1b015e39ba59eca0dca0e905a67ab1c8)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDataset", [resource]))

    @jsii.member(jsii_name="isCfnDataset")
    @builtins.classmethod
    def is_cfn_dataset(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDataset.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5c3612143d1ebda75cead47c2a407674d15ae2cbc81c6b0ea847155991964a13)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDataset", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b790c490148793cf7fb42be0d1176aa29321d647e95a540c651051fee776f2a5)
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
            type_hints = cached_type_hints(_typecheckingstub__6fe88d9dee7bbee9a271e0f0761b5a4edce4a0e0953c46809f3dc14ced2dda38)
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
        '''The Amazon Resource Name (ARN) of the dataset.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''The creation time of the dataset.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''The last modified time of the dataset.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

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
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "_aws_scn_c02cfff3.DatasetReference":
        '''A reference to a Dataset resource.'''
        return typing.cast("_aws_scn_c02cfff3.DatasetReference", jsii.get(self, "datasetRef"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Amazon Web Services Supply Chain instance identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__692b7e7db8335f2e0849f40229f7963c4d88c5439354b01731f720276adc02a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__afbf74d724cd07020c49e9d530618c340846ce91b7d8e8936a39aacf79662783)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        '''The namespace of the dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dd550a20a7abd2f4bbce813cc29868733c58ad8b4e43d6ae02fb745cae96cd8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the dataset.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c0f9becb179b4e013eb95c1ea2434d272e31cb319586e56bef27fbc2290dbb8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="partitionSpec")
    def partition_spec(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.PartitionSpecProperty"]]:
        '''The partition specification of the dataset.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.PartitionSpecProperty"]], jsii.get(self, "partitionSpec"))

    @partition_spec.setter
    def partition_spec(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.PartitionSpecProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d40c701ff04c187ea21ddadf1c8c0dde296e31f0f8281bf7dd0f396c7171b93e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionSpec", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.SchemaProperty"]]:
        '''The schema of the dataset.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.SchemaProperty"]], jsii.get(self, "schema"))

    @schema.setter
    def schema(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.SchemaProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e224fd996762cfe8cde3dd60c907edfe9f2161c254ac5b2e3518304b306d2878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the dataset.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__92a856a654b31354d129a109309153c7905d19f534e8f7ca4c892d4356a1afee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataset.DataLakeDatasetPartitionFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "transform": "transform"},
    )
    class DataLakeDatasetPartitionFieldProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            transform: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataset.TransformProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The partition field details.

            :param name: The name of the partition field.
            :param transform: The transformation of the partition field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetpartitionfield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                data_lake_dataset_partition_field_property = scn.CfnDataset.DataLakeDatasetPartitionFieldProperty(
                    name="name",
                    transform=scn.CfnDataset.TransformProperty(
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e7f696b88e2a40a8469748704e76ed8f598825c6ff4f8879be55739770866c98)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument transform", value=transform, expected_type=type_hints["transform"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "transform": transform,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the partition field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetpartitionfield.html#cfn-scn-dataset-datalakedatasetpartitionfield-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def transform(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.TransformProperty"]:
            '''The transformation of the partition field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetpartitionfield.html#cfn-scn-dataset-datalakedatasetpartitionfield-transform
            '''
            result = self._values.get("transform")
            assert result is not None, "Required property 'transform' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.TransformProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakeDatasetPartitionFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class DataLakeDatasetPrimaryKeyFieldProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''The primary key field details.

            :param name: The name of the primary key field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetprimarykeyfield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                data_lake_dataset_primary_key_field_property = scn.CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1720f2d066e37077bab908779ab357421247c57b4d867dcf5dbb014b2c7be916)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the primary key field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetprimarykeyfield.html#cfn-scn-dataset-datalakedatasetprimarykeyfield-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakeDatasetPrimaryKeyFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataset.DataLakeDatasetSchemaFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"is_required": "isRequired", "name": "name", "type": "type"},
    )
    class DataLakeDatasetSchemaFieldProperty:
        def __init__(
            self,
            *,
            is_required: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
            name: builtins.str,
            type: builtins.str,
        ) -> None:
            '''The dataset field details.

            :param is_required: Indicate if the field is required or not.
            :param name: The dataset field name.
            :param type: The dataset field type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetschemafield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                data_lake_dataset_schema_field_property = scn.CfnDataset.DataLakeDatasetSchemaFieldProperty(
                    is_required=False,
                    name="name",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2c66d5d1a202effa625bba4f6cf4784aa0fde8a510b4c762dd4e57f6e46009ce)
                check_type(argname="argument is_required", value=is_required, expected_type=type_hints["is_required"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_required": is_required,
                "name": name,
                "type": type,
            }

        @builtins.property
        def is_required(
            self,
        ) -> typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]:
            '''Indicate if the field is required or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetschemafield.html#cfn-scn-dataset-datalakedatasetschemafield-isrequired
            '''
            result = self._values.get("is_required")
            assert result is not None, "Required property 'is_required' is missing"
            return typing.cast(typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The dataset field name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetschemafield.html#cfn-scn-dataset-datalakedatasetschemafield-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The dataset field type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-datalakedatasetschemafield.html#cfn-scn-dataset-datalakedatasetschemafield-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakeDatasetSchemaFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataset.PartitionSpecProperty",
        jsii_struct_bases=[],
        name_mapping={"fields": "fields"},
    )
    class PartitionSpecProperty:
        def __init__(
            self,
            *,
            fields: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataset.DataLakeDatasetPartitionFieldProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The partition specification of the dataset.

            :param fields: The partition fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-partitionspec.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                partition_spec_property = scn.CfnDataset.PartitionSpecProperty(
                    fields=[scn.CfnDataset.DataLakeDatasetPartitionFieldProperty(
                        name="name",
                        transform=scn.CfnDataset.TransformProperty(
                            type="type"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f1fe2cd105d48079074053db97f3bf0fc560f4a333feef3029b66bf1e9e54d01)
                check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fields": fields,
            }

        @builtins.property
        def fields(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.DataLakeDatasetPartitionFieldProperty"]]]:
            '''The partition fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-partitionspec.html#cfn-scn-dataset-partitionspec-fields
            '''
            result = self._values.get("fields")
            assert result is not None, "Required property 'fields' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.DataLakeDatasetPartitionFieldProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PartitionSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataset.SchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fields": "fields",
            "name": "name",
            "primary_keys": "primaryKeys",
        },
    )
    class SchemaProperty:
        def __init__(
            self,
            *,
            fields: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataset.DataLakeDatasetSchemaFieldProperty", typing.Dict[builtins.str, typing.Any]]]]],
            name: builtins.str,
            primary_keys: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The schema of the dataset.

            :param fields: The list of field details of the dataset schema.
            :param name: The name of the dataset schema.
            :param primary_keys: The list of primary key fields for the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-schema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                schema_property = scn.CfnDataset.SchemaProperty(
                    fields=[scn.CfnDataset.DataLakeDatasetSchemaFieldProperty(
                        is_required=False,
                        name="name",
                        type="type"
                    )],
                    name="name",
                
                    # the properties below are optional
                    primary_keys=[scn.CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty(
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1d4bc9550c2e0a5edba637fc034e0d4947ea0989884034e5fcd41166d43e1b6d)
                check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument primary_keys", value=primary_keys, expected_type=type_hints["primary_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fields": fields,
                "name": name,
            }
            if primary_keys is not None:
                self._values["primary_keys"] = primary_keys

        @builtins.property
        def fields(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.DataLakeDatasetSchemaFieldProperty"]]]:
            '''The list of field details of the dataset schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-schema.html#cfn-scn-dataset-schema-fields
            '''
            result = self._values.get("fields")
            assert result is not None, "Required property 'fields' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.DataLakeDatasetSchemaFieldProperty"]]], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the dataset schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-schema.html#cfn-scn-dataset-schema-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def primary_keys(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty"]]]]:
            '''The list of primary key fields for the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-schema.html#cfn-scn-dataset-schema-primarykeys
            '''
            result = self._values.get("primary_keys")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scn.CfnDataset.TransformProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class TransformProperty:
        def __init__(self, *, type: builtins.str) -> None:
            '''The transformation of the partition field.

            :param type: The type of partitioning transformation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-transform.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scn as scn
                
                transform_property = scn.CfnDataset.TransformProperty(
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__fc8ad7a0883f2995f608556418aa7c01fe5a719736f71dde0367de7bb24df83b)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of partitioning transformation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scn-dataset-transform.html#cfn-scn-dataset-transform-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scn.CfnDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_id": "instanceId",
        "name": "name",
        "namespace": "namespace",
        "description": "description",
        "partition_spec": "partitionSpec",
        "schema": "schema",
        "tags": "tags",
    },
)
class CfnDatasetProps:
    def __init__(
        self,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        namespace: builtins.str,
        description: typing.Optional[builtins.str] = None,
        partition_spec: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataset.PartitionSpecProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schema: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataset.SchemaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataset``.

        :param instance_id: The Amazon Web Services Supply Chain instance identifier.
        :param name: The name of the dataset.
        :param namespace: The namespace of the dataset.
        :param description: The description of the dataset.
        :param partition_spec: The partition specification of the dataset.
        :param schema: The schema of the dataset.
        :param tags: The tags for the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scn as scn
            
            cfn_dataset_props = scn.CfnDatasetProps(
                instance_id="instanceId",
                name="name",
                namespace="namespace",
            
                # the properties below are optional
                description="description",
                partition_spec=scn.CfnDataset.PartitionSpecProperty(
                    fields=[scn.CfnDataset.DataLakeDatasetPartitionFieldProperty(
                        name="name",
                        transform=scn.CfnDataset.TransformProperty(
                            type="type"
                        )
                    )]
                ),
                schema=scn.CfnDataset.SchemaProperty(
                    fields=[scn.CfnDataset.DataLakeDatasetSchemaFieldProperty(
                        is_required=False,
                        name="name",
                        type="type"
                    )],
                    name="name",
            
                    # the properties below are optional
                    primary_keys=[scn.CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty(
                        name="name"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__299d7f5b18e1bef7e601c53bd182755b210309da5167a84ba8050cb8c0a2d313)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument partition_spec", value=partition_spec, expected_type=type_hints["partition_spec"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
            "namespace": namespace,
        }
        if description is not None:
            self._values["description"] = description
        if partition_spec is not None:
            self._values["partition_spec"] = partition_spec
        if schema is not None:
            self._values["schema"] = schema
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The Amazon Web Services Supply Chain instance identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html#cfn-scn-dataset-instanceid
        '''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html#cfn-scn-dataset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace of the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html#cfn-scn-dataset-namespace
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html#cfn-scn-dataset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition_spec(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.PartitionSpecProperty"]]:
        '''The partition specification of the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html#cfn-scn-dataset-partitionspec
        '''
        result = self._values.get("partition_spec")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.PartitionSpecProperty"]], result)

    @builtins.property
    def schema(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.SchemaProperty"]]:
        '''The schema of the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html#cfn-scn-dataset-schema
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataset.SchemaProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-dataset.html#cfn-scn-dataset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_scn_c02cfff3.INamespaceRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnNamespace(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scn.CfnNamespace",
):
    '''Definition of AWS::SCN::Namespace Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-namespace.html
    :cloudformationResource: AWS::SCN::Namespace
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_scn as scn
        
        cfn_namespace = scn.CfnNamespace(self, "MyCfnNamespace",
            instance_id="instanceId",
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
        instance_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SCN::Namespace``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_id: The Amazon Web Services Supply Chain instance identifier.
        :param name: The name of the namespace.
        :param description: The description of the namespace.
        :param tags: The tags for the namespace.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4d5966f297271dae5701ca51fe627717863b15caf21e1583334c983f40f9f7a9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNamespaceProps(
            instance_id=instance_id, name=name, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForNamespace")
    @builtins.classmethod
    def arn_for_namespace(
        cls,
        resource: "_aws_scn_c02cfff3.INamespaceRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5bc932032c6305f3eaa2a9a7b416aa6ed72ce033769c6d3a1331500084d1009b)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForNamespace", [resource]))

    @jsii.member(jsii_name="isCfnNamespace")
    @builtins.classmethod
    def is_cfn_namespace(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnNamespace.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e58eed01efa356d4d5125fb4ebc36fb2d694d765a483747b61c0091b6b975917)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnNamespace", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ecf45f508296ed744d9b7ef554868d595567eb96cb864b97dab6a1b78f94b4b5)
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
            type_hints = cached_type_hints(_typecheckingstub__6e280f6e065dc722931671355e660b5d8c3a9041f0ae06b712fb1fcb57ddc40b)
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
        '''The Amazon Resource Name (ARN) of the namespace.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''The creation time of the namespace.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''The last modified time of the namespace.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

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
    @jsii.member(jsii_name="namespaceRef")
    def namespace_ref(self) -> "_aws_scn_c02cfff3.NamespaceReference":
        '''A reference to a Namespace resource.'''
        return typing.cast("_aws_scn_c02cfff3.NamespaceReference", jsii.get(self, "namespaceRef"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Amazon Web Services Supply Chain instance identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6e5d84e27e9d28c80923ddf02c7c43dca9dcaaf46f75b9a03e6ca4c07aa6e17a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ed3d5b5ce1af9df35b4e0ca6205eb4ce434bde8152bc328c1d313aa216175bee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__92d4124f9f87273eaf6513746fb6c5981af5affcbdc1655259fe5fe8cf52b259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the namespace.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b91005fd3dce91447888e36ccdf4f9a89c6bb1a6c80d831c4d54a26af70aec03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scn.CfnNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_id": "instanceId",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnNamespaceProps:
    def __init__(
        self,
        *,
        instance_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnNamespace``.

        :param instance_id: The Amazon Web Services Supply Chain instance identifier.
        :param name: The name of the namespace.
        :param description: The description of the namespace.
        :param tags: The tags for the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-namespace.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scn as scn
            
            cfn_namespace_props = scn.CfnNamespaceProps(
                instance_id="instanceId",
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
            type_hints = cached_type_hints(_typecheckingstub__03f4456a34163a1ef81bc2953e6889069a0a7a67cda8cac84a1250eb4cccfa64)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The Amazon Web Services Supply Chain instance identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-namespace.html#cfn-scn-namespace-instanceid
        '''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-namespace.html#cfn-scn-namespace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-namespace.html#cfn-scn-namespace-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scn-namespace.html#cfn-scn-namespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataIntegrationFlow",
    "CfnDataIntegrationFlowProps",
    "CfnDataset",
    "CfnDatasetProps",
    "CfnNamespace",
    "CfnNamespaceProps",
]

publication.publish()

def _typecheckingstub__c861bd22c83042fae89a369505911a23b7b3a123d711242c38ce48ba21bbadd8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_id: builtins.str,
    name: builtins.str,
    sources: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    target: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty, typing.Dict[builtins.str, typing.Any]]],
    transformation: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f4136f3e2e1a912bb6594d91b516e21e0008cbb3b8c5c638f7c5b667ba3d85(
    resource: _aws_scn_c02cfff3.IDataIntegrationFlowRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fcbeefa7d23d57d359a9b7911e18e16d7f55ed900029b80499b8ce93f450069(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2fbc3edc6e854b7914849bf32a083198be059da49b8867a9f87294419cbf8cb(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b1d6114f9df421afeda92936e8421c67b03fe9126b7a506b3f01b3360cfe0c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de0acbd95c506da8bc3016915b20dbb875bcfd23301e1fe85e499ab5fd0a867d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae3b43b763a82d3c4e65e16cee6f8ff1aa3cb6f1857e6afec8d53fa14bf8a9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc36d52be1d6ea8db516074239c41cd6b31cbac111e39faf24f1f099d6e83053(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6693bf50c5128fa82109f4d91d8c6869d3f947548f5b46592e4d0b0e94834fd2(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4236450b032246d6a39b497a1363689422f70bf1b306c48720aeddab4db0072(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a131009bc141a31f64f6ff524630ae9a45fd63fb375764a1cf60bd320454d932(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648f395366f0dad4e3dc96cf1c9ee97dc59335ee195740237c6288818e844383(
    *,
    source_name: builtins.str,
    source_type: builtins.str,
    dataset_source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DatasetSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.S3SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05ff02c354716ca33f6945b309f9d38bdaa9d52b60ecabaa4b1d6d6b5ba6b051(
    *,
    target_type: builtins.str,
    dataset_target: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DatasetTargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d83e465d4b6300c044f3926d7e392917fa342d35e29c06f7631290aafa863f18(
    *,
    transformation_type: builtins.str,
    sql_transformation: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.SqlTransformationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b502239a24d0f57334572ea93dfa918bb458005651afee46f541afcf841c51a9(
    *,
    dedupe_records: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    dedupe_strategy: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DedupeStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    load_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73acee648d866db276f1215d3e3abe59b183892fdf7725e7001efa105456b35c(
    *,
    dataset_identifier: builtins.str,
    options: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DatasetOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea2d4d4cbb0c76586b0384ea662560b4279e840ec1043b1077aa0b72a708c29(
    *,
    dataset_identifier: builtins.str,
    options: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DatasetOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63141d07eb182efc74aeadc49cbfc1e3077f448727186c5de53d7d8f065e7ce8(
    *,
    type: builtins.str,
    field_priority: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.FieldPriorityDedupeStrategyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a32f65228bcb8164a32555a13ae818c2bcadd29d8fc6d26f503b6bdb59201f7(
    *,
    name: builtins.str,
    sort_order: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0631ea44a54ce68d8fd71d130cbcd0d149a84cc4d0f8965f581c4fe3407a4582(
    *,
    fields: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.FieldPriorityDedupeFieldProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1668a565befa3528bebb3ef0ee60214d64f05046453c504eb03161a2f163838d(
    *,
    file_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bd4807f12c06202a291824e00f8f757e98fd0f51a2279ef1fd6b09d10542e51(
    *,
    bucket_name: builtins.str,
    prefix: builtins.str,
    options: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.S3OptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1747a906c0431f5e984168eda35be39a55cd30cd402837f456f378b16c522307(
    *,
    query: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0841ed65c1206011f80abde77695fa169572cf446013fe89b53878125c152de8(
    *,
    instance_id: builtins.str,
    name: builtins.str,
    sources: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DataIntegrationFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    target: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DataIntegrationFlowTargetProperty, typing.Dict[builtins.str, typing.Any]]],
    transformation: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataIntegrationFlow.DataIntegrationFlowTransformationProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__190557729091c09211becb4695232c6b7ee875f32e7b38ba31b9f53825686eda(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_id: builtins.str,
    name: builtins.str,
    namespace: builtins.str,
    description: typing.Optional[builtins.str] = None,
    partition_spec: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataset.PartitionSpecProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schema: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataset.SchemaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a159fa5cc85a26e1772dd130543169a1b015e39ba59eca0dca0e905a67ab1c8(
    resource: _aws_scn_c02cfff3.IDatasetRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c3612143d1ebda75cead47c2a407674d15ae2cbc81c6b0ea847155991964a13(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b790c490148793cf7fb42be0d1176aa29321d647e95a540c651051fee776f2a5(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fe88d9dee7bbee9a271e0f0761b5a4edce4a0e0953c46809f3dc14ced2dda38(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__692b7e7db8335f2e0849f40229f7963c4d88c5439354b01731f720276adc02a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afbf74d724cd07020c49e9d530618c340846ce91b7d8e8936a39aacf79662783(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd550a20a7abd2f4bbce813cc29868733c58ad8b4e43d6ae02fb745cae96cd8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f9becb179b4e013eb95c1ea2434d272e31cb319586e56bef27fbc2290dbb8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d40c701ff04c187ea21ddadf1c8c0dde296e31f0f8281bf7dd0f396c7171b93e(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnDataset.PartitionSpecProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e224fd996762cfe8cde3dd60c907edfe9f2161c254ac5b2e3518304b306d2878(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnDataset.SchemaProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a856a654b31354d129a109309153c7905d19f534e8f7ca4c892d4356a1afee(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f696b88e2a40a8469748704e76ed8f598825c6ff4f8879be55739770866c98(
    *,
    name: builtins.str,
    transform: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataset.TransformProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1720f2d066e37077bab908779ab357421247c57b4d867dcf5dbb014b2c7be916(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c66d5d1a202effa625bba4f6cf4784aa0fde8a510b4c762dd4e57f6e46009ce(
    *,
    is_required: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
    name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1fe2cd105d48079074053db97f3bf0fc560f4a333feef3029b66bf1e9e54d01(
    *,
    fields: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataset.DataLakeDatasetPartitionFieldProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d4bc9550c2e0a5edba637fc034e0d4947ea0989884034e5fcd41166d43e1b6d(
    *,
    fields: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataset.DataLakeDatasetSchemaFieldProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    primary_keys: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataset.DataLakeDatasetPrimaryKeyFieldProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8ad7a0883f2995f608556418aa7c01fe5a719736f71dde0367de7bb24df83b(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299d7f5b18e1bef7e601c53bd182755b210309da5167a84ba8050cb8c0a2d313(
    *,
    instance_id: builtins.str,
    name: builtins.str,
    namespace: builtins.str,
    description: typing.Optional[builtins.str] = None,
    partition_spec: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataset.PartitionSpecProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schema: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataset.SchemaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5966f297271dae5701ca51fe627717863b15caf21e1583334c983f40f9f7a9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_id: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc932032c6305f3eaa2a9a7b416aa6ed72ce033769c6d3a1331500084d1009b(
    resource: _aws_scn_c02cfff3.INamespaceRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e58eed01efa356d4d5125fb4ebc36fb2d694d765a483747b61c0091b6b975917(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf45f508296ed744d9b7ef554868d595567eb96cb864b97dab6a1b78f94b4b5(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e280f6e065dc722931671355e660b5d8c3a9041f0ae06b712fb1fcb57ddc40b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e5d84e27e9d28c80923ddf02c7c43dca9dcaaf46f75b9a03e6ca4c07aa6e17a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed3d5b5ce1af9df35b4e0ca6205eb4ce434bde8152bc328c1d313aa216175bee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d4124f9f87273eaf6513746fb6c5981af5affcbdc1655259fe5fe8cf52b259(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91005fd3dce91447888e36ccdf4f9a89c6bb1a6c80d831c4d54a26af70aec03(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f4456a34163a1ef81bc2953e6889069a0a7a67cda8cac84a1250eb4cccfa64(
    *,
    instance_id: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
