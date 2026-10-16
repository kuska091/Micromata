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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_storagegateway.ITapePoolRef")
class ITapePoolRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TapePool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tapePoolRef")
    def tape_pool_ref(self) -> "TapePoolReference":
        '''(experimental) A reference to a TapePool resource.

        :stability: experimental
        '''
        ...


class _ITapePoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TapePool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_storagegateway.ITapePoolRef"

    @builtins.property
    @jsii.member(jsii_name="tapePoolRef")
    def tape_pool_ref(self) -> "TapePoolReference":
        '''(experimental) A reference to a TapePool resource.

        :stability: experimental
        '''
        return typing.cast("TapePoolReference", jsii.get(self, "tapePoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITapePoolRef).__jsii_proxy_class__ = lambda : _ITapePoolRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_storagegateway.ITapeRef")
class ITapeRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Tape.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tapeRef")
    def tape_ref(self) -> "TapeReference":
        '''(experimental) A reference to a Tape resource.

        :stability: experimental
        '''
        ...


class _ITapeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Tape.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_storagegateway.ITapeRef"

    @builtins.property
    @jsii.member(jsii_name="tapeRef")
    def tape_ref(self) -> "TapeReference":
        '''(experimental) A reference to a Tape resource.

        :stability: experimental
        '''
        return typing.cast("TapeReference", jsii.get(self, "tapeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITapeRef).__jsii_proxy_class__ = lambda : _ITapeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_storagegateway.IVolumeRef")
class IVolumeRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        ...


class _IVolumeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_storagegateway.IVolumeRef"

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        return typing.cast("VolumeReference", jsii.get(self, "volumeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVolumeRef).__jsii_proxy_class__ = lambda : _IVolumeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_storagegateway.TapePoolReference",
    jsii_struct_bases=[],
    name_mapping={"pool_arn": "poolArn", "pool_id": "poolId"},
)
class TapePoolReference:
    def __init__(self, *, pool_arn: builtins.str, pool_id: builtins.str) -> None:
        '''A reference to a TapePool resource.

        :param pool_arn: The PoolARN of the TapePool resource.
        :param pool_id: The PoolId of the TapePool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_storagegateway as interfaces_storagegateway
            
            tape_pool_reference = interfaces_storagegateway.TapePoolReference(
                pool_arn="poolArn",
                pool_id="poolId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__931a079c099cafcf7c3658f645d8e30f357c406d91c831ab4fc86f2ae8c9fdce)
            check_type(argname="argument pool_arn", value=pool_arn, expected_type=type_hints["pool_arn"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pool_arn": pool_arn,
            "pool_id": pool_id,
        }

    @builtins.property
    def pool_arn(self) -> builtins.str:
        '''The PoolARN of the TapePool resource.'''
        result = self._values.get("pool_arn")
        assert result is not None, "Required property 'pool_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pool_id(self) -> builtins.str:
        '''The PoolId of the TapePool resource.'''
        result = self._values.get("pool_id")
        assert result is not None, "Required property 'pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TapePoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_storagegateway.TapeReference",
    jsii_struct_bases=[],
    name_mapping={"tape_arn": "tapeArn"},
)
class TapeReference:
    def __init__(self, *, tape_arn: builtins.str) -> None:
        '''A reference to a Tape resource.

        :param tape_arn: The TapeARN of the Tape resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_storagegateway as interfaces_storagegateway
            
            tape_reference = interfaces_storagegateway.TapeReference(
                tape_arn="tapeArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c9f0711496041eef9374207d243de9b8c5298ca999dd19031e3b54759c5c4306)
            check_type(argname="argument tape_arn", value=tape_arn, expected_type=type_hints["tape_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tape_arn": tape_arn,
        }

    @builtins.property
    def tape_arn(self) -> builtins.str:
        '''The TapeARN of the Tape resource.'''
        result = self._values.get("tape_arn")
        assert result is not None, "Required property 'tape_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TapeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_storagegateway.VolumeReference",
    jsii_struct_bases=[],
    name_mapping={"volume_arn": "volumeArn"},
)
class VolumeReference:
    def __init__(self, *, volume_arn: builtins.str) -> None:
        '''A reference to a Volume resource.

        :param volume_arn: The VolumeARN of the Volume resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_storagegateway as interfaces_storagegateway
            
            volume_reference = interfaces_storagegateway.VolumeReference(
                volume_arn="volumeArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fa56affb5b28498dfa94bfc6e9e66be39cd6b3647aaa44b547b63aa80f8b6918)
            check_type(argname="argument volume_arn", value=volume_arn, expected_type=type_hints["volume_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_arn": volume_arn,
        }

    @builtins.property
    def volume_arn(self) -> builtins.str:
        '''The VolumeARN of the Volume resource.'''
        result = self._values.get("volume_arn")
        assert result is not None, "Required property 'volume_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ITapePoolRef",
    "ITapeRef",
    "IVolumeRef",
    "TapePoolReference",
    "TapeReference",
    "VolumeReference",
]

publication.publish()

def _typecheckingstub__931a079c099cafcf7c3658f645d8e30f357c406d91c831ab4fc86f2ae8c9fdce(
    *,
    pool_arn: builtins.str,
    pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9f0711496041eef9374207d243de9b8c5298ca999dd19031e3b54759c5c4306(
    *,
    tape_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa56affb5b28498dfa94bfc6e9e66be39cd6b3647aaa44b547b63aa80f8b6918(
    *,
    volume_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ITapePoolRef, ITapeRef, IVolumeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
