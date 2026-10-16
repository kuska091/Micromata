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
    jsii_type="aws-cdk-lib.interfaces.aws_fms.ApplicationsListReference",
    jsii_struct_bases=[],
    name_mapping={"applications_list_arn": "applicationsListArn"},
)
class ApplicationsListReference:
    def __init__(self, *, applications_list_arn: builtins.str) -> None:
        '''A reference to a ApplicationsList resource.

        :param applications_list_arn: The Arn of the ApplicationsList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fms as interfaces_fms
            
            applications_list_reference = interfaces_fms.ApplicationsListReference(
                applications_list_arn="applicationsListArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fd767062b9c3c66613bcb1cdd0cd64ff908bd5264eccb796fbfcc4a324658cef)
            check_type(argname="argument applications_list_arn", value=applications_list_arn, expected_type=type_hints["applications_list_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "applications_list_arn": applications_list_arn,
        }

    @builtins.property
    def applications_list_arn(self) -> builtins.str:
        '''The Arn of the ApplicationsList resource.'''
        result = self._values.get("applications_list_arn")
        assert result is not None, "Required property 'applications_list_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationsListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fms.IApplicationsListRef")
class IApplicationsListRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationsList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationsListRef")
    def applications_list_ref(self) -> "ApplicationsListReference":
        '''(experimental) A reference to a ApplicationsList resource.

        :stability: experimental
        '''
        ...


class _IApplicationsListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationsList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fms.IApplicationsListRef"

    @builtins.property
    @jsii.member(jsii_name="applicationsListRef")
    def applications_list_ref(self) -> "ApplicationsListReference":
        '''(experimental) A reference to a ApplicationsList resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationsListReference", jsii.get(self, "applicationsListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationsListRef).__jsii_proxy_class__ = lambda : _IApplicationsListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fms.INotificationChannelRef")
class INotificationChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="notificationChannelRef")
    def notification_channel_ref(self) -> "NotificationChannelReference":
        '''(experimental) A reference to a NotificationChannel resource.

        :stability: experimental
        '''
        ...


class _INotificationChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fms.INotificationChannelRef"

    @builtins.property
    @jsii.member(jsii_name="notificationChannelRef")
    def notification_channel_ref(self) -> "NotificationChannelReference":
        '''(experimental) A reference to a NotificationChannel resource.

        :stability: experimental
        '''
        return typing.cast("NotificationChannelReference", jsii.get(self, "notificationChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationChannelRef).__jsii_proxy_class__ = lambda : _INotificationChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fms.IPolicyRef")
class IPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Policy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyRef")
    def policy_ref(self) -> "PolicyReference":
        '''(experimental) A reference to a Policy resource.

        :stability: experimental
        '''
        ...


class _IPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Policy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fms.IPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="policyRef")
    def policy_ref(self) -> "PolicyReference":
        '''(experimental) A reference to a Policy resource.

        :stability: experimental
        '''
        return typing.cast("PolicyReference", jsii.get(self, "policyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyRef).__jsii_proxy_class__ = lambda : _IPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fms.IProtocolsListRef")
class IProtocolsListRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProtocolsList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="protocolsListRef")
    def protocols_list_ref(self) -> "ProtocolsListReference":
        '''(experimental) A reference to a ProtocolsList resource.

        :stability: experimental
        '''
        ...


