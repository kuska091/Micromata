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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_invoicing.IInvoiceUnitRef")
class IInvoiceUnitRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InvoiceUnit.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="invoiceUnitRef")
    def invoice_unit_ref(self) -> "InvoiceUnitReference":
        '''(experimental) A reference to a InvoiceUnit resource.

        :stability: experimental
        '''
        ...


class _IInvoiceUnitRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InvoiceUnit.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_invoicing.IInvoiceUnitRef"

    @builtins.property
    @jsii.member(jsii_name="invoiceUnitRef")
    def invoice_unit_ref(self) -> "InvoiceUnitReference":
        '''(experimental) A reference to a InvoiceUnit resource.

        :stability: experimental
        '''
        return typing.cast("InvoiceUnitReference", jsii.get(self, "invoiceUnitRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInvoiceUnitRef).__jsii_proxy_class__ = lambda : _IInvoiceUnitRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_invoicing.IProcurementPortalPreferenceRef"
)
class IProcurementPortalPreferenceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProcurementPortalPreference.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="procurementPortalPreferenceRef")
    def procurement_portal_preference_ref(
        self,
    ) -> "ProcurementPortalPreferenceReference":
        '''(experimental) A reference to a ProcurementPortalPreference resource.

        :stability: experimental
        '''
        ...


class _IProcurementPortalPreferenceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProcurementPortalPreference.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_invoicing.IProcurementPortalPreferenceRef"

    @builtins.property
    @jsii.member(jsii_name="procurementPortalPreferenceRef")
    def procurement_portal_preference_ref(
        self,
    ) -> "ProcurementPortalPreferenceReference":
        '''(experimental) A reference to a ProcurementPortalPreference resource.

        :stability: experimental
        '''
        return typing.cast("ProcurementPortalPreferenceReference", jsii.get(self, "procurementPortalPreferenceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProcurementPortalPreferenceRef).__jsii_proxy_class__ = lambda : _IProcurementPortalPreferenceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_invoicing.InvoiceUnitReference",
    jsii_struct_bases=[],
    name_mapping={"invoice_unit_arn": "invoiceUnitArn"},
)
class InvoiceUnitReference:
    def __init__(self, *, invoice_unit_arn: builtins.str) -> None:
        '''A reference to a InvoiceUnit resource.

        :param invoice_unit_arn: The InvoiceUnitArn of the InvoiceUnit resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_invoicing as interfaces_invoicing
            
            invoice_unit_reference = interfaces_invoicing.InvoiceUnitReference(
                invoice_unit_arn="invoiceUnitArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9e1bc14d8a543b4d8a37813d74724155f93908a344cc67210c22eb17864474bc)
            check_type(argname="argument invoice_unit_arn", value=invoice_unit_arn, expected_type=type_hints["invoice_unit_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "invoice_unit_arn": invoice_unit_arn,
        }

    @builtins.property
    def invoice_unit_arn(self) -> builtins.str:
        '''The InvoiceUnitArn of the InvoiceUnit resource.'''
        result = self._values.get("invoice_unit_arn")
        assert result is not None, "Required property 'invoice_unit_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InvoiceUnitReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_invoicing.ProcurementPortalPreferenceReference",
    jsii_struct_bases=[],
    name_mapping={
        "procurement_portal_preference_arn": "procurementPortalPreferenceArn",
    },
)
class ProcurementPortalPreferenceReference:
    def __init__(self, *, procurement_portal_preference_arn: builtins.str) -> None:
        '''A reference to a ProcurementPortalPreference resource.

        :param procurement_portal_preference_arn: The ProcurementPortalPreferenceArn of the ProcurementPortalPreference resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_invoicing as interfaces_invoicing
            
            procurement_portal_preference_reference = interfaces_invoicing.ProcurementPortalPreferenceReference(
                procurement_portal_preference_arn="procurementPortalPreferenceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e08da91a4b7587f275fad4dd1780aa9cc69771d7603ca6a0444219be4a2e5e36)
            check_type(argname="argument procurement_portal_preference_arn", value=procurement_portal_preference_arn, expected_type=type_hints["procurement_portal_preference_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "procurement_portal_preference_arn": procurement_portal_preference_arn,
        }

    @builtins.property
    def procurement_portal_preference_arn(self) -> builtins.str:
        '''The ProcurementPortalPreferenceArn of the ProcurementPortalPreference resource.'''
        result = self._values.get("procurement_portal_preference_arn")
        assert result is not None, "Required property 'procurement_portal_preference_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProcurementPortalPreferenceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IInvoiceUnitRef",
    "IProcurementPortalPreferenceRef",
    "InvoiceUnitReference",
    "ProcurementPortalPreferenceReference",
]

publication.publish()

def _typecheckingstub__9e1bc14d8a543b4d8a37813d74724155f93908a344cc67210c22eb17864474bc(
    *,
    invoice_unit_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e08da91a4b7587f275fad4dd1780aa9cc69771d7603ca6a0444219be4a2e5e36(
    *,
    procurement_portal_preference_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IInvoiceUnitRef, IProcurementPortalPreferenceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
