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
    jsii_type="aws-cdk-lib.interfaces.aws_workspaces.ConnectionAliasReference",
    jsii_struct_bases=[],
    name_mapping={"alias_id": "aliasId"},
)
class ConnectionAliasReference:
    def __init__(self, *, alias_id: builtins.str) -> None:
        '''A reference to a ConnectionAlias resource.

        :param alias_id: The AliasId of the ConnectionAlias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspaces as interfaces_workspaces
            
            connection_alias_reference = interfaces_workspaces.ConnectionAliasReference(
                alias_id="aliasId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e994ed6c2b81487e9ad88c3c7d73b4bf2d26702b4117ef662684dde75bedc571)
            check_type(argname="argument alias_id", value=alias_id, expected_type=type_hints["alias_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_id": alias_id,
        }

    @builtins.property
    def alias_id(self) -> builtins.str:
        '''The AliasId of the ConnectionAlias resource.'''
        result = self._values.get("alias_id")
        assert result is not None, "Required property 'alias_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionAliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspaces.IConnectionAliasRef")
class IConnectionAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectionAlias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionAliasRef")
    def connection_alias_ref(self) -> "ConnectionAliasReference":
        '''(experimental) A reference to a ConnectionAlias resource.

        :stability: experimental
        '''
        ...


class _IConnectionAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectionAlias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspaces.IConnectionAliasRef"

    @builtins.property
    @jsii.member(jsii_name="connectionAliasRef")
    def connection_alias_ref(self) -> "ConnectionAliasReference":
        '''(experimental) A reference to a ConnectionAlias resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionAliasReference", jsii.get(self, "connectionAliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionAliasRef).__jsii_proxy_class__ = lambda : _IConnectionAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspaces.IWorkspaceIpGroupRef")
class IWorkspaceIpGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WorkspaceIpGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workspaceIpGroupRef")
    def workspace_ip_group_ref(self) -> "WorkspaceIpGroupReference":
        '''(experimental) A reference to a WorkspaceIpGroup resource.

        :stability: experimental
        '''
        ...


