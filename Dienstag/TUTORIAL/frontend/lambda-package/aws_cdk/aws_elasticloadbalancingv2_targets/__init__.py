r'''
# Targets for AWS Elastic Load Balancing V2

This package contains targets for ELBv2. See the README of the `aws-cdk-lib/aws-elasticloadbalancingv2` library.
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

    import aws_cdk.aws_ec2 as _aws_ec2_09840e12
    import aws_cdk.aws_elasticloadbalancingv2 as _aws_elasticloadbalancingv2_1d9af53a
    import aws_cdk.aws_lambda as _aws_lambda_b8f2f472
else:

    _aws_ec2_09840e12 = _LazyImport("aws_cdk.aws_ec2")
    _aws_elasticloadbalancingv2_1d9af53a = _LazyImport("aws_cdk.aws_elasticloadbalancingv2")
    _aws_lambda_b8f2f472 = _LazyImport("aws_cdk.aws_lambda")


@jsii.implements(_aws_elasticloadbalancingv2_1d9af53a.INetworkLoadBalancerTarget)
class AlbArnTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.AlbArnTarget",
):
    '''A single Application Load Balancer as the target for load balancing.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        alb_arn_target = elasticloadbalancingv2_targets.AlbArnTarget("albArn", 123)
    '''

    def __init__(self, alb_arn: builtins.str, port: jsii.Number) -> None:
        '''Create a new alb target.

        Note that the ALB must have a listener on the provided target port.

        :param alb_arn: The ARN of the application load balancer to load balance to.
        :param port: The port on which the target is listening.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__25d70f2793026e068f7401c24a9086fabd06f88513447495a5230201e1c35f0b)
            check_type(argname="argument alb_arn", value=alb_arn, expected_type=type_hints["alb_arn"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [alb_arn, port])

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: "_aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup",
    ) -> "_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps":
        '''Register this alb target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0ea49d3d21e7fdd26737ad142510132a0b92aad60fc05d121077fff9d7ef5770)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast("_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps", jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


class AlbListenerTarget(
    AlbArnTarget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.AlbListenerTarget",
):
    '''A single Application Load Balancer's listener as the target for load balancing.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_elasticloadbalancingv2_targets as targets
        import aws_cdk.aws_ecs as ecs
        import aws_cdk.aws_ecs_patterns as patterns
        
        # vpc: ec2.Vpc
        
        
        task = ecs.FargateTaskDefinition(self, "Task", cpu=256, memory_limit_mi_b=512)
        task.add_container("nginx",
            image=ecs.ContainerImage.from_registry("public.ecr.aws/nginx/nginx:latest"),
            port_mappings=[ecs.PortMapping(container_port=80)]
        )
        
        svc = patterns.ApplicationLoadBalancedFargateService(self, "Service",
            vpc=vpc,
            task_definition=task,
            public_load_balancer=False
        )
        
        nlb = elbv2.NetworkLoadBalancer(self, "Nlb",
            vpc=vpc,
            cross_zone_enabled=True,
            internet_facing=True
        )
        
        listener = nlb.add_listener("listener", port=80)
        
        listener.add_targets("Targets",
            targets=[targets.AlbListenerTarget(svc.listener)],
            port=80
        )
        
        CfnOutput(self, "NlbEndpoint", value=f"http://{nlb.loadBalancerDnsName}")
    '''

    def __init__(
        self,
        alb_listener: "_aws_elasticloadbalancingv2_1d9af53a.ApplicationListener",
    ) -> None:
        '''Create a new ALB target.

        The associated target group will automatically have a dependency added
        against the ALB's listener.

        :param alb_listener: The application load balancer listener to target.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e31939d2001b9f2d9173770d02a5f42f518e7fc30f18b8d5d9c1ae30cd215337)
            check_type(argname="argument alb_listener", value=alb_listener, expected_type=type_hints["alb_listener"])
        jsii.create(self.__class__, self, [alb_listener])

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: "_aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup",
    ) -> "_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps":
        '''Register this ALB target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        This adds dependency on albListener because creation of ALB listener and NLB can vary during runtime.
        More Details on - https://github.com/aws/aws-cdk/issues/17208

        :param target_group: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__20a98e4d36be7fd597fbdb5dc2eb39c596b74bb2f49614c2332d5ae90c821450)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast("_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps", jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


class AlbTarget(
    AlbArnTarget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.AlbTarget",
):
    '''(deprecated) A single Application Load Balancer as the target for load balancing.

    :deprecated:

    Use ``AlbListenerTarget`` instead or
    ``AlbArnTarget`` for an imported load balancer. This target does not automatically
    add a dependency between the ALB listener and resulting NLB target group,
    without which may cause stack deployments to fail if the NLB target group is provisioned
    before the listener has been fully created.

    :stability: deprecated
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticloadbalancingv2 as elbv2
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        # application_load_balancer_ref: elbv2.IApplicationLoadBalancerRef
        
        alb_target = elasticloadbalancingv2_targets.AlbTarget(application_load_balancer_ref, 123)
    '''

    def __init__(
        self,
        alb: "_aws_elasticloadbalancingv2_1d9af53a.IApplicationLoadBalancerRef",
        port: jsii.Number,
    ) -> None:
        '''
        :param alb: The application load balancer to load balance to.
        :param port: The port on which the target is listening.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bd3c46777bea3cc0051ec19e4d49e906dc65667b0e86f1104c7ed8f70dc67e80)
            check_type(argname="argument alb", value=alb, expected_type=type_hints["alb"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [alb, port])


@jsii.implements(_aws_elasticloadbalancingv2_1d9af53a.IApplicationLoadBalancerTarget, _aws_elasticloadbalancingv2_1d9af53a.INetworkLoadBalancerTarget)
class InstanceIdTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.InstanceIdTarget",
):
    '''An EC2 instance that is the target for load balancing.

    If you register a target of this type, you are responsible for making
    sure the load balancer's security group can connect to the instance.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        instance_id_target = elasticloadbalancingv2_targets.InstanceIdTarget("instanceId", 123)
    '''

    def __init__(
        self,
        instance_id: builtins.str,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new Instance target.

        :param instance_id: Instance ID of the instance to register to.
        :param port: Override the default port for the target group.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1b3820af24c8d0caf9d54065ac5cda2ca9979ee90fbb15f9f692a3542160b38b)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [instance_id, port])

    @jsii.member(jsii_name="attachToApplicationTargetGroup")
    def attach_to_application_target_group(
        self,
        target_group: "_aws_elasticloadbalancingv2_1d9af53a.IApplicationTargetGroup",
    ) -> "_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps":
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3e70e7ee18a71770eaa08504d84271779a0a58094edefcc8ce3216dc7e9b68be)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast("_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps", jsii.invoke(self, "attachToApplicationTargetGroup", [target_group]))

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: "_aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup",
    ) -> "_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps":
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2c0af4f33601944860c7afb8bd7b24a7ae7f810bbfad86781e7210eacdf47b0a)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast("_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps", jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


class InstanceTarget(
    InstanceIdTarget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.InstanceTarget",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ec2 as ec2
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        # instance: ec2.Instance
        
        instance_target = elasticloadbalancingv2_targets.InstanceTarget(instance, 123)
    '''

    def __init__(
        self,
        instance: "_aws_ec2_09840e12.Instance",
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new Instance target.

        :param instance: Instance to register to.
        :param port: Override the default port for the target group.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d0b0a387fdd5384869920ca6a60983b93293d68a187d248cc55a87ec55602502)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [instance, port])


@jsii.implements(_aws_elasticloadbalancingv2_1d9af53a.IApplicationLoadBalancerTarget, _aws_elasticloadbalancingv2_1d9af53a.INetworkLoadBalancerTarget)
class IpTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.IpTarget",
):
    '''An IP address that is a target for load balancing.

    Specify IP addresses from the subnets of the virtual private cloud (VPC) for
    the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and
    192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify
    publicly routable IP addresses.

    If you register a target of this type, you are responsible for making
    sure the load balancer's security group can send packets to the IP address.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        ip_target = elasticloadbalancingv2_targets.IpTarget("ipAddress", 123, "availabilityZone")
    '''

    def __init__(
        self,
        ip_address: builtins.str,
        port: typing.Optional[jsii.Number] = None,
        availability_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new IPAddress target.

        The availabilityZone parameter determines whether the target receives
        traffic from the load balancer nodes in the specified Availability Zone
        or from all enabled Availability Zones for the load balancer.

        This parameter is not supported if the target type of the target group
        is instance. If the IP address is in a subnet of the VPC for the target
        group, the Availability Zone is automatically detected and this
        parameter is optional. If the IP address is outside the VPC, this
        parameter is required.

        With an Application Load Balancer, if the IP address is outside the VPC
        for the target group, the only supported value is all.

        Default is automatic.

        :param ip_address: The IP Address to load balance to.
        :param port: Override the group's default port.
        :param availability_zone: Availability zone to send traffic from.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ce293fbbbc943f4efe7d581fe7eec34ab650ed64fb91ba63a9a9f352c105579e)
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
        jsii.create(self.__class__, self, [ip_address, port, availability_zone])

    @jsii.member(jsii_name="attachToApplicationTargetGroup")
    def attach_to_application_target_group(
        self,
        target_group: "_aws_elasticloadbalancingv2_1d9af53a.IApplicationTargetGroup",
    ) -> "_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps":
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3a9a376c8ed3a883a27f4ae60ca1aec9ad984e59f8e7fa8a170556c3f7fe55e5)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast("_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps", jsii.invoke(self, "attachToApplicationTargetGroup", [target_group]))

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: "_aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup",
    ) -> "_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps":
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__069f34c3f18be180bdb72c9a996b9bd91047c65c9c1cf353e7587ca71c38032a)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast("_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps", jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


@jsii.implements(_aws_elasticloadbalancingv2_1d9af53a.IApplicationLoadBalancerTarget)
class LambdaTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.LambdaTarget",
):
    '''
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        import aws_cdk.aws_elasticloadbalancingv2_targets as targets
        
        # lambda_function: lambda.Function
        # lb: elbv2.ApplicationLoadBalancer
        
        
        listener = lb.add_listener("Listener", port=80)
        listener.add_targets("Targets",
            targets=[targets.LambdaTarget(lambda_function)],
        
            # For Lambda Targets, you need to explicitly enable health checks if you
            # want them.
            health_check=elbv2.HealthCheck(
                enabled=True
            )
        )
    '''

    def __init__(self, fn: "_aws_lambda_b8f2f472.IFunction") -> None:
        '''Create a new Lambda target.

        :param fn: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5275fd84f4406ac6b5a4f40a26b3d677ee61e71807bc8aeac8ac506eccc3bc3b)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        jsii.create(self.__class__, self, [fn])

    @jsii.member(jsii_name="attachToApplicationTargetGroup")
    def attach_to_application_target_group(
        self,
        target_group: "_aws_elasticloadbalancingv2_1d9af53a.IApplicationTargetGroup",
    ) -> "_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps":
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8b190f4c5fe7b990d3e274ecebf1188f5d7b6279fa49c8d06b07414c2348d886)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast("_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps", jsii.invoke(self, "attachToApplicationTargetGroup", [target_group]))

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: "_aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup",
    ) -> "_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps":
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a2f6c60936adbb8b62de293ba6e14e2a54ee5b179f71c61e5f73cca4e987d14a)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast("_aws_elasticloadbalancingv2_1d9af53a.LoadBalancerTargetProps", jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


__all__ = [
    "AlbArnTarget",
    "AlbListenerTarget",
    "AlbTarget",
    "InstanceIdTarget",
    "InstanceTarget",
    "IpTarget",
    "LambdaTarget",
]

publication.publish()

def _typecheckingstub__25d70f2793026e068f7401c24a9086fabd06f88513447495a5230201e1c35f0b(
    alb_arn: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea49d3d21e7fdd26737ad142510132a0b92aad60fc05d121077fff9d7ef5770(
    target_group: _aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e31939d2001b9f2d9173770d02a5f42f518e7fc30f18b8d5d9c1ae30cd215337(
    alb_listener: _aws_elasticloadbalancingv2_1d9af53a.ApplicationListener,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a98e4d36be7fd597fbdb5dc2eb39c596b74bb2f49614c2332d5ae90c821450(
    target_group: _aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3c46777bea3cc0051ec19e4d49e906dc65667b0e86f1104c7ed8f70dc67e80(
    alb: _aws_elasticloadbalancingv2_1d9af53a.IApplicationLoadBalancerRef,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b3820af24c8d0caf9d54065ac5cda2ca9979ee90fbb15f9f692a3542160b38b(
    instance_id: builtins.str,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e70e7ee18a71770eaa08504d84271779a0a58094edefcc8ce3216dc7e9b68be(
    target_group: _aws_elasticloadbalancingv2_1d9af53a.IApplicationTargetGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c0af4f33601944860c7afb8bd7b24a7ae7f810bbfad86781e7210eacdf47b0a(
    target_group: _aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0b0a387fdd5384869920ca6a60983b93293d68a187d248cc55a87ec55602502(
    instance: _aws_ec2_09840e12.Instance,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce293fbbbc943f4efe7d581fe7eec34ab650ed64fb91ba63a9a9f352c105579e(
    ip_address: builtins.str,
    port: typing.Optional[jsii.Number] = None,
    availability_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a9a376c8ed3a883a27f4ae60ca1aec9ad984e59f8e7fa8a170556c3f7fe55e5(
    target_group: _aws_elasticloadbalancingv2_1d9af53a.IApplicationTargetGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069f34c3f18be180bdb72c9a996b9bd91047c65c9c1cf353e7587ca71c38032a(
    target_group: _aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5275fd84f4406ac6b5a4f40a26b3d677ee61e71807bc8aeac8ac506eccc3bc3b(
    fn: _aws_lambda_b8f2f472.IFunction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b190f4c5fe7b990d3e274ecebf1188f5d7b6279fa49c8d06b07414c2348d886(
    target_group: _aws_elasticloadbalancingv2_1d9af53a.IApplicationTargetGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2f6c60936adbb8b62de293ba6e14e2a54ee5b179f71c61e5f73cca4e987d14a(
    target_group: _aws_elasticloadbalancingv2_1d9af53a.INetworkTargetGroup,
) -> None:
    """Type checking stubs"""
    pass
