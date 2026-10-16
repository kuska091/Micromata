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
    jsii_type="aws-cdk-lib.interfaces.aws_textract.AdapterReference",
    jsii_struct_bases=[],
    name_mapping={"adapter_arn": "adapterArn"},
)
class AdapterReference:
    def __init__(self, *, adapter_arn: builtins.str) -> None:
        '''A reference to a Adapter resource.

        :param adapter_arn: The Arn of the Adapter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_textract as interfaces_textract
            
            adapter_reference = interfaces_textract.AdapterReference(
                adapter_arn="adapterArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9bb2310aafbf06463094c745330a857231cfcedb663f339049c9ffae9152bdd1)
            check_type(argname="argument adapter_arn", value=adapter_arn, expected_type=type_hints["adapter_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "adapter_arn": adapter_arn,
        }

    @builtins.property
    def adapter_arn(self) -> builtins.str:
        '''The Arn of the Adapter resource.'''
        result = self._values.get("adapter_arn")
        assert result is not None, "Required property 'adapter_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdapterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_textract.IAdapterRef")
class IAdapterRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Adapter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="adapterRef")
    def adapter_ref(self) -> "AdapterReference":
        '''(experimental) A reference to a Adapter resource.

        :stability: experimental
        '''
        ...


class _IAdapterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Adapter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_textract.IAdapterRef"

    @builtins.property
    @jsii.member(jsii_name="adapterRef")
    def adapter_ref(self) -> "AdapterReference":
        '''(experimental) A reference to a Adapter resource.

        :stability: experimental
        '''
        return typing.cast("AdapterReference", jsii.get(self, "adapterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAdapterRef).__jsii_proxy_class__ = lambda : _IAdapterRefProxy


__all__ = [
    "AdapterReference",
    "IAdapterRef",
]

publication.publish()

def _typecheckingstub__9bb2310aafbf06463094c745330a857231cfcedb663f339049c9ffae9152bdd1(
    *,
    adapter_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAdapterRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
