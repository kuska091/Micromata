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
    jsii_type="aws-cdk-lib.interfaces.aws_opensearch.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={"data_source_arn": "dataSourceArn"},
)
class DataSourceReference:
    def __init__(self, *, data_source_arn: builtins.str) -> None:
        '''A reference to a DataSource resource.

        :param data_source_arn: The Arn of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearch as interfaces_opensearch
            
            data_source_reference = interfaces_opensearch.DataSourceReference(
                data_source_arn="dataSourceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7bceca273f0dcdb71ec059e6c70ffebc6f1e96a6f44ed7462dd23d2adf7af0e2)
            check_type(argname="argument data_source_arn", value=data_source_arn, expected_type=type_hints["data_source_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_arn": data_source_arn,
        }

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The Arn of the DataSource resource.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opensearch.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearch.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


__all__ = [
    "DataSourceReference",
    "IDataSourceRef",
]

publication.publish()

def _typecheckingstub__7bceca273f0dcdb71ec059e6c70ffebc6f1e96a6f44ed7462dd23d2adf7af0e2(
    *,
    data_source_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDataSourceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
