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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_agentregistry.IRegistryRecordRef"
)
class IRegistryRecordRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RegistryRecord.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="registryRecordRef")
    def registry_record_ref(self) -> "RegistryRecordReference":
        '''(experimental) A reference to a RegistryRecord resource.

        :stability: experimental
        '''
        ...


class _IRegistryRecordRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RegistryRecord.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_agentregistry.IRegistryRecordRef"

    @builtins.property
    @jsii.member(jsii_name="registryRecordRef")
    def registry_record_ref(self) -> "RegistryRecordReference":
        '''(experimental) A reference to a RegistryRecord resource.

        :stability: experimental
        '''
        return typing.cast("RegistryRecordReference", jsii.get(self, "registryRecordRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegistryRecordRef).__jsii_proxy_class__ = lambda : _IRegistryRecordRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_agentregistry.IRegistryRef")
class IRegistryRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Registry.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "RegistryReference":
        '''(experimental) A reference to a Registry resource.

        :stability: experimental
        '''
        ...


class _IRegistryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Registry.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_agentregistry.IRegistryRef"

    @builtins.property
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "RegistryReference":
        '''(experimental) A reference to a Registry resource.

        :stability: experimental
        '''
        return typing.cast("RegistryReference", jsii.get(self, "registryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegistryRef).__jsii_proxy_class__ = lambda : _IRegistryRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_agentregistry.RegistryRecordReference",
    jsii_struct_bases=[],
    name_mapping={"record_arn": "recordArn"},
)
class RegistryRecordReference:
    def __init__(self, *, record_arn: builtins.str) -> None:
        '''A reference to a RegistryRecord resource.

        :param record_arn: The RecordArn of the RegistryRecord resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_agentregistry as interfaces_agentregistry
            
            registry_record_reference = interfaces_agentregistry.RegistryRecordReference(
                record_arn="recordArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a3445081aedc579047d81a533016649cdd5d656e399878fd30150ac5e7267fef)
            check_type(argname="argument record_arn", value=record_arn, expected_type=type_hints["record_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_arn": record_arn,
        }

    @builtins.property
    def record_arn(self) -> builtins.str:
        '''The RecordArn of the RegistryRecord resource.'''
        result = self._values.get("record_arn")
        assert result is not None, "Required property 'record_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryRecordReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_agentregistry.RegistryReference",
    jsii_struct_bases=[],
    name_mapping={"registry_arn": "registryArn"},
)
class RegistryReference:
    def __init__(self, *, registry_arn: builtins.str) -> None:
        '''A reference to a Registry resource.

        :param registry_arn: The RegistryArn of the Registry resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_agentregistry as interfaces_agentregistry
            
            registry_reference = interfaces_agentregistry.RegistryReference(
                registry_arn="registryArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__214375e2d92be73347f277866be83e571afdde7a773016bc68e08310bd7f0d77)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_arn": registry_arn,
        }

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''The RegistryArn of the Registry resource.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IRegistryRecordRef",
    "IRegistryRef",
    "RegistryRecordReference",
    "RegistryReference",
]

publication.publish()

def _typecheckingstub__a3445081aedc579047d81a533016649cdd5d656e399878fd30150ac5e7267fef(
    *,
    record_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__214375e2d92be73347f277866be83e571afdde7a773016bc68e08310bd7f0d77(
    *,
    registry_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IRegistryRecordRef, IRegistryRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
