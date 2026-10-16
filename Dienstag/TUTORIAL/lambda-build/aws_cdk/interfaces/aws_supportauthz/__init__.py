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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_supportauthz.ISupportPermitRef")
class ISupportPermitRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SupportPermit.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="supportPermitRef")
    def support_permit_ref(self) -> "SupportPermitReference":
        '''(experimental) A reference to a SupportPermit resource.

        :stability: experimental
        '''
        ...


class _ISupportPermitRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SupportPermit.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_supportauthz.ISupportPermitRef"

    @builtins.property
    @jsii.member(jsii_name="supportPermitRef")
    def support_permit_ref(self) -> "SupportPermitReference":
        '''(experimental) A reference to a SupportPermit resource.

        :stability: experimental
        '''
        return typing.cast("SupportPermitReference", jsii.get(self, "supportPermitRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISupportPermitRef).__jsii_proxy_class__ = lambda : _ISupportPermitRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_supportauthz.SupportPermitReference",
    jsii_struct_bases=[],
    name_mapping={"support_permit_arn": "supportPermitArn"},
)
class SupportPermitReference:
    def __init__(self, *, support_permit_arn: builtins.str) -> None:
        '''A reference to a SupportPermit resource.

        :param support_permit_arn: The Arn of the SupportPermit resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_supportauthz as interfaces_supportauthz
            
            support_permit_reference = interfaces_supportauthz.SupportPermitReference(
                support_permit_arn="supportPermitArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8e894ab4afac15271901a7fb15247eadb02a57ae1a946bcee99a3545601d7bbd)
            check_type(argname="argument support_permit_arn", value=support_permit_arn, expected_type=type_hints["support_permit_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "support_permit_arn": support_permit_arn,
        }

    @builtins.property
    def support_permit_arn(self) -> builtins.str:
        '''The Arn of the SupportPermit resource.'''
        result = self._values.get("support_permit_arn")
        assert result is not None, "Required property 'support_permit_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SupportPermitReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ISupportPermitRef",
    "SupportPermitReference",
]

publication.publish()

def _typecheckingstub__8e894ab4afac15271901a7fb15247eadb02a57ae1a946bcee99a3545601d7bbd(
    *,
    support_permit_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ISupportPermitRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
