r'''
# Lifecycle Hook for the CDK AWS AutoScaling Library

This library contains integration classes for AutoScaling lifecycle hooks.
Instances of these classes should be passed to the
`autoScalingGroup.addLifecycleHook()` method.

Lifecycle hooks can be activated in one of the following ways:

* Invoke a Lambda function
* Publish to an SNS topic
* Send to an SQS queue

For more information on using this library, see the README of the
`aws-cdk-lib/aws-autoscaling` library.

For more information about lifecycle hooks, see
[Amazon EC2 AutoScaling Lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the Amazon EC2 User Guide.
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

    import aws_cdk.aws_autoscaling as _aws_autoscaling_6cbf8045
    import aws_cdk.aws_iam as _aws_iam_1f54b5e8
    import aws_cdk.aws_kms as _aws_kms_ff87d74a
    import aws_cdk.aws_lambda as _aws_lambda_b8f2f472
    import aws_cdk.aws_sns as _aws_sns_07ffc8ab
    import aws_cdk.aws_sqs as _aws_sqs_24ab9de4
    import constructs as _constructs_77d1e7e8
else:

    _aws_autoscaling_6cbf8045 = _LazyImport("aws_cdk.aws_autoscaling")
    _aws_iam_1f54b5e8 = _LazyImport("aws_cdk.aws_iam")
    _aws_kms_ff87d74a = _LazyImport("aws_cdk.aws_kms")
    _aws_lambda_b8f2f472 = _LazyImport("aws_cdk.aws_lambda")
    _aws_sns_07ffc8ab = _LazyImport("aws_cdk.aws_sns")
    _aws_sqs_24ab9de4 = _LazyImport("aws_cdk.aws_sqs")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_autoscaling_6cbf8045.ILifecycleHookTarget)
class FunctionHook(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_autoscaling_hooktargets.FunctionHook",
):
    '''Use a Lambda Function as a hook target.

    Internally creates a Topic to make the connection.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_autoscaling_hooktargets as autoscaling_hooktargets
        from aws_cdk import aws_kms as kms
        from aws_cdk import aws_lambda as lambda_
        
        # function_: lambda.Function
        # key: kms.Key
        
        function_hook = autoscaling_hooktargets.FunctionHook(function_, key)
    '''

    def __init__(
        self,
        fn: "_aws_lambda_b8f2f472.IFunction",
        encryption_key: typing.Optional["_aws_kms_ff87d74a.IKey"] = None,
    ) -> None:
        '''
        :param fn: Function to invoke in response to a lifecycle event.
        :param encryption_key: If provided, this key is used to encrypt the contents of the SNS topic.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__11dcc9863508c86117da29136549f0f23288cfd7a8d35f6f4980025ba69666f7)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
        jsii.create(self.__class__, self, [fn, encryption_key])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: "_constructs_77d1e7e8.Construct",
        *,
        lifecycle_hook: "_aws_autoscaling_6cbf8045.LifecycleHook",
        role: typing.Optional["_aws_iam_1f54b5e8.IRole"] = None,
    ) -> "_aws_autoscaling_6cbf8045.LifecycleHookTargetConfig":
        '''If the ``IRole`` does not exist in ``options``, will create an ``IRole`` and an SNS Topic and attach both to the lifecycle hook.

        If the ``IRole`` does exist in ``options``, will only create an SNS Topic and attach it to the lifecycle hook.

        :param _scope: -
        :param lifecycle_hook: The lifecycle hook to attach to. [disable-awslint:ref-via-interface]
        :param role: The role to use when attaching to the lifecycle hook. [disable-awslint:ref-via-interface] Default: : a role is not created unless the target arn is specified
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__87a0acf1a42ca54c117fbcf45b0c52a26bb2743ce4db48155ab9037da392189b)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        options = _aws_autoscaling_6cbf8045.BindHookTargetOptions(
            lifecycle_hook=lifecycle_hook, role=role
        )

        return typing.cast("_aws_autoscaling_6cbf8045.LifecycleHookTargetConfig", jsii.invoke(self, "bind", [_scope, options]))


@jsii.implements(_aws_autoscaling_6cbf8045.ILifecycleHookTarget)
class QueueHook(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_autoscaling_hooktargets.QueueHook",
):
    '''Use an SQS queue as a hook target.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_autoscaling_hooktargets as autoscaling_hooktargets
        from aws_cdk import aws_sqs as sqs
        
        # queue: sqs.Queue
        
        queue_hook = autoscaling_hooktargets.QueueHook(queue)
    '''

    def __init__(self, queue: "_aws_sqs_24ab9de4.IQueue") -> None:
        '''
        :param queue: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6a27ba4aae9f6814c160ec18cf273dfebbbe3de9d8ed316d4b35807460d0a0fb)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        jsii.create(self.__class__, self, [queue])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: "_constructs_77d1e7e8.Construct",
        *,
        lifecycle_hook: "_aws_autoscaling_6cbf8045.LifecycleHook",
        role: typing.Optional["_aws_iam_1f54b5e8.IRole"] = None,
    ) -> "_aws_autoscaling_6cbf8045.LifecycleHookTargetConfig":
        '''If an ``IRole`` is found in ``options``, grant it access to send messages.

        Otherwise, create a new ``IRole`` and grant it access to send messages.

        :param _scope: -
        :param lifecycle_hook: The lifecycle hook to attach to. [disable-awslint:ref-via-interface]
        :param role: The role to use when attaching to the lifecycle hook. [disable-awslint:ref-via-interface] Default: : a role is not created unless the target arn is specified

        :return: the ``IRole`` with access to send messages and the ARN of the queue it has access to send messages to.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__390c58e3c226b06273db2640e33a6c80d5f0edfea4afc87a87c39de5c4aa8a18)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        options = _aws_autoscaling_6cbf8045.BindHookTargetOptions(
            lifecycle_hook=lifecycle_hook, role=role
        )

        return typing.cast("_aws_autoscaling_6cbf8045.LifecycleHookTargetConfig", jsii.invoke(self, "bind", [_scope, options]))


@jsii.implements(_aws_autoscaling_6cbf8045.ILifecycleHookTarget)
class TopicHook(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_autoscaling_hooktargets.TopicHook",
):
    '''Use an SNS topic as a hook target.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_autoscaling_hooktargets as autoscaling_hooktargets
        from aws_cdk import aws_sns as sns
        
        # topic: sns.Topic
        
        topic_hook = autoscaling_hooktargets.TopicHook(topic)
    '''

    def __init__(self, topic: "_aws_sns_07ffc8ab.ITopic") -> None:
        '''
        :param topic: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0c04a924ccffcd9b9b114916cc17d30561c7914ac51c2927bb9a14d8932f477c)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        jsii.create(self.__class__, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: "_constructs_77d1e7e8.Construct",
        *,
        lifecycle_hook: "_aws_autoscaling_6cbf8045.LifecycleHook",
        role: typing.Optional["_aws_iam_1f54b5e8.IRole"] = None,
    ) -> "_aws_autoscaling_6cbf8045.LifecycleHookTargetConfig":
        '''If an ``IRole`` is found in ``options``, grant it topic publishing permissions.

        Otherwise, create a new ``IRole`` and grant it topic publishing permissions.

        :param _scope: -
        :param lifecycle_hook: The lifecycle hook to attach to. [disable-awslint:ref-via-interface]
        :param role: The role to use when attaching to the lifecycle hook. [disable-awslint:ref-via-interface] Default: : a role is not created unless the target arn is specified

        :return: the ``IRole`` with topic publishing permissions and the ARN of the topic it has publishing permission to.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9f93d65b58ecdfdd2691a7dbd634608337e3a3fb21dc00b4564ced3f039f7cf8)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        options = _aws_autoscaling_6cbf8045.BindHookTargetOptions(
            lifecycle_hook=lifecycle_hook, role=role
        )

        return typing.cast("_aws_autoscaling_6cbf8045.LifecycleHookTargetConfig", jsii.invoke(self, "bind", [_scope, options]))


__all__ = [
    "FunctionHook",
    "QueueHook",
    "TopicHook",
]

publication.publish()

def _typecheckingstub__11dcc9863508c86117da29136549f0f23288cfd7a8d35f6f4980025ba69666f7(
    fn: _aws_lambda_b8f2f472.IFunction,
    encryption_key: typing.Optional[_aws_kms_ff87d74a.IKey] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a0acf1a42ca54c117fbcf45b0c52a26bb2743ce4db48155ab9037da392189b(
    _scope: _constructs_77d1e7e8.Construct,
    *,
    lifecycle_hook: _aws_autoscaling_6cbf8045.LifecycleHook,
    role: typing.Optional[_aws_iam_1f54b5e8.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a27ba4aae9f6814c160ec18cf273dfebbbe3de9d8ed316d4b35807460d0a0fb(
    queue: _aws_sqs_24ab9de4.IQueue,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390c58e3c226b06273db2640e33a6c80d5f0edfea4afc87a87c39de5c4aa8a18(
    _scope: _constructs_77d1e7e8.Construct,
    *,
    lifecycle_hook: _aws_autoscaling_6cbf8045.LifecycleHook,
    role: typing.Optional[_aws_iam_1f54b5e8.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c04a924ccffcd9b9b114916cc17d30561c7914ac51c2927bb9a14d8932f477c(
    topic: _aws_sns_07ffc8ab.ITopic,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f93d65b58ecdfdd2691a7dbd634608337e3a3fb21dc00b4564ced3f039f7cf8(
    _scope: _constructs_77d1e7e8.Construct,
    *,
    lifecycle_hook: _aws_autoscaling_6cbf8045.LifecycleHook,
    role: typing.Optional[_aws_iam_1f54b5e8.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass
