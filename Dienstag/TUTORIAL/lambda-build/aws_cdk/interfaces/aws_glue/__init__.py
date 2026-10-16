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


from ..._jsii import *

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

    import aws_cdk.interfaces as _interfaces_8ca7e747
    import constructs as _constructs_77d1e7e8
else:

    _constructs_77d1e7e8 = _LazyImport("constructs")
    _interfaces_8ca7e747 = _LazyImport("aws_cdk.interfaces")


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.BlueprintReference",
    jsii_struct_bases=[],
    name_mapping={"blueprint_arn": "blueprintArn"},
)
class BlueprintReference:
    def __init__(self, *, blueprint_arn: builtins.str) -> None:
        '''A reference to a Blueprint resource.

        :param blueprint_arn: The Arn of the Blueprint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            blueprint_reference = interfaces_glue.BlueprintReference(
                blueprint_arn="blueprintArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__74f84cc3c6d0f263e9ddf1a55c7fdea806d5b8dc149e51187a6f8b187475d3c1)
            check_type(argname="argument blueprint_arn", value=blueprint_arn, expected_type=type_hints["blueprint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "blueprint_arn": blueprint_arn,
        }

    @builtins.property
    def blueprint_arn(self) -> builtins.str:
        '''The Arn of the Blueprint resource.'''
        result = self._values.get("blueprint_arn")
        assert result is not None, "Required property 'blueprint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlueprintReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.CatalogReference",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class CatalogReference:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''A reference to a Catalog resource.

        :param resource_arn: The ResourceArn of the Catalog resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            catalog_reference = interfaces_glue.CatalogReference(
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f73a6ea26762ecbddcfac7ae43b16414e1d43933b3ed36504fa0600d7b87e382)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the Catalog resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CatalogReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.ClassifierReference",
    jsii_struct_bases=[],
    name_mapping={"classifier_name": "classifierName"},
)
class ClassifierReference:
    def __init__(self, *, classifier_name: builtins.str) -> None:
        '''A reference to a Classifier resource.

        :param classifier_name: The Name of the Classifier resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            classifier_reference = interfaces_glue.ClassifierReference(
                classifier_name="classifierName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__153075acc355fb8c67c2595f86bb736959d7a3490470e1496c4634652a073e55)
            check_type(argname="argument classifier_name", value=classifier_name, expected_type=type_hints["classifier_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "classifier_name": classifier_name,
        }

    @builtins.property
    def classifier_name(self) -> builtins.str:
        '''The Name of the Classifier resource.'''
        result = self._values.get("classifier_name")
        assert result is not None, "Required property 'classifier_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClassifierReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.ConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"catalog_id": "catalogId", "connection_name": "connectionName"},
)
class ConnectionReference:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        connection_name: builtins.str,
    ) -> None:
        '''A reference to a Connection resource.

        :param catalog_id: The CatalogId of the Connection resource.
        :param connection_name: The Name of the Connection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            connection_reference = interfaces_glue.ConnectionReference(
                catalog_id="catalogId",
                connection_name="connectionName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d0c23f5314f51a17152319ab80f389d2f1b18975384c84d1d2931ac1a3121d9f)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "connection_name": connection_name,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The CatalogId of the Connection resource.'''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''The Name of the Connection resource.'''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.ConnectionTypeReference",
    jsii_struct_bases=[],
    name_mapping={"connection_type_arn": "connectionTypeArn"},
)
class ConnectionTypeReference:
    def __init__(self, *, connection_type_arn: builtins.str) -> None:
        '''A reference to a ConnectionType resource.

        :param connection_type_arn: The ConnectionTypeArn of the ConnectionType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            connection_type_reference = interfaces_glue.ConnectionTypeReference(
                connection_type_arn="connectionTypeArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ec4b9247a8aa2a5ea13fb42b422837b6534d7bdb249597cc280badd03a923cfd)
            check_type(argname="argument connection_type_arn", value=connection_type_arn, expected_type=type_hints["connection_type_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_type_arn": connection_type_arn,
        }

    @builtins.property
    def connection_type_arn(self) -> builtins.str:
        '''The ConnectionTypeArn of the ConnectionType resource.'''
        result = self._values.get("connection_type_arn")
        assert result is not None, "Required property 'connection_type_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.CrawlerReference",
    jsii_struct_bases=[],
    name_mapping={"crawler_name": "crawlerName"},
)
class CrawlerReference:
    def __init__(self, *, crawler_name: builtins.str) -> None:
        '''A reference to a Crawler resource.

        :param crawler_name: The Name of the Crawler resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            crawler_reference = interfaces_glue.CrawlerReference(
                crawler_name="crawlerName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ad53740eb8897f033af56fd03963af3e4f644f727baf57ca71c35961fceb97b6)
            check_type(argname="argument crawler_name", value=crawler_name, expected_type=type_hints["crawler_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "crawler_name": crawler_name,
        }

    @builtins.property
    def crawler_name(self) -> builtins.str:
        '''The Name of the Crawler resource.'''
        result = self._values.get("crawler_name")
        assert result is not None, "Required property 'crawler_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CrawlerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.CustomEntityTypeReference",
    jsii_struct_bases=[],
    name_mapping={"custom_entity_type_name": "customEntityTypeName"},
)
class CustomEntityTypeReference:
    def __init__(self, *, custom_entity_type_name: builtins.str) -> None:
        '''A reference to a CustomEntityType resource.

        :param custom_entity_type_name: The Name of the CustomEntityType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            custom_entity_type_reference = interfaces_glue.CustomEntityTypeReference(
                custom_entity_type_name="customEntityTypeName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2752daff245d03b65a99c918eff72a3eb4c7c58fc56a5bf622d9117515921d7f)
            check_type(argname="argument custom_entity_type_name", value=custom_entity_type_name, expected_type=type_hints["custom_entity_type_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_entity_type_name": custom_entity_type_name,
        }

    @builtins.property
    def custom_entity_type_name(self) -> builtins.str:
        '''The Name of the CustomEntityType resource.'''
        result = self._values.get("custom_entity_type_name")
        assert result is not None, "Required property 'custom_entity_type_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomEntityTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.DataCatalogEncryptionSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"catalog_id": "catalogId"},
)
class DataCatalogEncryptionSettingsReference:
    def __init__(self, *, catalog_id: builtins.str) -> None:
        '''A reference to a DataCatalogEncryptionSettings resource.

        :param catalog_id: The CatalogId of the DataCatalogEncryptionSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            data_catalog_encryption_settings_reference = interfaces_glue.DataCatalogEncryptionSettingsReference(
                catalog_id="catalogId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__824f5a564c0864f04cf9c7b44937b6e5dbe2d9acb8bd8b048f28e3b1f667a924)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The CatalogId of the DataCatalogEncryptionSettings resource.'''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataCatalogEncryptionSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.DataQualityRulesetReference",
    jsii_struct_bases=[],
    name_mapping={"data_quality_ruleset_name": "dataQualityRulesetName"},
)
class DataQualityRulesetReference:
    def __init__(self, *, data_quality_ruleset_name: builtins.str) -> None:
        '''A reference to a DataQualityRuleset resource.

        :param data_quality_ruleset_name: The Name of the DataQualityRuleset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            data_quality_ruleset_reference = interfaces_glue.DataQualityRulesetReference(
                data_quality_ruleset_name="dataQualityRulesetName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__637b7e752aad4e64a85b4673d0fd9fbde33283ca6452dac108809ad38887f3cd)
            check_type(argname="argument data_quality_ruleset_name", value=data_quality_ruleset_name, expected_type=type_hints["data_quality_ruleset_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_quality_ruleset_name": data_quality_ruleset_name,
        }

    @builtins.property
    def data_quality_ruleset_name(self) -> builtins.str:
        '''The Name of the DataQualityRuleset resource.'''
        result = self._values.get("data_quality_ruleset_name")
        assert result is not None, "Required property 'data_quality_ruleset_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataQualityRulesetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.DatabaseReference",
    jsii_struct_bases=[],
    name_mapping={"database_name": "databaseName"},
)
class DatabaseReference:
    def __init__(self, *, database_name: builtins.str) -> None:
        '''A reference to a Database resource.

        :param database_name: The DatabaseName of the Database resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            database_reference = interfaces_glue.DatabaseReference(
                database_name="databaseName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b006942e6851e8e5b67ab80d761f762e021506f9975b704097cc0df559962e7e)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
        }

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The DatabaseName of the Database resource.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.DevEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_name": "endpointName"},
)
class DevEndpointReference:
    def __init__(self, *, endpoint_name: builtins.str) -> None:
        '''A reference to a DevEndpoint resource.

        :param endpoint_name: The EndpointName of the DevEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            dev_endpoint_reference = interfaces_glue.DevEndpointReference(
                endpoint_name="endpointName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__050454acd533b9c974358b1bfdec6277e66592a87a752610c62dc6b896b95d0f)
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_name": endpoint_name,
        }

    @builtins.property
    def endpoint_name(self) -> builtins.str:
        '''The EndpointName of the DevEndpoint resource.'''
        result = self._values.get("endpoint_name")
        assert result is not None, "Required property 'endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IBlueprintRef")
class IBlueprintRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Blueprint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="blueprintRef")
    def blueprint_ref(self) -> "BlueprintReference":
        '''(experimental) A reference to a Blueprint resource.

        :stability: experimental
        '''
        ...


class _IBlueprintRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Blueprint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IBlueprintRef"

    @builtins.property
    @jsii.member(jsii_name="blueprintRef")
    def blueprint_ref(self) -> "BlueprintReference":
        '''(experimental) A reference to a Blueprint resource.

        :stability: experimental
        '''
        return typing.cast("BlueprintReference", jsii.get(self, "blueprintRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBlueprintRef).__jsii_proxy_class__ = lambda : _IBlueprintRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ICatalogRef")
class ICatalogRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Catalog.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="catalogRef")
    def catalog_ref(self) -> "CatalogReference":
        '''(experimental) A reference to a Catalog resource.

        :stability: experimental
        '''
        ...


class _ICatalogRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Catalog.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ICatalogRef"

    @builtins.property
    @jsii.member(jsii_name="catalogRef")
    def catalog_ref(self) -> "CatalogReference":
        '''(experimental) A reference to a Catalog resource.

        :stability: experimental
        '''
        return typing.cast("CatalogReference", jsii.get(self, "catalogRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICatalogRef).__jsii_proxy_class__ = lambda : _ICatalogRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IClassifierRef")
class IClassifierRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Classifier.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="classifierRef")
    def classifier_ref(self) -> "ClassifierReference":
        '''(experimental) A reference to a Classifier resource.

        :stability: experimental
        '''
        ...


class _IClassifierRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Classifier.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IClassifierRef"

    @builtins.property
    @jsii.member(jsii_name="classifierRef")
    def classifier_ref(self) -> "ClassifierReference":
        '''(experimental) A reference to a Classifier resource.

        :stability: experimental
        '''
        return typing.cast("ClassifierReference", jsii.get(self, "classifierRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClassifierRef).__jsii_proxy_class__ = lambda : _IClassifierRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IConnectionRef")
class IConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        ...


class _IConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionReference", jsii.get(self, "connectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionRef).__jsii_proxy_class__ = lambda : _IConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IConnectionTypeRef")
class IConnectionTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectionType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionTypeRef")
    def connection_type_ref(self) -> "ConnectionTypeReference":
        '''(experimental) A reference to a ConnectionType resource.

        :stability: experimental
        '''
        ...


class _IConnectionTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectionType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IConnectionTypeRef"

    @builtins.property
    @jsii.member(jsii_name="connectionTypeRef")
    def connection_type_ref(self) -> "ConnectionTypeReference":
        '''(experimental) A reference to a ConnectionType resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionTypeReference", jsii.get(self, "connectionTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionTypeRef).__jsii_proxy_class__ = lambda : _IConnectionTypeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ICrawlerRef")
class ICrawlerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Crawler.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="crawlerRef")
    def crawler_ref(self) -> "CrawlerReference":
        '''(experimental) A reference to a Crawler resource.

        :stability: experimental
        '''
        ...


class _ICrawlerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Crawler.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ICrawlerRef"

    @builtins.property
    @jsii.member(jsii_name="crawlerRef")
    def crawler_ref(self) -> "CrawlerReference":
        '''(experimental) A reference to a Crawler resource.

        :stability: experimental
        '''
        return typing.cast("CrawlerReference", jsii.get(self, "crawlerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICrawlerRef).__jsii_proxy_class__ = lambda : _ICrawlerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ICustomEntityTypeRef")
class ICustomEntityTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomEntityType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customEntityTypeRef")
    def custom_entity_type_ref(self) -> "CustomEntityTypeReference":
        '''(experimental) A reference to a CustomEntityType resource.

        :stability: experimental
        '''
        ...


class _ICustomEntityTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomEntityType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ICustomEntityTypeRef"

    @builtins.property
    @jsii.member(jsii_name="customEntityTypeRef")
    def custom_entity_type_ref(self) -> "CustomEntityTypeReference":
        '''(experimental) A reference to a CustomEntityType resource.

        :stability: experimental
        '''
        return typing.cast("CustomEntityTypeReference", jsii.get(self, "customEntityTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomEntityTypeRef).__jsii_proxy_class__ = lambda : _ICustomEntityTypeRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IDataCatalogEncryptionSettingsRef"
)
class IDataCatalogEncryptionSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataCatalogEncryptionSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataCatalogEncryptionSettingsRef")
    def data_catalog_encryption_settings_ref(
        self,
    ) -> "DataCatalogEncryptionSettingsReference":
        '''(experimental) A reference to a DataCatalogEncryptionSettings resource.

        :stability: experimental
        '''
        ...


class _IDataCatalogEncryptionSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataCatalogEncryptionSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IDataCatalogEncryptionSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="dataCatalogEncryptionSettingsRef")
    def data_catalog_encryption_settings_ref(
        self,
    ) -> "DataCatalogEncryptionSettingsReference":
        '''(experimental) A reference to a DataCatalogEncryptionSettings resource.

        :stability: experimental
        '''
        return typing.cast("DataCatalogEncryptionSettingsReference", jsii.get(self, "dataCatalogEncryptionSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataCatalogEncryptionSettingsRef).__jsii_proxy_class__ = lambda : _IDataCatalogEncryptionSettingsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IDataQualityRulesetRef")
class IDataQualityRulesetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataQualityRuleset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataQualityRulesetRef")
    def data_quality_ruleset_ref(self) -> "DataQualityRulesetReference":
        '''(experimental) A reference to a DataQualityRuleset resource.

        :stability: experimental
        '''
        ...


class _IDataQualityRulesetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataQualityRuleset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IDataQualityRulesetRef"

    @builtins.property
    @jsii.member(jsii_name="dataQualityRulesetRef")
    def data_quality_ruleset_ref(self) -> "DataQualityRulesetReference":
        '''(experimental) A reference to a DataQualityRuleset resource.

        :stability: experimental
        '''
        return typing.cast("DataQualityRulesetReference", jsii.get(self, "dataQualityRulesetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataQualityRulesetRef).__jsii_proxy_class__ = lambda : _IDataQualityRulesetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IDatabaseRef")
class IDatabaseRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Database.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="databaseRef")
    def database_ref(self) -> "DatabaseReference":
        '''(experimental) A reference to a Database resource.

        :stability: experimental
        '''
        ...


class _IDatabaseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Database.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IDatabaseRef"

    @builtins.property
    @jsii.member(jsii_name="databaseRef")
    def database_ref(self) -> "DatabaseReference":
        '''(experimental) A reference to a Database resource.

        :stability: experimental
        '''
        return typing.cast("DatabaseReference", jsii.get(self, "databaseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseRef).__jsii_proxy_class__ = lambda : _IDatabaseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IDevEndpointRef")
class IDevEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DevEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="devEndpointRef")
    def dev_endpoint_ref(self) -> "DevEndpointReference":
        '''(experimental) A reference to a DevEndpoint resource.

        :stability: experimental
        '''
        ...


class _IDevEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DevEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IDevEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="devEndpointRef")
    def dev_endpoint_ref(self) -> "DevEndpointReference":
        '''(experimental) A reference to a DevEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("DevEndpointReference", jsii.get(self, "devEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDevEndpointRef).__jsii_proxy_class__ = lambda : _IDevEndpointRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IIdentityCenterConfigurationRef"
)
class IIdentityCenterConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityCenterConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identityCenterConfigurationRef")
    def identity_center_configuration_ref(
        self,
    ) -> "IdentityCenterConfigurationReference":
        '''(experimental) A reference to a IdentityCenterConfiguration resource.

        :stability: experimental
        '''
        ...


class _IIdentityCenterConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityCenterConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IIdentityCenterConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="identityCenterConfigurationRef")
    def identity_center_configuration_ref(
        self,
    ) -> "IdentityCenterConfigurationReference":
        '''(experimental) A reference to a IdentityCenterConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("IdentityCenterConfigurationReference", jsii.get(self, "identityCenterConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityCenterConfigurationRef).__jsii_proxy_class__ = lambda : _IIdentityCenterConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IIntegrationRef")
class IIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        ...


class _IIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationReference", jsii.get(self, "integrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationRef).__jsii_proxy_class__ = lambda : _IIntegrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IIntegrationResourcePropertyRef"
)
class IIntegrationResourcePropertyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IntegrationResourceProperty.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationResourcePropertyRef")
    def integration_resource_property_ref(
        self,
    ) -> "IntegrationResourcePropertyReference":
        '''(experimental) A reference to a IntegrationResourceProperty resource.

        :stability: experimental
        '''
        ...


class _IIntegrationResourcePropertyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IntegrationResourceProperty.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IIntegrationResourcePropertyRef"

    @builtins.property
    @jsii.member(jsii_name="integrationResourcePropertyRef")
    def integration_resource_property_ref(
        self,
    ) -> "IntegrationResourcePropertyReference":
        '''(experimental) A reference to a IntegrationResourceProperty resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationResourcePropertyReference", jsii.get(self, "integrationResourcePropertyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationResourcePropertyRef).__jsii_proxy_class__ = lambda : _IIntegrationResourcePropertyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IJobRef")
class IJobRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Job.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="jobRef")
    def job_ref(self) -> "JobReference":
        '''(experimental) A reference to a Job resource.

        :stability: experimental
        '''
        ...


class _IJobRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Job.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IJobRef"

    @builtins.property
    @jsii.member(jsii_name="jobRef")
    def job_ref(self) -> "JobReference":
        '''(experimental) A reference to a Job resource.

        :stability: experimental
        '''
        return typing.cast("JobReference", jsii.get(self, "jobRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJobRef).__jsii_proxy_class__ = lambda : _IJobRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IMLTransformRef")
class IMLTransformRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MLTransform.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mlTransformRef")
    def ml_transform_ref(self) -> "MLTransformReference":
        '''(experimental) A reference to a MLTransform resource.

        :stability: experimental
        '''
        ...


class _IMLTransformRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MLTransform.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IMLTransformRef"

    @builtins.property
    @jsii.member(jsii_name="mlTransformRef")
    def ml_transform_ref(self) -> "MLTransformReference":
        '''(experimental) A reference to a MLTransform resource.

        :stability: experimental
        '''
        return typing.cast("MLTransformReference", jsii.get(self, "mlTransformRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMLTransformRef).__jsii_proxy_class__ = lambda : _IMLTransformRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IPartitionRef")
class IPartitionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Partition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="partitionRef")
    def partition_ref(self) -> "PartitionReference":
        '''(experimental) A reference to a Partition resource.

        :stability: experimental
        '''
        ...


class _IPartitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Partition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IPartitionRef"

    @builtins.property
    @jsii.member(jsii_name="partitionRef")
    def partition_ref(self) -> "PartitionReference":
        '''(experimental) A reference to a Partition resource.

        :stability: experimental
        '''
        return typing.cast("PartitionReference", jsii.get(self, "partitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPartitionRef).__jsii_proxy_class__ = lambda : _IPartitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IRegistryRef")
class IRegistryRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Registry.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "RegistryReference":
        '''(experimental) A reference to a Registry resource.

        :stability: experimental
        '''
        ...


class _IRegistryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Registry.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IRegistryRef"

    @builtins.property
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "RegistryReference":
        '''(experimental) A reference to a Registry resource.

        :stability: experimental
        '''
        return typing.cast("RegistryReference", jsii.get(self, "registryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegistryRef).__jsii_proxy_class__ = lambda : _IRegistryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISchemaRef")
class ISchemaRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        ...


class _ISchemaRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISchemaRef"

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        return typing.cast("SchemaReference", jsii.get(self, "schemaRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaRef).__jsii_proxy_class__ = lambda : _ISchemaRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISchemaVersionMetadataRef")
class ISchemaVersionMetadataRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaVersionMetadata.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaVersionMetadataRef")
    def schema_version_metadata_ref(self) -> "SchemaVersionMetadataReference":
        '''(experimental) A reference to a SchemaVersionMetadata resource.

        :stability: experimental
        '''
        ...


class _ISchemaVersionMetadataRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaVersionMetadata.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISchemaVersionMetadataRef"

    @builtins.property
    @jsii.member(jsii_name="schemaVersionMetadataRef")
    def schema_version_metadata_ref(self) -> "SchemaVersionMetadataReference":
        '''(experimental) A reference to a SchemaVersionMetadata resource.

        :stability: experimental
        '''
        return typing.cast("SchemaVersionMetadataReference", jsii.get(self, "schemaVersionMetadataRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaVersionMetadataRef).__jsii_proxy_class__ = lambda : _ISchemaVersionMetadataRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISchemaVersionRef")
class ISchemaVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaVersionRef")
    def schema_version_ref(self) -> "SchemaVersionReference":
        '''(experimental) A reference to a SchemaVersion resource.

        :stability: experimental
        '''
        ...


class _ISchemaVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISchemaVersionRef"

    @builtins.property
    @jsii.member(jsii_name="schemaVersionRef")
    def schema_version_ref(self) -> "SchemaVersionReference":
        '''(experimental) A reference to a SchemaVersion resource.

        :stability: experimental
        '''
        return typing.cast("SchemaVersionReference", jsii.get(self, "schemaVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaVersionRef).__jsii_proxy_class__ = lambda : _ISchemaVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISecurityConfigurationRef")
class ISecurityConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "SecurityConfigurationReference":
        '''(experimental) A reference to a SecurityConfiguration resource.

        :stability: experimental
        '''
        ...


class _ISecurityConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISecurityConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "SecurityConfigurationReference":
        '''(experimental) A reference to a SecurityConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SecurityConfigurationReference", jsii.get(self, "securityConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityConfigurationRef).__jsii_proxy_class__ = lambda : _ISecurityConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISessionRef")
class ISessionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Session.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sessionRef")
    def session_ref(self) -> "SessionReference":
        '''(experimental) A reference to a Session resource.

        :stability: experimental
        '''
        ...


class _ISessionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Session.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISessionRef"

    @builtins.property
    @jsii.member(jsii_name="sessionRef")
    def session_ref(self) -> "SessionReference":
        '''(experimental) A reference to a Session resource.

        :stability: experimental
        '''
        return typing.cast("SessionReference", jsii.get(self, "sessionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISessionRef).__jsii_proxy_class__ = lambda : _ISessionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ITableOptimizerRef")
class ITableOptimizerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TableOptimizer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tableOptimizerRef")
    def table_optimizer_ref(self) -> "TableOptimizerReference":
        '''(experimental) A reference to a TableOptimizer resource.

        :stability: experimental
        '''
        ...


class _ITableOptimizerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TableOptimizer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ITableOptimizerRef"

    @builtins.property
    @jsii.member(jsii_name="tableOptimizerRef")
    def table_optimizer_ref(self) -> "TableOptimizerReference":
        '''(experimental) A reference to a TableOptimizer resource.

        :stability: experimental
        '''
        return typing.cast("TableOptimizerReference", jsii.get(self, "tableOptimizerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITableOptimizerRef).__jsii_proxy_class__ = lambda : _ITableOptimizerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ITableRef")
class ITableRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Table.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tableRef")
    def table_ref(self) -> "TableReference":
        '''(experimental) A reference to a Table resource.

        :stability: experimental
        '''
        ...


class _ITableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Table.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ITableRef"

    @builtins.property
    @jsii.member(jsii_name="tableRef")
    def table_ref(self) -> "TableReference":
        '''(experimental) A reference to a Table resource.

        :stability: experimental
        '''
        return typing.cast("TableReference", jsii.get(self, "tableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITableRef).__jsii_proxy_class__ = lambda : _ITableRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ITriggerRef")
class ITriggerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Trigger.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="triggerRef")
    def trigger_ref(self) -> "TriggerReference":
        '''(experimental) A reference to a Trigger resource.

        :stability: experimental
        '''
        ...


class _ITriggerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Trigger.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ITriggerRef"

    @builtins.property
    @jsii.member(jsii_name="triggerRef")
    def trigger_ref(self) -> "TriggerReference":
        '''(experimental) A reference to a Trigger resource.

        :stability: experimental
        '''
        return typing.cast("TriggerReference", jsii.get(self, "triggerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITriggerRef).__jsii_proxy_class__ = lambda : _ITriggerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IUsageProfileRef")
class IUsageProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UsageProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="usageProfileRef")
    def usage_profile_ref(self) -> "UsageProfileReference":
        '''(experimental) A reference to a UsageProfile resource.

        :stability: experimental
        '''
        ...


class _IUsageProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UsageProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IUsageProfileRef"

    @builtins.property
    @jsii.member(jsii_name="usageProfileRef")
    def usage_profile_ref(self) -> "UsageProfileReference":
        '''(experimental) A reference to a UsageProfile resource.

        :stability: experimental
        '''
        return typing.cast("UsageProfileReference", jsii.get(self, "usageProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUsageProfileRef).__jsii_proxy_class__ = lambda : _IUsageProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IUserDefinedFunctionRef")
class IUserDefinedFunctionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserDefinedFunction.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userDefinedFunctionRef")
    def user_defined_function_ref(self) -> "UserDefinedFunctionReference":
        '''(experimental) A reference to a UserDefinedFunction resource.

        :stability: experimental
        '''
        ...


class _IUserDefinedFunctionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserDefinedFunction.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IUserDefinedFunctionRef"

    @builtins.property
    @jsii.member(jsii_name="userDefinedFunctionRef")
    def user_defined_function_ref(self) -> "UserDefinedFunctionReference":
        '''(experimental) A reference to a UserDefinedFunction resource.

        :stability: experimental
        '''
        return typing.cast("UserDefinedFunctionReference", jsii.get(self, "userDefinedFunctionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserDefinedFunctionRef).__jsii_proxy_class__ = lambda : _IUserDefinedFunctionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IWorkflowRef")
class IWorkflowRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        ...


class _IWorkflowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IWorkflowRef"

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        return typing.cast("WorkflowReference", jsii.get(self, "workflowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkflowRef).__jsii_proxy_class__ = lambda : _IWorkflowRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IdentityCenterConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class IdentityCenterConfigurationReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a IdentityCenterConfiguration resource.

        :param account_id: The AccountId of the IdentityCenterConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            identity_center_configuration_reference = interfaces_glue.IdentityCenterConfigurationReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dce890d13c4e501fd50bfd966cbe5558eac1e8b2415bc6f873c45a675fef0455)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the IdentityCenterConfiguration resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityCenterConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IntegrationReference",
    jsii_struct_bases=[],
    name_mapping={
        "integration_arn": "integrationArn",
        "integration_name": "integrationName",
    },
)
class IntegrationReference:
    def __init__(
        self,
        *,
        integration_arn: builtins.str,
        integration_name: builtins.str,
    ) -> None:
        '''A reference to a Integration resource.

        :param integration_arn: The IntegrationArn of the Integration resource.
        :param integration_name: The IntegrationName of the Integration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            integration_reference = interfaces_glue.IntegrationReference(
                integration_arn="integrationArn",
                integration_name="integrationName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__487ef973bf980b9533ab5e35911c785df93801badcd04a6ad9191c32ce95e300)
            check_type(argname="argument integration_arn", value=integration_arn, expected_type=type_hints["integration_arn"])
            check_type(argname="argument integration_name", value=integration_name, expected_type=type_hints["integration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "integration_arn": integration_arn,
            "integration_name": integration_name,
        }

    @builtins.property
    def integration_arn(self) -> builtins.str:
        '''The IntegrationArn of the Integration resource.'''
        result = self._values.get("integration_arn")
        assert result is not None, "Required property 'integration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_name(self) -> builtins.str:
        '''The IntegrationName of the Integration resource.'''
        result = self._values.get("integration_name")
        assert result is not None, "Required property 'integration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IntegrationResourcePropertyReference",
    jsii_struct_bases=[],
    name_mapping={
        "resource_arn": "resourceArn",
        "resource_property_arn": "resourcePropertyArn",
    },
)
class IntegrationResourcePropertyReference:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        resource_property_arn: builtins.str,
    ) -> None:
        '''A reference to a IntegrationResourceProperty resource.

        :param resource_arn: The ResourceArn of the IntegrationResourceProperty resource.
        :param resource_property_arn: The ResourcePropertyArn of the IntegrationResourceProperty resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            integration_resource_property_reference = interfaces_glue.IntegrationResourcePropertyReference(
                resource_arn="resourceArn",
                resource_property_arn="resourcePropertyArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d78e927b289090d3ea11c2e52f58b5cdc45b50ebf0cb9ac19af7a86759d45975)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument resource_property_arn", value=resource_property_arn, expected_type=type_hints["resource_property_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "resource_property_arn": resource_property_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the IntegrationResourceProperty resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_property_arn(self) -> builtins.str:
        '''The ResourcePropertyArn of the IntegrationResourceProperty resource.'''
        result = self._values.get("resource_property_arn")
        assert result is not None, "Required property 'resource_property_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationResourcePropertyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.JobReference",
    jsii_struct_bases=[],
    name_mapping={"job_name": "jobName"},
)
class JobReference:
    def __init__(self, *, job_name: builtins.str) -> None:
        '''A reference to a Job resource.

        :param job_name: The Name of the Job resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            job_reference = interfaces_glue.JobReference(
                job_name="jobName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f8c47c403cca6462755fa024cf63a9b8531d52ca6834543a739c13e8ee51c9e9)
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_name": job_name,
        }

    @builtins.property
    def job_name(self) -> builtins.str:
        '''The Name of the Job resource.'''
        result = self._values.get("job_name")
        assert result is not None, "Required property 'job_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.MLTransformReference",
    jsii_struct_bases=[],
    name_mapping={"transform_id": "transformId"},
)
class MLTransformReference:
    def __init__(self, *, transform_id: builtins.str) -> None:
        '''A reference to a MLTransform resource.

        :param transform_id: The TransformId of the MLTransform resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            m_l_transform_reference = interfaces_glue.MLTransformReference(
                transform_id="transformId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b3f1a2f7b4f39bcc3b7be922b88fffd5ccf9f63df878ae375f85fa00250d7cff)
            check_type(argname="argument transform_id", value=transform_id, expected_type=type_hints["transform_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transform_id": transform_id,
        }

    @builtins.property
    def transform_id(self) -> builtins.str:
        '''The TransformId of the MLTransform resource.'''
        result = self._values.get("transform_id")
        assert result is not None, "Required property 'transform_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MLTransformReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.PartitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "catalog_id": "catalogId",
        "database_name": "databaseName",
        "identifier_partition_input_values": "identifierPartitionInputValues",
        "table_name": "tableName",
    },
)
class PartitionReference:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
        identifier_partition_input_values: builtins.str,
        table_name: builtins.str,
    ) -> None:
        '''A reference to a Partition resource.

        :param catalog_id: The CatalogId of the Partition resource.
        :param database_name: The DatabaseName of the Partition resource.
        :param identifier_partition_input_values: The IdentifierPartitionInputValues of the Partition resource.
        :param table_name: The TableName of the Partition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            partition_reference = interfaces_glue.PartitionReference(
                catalog_id="catalogId",
                database_name="databaseName",
                identifier_partition_input_values="identifierPartitionInputValues",
                table_name="tableName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5a9698059eb8899c746fb237350793d2faff1bdfa61b71f202add91131734519)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument identifier_partition_input_values", value=identifier_partition_input_values, expected_type=type_hints["identifier_partition_input_values"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "database_name": database_name,
            "identifier_partition_input_values": identifier_partition_input_values,
            "table_name": table_name,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The CatalogId of the Partition resource.'''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The DatabaseName of the Partition resource.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier_partition_input_values(self) -> builtins.str:
        '''The IdentifierPartitionInputValues of the Partition resource.'''
        result = self._values.get("identifier_partition_input_values")
        assert result is not None, "Required property 'identifier_partition_input_values' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''The TableName of the Partition resource.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PartitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.RegistryReference",
    jsii_struct_bases=[],
    name_mapping={"registry_arn": "registryArn"},
)
class RegistryReference:
    def __init__(self, *, registry_arn: builtins.str) -> None:
        '''A reference to a Registry resource.

        :param registry_arn: The Arn of the Registry resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            registry_reference = interfaces_glue.RegistryReference(
                registry_arn="registryArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2f46875075b9b44d3958fe5be64778d351238ba406d2bfaf624a127c572ecfdd)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_arn": registry_arn,
        }

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''The Arn of the Registry resource.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SchemaReference",
    jsii_struct_bases=[],
    name_mapping={"schema_arn": "schemaArn"},
)
class SchemaReference:
    def __init__(self, *, schema_arn: builtins.str) -> None:
        '''A reference to a Schema resource.

        :param schema_arn: The Arn of the Schema resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            schema_reference = interfaces_glue.SchemaReference(
                schema_arn="schemaArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b578c469d6ed870abb6802e9d10670c2f571c62a79988a4ded4d3dccbcf0754e)
            check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_arn": schema_arn,
        }

    @builtins.property
    def schema_arn(self) -> builtins.str:
        '''The Arn of the Schema resource.'''
        result = self._values.get("schema_arn")
        assert result is not None, "Required property 'schema_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SchemaVersionMetadataReference",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "schema_version_id": "schemaVersionId",
        "value": "value",
    },
)
class SchemaVersionMetadataReference:
    def __init__(
        self,
        *,
        key: builtins.str,
        schema_version_id: builtins.str,
        value: builtins.str,
    ) -> None:
        '''A reference to a SchemaVersionMetadata resource.

        :param key: The Key of the SchemaVersionMetadata resource.
        :param schema_version_id: The SchemaVersionId of the SchemaVersionMetadata resource.
        :param value: The Value of the SchemaVersionMetadata resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            schema_version_metadata_reference = interfaces_glue.SchemaVersionMetadataReference(
                key="key",
                schema_version_id="schemaVersionId",
                value="value"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d4b127790a6c1e064bc511d8914a963c65c84be0739a54f9274fdb48b4f2105d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument schema_version_id", value=schema_version_id, expected_type=type_hints["schema_version_id"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "schema_version_id": schema_version_id,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''The Key of the SchemaVersionMetadata resource.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_version_id(self) -> builtins.str:
        '''The SchemaVersionId of the SchemaVersionMetadata resource.'''
        result = self._values.get("schema_version_id")
        assert result is not None, "Required property 'schema_version_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The Value of the SchemaVersionMetadata resource.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaVersionMetadataReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SchemaVersionReference",
    jsii_struct_bases=[],
    name_mapping={"version_id": "versionId"},
)
class SchemaVersionReference:
    def __init__(self, *, version_id: builtins.str) -> None:
        '''A reference to a SchemaVersion resource.

        :param version_id: The VersionId of the SchemaVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            schema_version_reference = interfaces_glue.SchemaVersionReference(
                version_id="versionId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8183bbaf7cbe72ac30393afbba3db6508105f9305b6e69bf1acef9abffd833d2)
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version_id": version_id,
        }

    @builtins.property
    def version_id(self) -> builtins.str:
        '''The VersionId of the SchemaVersion resource.'''
        result = self._values.get("version_id")
        assert result is not None, "Required property 'version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SecurityConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"security_configuration_name": "securityConfigurationName"},
)
class SecurityConfigurationReference:
    def __init__(self, *, security_configuration_name: builtins.str) -> None:
        '''A reference to a SecurityConfiguration resource.

        :param security_configuration_name: The Name of the SecurityConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            security_configuration_reference = interfaces_glue.SecurityConfigurationReference(
                security_configuration_name="securityConfigurationName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5f762055d8744dcdcadf6d3ee48e027edbbedb409f2aee69d69051529ab7d003)
            check_type(argname="argument security_configuration_name", value=security_configuration_name, expected_type=type_hints["security_configuration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_configuration_name": security_configuration_name,
        }

    @builtins.property
    def security_configuration_name(self) -> builtins.str:
        '''The Name of the SecurityConfiguration resource.'''
        result = self._values.get("security_configuration_name")
        assert result is not None, "Required property 'security_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SessionReference",
    jsii_struct_bases=[],
    name_mapping={"session_arn": "sessionArn"},
)
class SessionReference:
    def __init__(self, *, session_arn: builtins.str) -> None:
        '''A reference to a Session resource.

        :param session_arn: The Arn of the Session resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            session_reference = interfaces_glue.SessionReference(
                session_arn="sessionArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5d556c62e8ccef01cb2ebde5bdf8e8e61850e36ae87a512eb64e73be540ab0fa)
            check_type(argname="argument session_arn", value=session_arn, expected_type=type_hints["session_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "session_arn": session_arn,
        }

    @builtins.property
    def session_arn(self) -> builtins.str:
        '''The Arn of the Session resource.'''
        result = self._values.get("session_arn")
        assert result is not None, "Required property 'session_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SessionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.TableOptimizerReference",
    jsii_struct_bases=[],
    name_mapping={
        "catalog_id": "catalogId",
        "database_name": "databaseName",
        "table_name": "tableName",
        "type": "type",
    },
)
class TableOptimizerReference:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
        table_name: builtins.str,
        type: builtins.str,
    ) -> None:
        '''A reference to a TableOptimizer resource.

        :param catalog_id: The CatalogId of the TableOptimizer resource.
        :param database_name: The DatabaseName of the TableOptimizer resource.
        :param table_name: The TableName of the TableOptimizer resource.
        :param type: The Type of the TableOptimizer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            table_optimizer_reference = interfaces_glue.TableOptimizerReference(
                catalog_id="catalogId",
                database_name="databaseName",
                table_name="tableName",
                type="type"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__36d18932d532cd2df3f2355353c78a3d21a028fa0d2181f51b94ae7c9101726b)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "database_name": database_name,
            "table_name": table_name,
            "type": type,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The CatalogId of the TableOptimizer resource.'''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The DatabaseName of the TableOptimizer resource.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''The TableName of the TableOptimizer resource.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The Type of the TableOptimizer resource.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableOptimizerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.TableReference",
    jsii_struct_bases=[],
    name_mapping={"table_id": "tableId"},
)
class TableReference:
    def __init__(self, *, table_id: builtins.str) -> None:
        '''A reference to a Table resource.

        :param table_id: The Id of the Table resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            table_reference = interfaces_glue.TableReference(
                table_id="tableId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d91e1bc0dff8ee618900793d998bcf5ed91fd48153fcbcc02d63186fa2219535)
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_id": table_id,
        }

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The Id of the Table resource.'''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.TriggerReference",
    jsii_struct_bases=[],
    name_mapping={"trigger_name": "triggerName"},
)
class TriggerReference:
    def __init__(self, *, trigger_name: builtins.str) -> None:
        '''A reference to a Trigger resource.

        :param trigger_name: The Name of the Trigger resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            trigger_reference = interfaces_glue.TriggerReference(
                trigger_name="triggerName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__85c96b93a2c298c01219667b5012a8e417cd40c14e36afd3fd093081bbfc5a3e)
            check_type(argname="argument trigger_name", value=trigger_name, expected_type=type_hints["trigger_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trigger_name": trigger_name,
        }

    @builtins.property
    def trigger_name(self) -> builtins.str:
        '''The Name of the Trigger resource.'''
        result = self._values.get("trigger_name")
        assert result is not None, "Required property 'trigger_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.UsageProfileReference",
    jsii_struct_bases=[],
    name_mapping={"usage_profile_name": "usageProfileName"},
)
class UsageProfileReference:
    def __init__(self, *, usage_profile_name: builtins.str) -> None:
        '''A reference to a UsageProfile resource.

        :param usage_profile_name: The Name of the UsageProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            usage_profile_reference = interfaces_glue.UsageProfileReference(
                usage_profile_name="usageProfileName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__31cd7baf9c81bae2e0d29221ca6cf6bf1b06b730a8c9d8fedf8630e653710373)
            check_type(argname="argument usage_profile_name", value=usage_profile_name, expected_type=type_hints["usage_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "usage_profile_name": usage_profile_name,
        }

    @builtins.property
    def usage_profile_name(self) -> builtins.str:
        '''The Name of the UsageProfile resource.'''
        result = self._values.get("usage_profile_name")
        assert result is not None, "Required property 'usage_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsageProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.UserDefinedFunctionReference",
    jsii_struct_bases=[],
    name_mapping={"user_defined_function_arn": "userDefinedFunctionArn"},
)
class UserDefinedFunctionReference:
    def __init__(self, *, user_defined_function_arn: builtins.str) -> None:
        '''A reference to a UserDefinedFunction resource.

        :param user_defined_function_arn: The Arn of the UserDefinedFunction resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            user_defined_function_reference = interfaces_glue.UserDefinedFunctionReference(
                user_defined_function_arn="userDefinedFunctionArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5e1ff3d4751c7ba1689180d09777a0d7407fc90ef06c219bedeb2047180cc973)
            check_type(argname="argument user_defined_function_arn", value=user_defined_function_arn, expected_type=type_hints["user_defined_function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_defined_function_arn": user_defined_function_arn,
        }

    @builtins.property
    def user_defined_function_arn(self) -> builtins.str:
        '''The Arn of the UserDefinedFunction resource.'''
        result = self._values.get("user_defined_function_arn")
        assert result is not None, "Required property 'user_defined_function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserDefinedFunctionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.WorkflowReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_name": "workflowName"},
)
class WorkflowReference:
    def __init__(self, *, workflow_name: builtins.str) -> None:
        '''A reference to a Workflow resource.

        :param workflow_name: The Name of the Workflow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            workflow_reference = interfaces_glue.WorkflowReference(
                workflow_name="workflowName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__05490662a534e7ac737a01a3e54258abf2c5d6dd3a563391b841bd656b5b6220)
            check_type(argname="argument workflow_name", value=workflow_name, expected_type=type_hints["workflow_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_name": workflow_name,
        }

    @builtins.property
    def workflow_name(self) -> builtins.str:
        '''The Name of the Workflow resource.'''
        result = self._values.get("workflow_name")
        assert result is not None, "Required property 'workflow_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BlueprintReference",
    "CatalogReference",
    "ClassifierReference",
    "ConnectionReference",
    "ConnectionTypeReference",
    "CrawlerReference",
    "CustomEntityTypeReference",
    "DataCatalogEncryptionSettingsReference",
    "DataQualityRulesetReference",
    "DatabaseReference",
    "DevEndpointReference",
    "IBlueprintRef",
    "ICatalogRef",
    "IClassifierRef",
    "IConnectionRef",
    "IConnectionTypeRef",
    "ICrawlerRef",
    "ICustomEntityTypeRef",
    "IDataCatalogEncryptionSettingsRef",
    "IDataQualityRulesetRef",
    "IDatabaseRef",
    "IDevEndpointRef",
    "IIdentityCenterConfigurationRef",
    "IIntegrationRef",
    "IIntegrationResourcePropertyRef",
    "IJobRef",
    "IMLTransformRef",
    "IPartitionRef",
    "IRegistryRef",
    "ISchemaRef",
    "ISchemaVersionMetadataRef",
    "ISchemaVersionRef",
    "ISecurityConfigurationRef",
    "ISessionRef",
    "ITableOptimizerRef",
    "ITableRef",
    "ITriggerRef",
    "IUsageProfileRef",
    "IUserDefinedFunctionRef",
    "IWorkflowRef",
    "IdentityCenterConfigurationReference",
    "IntegrationReference",
    "IntegrationResourcePropertyReference",
    "JobReference",
    "MLTransformReference",
    "PartitionReference",
    "RegistryReference",
    "SchemaReference",
    "SchemaVersionMetadataReference",
    "SchemaVersionReference",
    "SecurityConfigurationReference",
    "SessionReference",
    "TableOptimizerReference",
    "TableReference",
    "TriggerReference",
    "UsageProfileReference",
    "UserDefinedFunctionReference",
    "WorkflowReference",
]

publication.publish()

def _typecheckingstub__74f84cc3c6d0f263e9ddf1a55c7fdea806d5b8dc149e51187a6f8b187475d3c1(
    *,
    blueprint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f73a6ea26762ecbddcfac7ae43b16414e1d43933b3ed36504fa0600d7b87e382(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__153075acc355fb8c67c2595f86bb736959d7a3490470e1496c4634652a073e55(
    *,
    classifier_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0c23f5314f51a17152319ab80f389d2f1b18975384c84d1d2931ac1a3121d9f(
    *,
    catalog_id: builtins.str,
    connection_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4b9247a8aa2a5ea13fb42b422837b6534d7bdb249597cc280badd03a923cfd(
    *,
    connection_type_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad53740eb8897f033af56fd03963af3e4f644f727baf57ca71c35961fceb97b6(
    *,
    crawler_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2752daff245d03b65a99c918eff72a3eb4c7c58fc56a5bf622d9117515921d7f(
    *,
    custom_entity_type_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824f5a564c0864f04cf9c7b44937b6e5dbe2d9acb8bd8b048f28e3b1f667a924(
    *,
    catalog_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__637b7e752aad4e64a85b4673d0fd9fbde33283ca6452dac108809ad38887f3cd(
    *,
    data_quality_ruleset_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b006942e6851e8e5b67ab80d761f762e021506f9975b704097cc0df559962e7e(
    *,
    database_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__050454acd533b9c974358b1bfdec6277e66592a87a752610c62dc6b896b95d0f(
    *,
    endpoint_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce890d13c4e501fd50bfd966cbe5558eac1e8b2415bc6f873c45a675fef0455(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__487ef973bf980b9533ab5e35911c785df93801badcd04a6ad9191c32ce95e300(
    *,
    integration_arn: builtins.str,
    integration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78e927b289090d3ea11c2e52f58b5cdc45b50ebf0cb9ac19af7a86759d45975(
    *,
    resource_arn: builtins.str,
    resource_property_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c47c403cca6462755fa024cf63a9b8531d52ca6834543a739c13e8ee51c9e9(
    *,
    job_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f1a2f7b4f39bcc3b7be922b88fffd5ccf9f63df878ae375f85fa00250d7cff(
    *,
    transform_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a9698059eb8899c746fb237350793d2faff1bdfa61b71f202add91131734519(
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    identifier_partition_input_values: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f46875075b9b44d3958fe5be64778d351238ba406d2bfaf624a127c572ecfdd(
    *,
    registry_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b578c469d6ed870abb6802e9d10670c2f571c62a79988a4ded4d3dccbcf0754e(
    *,
    schema_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b127790a6c1e064bc511d8914a963c65c84be0739a54f9274fdb48b4f2105d(
    *,
    key: builtins.str,
    schema_version_id: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8183bbaf7cbe72ac30393afbba3db6508105f9305b6e69bf1acef9abffd833d2(
    *,
    version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f762055d8744dcdcadf6d3ee48e027edbbedb409f2aee69d69051529ab7d003(
    *,
    security_configuration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d556c62e8ccef01cb2ebde5bdf8e8e61850e36ae87a512eb64e73be540ab0fa(
    *,
    session_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36d18932d532cd2df3f2355353c78a3d21a028fa0d2181f51b94ae7c9101726b(
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    table_name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91e1bc0dff8ee618900793d998bcf5ed91fd48153fcbcc02d63186fa2219535(
    *,
    table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85c96b93a2c298c01219667b5012a8e417cd40c14e36afd3fd093081bbfc5a3e(
    *,
    trigger_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31cd7baf9c81bae2e0d29221ca6cf6bf1b06b730a8c9d8fedf8630e653710373(
    *,
    usage_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e1ff3d4751c7ba1689180d09777a0d7407fc90ef06c219bedeb2047180cc973(
    *,
    user_defined_function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05490662a534e7ac737a01a3e54258abf2c5d6dd3a563391b841bd656b5b6220(
    *,
    workflow_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBlueprintRef, ICatalogRef, IClassifierRef, IConnectionRef, IConnectionTypeRef, ICrawlerRef, ICustomEntityTypeRef, IDataCatalogEncryptionSettingsRef, IDataQualityRulesetRef, IDatabaseRef, IDevEndpointRef, IIdentityCenterConfigurationRef, IIntegrationRef, IIntegrationResourcePropertyRef, IJobRef, IMLTransformRef, IPartitionRef, IRegistryRef, ISchemaRef, ISchemaVersionMetadataRef, ISchemaVersionRef, ISecurityConfigurationRef, ISessionRef, ITableOptimizerRef, ITableRef, ITriggerRef, IUsageProfileRef, IUserDefinedFunctionRef, IWorkflowRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
