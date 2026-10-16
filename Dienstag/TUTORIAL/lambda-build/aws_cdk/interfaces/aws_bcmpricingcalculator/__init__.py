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
    jsii_type="aws-cdk-lib.interfaces.aws_bcmpricingcalculator.BillScenarioReference",
    jsii_struct_bases=[],
    name_mapping={"bill_scenario_arn": "billScenarioArn"},
)
class BillScenarioReference:
    def __init__(self, *, bill_scenario_arn: builtins.str) -> None:
        '''A reference to a BillScenario resource.

        :param bill_scenario_arn: The Arn of the BillScenario resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bcmpricingcalculator as interfaces_bcmpricingcalculator
            
            bill_scenario_reference = interfaces_bcmpricingcalculator.BillScenarioReference(
                bill_scenario_arn="billScenarioArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1a4b8207a20270e6b553edc4af87ceaf942f02e0451a503352b2dd42aa4f4365)
            check_type(argname="argument bill_scenario_arn", value=bill_scenario_arn, expected_type=type_hints["bill_scenario_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bill_scenario_arn": bill_scenario_arn,
        }

    @builtins.property
    def bill_scenario_arn(self) -> builtins.str:
        '''The Arn of the BillScenario resource.'''
        result = self._values.get("bill_scenario_arn")
        assert result is not None, "Required property 'bill_scenario_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillScenarioReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_bcmpricingcalculator.IBillScenarioRef"
)
class IBillScenarioRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BillScenario.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="billScenarioRef")
    def bill_scenario_ref(self) -> "BillScenarioReference":
        '''(experimental) A reference to a BillScenario resource.

        :stability: experimental
        '''
        ...


class _IBillScenarioRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BillScenario.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bcmpricingcalculator.IBillScenarioRef"

    @builtins.property
    @jsii.member(jsii_name="billScenarioRef")
    def bill_scenario_ref(self) -> "BillScenarioReference":
        '''(experimental) A reference to a BillScenario resource.

        :stability: experimental
        '''
        return typing.cast("BillScenarioReference", jsii.get(self, "billScenarioRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBillScenarioRef).__jsii_proxy_class__ = lambda : _IBillScenarioRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_bcmpricingcalculator.IWorkloadEstimateRef"
)
class IWorkloadEstimateRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WorkloadEstimate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workloadEstimateRef")
    def workload_estimate_ref(self) -> "WorkloadEstimateReference":
        '''(experimental) A reference to a WorkloadEstimate resource.

        :stability: experimental
        '''
        ...


class _IWorkloadEstimateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WorkloadEstimate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bcmpricingcalculator.IWorkloadEstimateRef"

    @builtins.property
    @jsii.member(jsii_name="workloadEstimateRef")
    def workload_estimate_ref(self) -> "WorkloadEstimateReference":
        '''(experimental) A reference to a WorkloadEstimate resource.

        :stability: experimental
        '''
        return typing.cast("WorkloadEstimateReference", jsii.get(self, "workloadEstimateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkloadEstimateRef).__jsii_proxy_class__ = lambda : _IWorkloadEstimateRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bcmpricingcalculator.WorkloadEstimateReference",
    jsii_struct_bases=[],
    name_mapping={"workload_estimate_arn": "workloadEstimateArn"},
)
class WorkloadEstimateReference:
    def __init__(self, *, workload_estimate_arn: builtins.str) -> None:
        '''A reference to a WorkloadEstimate resource.

        :param workload_estimate_arn: The Arn of the WorkloadEstimate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bcmpricingcalculator as interfaces_bcmpricingcalculator
            
            workload_estimate_reference = interfaces_bcmpricingcalculator.WorkloadEstimateReference(
                workload_estimate_arn="workloadEstimateArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__de6ba9bcdde6ecb3896855e90eb55ce2987027371ff94e31cc1a9d907991e0a4)
            check_type(argname="argument workload_estimate_arn", value=workload_estimate_arn, expected_type=type_hints["workload_estimate_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workload_estimate_arn": workload_estimate_arn,
        }

    @builtins.property
    def workload_estimate_arn(self) -> builtins.str:
        '''The Arn of the WorkloadEstimate resource.'''
        result = self._values.get("workload_estimate_arn")
        assert result is not None, "Required property 'workload_estimate_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadEstimateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BillScenarioReference",
    "IBillScenarioRef",
    "IWorkloadEstimateRef",
    "WorkloadEstimateReference",
]

publication.publish()

def _typecheckingstub__1a4b8207a20270e6b553edc4af87ceaf942f02e0451a503352b2dd42aa4f4365(
    *,
    bill_scenario_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6ba9bcdde6ecb3896855e90eb55ce2987027371ff94e31cc1a9d907991e0a4(
    *,
    workload_estimate_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBillScenarioRef, IWorkloadEstimateRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
