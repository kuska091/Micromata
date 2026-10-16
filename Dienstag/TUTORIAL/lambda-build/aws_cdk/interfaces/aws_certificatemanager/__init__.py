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
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.AccountReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class AccountReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a Account resource.

        :param account_id: The AccountId of the Account resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_certificatemanager as interfaces_certificatemanager
            
            account_reference = interfaces_certificatemanager.AccountReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__159c8945326c35b29d1ebc3cee0ceaf15f106314c5b1bd9f9e99b0e6b54e3647)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the Account resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.AcmeDomainValidationReference",
    jsii_struct_bases=[],
    name_mapping={"acme_domain_validation_arn": "acmeDomainValidationArn"},
)
class AcmeDomainValidationReference:
    def __init__(self, *, acme_domain_validation_arn: builtins.str) -> None:
        '''A reference to a AcmeDomainValidation resource.

        :param acme_domain_validation_arn: The Arn of the AcmeDomainValidation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_certificatemanager as interfaces_certificatemanager
            
            acme_domain_validation_reference = interfaces_certificatemanager.AcmeDomainValidationReference(
                acme_domain_validation_arn="acmeDomainValidationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c2f082673d80d23de00bc64c055947ebdfbff033619cec67dd64f2edfdfb19f6)
            check_type(argname="argument acme_domain_validation_arn", value=acme_domain_validation_arn, expected_type=type_hints["acme_domain_validation_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acme_domain_validation_arn": acme_domain_validation_arn,
        }

    @builtins.property
    def acme_domain_validation_arn(self) -> builtins.str:
        '''The Arn of the AcmeDomainValidation resource.'''
        result = self._values.get("acme_domain_validation_arn")
        assert result is not None, "Required property 'acme_domain_validation_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmeDomainValidationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.AcmeEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"acme_endpoint_arn": "acmeEndpointArn"},
)
class AcmeEndpointReference:
    def __init__(self, *, acme_endpoint_arn: builtins.str) -> None:
        '''A reference to a AcmeEndpoint resource.

        :param acme_endpoint_arn: The AcmeEndpointArn of the AcmeEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_certificatemanager as interfaces_certificatemanager
            
            acme_endpoint_reference = interfaces_certificatemanager.AcmeEndpointReference(
                acme_endpoint_arn="acmeEndpointArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__306a982bf59744dd8da1afdcfa0904590353198912b0a93472d7e74ec4df3293)
            check_type(argname="argument acme_endpoint_arn", value=acme_endpoint_arn, expected_type=type_hints["acme_endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acme_endpoint_arn": acme_endpoint_arn,
        }

    @builtins.property
    def acme_endpoint_arn(self) -> builtins.str:
        '''The AcmeEndpointArn of the AcmeEndpoint resource.'''
        result = self._values.get("acme_endpoint_arn")
        assert result is not None, "Required property 'acme_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmeEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.AcmeExternalAccountBindingReference",
    jsii_struct_bases=[],
    name_mapping={
        "acme_external_account_binding_arn": "acmeExternalAccountBindingArn",
    },
)
class AcmeExternalAccountBindingReference:
    def __init__(self, *, acme_external_account_binding_arn: builtins.str) -> None:
        '''A reference to a AcmeExternalAccountBinding resource.

        :param acme_external_account_binding_arn: The AcmeExternalAccountBindingArn of the AcmeExternalAccountBinding resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_certificatemanager as interfaces_certificatemanager
            
            acme_external_account_binding_reference = interfaces_certificatemanager.AcmeExternalAccountBindingReference(
                acme_external_account_binding_arn="acmeExternalAccountBindingArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bf00c9f351d7c651cf1400d81a66cd919ff75aa88bc07d23ae5d19a51fa7ed33)
            check_type(argname="argument acme_external_account_binding_arn", value=acme_external_account_binding_arn, expected_type=type_hints["acme_external_account_binding_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acme_external_account_binding_arn": acme_external_account_binding_arn,
        }

    @builtins.property
    def acme_external_account_binding_arn(self) -> builtins.str:
        '''The AcmeExternalAccountBindingArn of the AcmeExternalAccountBinding resource.'''
        result = self._values.get("acme_external_account_binding_arn")
        assert result is not None, "Required property 'acme_external_account_binding_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmeExternalAccountBindingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.CertificateReference",
    jsii_struct_bases=[],
    name_mapping={"certificate_arn": "certificateArn"},
)
class CertificateReference:
    def __init__(self, *, certificate_arn: builtins.str) -> None:
        '''A reference to a Certificate resource.

        :param certificate_arn: The CertificateArn of the Certificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_certificatemanager as interfaces_certificatemanager
            
            certificate_reference = interfaces_certificatemanager.CertificateReference(
                certificate_arn="certificateArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__da5e0111dc240001304a5eccb1ff5f839789b5eba06c7b66c6a6a3c8491a98fd)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
        }

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''The CertificateArn of the Certificate resource.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.IAccountRef")
class IAccountRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Account.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accountRef")
    def account_ref(self) -> "AccountReference":
        '''(experimental) A reference to a Account resource.

        :stability: experimental
        '''
        ...


class _IAccountRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Account.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_certificatemanager.IAccountRef"

    @builtins.property
    @jsii.member(jsii_name="accountRef")
    def account_ref(self) -> "AccountReference":
        '''(experimental) A reference to a Account resource.

        :stability: experimental
        '''
        return typing.cast("AccountReference", jsii.get(self, "accountRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccountRef).__jsii_proxy_class__ = lambda : _IAccountRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.IAcmeDomainValidationRef"
)
class IAcmeDomainValidationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AcmeDomainValidation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="acmeDomainValidationRef")
    def acme_domain_validation_ref(self) -> "AcmeDomainValidationReference":
        '''(experimental) A reference to a AcmeDomainValidation resource.

        :stability: experimental
        '''
        ...


class _IAcmeDomainValidationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AcmeDomainValidation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_certificatemanager.IAcmeDomainValidationRef"

    @builtins.property
    @jsii.member(jsii_name="acmeDomainValidationRef")
    def acme_domain_validation_ref(self) -> "AcmeDomainValidationReference":
        '''(experimental) A reference to a AcmeDomainValidation resource.

        :stability: experimental
        '''
        return typing.cast("AcmeDomainValidationReference", jsii.get(self, "acmeDomainValidationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAcmeDomainValidationRef).__jsii_proxy_class__ = lambda : _IAcmeDomainValidationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.IAcmeEndpointRef"
)
class IAcmeEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AcmeEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="acmeEndpointRef")
    def acme_endpoint_ref(self) -> "AcmeEndpointReference":
        '''(experimental) A reference to a AcmeEndpoint resource.

        :stability: experimental
        '''
        ...


class _IAcmeEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AcmeEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_certificatemanager.IAcmeEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="acmeEndpointRef")
    def acme_endpoint_ref(self) -> "AcmeEndpointReference":
        '''(experimental) A reference to a AcmeEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("AcmeEndpointReference", jsii.get(self, "acmeEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAcmeEndpointRef).__jsii_proxy_class__ = lambda : _IAcmeEndpointRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.IAcmeExternalAccountBindingRef"
)
class IAcmeExternalAccountBindingRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AcmeExternalAccountBinding.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="acmeExternalAccountBindingRef")
    def acme_external_account_binding_ref(
        self,
    ) -> "AcmeExternalAccountBindingReference":
        '''(experimental) A reference to a AcmeExternalAccountBinding resource.

        :stability: experimental
        '''
        ...


class _IAcmeExternalAccountBindingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AcmeExternalAccountBinding.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_certificatemanager.IAcmeExternalAccountBindingRef"

    @builtins.property
    @jsii.member(jsii_name="acmeExternalAccountBindingRef")
    def acme_external_account_binding_ref(
        self,
    ) -> "AcmeExternalAccountBindingReference":
        '''(experimental) A reference to a AcmeExternalAccountBinding resource.

        :stability: experimental
        '''
        return typing.cast("AcmeExternalAccountBindingReference", jsii.get(self, "acmeExternalAccountBindingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAcmeExternalAccountBindingRef).__jsii_proxy_class__ = lambda : _IAcmeExternalAccountBindingRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_certificatemanager.ICertificateRef"
)
class ICertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Certificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        ...


class _ICertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Certificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_certificatemanager.ICertificateRef"

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        return typing.cast("CertificateReference", jsii.get(self, "certificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateRef).__jsii_proxy_class__ = lambda : _ICertificateRefProxy


__all__ = [
    "AccountReference",
    "AcmeDomainValidationReference",
    "AcmeEndpointReference",
    "AcmeExternalAccountBindingReference",
    "CertificateReference",
    "IAccountRef",
    "IAcmeDomainValidationRef",
    "IAcmeEndpointRef",
    "IAcmeExternalAccountBindingRef",
    "ICertificateRef",
]

publication.publish()

def _typecheckingstub__159c8945326c35b29d1ebc3cee0ceaf15f106314c5b1bd9f9e99b0e6b54e3647(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2f082673d80d23de00bc64c055947ebdfbff033619cec67dd64f2edfdfb19f6(
    *,
    acme_domain_validation_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__306a982bf59744dd8da1afdcfa0904590353198912b0a93472d7e74ec4df3293(
    *,
    acme_endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf00c9f351d7c651cf1400d81a66cd919ff75aa88bc07d23ae5d19a51fa7ed33(
    *,
    acme_external_account_binding_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5e0111dc240001304a5eccb1ff5f839789b5eba06c7b66c6a6a3c8491a98fd(
    *,
    certificate_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccountRef, IAcmeDomainValidationRef, IAcmeEndpointRef, IAcmeExternalAccountBindingRef, ICertificateRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
