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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssmincidents.IReplicationSetRef")
class IReplicationSetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicationSetRef")
    def replication_set_ref(self) -> "ReplicationSetReference":
        '''(experimental) A reference to a ReplicationSet resource.

        :stability: experimental
        '''
        ...


class _IReplicationSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssmincidents.IReplicationSetRef"

    @builtins.property
    @jsii.member(jsii_name="replicationSetRef")
    def replication_set_ref(self) -> "ReplicationSetReference":
        '''(experimental) A reference to a ReplicationSet resource.

        :stability: experimental
        '''
        return typing.cast("ReplicationSetReference", jsii.get(self, "replicationSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicationSetRef).__jsii_proxy_class__ = lambda : _IReplicationSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssmincidents.IResponsePlanRef")
class IResponsePlanRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResponsePlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="responsePlanRef")
    def response_plan_ref(self) -> "ResponsePlanReference":
        '''(experimental) A reference to a ResponsePlan resource.

        :stability: experimental
        '''
        ...


class _IResponsePlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResponsePlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssmincidents.IResponsePlanRef"

    @builtins.property
    @jsii.member(jsii_name="responsePlanRef")
    def response_plan_ref(self) -> "ResponsePlanReference":
        '''(experimental) A reference to a ResponsePlan resource.

        :stability: experimental
        '''
        return typing.cast("ResponsePlanReference", jsii.get(self, "responsePlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResponsePlanRef).__jsii_proxy_class__ = lambda : _IResponsePlanRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssmincidents.ReplicationSetReference",
    jsii_struct_bases=[],
    name_mapping={"replication_set_arn": "replicationSetArn"},
)
class ReplicationSetReference:
    def __init__(self, *, replication_set_arn: builtins.str) -> None:
        '''A reference to a ReplicationSet resource.

        :param replication_set_arn: The Arn of the ReplicationSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssmincidents as interfaces_ssmincidents
            
            replication_set_reference = interfaces_ssmincidents.ReplicationSetReference(
                replication_set_arn="replicationSetArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__474095d195b5d0f5924650d969964649459f233d088001e0e567586503a0afa4)
            check_type(argname="argument replication_set_arn", value=replication_set_arn, expected_type=type_hints["replication_set_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_set_arn": replication_set_arn,
        }

    @builtins.property
    def replication_set_arn(self) -> builtins.str:
        '''The Arn of the ReplicationSet resource.'''
        result = self._values.get("replication_set_arn")
        assert result is not None, "Required property 'replication_set_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssmincidents.ResponsePlanReference",
    jsii_struct_bases=[],
    name_mapping={"response_plan_arn": "responsePlanArn"},
)
class ResponsePlanReference:
    def __init__(self, *, response_plan_arn: builtins.str) -> None:
        '''A reference to a ResponsePlan resource.

        :param response_plan_arn: The Arn of the ResponsePlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssmincidents as interfaces_ssmincidents
            
            response_plan_reference = interfaces_ssmincidents.ResponsePlanReference(
                response_plan_arn="responsePlanArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d23ee8f18edcf755f00bf1179edc2b037d68c498b2c72657c9f976ba0da8550f)
            check_type(argname="argument response_plan_arn", value=response_plan_arn, expected_type=type_hints["response_plan_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "response_plan_arn": response_plan_arn,
        }

    @builtins.property
    def response_plan_arn(self) -> builtins.str:
        '''The Arn of the ResponsePlan resource.'''
        result = self._values.get("response_plan_arn")
        assert result is not None, "Required property 'response_plan_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResponsePlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IReplicationSetRef",
    "IResponsePlanRef",
    "ReplicationSetReference",
    "ResponsePlanReference",
]

publication.publish()

def _typecheckingstub__474095d195b5d0f5924650d969964649459f233d088001e0e567586503a0afa4(
    *,
    replication_set_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d23ee8f18edcf755f00bf1179edc2b037d68c498b2c72657c9f976ba0da8550f(
    *,
    response_plan_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IReplicationSetRef, IResponsePlanRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
