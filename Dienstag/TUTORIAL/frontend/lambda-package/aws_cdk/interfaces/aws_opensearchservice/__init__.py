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
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchservice.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_arn": "applicationArn",
        "application_name": "applicationName",
    },
)
class ApplicationReference:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        application_name: builtins.str,
    ) -> None:
        '''A reference to a Application resource.

        :param application_arn: The ARN of the Application resource.
        :param application_name: The Name of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchservice as interfaces_opensearchservice
            
            application_reference = interfaces_opensearchservice.ApplicationReference(
                application_arn="applicationArn",
                application_name="applicationName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__653505cb84ffd67d5a8b074186a5eec309028697d8d960b11981079024303304)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "application_name": application_name,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ARN of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The Name of the Application resource.'''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchservice.DomainReference",
    jsii_struct_bases=[],
    name_mapping={"domain_arn": "domainArn", "domain_name": "domainName"},
)
class DomainReference:
    def __init__(self, *, domain_arn: builtins.str, domain_name: builtins.str) -> None:
        '''A reference to a Domain resource.

        :param domain_arn: The ARN of the Domain resource.
        :param domain_name: The DomainName of the Domain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchservice as interfaces_opensearchservice
            
            domain_reference = interfaces_opensearchservice.DomainReference(
                domain_arn="domainArn",
                domain_name="domainName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__55b4b43243b00404cbed9c6f7ee53fefed3df2b9d7097f0f4f23221ca2046924)
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_arn": domain_arn,
            "domain_name": domain_name,
        }

    @builtins.property
    def domain_arn(self) -> builtins.str:
        '''The ARN of the Domain resource.'''
        result = self._values.get("domain_arn")
        assert result is not None, "Required property 'domain_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the Domain resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchservice.IApplicationRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchservice.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opensearchservice.IDomainRef")
class IDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        ...


class _IDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchservice.IDomainRef"

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        return typing.cast("DomainReference", jsii.get(self, "domainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainRef).__jsii_proxy_class__ = lambda : _IDomainRefProxy


__all__ = [
    "ApplicationReference",
    "DomainReference",
    "IApplicationRef",
    "IDomainRef",
]

publication.publish()

def _typecheckingstub__653505cb84ffd67d5a8b074186a5eec309028697d8d960b11981079024303304(
    *,
    application_arn: builtins.str,
    application_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55b4b43243b00404cbed9c6f7ee53fefed3df2b9d7097f0f4f23221ca2046924(
    *,
    domain_arn: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IDomainRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
