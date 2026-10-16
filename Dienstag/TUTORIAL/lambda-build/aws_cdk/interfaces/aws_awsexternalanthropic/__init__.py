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
    jsii_type="aws-cdk-lib.interfaces.aws_awsexternalanthropic.IWorkspaceRef"
)
class IWorkspaceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workspace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workspaceRef")
    def workspace_ref(self) -> "WorkspaceReference":
        '''(experimental) A reference to a Workspace resource.

        :stability: experimental
        '''
        ...


class _IWorkspaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workspace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_awsexternalanthropic.IWorkspaceRef"

    @builtins.property
    @jsii.member(jsii_name="workspaceRef")
    def workspace_ref(self) -> "WorkspaceReference":
        '''(experimental) A reference to a Workspace resource.

        :stability: experimental
        '''
        return typing.cast("WorkspaceReference", jsii.get(self, "workspaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkspaceRef).__jsii_proxy_class__ = lambda : _IWorkspaceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_awsexternalanthropic.WorkspaceReference",
    jsii_struct_bases=[],
    name_mapping={"workspace_arn": "workspaceArn"},
)
class WorkspaceReference:
    def __init__(self, *, workspace_arn: builtins.str) -> None:
        '''A reference to a Workspace resource.

        :param workspace_arn: The Arn of the Workspace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_awsexternalanthropic as interfaces_awsexternalanthropic
            
            workspace_reference = interfaces_awsexternalanthropic.WorkspaceReference(
                workspace_arn="workspaceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__563b1f3ab4fc18eecbd72ca1e4cfacb1866f28b8ec7e22b657a8fca201ced5d6)
            check_type(argname="argument workspace_arn", value=workspace_arn, expected_type=type_hints["workspace_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workspace_arn": workspace_arn,
        }

    @builtins.property
    def workspace_arn(self) -> builtins.str:
        '''The Arn of the Workspace resource.'''
        result = self._values.get("workspace_arn")
        assert result is not None, "Required property 'workspace_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IWorkspaceRef",
    "WorkspaceReference",
]

publication.publish()

def _typecheckingstub__563b1f3ab4fc18eecbd72ca1e4cfacb1866f28b8ec7e22b657a8fca201ced5d6(
    *,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IWorkspaceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
