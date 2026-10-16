r'''
# S3 Bucket Notifications Destinations

This module includes integration classes for using Topics, Queues or Lambdas
as S3 Notification Destinations.

## Examples

The following example shows how to send a notification to an SNS
topic when an object is created in an S3 bucket:

```python
import aws_cdk.aws_sns as sns


bucket = s3.Bucket(self, "Bucket")
topic = sns.Topic(self, "Topic")

bucket.add_event_notification(s3.EventType.OBJECT_CREATED_PUT, s3n.SnsDestination(topic))
```

The following example shows how to send a notification to an SQS queue
when an object is created in an S3 bucket:

```python
import aws_cdk.aws_sqs as sqs


bucket = s3.Bucket(self, "Bucket")
queue = sqs.Queue(self, "Queue")

bucket.add_event_notification(s3.EventType.OBJECT_CREATED_PUT, s3n.SqsDestination(queue))
```

The following example shows how to send a notification to a Lambda function when an object is created in an S3 bucket:

```python
import aws_cdk.aws_lambda as lambda_


bucket = s3.Bucket(self, "Bucket")
fn = lambda_.Function(self, "MyFunction",
    runtime=lambda_.Runtime.NODEJS_LATEST,
    handler="index.handler",
    code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler"))
)

bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(fn))
```
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

    import aws_cdk.aws_lambda as _aws_lambda_b8f2f472
    import aws_cdk.aws_s3 as _aws_s3_01158f40
    import aws_cdk.aws_sns as _aws_sns_07ffc8ab
    import aws_cdk.aws_sqs as _aws_sqs_24ab9de4
    import aws_cdk.interfaces.aws_s3 as _aws_s3_03fe213b
    import constructs as _constructs_77d1e7e8
else:

    _aws_lambda_b8f2f472 = _LazyImport("aws_cdk.aws_lambda")
    _aws_s3_01158f40 = _LazyImport("aws_cdk.aws_s3")
    _aws_s3_03fe213b = _LazyImport("aws_cdk.interfaces.aws_s3")
    _aws_sns_07ffc8ab = _LazyImport("aws_cdk.aws_sns")
    _aws_sqs_24ab9de4 = _LazyImport("aws_cdk.aws_sqs")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_s3_01158f40.IBucketNotificationDestination)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_notifications.LambdaDestination",
):
    '''Use a Lambda function as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        # my_lambda: lambda.Function
        
        bucket = s3.Bucket.from_bucket_attributes(self, "ImportedBucket",
            bucket_arn="arn:aws:s3:::amzn-s3-demo-bucket"
        )
        
        # now you can just call methods on the bucket
        filter = s3.NotificationKeyFilter(prefix="home/myusername/*")
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(my_lambda), filter)
    '''

    def __init__(self, fn: "_aws_lambda_b8f2f472.IFunction") -> None:
        '''
        :param fn: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aa31f009d508c5e9716ef8081ccf63abb6866ffbf349417ea81abf6f60c25acc)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        jsii.create(self.__class__, self, [fn])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        bucket: "_aws_s3_03fe213b.IBucketRef",
    ) -> "_aws_s3_01158f40.BucketNotificationDestinationConfig":
        '''Registers this resource to receive notifications for the specified bucket.

        This method will only be called once for each destination/bucket
        pair and the result will be cached, so there is no need to implement
        idempotency in each destination.

        :param scope: -
        :param bucket: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__72fb0e43c5d0bdebbc9b643b327c5cd42f851dbe4c4a6ac53bb2849787b3adec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast("_aws_s3_01158f40.BucketNotificationDestinationConfig", jsii.invoke(self, "bind", [scope, bucket]))


@jsii.implements(_aws_s3_01158f40.IBucketNotificationDestination)
class SnsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_notifications.SnsDestination",
):
    '''Use an SNS topic as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        bucket = s3.Bucket(self, "MyBucket")
        topic = sns.Topic(self, "MyTopic")
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.SnsDestination(topic))
    '''

    def __init__(self, topic: "_aws_sns_07ffc8ab.ITopic") -> None:
        '''
        :param topic: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__88bc302a2eb7b4d1c7dc00b1564ab4c536d2626942f2cec60d543582b3f80f43)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        jsii.create(self.__class__, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        bucket: "_aws_s3_03fe213b.IBucketRef",
    ) -> "_aws_s3_01158f40.BucketNotificationDestinationConfig":
        '''Registers this resource to receive notifications for the specified bucket.

        This method will only be called once for each destination/bucket
        pair and the result will be cached, so there is no need to implement
        idempotency in each destination.

        :param scope: -
        :param bucket: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3553ece4b599ce7e526b55722477cb04771e1907840471521f08a9dbdea726a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast("_aws_s3_01158f40.BucketNotificationDestinationConfig", jsii.invoke(self, "bind", [scope, bucket]))


@jsii.implements(_aws_s3_01158f40.IBucketNotificationDestination)
class SqsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_notifications.SqsDestination",
):
    '''Use an SQS queue as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        # my_queue: sqs.Queue
        
        bucket = s3.Bucket(self, "MyBucket",
            notifications_skip_destination_validation=True
        )
        bucket.add_event_notification(s3.EventType.OBJECT_REMOVED, s3n.SqsDestination(my_queue))
    '''

    def __init__(self, queue: "_aws_sqs_24ab9de4.IQueue") -> None:
        '''
        :param queue: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b615fa89f2fab6db113bd6376cf27eba6eb754a702e60b29024bc94c89bac4c6)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        jsii.create(self.__class__, self, [queue])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: "_constructs_77d1e7e8.Construct",
        bucket: "_aws_s3_03fe213b.IBucketRef",
    ) -> "_aws_s3_01158f40.BucketNotificationDestinationConfig":
        '''Allows using SQS queues as destinations for bucket notifications.

        Use ``bucket.onEvent(event, queue)`` to subscribe.

        :param _scope: -
        :param bucket: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e60900d91c64bba2d0ee8f8b0ace07ff0ee2d07e518d7b03941ed5bb85044f8b)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast("_aws_s3_01158f40.BucketNotificationDestinationConfig", jsii.invoke(self, "bind", [_scope, bucket]))


__all__ = [
    "LambdaDestination",
    "SnsDestination",
    "SqsDestination",
]

publication.publish()

def _typecheckingstub__aa31f009d508c5e9716ef8081ccf63abb6866ffbf349417ea81abf6f60c25acc(
    fn: _aws_lambda_b8f2f472.IFunction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72fb0e43c5d0bdebbc9b643b327c5cd42f851dbe4c4a6ac53bb2849787b3adec(
    scope: _constructs_77d1e7e8.Construct,
    bucket: _aws_s3_03fe213b.IBucketRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88bc302a2eb7b4d1c7dc00b1564ab4c536d2626942f2cec60d543582b3f80f43(
    topic: _aws_sns_07ffc8ab.ITopic,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3553ece4b599ce7e526b55722477cb04771e1907840471521f08a9dbdea726a1(
    scope: _constructs_77d1e7e8.Construct,
    bucket: _aws_s3_03fe213b.IBucketRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b615fa89f2fab6db113bd6376cf27eba6eb754a702e60b29024bc94c89bac4c6(
    queue: _aws_sqs_24ab9de4.IQueue,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e60900d91c64bba2d0ee8f8b0ace07ff0ee2d07e518d7b03941ed5bb85044f8b(
    _scope: _constructs_77d1e7e8.Construct,
    bucket: _aws_s3_03fe213b.IBucketRef,
) -> None:
    """Type checking stubs"""
    pass
