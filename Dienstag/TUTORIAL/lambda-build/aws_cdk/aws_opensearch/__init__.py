r'''
# AWS::OpenSearch Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_opensearch as opensearch
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for OpenSearch construct libraries](https://constructs.dev/search?q=opensearch)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::OpenSearch resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpenSearch.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::OpenSearch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpenSearch.html).

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
    import aws_cdk.interfaces.aws_opensearch as _aws_opensearch_cad6b9aa
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_opensearch_cad6b9aa = _LazyImport("aws_cdk.interfaces.aws_opensearch")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_opensearch_cad6b9aa.IDataSourceRef)
class CfnDataSource(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opensearch.CfnDataSource",
):
    '''Creates a data source for an Amazon OpenSearch Service domain.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearch-datasource.html
    :cloudformationResource: AWS::OpenSearch::DataSource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opensearch as opensearch
        
        cfn_data_source = opensearch.CfnDataSource(self, "MyCfnDataSource",
            data_source_type=opensearch.CfnDataSource.DataSourceTypeProperty(
                s3_glue_data_catalog=opensearch.CfnDataSource.S3GlueDataCatalogProperty(
                    role_arn="roleArn"
                )
            ),
            domain_name="domainName",
            name="name",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        data_source_type: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataSource.DataSourceTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        domain_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::OpenSearch::DataSource``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_source_type: The type of data source.
        :param domain_name: The name of the OpenSearch Service domain.
        :param name: The name of the data source.
        :param description: A description of the data source.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f69a824ff7ca05b56a81cb36e192d5e0a7b3d42b4a8a7c569623ee9323059bb8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataSourceProps(
            data_source_type=data_source_type,
            domain_name=domain_name,
            name=name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDataSource")
    @builtins.classmethod
    def arn_for_data_source(
        cls,
        resource: "_aws_opensearch_cad6b9aa.IDataSourceRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9ca0d38ed29ae58b3d8fb508da248d6cba71eb1b0aa771e45ac2a6560251849a)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDataSource", [resource]))

    @jsii.member(jsii_name="isCfnDataSource")
    @builtins.classmethod
    def is_cfn_data_source(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDataSource.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__41170ba07557497e7f7c319f475b18cb7f27efbadd2661fdf44610df35a285d2)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDataSource", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ba4c566b87b06c0e797839e77a1ac77daac490643cf894d692546a7de114d1f3)
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
            type_hints = cached_type_hints(_typecheckingstub__a7833345b42ea6b00658ebed1a52d7efd427c832199d2fdddc0fbecc52b1bc46)
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
        '''The Amazon Resource Name (ARN) of the data source.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the data source.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "_aws_opensearch_cad6b9aa.DataSourceReference":
        '''A reference to a DataSource resource.'''
        return typing.cast("_aws_opensearch_cad6b9aa.DataSourceReference", jsii.get(self, "dataSourceRef"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceType")
    def data_source_type(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataSource.DataSourceTypeProperty"]:
        '''The type of data source.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataSource.DataSourceTypeProperty"], jsii.get(self, "dataSourceType"))

    @data_source_type.setter
    def data_source_type(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataSource.DataSourceTypeProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5fd53ed0a74d133f1794fbf48d296a3ff088e24b139405347dfc0dcc6ee03a65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The name of the OpenSearch Service domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3bd20d259bb4ce3f3b95ac5d03b867e73d39a69b92deb5d743ac31ec95a7d582)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2721c6a9354b3eca652a8fe48632f79783a832fa8b7729edc5a35123ada9212b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the data source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bc7193ebef40e9e0b052dc80c80ac1d447480891f8181fbd487b4a7a1589770c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearch.CfnDataSource.DataSourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_glue_data_catalog": "s3GlueDataCatalog"},
    )
    class DataSourceTypeProperty:
        def __init__(
            self,
            *,
            s3_glue_data_catalog: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataSource.S3GlueDataCatalogProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The type of data source.

            :param s3_glue_data_catalog: Configuration for an S3 Glue Data Catalog data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearch-datasource-datasourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearch as opensearch
                
                data_source_type_property = opensearch.CfnDataSource.DataSourceTypeProperty(
                    s3_glue_data_catalog=opensearch.CfnDataSource.S3GlueDataCatalogProperty(
                        role_arn="roleArn"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__96455842b702c608b3812f3467d871ddc7d364e01cf6ddd26980a6f1108a109b)
                check_type(argname="argument s3_glue_data_catalog", value=s3_glue_data_catalog, expected_type=type_hints["s3_glue_data_catalog"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_glue_data_catalog is not None:
                self._values["s3_glue_data_catalog"] = s3_glue_data_catalog

        @builtins.property
        def s3_glue_data_catalog(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataSource.S3GlueDataCatalogProperty"]]:
            '''Configuration for an S3 Glue Data Catalog data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearch-datasource-datasourcetype.html#cfn-opensearch-datasource-datasourcetype-s3gluedatacatalog
            '''
            result = self._values.get("s3_glue_data_catalog")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataSource.S3GlueDataCatalogProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opensearch.CfnDataSource.S3GlueDataCatalogProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn"},
    )
    class S3GlueDataCatalogProperty:
        def __init__(self, *, role_arn: builtins.str) -> None:
            '''Configuration for an S3 Glue Data Catalog data source.

            :param role_arn: The ARN of the IAM role that grants OpenSearch Service permission to access the Glue Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearch-datasource-s3gluedatacatalog.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opensearch as opensearch
                
                s3_glue_data_catalog_property = opensearch.CfnDataSource.S3GlueDataCatalogProperty(
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e51057e7043e62b4e13080c7ba922bcf111bdc4afd0f8d4022a1d17da25f0fad)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants OpenSearch Service permission to access the Glue Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearch-datasource-s3gluedatacatalog.html#cfn-opensearch-datasource-s3gluedatacatalog-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3GlueDataCatalogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opensearch.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_type": "dataSourceType",
        "domain_name": "domainName",
        "name": "name",
        "description": "description",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        data_source_type: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataSource.DataSourceTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        domain_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataSource``.

        :param data_source_type: The type of data source.
        :param domain_name: The name of the OpenSearch Service domain.
        :param name: The name of the data source.
        :param description: A description of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearch-datasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opensearch as opensearch
            
            cfn_data_source_props = opensearch.CfnDataSourceProps(
                data_source_type=opensearch.CfnDataSource.DataSourceTypeProperty(
                    s3_glue_data_catalog=opensearch.CfnDataSource.S3GlueDataCatalogProperty(
                        role_arn="roleArn"
                    )
                ),
                domain_name="domainName",
                name="name",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2d27b630662ce881d41f9ed0cb97a67ad23ef3dbf9e78d67e5885d8253117f40)
            check_type(argname="argument data_source_type", value=data_source_type, expected_type=type_hints["data_source_type"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_type": data_source_type,
            "domain_name": domain_name,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def data_source_type(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataSource.DataSourceTypeProperty"]:
        '''The type of data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearch-datasource.html#cfn-opensearch-datasource-datasourcetype
        '''
        result = self._values.get("data_source_type")
        assert result is not None, "Required property 'data_source_type' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataSource.DataSourceTypeProperty"], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The name of the OpenSearch Service domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearch-datasource.html#cfn-opensearch-datasource-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearch-datasource.html#cfn-opensearch-datasource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearch-datasource.html#cfn-opensearch-datasource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataSource",
    "CfnDataSourceProps",
]

publication.publish()

def _typecheckingstub__f69a824ff7ca05b56a81cb36e192d5e0a7b3d42b4a8a7c569623ee9323059bb8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_source_type: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataSource.DataSourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    domain_name: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca0d38ed29ae58b3d8fb508da248d6cba71eb1b0aa771e45ac2a6560251849a(
    resource: _aws_opensearch_cad6b9aa.IDataSourceRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41170ba07557497e7f7c319f475b18cb7f27efbadd2661fdf44610df35a285d2(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba4c566b87b06c0e797839e77a1ac77daac490643cf894d692546a7de114d1f3(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7833345b42ea6b00658ebed1a52d7efd427c832199d2fdddc0fbecc52b1bc46(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd53ed0a74d133f1794fbf48d296a3ff088e24b139405347dfc0dcc6ee03a65(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnDataSource.DataSourceTypeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd20d259bb4ce3f3b95ac5d03b867e73d39a69b92deb5d743ac31ec95a7d582(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2721c6a9354b3eca652a8fe48632f79783a832fa8b7729edc5a35123ada9212b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc7193ebef40e9e0b052dc80c80ac1d447480891f8181fbd487b4a7a1589770c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96455842b702c608b3812f3467d871ddc7d364e01cf6ddd26980a6f1108a109b(
    *,
    s3_glue_data_catalog: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataSource.S3GlueDataCatalogProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51057e7043e62b4e13080c7ba922bcf111bdc4afd0f8d4022a1d17da25f0fad(
    *,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d27b630662ce881d41f9ed0cb97a67ad23ef3dbf9e78d67e5885d8253117f40(
    *,
    data_source_type: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataSource.DataSourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    domain_name: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
