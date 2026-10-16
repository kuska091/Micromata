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
    jsii_type="aws-cdk-lib.interfaces.aws_cloud9.EnvironmentEC2Reference",
    jsii_struct_bases=[],
    name_mapping={
        "environment_ec2_arn": "environmentEc2Arn",
        "environment_ec2_id": "environmentEc2Id",
    },
)
class EnvironmentEC2Reference:
    def __init__(
        self,
        *,
        environment_ec2_arn: builtins.str,
        environment_ec2_id: builtins.str,
    ) -> None:
        '''A reference to a EnvironmentEC2 resource.

        :param environment_ec2_arn: The ARN of the EnvironmentEC2 resource.
        :param environment_ec2_id: The Id of the EnvironmentEC2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloud9 as interfaces_cloud9
            
            environment_ec2_reference = interfaces_cloud9.EnvironmentEC2Reference(
                environment_ec2_arn="environmentEc2Arn",
                environment_ec2_id="environmentEc2Id"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d538c7572cb9bf5accfa63d3dd7f7c618baa2212148862a7177ea9c3791a10e4)
            check_type(argname="argument environment_ec2_arn", value=environment_ec2_arn, expected_type=type_hints["environment_ec2_arn"])
            check_type(argname="argument environment_ec2_id", value=environment_ec2_id, expected_type=type_hints["environment_ec2_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_ec2_arn": environment_ec2_arn,
            "environment_ec2_id": environment_ec2_id,
        }

    @builtins.property
    def environment_ec2_arn(self) -> builtins.str:
        '''The ARN of the EnvironmentEC2 resource.'''
        result = self._values.get("environment_ec2_arn")
        assert result is not None, "Required property 'environment_ec2_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_ec2_id(self) -> builtins.str:
        '''The Id of the EnvironmentEC2 resource.'''
        result = self._values.get("environment_ec2_id")
        assert result is not None, "Required property 'environment_ec2_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentEC2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloud9.IEnvironmentEC2Ref")
class IEnvironmentEC2Ref(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentEC2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentEc2Ref")
    def environment_ec2_ref(self) -> "EnvironmentEC2Reference":
        '''(experimental) A reference to a EnvironmentEC2 resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentEC2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentEC2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloud9.IEnvironmentEC2Ref"

    @builtins.property
    @jsii.member(jsii_name="environmentEc2Ref")
    def environment_ec2_ref(self) -> "EnvironmentEC2Reference":
        '''(experimental) A reference to a EnvironmentEC2 resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentEC2Reference", jsii.get(self, "environmentEc2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentEC2Ref).__jsii_proxy_class__ = lambda : _IEnvironmentEC2RefProxy


__all__ = [
    "EnvironmentEC2Reference",
    "IEnvironmentEC2Ref",
]

publication.publish()

def _typecheckingstub__d538c7572cb9bf5accfa63d3dd7f7c618baa2212148862a7177ea9c3791a10e4(
    *,
    environment_ec2_arn: builtins.str,
    environment_ec2_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEnvironmentEC2Ref]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
