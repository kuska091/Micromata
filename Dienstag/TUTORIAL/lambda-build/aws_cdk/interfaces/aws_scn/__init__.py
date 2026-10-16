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
    jsii_type="aws-cdk-lib.interfaces.aws_scn.DataIntegrationFlowReference",
    jsii_struct_bases=[],
    name_mapping={"data_integration_flow_arn": "dataIntegrationFlowArn"},
)
class DataIntegrationFlowReference:
    def __init__(self, *, data_integration_flow_arn: builtins.str) -> None:
        '''A reference to a DataIntegrationFlow resource.

        :param data_integration_flow_arn: The Arn of the DataIntegrationFlow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_scn as interfaces_scn
            
            data_integration_flow_reference = interfaces_scn.DataIntegrationFlowReference(
                data_integration_flow_arn="dataIntegrationFlowArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__335d0e77b42ced5c9ddcb8af4146e1ef8ac0860716eac2de70800a3a63ce2fdf)
            check_type(argname="argument data_integration_flow_arn", value=data_integration_flow_arn, expected_type=type_hints["data_integration_flow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_integration_flow_arn": data_integration_flow_arn,
        }

    @builtins.property
    def data_integration_flow_arn(self) -> builtins.str:
        '''The Arn of the DataIntegrationFlow resource.'''
        result = self._values.get("data_integration_flow_arn")
        assert result is not None, "Required property 'data_integration_flow_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataIntegrationFlowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_scn.DatasetReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_arn": "datasetArn"},
)
class DatasetReference:
    def __init__(self, *, dataset_arn: builtins.str) -> None:
        '''A reference to a Dataset resource.

        :param dataset_arn: The Arn of the Dataset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_scn as interfaces_scn
            
            dataset_reference = interfaces_scn.DatasetReference(
                dataset_arn="datasetArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__58fbe378483e1a46065f6e5466be65a2a964d4985557e01efac8aec3109fb252)
            check_type(argname="argument dataset_arn", value=dataset_arn, expected_type=type_hints["dataset_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_arn": dataset_arn,
        }

    @builtins.property
    def dataset_arn(self) -> builtins.str:
        '''The Arn of the Dataset resource.'''
        result = self._values.get("dataset_arn")
        assert result is not None, "Required property 'dataset_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_scn.IDataIntegrationFlowRef")
class IDataIntegrationFlowRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataIntegrationFlow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataIntegrationFlowRef")
    def data_integration_flow_ref(self) -> "DataIntegrationFlowReference":
        '''(experimental) A reference to a DataIntegrationFlow resource.

        :stability: experimental
        '''
        ...


class _IDataIntegrationFlowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataIntegrationFlow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_scn.IDataIntegrationFlowRef"

    @builtins.property
    @jsii.member(jsii_name="dataIntegrationFlowRef")
    def data_integration_flow_ref(self) -> "DataIntegrationFlowReference":
        '''(experimental) A reference to a DataIntegrationFlow resource.

        :stability: experimental
        '''
        return typing.cast("DataIntegrationFlowReference", jsii.get(self, "dataIntegrationFlowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataIntegrationFlowRef).__jsii_proxy_class__ = lambda : _IDataIntegrationFlowRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_scn.IDatasetRef")
class IDatasetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Dataset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        ...


class _IDatasetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Dataset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_scn.IDatasetRef"

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        return typing.cast("DatasetReference", jsii.get(self, "datasetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetRef).__jsii_proxy_class__ = lambda : _IDatasetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_scn.INamespaceRef")
class INamespaceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Namespace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="namespaceRef")
    def namespace_ref(self) -> "NamespaceReference":
        '''(experimental) A reference to a Namespace resource.

        :stability: experimental
        '''
        ...


class _INamespaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Namespace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_scn.INamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="namespaceRef")
    def namespace_ref(self) -> "NamespaceReference":
        '''(experimental) A reference to a Namespace resource.

        :stability: experimental
        '''
        return typing.cast("NamespaceReference", jsii.get(self, "namespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INamespaceRef).__jsii_proxy_class__ = lambda : _INamespaceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_scn.NamespaceReference",
    jsii_struct_bases=[],
    name_mapping={"namespace_arn": "namespaceArn"},
)
class NamespaceReference:
    def __init__(self, *, namespace_arn: builtins.str) -> None:
        '''A reference to a Namespace resource.

        :param namespace_arn: The Arn of the Namespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_scn as interfaces_scn
            
            namespace_reference = interfaces_scn.NamespaceReference(
                namespace_arn="namespaceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b720fee81ff1d853f207c887b1294a00c89e23b2e20478eb262206b4253d4b2f)
            check_type(argname="argument namespace_arn", value=namespace_arn, expected_type=type_hints["namespace_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace_arn": namespace_arn,
        }

    @builtins.property
    def namespace_arn(self) -> builtins.str:
        '''The Arn of the Namespace resource.'''
        result = self._values.get("namespace_arn")
        assert result is not None, "Required property 'namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataIntegrationFlowReference",
    "DatasetReference",
    "IDataIntegrationFlowRef",
    "IDatasetRef",
    "INamespaceRef",
    "NamespaceReference",
]

publication.publish()

def _typecheckingstub__335d0e77b42ced5c9ddcb8af4146e1ef8ac0860716eac2de70800a3a63ce2fdf(
    *,
    data_integration_flow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58fbe378483e1a46065f6e5466be65a2a964d4985557e01efac8aec3109fb252(
    *,
    dataset_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b720fee81ff1d853f207c887b1294a00c89e23b2e20478eb262206b4253d4b2f(
    *,
    namespace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDataIntegrationFlowRef, IDatasetRef, INamespaceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
