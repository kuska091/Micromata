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
    jsii_type="aws-cdk-lib.interfaces.aws_eventsv2.EventBusReference",
    jsii_struct_bases=[],
    name_mapping={"event_bus_arn": "eventBusArn"},
)
class EventBusReference:
    def __init__(self, *, event_bus_arn: builtins.str) -> None:
        '''A reference to a EventBus resource.

        :param event_bus_arn: The EventBusArn of the EventBus resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eventsv2 as interfaces_eventsv2
            
            event_bus_reference = interfaces_eventsv2.EventBusReference(
                event_bus_arn="eventBusArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__64e0c43e5b1323c7ef3e9729c8a0590d543e390ee50167753b2fc5360bcb384a)
            check_type(argname="argument event_bus_arn", value=event_bus_arn, expected_type=type_hints["event_bus_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bus_arn": event_bus_arn,
        }

    @builtins.property
    def event_bus_arn(self) -> builtins.str:
        '''The EventBusArn of the EventBus resource.'''
        result = self._values.get("event_bus_arn")
        assert result is not None, "Required property 'event_bus_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBusReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eventsv2.EventSourceReference",
    jsii_struct_bases=[],
    name_mapping={"event_source_arn": "eventSourceArn"},
)
class EventSourceReference:
    def __init__(self, *, event_source_arn: builtins.str) -> None:
        '''A reference to a EventSource resource.

        :param event_source_arn: The EventSourceArn of the EventSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eventsv2 as interfaces_eventsv2
            
            event_source_reference = interfaces_eventsv2.EventSourceReference(
                event_source_arn="eventSourceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d928a37af475af0518a3dd3ed1af321dde5ebb2d83aabed27f5424140ec3a06d)
            check_type(argname="argument event_source_arn", value=event_source_arn, expected_type=type_hints["event_source_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_source_arn": event_source_arn,
        }

    @builtins.property
    def event_source_arn(self) -> builtins.str:
        '''The EventSourceArn of the EventSource resource.'''
        result = self._values.get("event_source_arn")
        assert result is not None, "Required property 'event_source_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eventsv2.IEventBusRef")
class IEventBusRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventBus.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventBusRef")
    def event_bus_ref(self) -> "EventBusReference":
        '''(experimental) A reference to a EventBus resource.

        :stability: experimental
        '''
        ...


class _IEventBusRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventBus.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eventsv2.IEventBusRef"

    @builtins.property
    @jsii.member(jsii_name="eventBusRef")
    def event_bus_ref(self) -> "EventBusReference":
        '''(experimental) A reference to a EventBus resource.

        :stability: experimental
        '''
        return typing.cast("EventBusReference", jsii.get(self, "eventBusRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventBusRef).__jsii_proxy_class__ = lambda : _IEventBusRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eventsv2.IEventSourceRef")
class IEventSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventSourceRef")
    def event_source_ref(self) -> "EventSourceReference":
        '''(experimental) A reference to a EventSource resource.

        :stability: experimental
        '''
        ...


class _IEventSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eventsv2.IEventSourceRef"

    @builtins.property
    @jsii.member(jsii_name="eventSourceRef")
    def event_source_ref(self) -> "EventSourceReference":
        '''(experimental) A reference to a EventSource resource.

        :stability: experimental
        '''
        return typing.cast("EventSourceReference", jsii.get(self, "eventSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventSourceRef).__jsii_proxy_class__ = lambda : _IEventSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eventsv2.IResourcePolicyRef")
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eventsv2.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eventsv2.ISubscriberRef")
class ISubscriberRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Subscriber.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subscriberRef")
    def subscriber_ref(self) -> "SubscriberReference":
        '''(experimental) A reference to a Subscriber resource.

        :stability: experimental
        '''
        ...


class _ISubscriberRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Subscriber.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eventsv2.ISubscriberRef"

    @builtins.property
    @jsii.member(jsii_name="subscriberRef")
    def subscriber_ref(self) -> "SubscriberReference":
        '''(experimental) A reference to a Subscriber resource.

        :stability: experimental
        '''
        return typing.cast("SubscriberReference", jsii.get(self, "subscriberRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubscriberRef).__jsii_proxy_class__ = lambda : _ISubscriberRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eventsv2.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"event_bus_arn": "eventBusArn"},
)
class ResourcePolicyReference:
    def __init__(self, *, event_bus_arn: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param event_bus_arn: The EventBusArn of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eventsv2 as interfaces_eventsv2
            
            resource_policy_reference = interfaces_eventsv2.ResourcePolicyReference(
                event_bus_arn="eventBusArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fb1b1e9df0642c07edf4a4af74f455fc5c97ef7c72d48a1e10e32596197eb39b)
            check_type(argname="argument event_bus_arn", value=event_bus_arn, expected_type=type_hints["event_bus_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bus_arn": event_bus_arn,
        }

    @builtins.property
    def event_bus_arn(self) -> builtins.str:
        '''The EventBusArn of the ResourcePolicy resource.'''
        result = self._values.get("event_bus_arn")
        assert result is not None, "Required property 'event_bus_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eventsv2.SubscriberReference",
    jsii_struct_bases=[],
    name_mapping={"subscriber_arn": "subscriberArn"},
)
class SubscriberReference:
    def __init__(self, *, subscriber_arn: builtins.str) -> None:
        '''A reference to a Subscriber resource.

        :param subscriber_arn: The SubscriberArn of the Subscriber resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eventsv2 as interfaces_eventsv2
            
            subscriber_reference = interfaces_eventsv2.SubscriberReference(
                subscriber_arn="subscriberArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__809fd906d0350cb2e7f8b29bfbea67f21f5780a33d4deacf77b1b3566efc3600)
            check_type(argname="argument subscriber_arn", value=subscriber_arn, expected_type=type_hints["subscriber_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscriber_arn": subscriber_arn,
        }

    @builtins.property
    def subscriber_arn(self) -> builtins.str:
        '''The SubscriberArn of the Subscriber resource.'''
        result = self._values.get("subscriber_arn")
        assert result is not None, "Required property 'subscriber_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriberReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EventBusReference",
    "EventSourceReference",
    "IEventBusRef",
    "IEventSourceRef",
    "IResourcePolicyRef",
    "ISubscriberRef",
    "ResourcePolicyReference",
    "SubscriberReference",
]

publication.publish()

def _typecheckingstub__64e0c43e5b1323c7ef3e9729c8a0590d543e390ee50167753b2fc5360bcb384a(
    *,
    event_bus_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d928a37af475af0518a3dd3ed1af321dde5ebb2d83aabed27f5424140ec3a06d(
    *,
    event_source_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1b1e9df0642c07edf4a4af74f455fc5c97ef7c72d48a1e10e32596197eb39b(
    *,
    event_bus_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__809fd906d0350cb2e7f8b29bfbea67f21f5780a33d4deacf77b1b3566efc3600(
    *,
    subscriber_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEventBusRef, IEventSourceRef, IResourcePolicyRef, ISubscriberRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
