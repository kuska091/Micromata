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
    jsii_type="aws-cdk-lib.interfaces.aws_paymentcryptography.AliasReference",
    jsii_struct_bases=[],
    name_mapping={"alias_name": "aliasName"},
)
class AliasReference:
    def __init__(self, *, alias_name: builtins.str) -> None:
        '''A reference to a Alias resource.

        :param alias_name: The AliasName of the Alias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_paymentcryptography as interfaces_paymentcryptography
            
            alias_reference = interfaces_paymentcryptography.AliasReference(
                alias_name="aliasName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c65d46218da026d09cdeca54761703fee21ed5f0c9acf1f26ecbae067a002314)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_name": alias_name,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The AliasName of the Alias resource.'''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_paymentcryptography.IAliasRef")
class IAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Alias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aliasRef")
    def alias_ref(self) -> "AliasReference":
        '''(experimental) A reference to a Alias resource.

        :stability: experimental
        '''
        ...


class _IAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Alias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_paymentcryptography.IAliasRef"

    @builtins.property
    @jsii.member(jsii_name="aliasRef")
    def alias_ref(self) -> "AliasReference":
        '''(experimental) A reference to a Alias resource.

        :stability: experimental
        '''
        return typing.cast("AliasReference", jsii.get(self, "aliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAliasRef).__jsii_proxy_class__ = lambda : _IAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_paymentcryptography.IKeyRef")
class IKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Key.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="keyRef")
    def key_ref(self) -> "KeyReference":
        '''(experimental) A reference to a Key resource.

        :stability: experimental
        '''
        ...


class _IKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Key.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_paymentcryptography.IKeyRef"

    @builtins.property
    @jsii.member(jsii_name="keyRef")
    def key_ref(self) -> "KeyReference":
        '''(experimental) A reference to a Key resource.

        :stability: experimental
        '''
        return typing.cast("KeyReference", jsii.get(self, "keyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeyRef).__jsii_proxy_class__ = lambda : _IKeyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_paymentcryptography.KeyReference",
    jsii_struct_bases=[],
    name_mapping={"key_identifier": "keyIdentifier"},
)
class KeyReference:
    def __init__(self, *, key_identifier: builtins.str) -> None:
        '''A reference to a Key resource.

        :param key_identifier: The KeyIdentifier of the Key resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_paymentcryptography as interfaces_paymentcryptography
            
            key_reference = interfaces_paymentcryptography.KeyReference(
                key_identifier="keyIdentifier"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4daabae5e3a601ac4ed9c5bd891e40b3fea075ef142ee8b0e6f27870084123b3)
            check_type(argname="argument key_identifier", value=key_identifier, expected_type=type_hints["key_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_identifier": key_identifier,
        }

    @builtins.property
    def key_identifier(self) -> builtins.str:
        '''The KeyIdentifier of the Key resource.'''
        result = self._values.get("key_identifier")
        assert result is not None, "Required property 'key_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AliasReference",
    "IAliasRef",
    "IKeyRef",
    "KeyReference",
]

publication.publish()

def _typecheckingstub__c65d46218da026d09cdeca54761703fee21ed5f0c9acf1f26ecbae067a002314(
    *,
    alias_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4daabae5e3a601ac4ed9c5bd891e40b3fea075ef142ee8b0e6f27870084123b3(
    *,
    key_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAliasRef, IKeyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
