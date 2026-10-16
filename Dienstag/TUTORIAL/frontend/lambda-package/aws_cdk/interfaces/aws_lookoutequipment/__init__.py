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
    jsii_type="aws-cdk-lib.interfaces.aws_lookoutequipment.IInferenceSchedulerRef"
)
class IInferenceSchedulerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InferenceScheduler.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="inferenceSchedulerRef")
    def inference_scheduler_ref(self) -> "InferenceSchedulerReference":
        '''(experimental) A reference to a InferenceScheduler resource.

        :stability: experimental
        '''
        ...


class _IInferenceSchedulerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InferenceScheduler.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lookoutequipment.IInferenceSchedulerRef"

    @builtins.property
    @jsii.member(jsii_name="inferenceSchedulerRef")
    def inference_scheduler_ref(self) -> "InferenceSchedulerReference":
        '''(experimental) A reference to a InferenceScheduler resource.

        :stability: experimental
        '''
        return typing.cast("InferenceSchedulerReference", jsii.get(self, "inferenceSchedulerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInferenceSchedulerRef).__jsii_proxy_class__ = lambda : _IInferenceSchedulerRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lookoutequipment.InferenceSchedulerReference",
    jsii_struct_bases=[],
    name_mapping={
        "inference_scheduler_arn": "inferenceSchedulerArn",
        "inference_scheduler_name": "inferenceSchedulerName",
    },
)
class InferenceSchedulerReference:
    def __init__(
        self,
        *,
        inference_scheduler_arn: builtins.str,
        inference_scheduler_name: builtins.str,
    ) -> None:
        '''A reference to a InferenceScheduler resource.

        :param inference_scheduler_arn: The ARN of the InferenceScheduler resource.
        :param inference_scheduler_name: The InferenceSchedulerName of the InferenceScheduler resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lookoutequipment as interfaces_lookoutequipment
            
            inference_scheduler_reference = interfaces_lookoutequipment.InferenceSchedulerReference(
                inference_scheduler_arn="inferenceSchedulerArn",
                inference_scheduler_name="inferenceSchedulerName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__be59a8e0c1b0b706aaaa38ed127d9b6b982e0771c3d871f23364f1a2831472bd)
            check_type(argname="argument inference_scheduler_arn", value=inference_scheduler_arn, expected_type=type_hints["inference_scheduler_arn"])
            check_type(argname="argument inference_scheduler_name", value=inference_scheduler_name, expected_type=type_hints["inference_scheduler_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "inference_scheduler_arn": inference_scheduler_arn,
            "inference_scheduler_name": inference_scheduler_name,
        }

    @builtins.property
    def inference_scheduler_arn(self) -> builtins.str:
        '''The ARN of the InferenceScheduler resource.'''
        result = self._values.get("inference_scheduler_arn")
        assert result is not None, "Required property 'inference_scheduler_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def inference_scheduler_name(self) -> builtins.str:
        '''The InferenceSchedulerName of the InferenceScheduler resource.'''
        result = self._values.get("inference_scheduler_name")
        assert result is not None, "Required property 'inference_scheduler_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InferenceSchedulerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IInferenceSchedulerRef",
    "InferenceSchedulerReference",
]

publication.publish()

def _typecheckingstub__be59a8e0c1b0b706aaaa38ed127d9b6b982e0771c3d871f23364f1a2831472bd(
    *,
    inference_scheduler_arn: builtins.str,
    inference_scheduler_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IInferenceSchedulerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
