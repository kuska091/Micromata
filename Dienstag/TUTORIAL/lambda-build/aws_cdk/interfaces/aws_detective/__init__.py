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
    jsii_type="aws-cdk-lib.interfaces.aws_detective.GraphReference",
    jsii_struct_bases=[],
    name_mapping={"graph_arn": "graphArn"},
)
class GraphReference:
    def __init__(self, *, graph_arn: builtins.str) -> None:
        '''A reference to a Graph resource.

        :param graph_arn: The Arn of the Graph resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_detective as interfaces_detective
            
            graph_reference = interfaces_detective.GraphReference(
                graph_arn="graphArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__db38b928989b3e4a0c3a542a01fa8b7a9dd761c3bf94cf38014f63785f66b5e2)
            check_type(argname="argument graph_arn", value=graph_arn, expected_type=type_hints["graph_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_arn": graph_arn,
        }

    @builtins.property
    def graph_arn(self) -> builtins.str:
        '''The Arn of the Graph resource.'''
        result = self._values.get("graph_arn")
        assert result is not None, "Required property 'graph_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_detective.IGraphRef")
class IGraphRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Graph.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="graphRef")
    def graph_ref(self) -> "GraphReference":
        '''(experimental) A reference to a Graph resource.

        :stability: experimental
        '''
        ...


class _IGraphRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Graph.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_detective.IGraphRef"

    @builtins.property
    @jsii.member(jsii_name="graphRef")
    def graph_ref(self) -> "GraphReference":
        '''(experimental) A reference to a Graph resource.

        :stability: experimental
        '''
        return typing.cast("GraphReference", jsii.get(self, "graphRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphRef).__jsii_proxy_class__ = lambda : _IGraphRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_detective.IMemberInvitationRef")
class IMemberInvitationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MemberInvitation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="memberInvitationRef")
    def member_invitation_ref(self) -> "MemberInvitationReference":
        '''(experimental) A reference to a MemberInvitation resource.

        :stability: experimental
        '''
        ...


class _IMemberInvitationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MemberInvitation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_detective.IMemberInvitationRef"

    @builtins.property
    @jsii.member(jsii_name="memberInvitationRef")
    def member_invitation_ref(self) -> "MemberInvitationReference":
        '''(experimental) A reference to a MemberInvitation resource.

        :stability: experimental
        '''
        return typing.cast("MemberInvitationReference", jsii.get(self, "memberInvitationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMemberInvitationRef).__jsii_proxy_class__ = lambda : _IMemberInvitationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_detective.IOrganizationAdminRef")
class IOrganizationAdminRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationAdmin.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationAdminRef")
    def organization_admin_ref(self) -> "OrganizationAdminReference":
        '''(experimental) A reference to a OrganizationAdmin resource.

        :stability: experimental
        '''
        ...


class _IOrganizationAdminRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationAdmin.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_detective.IOrganizationAdminRef"

    @builtins.property
    @jsii.member(jsii_name="organizationAdminRef")
    def organization_admin_ref(self) -> "OrganizationAdminReference":
        '''(experimental) A reference to a OrganizationAdmin resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationAdminReference", jsii.get(self, "organizationAdminRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationAdminRef).__jsii_proxy_class__ = lambda : _IOrganizationAdminRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_detective.MemberInvitationReference",
    jsii_struct_bases=[],
    name_mapping={"graph_arn": "graphArn", "member_id": "memberId"},
)
class MemberInvitationReference:
    def __init__(self, *, graph_arn: builtins.str, member_id: builtins.str) -> None:
        '''A reference to a MemberInvitation resource.

        :param graph_arn: The GraphArn of the MemberInvitation resource.
        :param member_id: The MemberId of the MemberInvitation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_detective as interfaces_detective
            
            member_invitation_reference = interfaces_detective.MemberInvitationReference(
                graph_arn="graphArn",
                member_id="memberId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8c46cb8217d3fb9ee2b431fc4a287dd07bbf9b77979b9dbfa452e9bc5e62c6f1)
            check_type(argname="argument graph_arn", value=graph_arn, expected_type=type_hints["graph_arn"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_arn": graph_arn,
            "member_id": member_id,
        }

    @builtins.property
    def graph_arn(self) -> builtins.str:
        '''The GraphArn of the MemberInvitation resource.'''
        result = self._values.get("graph_arn")
        assert result is not None, "Required property 'graph_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(self) -> builtins.str:
        '''The MemberId of the MemberInvitation resource.'''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MemberInvitationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_detective.OrganizationAdminReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class OrganizationAdminReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a OrganizationAdmin resource.

        :param account_id: The AccountId of the OrganizationAdmin resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_detective as interfaces_detective
            
            organization_admin_reference = interfaces_detective.OrganizationAdminReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4e88be3eaba4aa6bd6c59dcc5238633385dc3a958c92bf859a07ec2018290b09)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the OrganizationAdmin resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationAdminReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GraphReference",
    "IGraphRef",
    "IMemberInvitationRef",
    "IOrganizationAdminRef",
    "MemberInvitationReference",
    "OrganizationAdminReference",
]

publication.publish()

def _typecheckingstub__db38b928989b3e4a0c3a542a01fa8b7a9dd761c3bf94cf38014f63785f66b5e2(
    *,
    graph_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c46cb8217d3fb9ee2b431fc4a287dd07bbf9b77979b9dbfa452e9bc5e62c6f1(
    *,
    graph_arn: builtins.str,
    member_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e88be3eaba4aa6bd6c59dcc5238633385dc3a958c92bf859a07ec2018290b09(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGraphRef, IMemberInvitationRef, IOrganizationAdminRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
