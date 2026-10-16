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
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.AgentContextReference",
    jsii_struct_bases=[],
    name_mapping={"agent_context_arn": "agentContextArn"},
)
class AgentContextReference:
    def __init__(self, *, agent_context_arn: builtins.str) -> None:
        '''A reference to a AgentContext resource.

        :param agent_context_arn: The Arn of the AgentContext resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wellarchitected as interfaces_wellarchitected
            
            agent_context_reference = interfaces_wellarchitected.AgentContextReference(
                agent_context_arn="agentContextArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2005652a4c7aeb4c9c766bde2753cbd872f80046ba3343f2baa92463aa142d95)
            check_type(argname="argument agent_context_arn", value=agent_context_arn, expected_type=type_hints["agent_context_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_context_arn": agent_context_arn,
        }

    @builtins.property
    def agent_context_arn(self) -> builtins.str:
        '''The Arn of the AgentContext resource.'''
        result = self._values.get("agent_context_arn")
        assert result is not None, "Required property 'agent_context_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentContextReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.AgentGoalReference",
    jsii_struct_bases=[],
    name_mapping={"agent_goal_arn": "agentGoalArn"},
)
class AgentGoalReference:
    def __init__(self, *, agent_goal_arn: builtins.str) -> None:
        '''A reference to a AgentGoal resource.

        :param agent_goal_arn: The Arn of the AgentGoal resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wellarchitected as interfaces_wellarchitected
            
            agent_goal_reference = interfaces_wellarchitected.AgentGoalReference(
                agent_goal_arn="agentGoalArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dc600cefd3fcbdb5270939e69bf2b3fcdb04992bfab764cbc3cd78d5f3ced5e0)
            check_type(argname="argument agent_goal_arn", value=agent_goal_arn, expected_type=type_hints["agent_goal_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_goal_arn": agent_goal_arn,
        }

    @builtins.property
    def agent_goal_arn(self) -> builtins.str:
        '''The Arn of the AgentGoal resource.'''
        result = self._values.get("agent_goal_arn")
        assert result is not None, "Required property 'agent_goal_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentGoalReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.AgentProfileReference",
    jsii_struct_bases=[],
    name_mapping={"agent_profile_arn": "agentProfileArn"},
)
class AgentProfileReference:
    def __init__(self, *, agent_profile_arn: builtins.str) -> None:
        '''A reference to a AgentProfile resource.

        :param agent_profile_arn: The Arn of the AgentProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wellarchitected as interfaces_wellarchitected
            
            agent_profile_reference = interfaces_wellarchitected.AgentProfileReference(
                agent_profile_arn="agentProfileArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f1b789c8a6e2850f509bdd44d1e5975fb9dcfa99953874837034eca4dd50d22a)
            check_type(argname="argument agent_profile_arn", value=agent_profile_arn, expected_type=type_hints["agent_profile_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_profile_arn": agent_profile_arn,
        }

    @builtins.property
    def agent_profile_arn(self) -> builtins.str:
        '''The Arn of the AgentProfile resource.'''
        result = self._values.get("agent_profile_arn")
        assert result is not None, "Required property 'agent_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.IAgentContextRef"
)
class IAgentContextRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentContext.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentContextRef")
    def agent_context_ref(self) -> "AgentContextReference":
        '''(experimental) A reference to a AgentContext resource.

        :stability: experimental
        '''
        ...


class _IAgentContextRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentContext.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wellarchitected.IAgentContextRef"

    @builtins.property
    @jsii.member(jsii_name="agentContextRef")
    def agent_context_ref(self) -> "AgentContextReference":
        '''(experimental) A reference to a AgentContext resource.

        :stability: experimental
        '''
        return typing.cast("AgentContextReference", jsii.get(self, "agentContextRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentContextRef).__jsii_proxy_class__ = lambda : _IAgentContextRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.IAgentGoalRef")
class IAgentGoalRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentGoal.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentGoalRef")
    def agent_goal_ref(self) -> "AgentGoalReference":
        '''(experimental) A reference to a AgentGoal resource.

        :stability: experimental
        '''
        ...


class _IAgentGoalRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentGoal.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wellarchitected.IAgentGoalRef"

    @builtins.property
    @jsii.member(jsii_name="agentGoalRef")
    def agent_goal_ref(self) -> "AgentGoalReference":
        '''(experimental) A reference to a AgentGoal resource.

        :stability: experimental
        '''
        return typing.cast("AgentGoalReference", jsii.get(self, "agentGoalRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentGoalRef).__jsii_proxy_class__ = lambda : _IAgentGoalRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.IAgentProfileRef"
)
class IAgentProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentProfileRef")
    def agent_profile_ref(self) -> "AgentProfileReference":
        '''(experimental) A reference to a AgentProfile resource.

        :stability: experimental
        '''
        ...


class _IAgentProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wellarchitected.IAgentProfileRef"

    @builtins.property
    @jsii.member(jsii_name="agentProfileRef")
    def agent_profile_ref(self) -> "AgentProfileReference":
        '''(experimental) A reference to a AgentProfile resource.

        :stability: experimental
        '''
        return typing.cast("AgentProfileReference", jsii.get(self, "agentProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentProfileRef).__jsii_proxy_class__ = lambda : _IAgentProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.ILensRef")
class ILensRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Lens.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="lensRef")
    def lens_ref(self) -> "LensReference":
        '''(experimental) A reference to a Lens resource.

        :stability: experimental
        '''
        ...


class _ILensRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Lens.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wellarchitected.ILensRef"

    @builtins.property
    @jsii.member(jsii_name="lensRef")
    def lens_ref(self) -> "LensReference":
        '''(experimental) A reference to a Lens resource.

        :stability: experimental
        '''
        return typing.cast("LensReference", jsii.get(self, "lensRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILensRef).__jsii_proxy_class__ = lambda : _ILensRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.IProfileRef")
class IProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Profile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        ...


class _IProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Profile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wellarchitected.IProfileRef"

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        return typing.cast("ProfileReference", jsii.get(self, "profileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfileRef).__jsii_proxy_class__ = lambda : _IProfileRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.IReviewTemplateRef"
)
class IReviewTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReviewTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="reviewTemplateRef")
    def review_template_ref(self) -> "ReviewTemplateReference":
        '''(experimental) A reference to a ReviewTemplate resource.

        :stability: experimental
        '''
        ...


class _IReviewTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReviewTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wellarchitected.IReviewTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="reviewTemplateRef")
    def review_template_ref(self) -> "ReviewTemplateReference":
        '''(experimental) A reference to a ReviewTemplate resource.

        :stability: experimental
        '''
        return typing.cast("ReviewTemplateReference", jsii.get(self, "reviewTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReviewTemplateRef).__jsii_proxy_class__ = lambda : _IReviewTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.IWorkloadRef")
class IWorkloadRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workload.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workloadRef")
    def workload_ref(self) -> "WorkloadReference":
        '''(experimental) A reference to a Workload resource.

        :stability: experimental
        '''
        ...


class _IWorkloadRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workload.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wellarchitected.IWorkloadRef"

    @builtins.property
    @jsii.member(jsii_name="workloadRef")
    def workload_ref(self) -> "WorkloadReference":
        '''(experimental) A reference to a Workload resource.

        :stability: experimental
        '''
        return typing.cast("WorkloadReference", jsii.get(self, "workloadRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkloadRef).__jsii_proxy_class__ = lambda : _IWorkloadRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.LensReference",
    jsii_struct_bases=[],
    name_mapping={"lens_arn": "lensArn"},
)
class LensReference:
    def __init__(self, *, lens_arn: builtins.str) -> None:
        '''A reference to a Lens resource.

        :param lens_arn: The LensArn of the Lens resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wellarchitected as interfaces_wellarchitected
            
            lens_reference = interfaces_wellarchitected.LensReference(
                lens_arn="lensArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f32344e8e195ba084ce4fcf47286bb12830dd7f6eb5a3d62943b345edff1b52f)
            check_type(argname="argument lens_arn", value=lens_arn, expected_type=type_hints["lens_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lens_arn": lens_arn,
        }

    @builtins.property
    def lens_arn(self) -> builtins.str:
        '''The LensArn of the Lens resource.'''
        result = self._values.get("lens_arn")
        assert result is not None, "Required property 'lens_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LensReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.ProfileReference",
    jsii_struct_bases=[],
    name_mapping={"profile_arn": "profileArn"},
)
class ProfileReference:
    def __init__(self, *, profile_arn: builtins.str) -> None:
        '''A reference to a Profile resource.

        :param profile_arn: The ProfileArn of the Profile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wellarchitected as interfaces_wellarchitected
            
            profile_reference = interfaces_wellarchitected.ProfileReference(
                profile_arn="profileArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8ae04271fcde99607a1aceb6f7563e89a6fe87895a913e2d8e18fa75b01e68eb)
            check_type(argname="argument profile_arn", value=profile_arn, expected_type=type_hints["profile_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_arn": profile_arn,
        }

    @builtins.property
    def profile_arn(self) -> builtins.str:
        '''The ProfileArn of the Profile resource.'''
        result = self._values.get("profile_arn")
        assert result is not None, "Required property 'profile_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.ReviewTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"template_arn": "templateArn"},
)
class ReviewTemplateReference:
    def __init__(self, *, template_arn: builtins.str) -> None:
        '''A reference to a ReviewTemplate resource.

        :param template_arn: The TemplateArn of the ReviewTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wellarchitected as interfaces_wellarchitected
            
            review_template_reference = interfaces_wellarchitected.ReviewTemplateReference(
                template_arn="templateArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aff0e657e253e8180fdf4b38be6787eb3cfa2166327da2bcb2125bd911df96a6)
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_arn": template_arn,
        }

    @builtins.property
    def template_arn(self) -> builtins.str:
        '''The TemplateArn of the ReviewTemplate resource.'''
        result = self._values.get("template_arn")
        assert result is not None, "Required property 'template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReviewTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wellarchitected.WorkloadReference",
    jsii_struct_bases=[],
    name_mapping={"workload_arn": "workloadArn"},
)
class WorkloadReference:
    def __init__(self, *, workload_arn: builtins.str) -> None:
        '''A reference to a Workload resource.

        :param workload_arn: The WorkloadArn of the Workload resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wellarchitected as interfaces_wellarchitected
            
            workload_reference = interfaces_wellarchitected.WorkloadReference(
                workload_arn="workloadArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b80aadace37defea5bb38980b5834ceb8b9a78873d0957dc8eeea4651ac8e82d)
            check_type(argname="argument workload_arn", value=workload_arn, expected_type=type_hints["workload_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workload_arn": workload_arn,
        }

    @builtins.property
    def workload_arn(self) -> builtins.str:
        '''The WorkloadArn of the Workload resource.'''
        result = self._values.get("workload_arn")
        assert result is not None, "Required property 'workload_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AgentContextReference",
    "AgentGoalReference",
    "AgentProfileReference",
    "IAgentContextRef",
    "IAgentGoalRef",
    "IAgentProfileRef",
    "ILensRef",
    "IProfileRef",
    "IReviewTemplateRef",
    "IWorkloadRef",
    "LensReference",
    "ProfileReference",
    "ReviewTemplateReference",
    "WorkloadReference",
]

publication.publish()

def _typecheckingstub__2005652a4c7aeb4c9c766bde2753cbd872f80046ba3343f2baa92463aa142d95(
    *,
    agent_context_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc600cefd3fcbdb5270939e69bf2b3fcdb04992bfab764cbc3cd78d5f3ced5e0(
    *,
    agent_goal_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b789c8a6e2850f509bdd44d1e5975fb9dcfa99953874837034eca4dd50d22a(
    *,
    agent_profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f32344e8e195ba084ce4fcf47286bb12830dd7f6eb5a3d62943b345edff1b52f(
    *,
    lens_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae04271fcde99607a1aceb6f7563e89a6fe87895a913e2d8e18fa75b01e68eb(
    *,
    profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff0e657e253e8180fdf4b38be6787eb3cfa2166327da2bcb2125bd911df96a6(
    *,
    template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80aadace37defea5bb38980b5834ceb8b9a78873d0957dc8eeea4651ac8e82d(
    *,
    workload_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgentContextRef, IAgentGoalRef, IAgentProfileRef, ILensRef, IProfileRef, IReviewTemplateRef, IWorkloadRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
