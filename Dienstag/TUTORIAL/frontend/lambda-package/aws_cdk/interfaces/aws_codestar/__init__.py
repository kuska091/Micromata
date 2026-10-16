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
    jsii_type="aws-cdk-lib.interfaces.aws_codestar.GitHubRepositoryReference",
    jsii_struct_bases=[],
    name_mapping={"git_hub_repository_id": "gitHubRepositoryId"},
)
class GitHubRepositoryReference:
    def __init__(self, *, git_hub_repository_id: builtins.str) -> None:
        '''A reference to a GitHubRepository resource.

        :param git_hub_repository_id: The Id of the GitHubRepository resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codestar as interfaces_codestar
            
            git_hub_repository_reference = interfaces_codestar.GitHubRepositoryReference(
                git_hub_repository_id="gitHubRepositoryId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__af37bc4bdc7eecd04a055cafb512aea3784a41fb9ead4fae7c4443b9a78d0aa0)
            check_type(argname="argument git_hub_repository_id", value=git_hub_repository_id, expected_type=type_hints["git_hub_repository_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "git_hub_repository_id": git_hub_repository_id,
        }

    @builtins.property
    def git_hub_repository_id(self) -> builtins.str:
        '''The Id of the GitHubRepository resource.'''
        result = self._values.get("git_hub_repository_id")
        assert result is not None, "Required property 'git_hub_repository_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitHubRepositoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codestar.IGitHubRepositoryRef")
class IGitHubRepositoryRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GitHubRepository.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gitHubRepositoryRef")
    def git_hub_repository_ref(self) -> "GitHubRepositoryReference":
        '''(experimental) A reference to a GitHubRepository resource.

        :stability: experimental
        '''
        ...


class _IGitHubRepositoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GitHubRepository.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codestar.IGitHubRepositoryRef"

    @builtins.property
    @jsii.member(jsii_name="gitHubRepositoryRef")
    def git_hub_repository_ref(self) -> "GitHubRepositoryReference":
        '''(experimental) A reference to a GitHubRepository resource.

        :stability: experimental
        '''
        return typing.cast("GitHubRepositoryReference", jsii.get(self, "gitHubRepositoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGitHubRepositoryRef).__jsii_proxy_class__ = lambda : _IGitHubRepositoryRefProxy


__all__ = [
    "GitHubRepositoryReference",
    "IGitHubRepositoryRef",
]

publication.publish()

def _typecheckingstub__af37bc4bdc7eecd04a055cafb512aea3784a41fb9ead4fae7c4443b9a78d0aa0(
    *,
    git_hub_repository_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGitHubRepositoryRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
