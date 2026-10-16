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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_translate.IParallelDataRef")
class IParallelDataRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ParallelData.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="parallelDataRef")
    def parallel_data_ref(self) -> "ParallelDataReference":
        '''(experimental) A reference to a ParallelData resource.

        :stability: experimental
        '''
        ...


class _IParallelDataRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ParallelData.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_translate.IParallelDataRef"

    @builtins.property
    @jsii.member(jsii_name="parallelDataRef")
    def parallel_data_ref(self) -> "ParallelDataReference":
        '''(experimental) A reference to a ParallelData resource.

        :stability: experimental
        '''
        return typing.cast("ParallelDataReference", jsii.get(self, "parallelDataRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParallelDataRef).__jsii_proxy_class__ = lambda : _IParallelDataRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_translate.ParallelDataReference",
    jsii_struct_bases=[],
    name_mapping={"parallel_data_arn": "parallelDataArn"},
)
class ParallelDataReference:
    def __init__(self, *, parallel_data_arn: builtins.str) -> None:
        '''A reference to a ParallelData resource.

        :param parallel_data_arn: The Arn of the ParallelData resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_translate as interfaces_translate
            
            parallel_data_reference = interfaces_translate.ParallelDataReference(
                parallel_data_arn="parallelDataArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1f563aaa859cf1c55eccea6ecdd28403f7b335b9f15bcb14259f644d98c30314)
            check_type(argname="argument parallel_data_arn", value=parallel_data_arn, expected_type=type_hints["parallel_data_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parallel_data_arn": parallel_data_arn,
        }

    @builtins.property
    def parallel_data_arn(self) -> builtins.str:
        '''The Arn of the ParallelData resource.'''
        result = self._values.get("parallel_data_arn")
        assert result is not None, "Required property 'parallel_data_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParallelDataReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IParallelDataRef",
    "ParallelDataReference",
]

publication.publish()

def _typecheckingstub__1f563aaa859cf1c55eccea6ecdd28403f7b335b9f15bcb14259f644d98c30314(
    *,
    parallel_data_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IParallelDataRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
