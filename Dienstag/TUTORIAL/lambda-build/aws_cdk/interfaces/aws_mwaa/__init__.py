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
    jsii_type="aws-cdk-lib.interfaces.aws_mwaa.EnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "environment_arn": "environmentArn",
        "environment_name": "environmentName",
    },
)
class EnvironmentReference:
    def __init__(
        self,
        *,
        environment_arn: builtins.str,
        environment_name: builtins.str,
    ) -> None:
        '''A reference to a Environment resource.

        :param environment_arn: The ARN of the Environment resource.
        :param environment_name: The Name of the Environment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mwaa as interfaces_mwaa
            
            environment_reference = interfaces_mwaa.EnvironmentReference(
                environment_arn="environmentArn",
                environment_name="environmentName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ef33bf7356d4d77898d81dde6d08508edc50ac2ccc667eae7b803d4fc25588ba)
            check_type(argname="argument environment_arn", value=environment_arn, expected_type=type_hints["environment_arn"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_arn": environment_arn,
            "environment_name": environment_name,
        }

    @builtins.property
    def environment_arn(self) -> builtins.str:
        '''The ARN of the Environment resource.'''
        result = self._values.get("environment_arn")
        assert result is not None, "Required property 'environment_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_name(self) -> builtins.str:
        '''The Name of the Environment resource.'''
        result = self._values.get("environment_name")
        assert result is not None, "Required property 'environment_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mwaa.IEnvironmentRef")
class IEnvironmentRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mwaa.IEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentReference", jsii.get(self, "environmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentRef).__jsii_proxy_class__ = lambda : _IEnvironmentRefProxy


__all__ = [
    "EnvironmentReference",
    "IEnvironmentRef",
]

publication.publish()

def _typecheckingstub__ef33bf7356d4d77898d81dde6d08508edc50ac2ccc667eae7b803d4fc25588ba(
    *,
    environment_arn: builtins.str,
    environment_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEnvironmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
