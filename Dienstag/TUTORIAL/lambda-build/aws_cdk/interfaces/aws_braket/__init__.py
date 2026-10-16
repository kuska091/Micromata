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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_braket.ISpendingLimitRef")
class ISpendingLimitRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SpendingLimit.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="spendingLimitRef")
    def spending_limit_ref(self) -> "SpendingLimitReference":
        '''(experimental) A reference to a SpendingLimit resource.

        :stability: experimental
        '''
        ...


class _ISpendingLimitRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SpendingLimit.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_braket.ISpendingLimitRef"

    @builtins.property
    @jsii.member(jsii_name="spendingLimitRef")
    def spending_limit_ref(self) -> "SpendingLimitReference":
        '''(experimental) A reference to a SpendingLimit resource.

        :stability: experimental
        '''
        return typing.cast("SpendingLimitReference", jsii.get(self, "spendingLimitRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISpendingLimitRef).__jsii_proxy_class__ = lambda : _ISpendingLimitRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_braket.SpendingLimitReference",
    jsii_struct_bases=[],
    name_mapping={"spending_limit_arn": "spendingLimitArn"},
)
class SpendingLimitReference:
    def __init__(self, *, spending_limit_arn: builtins.str) -> None:
        '''A reference to a SpendingLimit resource.

        :param spending_limit_arn: The SpendingLimitArn of the SpendingLimit resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_braket as interfaces_braket
            
            spending_limit_reference = interfaces_braket.SpendingLimitReference(
                spending_limit_arn="spendingLimitArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__29a37ac823f2e44c245564f4dac8272bbbb57a1bef82b0cce5a57f4a4bb0a2ed)
            check_type(argname="argument spending_limit_arn", value=spending_limit_arn, expected_type=type_hints["spending_limit_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "spending_limit_arn": spending_limit_arn,
        }

    @builtins.property
    def spending_limit_arn(self) -> builtins.str:
        '''The SpendingLimitArn of the SpendingLimit resource.'''
        result = self._values.get("spending_limit_arn")
        assert result is not None, "Required property 'spending_limit_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpendingLimitReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ISpendingLimitRef",
    "SpendingLimitReference",
]

publication.publish()

def _typecheckingstub__29a37ac823f2e44c245564f4dac8272bbbb57a1bef82b0cce5a57f4a4bb0a2ed(
    *,
    spending_limit_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ISpendingLimitRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
