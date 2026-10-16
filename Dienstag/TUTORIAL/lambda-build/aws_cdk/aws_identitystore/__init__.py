r'''
# AWS::IdentityStore Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_identitystore as identitystore
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IdentityStore construct libraries](https://constructs.dev/search?q=identitystore)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IdentityStore resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IdentityStore.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IdentityStore](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IdentityStore.html).

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
    import aws_cdk.interfaces.aws_identitystore as _aws_identitystore_22a099c6
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_identitystore_22a099c6 = _LazyImport("aws_cdk.interfaces.aws_identitystore")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_identitystore_22a099c6.IGroupRef)
class CfnGroup(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_identitystore.CfnGroup",
):
    '''A group object, which contains a specified group’s metadata and attributes.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html
    :cloudformationResource: AWS::IdentityStore::Group
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_identitystore as identitystore
        
        cfn_group = identitystore.CfnGroup(self, "MyCfnGroup",
            display_name="displayName",
            identity_store_id="identityStoreId",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        display_name: builtins.str,
        identity_store_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IdentityStore::Group``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param display_name: The display name value for the group. The length limit is 1,024 characters. This value can consist of letters, accented characters, symbols, numbers, punctuation, tab, new line, carriage return, space, and nonbreaking space in this attribute. This value is specified at the time the group is created and stored as an attribute of the group object in the identity store. Prefix search supports a maximum of 1,000 characters for the string.
        :param identity_store_id: The globally unique identifier for the identity store.
        :param description: A string containing the description of the group.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__37e27ff46dfa4082cad1981cc4ade1e2a9ce445cf9aad4a8eb75e162b9b429f1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(
            display_name=display_name,
            identity_store_id=identity_store_id,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForGroup")
    @builtins.classmethod
    def arn_for_group(
        cls,
        resource: "_aws_identitystore_22a099c6.IGroupRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__01ab3c0d3cca733429f775beb080c97f01d0699872b9a2cf17cb7dec5795d17c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForGroup", [resource]))

    @jsii.member(jsii_name="isCfnGroup")
    @builtins.classmethod
    def is_cfn_group(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGroup.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b25553d499e3434e811a8393022add9b93718a56b976df383923e4e30e5c468f)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGroup", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fd30cf433d0f11c47c01b425898b3b3494dae8561dd252ec97cb62a6f3ea01c0)
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
            type_hints = cached_type_hints(_typecheckingstub__181a3492db49132403d11a30d4f4ede267eaa3675413217fae9f2a57427d93a5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGroupId")
    def attr_group_id(self) -> builtins.str:
        '''The identifier of the newly created group in the identity store.

        :cloudformationAttribute: GroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGroupId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "_aws_identitystore_22a099c6.GroupReference":
        '''A reference to a Group resource.'''
        return typing.cast("_aws_identitystore_22a099c6.GroupReference", jsii.get(self, "groupRef"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The display name value for the group.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5e2f0d1e640344318d6ca1684bf877149c58a04ff3b658cc26437fd42577ae42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.'''
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1ec5af9bcaa29b5bd7b1489efc7cb2d8be21651e7c0abc6581d713983f718c75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A string containing the description of the group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__adb1a463b108d61759d25cd969fb5fed9a681bdbfadbf09cefe6655715c026df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_identitystore_22a099c6.IGroupMembershipRef)
class CfnGroupMembership(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_identitystore.CfnGroupMembership",
):
    '''Creates a relationship between a member and a group.

    The following identifiers must be specified: ``GroupId`` , ``IdentityStoreId`` , and ``MemberId`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html
    :cloudformationResource: AWS::IdentityStore::GroupMembership
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_identitystore as identitystore
        
        cfn_group_membership = identitystore.CfnGroupMembership(self, "MyCfnGroupMembership",
            group_id="groupId",
            identity_store_id="identityStoreId",
            member_id=identitystore.CfnGroupMembership.MemberIdProperty(
                user_id="userId"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        group_id: builtins.str,
        identity_store_id: builtins.str,
        member_id: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnGroupMembership.MemberIdProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::IdentityStore::GroupMembership``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param group_id: The identifier for a group in the identity store.
        :param identity_store_id: The globally unique identifier for the identity store.
        :param member_id: An object containing the identifier of a group member. Setting the ``MemberId`` 's ``UserId`` field to a specific User's ID indicates that user is a member of the group.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__76d55a804ce565c6f3a413944bff86b3236786318808951cf53ad4eff71316db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupMembershipProps(
            group_id=group_id, identity_store_id=identity_store_id, member_id=member_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForGroupMembership")
    @builtins.classmethod
    def arn_for_group_membership(
        cls,
        resource: "_aws_identitystore_22a099c6.IGroupMembershipRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7ff9fad22921b91752db10653f5c61dd0bc13a0bf8a3b3888623273813a4e50c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForGroupMembership", [resource]))

    @jsii.member(jsii_name="isCfnGroupMembership")
    @builtins.classmethod
    def is_cfn_group_membership(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGroupMembership.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dc267ec839f05f7b319ddb3ef057abfd744e9c55e1ac011a7d51c236a00817e1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGroupMembership", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9bbe599298882f9cb39ad950a183df2f00325817213542a0979da08b15e837de)
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
            type_hints = cached_type_hints(_typecheckingstub__f8c6b11b08fd290fc0948df25fb4993347b63ee62d6cc093b9fdb1639f9be8e9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipId")
    def attr_membership_id(self) -> builtins.str:
        '''The identifier for a ``GroupMembership`` in the identity store.

        :cloudformationAttribute: MembershipId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="groupMembershipRef")
    def group_membership_ref(
        self,
    ) -> "_aws_identitystore_22a099c6.GroupMembershipReference":
        '''A reference to a GroupMembership resource.'''
        return typing.cast("_aws_identitystore_22a099c6.GroupMembershipReference", jsii.get(self, "groupMembershipRef"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        '''The identifier for a group in the identity store.'''
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__84854d3f76ffaf3fcbc3f65a33c1661f74f5b69424e248ef1e8272d270ac7f78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.'''
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cbe6d44611bf93ff14a416179e20aded09542ea5eeadef3315ca4e2b9610a458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memberId")
    def member_id(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGroupMembership.MemberIdProperty"]:
        '''An object containing the identifier of a group member.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGroupMembership.MemberIdProperty"], jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGroupMembership.MemberIdProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1cf491e3e3c3bfc7f52caab31db7140718db94dfca804458b592c7195b7552ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberId", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_identitystore.CfnGroupMembership.MemberIdProperty",
        jsii_struct_bases=[],
        name_mapping={"user_id": "userId"},
    )
    class MemberIdProperty:
        def __init__(self, *, user_id: builtins.str) -> None:
            '''An object that contains the identifier of a group member.

            Setting the ``UserID`` field to the specific identifier for a user indicates that the user is a member of the group.

            :param user_id: An object containing the identifiers of resources that can be members.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-groupmembership-memberid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_identitystore as identitystore
                
                member_id_property = identitystore.CfnGroupMembership.MemberIdProperty(
                    user_id="userId"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__aa85e069965fcc2401129e3357a969b039233bb2ccffdd9a02afd5dde1c53e25)
                check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "user_id": user_id,
            }

        @builtins.property
        def user_id(self) -> builtins.str:
            '''An object containing the identifiers of resources that can be members.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-groupmembership-memberid.html#cfn-identitystore-groupmembership-memberid-userid
            '''
            result = self._values.get("user_id")
            assert result is not None, "Required property 'user_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_identitystore.CfnGroupMembershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_id": "groupId",
        "identity_store_id": "identityStoreId",
        "member_id": "memberId",
    },
)
class CfnGroupMembershipProps:
    def __init__(
        self,
        *,
        group_id: builtins.str,
        identity_store_id: builtins.str,
        member_id: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnGroupMembership.MemberIdProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnGroupMembership``.

        :param group_id: The identifier for a group in the identity store.
        :param identity_store_id: The globally unique identifier for the identity store.
        :param member_id: An object containing the identifier of a group member. Setting the ``MemberId`` 's ``UserId`` field to a specific User's ID indicates that user is a member of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_identitystore as identitystore
            
            cfn_group_membership_props = identitystore.CfnGroupMembershipProps(
                group_id="groupId",
                identity_store_id="identityStoreId",
                member_id=identitystore.CfnGroupMembership.MemberIdProperty(
                    user_id="userId"
                )
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__44a916716d7f3a98b073b5f0337cf90a6d86bd04dc851e6b431e842d7c7184b8)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
            "identity_store_id": identity_store_id,
            "member_id": member_id,
        }

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The identifier for a group in the identity store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-groupid
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-identitystoreid
        '''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGroupMembership.MemberIdProperty"]:
        '''An object containing the identifier of a group member.

        Setting the ``MemberId`` 's ``UserId`` field to a specific User's ID indicates that user is a member of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnGroupMembership.MemberIdProperty"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupMembershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_identitystore.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "identity_store_id": "identityStoreId",
        "description": "description",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        identity_store_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroup``.

        :param display_name: The display name value for the group. The length limit is 1,024 characters. This value can consist of letters, accented characters, symbols, numbers, punctuation, tab, new line, carriage return, space, and nonbreaking space in this attribute. This value is specified at the time the group is created and stored as an attribute of the group object in the identity store. Prefix search supports a maximum of 1,000 characters for the string.
        :param identity_store_id: The globally unique identifier for the identity store.
        :param description: A string containing the description of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_identitystore as identitystore
            
            cfn_group_props = identitystore.CfnGroupProps(
                display_name="displayName",
                identity_store_id="identityStoreId",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__84bf79ae8bc719d02791d6f72a1b629f44562f761a2049ee295009880b02ea18)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
            "identity_store_id": identity_store_id,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The display name value for the group.

        The length limit is 1,024 characters. This value can consist of letters, accented characters, symbols, numbers, punctuation, tab, new line, carriage return, space, and nonbreaking space in this attribute. This value is specified at the time the group is created and stored as an attribute of the group object in the identity store.

        Prefix search supports a maximum of 1,000 characters for the string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-identitystoreid
        '''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A string containing the description of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_identitystore_22a099c6.IUserRef)
class CfnUser(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_identitystore.CfnUser",
):
    '''Creates a user within the specified identity store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html
    :cloudformationResource: AWS::IdentityStore::User
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_identitystore as identitystore
        
        cfn_user = identitystore.CfnUser(self, "MyCfnUser",
            identity_store_id="identityStoreId",
        
            # the properties below are optional
            addresses=[identitystore.CfnUser.AddressesItemsProperty(
                country="country",
                formatted="formatted",
                locality="locality",
                postal_code="postalCode",
                primary=False,
                region="region",
                street_address="streetAddress",
                type="type"
            )],
            birthdate="birthdate",
            display_name="displayName",
            emails=[identitystore.CfnUser.EmailsItemsProperty(
                primary=False,
                type="type",
                value="value"
            )],
            locale="locale",
            name=identitystore.CfnUser.NameProperty(
                family_name="familyName",
                formatted="formatted",
                given_name="givenName",
                honorific_prefix="honorificPrefix",
                honorific_suffix="honorificSuffix",
                middle_name="middleName"
            ),
            nick_name="nickName",
            phone_numbers=[identitystore.CfnUser.PhoneNumbersItemsProperty(
                primary=False,
                type="type",
                value="value"
            )],
            photos=[identitystore.CfnUser.PhotosItemsProperty(
                value="value",
        
                # the properties below are optional
                display="display",
                primary=False,
                type="type"
            )],
            preferred_language="preferredLanguage",
            profile_url="profileUrl",
            roles=[identitystore.CfnUser.RolesItemsProperty(
                primary=False,
                type="type",
                value="value"
            )],
            timezone="timezone",
            title="title",
            user_name="userName",
            user_type="userType",
            website="website"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        identity_store_id: builtins.str,
        addresses: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.AddressesItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        birthdate: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        emails: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.EmailsItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        locale: typing.Optional[builtins.str] = None,
        name: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.NameProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        nick_name: typing.Optional[builtins.str] = None,
        phone_numbers: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.PhoneNumbersItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        photos: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.PhotosItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        preferred_language: typing.Optional[builtins.str] = None,
        profile_url: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.RolesItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
        website: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IdentityStore::User``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param identity_store_id: The globally unique identifier for the identity store.
        :param addresses: A list of addresses associated with the user.
        :param birthdate: The user's birthdate in YYYY-MM-DD format.
        :param display_name: A string containing the name of the user for display.
        :param emails: A list of email addresses associated with the user.
        :param locale: The geographical region or location of the user.
        :param name: The name of the user.
        :param nick_name: An alternate name for the user.
        :param phone_numbers: A list of phone numbers associated with the user.
        :param photos: A list of photos associated with the user.
        :param preferred_language: The preferred language of the user.
        :param profile_url: A URL associated with the user.
        :param roles: A list of roles associated with the user.
        :param timezone: The time zone for the user.
        :param title: The title of the user.
        :param user_name: A unique string used to identify the user.
        :param user_type: A string indicating the type of user.
        :param website: The user's personal website or blog URL.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0ff718e916c470bf747f4ae7e91ceaef6856ff010376310e89893a9a05751da6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            identity_store_id=identity_store_id,
            addresses=addresses,
            birthdate=birthdate,
            display_name=display_name,
            emails=emails,
            locale=locale,
            name=name,
            nick_name=nick_name,
            phone_numbers=phone_numbers,
            photos=photos,
            preferred_language=preferred_language,
            profile_url=profile_url,
            roles=roles,
            timezone=timezone,
            title=title,
            user_name=user_name,
            user_type=user_type,
            website=website,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForUser")
    @builtins.classmethod
    def arn_for_user(
        cls,
        resource: "_aws_identitystore_22a099c6.IUserRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__159f223fe8f174d77fa2870a2a1960e15fedc6c150f7f199a1989051d85a2e46)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForUser", [resource]))

    @jsii.member(jsii_name="isCfnUser")
    @builtins.classmethod
    def is_cfn_user(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnUser.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f88d43fb3928f91524606e4b1c9f8ddace15a1dd05b1718614e641e2d0fcf949)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnUser", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ce256358faacf521a3095747740aa6aaa55f5d0d94405eec388ef6531a5ead2c)
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
            type_hints = cached_type_hints(_typecheckingstub__66cf2a88185b02ade7b396144cc943cb814d4c6fa1f8445451ef9ce8ae00c9c7)
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
        '''The Amazon Resource Name (ARN) of the user.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time the user was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The identifier of the user or system that created the user.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The date and time the user was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedBy")
    def attr_updated_by(self) -> builtins.str:
        '''The identifier of the user or system that last updated the user.

        :cloudformationAttribute: UpdatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrUserId")
    def attr_user_id(self) -> builtins.str:
        '''The identifier for a user in the identity store.

        :cloudformationAttribute: UserId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserId"))

    @builtins.property
    @jsii.member(jsii_name="attrUserStatus")
    def attr_user_status(self) -> builtins.str:
        '''The current status of the user account.

        :cloudformationAttribute: UserStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "_aws_identitystore_22a099c6.UserReference":
        '''A reference to a User resource.'''
        return typing.cast("_aws_identitystore_22a099c6.UserReference", jsii.get(self, "userRef"))

    @builtins.property
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.'''
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__301900d33c75a62d1e3c1bd02c03f25b0d11bc589ec75f854ce7399b17f2826c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.AddressesItemsProperty"]]]]:
        '''A list of addresses associated with the user.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.AddressesItemsProperty"]]]], jsii.get(self, "addresses"))

    @addresses.setter
    def addresses(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.AddressesItemsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__66e5124c9e5a7c78e33df91e2e81046dd068c7e448ff1b2c1719dcf440af0c5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addresses", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="birthdate")
    def birthdate(self) -> typing.Optional[builtins.str]:
        '''The user's birthdate in YYYY-MM-DD format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "birthdate"))

    @birthdate.setter
    def birthdate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e2b5a11c29668b4b568184e7dc0a3f3489774c6b1f99ba18fb280a596a9bc522)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "birthdate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''A string containing the name of the user for display.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__45dc4f84fef48437c2a4a6f155c7f159b723f8daf007bfefb68bbb02438230c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="emails")
    def emails(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.EmailsItemsProperty"]]]]:
        '''A list of email addresses associated with the user.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.EmailsItemsProperty"]]]], jsii.get(self, "emails"))

    @emails.setter
    def emails(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.EmailsItemsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__41e7153616933de516f0ab5eabacc07e74bc9198c4fc9b6d7d6e963ab6a4f2da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emails", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="locale")
    def locale(self) -> typing.Optional[builtins.str]:
        '''The geographical region or location of the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locale"))

    @locale.setter
    def locale(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__143d1b357e325b4d0f4fbaf25498e93ae27b316db87d2b0a24c2ca3d32c0bea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locale", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.NameProperty"]]:
        '''The name of the user.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.NameProperty"]], jsii.get(self, "name"))

    @name.setter
    def name(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.NameProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__55a7971e0f81d1b982329593e6d3c02a126ac61dd7bfff8f570fc5f70599ed50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="nickName")
    def nick_name(self) -> typing.Optional[builtins.str]:
        '''An alternate name for the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nickName"))

    @nick_name.setter
    def nick_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9a979e88fa2913d9b4b68f6ba2abef40fa6fe90a3a763de28f88a867a0305d56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nickName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="phoneNumbers")
    def phone_numbers(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhoneNumbersItemsProperty"]]]]:
        '''A list of phone numbers associated with the user.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhoneNumbersItemsProperty"]]]], jsii.get(self, "phoneNumbers"))

    @phone_numbers.setter
    def phone_numbers(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhoneNumbersItemsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__482d17169fc7168926f2335e6f8fc648e43aa0b0fea16dc47f2fc67a13b2ec0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneNumbers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="photos")
    def photos(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhotosItemsProperty"]]]]:
        '''A list of photos associated with the user.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhotosItemsProperty"]]]], jsii.get(self, "photos"))

    @photos.setter
    def photos(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhotosItemsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ecc9aeaf0fdeb61c4a9e382987db4d57e3129fca4e373f98750e4f2ecf2b6c54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "photos", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="preferredLanguage")
    def preferred_language(self) -> typing.Optional[builtins.str]:
        '''The preferred language of the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredLanguage"))

    @preferred_language.setter
    def preferred_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3e16cde9732b2e609a5bc0b02bafa24e640d671c3001e82686337e7e5ad5ab85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredLanguage", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="profileUrl")
    def profile_url(self) -> typing.Optional[builtins.str]:
        '''A URL associated with the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileUrl"))

    @profile_url.setter
    def profile_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6001a7982fce667a4ed2f934f209accd5d58ba6916de42ce2df05df3c0c5d2e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.RolesItemsProperty"]]]]:
        '''A list of roles associated with the user.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.RolesItemsProperty"]]]], jsii.get(self, "roles"))

    @roles.setter
    def roles(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.RolesItemsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__405dc798ecf08df1750a0b40ca59618cea414ac55b836d62d3455ebdc910a556)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> typing.Optional[builtins.str]:
        '''The time zone for the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e2565fccd1d43245d2e1f04c999521a09ff1ea5c53c7d57bd9ee72f5283fd169)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> typing.Optional[builtins.str]:
        '''The title of the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "title"))

    @title.setter
    def title(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8ef9066c800099a8d07d7c473cce870dfb69299e4e351ad02795d8992f404e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> typing.Optional[builtins.str]:
        '''A unique string used to identify the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__85c505e17606aa59b1fea8eeb5349035b31eeebbf3110dfac5d1ad7db3409b93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userType")
    def user_type(self) -> typing.Optional[builtins.str]:
        '''A string indicating the type of user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userType"))

    @user_type.setter
    def user_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__810e987ecd3d4c4abb05fa5393cdd6cae64a7a7c2b526a2abd1c5086cf703793)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="website")
    def website(self) -> typing.Optional[builtins.str]:
        '''The user's personal website or blog URL.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "website"))

    @website.setter
    def website(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__921f82f7eea54d7e0e8a9cf502ce4c31968cb9144304f27f6ac6fcd0efb6ddcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "website", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_identitystore.CfnUser.AddressesItemsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "country": "country",
            "formatted": "formatted",
            "locality": "locality",
            "postal_code": "postalCode",
            "primary": "primary",
            "region": "region",
            "street_address": "streetAddress",
            "type": "type",
        },
    )
    class AddressesItemsProperty:
        def __init__(
            self,
            *,
            country: typing.Optional[builtins.str] = None,
            formatted: typing.Optional[builtins.str] = None,
            locality: typing.Optional[builtins.str] = None,
            postal_code: typing.Optional[builtins.str] = None,
            primary: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            region: typing.Optional[builtins.str] = None,
            street_address: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param country: The country of the address.
            :param formatted: A formatted version of the address for display.
            :param locality: A string of the address locality.
            :param postal_code: The postal code of the address.
            :param primary: Whether this is the primary address.
            :param region: The region of the address.
            :param street_address: The street of the address.
            :param type: The type of address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_identitystore as identitystore
                
                addresses_items_property = identitystore.CfnUser.AddressesItemsProperty(
                    country="country",
                    formatted="formatted",
                    locality="locality",
                    postal_code="postalCode",
                    primary=False,
                    region="region",
                    street_address="streetAddress",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e5a9c1a0848c4d913cf0a9dce65a757b291caca2d9cfa86f24a8a22ea5e1f024)
                check_type(argname="argument country", value=country, expected_type=type_hints["country"])
                check_type(argname="argument formatted", value=formatted, expected_type=type_hints["formatted"])
                check_type(argname="argument locality", value=locality, expected_type=type_hints["locality"])
                check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
                check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument street_address", value=street_address, expected_type=type_hints["street_address"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if country is not None:
                self._values["country"] = country
            if formatted is not None:
                self._values["formatted"] = formatted
            if locality is not None:
                self._values["locality"] = locality
            if postal_code is not None:
                self._values["postal_code"] = postal_code
            if primary is not None:
                self._values["primary"] = primary
            if region is not None:
                self._values["region"] = region
            if street_address is not None:
                self._values["street_address"] = street_address
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def country(self) -> typing.Optional[builtins.str]:
            '''The country of the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html#cfn-identitystore-user-addressesitems-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def formatted(self) -> typing.Optional[builtins.str]:
            '''A formatted version of the address for display.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html#cfn-identitystore-user-addressesitems-formatted
            '''
            result = self._values.get("formatted")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def locality(self) -> typing.Optional[builtins.str]:
            '''A string of the address locality.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html#cfn-identitystore-user-addressesitems-locality
            '''
            result = self._values.get("locality")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def postal_code(self) -> typing.Optional[builtins.str]:
            '''The postal code of the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html#cfn-identitystore-user-addressesitems-postalcode
            '''
            result = self._values.get("postal_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether this is the primary address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html#cfn-identitystore-user-addressesitems-primary
            '''
            result = self._values.get("primary")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The region of the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html#cfn-identitystore-user-addressesitems-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def street_address(self) -> typing.Optional[builtins.str]:
            '''The street of the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html#cfn-identitystore-user-addressesitems-streetaddress
            '''
            result = self._values.get("street_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-addressesitems.html#cfn-identitystore-user-addressesitems-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddressesItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_identitystore.CfnUser.EmailsItemsProperty",
        jsii_struct_bases=[],
        name_mapping={"primary": "primary", "type": "type", "value": "value"},
    )
    class EmailsItemsProperty:
        def __init__(
            self,
            *,
            primary: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param primary: Whether this is the primary email address.
            :param type: The type of email address.
            :param value: The email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-emailsitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_identitystore as identitystore
                
                emails_items_property = identitystore.CfnUser.EmailsItemsProperty(
                    primary=False,
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__5075658f0f13fa228bd4584159657fb117ad1bb8c481fc7d6c433c52de910dce)
                check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if primary is not None:
                self._values["primary"] = primary
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def primary(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether this is the primary email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-emailsitems.html#cfn-identitystore-user-emailsitems-primary
            '''
            result = self._values.get("primary")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-emailsitems.html#cfn-identitystore-user-emailsitems-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-emailsitems.html#cfn-identitystore-user-emailsitems-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmailsItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_identitystore.CfnUser.NameProperty",
        jsii_struct_bases=[],
        name_mapping={
            "family_name": "familyName",
            "formatted": "formatted",
            "given_name": "givenName",
            "honorific_prefix": "honorificPrefix",
            "honorific_suffix": "honorificSuffix",
            "middle_name": "middleName",
        },
    )
    class NameProperty:
        def __init__(
            self,
            *,
            family_name: typing.Optional[builtins.str] = None,
            formatted: typing.Optional[builtins.str] = None,
            given_name: typing.Optional[builtins.str] = None,
            honorific_prefix: typing.Optional[builtins.str] = None,
            honorific_suffix: typing.Optional[builtins.str] = None,
            middle_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The name of the user.

            :param family_name: The family name of the user.
            :param formatted: A string containing a formatted version of the name for display.
            :param given_name: The given name of the user.
            :param honorific_prefix: The honorific prefix of the user.
            :param honorific_suffix: The honorific suffix of the user.
            :param middle_name: The middle name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-name.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_identitystore as identitystore
                
                name_property = identitystore.CfnUser.NameProperty(
                    family_name="familyName",
                    formatted="formatted",
                    given_name="givenName",
                    honorific_prefix="honorificPrefix",
                    honorific_suffix="honorificSuffix",
                    middle_name="middleName"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__280987697b2c2798e1bab26544d03994214de75158ac9275891733771c7c32cd)
                check_type(argname="argument family_name", value=family_name, expected_type=type_hints["family_name"])
                check_type(argname="argument formatted", value=formatted, expected_type=type_hints["formatted"])
                check_type(argname="argument given_name", value=given_name, expected_type=type_hints["given_name"])
                check_type(argname="argument honorific_prefix", value=honorific_prefix, expected_type=type_hints["honorific_prefix"])
                check_type(argname="argument honorific_suffix", value=honorific_suffix, expected_type=type_hints["honorific_suffix"])
                check_type(argname="argument middle_name", value=middle_name, expected_type=type_hints["middle_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if family_name is not None:
                self._values["family_name"] = family_name
            if formatted is not None:
                self._values["formatted"] = formatted
            if given_name is not None:
                self._values["given_name"] = given_name
            if honorific_prefix is not None:
                self._values["honorific_prefix"] = honorific_prefix
            if honorific_suffix is not None:
                self._values["honorific_suffix"] = honorific_suffix
            if middle_name is not None:
                self._values["middle_name"] = middle_name

        @builtins.property
        def family_name(self) -> typing.Optional[builtins.str]:
            '''The family name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-name.html#cfn-identitystore-user-name-familyname
            '''
            result = self._values.get("family_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def formatted(self) -> typing.Optional[builtins.str]:
            '''A string containing a formatted version of the name for display.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-name.html#cfn-identitystore-user-name-formatted
            '''
            result = self._values.get("formatted")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def given_name(self) -> typing.Optional[builtins.str]:
            '''The given name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-name.html#cfn-identitystore-user-name-givenname
            '''
            result = self._values.get("given_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def honorific_prefix(self) -> typing.Optional[builtins.str]:
            '''The honorific prefix of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-name.html#cfn-identitystore-user-name-honorificprefix
            '''
            result = self._values.get("honorific_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def honorific_suffix(self) -> typing.Optional[builtins.str]:
            '''The honorific suffix of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-name.html#cfn-identitystore-user-name-honorificsuffix
            '''
            result = self._values.get("honorific_suffix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def middle_name(self) -> typing.Optional[builtins.str]:
            '''The middle name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-name.html#cfn-identitystore-user-name-middlename
            '''
            result = self._values.get("middle_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_identitystore.CfnUser.PhoneNumbersItemsProperty",
        jsii_struct_bases=[],
        name_mapping={"primary": "primary", "type": "type", "value": "value"},
    )
    class PhoneNumbersItemsProperty:
        def __init__(
            self,
            *,
            primary: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param primary: Whether this is the primary phone number.
            :param type: The type of phone number.
            :param value: The phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-phonenumbersitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_identitystore as identitystore
                
                phone_numbers_items_property = identitystore.CfnUser.PhoneNumbersItemsProperty(
                    primary=False,
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1c277dd8d024dd3214b233e33e406554dcbbef9673c9b5a007d8993f8f4ad3a8)
                check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if primary is not None:
                self._values["primary"] = primary
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def primary(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether this is the primary phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-phonenumbersitems.html#cfn-identitystore-user-phonenumbersitems-primary
            '''
            result = self._values.get("primary")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-phonenumbersitems.html#cfn-identitystore-user-phonenumbersitems-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-phonenumbersitems.html#cfn-identitystore-user-phonenumbersitems-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhoneNumbersItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_identitystore.CfnUser.PhotosItemsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "value": "value",
            "display": "display",
            "primary": "primary",
            "type": "type",
        },
    )
    class PhotosItemsProperty:
        def __init__(
            self,
            *,
            value: builtins.str,
            display: typing.Optional[builtins.str] = None,
            primary: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param value: The photo data or URL.
            :param display: A display name for the photo.
            :param primary: Whether this is the primary photo.
            :param type: The type of photo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-photositems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_identitystore as identitystore
                
                photos_items_property = identitystore.CfnUser.PhotosItemsProperty(
                    value="value",
                
                    # the properties below are optional
                    display="display",
                    primary=False,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a50d10d3e2588b6a4edea21018186d3d70e9dfcf5a70f3280499d22f08ed9d75)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument display", value=display, expected_type=type_hints["display"])
                check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }
            if display is not None:
                self._values["display"] = display
            if primary is not None:
                self._values["primary"] = primary
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def value(self) -> builtins.str:
            '''The photo data or URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-photositems.html#cfn-identitystore-user-photositems-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def display(self) -> typing.Optional[builtins.str]:
            '''A display name for the photo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-photositems.html#cfn-identitystore-user-photositems-display
            '''
            result = self._values.get("display")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether this is the primary photo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-photositems.html#cfn-identitystore-user-photositems-primary
            '''
            result = self._values.get("primary")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of photo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-photositems.html#cfn-identitystore-user-photositems-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhotosItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_identitystore.CfnUser.RolesItemsProperty",
        jsii_struct_bases=[],
        name_mapping={"primary": "primary", "type": "type", "value": "value"},
    )
    class RolesItemsProperty:
        def __init__(
            self,
            *,
            primary: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param primary: Whether this is the primary role.
            :param type: The type of role.
            :param value: The role name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-rolesitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_identitystore as identitystore
                
                roles_items_property = identitystore.CfnUser.RolesItemsProperty(
                    primary=False,
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__430033a6361487414084290e1a9ff6aa6fcd5faf6ce920cded586b061d5e6cd0)
                check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if primary is not None:
                self._values["primary"] = primary
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def primary(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether this is the primary role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-rolesitems.html#cfn-identitystore-user-rolesitems-primary
            '''
            result = self._values.get("primary")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-rolesitems.html#cfn-identitystore-user-rolesitems-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The role name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-user-rolesitems.html#cfn-identitystore-user-rolesitems-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RolesItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_identitystore.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "identity_store_id": "identityStoreId",
        "addresses": "addresses",
        "birthdate": "birthdate",
        "display_name": "displayName",
        "emails": "emails",
        "locale": "locale",
        "name": "name",
        "nick_name": "nickName",
        "phone_numbers": "phoneNumbers",
        "photos": "photos",
        "preferred_language": "preferredLanguage",
        "profile_url": "profileUrl",
        "roles": "roles",
        "timezone": "timezone",
        "title": "title",
        "user_name": "userName",
        "user_type": "userType",
        "website": "website",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        identity_store_id: builtins.str,
        addresses: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.AddressesItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        birthdate: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        emails: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.EmailsItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        locale: typing.Optional[builtins.str] = None,
        name: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.NameProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        nick_name: typing.Optional[builtins.str] = None,
        phone_numbers: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.PhoneNumbersItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        photos: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.PhotosItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        preferred_language: typing.Optional[builtins.str] = None,
        profile_url: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnUser.RolesItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
        website: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnUser``.

        :param identity_store_id: The globally unique identifier for the identity store.
        :param addresses: A list of addresses associated with the user.
        :param birthdate: The user's birthdate in YYYY-MM-DD format.
        :param display_name: A string containing the name of the user for display.
        :param emails: A list of email addresses associated with the user.
        :param locale: The geographical region or location of the user.
        :param name: The name of the user.
        :param nick_name: An alternate name for the user.
        :param phone_numbers: A list of phone numbers associated with the user.
        :param photos: A list of photos associated with the user.
        :param preferred_language: The preferred language of the user.
        :param profile_url: A URL associated with the user.
        :param roles: A list of roles associated with the user.
        :param timezone: The time zone for the user.
        :param title: The title of the user.
        :param user_name: A unique string used to identify the user.
        :param user_type: A string indicating the type of user.
        :param website: The user's personal website or blog URL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_identitystore as identitystore
            
            cfn_user_props = identitystore.CfnUserProps(
                identity_store_id="identityStoreId",
            
                # the properties below are optional
                addresses=[identitystore.CfnUser.AddressesItemsProperty(
                    country="country",
                    formatted="formatted",
                    locality="locality",
                    postal_code="postalCode",
                    primary=False,
                    region="region",
                    street_address="streetAddress",
                    type="type"
                )],
                birthdate="birthdate",
                display_name="displayName",
                emails=[identitystore.CfnUser.EmailsItemsProperty(
                    primary=False,
                    type="type",
                    value="value"
                )],
                locale="locale",
                name=identitystore.CfnUser.NameProperty(
                    family_name="familyName",
                    formatted="formatted",
                    given_name="givenName",
                    honorific_prefix="honorificPrefix",
                    honorific_suffix="honorificSuffix",
                    middle_name="middleName"
                ),
                nick_name="nickName",
                phone_numbers=[identitystore.CfnUser.PhoneNumbersItemsProperty(
                    primary=False,
                    type="type",
                    value="value"
                )],
                photos=[identitystore.CfnUser.PhotosItemsProperty(
                    value="value",
            
                    # the properties below are optional
                    display="display",
                    primary=False,
                    type="type"
                )],
                preferred_language="preferredLanguage",
                profile_url="profileUrl",
                roles=[identitystore.CfnUser.RolesItemsProperty(
                    primary=False,
                    type="type",
                    value="value"
                )],
                timezone="timezone",
                title="title",
                user_name="userName",
                user_type="userType",
                website="website"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d95946a0f7a571f039f89147aa94b1da9ef7cf33a8412bc07c86501b7afdca16)
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
            check_type(argname="argument birthdate", value=birthdate, expected_type=type_hints["birthdate"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument emails", value=emails, expected_type=type_hints["emails"])
            check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument nick_name", value=nick_name, expected_type=type_hints["nick_name"])
            check_type(argname="argument phone_numbers", value=phone_numbers, expected_type=type_hints["phone_numbers"])
            check_type(argname="argument photos", value=photos, expected_type=type_hints["photos"])
            check_type(argname="argument preferred_language", value=preferred_language, expected_type=type_hints["preferred_language"])
            check_type(argname="argument profile_url", value=profile_url, expected_type=type_hints["profile_url"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument user_type", value=user_type, expected_type=type_hints["user_type"])
            check_type(argname="argument website", value=website, expected_type=type_hints["website"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_store_id": identity_store_id,
        }
        if addresses is not None:
            self._values["addresses"] = addresses
        if birthdate is not None:
            self._values["birthdate"] = birthdate
        if display_name is not None:
            self._values["display_name"] = display_name
        if emails is not None:
            self._values["emails"] = emails
        if locale is not None:
            self._values["locale"] = locale
        if name is not None:
            self._values["name"] = name
        if nick_name is not None:
            self._values["nick_name"] = nick_name
        if phone_numbers is not None:
            self._values["phone_numbers"] = phone_numbers
        if photos is not None:
            self._values["photos"] = photos
        if preferred_language is not None:
            self._values["preferred_language"] = preferred_language
        if profile_url is not None:
            self._values["profile_url"] = profile_url
        if roles is not None:
            self._values["roles"] = roles
        if timezone is not None:
            self._values["timezone"] = timezone
        if title is not None:
            self._values["title"] = title
        if user_name is not None:
            self._values["user_name"] = user_name
        if user_type is not None:
            self._values["user_type"] = user_type
        if website is not None:
            self._values["website"] = website

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''The globally unique identifier for the identity store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-identitystoreid
        '''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addresses(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.AddressesItemsProperty"]]]]:
        '''A list of addresses associated with the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-addresses
        '''
        result = self._values.get("addresses")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.AddressesItemsProperty"]]]], result)

    @builtins.property
    def birthdate(self) -> typing.Optional[builtins.str]:
        '''The user's birthdate in YYYY-MM-DD format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-birthdate
        '''
        result = self._values.get("birthdate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''A string containing the name of the user for display.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emails(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.EmailsItemsProperty"]]]]:
        '''A list of email addresses associated with the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-emails
        '''
        result = self._values.get("emails")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.EmailsItemsProperty"]]]], result)

    @builtins.property
    def locale(self) -> typing.Optional[builtins.str]:
        '''The geographical region or location of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-locale
        '''
        result = self._values.get("locale")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.NameProperty"]]:
        '''The name of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.NameProperty"]], result)

    @builtins.property
    def nick_name(self) -> typing.Optional[builtins.str]:
        '''An alternate name for the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-nickname
        '''
        result = self._values.get("nick_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phone_numbers(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhoneNumbersItemsProperty"]]]]:
        '''A list of phone numbers associated with the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-phonenumbers
        '''
        result = self._values.get("phone_numbers")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhoneNumbersItemsProperty"]]]], result)

    @builtins.property
    def photos(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhotosItemsProperty"]]]]:
        '''A list of photos associated with the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-photos
        '''
        result = self._values.get("photos")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.PhotosItemsProperty"]]]], result)

    @builtins.property
    def preferred_language(self) -> typing.Optional[builtins.str]:
        '''The preferred language of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-preferredlanguage
        '''
        result = self._values.get("preferred_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile_url(self) -> typing.Optional[builtins.str]:
        '''A URL associated with the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-profileurl
        '''
        result = self._values.get("profile_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.RolesItemsProperty"]]]]:
        '''A list of roles associated with the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnUser.RolesItemsProperty"]]]], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''The time zone for the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-timezone
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''The title of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''A unique string used to identify the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-username
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_type(self) -> typing.Optional[builtins.str]:
        '''A string indicating the type of user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-usertype
        '''
        result = self._values.get("user_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def website(self) -> typing.Optional[builtins.str]:
        '''The user's personal website or blog URL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-user.html#cfn-identitystore-user-website
        '''
        result = self._values.get("website")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGroup",
    "CfnGroupMembership",
    "CfnGroupMembershipProps",
    "CfnGroupProps",
    "CfnUser",
    "CfnUserProps",
]

publication.publish()

def _typecheckingstub__37e27ff46dfa4082cad1981cc4ade1e2a9ce445cf9aad4a8eb75e162b9b429f1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    display_name: builtins.str,
    identity_store_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01ab3c0d3cca733429f775beb080c97f01d0699872b9a2cf17cb7dec5795d17c(
    resource: _aws_identitystore_22a099c6.IGroupRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25553d499e3434e811a8393022add9b93718a56b976df383923e4e30e5c468f(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd30cf433d0f11c47c01b425898b3b3494dae8561dd252ec97cb62a6f3ea01c0(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__181a3492db49132403d11a30d4f4ede267eaa3675413217fae9f2a57427d93a5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2f0d1e640344318d6ca1684bf877149c58a04ff3b658cc26437fd42577ae42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ec5af9bcaa29b5bd7b1489efc7cb2d8be21651e7c0abc6581d713983f718c75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb1a463b108d61759d25cd969fb5fed9a681bdbfadbf09cefe6655715c026df(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76d55a804ce565c6f3a413944bff86b3236786318808951cf53ad4eff71316db(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_id: builtins.str,
    identity_store_id: builtins.str,
    member_id: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnGroupMembership.MemberIdProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff9fad22921b91752db10653f5c61dd0bc13a0bf8a3b3888623273813a4e50c(
    resource: _aws_identitystore_22a099c6.IGroupMembershipRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc267ec839f05f7b319ddb3ef057abfd744e9c55e1ac011a7d51c236a00817e1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bbe599298882f9cb39ad950a183df2f00325817213542a0979da08b15e837de(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c6b11b08fd290fc0948df25fb4993347b63ee62d6cc093b9fdb1639f9be8e9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84854d3f76ffaf3fcbc3f65a33c1661f74f5b69424e248ef1e8272d270ac7f78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe6d44611bf93ff14a416179e20aded09542ea5eeadef3315ca4e2b9610a458(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cf491e3e3c3bfc7f52caab31db7140718db94dfca804458b592c7195b7552ec(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnGroupMembership.MemberIdProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa85e069965fcc2401129e3357a969b039233bb2ccffdd9a02afd5dde1c53e25(
    *,
    user_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a916716d7f3a98b073b5f0337cf90a6d86bd04dc851e6b431e842d7c7184b8(
    *,
    group_id: builtins.str,
    identity_store_id: builtins.str,
    member_id: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnGroupMembership.MemberIdProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84bf79ae8bc719d02791d6f72a1b629f44562f761a2049ee295009880b02ea18(
    *,
    display_name: builtins.str,
    identity_store_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ff718e916c470bf747f4ae7e91ceaef6856ff010376310e89893a9a05751da6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identity_store_id: builtins.str,
    addresses: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.AddressesItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    birthdate: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    emails: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.EmailsItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    locale: typing.Optional[builtins.str] = None,
    name: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.NameProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    nick_name: typing.Optional[builtins.str] = None,
    phone_numbers: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.PhoneNumbersItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    photos: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.PhotosItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    preferred_language: typing.Optional[builtins.str] = None,
    profile_url: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.RolesItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    timezone: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    user_name: typing.Optional[builtins.str] = None,
    user_type: typing.Optional[builtins.str] = None,
    website: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159f223fe8f174d77fa2870a2a1960e15fedc6c150f7f199a1989051d85a2e46(
    resource: _aws_identitystore_22a099c6.IUserRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f88d43fb3928f91524606e4b1c9f8ddace15a1dd05b1718614e641e2d0fcf949(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce256358faacf521a3095747740aa6aaa55f5d0d94405eec388ef6531a5ead2c(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66cf2a88185b02ade7b396144cc943cb814d4c6fa1f8445451ef9ce8ae00c9c7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__301900d33c75a62d1e3c1bd02c03f25b0d11bc589ec75f854ce7399b17f2826c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e5124c9e5a7c78e33df91e2e81046dd068c7e448ff1b2c1719dcf440af0c5e(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnUser.AddressesItemsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b5a11c29668b4b568184e7dc0a3f3489774c6b1f99ba18fb280a596a9bc522(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45dc4f84fef48437c2a4a6f155c7f159b723f8daf007bfefb68bbb02438230c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41e7153616933de516f0ab5eabacc07e74bc9198c4fc9b6d7d6e963ab6a4f2da(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnUser.EmailsItemsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143d1b357e325b4d0f4fbaf25498e93ae27b316db87d2b0a24c2ca3d32c0bea1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55a7971e0f81d1b982329593e6d3c02a126ac61dd7bfff8f570fc5f70599ed50(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnUser.NameProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a979e88fa2913d9b4b68f6ba2abef40fa6fe90a3a763de28f88a867a0305d56(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__482d17169fc7168926f2335e6f8fc648e43aa0b0fea16dc47f2fc67a13b2ec0f(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnUser.PhoneNumbersItemsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc9aeaf0fdeb61c4a9e382987db4d57e3129fca4e373f98750e4f2ecf2b6c54(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnUser.PhotosItemsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e16cde9732b2e609a5bc0b02bafa24e640d671c3001e82686337e7e5ad5ab85(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6001a7982fce667a4ed2f934f209accd5d58ba6916de42ce2df05df3c0c5d2e5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405dc798ecf08df1750a0b40ca59618cea414ac55b836d62d3455ebdc910a556(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnUser.RolesItemsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2565fccd1d43245d2e1f04c999521a09ff1ea5c53c7d57bd9ee72f5283fd169(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ef9066c800099a8d07d7c473cce870dfb69299e4e351ad02795d8992f404e00(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85c505e17606aa59b1fea8eeb5349035b31eeebbf3110dfac5d1ad7db3409b93(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__810e987ecd3d4c4abb05fa5393cdd6cae64a7a7c2b526a2abd1c5086cf703793(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921f82f7eea54d7e0e8a9cf502ce4c31968cb9144304f27f6ac6fcd0efb6ddcf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a9c1a0848c4d913cf0a9dce65a757b291caca2d9cfa86f24a8a22ea5e1f024(
    *,
    country: typing.Optional[builtins.str] = None,
    formatted: typing.Optional[builtins.str] = None,
    locality: typing.Optional[builtins.str] = None,
    postal_code: typing.Optional[builtins.str] = None,
    primary: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    region: typing.Optional[builtins.str] = None,
    street_address: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5075658f0f13fa228bd4584159657fb117ad1bb8c481fc7d6c433c52de910dce(
    *,
    primary: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__280987697b2c2798e1bab26544d03994214de75158ac9275891733771c7c32cd(
    *,
    family_name: typing.Optional[builtins.str] = None,
    formatted: typing.Optional[builtins.str] = None,
    given_name: typing.Optional[builtins.str] = None,
    honorific_prefix: typing.Optional[builtins.str] = None,
    honorific_suffix: typing.Optional[builtins.str] = None,
    middle_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c277dd8d024dd3214b233e33e406554dcbbef9673c9b5a007d8993f8f4ad3a8(
    *,
    primary: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a50d10d3e2588b6a4edea21018186d3d70e9dfcf5a70f3280499d22f08ed9d75(
    *,
    value: builtins.str,
    display: typing.Optional[builtins.str] = None,
    primary: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__430033a6361487414084290e1a9ff6aa6fcd5faf6ce920cded586b061d5e6cd0(
    *,
    primary: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d95946a0f7a571f039f89147aa94b1da9ef7cf33a8412bc07c86501b7afdca16(
    *,
    identity_store_id: builtins.str,
    addresses: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.AddressesItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    birthdate: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    emails: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.EmailsItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    locale: typing.Optional[builtins.str] = None,
    name: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.NameProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    nick_name: typing.Optional[builtins.str] = None,
    phone_numbers: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.PhoneNumbersItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    photos: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.PhotosItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    preferred_language: typing.Optional[builtins.str] = None,
    profile_url: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnUser.RolesItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    timezone: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    user_name: typing.Optional[builtins.str] = None,
    user_type: typing.Optional[builtins.str] = None,
    website: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
