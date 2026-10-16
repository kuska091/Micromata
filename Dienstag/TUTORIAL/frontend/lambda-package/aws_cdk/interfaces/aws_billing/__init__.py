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
    jsii_type="aws-cdk-lib.interfaces.aws_billing.BillingViewReference",
    jsii_struct_bases=[],
    name_mapping={"billing_view_arn": "billingViewArn"},
)
class BillingViewReference:
    def __init__(self, *, billing_view_arn: builtins.str) -> None:
        '''A reference to a BillingView resource.

        :param billing_view_arn: The Arn of the BillingView resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_billing as interfaces_billing
            
            billing_view_reference = interfaces_billing.BillingViewReference(
                billing_view_arn="billingViewArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1b420f8e76050ee04d846a5cb0ac8ea3244a1e7a1f22883dd09601802d06f2c9)
            check_type(argname="argument billing_view_arn", value=billing_view_arn, expected_type=type_hints["billing_view_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "billing_view_arn": billing_view_arn,
        }

    @builtins.property
    def billing_view_arn(self) -> builtins.str:
        '''The Arn of the BillingView resource.'''
        result = self._values.get("billing_view_arn")
        assert result is not None, "Required property 'billing_view_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingViewReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_billing.IBillingViewRef")
class IBillingViewRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BillingView.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="billingViewRef")
    def billing_view_ref(self) -> "BillingViewReference":
        '''(experimental) A reference to a BillingView resource.

        :stability: experimental
        '''
        ...


class _IBillingViewRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BillingView.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_billing.IBillingViewRef"

    @builtins.property
    @jsii.member(jsii_name="billingViewRef")
    def billing_view_ref(self) -> "BillingViewReference":
        '''(experimental) A reference to a BillingView resource.

        :stability: experimental
        '''
        return typing.cast("BillingViewReference", jsii.get(self, "billingViewRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBillingViewRef).__jsii_proxy_class__ = lambda : _IBillingViewRefProxy


__all__ = [
    "BillingViewReference",
    "IBillingViewRef",
]

publication.publish()

def _typecheckingstub__1b420f8e76050ee04d846a5cb0ac8ea3244a1e7a1f22883dd09601802d06f2c9(
    *,
    billing_view_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBillingViewRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
