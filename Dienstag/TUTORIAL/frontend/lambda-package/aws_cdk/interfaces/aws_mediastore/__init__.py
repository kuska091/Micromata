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
    jsii_type="aws-cdk-lib.interfaces.aws_mediastore.ContainerReference",
    jsii_struct_bases=[],
    name_mapping={"container_id": "containerId", "container_name": "containerName"},
)
class ContainerReference:
    def __init__(
        self,
        *,
        container_id: builtins.str,
        container_name: builtins.str,
    ) -> None:
        '''A reference to a Container resource.

        :param container_id: The Id of the Container resource.
        :param container_name: The ContainerName of the Container resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediastore as interfaces_mediastore
            
            container_reference = interfaces_mediastore.ContainerReference(
                container_id="containerId",
                container_name="containerName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5fc1e7d63ffcff822c29c0c5b4e61add8e8b4ea0adcb2738490b14e8602e367c)
            check_type(argname="argument container_id", value=container_id, expected_type=type_hints["container_id"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_id": container_id,
            "container_name": container_name,
        }

    @builtins.property
    def container_id(self) -> builtins.str:
        '''The Id of the Container resource.'''
        result = self._values.get("container_id")
        assert result is not None, "Required property 'container_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> builtins.str:
        '''The ContainerName of the Container resource.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediastore.IContainerRef")
class IContainerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Container.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="containerRef")
    def container_ref(self) -> "ContainerReference":
        '''(experimental) A reference to a Container resource.

        :stability: experimental
        '''
        ...


class _IContainerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Container.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediastore.IContainerRef"

    @builtins.property
    @jsii.member(jsii_name="containerRef")
    def container_ref(self) -> "ContainerReference":
        '''(experimental) A reference to a Container resource.

        :stability: experimental
        '''
        return typing.cast("ContainerReference", jsii.get(self, "containerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContainerRef).__jsii_proxy_class__ = lambda : _IContainerRefProxy


__all__ = [
    "ContainerReference",
    "IContainerRef",
]

publication.publish()

def _typecheckingstub__5fc1e7d63ffcff822c29c0c5b4e61add8e8b4ea0adcb2738490b14e8602e367c(
    *,
    container_id: builtins.str,
    container_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IContainerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
