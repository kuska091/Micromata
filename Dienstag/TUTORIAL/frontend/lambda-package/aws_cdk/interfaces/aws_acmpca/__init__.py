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
    jsii_type="aws-cdk-lib.interfaces.aws_acmpca.CertificateAuthorityActivationReference",
    jsii_struct_bases=[],
    name_mapping={"certificate_authority_arn": "certificateAuthorityArn"},
)
class CertificateAuthorityActivationReference:
    def __init__(self, *, certificate_authority_arn: builtins.str) -> None:
        '''A reference to a CertificateAuthorityActivation resource.

        :param certificate_authority_arn: The CertificateAuthorityArn of the CertificateAuthorityActivation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_acmpca as interfaces_acmpca
            
            certificate_authority_activation_reference = interfaces_acmpca.CertificateAuthorityActivationReference(
                certificate_authority_arn="certificateAuthorityArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e23e0c74cbcd309ca846ebc65a1406e1e62e4de6c291ba5444ad49d55870b992)
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arn": certificate_authority_arn,
        }

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The CertificateAuthorityArn of the CertificateAuthorityActivation resource.'''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateAuthorityActivationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_acmpca.CertificateAuthorityReference",
    jsii_struct_bases=[],
    name_mapping={"certificate_authority_arn": "certificateAuthorityArn"},
)
class CertificateAuthorityReference:
    def __init__(self, *, certificate_authority_arn: builtins.str) -> None:
        '''A reference to a CertificateAuthority resource.

        :param certificate_authority_arn: The Arn of the CertificateAuthority resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_acmpca as interfaces_acmpca
            
            certificate_authority_reference = interfaces_acmpca.CertificateAuthorityReference(
                certificate_authority_arn="certificateAuthorityArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4e639ef1a9e4c66dfa491293c1d496f5e14ff2595bcc0bcfda464a6a9864fcc2)
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arn": certificate_authority_arn,
        }

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The Arn of the CertificateAuthority resource.'''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateAuthorityReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_acmpca.CertificateReference",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_arn": "certificateArn",
        "certificate_authority_arn": "certificateAuthorityArn",
    },
)
class CertificateReference:
    def __init__(
        self,
        *,
        certificate_arn: builtins.str,
        certificate_authority_arn: builtins.str,
    ) -> None:
        '''A reference to a Certificate resource.

        :param certificate_arn: The Arn of the Certificate resource.
        :param certificate_authority_arn: The CertificateAuthorityArn of the Certificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_acmpca as interfaces_acmpca
            
            certificate_reference = interfaces_acmpca.CertificateReference(
                certificate_arn="certificateArn",
                certificate_authority_arn="certificateAuthorityArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__746d01cab9137f5ae4e7c002f97381a94ea87feedbf5b817f4713478b5f25677)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
            "certificate_authority_arn": certificate_authority_arn,
        }

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''The Arn of the Certificate resource.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The CertificateAuthorityArn of the Certificate resource.'''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_acmpca.ICertificateAuthorityActivationRef"
)
class ICertificateAuthorityActivationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CertificateAuthorityActivation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityActivationRef")
    def certificate_authority_activation_ref(
        self,
    ) -> "CertificateAuthorityActivationReference":
        '''(experimental) A reference to a CertificateAuthorityActivation resource.

        :stability: experimental
        '''
        ...


class _ICertificateAuthorityActivationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CertificateAuthorityActivation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_acmpca.ICertificateAuthorityActivationRef"

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityActivationRef")
    def certificate_authority_activation_ref(
        self,
    ) -> "CertificateAuthorityActivationReference":
        '''(experimental) A reference to a CertificateAuthorityActivation resource.

        :stability: experimental
        '''
        return typing.cast("CertificateAuthorityActivationReference", jsii.get(self, "certificateAuthorityActivationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateAuthorityActivationRef).__jsii_proxy_class__ = lambda : _ICertificateAuthorityActivationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_acmpca.ICertificateAuthorityRef")
class ICertificateAuthorityRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CertificateAuthority.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityRef")
    def certificate_authority_ref(self) -> "CertificateAuthorityReference":
        '''(experimental) A reference to a CertificateAuthority resource.

        :stability: experimental
        '''
        ...


class _ICertificateAuthorityRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CertificateAuthority.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_acmpca.ICertificateAuthorityRef"

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityRef")
    def certificate_authority_ref(self) -> "CertificateAuthorityReference":
        '''(experimental) A reference to a CertificateAuthority resource.

        :stability: experimental
        '''
        return typing.cast("CertificateAuthorityReference", jsii.get(self, "certificateAuthorityRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateAuthorityRef).__jsii_proxy_class__ = lambda : _ICertificateAuthorityRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_acmpca.ICertificateRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_acmpca.ICertificateRef"

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        return typing.cast("CertificateReference", jsii.get(self, "certificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateRef).__jsii_proxy_class__ = lambda : _ICertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_acmpca.IPermissionRef")
class IPermissionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Permission.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="permissionRef")
    def permission_ref(self) -> "PermissionReference":
        '''(experimental) A reference to a Permission resource.

        :stability: experimental
        '''
        ...


class _IPermissionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Permission.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_acmpca.IPermissionRef"

    @builtins.property
    @jsii.member(jsii_name="permissionRef")
    def permission_ref(self) -> "PermissionReference":
        '''(experimental) A reference to a Permission resource.

        :stability: experimental
        '''
        return typing.cast("PermissionReference", jsii.get(self, "permissionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPermissionRef).__jsii_proxy_class__ = lambda : _IPermissionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_acmpca.PermissionReference",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_authority_arn": "certificateAuthorityArn",
        "principal": "principal",
    },
)
class PermissionReference:
    def __init__(
        self,
        *,
        certificate_authority_arn: builtins.str,
        principal: builtins.str,
    ) -> None:
        '''A reference to a Permission resource.

        :param certificate_authority_arn: The CertificateAuthorityArn of the Permission resource.
        :param principal: The Principal of the Permission resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_acmpca as interfaces_acmpca
            
            permission_reference = interfaces_acmpca.PermissionReference(
                certificate_authority_arn="certificateAuthorityArn",
                principal="principal"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8747435620ec2e2c1717ff8b6d1bae5fbe0327671b2b20a18d2dd8361e4b6998)
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arn": certificate_authority_arn,
            "principal": principal,
        }

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The CertificateAuthorityArn of the Permission resource.'''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''The Principal of the Permission resource.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PermissionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CertificateAuthorityActivationReference",
    "CertificateAuthorityReference",
    "CertificateReference",
    "ICertificateAuthorityActivationRef",
    "ICertificateAuthorityRef",
    "ICertificateRef",
    "IPermissionRef",
    "PermissionReference",
]

publication.publish()

def _typecheckingstub__e23e0c74cbcd309ca846ebc65a1406e1e62e4de6c291ba5444ad49d55870b992(
    *,
    certificate_authority_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e639ef1a9e4c66dfa491293c1d496f5e14ff2595bcc0bcfda464a6a9864fcc2(
    *,
    certificate_authority_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746d01cab9137f5ae4e7c002f97381a94ea87feedbf5b817f4713478b5f25677(
    *,
    certificate_arn: builtins.str,
    certificate_authority_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8747435620ec2e2c1717ff8b6d1bae5fbe0327671b2b20a18d2dd8361e4b6998(
    *,
    certificate_authority_arn: builtins.str,
    principal: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICertificateAuthorityActivationRef, ICertificateAuthorityRef, ICertificateRef, IPermissionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
