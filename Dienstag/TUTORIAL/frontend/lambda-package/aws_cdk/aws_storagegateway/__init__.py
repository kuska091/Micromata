r'''
# AWS::StorageGateway Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_storagegateway as storagegateway
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for StorageGateway construct libraries](https://constructs.dev/search?q=storagegateway)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::StorageGateway resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_StorageGateway.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::StorageGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_StorageGateway.html).

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
    import aws_cdk.interfaces.aws_storagegateway as _aws_storagegateway_f426d4c4
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_storagegateway_f426d4c4 = _LazyImport("aws_cdk.interfaces.aws_storagegateway")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_storagegateway_f426d4c4.ITapeRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnTape(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_storagegateway.CfnTape",
):
    '''Creates a virtual tape with a user-defined barcode on a Tape Gateway (VTL).

    A virtual tape is stored in Amazon S3 and can be archived to S3 Glacier or S3 Glacier Deep Archive.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html
    :cloudformationResource: AWS::StorageGateway::Tape
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_storagegateway as storagegateway
        
        cfn_tape = storagegateway.CfnTape(self, "MyCfnTape",
            gateway_arn="gatewayArn",
            tape_size_in_bytes=123,
        
            # the properties below are optional
            kms_encrypted=False,
            kms_key="kmsKey",
            pool_id="poolId",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            tape_barcode="tapeBarcode",
            worm=False
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        gateway_arn: builtins.str,
        tape_size_in_bytes: jsii.Number,
        kms_encrypted: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        kms_key: typing.Optional[builtins.str] = None,
        pool_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        tape_barcode: typing.Optional[builtins.str] = None,
        worm: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
    ) -> None:
        '''Create a new ``AWS::StorageGateway::Tape``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param gateway_arn: The Amazon Resource Name (ARN) of the Tape Gateway that hosts the virtual tape.
        :param tape_size_in_bytes: The size, in bytes, of the virtual tape that you want to create.
        :param kms_encrypted: Set to true to use Amazon S3 server-side encryption with your own KMS key, or false to use a key managed by Amazon S3. Optional.
        :param kms_key: The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. This value must be set if KMSEncrypted is true.
        :param pool_id: The ID of the pool that you want to add your tape to for archiving. Tapes in this pool are archived in the S3 storage class that is associated with the pool.
        :param tags: A list of up to 50 tags to assign to the virtual tape.
        :param tape_barcode: The barcode that you want to assign to the virtual tape. Barcodes cannot be reused, even after a tape is deleted.
        :param worm: Set to true to create a write-once-read-many (WORM) virtual tape.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__363b2f7813c184123160ffaf59a488211565913fb5126a1fa69bcb36310d32dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTapeProps(
            gateway_arn=gateway_arn,
            tape_size_in_bytes=tape_size_in_bytes,
            kms_encrypted=kms_encrypted,
            kms_key=kms_key,
            pool_id=pool_id,
            tags=tags,
            tape_barcode=tape_barcode,
            worm=worm,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForTape")
    @builtins.classmethod
    def arn_for_tape(
        cls,
        resource: "_aws_storagegateway_f426d4c4.ITapeRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ae610be3890fbb42584972211b0c5af3006370462c1bf3c6c3b219eb44a03b39)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForTape", [resource]))

    @jsii.member(jsii_name="isCfnTape")
    @builtins.classmethod
    def is_cfn_tape(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTape.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ebb8f5d769e86e9451e9c5e5b3470e03b5d0dfb0c67afc78fc0e8c2598c707dd)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTape", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bd33548844c3c66482e5960a6a6f61789c9af04eb374db35a888509e0a56ab58)
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
            type_hints = cached_type_hints(_typecheckingstub__7ae0da0b888c3ffbaa5eb6cd82d55bf20a66d98c9c309e38a2589910332683ed)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTapeArn")
    def attr_tape_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the virtual tape.

        :cloudformationAttribute: TapeARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTapeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTapeCreatedDate")
    def attr_tape_created_date(self) -> builtins.str:
        '''The date and time that the virtual tape was created.

        :cloudformationAttribute: TapeCreatedDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTapeCreatedDate"))

    @builtins.property
    @jsii.member(jsii_name="attrTapeStatus")
    def attr_tape_status(self) -> builtins.str:
        '''The current status of the virtual tape.

        :cloudformationAttribute: TapeStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTapeStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTapeUsedInBytes")
    def attr_tape_used_in_bytes(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''The size, in bytes, of data stored on the virtual tape.

        :cloudformationAttribute: TapeUsedInBytes
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrTapeUsedInBytes"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="tapeRef")
    def tape_ref(self) -> "_aws_storagegateway_f426d4c4.TapeReference":
        '''A reference to a Tape resource.'''
        return typing.cast("_aws_storagegateway_f426d4c4.TapeReference", jsii.get(self, "tapeRef"))

    @builtins.property
    @jsii.member(jsii_name="gatewayArn")
    def gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Tape Gateway that hosts the virtual tape.'''
        return typing.cast(builtins.str, jsii.get(self, "gatewayArn"))

    @gateway_arn.setter
    def gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__662f1b01cec9fb4c578c1bbb30288dbf38679b5353e5dda5dbd320ef43291325)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tapeSizeInBytes")
    def tape_size_in_bytes(self) -> jsii.Number:
        '''The size, in bytes, of the virtual tape that you want to create.'''
        return typing.cast(jsii.Number, jsii.get(self, "tapeSizeInBytes"))

    @tape_size_in_bytes.setter
    def tape_size_in_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__020d09dce3e65ad2aaf95651a3b71d13e7e4491b13562a0833109864a3cdaa0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tapeSizeInBytes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsEncrypted")
    def kms_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Set to true to use Amazon S3 server-side encryption with your own KMS key, or false to use a key managed by Amazon S3.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "kmsEncrypted"))

    @kms_encrypted.setter
    def kms_encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ee66a67c862d78755548260dd465bb54d1d4135b9bbb9ac1bae6ba2ea3475fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsEncrypted", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e1696f2d90ac34d1befe0d8f8fdff10c6a152824cfb1cea61f78cb3c939d074b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="poolId")
    def pool_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the pool that you want to add your tape to for archiving.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolId"))

    @pool_id.setter
    def pool_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__771aea9bb34cd7a52d93c075fca8422288c8149c586c2433579b77e674bbc411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of up to 50 tags to assign to the virtual tape.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b43111da63c8804b5553828beed62e0fc46e21d09e17e06cfa23a83a7d5f7756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tapeBarcode")
    def tape_barcode(self) -> typing.Optional[builtins.str]:
        '''The barcode that you want to assign to the virtual tape.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tapeBarcode"))

    @tape_barcode.setter
    def tape_barcode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5023431719ea44a143693a72e05f0b2a264ee01337c78f4ade43d1fe0d4746bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tapeBarcode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="worm")
    def worm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Set to true to create a write-once-read-many (WORM) virtual tape.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "worm"))

    @worm.setter
    def worm(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cdca3fd4b57f957db6910289a79178f6960086b883d0e146cdbbf55066ade533)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "worm", value) # pyright: ignore[reportArgumentType]


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_storagegateway_f426d4c4.ITapePoolRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnTapePool(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_storagegateway.CfnTapePool",
):
    '''Creates a custom tape pool for archiving virtual tapes with optional retention lock.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tapepool.html
    :cloudformationResource: AWS::StorageGateway::TapePool
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_storagegateway as storagegateway
        
        cfn_tape_pool = storagegateway.CfnTapePool(self, "MyCfnTapePool",
            pool_name="poolName",
            storage_class="storageClass",
        
            # the properties below are optional
            retention_lock_time_in_days=123,
            retention_lock_type="retentionLockType",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        pool_name: builtins.str,
        storage_class: builtins.str,
        retention_lock_time_in_days: typing.Optional[jsii.Number] = None,
        retention_lock_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::StorageGateway::TapePool``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param pool_name: The name of the custom tape pool.
        :param storage_class: The storage class associated with the custom pool (S3 Glacier or S3 Glacier Deep Archive).
        :param retention_lock_time_in_days: Tape retention lock time in days (up to 36,500 days / 100 years).
        :param retention_lock_type: Tape retention lock type. Governance mode allows authorized removal; compliance mode prevents all removal.
        :param tags: A list of up to 50 tags for the tape pool.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ac2c1692ba4edccb604aef75af4b88463d090c7db3c8f08741d200a884adedac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTapePoolProps(
            pool_name=pool_name,
            storage_class=storage_class,
            retention_lock_time_in_days=retention_lock_time_in_days,
            retention_lock_type=retention_lock_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForTapePool")
    @builtins.classmethod
    def arn_for_tape_pool(
        cls,
        resource: "_aws_storagegateway_f426d4c4.ITapePoolRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3bdaa23426ff87911afa19f9997f4ea57420c29c61fc1892987875628fdf638b)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForTapePool", [resource]))

    @jsii.member(jsii_name="fromPoolId")
    @builtins.classmethod
    def from_pool_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        pool_id: builtins.str,
    ) -> "_aws_storagegateway_f426d4c4.ITapePoolRef":
        '''Creates a new ITapePoolRef from a poolId.

        :param scope: -
        :param id: -
        :param pool_id: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a8b4c436c83b9aad89b0f338e63d3ef15cdc1d6880fa6e5c24369f59ab7d5e34)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
        return typing.cast("_aws_storagegateway_f426d4c4.ITapePoolRef", jsii.sinvoke(cls, "fromPoolId", [scope, id, pool_id]))

    @jsii.member(jsii_name="isCfnTapePool")
    @builtins.classmethod
    def is_cfn_tape_pool(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTapePool.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4f4ac6b6ba23515dcc27d4c5a84961fe7a159a83305f9188d9b81d341eac359a)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTapePool", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bb3a41212781376c4f3874b92a3aeae3808be50104fb587f50096ee25d9cbdfe)
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
            type_hints = cached_type_hints(_typecheckingstub__9a89e9380fc69f21f542d0c5d15978f09dbb5fc7563f2badbf156059dafb2775)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPoolArn")
    def attr_pool_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the custom tape pool.

        :cloudformationAttribute: PoolARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPoolArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPoolId")
    def attr_pool_id(self) -> builtins.str:
        '''The unique identifier of the custom tape pool, extracted from the ARN.

        :cloudformationAttribute: PoolId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPoolId"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="tapePoolRef")
    def tape_pool_ref(self) -> "_aws_storagegateway_f426d4c4.TapePoolReference":
        '''A reference to a TapePool resource.'''
        return typing.cast("_aws_storagegateway_f426d4c4.TapePoolReference", jsii.get(self, "tapePoolRef"))

    @builtins.property
    @jsii.member(jsii_name="poolName")
    def pool_name(self) -> builtins.str:
        '''The name of the custom tape pool.'''
        return typing.cast(builtins.str, jsii.get(self, "poolName"))

    @pool_name.setter
    def pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e2aa2850a80df094617446432f9ff1341cc436487f9fdcde124fff6e23224b3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        '''The storage class associated with the custom pool (S3 Glacier or S3 Glacier Deep Archive).'''
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__59e6b638819f00096b40770703546150877b22e670bd72107418a00ab661a3c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retentionLockTimeInDays")
    def retention_lock_time_in_days(self) -> typing.Optional[jsii.Number]:
        '''Tape retention lock time in days (up to 36,500 days / 100 years).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionLockTimeInDays"))

    @retention_lock_time_in_days.setter
    def retention_lock_time_in_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f9a75e037e394e1a483c9c37c628c1a3fd5236ed311d296563d7c92ed300cf84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionLockTimeInDays", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retentionLockType")
    def retention_lock_type(self) -> typing.Optional[builtins.str]:
        '''Tape retention lock type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retentionLockType"))

    @retention_lock_type.setter
    def retention_lock_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4607d71dfda14f2f335c62ade52d5f18924d070d446cf3004dcb39ec784be160)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionLockType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of up to 50 tags for the tape pool.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3795fcc974a44ec324d8e597cdf4de7162f69066e260ed1f4273fc3bc7275cc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_storagegateway.CfnTapePoolProps",
    jsii_struct_bases=[],
    name_mapping={
        "pool_name": "poolName",
        "storage_class": "storageClass",
        "retention_lock_time_in_days": "retentionLockTimeInDays",
        "retention_lock_type": "retentionLockType",
        "tags": "tags",
    },
)
class CfnTapePoolProps:
    def __init__(
        self,
        *,
        pool_name: builtins.str,
        storage_class: builtins.str,
        retention_lock_time_in_days: typing.Optional[jsii.Number] = None,
        retention_lock_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTapePool``.

        :param pool_name: The name of the custom tape pool.
        :param storage_class: The storage class associated with the custom pool (S3 Glacier or S3 Glacier Deep Archive).
        :param retention_lock_time_in_days: Tape retention lock time in days (up to 36,500 days / 100 years).
        :param retention_lock_type: Tape retention lock type. Governance mode allows authorized removal; compliance mode prevents all removal.
        :param tags: A list of up to 50 tags for the tape pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tapepool.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_storagegateway as storagegateway
            
            cfn_tape_pool_props = storagegateway.CfnTapePoolProps(
                pool_name="poolName",
                storage_class="storageClass",
            
                # the properties below are optional
                retention_lock_time_in_days=123,
                retention_lock_type="retentionLockType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__313c929df3254bd85bbd9d06cbd71bce8cccb516d3867f49894385585d8f30e9)
            check_type(argname="argument pool_name", value=pool_name, expected_type=type_hints["pool_name"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument retention_lock_time_in_days", value=retention_lock_time_in_days, expected_type=type_hints["retention_lock_time_in_days"])
            check_type(argname="argument retention_lock_type", value=retention_lock_type, expected_type=type_hints["retention_lock_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pool_name": pool_name,
            "storage_class": storage_class,
        }
        if retention_lock_time_in_days is not None:
            self._values["retention_lock_time_in_days"] = retention_lock_time_in_days
        if retention_lock_type is not None:
            self._values["retention_lock_type"] = retention_lock_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pool_name(self) -> builtins.str:
        '''The name of the custom tape pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tapepool.html#cfn-storagegateway-tapepool-poolname
        '''
        result = self._values.get("pool_name")
        assert result is not None, "Required property 'pool_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_class(self) -> builtins.str:
        '''The storage class associated with the custom pool (S3 Glacier or S3 Glacier Deep Archive).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tapepool.html#cfn-storagegateway-tapepool-storageclass
        '''
        result = self._values.get("storage_class")
        assert result is not None, "Required property 'storage_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_lock_time_in_days(self) -> typing.Optional[jsii.Number]:
        '''Tape retention lock time in days (up to 36,500 days / 100 years).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tapepool.html#cfn-storagegateway-tapepool-retentionlocktimeindays
        '''
        result = self._values.get("retention_lock_time_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retention_lock_type(self) -> typing.Optional[builtins.str]:
        '''Tape retention lock type.

        Governance mode allows authorized removal; compliance mode prevents all removal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tapepool.html#cfn-storagegateway-tapepool-retentionlocktype
        '''
        result = self._values.get("retention_lock_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of up to 50 tags for the tape pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tapepool.html#cfn-storagegateway-tapepool-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTapePoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_storagegateway.CfnTapeProps",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_arn": "gatewayArn",
        "tape_size_in_bytes": "tapeSizeInBytes",
        "kms_encrypted": "kmsEncrypted",
        "kms_key": "kmsKey",
        "pool_id": "poolId",
        "tags": "tags",
        "tape_barcode": "tapeBarcode",
        "worm": "worm",
    },
)
class CfnTapeProps:
    def __init__(
        self,
        *,
        gateway_arn: builtins.str,
        tape_size_in_bytes: jsii.Number,
        kms_encrypted: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        kms_key: typing.Optional[builtins.str] = None,
        pool_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        tape_barcode: typing.Optional[builtins.str] = None,
        worm: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTape``.

        :param gateway_arn: The Amazon Resource Name (ARN) of the Tape Gateway that hosts the virtual tape.
        :param tape_size_in_bytes: The size, in bytes, of the virtual tape that you want to create.
        :param kms_encrypted: Set to true to use Amazon S3 server-side encryption with your own KMS key, or false to use a key managed by Amazon S3. Optional.
        :param kms_key: The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. This value must be set if KMSEncrypted is true.
        :param pool_id: The ID of the pool that you want to add your tape to for archiving. Tapes in this pool are archived in the S3 storage class that is associated with the pool.
        :param tags: A list of up to 50 tags to assign to the virtual tape.
        :param tape_barcode: The barcode that you want to assign to the virtual tape. Barcodes cannot be reused, even after a tape is deleted.
        :param worm: Set to true to create a write-once-read-many (WORM) virtual tape.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_storagegateway as storagegateway
            
            cfn_tape_props = storagegateway.CfnTapeProps(
                gateway_arn="gatewayArn",
                tape_size_in_bytes=123,
            
                # the properties below are optional
                kms_encrypted=False,
                kms_key="kmsKey",
                pool_id="poolId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                tape_barcode="tapeBarcode",
                worm=False
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aa2d145c5722622b5c7cd133c48409678c375141152fd14546bec9a5731ba577)
            check_type(argname="argument gateway_arn", value=gateway_arn, expected_type=type_hints["gateway_arn"])
            check_type(argname="argument tape_size_in_bytes", value=tape_size_in_bytes, expected_type=type_hints["tape_size_in_bytes"])
            check_type(argname="argument kms_encrypted", value=kms_encrypted, expected_type=type_hints["kms_encrypted"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tape_barcode", value=tape_barcode, expected_type=type_hints["tape_barcode"])
            check_type(argname="argument worm", value=worm, expected_type=type_hints["worm"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_arn": gateway_arn,
            "tape_size_in_bytes": tape_size_in_bytes,
        }
        if kms_encrypted is not None:
            self._values["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if pool_id is not None:
            self._values["pool_id"] = pool_id
        if tags is not None:
            self._values["tags"] = tags
        if tape_barcode is not None:
            self._values["tape_barcode"] = tape_barcode
        if worm is not None:
            self._values["worm"] = worm

    @builtins.property
    def gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Tape Gateway that hosts the virtual tape.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html#cfn-storagegateway-tape-gatewayarn
        '''
        result = self._values.get("gateway_arn")
        assert result is not None, "Required property 'gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tape_size_in_bytes(self) -> jsii.Number:
        '''The size, in bytes, of the virtual tape that you want to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html#cfn-storagegateway-tape-tapesizeinbytes
        '''
        result = self._values.get("tape_size_in_bytes")
        assert result is not None, "Required property 'tape_size_in_bytes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def kms_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Set to true to use Amazon S3 server-side encryption with your own KMS key, or false to use a key managed by Amazon S3.

        Optional.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html#cfn-storagegateway-tape-kmsencrypted
        '''
        result = self._values.get("kms_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption.

        This value must be set if KMSEncrypted is true.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html#cfn-storagegateway-tape-kmskey
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pool_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the pool that you want to add your tape to for archiving.

        Tapes in this pool are archived in the S3 storage class that is associated with the pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html#cfn-storagegateway-tape-poolid
        '''
        result = self._values.get("pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of up to 50 tags to assign to the virtual tape.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html#cfn-storagegateway-tape-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def tape_barcode(self) -> typing.Optional[builtins.str]:
        '''The barcode that you want to assign to the virtual tape.

        Barcodes cannot be reused, even after a tape is deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html#cfn-storagegateway-tape-tapebarcode
        '''
        result = self._values.get("tape_barcode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def worm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Set to true to create a write-once-read-many (WORM) virtual tape.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-tape.html#cfn-storagegateway-tape-worm
        '''
        result = self._values.get("worm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTapeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_storagegateway_f426d4c4.IVolumeRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnVolume(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_storagegateway.CfnVolume",
):
    '''Creates a cached iSCSI volume on a Storage Gateway.

    A cached volume stores data in Amazon S3 and retains a copy of frequently accessed data subsets locally.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html
    :cloudformationResource: AWS::StorageGateway::Volume
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_storagegateway as storagegateway
        
        cfn_volume = storagegateway.CfnVolume(self, "MyCfnVolume",
            gateway_arn="gatewayArn",
            network_interface_id="networkInterfaceId",
            target_name="targetName",
            volume_size_in_bytes=123,
        
            # the properties below are optional
            kms_encrypted=False,
            kms_key="kmsKey",
            snapshot_id="snapshotId",
            source_volume_arn="sourceVolumeArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        gateway_arn: builtins.str,
        network_interface_id: builtins.str,
        target_name: builtins.str,
        volume_size_in_bytes: jsii.Number,
        kms_encrypted: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        kms_key: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        source_volume_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::StorageGateway::Volume``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param gateway_arn: The Amazon Resource Name (ARN) of the gateway on which to create the volume.
        :param network_interface_id: The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.
        :param target_name: The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN.
        :param volume_size_in_bytes: The size of the volume in bytes.
        :param kms_encrypted: Set to true to use Amazon S3 server-side encryption with your own KMS key, or false to use a key managed by Amazon S3.
        :param kms_key: The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption.
        :param snapshot_id: The snapshot ID of the snapshot to restore as the new cached volume (e.g., snap-1122aabb).
        :param source_volume_arn: The ARN of an existing volume from which to create the new volume.
        :param tags: A list of up to 50 tags to assign to the volume.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__271ddda20ad6264f77cc2f79555b3fa6ea997c8e5dccba6d566d2dcf154f898f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVolumeProps(
            gateway_arn=gateway_arn,
            network_interface_id=network_interface_id,
            target_name=target_name,
            volume_size_in_bytes=volume_size_in_bytes,
            kms_encrypted=kms_encrypted,
            kms_key=kms_key,
            snapshot_id=snapshot_id,
            source_volume_arn=source_volume_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVolume")
    @builtins.classmethod
    def arn_for_volume(
        cls,
        resource: "_aws_storagegateway_f426d4c4.IVolumeRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bf4b04a4849965fc4cd022c8e0fd09da482cd62aef80e780fb96a074696e4817)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVolume", [resource]))

    @jsii.member(jsii_name="isCfnVolume")
    @builtins.classmethod
    def is_cfn_volume(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVolume.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8697be7703a6f5458994a17690dde8dd46e21cc40628f1a0720415688dddf65b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVolume", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__10e0a5d67c599ccc35a189f881ed3e303c2f2e0453a222f914017c743a9e364d)
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
            type_hints = cached_type_hints(_typecheckingstub__21658029a19b77c6623b63fe0a949fb1e70c240363e99c57a2637e632dc6f9b3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedDate")
    def attr_created_date(self) -> builtins.str:
        '''The date the volume was created.

        :cloudformationAttribute: CreatedDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedDate"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetArn")
    def attr_target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI target name.

        :cloudformationAttribute: TargetARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVolumeArn")
    def attr_volume_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the storage volume.

        :cloudformationAttribute: VolumeARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVolumeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVolumeAttachmentStatus")
    def attr_volume_attachment_status(self) -> builtins.str:
        '''Indicates whether the storage volume is attached to or detached from the gateway.

        :cloudformationAttribute: VolumeAttachmentStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVolumeAttachmentStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrVolumeId")
    def attr_volume_id(self) -> builtins.str:
        '''The unique identifier of the volume, extracted from the ARN.

        :cloudformationAttribute: VolumeId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVolumeId"))

    @builtins.property
    @jsii.member(jsii_name="attrVolumeStatus")
    def attr_volume_status(self) -> builtins.str:
        '''The status of the storage volume.

        :cloudformationAttribute: VolumeStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVolumeStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrVolumeType")
    def attr_volume_type(self) -> builtins.str:
        '''The type of the volume (CACHED iSCSI).

        :cloudformationAttribute: VolumeType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVolumeType"))

    @builtins.property
    @jsii.member(jsii_name="attrVolumeUsedInBytes")
    def attr_volume_used_in_bytes(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''The size of the data stored on the volume in bytes.

        :cloudformationAttribute: VolumeUsedInBytes
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrVolumeUsedInBytes"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "_aws_storagegateway_f426d4c4.VolumeReference":
        '''A reference to a Volume resource.'''
        return typing.cast("_aws_storagegateway_f426d4c4.VolumeReference", jsii.get(self, "volumeRef"))

    @builtins.property
    @jsii.member(jsii_name="gatewayArn")
    def gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the gateway on which to create the volume.'''
        return typing.cast(builtins.str, jsii.get(self, "gatewayArn"))

    @gateway_arn.setter
    def gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1ba45071b81b984f48cd44af0429167dc533fc2274a5191804ba42e94d90d6dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> builtins.str:
        '''The network interface of the gateway on which to expose the iSCSI target.'''
        return typing.cast(builtins.str, jsii.get(self, "networkInterfaceId"))

    @network_interface_id.setter
    def network_interface_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b987f8d436ae585f6d3372ba67b76fb477d21bb29ad5e0b2846a3acc95a00b4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetName")
    def target_name(self) -> builtins.str:
        '''The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN.'''
        return typing.cast(builtins.str, jsii.get(self, "targetName"))

    @target_name.setter
    def target_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f9c563b890b87a18c8920e9fabc30de93962af66c51e6b9482efbbe74a9c65a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInBytes")
    def volume_size_in_bytes(self) -> jsii.Number:
        '''The size of the volume in bytes.'''
        return typing.cast(jsii.Number, jsii.get(self, "volumeSizeInBytes"))

    @volume_size_in_bytes.setter
    def volume_size_in_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__da7ac1e7e402554d7ddb599eda8bfd6a13d073cbfd9f82c7199f8413538d8524)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSizeInBytes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsEncrypted")
    def kms_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Set to true to use Amazon S3 server-side encryption with your own KMS key, or false to use a key managed by Amazon S3.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "kmsEncrypted"))

    @kms_encrypted.setter
    def kms_encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a7e2fbfba7700d7ecaed89d90b0c98d7dde5dc9c07231f2de5eef729fce3e004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsEncrypted", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__50c125bdcfd2df308abe2d69461be24ac0d3452057ad900b769e284c51bc97b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''The snapshot ID of the snapshot to restore as the new cached volume (e.g., snap-1122aabb).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__143b58e3ee8398af2ded9c9c4ddbd83a8a7e8e239bff88ebeac284c9e4ea9542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceVolumeArn")
    def source_volume_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an existing volume from which to create the new volume.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVolumeArn"))

    @source_volume_arn.setter
    def source_volume_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9ae42c42008f06ea12289b5afddd7ba4a9127c40a6e07538bbc94150850d4fa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVolumeArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of up to 50 tags to assign to the volume.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b684f61a2857a73881de4565194ef2d7854f72db3bf20d5d1f7ec27f1dcad007)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_storagegateway.CfnVolumeProps",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_arn": "gatewayArn",
        "network_interface_id": "networkInterfaceId",
        "target_name": "targetName",
        "volume_size_in_bytes": "volumeSizeInBytes",
        "kms_encrypted": "kmsEncrypted",
        "kms_key": "kmsKey",
        "snapshot_id": "snapshotId",
        "source_volume_arn": "sourceVolumeArn",
        "tags": "tags",
    },
)
class CfnVolumeProps:
    def __init__(
        self,
        *,
        gateway_arn: builtins.str,
        network_interface_id: builtins.str,
        target_name: builtins.str,
        volume_size_in_bytes: jsii.Number,
        kms_encrypted: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        kms_key: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        source_volume_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVolume``.

        :param gateway_arn: The Amazon Resource Name (ARN) of the gateway on which to create the volume.
        :param network_interface_id: The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.
        :param target_name: The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN.
        :param volume_size_in_bytes: The size of the volume in bytes.
        :param kms_encrypted: Set to true to use Amazon S3 server-side encryption with your own KMS key, or false to use a key managed by Amazon S3.
        :param kms_key: The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption.
        :param snapshot_id: The snapshot ID of the snapshot to restore as the new cached volume (e.g., snap-1122aabb).
        :param source_volume_arn: The ARN of an existing volume from which to create the new volume.
        :param tags: A list of up to 50 tags to assign to the volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_storagegateway as storagegateway
            
            cfn_volume_props = storagegateway.CfnVolumeProps(
                gateway_arn="gatewayArn",
                network_interface_id="networkInterfaceId",
                target_name="targetName",
                volume_size_in_bytes=123,
            
                # the properties below are optional
                kms_encrypted=False,
                kms_key="kmsKey",
                snapshot_id="snapshotId",
                source_volume_arn="sourceVolumeArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__94b026bb8c34e7ff0faded979ad91712d2af5384fb09b5c6708123e14328a801)
            check_type(argname="argument gateway_arn", value=gateway_arn, expected_type=type_hints["gateway_arn"])
            check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
            check_type(argname="argument target_name", value=target_name, expected_type=type_hints["target_name"])
            check_type(argname="argument volume_size_in_bytes", value=volume_size_in_bytes, expected_type=type_hints["volume_size_in_bytes"])
            check_type(argname="argument kms_encrypted", value=kms_encrypted, expected_type=type_hints["kms_encrypted"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument source_volume_arn", value=source_volume_arn, expected_type=type_hints["source_volume_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_arn": gateway_arn,
            "network_interface_id": network_interface_id,
            "target_name": target_name,
            "volume_size_in_bytes": volume_size_in_bytes,
        }
        if kms_encrypted is not None:
            self._values["kms_encrypted"] = kms_encrypted
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if source_volume_arn is not None:
            self._values["source_volume_arn"] = source_volume_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the gateway on which to create the volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-gatewayarn
        '''
        result = self._values.get("gateway_arn")
        assert result is not None, "Required property 'gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface_id(self) -> builtins.str:
        '''The network interface of the gateway on which to expose the iSCSI target.

        Only IPv4 addresses are accepted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-networkinterfaceid
        '''
        result = self._values.get("network_interface_id")
        assert result is not None, "Required property 'network_interface_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_name(self) -> builtins.str:
        '''The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-targetname
        '''
        result = self._values.get("target_name")
        assert result is not None, "Required property 'target_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_size_in_bytes(self) -> jsii.Number:
        '''The size of the volume in bytes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-volumesizeinbytes
        '''
        result = self._values.get("volume_size_in_bytes")
        assert result is not None, "Required property 'volume_size_in_bytes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def kms_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Set to true to use Amazon S3 server-side encryption with your own KMS key, or false to use a key managed by Amazon S3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-kmsencrypted
        '''
        result = self._values.get("kms_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-kmskey
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''The snapshot ID of the snapshot to restore as the new cached volume (e.g., snap-1122aabb).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-snapshotid
        '''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_volume_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an existing volume from which to create the new volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-sourcevolumearn
        '''
        result = self._values.get("source_volume_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of up to 50 tags to assign to the volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-storagegateway-volume.html#cfn-storagegateway-volume-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnTape",
    "CfnTapePool",
    "CfnTapePoolProps",
    "CfnTapeProps",
    "CfnVolume",
    "CfnVolumeProps",
]

publication.publish()

def _typecheckingstub__363b2f7813c184123160ffaf59a488211565913fb5126a1fa69bcb36310d32dc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    gateway_arn: builtins.str,
    tape_size_in_bytes: jsii.Number,
    kms_encrypted: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    kms_key: typing.Optional[builtins.str] = None,
    pool_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    tape_barcode: typing.Optional[builtins.str] = None,
    worm: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae610be3890fbb42584972211b0c5af3006370462c1bf3c6c3b219eb44a03b39(
    resource: _aws_storagegateway_f426d4c4.ITapeRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebb8f5d769e86e9451e9c5e5b3470e03b5d0dfb0c67afc78fc0e8c2598c707dd(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd33548844c3c66482e5960a6a6f61789c9af04eb374db35a888509e0a56ab58(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae0da0b888c3ffbaa5eb6cd82d55bf20a66d98c9c309e38a2589910332683ed(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662f1b01cec9fb4c578c1bbb30288dbf38679b5353e5dda5dbd320ef43291325(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__020d09dce3e65ad2aaf95651a3b71d13e7e4491b13562a0833109864a3cdaa0b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee66a67c862d78755548260dd465bb54d1d4135b9bbb9ac1bae6ba2ea3475fe8(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1696f2d90ac34d1befe0d8f8fdff10c6a152824cfb1cea61f78cb3c939d074b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__771aea9bb34cd7a52d93c075fca8422288c8149c586c2433579b77e674bbc411(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b43111da63c8804b5553828beed62e0fc46e21d09e17e06cfa23a83a7d5f7756(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5023431719ea44a143693a72e05f0b2a264ee01337c78f4ade43d1fe0d4746bb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdca3fd4b57f957db6910289a79178f6960086b883d0e146cdbbf55066ade533(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac2c1692ba4edccb604aef75af4b88463d090c7db3c8f08741d200a884adedac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    pool_name: builtins.str,
    storage_class: builtins.str,
    retention_lock_time_in_days: typing.Optional[jsii.Number] = None,
    retention_lock_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bdaa23426ff87911afa19f9997f4ea57420c29c61fc1892987875628fdf638b(
    resource: _aws_storagegateway_f426d4c4.ITapePoolRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8b4c436c83b9aad89b0f338e63d3ef15cdc1d6880fa6e5c24369f59ab7d5e34(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4ac6b6ba23515dcc27d4c5a84961fe7a159a83305f9188d9b81d341eac359a(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb3a41212781376c4f3874b92a3aeae3808be50104fb587f50096ee25d9cbdfe(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a89e9380fc69f21f542d0c5d15978f09dbb5fc7563f2badbf156059dafb2775(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2aa2850a80df094617446432f9ff1341cc436487f9fdcde124fff6e23224b3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e6b638819f00096b40770703546150877b22e670bd72107418a00ab661a3c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a75e037e394e1a483c9c37c628c1a3fd5236ed311d296563d7c92ed300cf84(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4607d71dfda14f2f335c62ade52d5f18924d070d446cf3004dcb39ec784be160(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3795fcc974a44ec324d8e597cdf4de7162f69066e260ed1f4273fc3bc7275cc1(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313c929df3254bd85bbd9d06cbd71bce8cccb516d3867f49894385585d8f30e9(
    *,
    pool_name: builtins.str,
    storage_class: builtins.str,
    retention_lock_time_in_days: typing.Optional[jsii.Number] = None,
    retention_lock_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa2d145c5722622b5c7cd133c48409678c375141152fd14546bec9a5731ba577(
    *,
    gateway_arn: builtins.str,
    tape_size_in_bytes: jsii.Number,
    kms_encrypted: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    kms_key: typing.Optional[builtins.str] = None,
    pool_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    tape_barcode: typing.Optional[builtins.str] = None,
    worm: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__271ddda20ad6264f77cc2f79555b3fa6ea997c8e5dccba6d566d2dcf154f898f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    gateway_arn: builtins.str,
    network_interface_id: builtins.str,
    target_name: builtins.str,
    volume_size_in_bytes: jsii.Number,
    kms_encrypted: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    kms_key: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    source_volume_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf4b04a4849965fc4cd022c8e0fd09da482cd62aef80e780fb96a074696e4817(
    resource: _aws_storagegateway_f426d4c4.IVolumeRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8697be7703a6f5458994a17690dde8dd46e21cc40628f1a0720415688dddf65b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e0a5d67c599ccc35a189f881ed3e303c2f2e0453a222f914017c743a9e364d(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21658029a19b77c6623b63fe0a949fb1e70c240363e99c57a2637e632dc6f9b3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba45071b81b984f48cd44af0429167dc533fc2274a5191804ba42e94d90d6dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b987f8d436ae585f6d3372ba67b76fb477d21bb29ad5e0b2846a3acc95a00b4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9c563b890b87a18c8920e9fabc30de93962af66c51e6b9482efbbe74a9c65a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da7ac1e7e402554d7ddb599eda8bfd6a13d073cbfd9f82c7199f8413538d8524(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e2fbfba7700d7ecaed89d90b0c98d7dde5dc9c07231f2de5eef729fce3e004(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c125bdcfd2df308abe2d69461be24ac0d3452057ad900b769e284c51bc97b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143b58e3ee8398af2ded9c9c4ddbd83a8a7e8e239bff88ebeac284c9e4ea9542(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ae42c42008f06ea12289b5afddd7ba4a9127c40a6e07538bbc94150850d4fa8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b684f61a2857a73881de4565194ef2d7854f72db3bf20d5d1f7ec27f1dcad007(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b026bb8c34e7ff0faded979ad91712d2af5384fb09b5c6708123e14328a801(
    *,
    gateway_arn: builtins.str,
    network_interface_id: builtins.str,
    target_name: builtins.str,
    volume_size_in_bytes: jsii.Number,
    kms_encrypted: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    kms_key: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    source_volume_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
