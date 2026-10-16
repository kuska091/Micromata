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
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.AppReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppReference:
    def __init__(self) -> None:
        '''A reference to a App resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            app_reference = interfaces_opsworks.AppReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.ElasticLoadBalancerAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class ElasticLoadBalancerAttachmentReference:
    def __init__(self) -> None:
        '''A reference to a ElasticLoadBalancerAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            elastic_load_balancer_attachment_reference = interfaces_opsworks.ElasticLoadBalancerAttachmentReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticLoadBalancerAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IAppRef")
class IAppRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        ...


class _IAppRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IAppRef"

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        return typing.cast("AppReference", jsii.get(self, "appRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppRef).__jsii_proxy_class__ = lambda : _IAppRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IElasticLoadBalancerAttachmentRef"
)
class IElasticLoadBalancerAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ElasticLoadBalancerAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancerAttachmentRef")
    def elastic_load_balancer_attachment_ref(
        self,
    ) -> "ElasticLoadBalancerAttachmentReference":
        '''(experimental) A reference to a ElasticLoadBalancerAttachment resource.

        :stability: experimental
        '''
        ...


class _IElasticLoadBalancerAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ElasticLoadBalancerAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IElasticLoadBalancerAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancerAttachmentRef")
    def elastic_load_balancer_attachment_ref(
        self,
    ) -> "ElasticLoadBalancerAttachmentReference":
        '''(experimental) A reference to a ElasticLoadBalancerAttachment resource.

        :stability: experimental
        '''
        return typing.cast("ElasticLoadBalancerAttachmentReference", jsii.get(self, "elasticLoadBalancerAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IElasticLoadBalancerAttachmentRef).__jsii_proxy_class__ = lambda : _IElasticLoadBalancerAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IInstanceRef")
class IInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Instance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        ...


class _IInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Instance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        return typing.cast("InstanceReference", jsii.get(self, "instanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceRef).__jsii_proxy_class__ = lambda : _IInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.ILayerRef")
class ILayerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Layer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="layerRef")
    def layer_ref(self) -> "LayerReference":
        '''(experimental) A reference to a Layer resource.

        :stability: experimental
        '''
        ...


class _ILayerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Layer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.ILayerRef"

    @builtins.property
    @jsii.member(jsii_name="layerRef")
    def layer_ref(self) -> "LayerReference":
        '''(experimental) A reference to a Layer resource.

        :stability: experimental
        '''
        return typing.cast("LayerReference", jsii.get(self, "layerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILayerRef).__jsii_proxy_class__ = lambda : _ILayerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IStackRef")
class IStackRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Stack.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stackRef")
    def stack_ref(self) -> "StackReference":
        '''(experimental) A reference to a Stack resource.

        :stability: experimental
        '''
        ...


class _IStackRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Stack.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IStackRef"

    @builtins.property
    @jsii.member(jsii_name="stackRef")
    def stack_ref(self) -> "StackReference":
        '''(experimental) A reference to a Stack resource.

        :stability: experimental
        '''
        return typing.cast("StackReference", jsii.get(self, "stackRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackRef).__jsii_proxy_class__ = lambda : _IStackRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IUserProfileRef")
class IUserProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userProfileRef")
    def user_profile_ref(self) -> "UserProfileReference":
        '''(experimental) A reference to a UserProfile resource.

        :stability: experimental
        '''
        ...


class _IUserProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IUserProfileRef"

    @builtins.property
    @jsii.member(jsii_name="userProfileRef")
    def user_profile_ref(self) -> "UserProfileReference":
        '''(experimental) A reference to a UserProfile resource.

        :stability: experimental
        '''
        return typing.cast("UserProfileReference", jsii.get(self, "userProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserProfileRef).__jsii_proxy_class__ = lambda : _IUserProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IVolumeRef")
class IVolumeRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        ...


class _IVolumeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IVolumeRef"

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        return typing.cast("VolumeReference", jsii.get(self, "volumeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVolumeRef).__jsii_proxy_class__ = lambda : _IVolumeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.InstanceReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class InstanceReference:
    def __init__(self) -> None:
        '''A reference to a Instance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            instance_reference = interfaces_opsworks.InstanceReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.LayerReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class LayerReference:
    def __init__(self) -> None:
        '''A reference to a Layer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            layer_reference = interfaces_opsworks.LayerReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.StackReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class StackReference:
    def __init__(self) -> None:
        '''A reference to a Stack resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            stack_reference = interfaces_opsworks.StackReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.UserProfileReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class UserProfileReference:
    def __init__(self) -> None:
        '''A reference to a UserProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            user_profile_reference = interfaces_opsworks.UserProfileReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.VolumeReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class VolumeReference:
    def __init__(self) -> None:
        '''A reference to a Volume resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            volume_reference = interfaces_opsworks.VolumeReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppReference",
    "ElasticLoadBalancerAttachmentReference",
    "IAppRef",
    "IElasticLoadBalancerAttachmentRef",
    "IInstanceRef",
    "ILayerRef",
    "IStackRef",
    "IUserProfileRef",
    "IVolumeRef",
    "InstanceReference",
    "LayerReference",
    "StackReference",
    "UserProfileReference",
    "VolumeReference",
]

publication.publish()

for cls in [IAppRef, IElasticLoadBalancerAttachmentRef, IInstanceRef, ILayerRef, IStackRef, IUserProfileRef, IVolumeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
