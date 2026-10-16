r'''
# AWS::DocDBElastic Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_docdbelastic as docdbelastic
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DocDBElastic construct libraries](https://constructs.dev/search?q=docdbelastic)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DocDBElastic resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DocDBElastic.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DocDBElastic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DocDBElastic.html).

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
    import aws_cdk.interfaces.aws_docdbelastic as _aws_docdbelastic_7fdcbbe8
    import aws_cdk.interfaces.aws_ec2 as _aws_ec2_18162e09
    import aws_cdk.interfaces.aws_kms as _aws_kms_18db7412
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_docdbelastic_7fdcbbe8 = _LazyImport("aws_cdk.interfaces.aws_docdbelastic")
    _aws_ec2_18162e09 = _LazyImport("aws_cdk.interfaces.aws_ec2")
    _aws_kms_18db7412 = _LazyImport("aws_cdk.interfaces.aws_kms")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_docdbelastic_7fdcbbe8.IClusterRef, _aws_cdk_0cae9daa.ITaggable)
class CfnCluster(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdbelastic.CfnCluster",
):
    '''Creates a new Amazon DocumentDB elastic cluster and returns its cluster structure.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html
    :cloudformationResource: AWS::DocDBElastic::Cluster
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdbelastic as docdbelastic
        
        cfn_cluster = docdbelastic.CfnCluster(self, "MyCfnCluster",
            admin_user_name="adminUserName",
            auth_type="authType",
            cluster_name="clusterName",
            shard_capacity=123,
            shard_count=123,
        
            # the properties below are optional
            admin_user_password="adminUserPassword",
            backup_retention_period=123,
            kms_key_id="kmsKeyId",
            preferred_backup_window="preferredBackupWindow",
            preferred_maintenance_window="preferredMaintenanceWindow",
            shard_instance_count=123,
            subnet_ids=["subnetIds"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        admin_user_name: builtins.str,
        auth_type: builtins.str,
        cluster_name: builtins.str,
        shard_capacity: jsii.Number,
        shard_count: jsii.Number,
        admin_user_password: typing.Optional[builtins.str] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[typing.Union[builtins.str, "_aws_kms_18db7412.IKeyRef"]] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        shard_instance_count: typing.Optional[jsii.Number] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[typing.Union[builtins.str, "_aws_ec2_18162e09.ISecurityGroupRef"]]] = None,
    ) -> None:
        '''Create a new ``AWS::DocDBElastic::Cluster``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param admin_user_name: The name of the Amazon DocumentDB elastic clusters administrator. *Constraints* : - Must be from 1 to 63 letters or numbers. - The first character must be a letter. - Cannot be a reserved word.
        :param auth_type: The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are ``PLAIN_TEXT`` or ``SECRET_ARN`` .
        :param cluster_name: The name of the new elastic cluster. This parameter is stored as a lowercase string. *Constraints* : - Must contain from 1 to 63 letters, numbers, or hyphens. - The first character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. *Example* : ``my-cluster``
        :param shard_capacity: The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        :param shard_count: The number of shards assigned to the elastic cluster. Maximum is 32.
        :param admin_user_password: The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters. *Constraints* : - Must contain from 8 to 100 characters. - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@). - A valid ``AdminUserName`` entry is also required.
        :param backup_retention_period: The number of days for which automatic snapshots are retained.
        :param kms_key_id: The KMS key identifier to use to encrypt the new elastic cluster. The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
        :param preferred_backup_window: The daily time range during which automated backups are created if automated backups are enabled, as determined by ``backupRetentionPeriod`` .
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). *Format* : ``ddd:hh24:mi-ddd:hh24:mi`` *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week. *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun *Constraints* : Minimum 30-minute window.
        :param shard_instance_count: The number of replica instances applying to all shards in the cluster. A ``shardInstanceCount`` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.
        :param subnet_ids: The Amazon EC2 subnet IDs for the new elastic cluster.
        :param tags: The tags to be assigned to the new elastic cluster.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with the new elastic cluster.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d18e65300a117432acf21688bd5e6ea35e026a31a5e4e4867ff7ee2d8db5564d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            admin_user_name=admin_user_name,
            auth_type=auth_type,
            cluster_name=cluster_name,
            shard_capacity=shard_capacity,
            shard_count=shard_count,
            admin_user_password=admin_user_password,
            backup_retention_period=backup_retention_period,
            kms_key_id=kms_key_id,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            shard_instance_count=shard_instance_count,
            subnet_ids=subnet_ids,
            tags=tags,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForCluster")
    @builtins.classmethod
    def arn_for_cluster(
        cls,
        resource: "_aws_docdbelastic_7fdcbbe8.IClusterRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ad99c1df984ce505659106e561bbbe55552ea239411e8a258f1fb028637e1d8d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForCluster", [resource]))

    @jsii.member(jsii_name="isCfnCluster")
    @builtins.classmethod
    def is_cfn_cluster(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnCluster.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ae75bf2b579cf7712e3e0d05ef903a442d69230ff6a71d3b1bad8e7312bbe152)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnCluster", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aec8e551077c21913b737a2bbc888da7a50a3375755b5e68b19b767f593e0257)
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
            type_hints = cached_type_hints(_typecheckingstub__a898906295d082897a7970db90e4e30b3fa698fffb4c8731a51f9a15878288a2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterArn")
    def attr_cluster_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ClusterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterArn"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterEndpoint")
    def attr_cluster_endpoint(self) -> builtins.str:
        '''The URL used to connect to the elastic cluster.

        :cloudformationAttribute: ClusterEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "_aws_docdbelastic_7fdcbbe8.ClusterReference":
        '''A reference to a Cluster resource.'''
        return typing.cast("_aws_docdbelastic_7fdcbbe8.ClusterReference", jsii.get(self, "clusterRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="adminUserName")
    def admin_user_name(self) -> builtins.str:
        '''The name of the Amazon DocumentDB elastic clusters administrator.'''
        return typing.cast(builtins.str, jsii.get(self, "adminUserName"))

    @admin_user_name.setter
    def admin_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__75e884ad993b4ce5fe022eb51a18cbb8f74e5912e83a15d50d9899aa3445bdcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUserName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        '''The authentication type used to determine where to fetch the password used for accessing the elastic cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__25c0c8636d6a5305b5ec107b1ced064baa846fc551d5b0ff94f55596f60cceef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The name of the new elastic cluster.

        This parameter is stored as a lowercase string.
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__35b5d057407f61272e574c114a6e28178b7fcb07d1c9cbe8c7ba5996a0be5262)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="shardCapacity")
    def shard_capacity(self) -> jsii.Number:
        '''The number of vCPUs assigned to each elastic cluster shard.'''
        return typing.cast(jsii.Number, jsii.get(self, "shardCapacity"))

    @shard_capacity.setter
    def shard_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cd6ddfaad6dd710cf923e794e6d68545333af2222ee08e33f275b5aeffaa20bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shardCapacity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="shardCount")
    def shard_count(self) -> jsii.Number:
        '''The number of shards assigned to the elastic cluster.'''
        return typing.cast(jsii.Number, jsii.get(self, "shardCount"))

    @shard_count.setter
    def shard_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cfcef7bfb595bba74106d2b94ae9ee7fde3cfc22a3ea86d938c1f50bc2c7966e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shardCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="adminUserPassword")
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUserPassword"))

    @admin_user_password.setter
    def admin_user_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__470579f0ad58114a88b5ed48276c3b18996b7302a73c462a28c5fe499da47fc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUserPassword", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backupRetentionPeriod")
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which automatic snapshots are retained.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupRetentionPeriod"))

    @backup_retention_period.setter
    def backup_retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d81338ed2d2b35425bdc6b440d859bf6f7104c7d3e66fb0b6a4b0b6ed4baaf00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetentionPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The KMS key identifier to use to encrypt the new elastic cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0953a51d1454415947e4ab62061cf85963bc67eaf8b442f55611367c42e51638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range during which automated backups are created if automated backups are enabled, as determined by ``backupRetentionPeriod`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindow"))

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8c4acb4ae8cd439155ec33ec8e279ea4474d4a87642ef3d269a76e5647be02bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBackupWindow", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0ffa8d3c73f9cb8dbb10a83c94105842d5c99d4532516cfb2e94ac10a5760cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="shardInstanceCount")
    def shard_instance_count(self) -> typing.Optional[jsii.Number]:
        '''The number of replica instances applying to all shards in the cluster.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shardInstanceCount"))

    @shard_instance_count.setter
    def shard_instance_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2081e1f0fbadf01af64a49f199c20e8ba4209c58b855709e74d727666c656b34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shardInstanceCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon EC2 subnet IDs for the new elastic cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c59fae2991fdf99f407d97835ea06b1afbfc6a97c5607c1b1b36dfc5aad6bb97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags to be assigned to the new elastic cluster.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7f105da06d91ef171ed924155e7737cd00df9c3b1289c1c0098e9af8a494bdb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of EC2 VPC security groups to associate with the new elastic cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__712dc02a5b00741b7b19719e7c7ce31507c5058d6a956dc9dd8e9d609da8dde3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdbelastic.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "admin_user_name": "adminUserName",
        "auth_type": "authType",
        "cluster_name": "clusterName",
        "shard_capacity": "shardCapacity",
        "shard_count": "shardCount",
        "admin_user_password": "adminUserPassword",
        "backup_retention_period": "backupRetentionPeriod",
        "kms_key_id": "kmsKeyId",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "shard_instance_count": "shardInstanceCount",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        admin_user_name: builtins.str,
        auth_type: builtins.str,
        cluster_name: builtins.str,
        shard_capacity: jsii.Number,
        shard_count: jsii.Number,
        admin_user_password: typing.Optional[builtins.str] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[typing.Union[builtins.str, "_aws_kms_18db7412.IKeyRef"]] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        shard_instance_count: typing.Optional[jsii.Number] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[typing.Union[builtins.str, "_aws_ec2_18162e09.ISecurityGroupRef"]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param admin_user_name: The name of the Amazon DocumentDB elastic clusters administrator. *Constraints* : - Must be from 1 to 63 letters or numbers. - The first character must be a letter. - Cannot be a reserved word.
        :param auth_type: The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are ``PLAIN_TEXT`` or ``SECRET_ARN`` .
        :param cluster_name: The name of the new elastic cluster. This parameter is stored as a lowercase string. *Constraints* : - Must contain from 1 to 63 letters, numbers, or hyphens. - The first character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. *Example* : ``my-cluster``
        :param shard_capacity: The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.
        :param shard_count: The number of shards assigned to the elastic cluster. Maximum is 32.
        :param admin_user_password: The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters. *Constraints* : - Must contain from 8 to 100 characters. - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@). - A valid ``AdminUserName`` entry is also required.
        :param backup_retention_period: The number of days for which automatic snapshots are retained.
        :param kms_key_id: The KMS key identifier to use to encrypt the new elastic cluster. The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.
        :param preferred_backup_window: The daily time range during which automated backups are created if automated backups are enabled, as determined by ``backupRetentionPeriod`` .
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). *Format* : ``ddd:hh24:mi-ddd:hh24:mi`` *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week. *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun *Constraints* : Minimum 30-minute window.
        :param shard_instance_count: The number of replica instances applying to all shards in the cluster. A ``shardInstanceCount`` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.
        :param subnet_ids: The Amazon EC2 subnet IDs for the new elastic cluster.
        :param tags: The tags to be assigned to the new elastic cluster.
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with the new elastic cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdbelastic as docdbelastic
            
            cfn_cluster_props = docdbelastic.CfnClusterProps(
                admin_user_name="adminUserName",
                auth_type="authType",
                cluster_name="clusterName",
                shard_capacity=123,
                shard_count=123,
            
                # the properties below are optional
                admin_user_password="adminUserPassword",
                backup_retention_period=123,
                kms_key_id="kmsKeyId",
                preferred_backup_window="preferredBackupWindow",
                preferred_maintenance_window="preferredMaintenanceWindow",
                shard_instance_count=123,
                subnet_ids=["subnetIds"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2b5fe934af328fd508365294b2de9cfcaa71e04fad229d22243ec4156b7f0441)
            check_type(argname="argument admin_user_name", value=admin_user_name, expected_type=type_hints["admin_user_name"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument shard_capacity", value=shard_capacity, expected_type=type_hints["shard_capacity"])
            check_type(argname="argument shard_count", value=shard_count, expected_type=type_hints["shard_count"])
            check_type(argname="argument admin_user_password", value=admin_user_password, expected_type=type_hints["admin_user_password"])
            check_type(argname="argument backup_retention_period", value=backup_retention_period, expected_type=type_hints["backup_retention_period"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument shard_instance_count", value=shard_instance_count, expected_type=type_hints["shard_instance_count"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_user_name": admin_user_name,
            "auth_type": auth_type,
            "cluster_name": cluster_name,
            "shard_capacity": shard_capacity,
            "shard_count": shard_count,
        }
        if admin_user_password is not None:
            self._values["admin_user_password"] = admin_user_password
        if backup_retention_period is not None:
            self._values["backup_retention_period"] = backup_retention_period
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if shard_instance_count is not None:
            self._values["shard_instance_count"] = shard_instance_count
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def admin_user_name(self) -> builtins.str:
        '''The name of the Amazon DocumentDB elastic clusters administrator.

        *Constraints* :

        - Must be from 1 to 63 letters or numbers.
        - The first character must be a letter.
        - Cannot be a reserved word.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-adminusername
        '''
        result = self._values.get("admin_user_name")
        assert result is not None, "Required property 'admin_user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_type(self) -> builtins.str:
        '''The authentication type used to determine where to fetch the password used for accessing the elastic cluster.

        Valid types are ``PLAIN_TEXT`` or ``SECRET_ARN`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-authtype
        '''
        result = self._values.get("auth_type")
        assert result is not None, "Required property 'auth_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the new elastic cluster. This parameter is stored as a lowercase string.

        *Constraints* :

        - Must contain from 1 to 63 letters, numbers, or hyphens.
        - The first character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        *Example* : ``my-cluster``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shard_capacity(self) -> jsii.Number:
        '''The number of vCPUs assigned to each elastic cluster shard.

        Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-shardcapacity
        '''
        result = self._values.get("shard_capacity")
        assert result is not None, "Required property 'shard_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def shard_count(self) -> jsii.Number:
        '''The number of shards assigned to the elastic cluster.

        Maximum is 32.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-shardcount
        '''
        result = self._values.get("shard_count")
        assert result is not None, "Required property 'shard_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.

        *Constraints* :

        - Must contain from 8 to 100 characters.
        - Cannot contain a forward slash (/), double quote ("), or the "at" symbol (@).
        - A valid ``AdminUserName`` entry is also required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-adminuserpassword
        '''
        result = self._values.get("admin_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which automatic snapshots are retained.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-backupretentionperiod
        '''
        result = self._values.get("backup_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, "_aws_kms_18db7412.IKeyRef"]]:
        '''The KMS key identifier to use to encrypt the new elastic cluster.

        The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.

        If an encryption key is not specified, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[typing.Union[builtins.str, "_aws_kms_18db7412.IKeyRef"]], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range during which automated backups are created if automated backups are enabled, as determined by ``backupRetentionPeriod`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-preferredbackupwindow
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        *Format* : ``ddd:hh24:mi-ddd:hh24:mi``

        *Default* : a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week.

        *Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun

        *Constraints* : Minimum 30-minute window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shard_instance_count(self) -> typing.Optional[jsii.Number]:
        '''The number of replica instances applying to all shards in the cluster.

        A ``shardInstanceCount`` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-shardinstancecount
        '''
        result = self._values.get("shard_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon EC2 subnet IDs for the new elastic cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags to be assigned to the new elastic cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def vpc_security_group_ids(
        self,
    ) -> typing.Optional[typing.List[typing.Union[builtins.str, "_aws_ec2_18162e09.ISecurityGroupRef"]]]:
        '''A list of EC2 VPC security groups to associate with the new elastic cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-cluster.html#cfn-docdbelastic-cluster-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[typing.Union[builtins.str, "_aws_ec2_18162e09.ISecurityGroupRef"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_docdbelastic_7fdcbbe8.IClusterSnapshotRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnClusterSnapshot(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdbelastic.CfnClusterSnapshot",
):
    '''Resource Type definition for AWS::DocDBElastic::ClusterSnapshot.

    Creates a manual snapshot of an Amazon DocumentDB elastic cluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-clustersnapshot.html
    :cloudformationResource: AWS::DocDBElastic::ClusterSnapshot
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdbelastic as docdbelastic
        
        cfn_cluster_snapshot = docdbelastic.CfnClusterSnapshot(self, "MyCfnClusterSnapshot",
            cluster_arn="clusterArn",
            snapshot_name="snapshotName",
        
            # the properties below are optional
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
        cluster_arn: builtins.str,
        snapshot_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DocDBElastic::ClusterSnapshot``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_arn: The ARN of the elastic cluster of which to create a snapshot.
        :param snapshot_name: The name of the elastic cluster snapshot.
        :param tags: An array of key-value pairs to apply to the elastic cluster snapshot.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0db109586ae8330af416009d17ee16b4686e262e70a1b0c3480e97e2565976a5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterSnapshotProps(
            cluster_arn=cluster_arn, snapshot_name=snapshot_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnClusterSnapshot")
    @builtins.classmethod
    def is_cfn_cluster_snapshot(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnClusterSnapshot.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fc736a86aca44169ab75b91e6a5bc9fb9a43cfe27a01e8c38846963070ea30a4)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnClusterSnapshot", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6aad750640176796941beeb2994e0394fef1dadab7a9c29e10df30180d185c10)
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
            type_hints = cached_type_hints(_typecheckingstub__736387f08a4345297421d2369890153118afd3a1c9b6cbc75f336506105185fe)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAdminUserName")
    def attr_admin_user_name(self) -> builtins.str:
        '''The name of the elastic cluster administrator.

        :cloudformationAttribute: AdminUserName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAdminUserName"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterCreationTime")
    def attr_cluster_creation_time(self) -> builtins.str:
        '''The time when the source elastic cluster was created, in Universal Coordinated Time (UTC).

        :cloudformationAttribute: ClusterCreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrKmsKeyId")
    def attr_kms_key_id(self) -> builtins.str:
        '''The KMS key identifier used to encrypt the source elastic cluster.

        :cloudformationAttribute: KmsKeyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKmsKeyId"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotArn")
    def attr_snapshot_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the elastic cluster snapshot.

        :cloudformationAttribute: SnapshotArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotCreationTime")
    def attr_snapshot_creation_time(self) -> builtins.str:
        '''The time when the elastic cluster snapshot was created, in Universal Coordinated Time (UTC).

        :cloudformationAttribute: SnapshotCreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotType")
    def attr_snapshot_type(self) -> builtins.str:
        '''The type of the elastic cluster snapshot (manual or automated).

        :cloudformationAttribute: SnapshotType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotType"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the elastic cluster snapshot.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrSubnetIds")
    def attr_subnet_ids(self) -> typing.List[builtins.str]:
        '''The Amazon EC2 subnet IDs associated with the source elastic cluster.

        :cloudformationAttribute: SubnetIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSubnetIds"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcSecurityGroupIds")
    def attr_vpc_security_group_ids(self) -> typing.List[builtins.str]:
        '''The Amazon EC2 security group IDs associated with the source elastic cluster.

        :cloudformationAttribute: VpcSecurityGroupIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrVpcSecurityGroupIds"))

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
    @jsii.member(jsii_name="clusterSnapshotRef")
    def cluster_snapshot_ref(
        self,
    ) -> "_aws_docdbelastic_7fdcbbe8.ClusterSnapshotReference":
        '''A reference to a ClusterSnapshot resource.'''
        return typing.cast("_aws_docdbelastic_7fdcbbe8.ClusterSnapshotReference", jsii.get(self, "clusterSnapshotRef"))

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''The ARN of the elastic cluster of which to create a snapshot.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9c15a6452d0eaad219d234ad09d56f1028eaeaecbba553cdd6c2a3cc49857c20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        '''The name of the elastic cluster snapshot.'''
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6f76b182e041e609adf533c8cc1d113dd9c8db9ae4690cbb8fced19e6890fd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to the elastic cluster snapshot.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__145fad72f653411ea7720841e041e0595cfcc8d97f0f21c41508e8362cd4e03c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdbelastic.CfnClusterSnapshotProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_arn": "clusterArn",
        "snapshot_name": "snapshotName",
        "tags": "tags",
    },
)
class CfnClusterSnapshotProps:
    def __init__(
        self,
        *,
        cluster_arn: builtins.str,
        snapshot_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterSnapshot``.

        :param cluster_arn: The ARN of the elastic cluster of which to create a snapshot.
        :param snapshot_name: The name of the elastic cluster snapshot.
        :param tags: An array of key-value pairs to apply to the elastic cluster snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-clustersnapshot.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdbelastic as docdbelastic
            
            cfn_cluster_snapshot_props = docdbelastic.CfnClusterSnapshotProps(
                cluster_arn="clusterArn",
                snapshot_name="snapshotName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d7312696a2836816e3012aa75e434596451dd7a2794d8a9813cf0afb177975ee)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
            "snapshot_name": snapshot_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The ARN of the elastic cluster of which to create a snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-clustersnapshot.html#cfn-docdbelastic-clustersnapshot-clusterarn
        '''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def snapshot_name(self) -> builtins.str:
        '''The name of the elastic cluster snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-clustersnapshot.html#cfn-docdbelastic-clustersnapshot-snapshotname
        '''
        result = self._values.get("snapshot_name")
        assert result is not None, "Required property 'snapshot_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to the elastic cluster snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdbelastic-clustersnapshot.html#cfn-docdbelastic-clustersnapshot-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterSnapshotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
    "CfnClusterSnapshot",
    "CfnClusterSnapshotProps",
]

publication.publish()

def _typecheckingstub__d18e65300a117432acf21688bd5e6ea35e026a31a5e4e4867ff7ee2d8db5564d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    admin_user_name: builtins.str,
    auth_type: builtins.str,
    cluster_name: builtins.str,
    shard_capacity: jsii.Number,
    shard_count: jsii.Number,
    admin_user_password: typing.Optional[builtins.str] = None,
    backup_retention_period: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[typing.Union[builtins.str, _aws_kms_18db7412.IKeyRef]] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    shard_instance_count: typing.Optional[jsii.Number] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[typing.Union[builtins.str, _aws_ec2_18162e09.ISecurityGroupRef]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad99c1df984ce505659106e561bbbe55552ea239411e8a258f1fb028637e1d8d(
    resource: _aws_docdbelastic_7fdcbbe8.IClusterRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae75bf2b579cf7712e3e0d05ef903a442d69230ff6a71d3b1bad8e7312bbe152(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec8e551077c21913b737a2bbc888da7a50a3375755b5e68b19b767f593e0257(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a898906295d082897a7970db90e4e30b3fa698fffb4c8731a51f9a15878288a2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e884ad993b4ce5fe022eb51a18cbb8f74e5912e83a15d50d9899aa3445bdcd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c0c8636d6a5305b5ec107b1ced064baa846fc551d5b0ff94f55596f60cceef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35b5d057407f61272e574c114a6e28178b7fcb07d1c9cbe8c7ba5996a0be5262(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd6ddfaad6dd710cf923e794e6d68545333af2222ee08e33f275b5aeffaa20bb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfcef7bfb595bba74106d2b94ae9ee7fde3cfc22a3ea86d938c1f50bc2c7966e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470579f0ad58114a88b5ed48276c3b18996b7302a73c462a28c5fe499da47fc2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d81338ed2d2b35425bdc6b440d859bf6f7104c7d3e66fb0b6a4b0b6ed4baaf00(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0953a51d1454415947e4ab62061cf85963bc67eaf8b442f55611367c42e51638(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4acb4ae8cd439155ec33ec8e279ea4474d4a87642ef3d269a76e5647be02bf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffa8d3c73f9cb8dbb10a83c94105842d5c99d4532516cfb2e94ac10a5760cd3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2081e1f0fbadf01af64a49f199c20e8ba4209c58b855709e74d727666c656b34(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59fae2991fdf99f407d97835ea06b1afbfc6a97c5607c1b1b36dfc5aad6bb97(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f105da06d91ef171ed924155e7737cd00df9c3b1289c1c0098e9af8a494bdb6(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712dc02a5b00741b7b19719e7c7ce31507c5058d6a956dc9dd8e9d609da8dde3(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5fe934af328fd508365294b2de9cfcaa71e04fad229d22243ec4156b7f0441(
    *,
    admin_user_name: builtins.str,
    auth_type: builtins.str,
    cluster_name: builtins.str,
    shard_capacity: jsii.Number,
    shard_count: jsii.Number,
    admin_user_password: typing.Optional[builtins.str] = None,
    backup_retention_period: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[typing.Union[builtins.str, _aws_kms_18db7412.IKeyRef]] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    shard_instance_count: typing.Optional[jsii.Number] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[typing.Union[builtins.str, _aws_ec2_18162e09.ISecurityGroupRef]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0db109586ae8330af416009d17ee16b4686e262e70a1b0c3480e97e2565976a5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_arn: builtins.str,
    snapshot_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc736a86aca44169ab75b91e6a5bc9fb9a43cfe27a01e8c38846963070ea30a4(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aad750640176796941beeb2994e0394fef1dadab7a9c29e10df30180d185c10(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__736387f08a4345297421d2369890153118afd3a1c9b6cbc75f336506105185fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c15a6452d0eaad219d234ad09d56f1028eaeaecbba553cdd6c2a3cc49857c20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f76b182e041e609adf533c8cc1d113dd9c8db9ae4690cbb8fced19e6890fd64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145fad72f653411ea7720841e041e0595cfcc8d97f0f21c41508e8362cd4e03c(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7312696a2836816e3012aa75e434596451dd7a2794d8a9813cf0afb177975ee(
    *,
    cluster_arn: builtins.str,
    snapshot_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