class _IWorkspaceIpGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WorkspaceIpGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspaces.IWorkspaceIpGroupRef"

    @builtins.property
    @jsii.member(jsii_name="workspaceIpGroupRef")
    def workspace_ip_group_ref(self) -> "WorkspaceIpGroupReference":
        '''(experimental) A reference to a WorkspaceIpGroup resource.

        :stability: experimental
        '''
        return typing.cast("WorkspaceIpGroupReference", jsii.get(self, "workspaceIpGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkspaceIpGroupRef).__jsii_proxy_class__ = lambda : _IWorkspaceIpGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspaces.IWorkspaceRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspaces.IWorkspaceRef"

    @builtins.property
    @jsii.member(jsii_name="workspaceRef")
    def workspace_ref(self) -> "WorkspaceReference":
        '''(experimental) A reference to a Workspace resource.

        :stability: experimental
        '''
        return typing.cast("WorkspaceReference", jsii.get(self, "workspaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkspaceRef).__jsii_proxy_class__ = lambda : _IWorkspaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspaces.IWorkspacesPoolRef")
class IWorkspacesPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WorkspacesPool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workspacesPoolRef")
    def workspaces_pool_ref(self) -> "WorkspacesPoolReference":
        '''(experimental) A reference to a WorkspacesPool resource.

        :stability: experimental
        '''
        ...


class _IWorkspacesPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WorkspacesPool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspaces.IWorkspacesPoolRef"

    @builtins.property
    @jsii.member(jsii_name="workspacesPoolRef")
    def workspaces_pool_ref(self) -> "WorkspacesPoolReference":
        '''(experimental) A reference to a WorkspacesPool resource.

        :stability: experimental
        '''
        return typing.cast("WorkspacesPoolReference", jsii.get(self, "workspacesPoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkspacesPoolRef).__jsii_proxy_class__ = lambda : _IWorkspacesPoolRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspaces.WorkspaceIpGroupReference",
    jsii_struct_bases=[],
    name_mapping={"workspace_ip_group_arn": "workspaceIpGroupArn"},
)
class WorkspaceIpGroupReference:
    def __init__(self, *, workspace_ip_group_arn: builtins.str) -> None:
        '''A reference to a WorkspaceIpGroup resource.

        :param workspace_ip_group_arn: The Arn of the WorkspaceIpGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspaces as interfaces_workspaces
            
            workspace_ip_group_reference = interfaces_workspaces.WorkspaceIpGroupReference(
                workspace_ip_group_arn="workspaceIpGroupArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c6f44c974dc4c8d0d5c8d54baeb0d7f8266a42cf4180d28501a4914bbce97cb9)
            check_type(argname="argument workspace_ip_group_arn", value=workspace_ip_group_arn, expected_type=type_hints["workspace_ip_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workspace_ip_group_arn": workspace_ip_group_arn,
        }

    @builtins.property
    def workspace_ip_group_arn(self) -> builtins.str:
        '''The Arn of the WorkspaceIpGroup resource.'''
        result = self._values.get("workspace_ip_group_arn")
        assert result is not None, "Required property 'workspace_ip_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceIpGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspaces.WorkspaceReference",
    jsii_struct_bases=[],
    name_mapping={"workspace_id": "workspaceId"},
)
class WorkspaceReference:
    def __init__(self, *, workspace_id: builtins.str) -> None:
        '''A reference to a Workspace resource.

        :param workspace_id: The WorkspaceId of the Workspace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspaces as interfaces_workspaces
            
            workspace_reference = interfaces_workspaces.WorkspaceReference(
                workspace_id="workspaceId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d8a0b9af3fbd40b7ccd2d3217fbaf36417408e9e3d07780d4dbb4f264586cbc4)
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workspace_id": workspace_id,
        }

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''The WorkspaceId of the Workspace resource.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspaces.WorkspacesPoolReference",
    jsii_struct_bases=[],
    name_mapping={"pool_arn": "poolArn", "pool_id": "poolId"},
)
class WorkspacesPoolReference:
    def __init__(self, *, pool_arn: builtins.str, pool_id: builtins.str) -> None:
        '''A reference to a WorkspacesPool resource.

        :param pool_arn: The ARN of the WorkspacesPool resource.
        :param pool_id: The PoolId of the WorkspacesPool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspaces as interfaces_workspaces
            
            workspaces_pool_reference = interfaces_workspaces.WorkspacesPoolReference(
                pool_arn="poolArn",
                pool_id="poolId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__13c3123b4ec0e20a04c6106b766191404e3c10e79c6c19f9ea979723772ac51b)
            check_type(argname="argument pool_arn", value=pool_arn, expected_type=type_hints["pool_arn"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pool_arn": pool_arn,
            "pool_id": pool_id,
        }

    @builtins.property
    def pool_arn(self) -> builtins.str:
        '''The ARN of the WorkspacesPool resource.'''
        result = self._values.get("pool_arn")
        assert result is not None, "Required property 'pool_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pool_id(self) -> builtins.str:
        '''The PoolId of the WorkspacesPool resource.'''
        result = self._values.get("pool_id")
        assert result is not None, "Required property 'pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspacesPoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectionAliasReference",
    "IConnectionAliasRef",
    "IWorkspaceIpGroupRef",
    "IWorkspaceRef",
    "IWorkspacesPoolRef",
    "WorkspaceIpGroupReference",
    "WorkspaceReference",
    "WorkspacesPoolReference",
]

publication.publish()

def _typecheckingstub__e994ed6c2b81487e9ad88c3c7d73b4bf2d26702b4117ef662684dde75bedc571(
    *,
    alias_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f44c974dc4c8d0d5c8d54baeb0d7f8266a42cf4180d28501a4914bbce97cb9(
    *,
    workspace_ip_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8a0b9af3fbd40b7ccd2d3217fbaf36417408e9e3d07780d4dbb4f264586cbc4(
    *,
    workspace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13c3123b4ec0e20a04c6106b766191404e3c10e79c6c19f9ea979723772ac51b(
    *,
    pool_arn: builtins.str,
    pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectionAliasRef, IWorkspaceIpGroupRef, IWorkspaceRef, IWorkspacesPoolRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
