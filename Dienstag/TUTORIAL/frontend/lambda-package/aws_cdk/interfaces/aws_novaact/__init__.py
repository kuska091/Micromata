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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_novaact.IWorkflowDefinitionRef")
class IWorkflowDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WorkflowDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workflowDefinitionRef")
    def workflow_definition_ref(self) -> "WorkflowDefinitionReference":
        '''(experimental) A reference to a WorkflowDefinition resource.

        :stability: experimental
        '''
        ...


class _IWorkflowDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WorkflowDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_novaact.IWorkflowDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="workflowDefinitionRef")
    def workflow_definition_ref(self) -> "WorkflowDefinitionReference":
        '''(experimental) A reference to a WorkflowDefinition resource.

        :stability: experimental
        '''
        return typing.cast("WorkflowDefinitionReference", jsii.get(self, "workflowDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkflowDefinitionRef).__jsii_proxy_class__ = lambda : _IWorkflowDefinitionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_novaact.WorkflowDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_definition_arn": "workflowDefinitionArn"},
)
class WorkflowDefinitionReference:
    def __init__(self, *, workflow_definition_arn: builtins.str) -> None:
        '''A reference to a WorkflowDefinition resource.

        :param workflow_definition_arn: The Arn of the WorkflowDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_novaact as interfaces_novaact
            
            workflow_definition_reference = interfaces_novaact.WorkflowDefinitionReference(
                workflow_definition_arn="workflowDefinitionArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8b330f30e5808d2893fa4a25455d3e75e33c50501b5f228a742f699ae50d33ba)
            check_type(argname="argument workflow_definition_arn", value=workflow_definition_arn, expected_type=type_hints["workflow_definition_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_definition_arn": workflow_definition_arn,
        }

    @builtins.property
    def workflow_definition_arn(self) -> builtins.str:
        '''The Arn of the WorkflowDefinition resource.'''
        result = self._values.get("workflow_definition_arn")
        assert result is not None, "Required property 'workflow_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IWorkflowDefinitionRef",
    "WorkflowDefinitionReference",
]

publication.publish()

def _typecheckingstub__8b330f30e5808d2893fa4a25455d3e75e33c50501b5f228a742f699ae50d33ba(
    *,
    workflow_definition_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IWorkflowDefinitionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
