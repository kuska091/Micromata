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

    import aws_cdk as _aws_cdk_0cae9daa
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _constructs_77d1e7e8 = _LazyImport("constructs")


class RepositoryAutoDeleteImages(
    _aws_cdk_0cae9daa.Mixin,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.mixins.RepositoryAutoDeleteImages",
):
    '''ECR-specific Mixin to force-delete all images from a repository when the repository is removed from the stack or when the stack is deleted.

    Sets the ``emptyOnDelete`` property on the repository.

    :exampleMetadata: infused

    Example::

        ecr.CfnRepository(self, "Repo").with(ecr.mixins.RepositoryAutoDeleteImages())
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="applyTo")
    def apply_to(self, construct: "_constructs_77d1e7e8.IConstruct") -> None:
        '''Applies the mixin functionality to the target construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__22e2455beb109b896cd9727519758382be52ce357885d67e10f2c7fd9b7900dd)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(None, jsii.invoke(self, "applyTo", [construct]))

    @jsii.member(jsii_name="supports")
    def supports(self, construct: "_constructs_77d1e7e8.IConstruct") -> builtins.bool:
        '''Determines whether this mixin can be applied to the given construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7b56051b831cc1c1e9c65622167285b02ef56c08a6c2f46b6cd3a0fa9a223d70)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "supports", [construct]))


__all__ = [
    "RepositoryAutoDeleteImages",
]

publication.publish()

def _typecheckingstub__22e2455beb109b896cd9727519758382be52ce357885d67e10f2c7fd9b7900dd(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b56051b831cc1c1e9c65622167285b02ef56c08a6c2f46b6cd3a0fa9a223d70(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass
