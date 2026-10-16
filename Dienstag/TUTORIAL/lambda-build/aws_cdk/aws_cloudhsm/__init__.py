r'''
# AWS::CloudHSM Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cloudhsm as cloudhsm
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CloudHSM construct libraries](https://constructs.dev/search?q=cloudhsm)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CloudHSM resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CloudHSM.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CloudHSM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CloudHSM.html).

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
    import aws_cdk.interfaces.aws_cloudhsm as _aws_cloudhsm_fe2add2e
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_cloudhsm_fe2add2e = _LazyImport("aws_cdk.interfaces.aws_cloudhsm")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_cloudhsm_fe2add2e.IClusterRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnCluster(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudhsm.CfnCluster",
):
    '''Creates and manages an AWS CloudHSM cluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudhsm-cluster.html
    :cloudformationResource: AWS::CloudHSM::Cluster
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudhsm as cloudhsm
        
        cfn_cluster = cloudhsm.CfnCluster(self, "MyCfnCluster",
            hsm_type="hsmType",
        
            # the properties below are optional
            backup_retention_policy=cloudhsm.CfnCluster.BackupRetentionPolicyProperty(
                type="type",
                value="value"
            ),
            mode="mode",
            network_type="networkType",
            subnet_ids=["subnetIds"],
            tags=[cloudhsm.CfnCluster.TagsItemsProperty(
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
        hsm_type: builtins.str,
        backup_retention_policy: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCluster.BackupRetentionPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        mode: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnCluster.TagsItemsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::CloudHSM::Cluster``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param hsm_type: The type of HSM to use in the cluster.
        :param backup_retention_policy: A policy that defines how the service retains backups.
        :param mode: The mode to use in the cluster.
        :param network_type: The NetworkType to create a cluster with.
        :param subnet_ids: The identifiers (IDs) of the subnets where the cluster is created. You must specify at least one subnet.
        :param tags: Tags to apply to the CloudHSM cluster.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__11927f58ba0f3a3dce7a79e6251f010e6256babff3a1e40f8cd2ed87b54b77e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            hsm_type=hsm_type,
            backup_retention_policy=backup_retention_policy,
            mode=mode,
            network_type=network_type,
            subnet_ids=subnet_ids,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForCluster")
    @builtins.classmethod
    def arn_for_cluster(
        cls,
        resource: "_aws_cloudhsm_fe2add2e.IClusterRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__de17c7d12050cab21b8fb5370239a83ddaee83ec8c5c608ad413b47686ba0fac)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForCluster", [resource]))

    @jsii.member(jsii_name="isCfnCluster")
    @builtins.classmethod
    def is_cfn_cluster(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnCluster.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__94f7e0fd5b6e6f11bedc1491fa3fcd71b6d3952bde7528e15d1a8c6ba920c2d4)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnCluster", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3feb05599a80fd6afb49d375809c21fdcc4484d3f74a6e1402b56899b6c96134)
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
            type_hints = cached_type_hints(_typecheckingstub__ba63217cbb03f08355ab95d9d4902990d481d1db62c7c343377cdcc3d2f84863)
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
        '''The Amazon Resource Name (ARN) of the cluster.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupPolicy")
    def attr_backup_policy(self) -> builtins.str:
        '''The cluster's backup policy.

        :cloudformationAttribute: BackupPolicy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupPolicy"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterId")
    def attr_cluster_id(self) -> builtins.str:
        '''The cluster's identifier (ID).

        :cloudformationAttribute: ClusterId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterId"))

    @builtins.property
    @jsii.member(jsii_name="attrSecurityGroup")
    def attr_security_group(self) -> builtins.str:
        '''The identifier (ID) of the cluster's security group.

        :cloudformationAttribute: SecurityGroup
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSecurityGroup"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The cluster's state.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrSubnetMapping")
    def attr_subnet_mapping(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''A map from availability zone to the cluster's subnet in that availability zone.

        :cloudformationAttribute: SubnetMapping
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrSubnetMapping"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcId")
    def attr_vpc_id(self) -> builtins.str:
        '''The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

        :cloudformationAttribute: VpcId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcId"))

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
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "_aws_cloudhsm_fe2add2e.ClusterReference":
        '''A reference to a Cluster resource.'''
        return typing.cast("_aws_cloudhsm_fe2add2e.ClusterReference", jsii.get(self, "clusterRef"))

    @builtins.property
    @jsii.member(jsii_name="hsmType")
    def hsm_type(self) -> builtins.str:
        '''The type of HSM to use in the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "hsmType"))

    @hsm_type.setter
    def hsm_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e0647f5f5813502cab7ad8655f908599ce680409806924f4d66a36d46068d2c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backupRetentionPolicy")
    def backup_retention_policy(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCluster.BackupRetentionPolicyProperty"]]:
        '''A policy that defines how the service retains backups.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCluster.BackupRetentionPolicyProperty"]], jsii.get(self, "backupRetentionPolicy"))

    @backup_retention_policy.setter
    def backup_retention_policy(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCluster.BackupRetentionPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fb5fc587b7585e41f2e1be3d7f4f1e811b567a635a9245ba81cf76b12c477be6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetentionPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> typing.Optional[builtins.str]:
        '''The mode to use in the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bc8aa4654961253c45d9693134f6a5be057e55764040c27d530bfde34d4af8f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkType")
    def network_type(self) -> typing.Optional[builtins.str]:
        '''The NetworkType to create a cluster with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkType"))

    @network_type.setter
    def network_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ed80e285fc0faa87bbcd7f225ff3c0a09d65cb073c983cb87263455d2af4a2f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identifiers (IDs) of the subnets where the cluster is created.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3c3aa2ce47988ad4a4a836b0090debe10f95b0ddbf6350f58107d7af75903487)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnCluster.TagsItemsProperty"]]:
        '''Tags to apply to the CloudHSM cluster.'''
        return typing.cast(typing.Optional[typing.List["CfnCluster.TagsItemsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnCluster.TagsItemsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8b939138dec4f688bf5ae2b98fc59c9210b97ebe512410ef517d5931f3802e3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudhsm.CfnCluster.BackupRetentionPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class BackupRetentionPolicyProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A policy that defines how the service retains backups.

            :param type: The type of backup retention policy.
            :param value: Use a value between 7 - 379.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudhsm-cluster-backupretentionpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudhsm as cloudhsm
                
                backup_retention_policy_property = cloudhsm.CfnCluster.BackupRetentionPolicyProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f1a0cd535445c3ffa28a33371f80762767a47fe01390a6b8b9d30407d9e8da19)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of backup retention policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudhsm-cluster-backupretentionpolicy.html#cfn-cloudhsm-cluster-backupretentionpolicy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''Use a value between 7 - 379.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudhsm-cluster-backupretentionpolicy.html#cfn-cloudhsm-cluster-backupretentionpolicy-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackupRetentionPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudhsm.CfnCluster.TagsItemsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsItemsProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: The key of the tag.
            :param value: The value of the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudhsm-cluster-tagsitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudhsm as cloudhsm
                
                tags_items_property = cloudhsm.CfnCluster.TagsItemsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8e1e81f7811e1923f2b0aa09efc876e3fe0fd18fedb776df7677d8ca73dd30e6)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key of the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudhsm-cluster-tagsitems.html#cfn-cloudhsm-cluster-tagsitems-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudhsm-cluster-tagsitems.html#cfn-cloudhsm-cluster-tagsitems-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudhsm.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "hsm_type": "hsmType",
        "backup_retention_policy": "backupRetentionPolicy",
        "mode": "mode",
        "network_type": "networkType",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        hsm_type: builtins.str,
        backup_retention_policy: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnCluster.BackupRetentionPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        mode: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnCluster.TagsItemsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param hsm_type: The type of HSM to use in the cluster.
        :param backup_retention_policy: A policy that defines how the service retains backups.
        :param mode: The mode to use in the cluster.
        :param network_type: The NetworkType to create a cluster with.
        :param subnet_ids: The identifiers (IDs) of the subnets where the cluster is created. You must specify at least one subnet.
        :param tags: Tags to apply to the CloudHSM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudhsm-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudhsm as cloudhsm
            
            cfn_cluster_props = cloudhsm.CfnClusterProps(
                hsm_type="hsmType",
            
                # the properties below are optional
                backup_retention_policy=cloudhsm.CfnCluster.BackupRetentionPolicyProperty(
                    type="type",
                    value="value"
                ),
                mode="mode",
                network_type="networkType",
                subnet_ids=["subnetIds"],
                tags=[cloudhsm.CfnCluster.TagsItemsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8b165d045780aca93291e44b2327386b2e7c73984ba7e4476cd9675c497e34ab)
            check_type(argname="argument hsm_type", value=hsm_type, expected_type=type_hints["hsm_type"])
            check_type(argname="argument backup_retention_policy", value=backup_retention_policy, expected_type=type_hints["backup_retention_policy"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument network_type", value=network_type, expected_type=type_hints["network_type"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hsm_type": hsm_type,
        }
        if backup_retention_policy is not None:
            self._values["backup_retention_policy"] = backup_retention_policy
        if mode is not None:
            self._values["mode"] = mode
        if network_type is not None:
            self._values["network_type"] = network_type
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def hsm_type(self) -> builtins.str:
        '''The type of HSM to use in the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudhsm-cluster.html#cfn-cloudhsm-cluster-hsmtype
        '''
        result = self._values.get("hsm_type")
        assert result is not None, "Required property 'hsm_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_retention_policy(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCluster.BackupRetentionPolicyProperty"]]:
        '''A policy that defines how the service retains backups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudhsm-cluster.html#cfn-cloudhsm-cluster-backupretentionpolicy
        '''
        result = self._values.get("backup_retention_policy")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnCluster.BackupRetentionPolicyProperty"]], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''The mode to use in the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudhsm-cluster.html#cfn-cloudhsm-cluster-mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_type(self) -> typing.Optional[builtins.str]:
        '''The NetworkType to create a cluster with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudhsm-cluster.html#cfn-cloudhsm-cluster-networktype
        '''
        result = self._values.get("network_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identifiers (IDs) of the subnets where the cluster is created.

        You must specify at least one subnet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudhsm-cluster.html#cfn-cloudhsm-cluster-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnCluster.TagsItemsProperty"]]:
        '''Tags to apply to the CloudHSM cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudhsm-cluster.html#cfn-cloudhsm-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["CfnCluster.TagsItemsProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
]

publication.publish()

def _typecheckingstub__11927f58ba0f3a3dce7a79e6251f010e6256babff3a1e40f8cd2ed87b54b77e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hsm_type: builtins.str,
    backup_retention_policy: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCluster.BackupRetentionPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mode: typing.Optional[builtins.str] = None,
    network_type: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnCluster.TagsItemsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de17c7d12050cab21b8fb5370239a83ddaee83ec8c5c608ad413b47686ba0fac(
    resource: _aws_cloudhsm_fe2add2e.IClusterRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94f7e0fd5b6e6f11bedc1491fa3fcd71b6d3952bde7528e15d1a8c6ba920c2d4(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3feb05599a80fd6afb49d375809c21fdcc4484d3f74a6e1402b56899b6c96134(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba63217cbb03f08355ab95d9d4902990d481d1db62c7c343377cdcc3d2f84863(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0647f5f5813502cab7ad8655f908599ce680409806924f4d66a36d46068d2c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5fc587b7585e41f2e1be3d7f4f1e811b567a635a9245ba81cf76b12c477be6(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnCluster.BackupRetentionPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc8aa4654961253c45d9693134f6a5be057e55764040c27d530bfde34d4af8f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed80e285fc0faa87bbcd7f225ff3c0a09d65cb073c983cb87263455d2af4a2f9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c3aa2ce47988ad4a4a836b0090debe10f95b0ddbf6350f58107d7af75903487(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b939138dec4f688bf5ae2b98fc59c9210b97ebe512410ef517d5931f3802e3c(
    value: typing.Optional[typing.List[CfnCluster.TagsItemsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a0cd535445c3ffa28a33371f80762767a47fe01390a6b8b9d30407d9e8da19(
    *,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e1e81f7811e1923f2b0aa09efc876e3fe0fd18fedb776df7677d8ca73dd30e6(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b165d045780aca93291e44b2327386b2e7c73984ba7e4476cd9675c497e34ab(
    *,
    hsm_type: builtins.str,
    backup_retention_policy: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnCluster.BackupRetentionPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mode: typing.Optional[builtins.str] = None,
    network_type: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnCluster.TagsItemsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
