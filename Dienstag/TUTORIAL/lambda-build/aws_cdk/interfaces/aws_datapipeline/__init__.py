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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datapipeline.IPipelineRef")
class IPipelineRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Pipeline.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pipelineRef")
    def pipeline_ref(self) -> "PipelineReference":
        '''(experimental) A reference to a Pipeline resource.

        :stability: experimental
        '''
        ...


class _IPipelineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Pipeline.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datapipeline.IPipelineRef"

    @builtins.property
    @jsii.member(jsii_name="pipelineRef")
    def pipeline_ref(self) -> "PipelineReference":
        '''(experimental) A reference to a Pipeline resource.

        :stability: experimental
        '''
        return typing.cast("PipelineReference", jsii.get(self, "pipelineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPipelineRef).__jsii_proxy_class__ = lambda : _IPipelineRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datapipeline.PipelineReference",
    jsii_struct_bases=[],
    name_mapping={"pipeline_id": "pipelineId"},
)
class PipelineReference:
    def __init__(self, *, pipeline_id: builtins.str) -> None:
        '''A reference to a Pipeline resource.

        :param pipeline_id: The PipelineId of the Pipeline resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datapipeline as interfaces_datapipeline
            
            pipeline_reference = interfaces_datapipeline.PipelineReference(
                pipeline_id="pipelineId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__914739ab3d1d515815d82ec9d776f2446af762f22878de38b7b27d1f7c699932)
            check_type(argname="argument pipeline_id", value=pipeline_id, expected_type=type_hints["pipeline_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pipeline_id": pipeline_id,
        }

    @builtins.property
    def pipeline_id(self) -> builtins.str:
        '''The PipelineId of the Pipeline resource.'''
        result = self._values.get("pipeline_id")
        assert result is not None, "Required property 'pipeline_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IPipelineRef",
    "PipelineReference",
]

publication.publish()

def _typecheckingstub__914739ab3d1d515815d82ec9d776f2446af762f22878de38b7b27d1f7c699932(
    *,
    pipeline_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IPipelineRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
