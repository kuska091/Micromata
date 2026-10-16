r'''
# AWS::NeptuneGraph Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_neptunegraph as neptunegraph
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NeptuneGraph construct libraries](https://constructs.dev/search?q=neptunegraph)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NeptuneGraph resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NeptuneGraph.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NeptuneGraph](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NeptuneGraph.html).

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
    import aws_cdk.interfaces.aws_neptunegraph as _aws_neptunegraph_1ac4a341
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_neptunegraph_1ac4a341 = _LazyImport("aws_cdk.interfaces.aws_neptunegraph")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_neptunegraph_1ac4a341.IGraphRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnGraph(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraph",
):
    '''The ``AWS ::NeptuneGraph::Graph`` resource creates an  graph.

    is a memory-optimized graph database engine for analytics. For more information, see ` <https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html>`_ .

    You can use ``AWS ::NeptuneGraph::Graph.DeletionProtection`` to help guard against unintended deletion of your graph.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html
    :cloudformationResource: AWS::NeptuneGraph::Graph
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_neptunegraph as neptunegraph
        
        cfn_graph = neptunegraph.CfnGraph(self, "MyCfnGraph",
            provisioned_memory=123,
        
            # the properties below are optional
            deletion_protection=False,
            graph_name="graphName",
            import_task=neptunegraph.CfnGraph.ImportTaskProperty(
                role_arn="roleArn",
                source="source",
        
                # the properties below are optional
                blank_node_handling="blankNodeHandling",
                fail_on_error=False,
                format="format",
                import_options=neptunegraph.CfnGraph.ImportOptionsProperty(
                    neptune=neptunegraph.CfnGraph.NeptuneImportOptionsProperty(
                        s3_export_kms_key_id="s3ExportKmsKeyId",
                        s3_export_path="s3ExportPath",
        
                        # the properties below are optional
                        preserve_default_vertex_labels=False,
                        preserve_edge_ids=False
                    )
                ),
                max_provisioned_memory=123,
                min_provisioned_memory=123,
                parquet_type="parquetType"
            ),
            kms_key_identifier="kmsKeyIdentifier",
            public_connectivity=False,
            replica_count=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vector_search_configuration=neptunegraph.CfnGraph.VectorSearchConfigurationProperty(
                vector_search_dimension=123
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        provisioned_memory: jsii.Number,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        graph_name: typing.Optional[builtins.str] = None,
        import_task: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnGraph.ImportTaskProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        public_connectivity: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_search_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnGraph.VectorSearchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::NeptuneGraph::Graph``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param provisioned_memory: The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16
        :param deletion_protection: A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
        :param graph_name: The graph name. For example: ``my-graph-1`` . The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. If you don't specify a graph name, a unique graph name is generated for you using the prefix ``graph-for`` , followed by a combination of ``Stack Name`` and a ``UUID`` .
        :param import_task: The import task details to import data into the graph at creation time.
        :param kms_key_identifier: The ARN of the KMS key used to encrypt data in the Neptune Analytics graph. If not specified, the graph is encrypted with an AWS managed key.
        :param public_connectivity: Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. When the graph is publicly available, its domain name system (DNS) endpoint resolves to the public IP address from the internet. When the graph isn't publicly available, you need to create a ``PrivateGraphEndpoint`` in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC. Default: If not specified, the default value is false. .. epigraph:: If enabling public connectivity for the first time, there will be a delay while it is enabled.
        :param replica_count: The number of replicas in other AZs. Default: If not specified, the default value is 1.
        :param tags: Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
        :param vector_search_configuration: Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as ``dimension=`` value. Max = 65,535
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e963857650d4e99964bc9bad7da0b29a5d2d3c66d3452d1e9b4f35e89330e04b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphProps(
            provisioned_memory=provisioned_memory,
            deletion_protection=deletion_protection,
            graph_name=graph_name,
            import_task=import_task,
            kms_key_identifier=kms_key_identifier,
            public_connectivity=public_connectivity,
            replica_count=replica_count,
            tags=tags,
            vector_search_configuration=vector_search_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForGraph")
    @builtins.classmethod
    def arn_for_graph(
        cls,
        resource: "_aws_neptunegraph_1ac4a341.IGraphRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7c6900d1428655c3b11dde92fc61e291887db2224b4c48e95c00434783fbaa82)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForGraph", [resource]))

    @jsii.member(jsii_name="isCfnGraph")
    @builtins.classmethod
    def is_cfn_graph(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGraph.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__662fdced53feab93a21bfab8705f4ece37d75547b77b86412aa52a5e0ffea475)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGraph", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bf52fbc1feb3cff366f97eb4e18219365009dc4166140b56dc094f0ff30060e4)
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
            type_hints = cached_type_hints(_typecheckingstub__a52af3501a45e0012cf5459541c03326347319e68fa62eb909482cdc27da744c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''The connection endpoint for the graph.

        For example: ``g-12a3bcdef4.us-east-1.neptune-graph.amazonaws.com``

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrGraphArn")
    def attr_graph_arn(self) -> builtins.str:
        '''The ARN of the graph.

        For example: ``arn:aws:neptune-graph:us-east-1:111122223333:graph/g-12a3bcdef4``

        :cloudformationAttribute: GraphArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGraphArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGraphId")
    def attr_graph_id(self) -> builtins.str:
        '''The ID of the graph.

        For example: ``g-12a3bcdef4``

        :cloudformationAttribute: GraphId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGraphId"))

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
    @jsii.member(jsii_name="graphRef")
    def graph_ref(self) -> "_aws_neptunegraph_1ac4a341.GraphReference":
        '''A reference to a Graph resource.'''
        return typing.cast("_aws_neptunegraph_1ac4a341.GraphReference", jsii.get(self, "graphRef"))

    @builtins.property
    @jsii.member(jsii_name="provisionedMemory")
    def provisioned_memory(self) -> jsii.Number:
        '''The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.'''
        return typing.cast(jsii.Number, jsii.get(self, "provisionedMemory"))

    @provisioned_memory.setter
    def provisioned_memory(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__be08bf40b529ebc7ced68a048b332cc2239437062acb120b333ae55ee1a28087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionedMemory", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''A value that indicates whether the graph has deletion protection enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8d4dc803566213a64093ff7c2e80aeb4a54bbf259b51aa0f56875846630453c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="graphName")
    def graph_name(self) -> typing.Optional[builtins.str]:
        '''The graph name.

        For example: ``my-graph-1`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "graphName"))

    @graph_name.setter
    def graph_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e36e1cbffa42257001fdc31d1dd6378f3a98ce8e7f3bcd68a4772b9cb33cbbe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="importTask")
    def import_task(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.ImportTaskProperty"]]:
        '''The import task details to import data into the graph at creation time.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.ImportTaskProperty"]], jsii.get(self, "importTask"))

    @import_task.setter
    def import_task(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.ImportTaskProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__13f3ce8813d8cb6e7b44792fe5ad9ea3ff0a54eb7905b10a3d92e5b720263b30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importTask", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS key used to encrypt data in the Neptune Analytics graph.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdentifier"))

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__66eae9326926bf2762131d397fd2ef48f5c33238e6f606a97cfb83b84eadd586)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicConnectivity")
    def public_connectivity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Specifies whether or not the graph can be reachable over the internet.

        All access to graphs is IAM authenticated.
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "publicConnectivity"))

    @public_connectivity.setter
    def public_connectivity(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9704e1ee452151e117b8f45f27e9257936bf4012fb73bd4445e9f623dce33af6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicConnectivity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="replicaCount")
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''The number of replicas in other AZs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicaCount"))

    @replica_count.setter
    def replica_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f28b1503d0209026da409a25c88bd8a02abf6c3c5ad8dd42afd261c716df1e27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicaCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Adds metadata tags to the new graph.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__49f939472207baf1bb12ed3155e6d6c9c7b0a5427a254d271f09e144b617f439)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vectorSearchConfiguration")
    def vector_search_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.VectorSearchConfigurationProperty"]]:
        '''Specifies the number of dimensions for vector embeddings that will be loaded into the graph.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.VectorSearchConfigurationProperty"]], jsii.get(self, "vectorSearchConfiguration"))

    @vector_search_configuration.setter
    def vector_search_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.VectorSearchConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f52f361f4f645382b2e53faccee1b1e685b8665ddcc9f188eae9dec9c26ae9af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vectorSearchConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraph.ImportOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"neptune": "neptune"},
    )
    class ImportOptionsProperty:
        def __init__(
            self,
            *,
            neptune: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnGraph.NeptuneImportOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains options for controlling the import process.

            For example, if the failOnError key is set to false, the import skips the data that caused the error and continues if possible (whereas if set to true, the default, or if omitted, the import operation halts immediately when an error is encountered).

            :param neptune: Options for importing data from a Neptune database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_neptunegraph as neptunegraph
                
                import_options_property = neptunegraph.CfnGraph.ImportOptionsProperty(
                    neptune=neptunegraph.CfnGraph.NeptuneImportOptionsProperty(
                        s3_export_kms_key_id="s3ExportKmsKeyId",
                        s3_export_path="s3ExportPath",
                
                        # the properties below are optional
                        preserve_default_vertex_labels=False,
                        preserve_edge_ids=False
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ddadf29a4ab21556257400ce0e605c1645233ea3efd256cc0ff4526b01ab77e9)
                check_type(argname="argument neptune", value=neptune, expected_type=type_hints["neptune"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if neptune is not None:
                self._values["neptune"] = neptune

        @builtins.property
        def neptune(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.NeptuneImportOptionsProperty"]]:
            '''Options for importing data from a Neptune database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importoptions.html#cfn-neptunegraph-graph-importoptions-neptune
            '''
            result = self._values.get("neptune")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.NeptuneImportOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImportOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraph.ImportTaskProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "source": "source",
            "blank_node_handling": "blankNodeHandling",
            "fail_on_error": "failOnError",
            "format": "format",
            "import_options": "importOptions",
            "max_provisioned_memory": "maxProvisionedMemory",
            "min_provisioned_memory": "minProvisionedMemory",
            "parquet_type": "parquetType",
        },
    )
    class ImportTaskProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            source: builtins.str,
            blank_node_handling: typing.Optional[builtins.str] = None,
            fail_on_error: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            format: typing.Optional[builtins.str] = None,
            import_options: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnGraph.ImportOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            max_provisioned_memory: typing.Optional[jsii.Number] = None,
            min_provisioned_memory: typing.Optional[jsii.Number] = None,
            parquet_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The import task details to import data into the graph at creation time.

            :param role_arn: The ARN of the IAM role that will allow access to the data that is to be imported.
            :param source: A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.
            :param blank_node_handling: The method to handle blank nodes in the dataset. Currently, only convertToIri is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is NTRIPLES
            :param fail_on_error: If set to true, the task halts when an import error is encountered. If set to false, the task skips the data that caused the error and continues if possible.
            :param format: Specifies the format of S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format, OPEN_CYPHER, which identifies the openCypher load format, or NTRIPLES, which identifies the RDF n-triples format.
            :param import_options: Contains options for controlling the import process. For example, if the failOnError key is set to false, the import skips the data that caused the error and continues if possible (whereas if set to true, the default, or if omitted, the import operation halts immediately when an error is encountered).
            :param max_provisioned_memory: The maximum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 1024, or the approved upper limit for your account. If both the minimum and maximum values are specified, the final provisioned-memory will be chosen per the actual size of your imported data. If neither value is specified, 128 m-NCUs are used.
            :param min_provisioned_memory: The minimum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 16
            :param parquet_type: The parquet type of the import task. Required when Format is PARQUET.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_neptunegraph as neptunegraph
                
                import_task_property = neptunegraph.CfnGraph.ImportTaskProperty(
                    role_arn="roleArn",
                    source="source",
                
                    # the properties below are optional
                    blank_node_handling="blankNodeHandling",
                    fail_on_error=False,
                    format="format",
                    import_options=neptunegraph.CfnGraph.ImportOptionsProperty(
                        neptune=neptunegraph.CfnGraph.NeptuneImportOptionsProperty(
                            s3_export_kms_key_id="s3ExportKmsKeyId",
                            s3_export_path="s3ExportPath",
                
                            # the properties below are optional
                            preserve_default_vertex_labels=False,
                            preserve_edge_ids=False
                        )
                    ),
                    max_provisioned_memory=123,
                    min_provisioned_memory=123,
                    parquet_type="parquetType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2c49e39747481b5fbda1de3c6858f163fd27faefda3189efe47b7b6bb083e061)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument blank_node_handling", value=blank_node_handling, expected_type=type_hints["blank_node_handling"])
                check_type(argname="argument fail_on_error", value=fail_on_error, expected_type=type_hints["fail_on_error"])
                check_type(argname="argument format", value=format, expected_type=type_hints["format"])
                check_type(argname="argument import_options", value=import_options, expected_type=type_hints["import_options"])
                check_type(argname="argument max_provisioned_memory", value=max_provisioned_memory, expected_type=type_hints["max_provisioned_memory"])
                check_type(argname="argument min_provisioned_memory", value=min_provisioned_memory, expected_type=type_hints["min_provisioned_memory"])
                check_type(argname="argument parquet_type", value=parquet_type, expected_type=type_hints["parquet_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "source": source,
            }
            if blank_node_handling is not None:
                self._values["blank_node_handling"] = blank_node_handling
            if fail_on_error is not None:
                self._values["fail_on_error"] = fail_on_error
            if format is not None:
                self._values["format"] = format
            if import_options is not None:
                self._values["import_options"] = import_options
            if max_provisioned_memory is not None:
                self._values["max_provisioned_memory"] = max_provisioned_memory
            if min_provisioned_memory is not None:
                self._values["min_provisioned_memory"] = min_provisioned_memory
            if parquet_type is not None:
                self._values["parquet_type"] = parquet_type

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that will allow access to the data that is to be imported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''A URL identifying to the location of the data to be imported.

            This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def blank_node_handling(self) -> typing.Optional[builtins.str]:
            '''The method to handle blank nodes in the dataset.

            Currently, only convertToIri is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is NTRIPLES

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-blanknodehandling
            '''
            result = self._values.get("blank_node_handling")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fail_on_error(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''If set to true, the task halts when an import error is encountered.

            If set to false, the task skips the data that caused the error and continues if possible.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-failonerror
            '''
            result = self._values.get("fail_on_error")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''Specifies the format of S3 data to be imported.

            Valid values are CSV, which identifies the Gremlin CSV format, OPEN_CYPHER, which identifies the openCypher load format, or NTRIPLES, which identifies the RDF n-triples format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def import_options(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.ImportOptionsProperty"]]:
            '''Contains options for controlling the import process.

            For example, if the failOnError key is set to false, the import skips the data that caused the error and continues if possible (whereas if set to true, the default, or if omitted, the import operation halts immediately when an error is encountered).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-importoptions
            '''
            result = self._values.get("import_options")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.ImportOptionsProperty"]], result)

        @builtins.property
        def max_provisioned_memory(self) -> typing.Optional[jsii.Number]:
            '''The maximum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.

            Default: 1024, or the approved upper limit for your account. If both the minimum and maximum values are specified, the final provisioned-memory will be chosen per the actual size of your imported data. If neither value is specified, 128 m-NCUs are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-maxprovisionedmemory
            '''
            result = self._values.get("max_provisioned_memory")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_provisioned_memory(self) -> typing.Optional[jsii.Number]:
            '''The minimum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.

            Default: 16

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-minprovisionedmemory
            '''
            result = self._values.get("min_provisioned_memory")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parquet_type(self) -> typing.Optional[builtins.str]:
            '''The parquet type of the import task.

            Required when Format is PARQUET.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-importtask.html#cfn-neptunegraph-graph-importtask-parquettype
            '''
            result = self._values.get("parquet_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImportTaskProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraph.NeptuneImportOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_export_kms_key_id": "s3ExportKmsKeyId",
            "s3_export_path": "s3ExportPath",
            "preserve_default_vertex_labels": "preserveDefaultVertexLabels",
            "preserve_edge_ids": "preserveEdgeIds",
        },
    )
    class NeptuneImportOptionsProperty:
        def __init__(
            self,
            *,
            s3_export_kms_key_id: builtins.str,
            s3_export_path: builtins.str,
            preserve_default_vertex_labels: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            preserve_edge_ids: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        ) -> None:
            '''Options for importing data from a Neptune database.

            :param s3_export_kms_key_id: The KMS key to use to encrypt data in the S3 bucket where the graph data is exported.
            :param s3_export_path: The path to an S3 bucket from which to import data.
            :param preserve_default_vertex_labels: Neptune Analytics supports label-less vertices and no labels are assigned unless one is explicitly provided. Neptune assigns default labels when none is explicitly provided. When importing the data into Neptune Analytics, the default vertex labels can be omitted by setting preserveDefaultVertexLabels to false. Note that if the vertex only has default labels, and has no other properties or edges, then the vertex will effectively not get imported into Neptune Analytics when preserveDefaultVertexLabels is set to false.
            :param preserve_edge_ids: Neptune Analytics currently does not support user defined edge ids. The edge ids are not imported by default. They are imported if preserveEdgeIds is set to true, and ids are stored as properties on the relationships with the property name neptuneEdgeId.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-neptuneimportoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_neptunegraph as neptunegraph
                
                neptune_import_options_property = neptunegraph.CfnGraph.NeptuneImportOptionsProperty(
                    s3_export_kms_key_id="s3ExportKmsKeyId",
                    s3_export_path="s3ExportPath",
                
                    # the properties below are optional
                    preserve_default_vertex_labels=False,
                    preserve_edge_ids=False
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__5e9eb0cdf9204cd7b2a4c4165f1d1d71ffa416b3b65656ed9cc096939bff499c)
                check_type(argname="argument s3_export_kms_key_id", value=s3_export_kms_key_id, expected_type=type_hints["s3_export_kms_key_id"])
                check_type(argname="argument s3_export_path", value=s3_export_path, expected_type=type_hints["s3_export_path"])
                check_type(argname="argument preserve_default_vertex_labels", value=preserve_default_vertex_labels, expected_type=type_hints["preserve_default_vertex_labels"])
                check_type(argname="argument preserve_edge_ids", value=preserve_edge_ids, expected_type=type_hints["preserve_edge_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_export_kms_key_id": s3_export_kms_key_id,
                "s3_export_path": s3_export_path,
            }
            if preserve_default_vertex_labels is not None:
                self._values["preserve_default_vertex_labels"] = preserve_default_vertex_labels
            if preserve_edge_ids is not None:
                self._values["preserve_edge_ids"] = preserve_edge_ids

        @builtins.property
        def s3_export_kms_key_id(self) -> builtins.str:
            '''The KMS key to use to encrypt data in the S3 bucket where the graph data is exported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-neptuneimportoptions.html#cfn-neptunegraph-graph-neptuneimportoptions-s3exportkmskeyid
            '''
            result = self._values.get("s3_export_kms_key_id")
            assert result is not None, "Required property 's3_export_kms_key_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_export_path(self) -> builtins.str:
            '''The path to an S3 bucket from which to import data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-neptuneimportoptions.html#cfn-neptunegraph-graph-neptuneimportoptions-s3exportpath
            '''
            result = self._values.get("s3_export_path")
            assert result is not None, "Required property 's3_export_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def preserve_default_vertex_labels(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Neptune Analytics supports label-less vertices and no labels are assigned unless one is explicitly provided.

            Neptune assigns default labels when none is explicitly provided. When importing the data into Neptune Analytics, the default vertex labels can be omitted by setting preserveDefaultVertexLabels to false. Note that if the vertex only has default labels, and has no other properties or edges, then the vertex will effectively not get imported into Neptune Analytics when preserveDefaultVertexLabels is set to false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-neptuneimportoptions.html#cfn-neptunegraph-graph-neptuneimportoptions-preservedefaultvertexlabels
            '''
            result = self._values.get("preserve_default_vertex_labels")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def preserve_edge_ids(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Neptune Analytics currently does not support user defined edge ids.

            The edge ids are not imported by default. They are imported if preserveEdgeIds is set to true, and ids are stored as properties on the relationships with the property name neptuneEdgeId.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-neptuneimportoptions.html#cfn-neptunegraph-graph-neptuneimportoptions-preserveedgeids
            '''
            result = self._values.get("preserve_edge_ids")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NeptuneImportOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraph.VectorSearchConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vector_search_dimension": "vectorSearchDimension"},
    )
    class VectorSearchConfigurationProperty:
        def __init__(self, *, vector_search_dimension: jsii.Number) -> None:
            '''The vector-search configuration for the graph, which specifies the vector dimension to use in the vector index, if any.

            :param vector_search_dimension: The number of dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-vectorsearchconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_neptunegraph as neptunegraph
                
                vector_search_configuration_property = neptunegraph.CfnGraph.VectorSearchConfigurationProperty(
                    vector_search_dimension=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0a4625f08e1fb2af5a059a020fbbe4f9b64ced8f30cb593a275b3af90d3b579b)
                check_type(argname="argument vector_search_dimension", value=vector_search_dimension, expected_type=type_hints["vector_search_dimension"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "vector_search_dimension": vector_search_dimension,
            }

        @builtins.property
        def vector_search_dimension(self) -> jsii.Number:
            '''The number of dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptunegraph-graph-vectorsearchconfiguration.html#cfn-neptunegraph-graph-vectorsearchconfiguration-vectorsearchdimension
            '''
            result = self._values.get("vector_search_dimension")
            assert result is not None, "Required property 'vector_search_dimension' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VectorSearchConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraphProps",
    jsii_struct_bases=[],
    name_mapping={
        "provisioned_memory": "provisionedMemory",
        "deletion_protection": "deletionProtection",
        "graph_name": "graphName",
        "import_task": "importTask",
        "kms_key_identifier": "kmsKeyIdentifier",
        "public_connectivity": "publicConnectivity",
        "replica_count": "replicaCount",
        "tags": "tags",
        "vector_search_configuration": "vectorSearchConfiguration",
    },
)
class CfnGraphProps:
    def __init__(
        self,
        *,
        provisioned_memory: jsii.Number,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        graph_name: typing.Optional[builtins.str] = None,
        import_task: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnGraph.ImportTaskProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        public_connectivity: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_search_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnGraph.VectorSearchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraph``.

        :param provisioned_memory: The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16
        :param deletion_protection: A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
        :param graph_name: The graph name. For example: ``my-graph-1`` . The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. If you don't specify a graph name, a unique graph name is generated for you using the prefix ``graph-for`` , followed by a combination of ``Stack Name`` and a ``UUID`` .
        :param import_task: The import task details to import data into the graph at creation time.
        :param kms_key_identifier: The ARN of the KMS key used to encrypt data in the Neptune Analytics graph. If not specified, the graph is encrypted with an AWS managed key.
        :param public_connectivity: Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. When the graph is publicly available, its domain name system (DNS) endpoint resolves to the public IP address from the internet. When the graph isn't publicly available, you need to create a ``PrivateGraphEndpoint`` in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC. Default: If not specified, the default value is false. .. epigraph:: If enabling public connectivity for the first time, there will be a delay while it is enabled.
        :param replica_count: The number of replicas in other AZs. Default: If not specified, the default value is 1.
        :param tags: Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
        :param vector_search_configuration: Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as ``dimension=`` value. Max = 65,535

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_neptunegraph as neptunegraph
            
            cfn_graph_props = neptunegraph.CfnGraphProps(
                provisioned_memory=123,
            
                # the properties below are optional
                deletion_protection=False,
                graph_name="graphName",
                import_task=neptunegraph.CfnGraph.ImportTaskProperty(
                    role_arn="roleArn",
                    source="source",
            
                    # the properties below are optional
                    blank_node_handling="blankNodeHandling",
                    fail_on_error=False,
                    format="format",
                    import_options=neptunegraph.CfnGraph.ImportOptionsProperty(
                        neptune=neptunegraph.CfnGraph.NeptuneImportOptionsProperty(
                            s3_export_kms_key_id="s3ExportKmsKeyId",
                            s3_export_path="s3ExportPath",
            
                            # the properties below are optional
                            preserve_default_vertex_labels=False,
                            preserve_edge_ids=False
                        )
                    ),
                    max_provisioned_memory=123,
                    min_provisioned_memory=123,
                    parquet_type="parquetType"
                ),
                kms_key_identifier="kmsKeyIdentifier",
                public_connectivity=False,
                replica_count=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vector_search_configuration=neptunegraph.CfnGraph.VectorSearchConfigurationProperty(
                    vector_search_dimension=123
                )
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1c5873f5b0997b6619747c309d6a4e6c52de08653e961a9abf16f71c41b60b71)
            check_type(argname="argument provisioned_memory", value=provisioned_memory, expected_type=type_hints["provisioned_memory"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument graph_name", value=graph_name, expected_type=type_hints["graph_name"])
            check_type(argname="argument import_task", value=import_task, expected_type=type_hints["import_task"])
            check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            check_type(argname="argument public_connectivity", value=public_connectivity, expected_type=type_hints["public_connectivity"])
            check_type(argname="argument replica_count", value=replica_count, expected_type=type_hints["replica_count"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vector_search_configuration", value=vector_search_configuration, expected_type=type_hints["vector_search_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "provisioned_memory": provisioned_memory,
        }
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if graph_name is not None:
            self._values["graph_name"] = graph_name
        if import_task is not None:
            self._values["import_task"] = import_task
        if kms_key_identifier is not None:
            self._values["kms_key_identifier"] = kms_key_identifier
        if public_connectivity is not None:
            self._values["public_connectivity"] = public_connectivity
        if replica_count is not None:
            self._values["replica_count"] = replica_count
        if tags is not None:
            self._values["tags"] = tags
        if vector_search_configuration is not None:
            self._values["vector_search_configuration"] = vector_search_configuration

    @builtins.property
    def provisioned_memory(self) -> jsii.Number:
        '''The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.

        Min = 16

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-provisionedmemory
        '''
        result = self._values.get("provisioned_memory")
        assert result is not None, "Required property 'provisioned_memory' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''A value that indicates whether the graph has deletion protection enabled.

        The graph can't be deleted when deletion protection is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-deletionprotection
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def graph_name(self) -> typing.Optional[builtins.str]:
        '''The graph name. For example: ``my-graph-1`` .

        The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens.

        If you don't specify a graph name, a unique graph name is generated for you using the prefix ``graph-for`` , followed by a combination of ``Stack Name`` and a ``UUID`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-graphname
        '''
        result = self._values.get("graph_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def import_task(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.ImportTaskProperty"]]:
        '''The import task details to import data into the graph at creation time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-importtask
        '''
        result = self._values.get("import_task")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.ImportTaskProperty"]], result)

    @builtins.property
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS key used to encrypt data in the Neptune Analytics graph.

        If not specified, the graph is encrypted with an AWS managed key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-kmskeyidentifier
        '''
        result = self._values.get("kms_key_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_connectivity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated.

        When the graph is publicly available, its domain name system (DNS) endpoint resolves to the public IP address from the internet. When the graph isn't publicly available, you need to create a ``PrivateGraphEndpoint`` in a given VPC to ensure the DNS name resolves to a private IP address that is reachable from the VPC.

        Default: If not specified, the default value is false.
        .. epigraph::

           If enabling public connectivity for the first time, there will be a delay while it is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-publicconnectivity
        '''
        result = self._values.get("public_connectivity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''The number of replicas in other AZs.

        Default: If not specified, the default value is 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-replicacount
        '''
        result = self._values.get("replica_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Adds metadata tags to the new graph.

        These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def vector_search_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.VectorSearchConfigurationProperty"]]:
        '''Specifies the number of dimensions for vector embeddings that will be loaded into the graph.

        The value is specified as ``dimension=`` value. Max = 65,535

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graph.html#cfn-neptunegraph-graph-vectorsearchconfiguration
        '''
        result = self._values.get("vector_search_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGraph.VectorSearchConfigurationProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_neptunegraph_1ac4a341.IGraphSnapshotRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnGraphSnapshot(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraphSnapshot",
):
    '''Resource Type definition for AWS::NeptuneGraph::GraphSnapshot.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graphsnapshot.html
    :cloudformationResource: AWS::NeptuneGraph::GraphSnapshot
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_neptunegraph as neptunegraph
        
        cfn_graph_snapshot = neptunegraph.CfnGraphSnapshot(self, "MyCfnGraphSnapshot",
            graph_identifier="graphIdentifier",
            snapshot_name="snapshotName",
        
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
        graph_identifier: builtins.str,
        snapshot_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::NeptuneGraph::GraphSnapshot``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param graph_identifier: The unique identifier of the Neptune Analytics graph to create the snapshot from.
        :param snapshot_name: The snapshot name.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7b273af87939df7320e78f6dbbcda46d30a6cb3a886e613d553987ca21783091)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphSnapshotProps(
            graph_identifier=graph_identifier, snapshot_name=snapshot_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForGraphSnapshot")
    @builtins.classmethod
    def arn_for_graph_snapshot(
        cls,
        resource: "_aws_neptunegraph_1ac4a341.IGraphSnapshotRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2aff3a2c55c3bbe27cabdbfaa250e29f997c15921435adb7a60a31f2f31fca5c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForGraphSnapshot", [resource]))

    @jsii.member(jsii_name="isCfnGraphSnapshot")
    @builtins.classmethod
    def is_cfn_graph_snapshot(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGraphSnapshot.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8e2bd7fcc1af7512968450d56fdf837bfd34ea119dd1947bf8f40cb404864066)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGraphSnapshot", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__284080f94127e9c5751055c8ea194858d64a90afce11d6e15332d395ce48ce5a)
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
            type_hints = cached_type_hints(_typecheckingstub__366a7e3e25a64a38592f5cf1a057d02a05e8a02c41172807c4bc20679afd3737)
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
        '''The ARN of the graph snapshot.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the graph snapshot.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrKmsKeyIdentifier")
    def attr_kms_key_identifier(self) -> builtins.str:
        '''The ID of the KMS key used to encrypt and decrypt the snapshot.

        :cloudformationAttribute: KmsKeyIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKmsKeyIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotCreateTime")
    def attr_snapshot_create_time(self) -> builtins.str:
        '''The time when the snapshot was created.

        :cloudformationAttribute: SnapshotCreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the graph snapshot.

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
    @jsii.member(jsii_name="graphSnapshotRef")
    def graph_snapshot_ref(self) -> "_aws_neptunegraph_1ac4a341.GraphSnapshotReference":
        '''A reference to a GraphSnapshot resource.'''
        return typing.cast("_aws_neptunegraph_1ac4a341.GraphSnapshotReference", jsii.get(self, "graphSnapshotRef"))

    @builtins.property
    @jsii.member(jsii_name="graphIdentifier")
    def graph_identifier(self) -> builtins.str:
        '''The unique identifier of the Neptune Analytics graph to create the snapshot from.'''
        return typing.cast(builtins.str, jsii.get(self, "graphIdentifier"))

    @graph_identifier.setter
    def graph_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d0a2037a6ee434a7e65b019496dbfd45f74914d1a417fd92a7d81edd1da67ffc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        '''The snapshot name.'''
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1759ae4be2e5644b66f054d3c4adc3cca6727598fd99f15e86703859a38aaedd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value) # pyright: ignore[reportArgumentType]

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
            type_hints = cached_type_hints(_typecheckingstub__978655c50014b4b38ffb448afc36c36654ddcd652fe6d17e30faf72998b5c1c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnGraphSnapshotProps",
    jsii_struct_bases=[],
    name_mapping={
        "graph_identifier": "graphIdentifier",
        "snapshot_name": "snapshotName",
        "tags": "tags",
    },
)
class CfnGraphSnapshotProps:
    def __init__(
        self,
        *,
        graph_identifier: builtins.str,
        snapshot_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraphSnapshot``.

        :param graph_identifier: The unique identifier of the Neptune Analytics graph to create the snapshot from.
        :param snapshot_name: The snapshot name.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graphsnapshot.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_neptunegraph as neptunegraph
            
            cfn_graph_snapshot_props = neptunegraph.CfnGraphSnapshotProps(
                graph_identifier="graphIdentifier",
                snapshot_name="snapshotName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8cc8f9cb6d73aafcff273f6458108a762cbffccc4d5287fc5d75c40db810444c)
            check_type(argname="argument graph_identifier", value=graph_identifier, expected_type=type_hints["graph_identifier"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_identifier": graph_identifier,
            "snapshot_name": snapshot_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def graph_identifier(self) -> builtins.str:
        '''The unique identifier of the Neptune Analytics graph to create the snapshot from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graphsnapshot.html#cfn-neptunegraph-graphsnapshot-graphidentifier
        '''
        result = self._values.get("graph_identifier")
        assert result is not None, "Required property 'graph_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def snapshot_name(self) -> builtins.str:
        '''The snapshot name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graphsnapshot.html#cfn-neptunegraph-graphsnapshot-snapshotname
        '''
        result = self._values.get("snapshot_name")
        assert result is not None, "Required property 'snapshot_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-graphsnapshot.html#cfn-neptunegraph-graphsnapshot-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphSnapshotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_neptunegraph_1ac4a341.IPrivateGraphEndpointRef)
class CfnPrivateGraphEndpoint(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnPrivateGraphEndpoint",
):
    '''Create a private graph endpoint to allow private access from to the graph from within a VPC.

    You can attach security groups to the private graph endpoint.
    .. epigraph::

       VPC endpoint charges apply.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html
    :cloudformationResource: AWS::NeptuneGraph::PrivateGraphEndpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_neptunegraph as neptunegraph
        
        cfn_private_graph_endpoint = neptunegraph.CfnPrivateGraphEndpoint(self, "MyCfnPrivateGraphEndpoint",
            graph_identifier="graphIdentifier",
            vpc_id="vpcId",
        
            # the properties below are optional
            security_group_ids=["securityGroupIds"],
            subnet_ids=["subnetIds"]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        graph_identifier: builtins.str,
        vpc_id: builtins.str,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::NeptuneGraph::PrivateGraphEndpoint``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param graph_identifier: The unique identifier of the Neptune Analytics graph.
        :param vpc_id: The VPC in which the private graph endpoint needs to be created.
        :param security_group_ids: Security groups to be attached to the private graph endpoint..
        :param subnet_ids: Subnets in which private graph endpoint ENIs are created.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__01fbeae7e1567a93f602c30b996e949980cb85f4a6668a45a57e1fc68b7c6e1c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrivateGraphEndpointProps(
            graph_identifier=graph_identifier,
            vpc_id=vpc_id,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnPrivateGraphEndpoint")
    @builtins.classmethod
    def is_cfn_private_graph_endpoint(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPrivateGraphEndpoint.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cfd209f3d87c37a5a51e5ade8b2de4174a1ca2ccc4a29860df749049641c96cb)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPrivateGraphEndpoint", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cb2f8751fc71246393259a24b1f5b2dbf9fcd4b4b036f2fbc0dd9c938d27ed6b)
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
            type_hints = cached_type_hints(_typecheckingstub__8799795ac3d65adbbfd8af3b354287148d6f330fe76c184e9d21cc479404fe7c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPrivateGraphEndpointIdentifier")
    def attr_private_graph_endpoint_identifier(self) -> builtins.str:
        '''PrivateGraphEndpoint resource identifier generated by concatenating the associated GraphIdentifier and VpcId with an underscore separator.

        For example, if GraphIdentifier is ``g-12a3bcdef4`` and VpcId is ``vpc-111122223333aabbc`` , the generated PrivateGraphEndpointIdentifier will be ``g-12a3bcdef4_vpc-111122223333aabbc`` .

        :cloudformationAttribute: PrivateGraphEndpointIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateGraphEndpointIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcEndpointId")
    def attr_vpc_endpoint_id(self) -> builtins.str:
        '''VPC endpoint that provides a private connection between the Graph and specified VPC.

        For example: ``vpce-aabbaabbaabbaabba`` .

        :cloudformationAttribute: VpcEndpointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcEndpointId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="privateGraphEndpointRef")
    def private_graph_endpoint_ref(
        self,
    ) -> "_aws_neptunegraph_1ac4a341.PrivateGraphEndpointReference":
        '''A reference to a PrivateGraphEndpoint resource.'''
        return typing.cast("_aws_neptunegraph_1ac4a341.PrivateGraphEndpointReference", jsii.get(self, "privateGraphEndpointRef"))

    @builtins.property
    @jsii.member(jsii_name="graphIdentifier")
    def graph_identifier(self) -> builtins.str:
        '''The unique identifier of the Neptune Analytics graph.'''
        return typing.cast(builtins.str, jsii.get(self, "graphIdentifier"))

    @graph_identifier.setter
    def graph_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3c521eedd758be47324602ff294b6442e60a3e36064525b070eda655dce79b56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The VPC in which the private graph endpoint needs to be created.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c8cead657efa4cbd411fd2fce0f1d5a3ce1d6da29415a8974e2a94651164cccd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Security groups to be attached to the private graph endpoint..'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__682bcd6c1c60a24355d9121c725518329acfd29ac4c1e75c30476fa597fb3235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Subnets in which private graph endpoint ENIs are created.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b4fc8bb9e26efd06ea5bc87d6e7358de98fcb83d1fb96fc3f74ed77165366cd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_neptunegraph.CfnPrivateGraphEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "graph_identifier": "graphIdentifier",
        "vpc_id": "vpcId",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
    },
)
class CfnPrivateGraphEndpointProps:
    def __init__(
        self,
        *,
        graph_identifier: builtins.str,
        vpc_id: builtins.str,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrivateGraphEndpoint``.

        :param graph_identifier: The unique identifier of the Neptune Analytics graph.
        :param vpc_id: The VPC in which the private graph endpoint needs to be created.
        :param security_group_ids: Security groups to be attached to the private graph endpoint..
        :param subnet_ids: Subnets in which private graph endpoint ENIs are created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_neptunegraph as neptunegraph
            
            cfn_private_graph_endpoint_props = neptunegraph.CfnPrivateGraphEndpointProps(
                graph_identifier="graphIdentifier",
                vpc_id="vpcId",
            
                # the properties below are optional
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4034e8161715769ce918d492497f1ae3b63217d21450c72a2386f26fb2a4b186)
            check_type(argname="argument graph_identifier", value=graph_identifier, expected_type=type_hints["graph_identifier"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_identifier": graph_identifier,
            "vpc_id": vpc_id,
        }
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def graph_identifier(self) -> builtins.str:
        '''The unique identifier of the Neptune Analytics graph.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html#cfn-neptunegraph-privategraphendpoint-graphidentifier
        '''
        result = self._values.get("graph_identifier")
        assert result is not None, "Required property 'graph_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VPC in which the private graph endpoint needs to be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html#cfn-neptunegraph-privategraphendpoint-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Security groups to be attached to the private graph endpoint..

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html#cfn-neptunegraph-privategraphendpoint-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Subnets in which private graph endpoint ENIs are created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptunegraph-privategraphendpoint.html#cfn-neptunegraph-privategraphendpoint-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrivateGraphEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGraph",
    "CfnGraphProps",
    "CfnGraphSnapshot",
    "CfnGraphSnapshotProps",
    "CfnPrivateGraphEndpoint",
    "CfnPrivateGraphEndpointProps",
]

publication.publish()

def _typecheckingstub__e963857650d4e99964bc9bad7da0b29a5d2d3c66d3452d1e9b4f35e89330e04b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    provisioned_memory: jsii.Number,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    graph_name: typing.Optional[builtins.str] = None,
    import_task: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnGraph.ImportTaskProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    public_connectivity: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_search_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnGraph.VectorSearchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c6900d1428655c3b11dde92fc61e291887db2224b4c48e95c00434783fbaa82(
    resource: _aws_neptunegraph_1ac4a341.IGraphRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662fdced53feab93a21bfab8705f4ece37d75547b77b86412aa52a5e0ffea475(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf52fbc1feb3cff366f97eb4e18219365009dc4166140b56dc094f0ff30060e4(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a52af3501a45e0012cf5459541c03326347319e68fa62eb909482cdc27da744c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be08bf40b529ebc7ced68a048b332cc2239437062acb120b333ae55ee1a28087(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4dc803566213a64093ff7c2e80aeb4a54bbf259b51aa0f56875846630453c9(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e36e1cbffa42257001fdc31d1dd6378f3a98ce8e7f3bcd68a4772b9cb33cbbe7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13f3ce8813d8cb6e7b44792fe5ad9ea3ff0a54eb7905b10a3d92e5b720263b30(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnGraph.ImportTaskProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66eae9326926bf2762131d397fd2ef48f5c33238e6f606a97cfb83b84eadd586(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9704e1ee452151e117b8f45f27e9257936bf4012fb73bd4445e9f623dce33af6(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28b1503d0209026da409a25c88bd8a02abf6c3c5ad8dd42afd261c716df1e27(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49f939472207baf1bb12ed3155e6d6c9c7b0a5427a254d271f09e144b617f439(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52f361f4f645382b2e53faccee1b1e685b8665ddcc9f188eae9dec9c26ae9af(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnGraph.VectorSearchConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddadf29a4ab21556257400ce0e605c1645233ea3efd256cc0ff4526b01ab77e9(
    *,
    neptune: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnGraph.NeptuneImportOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c49e39747481b5fbda1de3c6858f163fd27faefda3189efe47b7b6bb083e061(
    *,
    role_arn: builtins.str,
    source: builtins.str,
    blank_node_handling: typing.Optional[builtins.str] = None,
    fail_on_error: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    format: typing.Optional[builtins.str] = None,
    import_options: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnGraph.ImportOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_provisioned_memory: typing.Optional[jsii.Number] = None,
    min_provisioned_memory: typing.Optional[jsii.Number] = None,
    parquet_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e9eb0cdf9204cd7b2a4c4165f1d1d71ffa416b3b65656ed9cc096939bff499c(
    *,
    s3_export_kms_key_id: builtins.str,
    s3_export_path: builtins.str,
    preserve_default_vertex_labels: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    preserve_edge_ids: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a4625f08e1fb2af5a059a020fbbe4f9b64ced8f30cb593a275b3af90d3b579b(
    *,
    vector_search_dimension: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c5873f5b0997b6619747c309d6a4e6c52de08653e961a9abf16f71c41b60b71(
    *,
    provisioned_memory: jsii.Number,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    graph_name: typing.Optional[builtins.str] = None,
    import_task: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnGraph.ImportTaskProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    public_connectivity: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_search_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnGraph.VectorSearchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b273af87939df7320e78f6dbbcda46d30a6cb3a886e613d553987ca21783091(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    graph_identifier: builtins.str,
    snapshot_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aff3a2c55c3bbe27cabdbfaa250e29f997c15921435adb7a60a31f2f31fca5c(
    resource: _aws_neptunegraph_1ac4a341.IGraphSnapshotRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e2bd7fcc1af7512968450d56fdf837bfd34ea119dd1947bf8f40cb404864066(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284080f94127e9c5751055c8ea194858d64a90afce11d6e15332d395ce48ce5a(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366a7e3e25a64a38592f5cf1a057d02a05e8a02c41172807c4bc20679afd3737(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a2037a6ee434a7e65b019496dbfd45f74914d1a417fd92a7d81edd1da67ffc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1759ae4be2e5644b66f054d3c4adc3cca6727598fd99f15e86703859a38aaedd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978655c50014b4b38ffb448afc36c36654ddcd652fe6d17e30faf72998b5c1c9(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc8f9cb6d73aafcff273f6458108a762cbffccc4d5287fc5d75c40db810444c(
    *,
    graph_identifier: builtins.str,
    snapshot_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01fbeae7e1567a93f602c30b996e949980cb85f4a6668a45a57e1fc68b7c6e1c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    graph_identifier: builtins.str,
    vpc_id: builtins.str,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfd209f3d87c37a5a51e5ade8b2de4174a1ca2ccc4a29860df749049641c96cb(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb2f8751fc71246393259a24b1f5b2dbf9fcd4b4b036f2fbc0dd9c938d27ed6b(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8799795ac3d65adbbfd8af3b354287148d6f330fe76c184e9d21cc479404fe7c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c521eedd758be47324602ff294b6442e60a3e36064525b070eda655dce79b56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8cead657efa4cbd411fd2fce0f1d5a3ce1d6da29415a8974e2a94651164cccd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682bcd6c1c60a24355d9121c725518329acfd29ac4c1e75c30476fa597fb3235(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4fc8bb9e26efd06ea5bc87d6e7358de98fcb83d1fb96fc3f74ed77165366cd5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4034e8161715769ce918d492497f1ae3b63217d21450c72a2386f26fb2a4b186(
    *,
    graph_identifier: builtins.str,
    vpc_id: builtins.str,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
