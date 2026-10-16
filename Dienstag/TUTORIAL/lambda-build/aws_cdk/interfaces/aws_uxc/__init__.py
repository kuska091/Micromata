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
    jsii_type="aws-cdk-lib.interfaces.aws_uxc.AccountCustomizationReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class AccountCustomizationReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a AccountCustomization resource.

        :param account_id: The AccountId of the AccountCustomization resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_uxc as interfaces_uxc
            
            account_customization_reference = interfaces_uxc.AccountCustomizationReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b524ce75dfdd13574d1d5d7ea878790755405050d1198fe620786f1d2d9f04b7)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the AccountCustomization resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountCustomizationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_uxc.IAccountCustomizationRef")
class IAccountCustomizationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccountCustomization.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accountCustomizationRef")
    def account_customization_ref(self) -> "AccountCustomizationReference":
        '''(experimental) A reference to a AccountCustomization resource.

        :stability: experimental
        '''
        ...


class _IAccountCustomizationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccountCustomization.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_uxc.IAccountCustomizationRef"

    @builtins.property
    @jsii.member(jsii_name="accountCustomizationRef")
    def account_customization_ref(self) -> "AccountCustomizationReference":
        '''(experimental) A reference to a AccountCustomization resource.

        :stability: experimental
        '''
        return typing.cast("AccountCustomizationReference", jsii.get(self, "accountCustomizationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccountCustomizationRef).__jsii_proxy_class__ = lambda : _IAccountCustomizationRefProxy


__all__ = [
    "AccountCustomizationReference",
    "IAccountCustomizationRef",
]

publication.publish()

def _typecheckingstub__b524ce75dfdd13574d1d5d7ea878790755405050d1198fe620786f1d2d9f04b7(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccountCustomizationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
