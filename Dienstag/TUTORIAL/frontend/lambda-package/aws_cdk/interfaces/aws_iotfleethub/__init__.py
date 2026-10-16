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
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleethub.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn"},
)
class ApplicationReference:
    def __init__(self, *, application_arn: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_arn: The ARN of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotfleethub as interfaces_iotfleethub
            
            application_reference = interfaces_iotfleethub.ApplicationReference(
                application_arn="applicationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__00995375b23956a66a2c2fcb9806442f494906c648a1b7a56cca2b8a8077ec8f)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ARN of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotfleethub.IApplicationRef")
class IApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        ...


class _IApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotfleethub.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


__all__ = [
    "ApplicationReference",
    "IApplicationRef",
]

publication.publish()

def _typecheckingstub__00995375b23956a66a2c2fcb9806442f494906c648a1b7a56cca2b8a8077ec8f(
    *,
    application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
