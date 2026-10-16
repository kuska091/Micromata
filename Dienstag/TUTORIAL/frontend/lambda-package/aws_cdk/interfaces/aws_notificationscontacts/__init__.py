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
    jsii_type="aws-cdk-lib.interfaces.aws_notificationscontacts.EmailContactReference",
    jsii_struct_bases=[],
    name_mapping={"email_contact_arn": "emailContactArn"},
)
class EmailContactReference:
    def __init__(self, *, email_contact_arn: builtins.str) -> None:
        '''A reference to a EmailContact resource.

        :param email_contact_arn: The Arn of the EmailContact resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_notificationscontacts as interfaces_notificationscontacts
            
            email_contact_reference = interfaces_notificationscontacts.EmailContactReference(
                email_contact_arn="emailContactArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__476cc576f5b2d1eb9f5210807985bbc97df74675b9f9a4c49e8bed4653776646)
            check_type(argname="argument email_contact_arn", value=email_contact_arn, expected_type=type_hints["email_contact_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email_contact_arn": email_contact_arn,
        }

    @builtins.property
    def email_contact_arn(self) -> builtins.str:
        '''The Arn of the EmailContact resource.'''
        result = self._values.get("email_contact_arn")
        assert result is not None, "Required property 'email_contact_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailContactReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_notificationscontacts.IEmailContactRef"
)
class IEmailContactRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EmailContact.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="emailContactRef")
    def email_contact_ref(self) -> "EmailContactReference":
        '''(experimental) A reference to a EmailContact resource.

        :stability: experimental
        '''
        ...


class _IEmailContactRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EmailContact.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_notificationscontacts.IEmailContactRef"

    @builtins.property
    @jsii.member(jsii_name="emailContactRef")
    def email_contact_ref(self) -> "EmailContactReference":
        '''(experimental) A reference to a EmailContact resource.

        :stability: experimental
        '''
        return typing.cast("EmailContactReference", jsii.get(self, "emailContactRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEmailContactRef).__jsii_proxy_class__ = lambda : _IEmailContactRefProxy


__all__ = [
    "EmailContactReference",
    "IEmailContactRef",
]

publication.publish()

def _typecheckingstub__476cc576f5b2d1eb9f5210807985bbc97df74675b9f9a4c49e8bed4653776646(
    *,
    email_contact_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEmailContactRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