class _IProtocolsListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProtocolsList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fms.IProtocolsListRef"

    @builtins.property
    @jsii.member(jsii_name="protocolsListRef")
    def protocols_list_ref(self) -> "ProtocolsListReference":
        '''(experimental) A reference to a ProtocolsList resource.

        :stability: experimental
        '''
        return typing.cast("ProtocolsListReference", jsii.get(self, "protocolsListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProtocolsListRef).__jsii_proxy_class__ = lambda : _IProtocolsListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fms.IResourceSetRef")
class IResourceSetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceSetRef")
    def resource_set_ref(self) -> "ResourceSetReference":
        '''(experimental) A reference to a ResourceSet resource.

        :stability: experimental
        '''
        ...


class _IResourceSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fms.IResourceSetRef"

    @builtins.property
    @jsii.member(jsii_name="resourceSetRef")
    def resource_set_ref(self) -> "ResourceSetReference":
        '''(experimental) A reference to a ResourceSet resource.

        :stability: experimental
        '''
        return typing.cast("ResourceSetReference", jsii.get(self, "resourceSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceSetRef).__jsii_proxy_class__ = lambda : _IResourceSetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fms.NotificationChannelReference",
    jsii_struct_bases=[],
    name_mapping={"sns_topic_arn": "snsTopicArn"},
)
class NotificationChannelReference:
    def __init__(self, *, sns_topic_arn: builtins.str) -> None:
        '''A reference to a NotificationChannel resource.

        :param sns_topic_arn: The SnsTopicArn of the NotificationChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fms as interfaces_fms
            
            notification_channel_reference = interfaces_fms.NotificationChannelReference(
                sns_topic_arn="snsTopicArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__11fd5ad4d8928cca23731dd4925a4c4b61b5283f3ecdbf3d402a96b85317ab09)
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sns_topic_arn": sns_topic_arn,
        }

    @builtins.property
    def sns_topic_arn(self) -> builtins.str:
        '''The SnsTopicArn of the NotificationChannel resource.'''
        result = self._values.get("sns_topic_arn")
        assert result is not None, "Required property 'sns_topic_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fms.PolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_arn": "policyArn", "policy_id": "policyId"},
)
class PolicyReference:
    def __init__(self, *, policy_arn: builtins.str, policy_id: builtins.str) -> None:
        '''A reference to a Policy resource.

        :param policy_arn: The ARN of the Policy resource.
        :param policy_id: The Id of the Policy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fms as interfaces_fms
            
            policy_reference = interfaces_fms.PolicyReference(
                policy_arn="policyArn",
                policy_id="policyId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a1a50e184a934e3356d7b0070074e8da1635ba43b19d7f82b5b1f6a022c6e702)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
            "policy_id": policy_id,
        }

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''The ARN of the Policy resource.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_id(self) -> builtins.str:
        '''The Id of the Policy resource.'''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fms.ProtocolsListReference",
    jsii_struct_bases=[],
    name_mapping={"protocols_list_arn": "protocolsListArn"},
)
class ProtocolsListReference:
    def __init__(self, *, protocols_list_arn: builtins.str) -> None:
        '''A reference to a ProtocolsList resource.

        :param protocols_list_arn: The Arn of the ProtocolsList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fms as interfaces_fms
            
            protocols_list_reference = interfaces_fms.ProtocolsListReference(
                protocols_list_arn="protocolsListArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__edf39307c4ca7d1969c0196554c8ae21e90186d73fb64886826739c37bc51d92)
            check_type(argname="argument protocols_list_arn", value=protocols_list_arn, expected_type=type_hints["protocols_list_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocols_list_arn": protocols_list_arn,
        }

    @builtins.property
    def protocols_list_arn(self) -> builtins.str:
        '''The Arn of the ProtocolsList resource.'''
        result = self._values.get("protocols_list_arn")
        assert result is not None, "Required property 'protocols_list_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProtocolsListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fms.ResourceSetReference",
    jsii_struct_bases=[],
    name_mapping={"resource_set_id": "resourceSetId"},
)
class ResourceSetReference:
    def __init__(self, *, resource_set_id: builtins.str) -> None:
        '''A reference to a ResourceSet resource.

        :param resource_set_id: The Id of the ResourceSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fms as interfaces_fms
            
            resource_set_reference = interfaces_fms.ResourceSetReference(
                resource_set_id="resourceSetId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__89970659b727214f77ccee79079710a31240d6a8920fa829257befbf1553f42b)
            check_type(argname="argument resource_set_id", value=resource_set_id, expected_type=type_hints["resource_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_set_id": resource_set_id,
        }

    @builtins.property
    def resource_set_id(self) -> builtins.str:
        '''The Id of the ResourceSet resource.'''
        result = self._values.get("resource_set_id")
        assert result is not None, "Required property 'resource_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApplicationsListReference",
    "IApplicationsListRef",
    "INotificationChannelRef",
    "IPolicyRef",
    "IProtocolsListRef",
    "IResourceSetRef",
    "NotificationChannelReference",
    "PolicyReference",
    "ProtocolsListReference",
    "ResourceSetReference",
]

publication.publish()

def _typecheckingstub__fd767062b9c3c66613bcb1cdd0cd64ff908bd5264eccb796fbfcc4a324658cef(
    *,
    applications_list_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11fd5ad4d8928cca23731dd4925a4c4b61b5283f3ecdbf3d402a96b85317ab09(
    *,
    sns_topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a50e184a934e3356d7b0070074e8da1635ba43b19d7f82b5b1f6a022c6e702(
    *,
    policy_arn: builtins.str,
    policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edf39307c4ca7d1969c0196554c8ae21e90186d73fb64886826739c37bc51d92(
    *,
    protocols_list_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89970659b727214f77ccee79079710a31240d6a8920fa829257befbf1553f42b(
    *,
    resource_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationsListRef, INotificationChannelRef, IPolicyRef, IProtocolsListRef, IResourceSetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
