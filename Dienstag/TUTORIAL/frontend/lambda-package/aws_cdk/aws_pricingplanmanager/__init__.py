r'''
# AWS::PricingPlanManager Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_pricingplanmanager as pricingplanmanager
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for PricingPlanManager construct libraries](https://constructs.dev/search?q=pricingplanmanager)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::PricingPlanManager resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PricingPlanManager.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::PricingPlanManager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PricingPlanManager.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
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


from .._jsii import *

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

    import aws_cdk as _aws_cdk_0cae9daa
    import aws_cdk.interfaces.aws_pricingplanmanager as _aws_pricingplanmanager_b613546d
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_pricingplanmanager_b613546d = _LazyImport("aws_cdk.interfaces.aws_pricingplanmanager")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_pricingplanmanager_b613546d.ISubscriptionRef)
class CfnSubscription(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pricingplanmanager.CfnSubscription",
):
    '''Resource type definition for AWS::PricingPlanManager::Subscription.

    Deleting an activated subscription does not terminate it immediately; it schedules a cancellation that takes effect at the end of the current billing period. Until that date the subscription remains active and billing continues. Deleting a subscription that has not yet been activated (PENDING_APPROVAL status) removes it immediately with no further charges.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pricingplanmanager-subscription.html
    :cloudformationResource: AWS::PricingPlanManager::Subscription
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pricingplanmanager as pricingplanmanager
        
        cfn_subscription = pricingplanmanager.CfnSubscription(self, "MyCfnSubscription",
            plan_family="planFamily",
            plan_tier="planTier",
            resource_arns=["resourceArns"],
        
            # the properties below are optional
            usage_level="usageLevel"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        plan_family: builtins.str,
        plan_tier: builtins.str,
        resource_arns: typing.Sequence[builtins.str],
        usage_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::PricingPlanManager::Subscription``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param plan_family: The name of the pricing plan family.
        :param plan_tier: The tier of the pricing plan. CloudFormation does not change the tier of an existing subscription; a stack update that changes the tier, upgrading or downgrading it, is rejected.
        :param resource_arns: The ARNs of resources associated with the subscription.
        :param usage_level: 
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d25e08da351cea3c41cf5ad39f89f1c42bd3210baa8ad98df13f72fe6ee56ac8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriptionProps(
            plan_family=plan_family,
            plan_tier=plan_tier,
            resource_arns=resource_arns,
            usage_level=usage_level,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSubscription")
    @builtins.classmethod
    def arn_for_subscription(
        cls,
        resource: "_aws_pricingplanmanager_b613546d.ISubscriptionRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fada87dadcd6905adaf78e242fbfdfb50463be8cd82964cc5eab4d6fbabffd92)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSubscription", [resource]))

    @jsii.member(jsii_name="isCfnSubscription")
    @builtins.classmethod
    def is_cfn_subscription(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSubscription.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3425388753190f42bb526cab857477f39ce13963b467cdba7cdaf35b4343fb67)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSubscription", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__93e2953d86857d56e1f89d967cc3223cb6766244e763a34f33d9ade56c39c17e)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__66862acfe804e965a4306f317088dc7e0b43eeace8f41a359baa411743d4789a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the subscription.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time the subscription was created, in ISO 8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCurrentPlanTier")
    def attr_current_plan_tier(self) -> builtins.str:
        '''The plan tier currently active on the subscription as reported by the API.

        Populated by the Read handler. Diverges from PlanTier after a non-reversible CloudFormation rollback; surface via drift detection.

        :cloudformationAttribute: CurrentPlanTier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCurrentPlanTier"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the subscription.

        PENDING_APPROVAL means a paid-tier subscription has been created but is not yet active and incurs no charges until it is approved out of band via a separate ApprovePaidSubscription call; CloudFormation never approves it. Free-tier subscriptions are activated immediately and do not use this status. ACTIVE means the subscription is in effect and, for paid tiers, billing has started. SYNC_IN_PROGRESS means a change is being applied. FAILED means provisioning did not complete; see StatusReason.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''A human-readable explanation of why the subscription is in its current status.

        Populated only when Status is FAILED, where it carries the reason the subscription could not be provisioned. Empty for all other statuses.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The time the subscription was last modified, in ISO 8601 format.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionRef")
    def subscription_ref(
        self,
    ) -> "_aws_pricingplanmanager_b613546d.SubscriptionReference":
        '''A reference to a Subscription resource.'''
        return typing.cast("_aws_pricingplanmanager_b613546d.SubscriptionReference", jsii.get(self, "subscriptionRef"))

    @builtins.property
    @jsii.member(jsii_name="planFamily")
    def plan_family(self) -> builtins.str:
        '''The name of the pricing plan family.'''
        return typing.cast(builtins.str, jsii.get(self, "planFamily"))

    @plan_family.setter
    def plan_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2264e4565d2d4d44c92ac482d1abca4e56a7ad39f2b5324e46eab75cc7fdf0bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "planFamily", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="planTier")
    def plan_tier(self) -> builtins.str:
        '''The tier of the pricing plan.'''
        return typing.cast(builtins.str, jsii.get(self, "planTier"))

    @plan_tier.setter
    def plan_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6e9f809cda0a88badeae8d937a4f8ea2bf227619f26816deceac90a4446c7c25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "planTier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of resources associated with the subscription.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceArns"))

    @resource_arns.setter
    def resource_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a39fdfdebc494ad5ca9c5f31f7927af341bed2fa1ae2e33ae02e20f6531a75a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="usageLevel")
    def usage_level(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageLevel"))

    @usage_level.setter
    def usage_level(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f54b40dddf5c2ac8ecc7cf7f4276637cc0539a0f7654de89b33c9be4140f8fbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usageLevel", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pricingplanmanager.CfnSubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "plan_family": "planFamily",
        "plan_tier": "planTier",
        "resource_arns": "resourceArns",
        "usage_level": "usageLevel",
    },
)
class CfnSubscriptionProps:
    def __init__(
        self,
        *,
        plan_family: builtins.str,
        plan_tier: builtins.str,
        resource_arns: typing.Sequence[builtins.str],
        usage_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscription``.

        :param plan_family: The name of the pricing plan family.
        :param plan_tier: The tier of the pricing plan. CloudFormation does not change the tier of an existing subscription; a stack update that changes the tier, upgrading or downgrading it, is rejected.
        :param resource_arns: The ARNs of resources associated with the subscription.
        :param usage_level: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pricingplanmanager-subscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pricingplanmanager as pricingplanmanager
            
            cfn_subscription_props = pricingplanmanager.CfnSubscriptionProps(
                plan_family="planFamily",
                plan_tier="planTier",
                resource_arns=["resourceArns"],
            
                # the properties below are optional
                usage_level="usageLevel"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ec5048a97b90cc3818afcd6adb730542673f5d6744df65ae3d56d9e033004a0f)
            check_type(argname="argument plan_family", value=plan_family, expected_type=type_hints["plan_family"])
            check_type(argname="argument plan_tier", value=plan_tier, expected_type=type_hints["plan_tier"])
            check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
            check_type(argname="argument usage_level", value=usage_level, expected_type=type_hints["usage_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "plan_family": plan_family,
            "plan_tier": plan_tier,
            "resource_arns": resource_arns,
        }
        if usage_level is not None:
            self._values["usage_level"] = usage_level

    @builtins.property
    def plan_family(self) -> builtins.str:
        '''The name of the pricing plan family.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pricingplanmanager-subscription.html#cfn-pricingplanmanager-subscription-planfamily
        '''
        result = self._values.get("plan_family")
        assert result is not None, "Required property 'plan_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plan_tier(self) -> builtins.str:
        '''The tier of the pricing plan.

        CloudFormation does not change the tier of an existing subscription; a stack update that changes the tier, upgrading or downgrading it, is rejected.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pricingplanmanager-subscription.html#cfn-pricingplanmanager-subscription-plantier
        '''
        result = self._values.get("plan_tier")
        assert result is not None, "Required property 'plan_tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of resources associated with the subscription.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pricingplanmanager-subscription.html#cfn-pricingplanmanager-subscription-resourcearns
        '''
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def usage_level(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pricingplanmanager-subscription.html#cfn-pricingplanmanager-subscription-usagelevel
        '''
        result = self._values.get("usage_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSubscription",
    "CfnSubscriptionProps",
]

publication.publish()

def _typecheckingstub__d25e08da351cea3c41cf5ad39f89f1c42bd3210baa8ad98df13f72fe6ee56ac8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    plan_family: builtins.str,
    plan_tier: builtins.str,
    resource_arns: typing.Sequence[builtins.str],
    usage_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fada87dadcd6905adaf78e242fbfdfb50463be8cd82964cc5eab4d6fbabffd92(
    resource: _aws_pricingplanmanager_b613546d.ISubscriptionRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3425388753190f42bb526cab857477f39ce13963b467cdba7cdaf35b4343fb67(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93e2953d86857d56e1f89d967cc3223cb6766244e763a34f33d9ade56c39c17e(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66862acfe804e965a4306f317088dc7e0b43eeace8f41a359baa411743d4789a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2264e4565d2d4d44c92ac482d1abca4e56a7ad39f2b5324e46eab75cc7fdf0bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e9f809cda0a88badeae8d937a4f8ea2bf227619f26816deceac90a4446c7c25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a39fdfdebc494ad5ca9c5f31f7927af341bed2fa1ae2e33ae02e20f6531a75a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f54b40dddf5c2ac8ecc7cf7f4276637cc0539a0f7654de89b33c9be4140f8fbc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5048a97b90cc3818afcd6adb730542673f5d6744df65ae3d56d9e033004a0f(
    *,
    plan_family: builtins.str,
    plan_tier: builtins.str,
    resource_arns: typing.Sequence[builtins.str],
    usage_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
