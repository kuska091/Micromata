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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codecommit.IRepositoryRef")
class IRepositoryRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Repository.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="repositoryRef")
    def repository_ref(self) -> "RepositoryReference":
        '''(experimental) A reference to a Repository resource.

        :stability: experimental
        '''
        ...


class _IRepositoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Repository.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codecommit.IRepositoryRef"

    @builtins.property
    @jsii.member(jsii_name="repositoryRef")
    def repository_ref(self) -> "RepositoryReference":
        '''(experimental) A reference to a Repository resource.

        :stability: experimental
        '''
        return typing.cast("RepositoryReference", jsii.get(self, "repositoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepositoryRef).__jsii_proxy_class__ = lambda : _IRepositoryRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codecommit.RepositoryReference",
    jsii_struct_bases=[],
    name_mapping={"repository_arn": "repositoryArn", "repository_id": "repositoryId"},
)
class RepositoryReference:
    def __init__(
        self,
        *,
        repository_arn: builtins.str,
        repository_id: builtins.str,
    ) -> None:
        '''A reference to a Repository resource.

        :param repository_arn: The ARN of the Repository resource.
        :param repository_id: The RepositoryId of the Repository resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codecommit as interfaces_codecommit
            
            repository_reference = interfaces_codecommit.RepositoryReference(
                repository_arn="repositoryArn",
                repository_id="repositoryId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__64e205c0c490b37d5c8c103f7a3f502306c44566ca81fca264b568b26537322f)
            check_type(argname="argument repository_arn", value=repository_arn, expected_type=type_hints["repository_arn"])
            check_type(argname="argument repository_id", value=repository_id, expected_type=type_hints["repository_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_arn": repository_arn,
            "repository_id": repository_id,
        }

    @builtins.property
    def repository_arn(self) -> builtins.str:
        '''The ARN of the Repository resource.'''
        result = self._values.get("repository_arn")
        assert result is not None, "Required property 'repository_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_id(self) -> builtins.str:
        '''The RepositoryId of the Repository resource.'''
        result = self._values.get("repository_id")
        assert result is not None, "Required property 'repository_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IRepositoryRef",
    "RepositoryReference",
]

publication.publish()

def _typecheckingstub__64e205c0c490b37d5c8c103f7a3f502306c44566ca81fca264b568b26537322f(
    *,
    repository_arn: builtins.str,
    repository_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IRepositoryRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
