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
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.AgentSpaceReference",
    jsii_struct_bases=[],
    name_mapping={"agent_space_id": "agentSpaceId"},
)
class AgentSpaceReference:
    def __init__(self, *, agent_space_id: builtins.str) -> None:
        '''A reference to a AgentSpace resource.

        :param agent_space_id: The AgentSpaceId of the AgentSpace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            agent_space_reference = interfaces_securityagent.AgentSpaceReference(
                agent_space_id="agentSpaceId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__80dedf4a214ecd7806d810d851b3baa4ed59f4243fc9421cf67a698090d71a90)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
        }

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the AgentSpace resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentSpaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_id": "applicationId"},
)
class ApplicationReference:
    def __init__(self, *, application_id: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_id: The ApplicationId of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            application_reference = interfaces_securityagent.ApplicationReference(
                application_id="applicationId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a74a282e747b054b47e21cebc993013e9c4a786746342d0a3b2c5e0aa3202151)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Application resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.ArtifactReference",
    jsii_struct_bases=[],
    name_mapping={"artifact_arn": "artifactArn"},
)
class ArtifactReference:
    def __init__(self, *, artifact_arn: builtins.str) -> None:
        '''A reference to a Artifact resource.

        :param artifact_arn: The Arn of the Artifact resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            artifact_reference = interfaces_securityagent.ArtifactReference(
                artifact_arn="artifactArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c34b7a63eadccf538b02bdbf65be6c24340a2945bb9b8c604acbb87baeff8f02)
            check_type(argname="argument artifact_arn", value=artifact_arn, expected_type=type_hints["artifact_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "artifact_arn": artifact_arn,
        }

    @builtins.property
    def artifact_arn(self) -> builtins.str:
        '''The Arn of the Artifact resource.'''
        result = self._values.get("artifact_arn")
        assert result is not None, "Required property 'artifact_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArtifactReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.IAgentSpaceRef")
class IAgentSpaceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentSpace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "AgentSpaceReference":
        '''(experimental) A reference to a AgentSpace resource.

        :stability: experimental
        '''
        ...


class _IAgentSpaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentSpace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.IAgentSpaceRef"

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "AgentSpaceReference":
        '''(experimental) A reference to a AgentSpace resource.

        :stability: experimental
        '''
        return typing.cast("AgentSpaceReference", jsii.get(self, "agentSpaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentSpaceRef).__jsii_proxy_class__ = lambda : _IAgentSpaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.IApplicationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.IArtifactRef")
class IArtifactRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Artifact.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="artifactRef")
    def artifact_ref(self) -> "ArtifactReference":
        '''(experimental) A reference to a Artifact resource.

        :stability: experimental
        '''
        ...


class _IArtifactRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Artifact.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.IArtifactRef"

    @builtins.property
    @jsii.member(jsii_name="artifactRef")
    def artifact_ref(self) -> "ArtifactReference":
        '''(experimental) A reference to a Artifact resource.

        :stability: experimental
        '''
        return typing.cast("ArtifactReference", jsii.get(self, "artifactRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IArtifactRef).__jsii_proxy_class__ = lambda : _IArtifactRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.IPentestRef")
class IPentestRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Pentest.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pentestRef")
    def pentest_ref(self) -> "PentestReference":
        '''(experimental) A reference to a Pentest resource.

        :stability: experimental
        '''
        ...


class _IPentestRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Pentest.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.IPentestRef"

    @builtins.property
    @jsii.member(jsii_name="pentestRef")
    def pentest_ref(self) -> "PentestReference":
        '''(experimental) A reference to a Pentest resource.

        :stability: experimental
        '''
        return typing.cast("PentestReference", jsii.get(self, "pentestRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPentestRef).__jsii_proxy_class__ = lambda : _IPentestRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.ISecurityRequirementPackRef"
)
class ISecurityRequirementPackRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityRequirementPack.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityRequirementPackRef")
    def security_requirement_pack_ref(self) -> "SecurityRequirementPackReference":
        '''(experimental) A reference to a SecurityRequirementPack resource.

        :stability: experimental
        '''
        ...


class _ISecurityRequirementPackRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityRequirementPack.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.ISecurityRequirementPackRef"

    @builtins.property
    @jsii.member(jsii_name="securityRequirementPackRef")
    def security_requirement_pack_ref(self) -> "SecurityRequirementPackReference":
        '''(experimental) A reference to a SecurityRequirementPack resource.

        :stability: experimental
        '''
        return typing.cast("SecurityRequirementPackReference", jsii.get(self, "securityRequirementPackRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityRequirementPackRef).__jsii_proxy_class__ = lambda : _ISecurityRequirementPackRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.ITargetDomainRef")
class ITargetDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TargetDomain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="targetDomainRef")
    def target_domain_ref(self) -> "TargetDomainReference":
        '''(experimental) A reference to a TargetDomain resource.

        :stability: experimental
        '''
        ...


class _ITargetDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TargetDomain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.ITargetDomainRef"

    @builtins.property
    @jsii.member(jsii_name="targetDomainRef")
    def target_domain_ref(self) -> "TargetDomainReference":
        '''(experimental) A reference to a TargetDomain resource.

        :stability: experimental
        '''
        return typing.cast("TargetDomainReference", jsii.get(self, "targetDomainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITargetDomainRef).__jsii_proxy_class__ = lambda : _ITargetDomainRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.PentestReference",
    jsii_struct_bases=[],
    name_mapping={"agent_space_id": "agentSpaceId", "pentest_id": "pentestId"},
)
class PentestReference:
    def __init__(
        self,
        *,
        agent_space_id: builtins.str,
        pentest_id: builtins.str,
    ) -> None:
        '''A reference to a Pentest resource.

        :param agent_space_id: The AgentSpaceId of the Pentest resource.
        :param pentest_id: The PentestId of the Pentest resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            pentest_reference = interfaces_securityagent.PentestReference(
                agent_space_id="agentSpaceId",
                pentest_id="pentestId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1adadeed55a2da3dec371b1cd0d9d6711c5766263216b8243bedad0c33c21f40)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
            check_type(argname="argument pentest_id", value=pentest_id, expected_type=type_hints["pentest_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
            "pentest_id": pentest_id,
        }

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the Pentest resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pentest_id(self) -> builtins.str:
        '''The PentestId of the Pentest resource.'''
        result = self._values.get("pentest_id")
        assert result is not None, "Required property 'pentest_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PentestReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.SecurityRequirementPackReference",
    jsii_struct_bases=[],
    name_mapping={"pack_id": "packId"},
)
class SecurityRequirementPackReference:
    def __init__(self, *, pack_id: builtins.str) -> None:
        '''A reference to a SecurityRequirementPack resource.

        :param pack_id: The PackId of the SecurityRequirementPack resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            security_requirement_pack_reference = interfaces_securityagent.SecurityRequirementPackReference(
                pack_id="packId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5c1eb83b28b4b710f7e1d1651ff78ebcd729bea2ff5fe93e5070397d28d66351)
            check_type(argname="argument pack_id", value=pack_id, expected_type=type_hints["pack_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pack_id": pack_id,
        }

    @builtins.property
    def pack_id(self) -> builtins.str:
        '''The PackId of the SecurityRequirementPack resource.'''
        result = self._values.get("pack_id")
        assert result is not None, "Required property 'pack_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityRequirementPackReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.TargetDomainReference",
    jsii_struct_bases=[],
    name_mapping={"target_domain_id": "targetDomainId"},
)
class TargetDomainReference:
    def __init__(self, *, target_domain_id: builtins.str) -> None:
        '''A reference to a TargetDomain resource.

        :param target_domain_id: The TargetDomainId of the TargetDomain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            target_domain_reference = interfaces_securityagent.TargetDomainReference(
                target_domain_id="targetDomainId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a75929dd06e26264ee7207057716102e007a7dbc3560e3d13e615050563c4f66)
            check_type(argname="argument target_domain_id", value=target_domain_id, expected_type=type_hints["target_domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_domain_id": target_domain_id,
        }

    @builtins.property
    def target_domain_id(self) -> builtins.str:
        '''The TargetDomainId of the TargetDomain resource.'''
        result = self._values.get("target_domain_id")
        assert result is not None, "Required property 'target_domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetDomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AgentSpaceReference",
    "ApplicationReference",
    "ArtifactReference",
    "IAgentSpaceRef",
    "IApplicationRef",
    "IArtifactRef",
    "IPentestRef",
    "ISecurityRequirementPackRef",
    "ITargetDomainRef",
    "PentestReference",
    "SecurityRequirementPackReference",
    "TargetDomainReference",
]

publication.publish()

def _typecheckingstub__80dedf4a214ecd7806d810d851b3baa4ed59f4243fc9421cf67a698090d71a90(
    *,
    agent_space_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74a282e747b054b47e21cebc993013e9c4a786746342d0a3b2c5e0aa3202151(
    *,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c34b7a63eadccf538b02bdbf65be6c24340a2945bb9b8c604acbb87baeff8f02(
    *,
    artifact_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1adadeed55a2da3dec371b1cd0d9d6711c5766263216b8243bedad0c33c21f40(
    *,
    agent_space_id: builtins.str,
    pentest_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c1eb83b28b4b710f7e1d1651ff78ebcd729bea2ff5fe93e5070397d28d66351(
    *,
    pack_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a75929dd06e26264ee7207057716102e007a7dbc3560e3d13e615050563c4f66(
    *,
    target_domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgentSpaceRef, IApplicationRef, IArtifactRef, IPentestRef, ISecurityRequirementPackRef, ITargetDomainRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
