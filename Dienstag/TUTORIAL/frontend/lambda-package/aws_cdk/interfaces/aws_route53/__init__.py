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
    jsii_type="aws-cdk-lib.interfaces.aws_route53.CidrCollectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "cidr_collection_arn": "cidrCollectionArn",
        "cidr_collection_id": "cidrCollectionId",
    },
)
class CidrCollectionReference:
    def __init__(
        self,
        *,
        cidr_collection_arn: builtins.str,
        cidr_collection_id: builtins.str,
    ) -> None:
        '''A reference to a CidrCollection resource.

        :param cidr_collection_arn: The ARN of the CidrCollection resource.
        :param cidr_collection_id: The Id of the CidrCollection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            cidr_collection_reference = interfaces_route53.CidrCollectionReference(
                cidr_collection_arn="cidrCollectionArn",
                cidr_collection_id="cidrCollectionId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a29c970e3dc59eb61f1e0e1c4183e889924847e040535cfbaa68366929f5a856)
            check_type(argname="argument cidr_collection_arn", value=cidr_collection_arn, expected_type=type_hints["cidr_collection_arn"])
            check_type(argname="argument cidr_collection_id", value=cidr_collection_id, expected_type=type_hints["cidr_collection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidr_collection_arn": cidr_collection_arn,
            "cidr_collection_id": cidr_collection_id,
        }

    @builtins.property
    def cidr_collection_arn(self) -> builtins.str:
        '''The ARN of the CidrCollection resource.'''
        result = self._values.get("cidr_collection_arn")
        assert result is not None, "Required property 'cidr_collection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_collection_id(self) -> builtins.str:
        '''The Id of the CidrCollection resource.'''
        result = self._values.get("cidr_collection_id")
        assert result is not None, "Required property 'cidr_collection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CidrCollectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.DNSSECReference",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_id": "hostedZoneId"},
)
class DNSSECReference:
    def __init__(self, *, hosted_zone_id: builtins.str) -> None:
        '''A reference to a DNSSEC resource.

        :param hosted_zone_id: The HostedZoneId of the DNSSEC resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            d_nssec_reference = interfaces_route53.DNSSECReference(
                hosted_zone_id="hostedZoneId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b5f748a2bea377e2fd2ed6d48058439646815e844893d9564084429051caf8f4)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''The HostedZoneId of the DNSSEC resource.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DNSSECReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.DelegationSetReference",
    jsii_struct_bases=[],
    name_mapping={"delegation_set_arn": "delegationSetArn"},
)
class DelegationSetReference:
    def __init__(self, *, delegation_set_arn: builtins.str) -> None:
        '''A reference to a DelegationSet resource.

        :param delegation_set_arn: The Arn of the DelegationSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            delegation_set_reference = interfaces_route53.DelegationSetReference(
                delegation_set_arn="delegationSetArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__70ea8bdca93efb6e0465035d00ee2a50843b0dabe0ffbcffba7146b6be994339)
            check_type(argname="argument delegation_set_arn", value=delegation_set_arn, expected_type=type_hints["delegation_set_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delegation_set_arn": delegation_set_arn,
        }

    @builtins.property
    def delegation_set_arn(self) -> builtins.str:
        '''The Arn of the DelegationSet resource.'''
        result = self._values.get("delegation_set_arn")
        assert result is not None, "Required property 'delegation_set_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DelegationSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.HealthCheckReference",
    jsii_struct_bases=[],
    name_mapping={"health_check_id": "healthCheckId"},
)
class HealthCheckReference:
    def __init__(self, *, health_check_id: builtins.str) -> None:
        '''A reference to a HealthCheck resource.

        :param health_check_id: The HealthCheckId of the HealthCheck resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            health_check_reference = interfaces_route53.HealthCheckReference(
                health_check_id="healthCheckId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__93a61fcf52d45a4375dfb1ae5d0b7b0555ae1091958107075e82bc35ca0d0275)
            check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "health_check_id": health_check_id,
        }

    @builtins.property
    def health_check_id(self) -> builtins.str:
        '''The HealthCheckId of the HealthCheck resource.'''
        result = self._values.get("health_check_id")
        assert result is not None, "Required property 'health_check_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthCheckReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.HostedZoneReference",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_id": "hostedZoneId"},
)
class HostedZoneReference:
    def __init__(self, *, hosted_zone_id: builtins.str) -> None:
        '''A reference to a HostedZone resource.

        :param hosted_zone_id: The Id of the HostedZone resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            hosted_zone_reference = interfaces_route53.HostedZoneReference(
                hosted_zone_id="hostedZoneId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3b4ca2affe8c503a8b4867d3e31a36ed15f0aa004cff0a9202da3d2bbbb7fe4c)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''The Id of the HostedZone resource.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.ICidrCollectionRef")
class ICidrCollectionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CidrCollection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cidrCollectionRef")
    def cidr_collection_ref(self) -> "CidrCollectionReference":
        '''(experimental) A reference to a CidrCollection resource.

        :stability: experimental
        '''
        ...


class _ICidrCollectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CidrCollection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.ICidrCollectionRef"

    @builtins.property
    @jsii.member(jsii_name="cidrCollectionRef")
    def cidr_collection_ref(self) -> "CidrCollectionReference":
        '''(experimental) A reference to a CidrCollection resource.

        :stability: experimental
        '''
        return typing.cast("CidrCollectionReference", jsii.get(self, "cidrCollectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICidrCollectionRef).__jsii_proxy_class__ = lambda : _ICidrCollectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IDNSSECRef")
class IDNSSECRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DNSSEC.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dnssecRef")
    def dnssec_ref(self) -> "DNSSECReference":
        '''(experimental) A reference to a DNSSEC resource.

        :stability: experimental
        '''
        ...


class _IDNSSECRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DNSSEC.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IDNSSECRef"

    @builtins.property
    @jsii.member(jsii_name="dnssecRef")
    def dnssec_ref(self) -> "DNSSECReference":
        '''(experimental) A reference to a DNSSEC resource.

        :stability: experimental
        '''
        return typing.cast("DNSSECReference", jsii.get(self, "dnssecRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDNSSECRef).__jsii_proxy_class__ = lambda : _IDNSSECRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IDelegationSetRef")
class IDelegationSetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DelegationSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="delegationSetRef")
    def delegation_set_ref(self) -> "DelegationSetReference":
        '''(experimental) A reference to a DelegationSet resource.

        :stability: experimental
        '''
        ...


class _IDelegationSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DelegationSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IDelegationSetRef"

    @builtins.property
    @jsii.member(jsii_name="delegationSetRef")
    def delegation_set_ref(self) -> "DelegationSetReference":
        '''(experimental) A reference to a DelegationSet resource.

        :stability: experimental
        '''
        return typing.cast("DelegationSetReference", jsii.get(self, "delegationSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDelegationSetRef).__jsii_proxy_class__ = lambda : _IDelegationSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IHealthCheckRef")
class IHealthCheckRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HealthCheck.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="healthCheckRef")
    def health_check_ref(self) -> "HealthCheckReference":
        '''(experimental) A reference to a HealthCheck resource.

        :stability: experimental
        '''
        ...


class _IHealthCheckRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HealthCheck.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IHealthCheckRef"

    @builtins.property
    @jsii.member(jsii_name="healthCheckRef")
    def health_check_ref(self) -> "HealthCheckReference":
        '''(experimental) A reference to a HealthCheck resource.

        :stability: experimental
        '''
        return typing.cast("HealthCheckReference", jsii.get(self, "healthCheckRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHealthCheckRef).__jsii_proxy_class__ = lambda : _IHealthCheckRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IHostedZoneRef")
class IHostedZoneRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HostedZone.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hostedZoneRef")
    def hosted_zone_ref(self) -> "HostedZoneReference":
        '''(experimental) A reference to a HostedZone resource.

        :stability: experimental
        '''
        ...


class _IHostedZoneRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HostedZone.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IHostedZoneRef"

    @builtins.property
    @jsii.member(jsii_name="hostedZoneRef")
    def hosted_zone_ref(self) -> "HostedZoneReference":
        '''(experimental) A reference to a HostedZone resource.

        :stability: experimental
        '''
        return typing.cast("HostedZoneReference", jsii.get(self, "hostedZoneRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHostedZoneRef).__jsii_proxy_class__ = lambda : _IHostedZoneRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IKeySigningKeyRef")
class IKeySigningKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a KeySigningKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyRef")
    def key_signing_key_ref(self) -> "KeySigningKeyReference":
        '''(experimental) A reference to a KeySigningKey resource.

        :stability: experimental
        '''
        ...


class _IKeySigningKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a KeySigningKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IKeySigningKeyRef"

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyRef")
    def key_signing_key_ref(self) -> "KeySigningKeyReference":
        '''(experimental) A reference to a KeySigningKey resource.

        :stability: experimental
        '''
        return typing.cast("KeySigningKeyReference", jsii.get(self, "keySigningKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeySigningKeyRef).__jsii_proxy_class__ = lambda : _IKeySigningKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IQueryLoggingConfigRef")
class IQueryLoggingConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QueryLoggingConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queryLoggingConfigRef")
    def query_logging_config_ref(self) -> "QueryLoggingConfigReference":
        '''(experimental) A reference to a QueryLoggingConfig resource.

        :stability: experimental
        '''
        ...


class _IQueryLoggingConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QueryLoggingConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IQueryLoggingConfigRef"

    @builtins.property
    @jsii.member(jsii_name="queryLoggingConfigRef")
    def query_logging_config_ref(self) -> "QueryLoggingConfigReference":
        '''(experimental) A reference to a QueryLoggingConfig resource.

        :stability: experimental
        '''
        return typing.cast("QueryLoggingConfigReference", jsii.get(self, "queryLoggingConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueryLoggingConfigRef).__jsii_proxy_class__ = lambda : _IQueryLoggingConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IRecordSetGroupRef")
class IRecordSetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RecordSetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="recordSetGroupRef")
    def record_set_group_ref(self) -> "RecordSetGroupReference":
        '''(experimental) A reference to a RecordSetGroup resource.

        :stability: experimental
        '''
        ...


class _IRecordSetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RecordSetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IRecordSetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="recordSetGroupRef")
    def record_set_group_ref(self) -> "RecordSetGroupReference":
        '''(experimental) A reference to a RecordSetGroup resource.

        :stability: experimental
        '''
        return typing.cast("RecordSetGroupReference", jsii.get(self, "recordSetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRecordSetGroupRef).__jsii_proxy_class__ = lambda : _IRecordSetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IRecordSetRef")
class IRecordSetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RecordSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="recordSetRef")
    def record_set_ref(self) -> "RecordSetReference":
        '''(experimental) A reference to a RecordSet resource.

        :stability: experimental
        '''
        ...


class _IRecordSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RecordSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IRecordSetRef"

    @builtins.property
    @jsii.member(jsii_name="recordSetRef")
    def record_set_ref(self) -> "RecordSetReference":
        '''(experimental) A reference to a RecordSet resource.

        :stability: experimental
        '''
        return typing.cast("RecordSetReference", jsii.get(self, "recordSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRecordSetRef).__jsii_proxy_class__ = lambda : _IRecordSetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.ITrafficPolicyInstanceRef"
)
class ITrafficPolicyInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficPolicyInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trafficPolicyInstanceRef")
    def traffic_policy_instance_ref(self) -> "TrafficPolicyInstanceReference":
        '''(experimental) A reference to a TrafficPolicyInstance resource.

        :stability: experimental
        '''
        ...


class _ITrafficPolicyInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficPolicyInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.ITrafficPolicyInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="trafficPolicyInstanceRef")
    def traffic_policy_instance_ref(self) -> "TrafficPolicyInstanceReference":
        '''(experimental) A reference to a TrafficPolicyInstance resource.

        :stability: experimental
        '''
        return typing.cast("TrafficPolicyInstanceReference", jsii.get(self, "trafficPolicyInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrafficPolicyInstanceRef).__jsii_proxy_class__ = lambda : _ITrafficPolicyInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.ITrafficPolicyRef")
class ITrafficPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trafficPolicyRef")
    def traffic_policy_ref(self) -> "TrafficPolicyReference":
        '''(experimental) A reference to a TrafficPolicy resource.

        :stability: experimental
        '''
        ...


class _ITrafficPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.ITrafficPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="trafficPolicyRef")
    def traffic_policy_ref(self) -> "TrafficPolicyReference":
        '''(experimental) A reference to a TrafficPolicy resource.

        :stability: experimental
        '''
        return typing.cast("TrafficPolicyReference", jsii.get(self, "trafficPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrafficPolicyRef).__jsii_proxy_class__ = lambda : _ITrafficPolicyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.KeySigningKeyReference",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone_id": "hostedZoneId",
        "key_signing_key_name": "keySigningKeyName",
    },
)
class KeySigningKeyReference:
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        key_signing_key_name: builtins.str,
    ) -> None:
        '''A reference to a KeySigningKey resource.

        :param hosted_zone_id: The HostedZoneId of the KeySigningKey resource.
        :param key_signing_key_name: The Name of the KeySigningKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            key_signing_key_reference = interfaces_route53.KeySigningKeyReference(
                hosted_zone_id="hostedZoneId",
                key_signing_key_name="keySigningKeyName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__740b6b79569b61714dbaad1664d38c2e457f5ba4d550ba6271197a8fd1b8e59d)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument key_signing_key_name", value=key_signing_key_name, expected_type=type_hints["key_signing_key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "key_signing_key_name": key_signing_key_name,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''The HostedZoneId of the KeySigningKey resource.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_signing_key_name(self) -> builtins.str:
        '''The Name of the KeySigningKey resource.'''
        result = self._values.get("key_signing_key_name")
        assert result is not None, "Required property 'key_signing_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeySigningKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.QueryLoggingConfigReference",
    jsii_struct_bases=[],
    name_mapping={"query_logging_config_arn": "queryLoggingConfigArn"},
)
class QueryLoggingConfigReference:
    def __init__(self, *, query_logging_config_arn: builtins.str) -> None:
        '''A reference to a QueryLoggingConfig resource.

        :param query_logging_config_arn: The Arn of the QueryLoggingConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            query_logging_config_reference = interfaces_route53.QueryLoggingConfigReference(
                query_logging_config_arn="queryLoggingConfigArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7f89b07174e4df1b7f17e2a6def5efe82f3108ce510b4a1c92079276cc44ff19)
            check_type(argname="argument query_logging_config_arn", value=query_logging_config_arn, expected_type=type_hints["query_logging_config_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_logging_config_arn": query_logging_config_arn,
        }

    @builtins.property
    def query_logging_config_arn(self) -> builtins.str:
        '''The Arn of the QueryLoggingConfig resource.'''
        result = self._values.get("query_logging_config_arn")
        assert result is not None, "Required property 'query_logging_config_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueryLoggingConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.RecordSetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"record_set_group_id": "recordSetGroupId"},
)
class RecordSetGroupReference:
    def __init__(self, *, record_set_group_id: builtins.str) -> None:
        '''A reference to a RecordSetGroup resource.

        :param record_set_group_id: The Id of the RecordSetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            record_set_group_reference = interfaces_route53.RecordSetGroupReference(
                record_set_group_id="recordSetGroupId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__843f82028bf43583ae47be1e10363ba4894e39f9bd7f71769ddfdced48189b19)
            check_type(argname="argument record_set_group_id", value=record_set_group_id, expected_type=type_hints["record_set_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_set_group_id": record_set_group_id,
        }

    @builtins.property
    def record_set_group_id(self) -> builtins.str:
        '''The Id of the RecordSetGroup resource.'''
        result = self._values.get("record_set_group_id")
        assert result is not None, "Required property 'record_set_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordSetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.RecordSetReference",
    jsii_struct_bases=[],
    name_mapping={"record_set_name": "recordSetName", "type": "type"},
)
class RecordSetReference:
    def __init__(self, *, record_set_name: builtins.str, type: builtins.str) -> None:
        '''A reference to a RecordSet resource.

        :param record_set_name: The Name of the RecordSet resource.
        :param type: The Type of the RecordSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            record_set_reference = interfaces_route53.RecordSetReference(
                record_set_name="recordSetName",
                type="type"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__309b4ebd3a2bc9de4559b92e46a6d5aa5ef18238d81d559d28fffaf3353eda80)
            check_type(argname="argument record_set_name", value=record_set_name, expected_type=type_hints["record_set_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_set_name": record_set_name,
            "type": type,
        }

    @builtins.property
    def record_set_name(self) -> builtins.str:
        '''The Name of the RecordSet resource.'''
        result = self._values.get("record_set_name")
        assert result is not None, "Required property 'record_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The Type of the RecordSet resource.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.TrafficPolicyInstanceReference",
    jsii_struct_bases=[],
    name_mapping={"traffic_policy_instance_arn": "trafficPolicyInstanceArn"},
)
class TrafficPolicyInstanceReference:
    def __init__(self, *, traffic_policy_instance_arn: builtins.str) -> None:
        '''A reference to a TrafficPolicyInstance resource.

        :param traffic_policy_instance_arn: The Arn of the TrafficPolicyInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            traffic_policy_instance_reference = interfaces_route53.TrafficPolicyInstanceReference(
                traffic_policy_instance_arn="trafficPolicyInstanceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__907cf5216db9b73f8bc0402dfbebacc12af955a2cd1397739b3cbaebf131aaa9)
            check_type(argname="argument traffic_policy_instance_arn", value=traffic_policy_instance_arn, expected_type=type_hints["traffic_policy_instance_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_policy_instance_arn": traffic_policy_instance_arn,
        }

    @builtins.property
    def traffic_policy_instance_arn(self) -> builtins.str:
        '''The Arn of the TrafficPolicyInstance resource.'''
        result = self._values.get("traffic_policy_instance_arn")
        assert result is not None, "Required property 'traffic_policy_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficPolicyInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.TrafficPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"traffic_policy_arn": "trafficPolicyArn"},
)
class TrafficPolicyReference:
    def __init__(self, *, traffic_policy_arn: builtins.str) -> None:
        '''A reference to a TrafficPolicy resource.

        :param traffic_policy_arn: The Arn of the TrafficPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            traffic_policy_reference = interfaces_route53.TrafficPolicyReference(
                traffic_policy_arn="trafficPolicyArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a690b715ddb12a54bd81e7afda640cce67b37a1f195ce6890c697023c76f67ea)
            check_type(argname="argument traffic_policy_arn", value=traffic_policy_arn, expected_type=type_hints["traffic_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_policy_arn": traffic_policy_arn,
        }

    @builtins.property
    def traffic_policy_arn(self) -> builtins.str:
        '''The Arn of the TrafficPolicy resource.'''
        result = self._values.get("traffic_policy_arn")
        assert result is not None, "Required property 'traffic_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CidrCollectionReference",
    "DNSSECReference",
    "DelegationSetReference",
    "HealthCheckReference",
    "HostedZoneReference",
    "ICidrCollectionRef",
    "IDNSSECRef",
    "IDelegationSetRef",
    "IHealthCheckRef",
    "IHostedZoneRef",
    "IKeySigningKeyRef",
    "IQueryLoggingConfigRef",
    "IRecordSetGroupRef",
    "IRecordSetRef",
    "ITrafficPolicyInstanceRef",
    "ITrafficPolicyRef",
    "KeySigningKeyReference",
    "QueryLoggingConfigReference",
    "RecordSetGroupReference",
    "RecordSetReference",
    "TrafficPolicyInstanceReference",
    "TrafficPolicyReference",
]

publication.publish()

def _typecheckingstub__a29c970e3dc59eb61f1e0e1c4183e889924847e040535cfbaa68366929f5a856(
    *,
    cidr_collection_arn: builtins.str,
    cidr_collection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5f748a2bea377e2fd2ed6d48058439646815e844893d9564084429051caf8f4(
    *,
    hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ea8bdca93efb6e0465035d00ee2a50843b0dabe0ffbcffba7146b6be994339(
    *,
    delegation_set_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a61fcf52d45a4375dfb1ae5d0b7b0555ae1091958107075e82bc35ca0d0275(
    *,
    health_check_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b4ca2affe8c503a8b4867d3e31a36ed15f0aa004cff0a9202da3d2bbbb7fe4c(
    *,
    hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740b6b79569b61714dbaad1664d38c2e457f5ba4d550ba6271197a8fd1b8e59d(
    *,
    hosted_zone_id: builtins.str,
    key_signing_key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f89b07174e4df1b7f17e2a6def5efe82f3108ce510b4a1c92079276cc44ff19(
    *,
    query_logging_config_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843f82028bf43583ae47be1e10363ba4894e39f9bd7f71769ddfdced48189b19(
    *,
    record_set_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309b4ebd3a2bc9de4559b92e46a6d5aa5ef18238d81d559d28fffaf3353eda80(
    *,
    record_set_name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__907cf5216db9b73f8bc0402dfbebacc12af955a2cd1397739b3cbaebf131aaa9(
    *,
    traffic_policy_instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a690b715ddb12a54bd81e7afda640cce67b37a1f195ce6890c697023c76f67ea(
    *,
    traffic_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICidrCollectionRef, IDNSSECRef, IDelegationSetRef, IHealthCheckRef, IHostedZoneRef, IKeySigningKeyRef, IQueryLoggingConfigRef, IRecordSetGroupRef, IRecordSetRef, ITrafficPolicyInstanceRef, ITrafficPolicyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
