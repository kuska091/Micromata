r'''
# AWS::LicenseManager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_licensemanager as licensemanager
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LicenseManager construct libraries](https://constructs.dev/search?q=licensemanager)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LicenseManager resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LicenseManager.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LicenseManager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LicenseManager.html).

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
    import aws_cdk.interfaces.aws_licensemanager as _aws_licensemanager_19fc2853
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_licensemanager_19fc2853 = _LazyImport("aws_cdk.interfaces.aws_licensemanager")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_licensemanager_19fc2853.IGrantRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnGrant(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnGrant",
):
    '''Specifies a grant.

    A grant shares the use of license entitlements with specific AWS accounts . For more information, see `Granted licenses <https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html>`_ in the *License Manager User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html
    :cloudformationResource: AWS::LicenseManager::Grant
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_licensemanager as licensemanager
        
        cfn_grant = licensemanager.CfnGrant(self, "MyCfnGrant",
            allowed_operations=["allowedOperations"],
            grant_name="grantName",
            home_region="homeRegion",
            license_arn="licenseArn",
            principals=["principals"],
            status="status",
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
        allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
        grant_name: typing.Optional[builtins.str] = None,
        home_region: typing.Optional[builtins.str] = None,
        license_arn: typing.Optional[builtins.str] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::LicenseManager::Grant``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param allowed_operations: Allowed operations for the grant.
        :param grant_name: Grant name.
        :param home_region: Home Region of the grant.
        :param license_arn: License ARN.
        :param principals: The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):. - An AWS account, which includes only the account specified. - An organizational unit (OU), which includes all accounts in the OU. - An organization, which will include all accounts across your organization.
        :param status: Granted license status.
        :param tags: A list of tags to attach.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e8429ee81c009103dd15c76170dfb52e5ca38f72a8912b82d6e63e3f460c3022)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGrantProps(
            allowed_operations=allowed_operations,
            grant_name=grant_name,
            home_region=home_region,
            license_arn=license_arn,
            principals=principals,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForGrant")
    @builtins.classmethod
    def arn_for_grant(
        cls,
        resource: "_aws_licensemanager_19fc2853.IGrantRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d75a1343afb37f47732759e1bffa4521f7146f8652ca23eb417d8545df2c5632)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForGrant", [resource]))

    @jsii.member(jsii_name="isCfnGrant")
    @builtins.classmethod
    def is_cfn_grant(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGrant.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__77395be3520b17c3fdb320cd771bc776e8d38fcf1699b4649b0b02baeb512632)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGrant", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__06f3d843a99f00dd40b93f69a334bda31af66745c91ef0da13aef948b5e7cd3b)
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
            type_hints = cached_type_hints(_typecheckingstub__2f21921653469c34829dafde09a61b6573c5caa1cd6413329ac50f150c61edce)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGrantArn")
    def attr_grant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the grant.

        :cloudformationAttribute: GrantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGrantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        '''The grant version.

        :cloudformationAttribute: Version
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersion"))

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
    @jsii.member(jsii_name="grantRef")
    def grant_ref(self) -> "_aws_licensemanager_19fc2853.GrantReference":
        '''A reference to a Grant resource.'''
        return typing.cast("_aws_licensemanager_19fc2853.GrantReference", jsii.get(self, "grantRef"))

    @builtins.property
    @jsii.member(jsii_name="allowedOperations")
    def allowed_operations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Allowed operations for the grant.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOperations"))

    @allowed_operations.setter
    def allowed_operations(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0365c0a6e5122b9fa8e724dcae1d11a86ea3be7b9c43576ae3984046a8a866a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOperations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="grantName")
    def grant_name(self) -> typing.Optional[builtins.str]:
        '''Grant name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grantName"))

    @grant_name.setter
    def grant_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5f4a134c7bb2f22cd48211ed5100e65a75fc658d9d8f836ea5c12000691c0cb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grantName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="homeRegion")
    def home_region(self) -> typing.Optional[builtins.str]:
        '''Home Region of the grant.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeRegion"))

    @home_region.setter
    def home_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5031789a0d9f35bd09ee7810379dcbe0da55436888a38e9623b68c7226da0990)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licenseArn")
    def license_arn(self) -> typing.Optional[builtins.str]:
        '''License ARN.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseArn"))

    @license_arn.setter
    def license_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e9ad1871340fca01eaad30a6180a827f5d9f498e7a913dbc15898d39ace8e741)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="principals")
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The grant principals.

        You can specify one of the following as an Amazon Resource Name (ARN):.
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "principals"))

    @principals.setter
    def principals(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2c571a4cf4f9bf1814a1015ca4a37680ca14b1356d42232abd8a71042c1e07bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principals", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''Granted license status.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__979cc3eeb34a65f4beb72557bbf7486f2c8b526da9a872d958b13f140f65edb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of tags to attach.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__25ecdb93f9976dac7ee80e59b54502ad27f8d5b03ad158b0d7b9624810f732c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnGrantProps",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_operations": "allowedOperations",
        "grant_name": "grantName",
        "home_region": "homeRegion",
        "license_arn": "licenseArn",
        "principals": "principals",
        "status": "status",
        "tags": "tags",
    },
)
class CfnGrantProps:
    def __init__(
        self,
        *,
        allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
        grant_name: typing.Optional[builtins.str] = None,
        home_region: typing.Optional[builtins.str] = None,
        license_arn: typing.Optional[builtins.str] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGrant``.

        :param allowed_operations: Allowed operations for the grant.
        :param grant_name: Grant name.
        :param home_region: Home Region of the grant.
        :param license_arn: License ARN.
        :param principals: The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):. - An AWS account, which includes only the account specified. - An organizational unit (OU), which includes all accounts in the OU. - An organization, which will include all accounts across your organization.
        :param status: Granted license status.
        :param tags: A list of tags to attach.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_licensemanager as licensemanager
            
            cfn_grant_props = licensemanager.CfnGrantProps(
                allowed_operations=["allowedOperations"],
                grant_name="grantName",
                home_region="homeRegion",
                license_arn="licenseArn",
                principals=["principals"],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__55c62319564e7f4daffb2869290c03b511d6440828cc8d89ddb4e628ea3e0f93)
            check_type(argname="argument allowed_operations", value=allowed_operations, expected_type=type_hints["allowed_operations"])
            check_type(argname="argument grant_name", value=grant_name, expected_type=type_hints["grant_name"])
            check_type(argname="argument home_region", value=home_region, expected_type=type_hints["home_region"])
            check_type(argname="argument license_arn", value=license_arn, expected_type=type_hints["license_arn"])
            check_type(argname="argument principals", value=principals, expected_type=type_hints["principals"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowed_operations is not None:
            self._values["allowed_operations"] = allowed_operations
        if grant_name is not None:
            self._values["grant_name"] = grant_name
        if home_region is not None:
            self._values["home_region"] = home_region
        if license_arn is not None:
            self._values["license_arn"] = license_arn
        if principals is not None:
            self._values["principals"] = principals
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def allowed_operations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Allowed operations for the grant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-allowedoperations
        '''
        result = self._values.get("allowed_operations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def grant_name(self) -> typing.Optional[builtins.str]:
        '''Grant name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-grantname
        '''
        result = self._values.get("grant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_region(self) -> typing.Optional[builtins.str]:
        '''Home Region of the grant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-homeregion
        '''
        result = self._values.get("home_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_arn(self) -> typing.Optional[builtins.str]:
        '''License ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-licensearn
        '''
        result = self._values.get("license_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):.

        - An AWS account, which includes only the account specified.
        - An organizational unit (OU), which includes all accounts in the OU.
        - An organization, which will include all accounts across your organization.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-principals
        '''
        result = self._values.get("principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Granted license status.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of tags to attach.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGrantProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_licensemanager_19fc2853.ILicenseRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnLicense(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense",
):
    '''Specifies a granted license.

    Granted licenses are licenses for products that your organization purchased from AWS Marketplace or directly from a seller who integrated their software with managed entitlements. For more information, see `Granted licenses <https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html>`_ in the *License Manager User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html
    :cloudformationResource: AWS::LicenseManager::License
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_licensemanager as licensemanager
        
        cfn_license = licensemanager.CfnLicense(self, "MyCfnLicense",
            beneficiary="beneficiary",
            consumption_configuration=licensemanager.CfnLicense.ConsumptionConfigurationProperty(
                borrow_configuration=licensemanager.CfnLicense.BorrowConfigurationProperty(
                    allow_early_check_in=False,
                    max_time_to_live_in_minutes=123
                ),
                provisional_configuration=licensemanager.CfnLicense.ProvisionalConfigurationProperty(
                    max_time_to_live_in_minutes=123
                ),
                renew_type="renewType"
            ),
            entitlements=[licensemanager.CfnLicense.EntitlementProperty(
                name="name",
                unit="unit",
        
                # the properties below are optional
                allow_check_in=False,
                max_count=123,
                overage=False,
                value="value"
            )],
            home_region="homeRegion",
            issuer=licensemanager.CfnLicense.IssuerDataProperty(
                name="name",
        
                # the properties below are optional
                sign_key="signKey"
            ),
            license_name="licenseName",
            product_name="productName",
            product_sku="productSku",
            validity=licensemanager.CfnLicense.ValidityDateFormatProperty(
                begin="begin",
                end="end"
            ),
        
            # the properties below are optional
            license_metadata=[licensemanager.CfnLicense.MetadataProperty(
                name="name",
                value="value"
            )],
            status="status",
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
        beneficiary: builtins.str,
        consumption_configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.ConsumptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        entitlements: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.EntitlementProperty", typing.Dict[builtins.str, typing.Any]]]]],
        home_region: builtins.str,
        issuer: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.IssuerDataProperty", typing.Dict[builtins.str, typing.Any]]],
        license_name: builtins.str,
        product_name: builtins.str,
        product_sku: builtins.str,
        validity: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.ValidityDateFormatProperty", typing.Dict[builtins.str, typing.Any]]],
        license_metadata: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.MetadataProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::LicenseManager::License``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param beneficiary: License beneficiary.
        :param consumption_configuration: Configuration for consumption of the license.
        :param entitlements: License entitlements.
        :param home_region: Home Region of the license.
        :param issuer: License issuer.
        :param license_name: License name.
        :param product_name: Product name.
        :param product_sku: Product SKU.
        :param validity: Date and time range during which the license is valid, in ISO8601-UTC format.
        :param license_metadata: License metadata.
        :param status: License status.
        :param tags: A list of tags to attach.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4fa5716b8b0216bdd1da1f12239ad6038aa037294da7f4a1f0215f1b16622526)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLicenseProps(
            beneficiary=beneficiary,
            consumption_configuration=consumption_configuration,
            entitlements=entitlements,
            home_region=home_region,
            issuer=issuer,
            license_name=license_name,
            product_name=product_name,
            product_sku=product_sku,
            validity=validity,
            license_metadata=license_metadata,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLicense")
    @builtins.classmethod
    def arn_for_license(
        cls,
        resource: "_aws_licensemanager_19fc2853.ILicenseRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__edbf08bc914e74c1bdf307cc4a134bf853aec8fa0fa88bdae05d34aad073560d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForLicense", [resource]))

    @jsii.member(jsii_name="isCfnLicense")
    @builtins.classmethod
    def is_cfn_license(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnLicense.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__44c0864b8227060c52869733f29658cb579ea455300bf39ad4a797305bc4a646)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnLicense", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c9cd2d3dab3901b09367da6f6bc033c9f014286742aa8f85c2c7a6834c1b1512)
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
            type_hints = cached_type_hints(_typecheckingstub__f5b3e1a3ed6019a3b4d49c9c0479889cc544e9ecc5ed6f1e04e62407fc3377a9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLicenseArn")
    def attr_license_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the license.

        :cloudformationAttribute: LicenseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLicenseArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        '''The license version.

        :cloudformationAttribute: Version
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersion"))

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
    @jsii.member(jsii_name="licenseRef")
    def license_ref(self) -> "_aws_licensemanager_19fc2853.LicenseReference":
        '''A reference to a License resource.'''
        return typing.cast("_aws_licensemanager_19fc2853.LicenseReference", jsii.get(self, "licenseRef"))

    @builtins.property
    @jsii.member(jsii_name="beneficiary")
    def beneficiary(self) -> builtins.str:
        '''License beneficiary.'''
        return typing.cast(builtins.str, jsii.get(self, "beneficiary"))

    @beneficiary.setter
    def beneficiary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bf9994475a7c52b73f7bc27dcb24ebe97709f2662d5138be4da7b3c42265936d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "beneficiary", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="consumptionConfiguration")
    def consumption_configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ConsumptionConfigurationProperty"]:
        '''Configuration for consumption of the license.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ConsumptionConfigurationProperty"], jsii.get(self, "consumptionConfiguration"))

    @consumption_configuration.setter
    def consumption_configuration(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ConsumptionConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__284aa1e5a6876d4f451b6e5e8f93fdb375fc583828e7e8d36f280d50e762d790)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="entitlements")
    def entitlements(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.EntitlementProperty"]]]:
        '''License entitlements.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.EntitlementProperty"]]], jsii.get(self, "entitlements"))

    @entitlements.setter
    def entitlements(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.EntitlementProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__73e1a84fbc6ca70d5dacac620ef3f77aa87a4d9b60385a5f2899f10ab1aefd7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entitlements", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="homeRegion")
    def home_region(self) -> builtins.str:
        '''Home Region of the license.'''
        return typing.cast(builtins.str, jsii.get(self, "homeRegion"))

    @home_region.setter
    def home_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__543ec2abfa87082c6465bd9aa1ff4096a9a5ba669d3147343b69c96ff2f90d67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.IssuerDataProperty"]:
        '''License issuer.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.IssuerDataProperty"], jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.IssuerDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d8b07f82f3d197d61c5edecbc56261a03ad65f4f99d1bb7a3c7b629126bb6ce9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licenseName")
    def license_name(self) -> builtins.str:
        '''License name.'''
        return typing.cast(builtins.str, jsii.get(self, "licenseName"))

    @license_name.setter
    def license_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3e97ac745c4faabd1c139a343ce905672f7e647741a9827bd7f203b40fb8f01c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="productName")
    def product_name(self) -> builtins.str:
        '''Product name.'''
        return typing.cast(builtins.str, jsii.get(self, "productName"))

    @product_name.setter
    def product_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a2a880e38bf22471203328b40fbe7cfbc719574af83c33d27bfb321c125d66fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="productSku")
    def product_sku(self) -> builtins.str:
        '''Product SKU.'''
        return typing.cast(builtins.str, jsii.get(self, "productSku"))

    @product_sku.setter
    def product_sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0e5b8b4e9b80cb8b0305a292b6c390efd67f677abdb467395dc1e4b849b9c418)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productSku", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="validity")
    def validity(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ValidityDateFormatProperty"]:
        '''Date and time range during which the license is valid, in ISO8601-UTC format.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ValidityDateFormatProperty"], jsii.get(self, "validity"))

    @validity.setter
    def validity(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ValidityDateFormatProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__14bfd7eea976b95153acfc2c36f571a86f5e204050b842561bf3f488085a466b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licenseMetadata")
    def license_metadata(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.MetadataProperty"]]]]:
        '''License metadata.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.MetadataProperty"]]]], jsii.get(self, "licenseMetadata"))

    @license_metadata.setter
    def license_metadata(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.MetadataProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5c94759710766169f67f670504ad6a0d56a36207b2a7008e6962da6595d9b62f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseMetadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''License status.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f3a0bb88a6f2431e141da5aa1e0e1d94957e1ec7a904c8a0b4f79254b7ef6f01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of tags to attach.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d3d5654748f0ba764790ff72d866ee568074e0ba162b9ce72977bba8050b12fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.BorrowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_early_check_in": "allowEarlyCheckIn",
            "max_time_to_live_in_minutes": "maxTimeToLiveInMinutes",
        },
    )
    class BorrowConfigurationProperty:
        def __init__(
            self,
            *,
            allow_early_check_in: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
            max_time_to_live_in_minutes: jsii.Number,
        ) -> None:
            '''Details about a borrow configuration.

            :param allow_early_check_in: Indicates whether early check-ins are allowed.
            :param max_time_to_live_in_minutes: Maximum time for the borrow configuration, in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                borrow_configuration_property = licensemanager.CfnLicense.BorrowConfigurationProperty(
                    allow_early_check_in=False,
                    max_time_to_live_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6e1d045a93aaf4354921dc5e95316f2bc7fa071c999fdf4edaa837886e37fb65)
                check_type(argname="argument allow_early_check_in", value=allow_early_check_in, expected_type=type_hints["allow_early_check_in"])
                check_type(argname="argument max_time_to_live_in_minutes", value=max_time_to_live_in_minutes, expected_type=type_hints["max_time_to_live_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_early_check_in": allow_early_check_in,
                "max_time_to_live_in_minutes": max_time_to_live_in_minutes,
            }

        @builtins.property
        def allow_early_check_in(
            self,
        ) -> typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]:
            '''Indicates whether early check-ins are allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html#cfn-licensemanager-license-borrowconfiguration-allowearlycheckin
            '''
            result = self._values.get("allow_early_check_in")
            assert result is not None, "Required property 'allow_early_check_in' is missing"
            return typing.cast(typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"], result)

        @builtins.property
        def max_time_to_live_in_minutes(self) -> jsii.Number:
            '''Maximum time for the borrow configuration, in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html#cfn-licensemanager-license-borrowconfiguration-maxtimetoliveinminutes
            '''
            result = self._values.get("max_time_to_live_in_minutes")
            assert result is not None, "Required property 'max_time_to_live_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BorrowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.ConsumptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "borrow_configuration": "borrowConfiguration",
            "provisional_configuration": "provisionalConfiguration",
            "renew_type": "renewType",
        },
    )
    class ConsumptionConfigurationProperty:
        def __init__(
            self,
            *,
            borrow_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.BorrowConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            provisional_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.ProvisionalConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            renew_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details about a consumption configuration.

            :param borrow_configuration: Details about a borrow configuration.
            :param provisional_configuration: Details about a provisional configuration.
            :param renew_type: Renewal frequency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                consumption_configuration_property = licensemanager.CfnLicense.ConsumptionConfigurationProperty(
                    borrow_configuration=licensemanager.CfnLicense.BorrowConfigurationProperty(
                        allow_early_check_in=False,
                        max_time_to_live_in_minutes=123
                    ),
                    provisional_configuration=licensemanager.CfnLicense.ProvisionalConfigurationProperty(
                        max_time_to_live_in_minutes=123
                    ),
                    renew_type="renewType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__4d0339c6f5ae5d479d45a7126a63515791f5389a9bec49ee661b2ba68e30f11f)
                check_type(argname="argument borrow_configuration", value=borrow_configuration, expected_type=type_hints["borrow_configuration"])
                check_type(argname="argument provisional_configuration", value=provisional_configuration, expected_type=type_hints["provisional_configuration"])
                check_type(argname="argument renew_type", value=renew_type, expected_type=type_hints["renew_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if borrow_configuration is not None:
                self._values["borrow_configuration"] = borrow_configuration
            if provisional_configuration is not None:
                self._values["provisional_configuration"] = provisional_configuration
            if renew_type is not None:
                self._values["renew_type"] = renew_type

        @builtins.property
        def borrow_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.BorrowConfigurationProperty"]]:
            '''Details about a borrow configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-borrowconfiguration
            '''
            result = self._values.get("borrow_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.BorrowConfigurationProperty"]], result)

        @builtins.property
        def provisional_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ProvisionalConfigurationProperty"]]:
            '''Details about a provisional configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-provisionalconfiguration
            '''
            result = self._values.get("provisional_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ProvisionalConfigurationProperty"]], result)

        @builtins.property
        def renew_type(self) -> typing.Optional[builtins.str]:
            '''Renewal frequency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-renewtype
            '''
            result = self._values.get("renew_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConsumptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.EntitlementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "unit": "unit",
            "allow_check_in": "allowCheckIn",
            "max_count": "maxCount",
            "overage": "overage",
            "value": "value",
        },
    )
    class EntitlementProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            unit: builtins.str,
            allow_check_in: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            max_count: typing.Optional[jsii.Number] = None,
            overage: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a resource entitled for use with a license.

            :param name: Entitlement name.
            :param unit: Entitlement unit.
            :param allow_check_in: Indicates whether check-ins are allowed.
            :param max_count: Maximum entitlement count. Use if the unit is not None.
            :param overage: Indicates whether overages are allowed.
            :param value: Entitlement resource. Use only if the unit is None.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                entitlement_property = licensemanager.CfnLicense.EntitlementProperty(
                    name="name",
                    unit="unit",
                
                    # the properties below are optional
                    allow_check_in=False,
                    max_count=123,
                    overage=False,
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0310e9bff8887cfad57aaed42cce71c67a7406c6a2a5cad997c2f8c17282a0fc)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument allow_check_in", value=allow_check_in, expected_type=type_hints["allow_check_in"])
                check_type(argname="argument max_count", value=max_count, expected_type=type_hints["max_count"])
                check_type(argname="argument overage", value=overage, expected_type=type_hints["overage"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "unit": unit,
            }
            if allow_check_in is not None:
                self._values["allow_check_in"] = allow_check_in
            if max_count is not None:
                self._values["max_count"] = max_count
            if overage is not None:
                self._values["overage"] = overage
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> builtins.str:
            '''Entitlement name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> builtins.str:
            '''Entitlement unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allow_check_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Indicates whether check-ins are allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-allowcheckin
            '''
            result = self._values.get("allow_check_in")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def max_count(self) -> typing.Optional[jsii.Number]:
            '''Maximum entitlement count.

            Use if the unit is not None.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-maxcount
            '''
            result = self._values.get("max_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def overage(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Indicates whether overages are allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-overage
            '''
            result = self._values.get("overage")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''Entitlement resource.

            Use only if the unit is None.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntitlementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.IssuerDataProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sign_key": "signKey"},
    )
    class IssuerDataProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sign_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details associated with the issuer of a license.

            :param name: Issuer name.
            :param sign_key: Asymmetric KMS key from AWS Key Management Service . The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                issuer_data_property = licensemanager.CfnLicense.IssuerDataProperty(
                    name="name",
                
                    # the properties below are optional
                    sign_key="signKey"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__14e6502acbee6acb56ae6f5303cd05a5e9e848984928eb8f7cdc300d203b0415)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sign_key", value=sign_key, expected_type=type_hints["sign_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if sign_key is not None:
                self._values["sign_key"] = sign_key

        @builtins.property
        def name(self) -> builtins.str:
            '''Issuer name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html#cfn-licensemanager-license-issuerdata-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sign_key(self) -> typing.Optional[builtins.str]:
            '''Asymmetric KMS key from AWS Key Management Service .

            The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html#cfn-licensemanager-license-issuerdata-signkey
            '''
            result = self._values.get("sign_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IssuerDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.MetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class MetadataProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Describes key/value pairs.

            :param name: The key name.
            :param value: The value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                metadata_property = licensemanager.CfnLicense.MetadataProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__43bd7660cdb11f18c2d3760a0a57df1cc7ec3d2ee1e8d2b9e99b3e66311ed38d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The key name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html#cfn-licensemanager-license-metadata-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html#cfn-licensemanager-license-metadata-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.ProvisionalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"max_time_to_live_in_minutes": "maxTimeToLiveInMinutes"},
    )
    class ProvisionalConfigurationProperty:
        def __init__(self, *, max_time_to_live_in_minutes: jsii.Number) -> None:
            '''Details about a provisional configuration.

            :param max_time_to_live_in_minutes: Maximum time for the provisional configuration, in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                provisional_configuration_property = licensemanager.CfnLicense.ProvisionalConfigurationProperty(
                    max_time_to_live_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__826b706a8e797ace8542469b88edc36e5448545c11f738cff1a9e72cb776c46e)
                check_type(argname="argument max_time_to_live_in_minutes", value=max_time_to_live_in_minutes, expected_type=type_hints["max_time_to_live_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_time_to_live_in_minutes": max_time_to_live_in_minutes,
            }

        @builtins.property
        def max_time_to_live_in_minutes(self) -> jsii.Number:
            '''Maximum time for the provisional configuration, in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html#cfn-licensemanager-license-provisionalconfiguration-maxtimetoliveinminutes
            '''
            result = self._values.get("max_time_to_live_in_minutes")
            assert result is not None, "Required property 'max_time_to_live_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.ValidityDateFormatProperty",
        jsii_struct_bases=[],
        name_mapping={"begin": "begin", "end": "end"},
    )
    class ValidityDateFormatProperty:
        def __init__(self, *, begin: builtins.str, end: builtins.str) -> None:
            '''Date and time range during which the license is valid, in ISO8601-UTC format.

            :param begin: Start of the time range.
            :param end: End of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                validity_date_format_property = licensemanager.CfnLicense.ValidityDateFormatProperty(
                    begin="begin",
                    end="end"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__483b5b4e301dfddf60a6c6da8bdc4898ec615b5045a70ceeeefc10fe7320e97e)
                check_type(argname="argument begin", value=begin, expected_type=type_hints["begin"])
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "begin": begin,
                "end": end,
            }

        @builtins.property
        def begin(self) -> builtins.str:
            '''Start of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html#cfn-licensemanager-license-validitydateformat-begin
            '''
            result = self._values.get("begin")
            assert result is not None, "Required property 'begin' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end(self) -> builtins.str:
            '''End of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html#cfn-licensemanager-license-validitydateformat-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidityDateFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_licensemanager_19fc2853.ILicenseAssetGroupRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnLicenseAssetGroup(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetGroup",
):
    '''Resource Type definition for AWS::LicenseManager::LicenseAssetGroup.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetgroup.html
    :cloudformationResource: AWS::LicenseManager::LicenseAssetGroup
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_licensemanager as licensemanager
        
        cfn_license_asset_group = licensemanager.CfnLicenseAssetGroup(self, "MyCfnLicenseAssetGroup",
            associated_license_asset_ruleset_arns=["associatedLicenseAssetRulesetArns"],
            license_asset_group_configurations=[licensemanager.CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty(
                usage_dimension="usageDimension"
            )],
            name="name",
        
            # the properties below are optional
            description="description",
            properties=[licensemanager.CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty(
                key="key",
                value="value"
            )],
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
        associated_license_asset_ruleset_arns: typing.Sequence[builtins.str],
        license_asset_group_configurations: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::LicenseManager::LicenseAssetGroup``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param associated_license_asset_ruleset_arns: ARNs of associated license asset rulesets.
        :param license_asset_group_configurations: License asset group configurations.
        :param name: License asset group name.
        :param description: License asset group description.
        :param properties: License asset group properties.
        :param tags: Tags to add to the license asset group.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2a7eb0e9c1a98c85e724ce832ff7b1ce8fd9f32ef8bf61202ebead342dde7569)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLicenseAssetGroupProps(
            associated_license_asset_ruleset_arns=associated_license_asset_ruleset_arns,
            license_asset_group_configurations=license_asset_group_configurations,
            name=name,
            description=description,
            properties=properties,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLicenseAssetGroup")
    @builtins.classmethod
    def arn_for_license_asset_group(
        cls,
        resource: "_aws_licensemanager_19fc2853.ILicenseAssetGroupRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c92447dc3b3c49f66871c1a5b5a94d680a51029f6ffeebee0ea6a9a49db5fe4d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForLicenseAssetGroup", [resource]))

    @jsii.member(jsii_name="isCfnLicenseAssetGroup")
    @builtins.classmethod
    def is_cfn_license_asset_group(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnLicenseAssetGroup.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__809d001e63215d9cbe3719b81bc0d851a7725b3c1e33600389221a747a4b4694)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnLicenseAssetGroup", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__294c05113bd809f9d7ad3d3d678cb92d5f7c387d8594b98d3d9f338704db204a)
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
            type_hints = cached_type_hints(_typecheckingstub__8e7983e6f5ad3b6189d4d6daec8f693b50dedac772c69ecb63a13196ff714f0b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLicenseAssetGroupArn")
    def attr_license_asset_group_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the license asset group.

        :cloudformationAttribute: LicenseAssetGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLicenseAssetGroupArn"))

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
    @jsii.member(jsii_name="licenseAssetGroupRef")
    def license_asset_group_ref(
        self,
    ) -> "_aws_licensemanager_19fc2853.LicenseAssetGroupReference":
        '''A reference to a LicenseAssetGroup resource.'''
        return typing.cast("_aws_licensemanager_19fc2853.LicenseAssetGroupReference", jsii.get(self, "licenseAssetGroupRef"))

    @builtins.property
    @jsii.member(jsii_name="associatedLicenseAssetRulesetArns")
    def associated_license_asset_ruleset_arns(self) -> typing.List[builtins.str]:
        '''ARNs of associated license asset rulesets.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "associatedLicenseAssetRulesetArns"))

    @associated_license_asset_ruleset_arns.setter
    def associated_license_asset_ruleset_arns(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f3bd6323563dab699ac4f56a2b8be33bf577eb047b1ad7b648129300e7eaba57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedLicenseAssetRulesetArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licenseAssetGroupConfigurations")
    def license_asset_group_configurations(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty"]]]:
        '''License asset group configurations.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty"]]], jsii.get(self, "licenseAssetGroupConfigurations"))

    @license_asset_group_configurations.setter
    def license_asset_group_configurations(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__340cb8b61867cff10d0f87786f4a341cff5fe7c9dc53e64930e02fe65785c798)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseAssetGroupConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''License asset group name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2b218cd3c7ad28e135e6494f201ffc4b62b1332a59401b8ad833c813c7ff9109)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''License asset group description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bcef867bdea5e6ef1b5800b42043e013de4ddb6765f453856d7febe33e461b87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty"]]]]:
        '''License asset group properties.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty"]]]], jsii.get(self, "properties"))

    @properties.setter
    def properties(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9524f9ed559fd633bd91a0b86c39e5f5a6d07331db60925db048195db1add97d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to add to the license asset group.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c87603fb324b8b9768432501e47e47aa25028284d613ae1f69d1f58ba57da505)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"usage_dimension": "usageDimension"},
    )
    class LicenseAssetGroupConfigurationProperty:
        def __init__(
            self,
            *,
            usage_dimension: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param usage_dimension: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetgroup-licenseassetgroupconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                license_asset_group_configuration_property = licensemanager.CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty(
                    usage_dimension="usageDimension"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__26e992d2e8922ca401097743ec0c3a2a582ade57aeb4570a2bc14e099629d256)
                check_type(argname="argument usage_dimension", value=usage_dimension, expected_type=type_hints["usage_dimension"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if usage_dimension is not None:
                self._values["usage_dimension"] = usage_dimension

        @builtins.property
        def usage_dimension(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetgroup-licenseassetgroupconfiguration.html#cfn-licensemanager-licenseassetgroup-licenseassetgroupconfiguration-usagedimension
            '''
            result = self._values.get("usage_dimension")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicenseAssetGroupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class LicenseAssetGroupPropertyProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetgroup-licenseassetgroupproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                license_asset_group_property_property = licensemanager.CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__b48c7fd38dd1f0cb7c228d8f0149ebdd7e4624db6dcf3b5f04ac311ca16a47d4)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetgroup-licenseassetgroupproperty.html#cfn-licensemanager-licenseassetgroup-licenseassetgroupproperty-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetgroup-licenseassetgroupproperty.html#cfn-licensemanager-licenseassetgroup-licenseassetgroupproperty-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicenseAssetGroupPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "associated_license_asset_ruleset_arns": "associatedLicenseAssetRulesetArns",
        "license_asset_group_configurations": "licenseAssetGroupConfigurations",
        "name": "name",
        "description": "description",
        "properties": "properties",
        "tags": "tags",
    },
)
class CfnLicenseAssetGroupProps:
    def __init__(
        self,
        *,
        associated_license_asset_ruleset_arns: typing.Sequence[builtins.str],
        license_asset_group_configurations: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLicenseAssetGroup``.

        :param associated_license_asset_ruleset_arns: ARNs of associated license asset rulesets.
        :param license_asset_group_configurations: License asset group configurations.
        :param name: License asset group name.
        :param description: License asset group description.
        :param properties: License asset group properties.
        :param tags: Tags to add to the license asset group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_licensemanager as licensemanager
            
            cfn_license_asset_group_props = licensemanager.CfnLicenseAssetGroupProps(
                associated_license_asset_ruleset_arns=["associatedLicenseAssetRulesetArns"],
                license_asset_group_configurations=[licensemanager.CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty(
                    usage_dimension="usageDimension"
                )],
                name="name",
            
                # the properties below are optional
                description="description",
                properties=[licensemanager.CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty(
                    key="key",
                    value="value"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a677826a5d01bc22ddf14d35068e5a795395e0d453105e9311ef16a8e59c34f9)
            check_type(argname="argument associated_license_asset_ruleset_arns", value=associated_license_asset_ruleset_arns, expected_type=type_hints["associated_license_asset_ruleset_arns"])
            check_type(argname="argument license_asset_group_configurations", value=license_asset_group_configurations, expected_type=type_hints["license_asset_group_configurations"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "associated_license_asset_ruleset_arns": associated_license_asset_ruleset_arns,
            "license_asset_group_configurations": license_asset_group_configurations,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if properties is not None:
            self._values["properties"] = properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def associated_license_asset_ruleset_arns(self) -> typing.List[builtins.str]:
        '''ARNs of associated license asset rulesets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetgroup.html#cfn-licensemanager-licenseassetgroup-associatedlicenseassetrulesetarns
        '''
        result = self._values.get("associated_license_asset_ruleset_arns")
        assert result is not None, "Required property 'associated_license_asset_ruleset_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def license_asset_group_configurations(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty"]]]:
        '''License asset group configurations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetgroup.html#cfn-licensemanager-licenseassetgroup-licenseassetgroupconfigurations
        '''
        result = self._values.get("license_asset_group_configurations")
        assert result is not None, "Required property 'license_asset_group_configurations' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty"]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''License asset group name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetgroup.html#cfn-licensemanager-licenseassetgroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''License asset group description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetgroup.html#cfn-licensemanager-licenseassetgroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty"]]]]:
        '''License asset group properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetgroup.html#cfn-licensemanager-licenseassetgroup-properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty"]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to add to the license asset group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetgroup.html#cfn-licensemanager-licenseassetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLicenseAssetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_licensemanager_19fc2853.ILicenseAssetRuleSetRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnLicenseAssetRuleSet(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet",
):
    '''Resource schema for AWS::LicenseManager::LicenseAssetRuleSet.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetruleset.html
    :cloudformationResource: AWS::LicenseManager::LicenseAssetRuleSet
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_licensemanager as licensemanager
        
        cfn_license_asset_rule_set = licensemanager.CfnLicenseAssetRuleSet(self, "MyCfnLicenseAssetRuleSet",
            name="name",
            rules=[licensemanager.CfnLicenseAssetRuleSet.LicenseAssetRuleProperty(
                rule_statement=licensemanager.CfnLicenseAssetRuleSet.RuleStatementProperty(
                    instance_rule_statement=licensemanager.CfnLicenseAssetRuleSet.InstanceRuleStatementProperty(
                        and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        ),
                        matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        ),
                        or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        )
                    ),
                    license_configuration_rule_statement=licensemanager.CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty(
                        and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        ),
                        matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        ),
                        or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        )
                    ),
                    license_rule_statement=licensemanager.CfnLicenseAssetRuleSet.LicenseRuleStatementProperty(
                        and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        ),
                        matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        ),
                        or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        )
                    )
                )
            )],
        
            # the properties below are optional
            description="description",
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
        name: builtins.str,
        rules: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.LicenseAssetRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::LicenseManager::LicenseAssetRuleSet``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: License asset ruleset name.
        :param rules: License asset rules.
        :param description: License asset ruleset description.
        :param tags: Tags to add to the license asset ruleset.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1ba952316268af1b26957b51d696b1aa8286e141cf7553db6307ec657096189f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLicenseAssetRuleSetProps(
            name=name, rules=rules, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnLicenseAssetRuleSet")
    @builtins.classmethod
    def is_cfn_license_asset_rule_set(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnLicenseAssetRuleSet.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ac108e2d28cc654bdf6815e52119293486a87fbf16ef9db3c23627d9d831950b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnLicenseAssetRuleSet", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6399b21f17aa776fc304c94465c25edf876170b90e49f08f31f8fca7bd9d3b78)
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
            type_hints = cached_type_hints(_typecheckingstub__51170ec63a26912fbad280745bb3f562c60b672319da63b9e45c0c5df343fe97)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLicenseAssetRulesetArn")
    def attr_license_asset_ruleset_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the license asset ruleset.

        :cloudformationAttribute: LicenseAssetRulesetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLicenseAssetRulesetArn"))

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
    @jsii.member(jsii_name="licenseAssetRuleSetRef")
    def license_asset_rule_set_ref(
        self,
    ) -> "_aws_licensemanager_19fc2853.LicenseAssetRuleSetReference":
        '''A reference to a LicenseAssetRuleSet resource.'''
        return typing.cast("_aws_licensemanager_19fc2853.LicenseAssetRuleSetReference", jsii.get(self, "licenseAssetRuleSetRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''License asset ruleset name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__525fd9dbe8cb0b4e5b67ba0b86a261c2521eac2baf72015a61b48e6486e0c83d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseAssetRuleProperty"]]]:
        '''License asset rules.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseAssetRuleProperty"]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseAssetRuleProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c97dfd6a5a6871608f5bc0744d456839b806943055976e35981d7fbcd2c2a454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''License asset ruleset description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e9abf4c54fba904f0a35e19401bd078be267956935a54d9ff60582ab955135ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to add to the license asset ruleset.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bc128a7be3b437201333f3b6713bc566c0df84f0e23a9da3991ccaf7faea26c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"matching_rule_statements": "matchingRuleStatements"},
    )
    class AndRuleStatementProperty:
        def __init__(
            self,
            *,
            matching_rule_statements: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.MatchingRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''AND rule statement.

            :param matching_rule_statements: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-andrulestatement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                and_rule_statement_property = licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                    matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                        constraint="constraint",
                        key_to_match="keyToMatch",
                        value_to_match=["valueToMatch"]
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f96a98025e44f891863a710cec51b576e4360ddda6b145b5d1d5cffcdcca98b1)
                check_type(argname="argument matching_rule_statements", value=matching_rule_statements, expected_type=type_hints["matching_rule_statements"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if matching_rule_statements is not None:
                self._values["matching_rule_statements"] = matching_rule_statements

        @builtins.property
        def matching_rule_statements(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-andrulestatement.html#cfn-licensemanager-licenseassetruleset-andrulestatement-matchingrulestatements
            '''
            result = self._values.get("matching_rule_statements")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AndRuleStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet.InstanceRuleStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_rule_statement": "andRuleStatement",
            "matching_rule_statement": "matchingRuleStatement",
            "or_rule_statement": "orRuleStatement",
        },
    )
    class InstanceRuleStatementProperty:
        def __init__(
            self,
            *,
            and_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.AndRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            matching_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.MatchingRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            or_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.OrRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Instance rule statement.

            :param and_rule_statement: AND rule statement.
            :param matching_rule_statement: Matching rule statement.
            :param or_rule_statement: OR rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-instancerulestatement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                instance_rule_statement_property = licensemanager.CfnLicenseAssetRuleSet.InstanceRuleStatementProperty(
                    and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                        matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        )]
                    ),
                    matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                        constraint="constraint",
                        key_to_match="keyToMatch",
                        value_to_match=["valueToMatch"]
                    ),
                    or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                        matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6bcc9a22c99817e2a9e86bd95e15419f2233ada65496bfc9db7d4a26d0c157b4)
                check_type(argname="argument and_rule_statement", value=and_rule_statement, expected_type=type_hints["and_rule_statement"])
                check_type(argname="argument matching_rule_statement", value=matching_rule_statement, expected_type=type_hints["matching_rule_statement"])
                check_type(argname="argument or_rule_statement", value=or_rule_statement, expected_type=type_hints["or_rule_statement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_rule_statement is not None:
                self._values["and_rule_statement"] = and_rule_statement
            if matching_rule_statement is not None:
                self._values["matching_rule_statement"] = matching_rule_statement
            if or_rule_statement is not None:
                self._values["or_rule_statement"] = or_rule_statement

        @builtins.property
        def and_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.AndRuleStatementProperty"]]:
            '''AND rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-instancerulestatement.html#cfn-licensemanager-licenseassetruleset-instancerulestatement-andrulestatement
            '''
            result = self._values.get("and_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.AndRuleStatementProperty"]], result)

        @builtins.property
        def matching_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]]:
            '''Matching rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-instancerulestatement.html#cfn-licensemanager-licenseassetruleset-instancerulestatement-matchingrulestatement
            '''
            result = self._values.get("matching_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]], result)

        @builtins.property
        def or_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.OrRuleStatementProperty"]]:
            '''OR rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-instancerulestatement.html#cfn-licensemanager-licenseassetruleset-instancerulestatement-orrulestatement
            '''
            result = self._values.get("or_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.OrRuleStatementProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceRuleStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet.LicenseAssetRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"rule_statement": "ruleStatement"},
    )
    class LicenseAssetRuleProperty:
        def __init__(
            self,
            *,
            rule_statement: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.RuleStatementProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''License asset rule.

            :param rule_statement: Rule statement. Specify exactly one of InstanceRuleStatement, LicenseRuleStatement, or LicenseConfigurationRuleStatement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenseassetrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                license_asset_rule_property = licensemanager.CfnLicenseAssetRuleSet.LicenseAssetRuleProperty(
                    rule_statement=licensemanager.CfnLicenseAssetRuleSet.RuleStatementProperty(
                        instance_rule_statement=licensemanager.CfnLicenseAssetRuleSet.InstanceRuleStatementProperty(
                            and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            ),
                            matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            ),
                            or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            )
                        ),
                        license_configuration_rule_statement=licensemanager.CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty(
                            and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            ),
                            matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            ),
                            or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            )
                        ),
                        license_rule_statement=licensemanager.CfnLicenseAssetRuleSet.LicenseRuleStatementProperty(
                            and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            ),
                            matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            ),
                            or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__30834bcde461fec39215a36939067432618a26c99b5fa09d6350a0636664f47b)
                check_type(argname="argument rule_statement", value=rule_statement, expected_type=type_hints["rule_statement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_statement": rule_statement,
            }

        @builtins.property
        def rule_statement(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.RuleStatementProperty"]:
            '''Rule statement.

            Specify exactly one of InstanceRuleStatement, LicenseRuleStatement, or LicenseConfigurationRuleStatement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenseassetrule.html#cfn-licensemanager-licenseassetruleset-licenseassetrule-rulestatement
            '''
            result = self._values.get("rule_statement")
            assert result is not None, "Required property 'rule_statement' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.RuleStatementProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicenseAssetRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_rule_statement": "andRuleStatement",
            "matching_rule_statement": "matchingRuleStatement",
            "or_rule_statement": "orRuleStatement",
        },
    )
    class LicenseConfigurationRuleStatementProperty:
        def __init__(
            self,
            *,
            and_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.AndRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            matching_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.MatchingRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            or_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.OrRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''License configuration rule statement.

            :param and_rule_statement: AND rule statement.
            :param matching_rule_statement: Matching rule statement.
            :param or_rule_statement: OR rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenseconfigurationrulestatement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                license_configuration_rule_statement_property = licensemanager.CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty(
                    and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                        matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        )]
                    ),
                    matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                        constraint="constraint",
                        key_to_match="keyToMatch",
                        value_to_match=["valueToMatch"]
                    ),
                    or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                        matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__5dde005b953b1c1cb411f34985858f76a2810b64878dd1d36534214161008fe7)
                check_type(argname="argument and_rule_statement", value=and_rule_statement, expected_type=type_hints["and_rule_statement"])
                check_type(argname="argument matching_rule_statement", value=matching_rule_statement, expected_type=type_hints["matching_rule_statement"])
                check_type(argname="argument or_rule_statement", value=or_rule_statement, expected_type=type_hints["or_rule_statement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_rule_statement is not None:
                self._values["and_rule_statement"] = and_rule_statement
            if matching_rule_statement is not None:
                self._values["matching_rule_statement"] = matching_rule_statement
            if or_rule_statement is not None:
                self._values["or_rule_statement"] = or_rule_statement

        @builtins.property
        def and_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.AndRuleStatementProperty"]]:
            '''AND rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenseconfigurationrulestatement.html#cfn-licensemanager-licenseassetruleset-licenseconfigurationrulestatement-andrulestatement
            '''
            result = self._values.get("and_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.AndRuleStatementProperty"]], result)

        @builtins.property
        def matching_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]]:
            '''Matching rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenseconfigurationrulestatement.html#cfn-licensemanager-licenseassetruleset-licenseconfigurationrulestatement-matchingrulestatement
            '''
            result = self._values.get("matching_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]], result)

        @builtins.property
        def or_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.OrRuleStatementProperty"]]:
            '''OR rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenseconfigurationrulestatement.html#cfn-licensemanager-licenseassetruleset-licenseconfigurationrulestatement-orrulestatement
            '''
            result = self._values.get("or_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.OrRuleStatementProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicenseConfigurationRuleStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet.LicenseRuleStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_rule_statement": "andRuleStatement",
            "matching_rule_statement": "matchingRuleStatement",
            "or_rule_statement": "orRuleStatement",
        },
    )
    class LicenseRuleStatementProperty:
        def __init__(
            self,
            *,
            and_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.AndRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            matching_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.MatchingRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            or_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.OrRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''License rule statement.

            :param and_rule_statement: AND rule statement.
            :param matching_rule_statement: Matching rule statement.
            :param or_rule_statement: OR rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenserulestatement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                license_rule_statement_property = licensemanager.CfnLicenseAssetRuleSet.LicenseRuleStatementProperty(
                    and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                        matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        )]
                    ),
                    matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                        constraint="constraint",
                        key_to_match="keyToMatch",
                        value_to_match=["valueToMatch"]
                    ),
                    or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                        matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1e8ef7dc20d4de655c8fb6e0d29e2aebd58bc58e2d8059e08b1a901cd4af5a42)
                check_type(argname="argument and_rule_statement", value=and_rule_statement, expected_type=type_hints["and_rule_statement"])
                check_type(argname="argument matching_rule_statement", value=matching_rule_statement, expected_type=type_hints["matching_rule_statement"])
                check_type(argname="argument or_rule_statement", value=or_rule_statement, expected_type=type_hints["or_rule_statement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_rule_statement is not None:
                self._values["and_rule_statement"] = and_rule_statement
            if matching_rule_statement is not None:
                self._values["matching_rule_statement"] = matching_rule_statement
            if or_rule_statement is not None:
                self._values["or_rule_statement"] = or_rule_statement

        @builtins.property
        def and_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.AndRuleStatementProperty"]]:
            '''AND rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenserulestatement.html#cfn-licensemanager-licenseassetruleset-licenserulestatement-andrulestatement
            '''
            result = self._values.get("and_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.AndRuleStatementProperty"]], result)

        @builtins.property
        def matching_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]]:
            '''Matching rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenserulestatement.html#cfn-licensemanager-licenseassetruleset-licenserulestatement-matchingrulestatement
            '''
            result = self._values.get("matching_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]], result)

        @builtins.property
        def or_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.OrRuleStatementProperty"]]:
            '''OR rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-licenserulestatement.html#cfn-licensemanager-licenseassetruleset-licenserulestatement-orrulestatement
            '''
            result = self._values.get("or_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.OrRuleStatementProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicenseRuleStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "constraint": "constraint",
            "key_to_match": "keyToMatch",
            "value_to_match": "valueToMatch",
        },
    )
    class MatchingRuleStatementProperty:
        def __init__(
            self,
            *,
            constraint: builtins.str,
            key_to_match: builtins.str,
            value_to_match: typing.Sequence[builtins.str],
        ) -> None:
            '''Matching rule statement.

            :param constraint: Constraint (e.g. Equals, Not_Equals).
            :param key_to_match: Key to match.
            :param value_to_match: Values to match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                matching_rule_statement_property = licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                    constraint="constraint",
                    key_to_match="keyToMatch",
                    value_to_match=["valueToMatch"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__6f56f947b615ee02a8b5cca0182a5fcd8cefb2725a1fe87cf9df9c73b6d348a0)
                check_type(argname="argument constraint", value=constraint, expected_type=type_hints["constraint"])
                check_type(argname="argument key_to_match", value=key_to_match, expected_type=type_hints["key_to_match"])
                check_type(argname="argument value_to_match", value=value_to_match, expected_type=type_hints["value_to_match"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "constraint": constraint,
                "key_to_match": key_to_match,
                "value_to_match": value_to_match,
            }

        @builtins.property
        def constraint(self) -> builtins.str:
            '''Constraint (e.g. Equals, Not_Equals).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.html#cfn-licensemanager-licenseassetruleset-matchingrulestatement-constraint
            '''
            result = self._values.get("constraint")
            assert result is not None, "Required property 'constraint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_to_match(self) -> builtins.str:
            '''Key to match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.html#cfn-licensemanager-licenseassetruleset-matchingrulestatement-keytomatch
            '''
            result = self._values.get("key_to_match")
            assert result is not None, "Required property 'key_to_match' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_to_match(self) -> typing.List[builtins.str]:
            '''Values to match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-matchingrulestatement.html#cfn-licensemanager-licenseassetruleset-matchingrulestatement-valuetomatch
            '''
            result = self._values.get("value_to_match")
            assert result is not None, "Required property 'value_to_match' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MatchingRuleStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"matching_rule_statements": "matchingRuleStatements"},
    )
    class OrRuleStatementProperty:
        def __init__(
            self,
            *,
            matching_rule_statements: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.MatchingRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''OR rule statement.

            :param matching_rule_statements: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-orrulestatement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                or_rule_statement_property = licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                    matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                        constraint="constraint",
                        key_to_match="keyToMatch",
                        value_to_match=["valueToMatch"]
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__803a611726146d376227fde8148339ba44283ba51ecc9ea0873dfc44542684aa)
                check_type(argname="argument matching_rule_statements", value=matching_rule_statements, expected_type=type_hints["matching_rule_statements"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if matching_rule_statements is not None:
                self._values["matching_rule_statements"] = matching_rule_statements

        @builtins.property
        def matching_rule_statements(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-orrulestatement.html#cfn-licensemanager-licenseassetruleset-orrulestatement-matchingrulestatements
            '''
            result = self._values.get("matching_rule_statements")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.MatchingRuleStatementProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrRuleStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSet.RuleStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_rule_statement": "instanceRuleStatement",
            "license_configuration_rule_statement": "licenseConfigurationRuleStatement",
            "license_rule_statement": "licenseRuleStatement",
        },
    )
    class RuleStatementProperty:
        def __init__(
            self,
            *,
            instance_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.InstanceRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            license_configuration_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            license_rule_statement: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.LicenseRuleStatementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Rule statement.

            Specify exactly one of InstanceRuleStatement, LicenseRuleStatement, or LicenseConfigurationRuleStatement.

            :param instance_rule_statement: Instance rule statement.
            :param license_configuration_rule_statement: License configuration rule statement.
            :param license_rule_statement: License rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-rulestatement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                rule_statement_property = licensemanager.CfnLicenseAssetRuleSet.RuleStatementProperty(
                    instance_rule_statement=licensemanager.CfnLicenseAssetRuleSet.InstanceRuleStatementProperty(
                        and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        ),
                        matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        ),
                        or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        )
                    ),
                    license_configuration_rule_statement=licensemanager.CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty(
                        and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        ),
                        matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        ),
                        or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        )
                    ),
                    license_rule_statement=licensemanager.CfnLicenseAssetRuleSet.LicenseRuleStatementProperty(
                        and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        ),
                        matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                            constraint="constraint",
                            key_to_match="keyToMatch",
                            value_to_match=["valueToMatch"]
                        ),
                        or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                            matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__077fd612350f2737baba6535b61919be84e60223a74345b4f15b888d80095bff)
                check_type(argname="argument instance_rule_statement", value=instance_rule_statement, expected_type=type_hints["instance_rule_statement"])
                check_type(argname="argument license_configuration_rule_statement", value=license_configuration_rule_statement, expected_type=type_hints["license_configuration_rule_statement"])
                check_type(argname="argument license_rule_statement", value=license_rule_statement, expected_type=type_hints["license_rule_statement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if instance_rule_statement is not None:
                self._values["instance_rule_statement"] = instance_rule_statement
            if license_configuration_rule_statement is not None:
                self._values["license_configuration_rule_statement"] = license_configuration_rule_statement
            if license_rule_statement is not None:
                self._values["license_rule_statement"] = license_rule_statement

        @builtins.property
        def instance_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.InstanceRuleStatementProperty"]]:
            '''Instance rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-rulestatement.html#cfn-licensemanager-licenseassetruleset-rulestatement-instancerulestatement
            '''
            result = self._values.get("instance_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.InstanceRuleStatementProperty"]], result)

        @builtins.property
        def license_configuration_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty"]]:
            '''License configuration rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-rulestatement.html#cfn-licensemanager-licenseassetruleset-rulestatement-licenseconfigurationrulestatement
            '''
            result = self._values.get("license_configuration_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty"]], result)

        @builtins.property
        def license_rule_statement(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseRuleStatementProperty"]]:
            '''License rule statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-licenseassetruleset-rulestatement.html#cfn-licensemanager-licenseassetruleset-rulestatement-licenserulestatement
            '''
            result = self._values.get("license_rule_statement")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseRuleStatementProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseAssetRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "rules": "rules",
        "description": "description",
        "tags": "tags",
    },
)
class CfnLicenseAssetRuleSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        rules: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicenseAssetRuleSet.LicenseAssetRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLicenseAssetRuleSet``.

        :param name: License asset ruleset name.
        :param rules: License asset rules.
        :param description: License asset ruleset description.
        :param tags: Tags to add to the license asset ruleset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetruleset.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_licensemanager as licensemanager
            
            cfn_license_asset_rule_set_props = licensemanager.CfnLicenseAssetRuleSetProps(
                name="name",
                rules=[licensemanager.CfnLicenseAssetRuleSet.LicenseAssetRuleProperty(
                    rule_statement=licensemanager.CfnLicenseAssetRuleSet.RuleStatementProperty(
                        instance_rule_statement=licensemanager.CfnLicenseAssetRuleSet.InstanceRuleStatementProperty(
                            and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            ),
                            matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            ),
                            or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            )
                        ),
                        license_configuration_rule_statement=licensemanager.CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty(
                            and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            ),
                            matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            ),
                            or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            )
                        ),
                        license_rule_statement=licensemanager.CfnLicenseAssetRuleSet.LicenseRuleStatementProperty(
                            and_rule_statement=licensemanager.CfnLicenseAssetRuleSet.AndRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            ),
                            matching_rule_statement=licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                constraint="constraint",
                                key_to_match="keyToMatch",
                                value_to_match=["valueToMatch"]
                            ),
                            or_rule_statement=licensemanager.CfnLicenseAssetRuleSet.OrRuleStatementProperty(
                                matching_rule_statements=[licensemanager.CfnLicenseAssetRuleSet.MatchingRuleStatementProperty(
                                    constraint="constraint",
                                    key_to_match="keyToMatch",
                                    value_to_match=["valueToMatch"]
                                )]
                            )
                        )
                    )
                )],
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c715e4e583b24c76ec87ab806ef270df3fcb252fd77e33889db896b624e3575f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "rules": rules,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''License asset ruleset name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetruleset.html#cfn-licensemanager-licenseassetruleset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseAssetRuleProperty"]]]:
        '''License asset rules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetruleset.html#cfn-licensemanager-licenseassetruleset-rules
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicenseAssetRuleSet.LicenseAssetRuleProperty"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''License asset ruleset description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetruleset.html#cfn-licensemanager-licenseassetruleset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''Tags to add to the license asset ruleset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-licenseassetruleset.html#cfn-licensemanager-licenseassetruleset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLicenseAssetRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseProps",
    jsii_struct_bases=[],
    name_mapping={
        "beneficiary": "beneficiary",
        "consumption_configuration": "consumptionConfiguration",
        "entitlements": "entitlements",
        "home_region": "homeRegion",
        "issuer": "issuer",
        "license_name": "licenseName",
        "product_name": "productName",
        "product_sku": "productSku",
        "validity": "validity",
        "license_metadata": "licenseMetadata",
        "status": "status",
        "tags": "tags",
    },
)
class CfnLicenseProps:
    def __init__(
        self,
        *,
        beneficiary: builtins.str,
        consumption_configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.ConsumptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        entitlements: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.EntitlementProperty", typing.Dict[builtins.str, typing.Any]]]]],
        home_region: builtins.str,
        issuer: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.IssuerDataProperty", typing.Dict[builtins.str, typing.Any]]],
        license_name: builtins.str,
        product_name: builtins.str,
        product_sku: builtins.str,
        validity: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.ValidityDateFormatProperty", typing.Dict[builtins.str, typing.Any]]],
        license_metadata: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLicense.MetadataProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLicense``.

        :param beneficiary: License beneficiary.
        :param consumption_configuration: Configuration for consumption of the license.
        :param entitlements: License entitlements.
        :param home_region: Home Region of the license.
        :param issuer: License issuer.
        :param license_name: License name.
        :param product_name: Product name.
        :param product_sku: Product SKU.
        :param validity: Date and time range during which the license is valid, in ISO8601-UTC format.
        :param license_metadata: License metadata.
        :param status: License status.
        :param tags: A list of tags to attach.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_licensemanager as licensemanager
            
            cfn_license_props = licensemanager.CfnLicenseProps(
                beneficiary="beneficiary",
                consumption_configuration=licensemanager.CfnLicense.ConsumptionConfigurationProperty(
                    borrow_configuration=licensemanager.CfnLicense.BorrowConfigurationProperty(
                        allow_early_check_in=False,
                        max_time_to_live_in_minutes=123
                    ),
                    provisional_configuration=licensemanager.CfnLicense.ProvisionalConfigurationProperty(
                        max_time_to_live_in_minutes=123
                    ),
                    renew_type="renewType"
                ),
                entitlements=[licensemanager.CfnLicense.EntitlementProperty(
                    name="name",
                    unit="unit",
            
                    # the properties below are optional
                    allow_check_in=False,
                    max_count=123,
                    overage=False,
                    value="value"
                )],
                home_region="homeRegion",
                issuer=licensemanager.CfnLicense.IssuerDataProperty(
                    name="name",
            
                    # the properties below are optional
                    sign_key="signKey"
                ),
                license_name="licenseName",
                product_name="productName",
                product_sku="productSku",
                validity=licensemanager.CfnLicense.ValidityDateFormatProperty(
                    begin="begin",
                    end="end"
                ),
            
                # the properties below are optional
                license_metadata=[licensemanager.CfnLicense.MetadataProperty(
                    name="name",
                    value="value"
                )],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a1d549419287a5a545bf5eecdc65cd6b52387eb01953f3d4ff24a43da333c424)
            check_type(argname="argument beneficiary", value=beneficiary, expected_type=type_hints["beneficiary"])
            check_type(argname="argument consumption_configuration", value=consumption_configuration, expected_type=type_hints["consumption_configuration"])
            check_type(argname="argument entitlements", value=entitlements, expected_type=type_hints["entitlements"])
            check_type(argname="argument home_region", value=home_region, expected_type=type_hints["home_region"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument license_name", value=license_name, expected_type=type_hints["license_name"])
            check_type(argname="argument product_name", value=product_name, expected_type=type_hints["product_name"])
            check_type(argname="argument product_sku", value=product_sku, expected_type=type_hints["product_sku"])
            check_type(argname="argument validity", value=validity, expected_type=type_hints["validity"])
            check_type(argname="argument license_metadata", value=license_metadata, expected_type=type_hints["license_metadata"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "beneficiary": beneficiary,
            "consumption_configuration": consumption_configuration,
            "entitlements": entitlements,
            "home_region": home_region,
            "issuer": issuer,
            "license_name": license_name,
            "product_name": product_name,
            "product_sku": product_sku,
            "validity": validity,
        }
        if license_metadata is not None:
            self._values["license_metadata"] = license_metadata
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def beneficiary(self) -> builtins.str:
        '''License beneficiary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-beneficiary
        '''
        result = self._values.get("beneficiary")
        assert result is not None, "Required property 'beneficiary' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumption_configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ConsumptionConfigurationProperty"]:
        '''Configuration for consumption of the license.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-consumptionconfiguration
        '''
        result = self._values.get("consumption_configuration")
        assert result is not None, "Required property 'consumption_configuration' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ConsumptionConfigurationProperty"], result)

    @builtins.property
    def entitlements(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.EntitlementProperty"]]]:
        '''License entitlements.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-entitlements
        '''
        result = self._values.get("entitlements")
        assert result is not None, "Required property 'entitlements' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.EntitlementProperty"]]], result)

    @builtins.property
    def home_region(self) -> builtins.str:
        '''Home Region of the license.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-homeregion
        '''
        result = self._values.get("home_region")
        assert result is not None, "Required property 'home_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.IssuerDataProperty"]:
        '''License issuer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-issuer
        '''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.IssuerDataProperty"], result)

    @builtins.property
    def license_name(self) -> builtins.str:
        '''License name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensename
        '''
        result = self._values.get("license_name")
        assert result is not None, "Required property 'license_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_name(self) -> builtins.str:
        '''Product name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productname
        '''
        result = self._values.get("product_name")
        assert result is not None, "Required property 'product_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_sku(self) -> builtins.str:
        '''Product SKU.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productsku
        '''
        result = self._values.get("product_sku")
        assert result is not None, "Required property 'product_sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ValidityDateFormatProperty"]:
        '''Date and time range during which the license is valid, in ISO8601-UTC format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-validity
        '''
        result = self._values.get("validity")
        assert result is not None, "Required property 'validity' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.ValidityDateFormatProperty"], result)

    @builtins.property
    def license_metadata(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.MetadataProperty"]]]]:
        '''License metadata.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensemetadata
        '''
        result = self._values.get("license_metadata")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLicense.MetadataProperty"]]]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''License status.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A list of tags to attach.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLicenseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGrant",
    "CfnGrantProps",
    "CfnLicense",
    "CfnLicenseAssetGroup",
    "CfnLicenseAssetGroupProps",
    "CfnLicenseAssetRuleSet",
    "CfnLicenseAssetRuleSetProps",
    "CfnLicenseProps",
]

publication.publish()

def _typecheckingstub__e8429ee81c009103dd15c76170dfb52e5ca38f72a8912b82d6e63e3f460c3022(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
    grant_name: typing.Optional[builtins.str] = None,
    home_region: typing.Optional[builtins.str] = None,
    license_arn: typing.Optional[builtins.str] = None,
    principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d75a1343afb37f47732759e1bffa4521f7146f8652ca23eb417d8545df2c5632(
    resource: _aws_licensemanager_19fc2853.IGrantRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77395be3520b17c3fdb320cd771bc776e8d38fcf1699b4649b0b02baeb512632(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f3d843a99f00dd40b93f69a334bda31af66745c91ef0da13aef948b5e7cd3b(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f21921653469c34829dafde09a61b6573c5caa1cd6413329ac50f150c61edce(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0365c0a6e5122b9fa8e724dcae1d11a86ea3be7b9c43576ae3984046a8a866a2(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f4a134c7bb2f22cd48211ed5100e65a75fc658d9d8f836ea5c12000691c0cb2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5031789a0d9f35bd09ee7810379dcbe0da55436888a38e9623b68c7226da0990(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ad1871340fca01eaad30a6180a827f5d9f498e7a913dbc15898d39ace8e741(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c571a4cf4f9bf1814a1015ca4a37680ca14b1356d42232abd8a71042c1e07bc(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979cc3eeb34a65f4beb72557bbf7486f2c8b526da9a872d958b13f140f65edb0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25ecdb93f9976dac7ee80e59b54502ad27f8d5b03ad158b0d7b9624810f732c5(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c62319564e7f4daffb2869290c03b511d6440828cc8d89ddb4e628ea3e0f93(
    *,
    allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
    grant_name: typing.Optional[builtins.str] = None,
    home_region: typing.Optional[builtins.str] = None,
    license_arn: typing.Optional[builtins.str] = None,
    principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa5716b8b0216bdd1da1f12239ad6038aa037294da7f4a1f0215f1b16622526(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    beneficiary: builtins.str,
    consumption_configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.ConsumptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    entitlements: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.EntitlementProperty, typing.Dict[builtins.str, typing.Any]]]]],
    home_region: builtins.str,
    issuer: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.IssuerDataProperty, typing.Dict[builtins.str, typing.Any]]],
    license_name: builtins.str,
    product_name: builtins.str,
    product_sku: builtins.str,
    validity: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.ValidityDateFormatProperty, typing.Dict[builtins.str, typing.Any]]],
    license_metadata: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.MetadataProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edbf08bc914e74c1bdf307cc4a134bf853aec8fa0fa88bdae05d34aad073560d(
    resource: _aws_licensemanager_19fc2853.ILicenseRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c0864b8227060c52869733f29658cb579ea455300bf39ad4a797305bc4a646(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9cd2d3dab3901b09367da6f6bc033c9f014286742aa8f85c2c7a6834c1b1512(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5b3e1a3ed6019a3b4d49c9c0479889cc544e9ecc5ed6f1e04e62407fc3377a9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf9994475a7c52b73f7bc27dcb24ebe97709f2662d5138be4da7b3c42265936d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284aa1e5a6876d4f451b6e5e8f93fdb375fc583828e7e8d36f280d50e762d790(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLicense.ConsumptionConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e1a84fbc6ca70d5dacac620ef3f77aa87a4d9b60385a5f2899f10ab1aefd7d(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLicense.EntitlementProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543ec2abfa87082c6465bd9aa1ff4096a9a5ba669d3147343b69c96ff2f90d67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b07f82f3d197d61c5edecbc56261a03ad65f4f99d1bb7a3c7b629126bb6ce9(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLicense.IssuerDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e97ac745c4faabd1c139a343ce905672f7e647741a9827bd7f203b40fb8f01c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a880e38bf22471203328b40fbe7cfbc719574af83c33d27bfb321c125d66fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e5b8b4e9b80cb8b0305a292b6c390efd67f677abdb467395dc1e4b849b9c418(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14bfd7eea976b95153acfc2c36f571a86f5e204050b842561bf3f488085a466b(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLicense.ValidityDateFormatProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c94759710766169f67f670504ad6a0d56a36207b2a7008e6962da6595d9b62f(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLicense.MetadataProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a0bb88a6f2431e141da5aa1e0e1d94957e1ec7a904c8a0b4f79254b7ef6f01(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d5654748f0ba764790ff72d866ee568074e0ba162b9ce72977bba8050b12fd(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1d045a93aaf4354921dc5e95316f2bc7fa071c999fdf4edaa837886e37fb65(
    *,
    allow_early_check_in: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
    max_time_to_live_in_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0339c6f5ae5d479d45a7126a63515791f5389a9bec49ee661b2ba68e30f11f(
    *,
    borrow_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.BorrowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    provisional_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.ProvisionalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    renew_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0310e9bff8887cfad57aaed42cce71c67a7406c6a2a5cad997c2f8c17282a0fc(
    *,
    name: builtins.str,
    unit: builtins.str,
    allow_check_in: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    max_count: typing.Optional[jsii.Number] = None,
    overage: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e6502acbee6acb56ae6f5303cd05a5e9e848984928eb8f7cdc300d203b0415(
    *,
    name: builtins.str,
    sign_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43bd7660cdb11f18c2d3760a0a57df1cc7ec3d2ee1e8d2b9e99b3e66311ed38d(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__826b706a8e797ace8542469b88edc36e5448545c11f738cff1a9e72cb776c46e(
    *,
    max_time_to_live_in_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__483b5b4e301dfddf60a6c6da8bdc4898ec615b5045a70ceeeefc10fe7320e97e(
    *,
    begin: builtins.str,
    end: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7eb0e9c1a98c85e724ce832ff7b1ce8fd9f32ef8bf61202ebead342dde7569(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    associated_license_asset_ruleset_arns: typing.Sequence[builtins.str],
    license_asset_group_configurations: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92447dc3b3c49f66871c1a5b5a94d680a51029f6ffeebee0ea6a9a49db5fe4d(
    resource: _aws_licensemanager_19fc2853.ILicenseAssetGroupRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__809d001e63215d9cbe3719b81bc0d851a7725b3c1e33600389221a747a4b4694(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__294c05113bd809f9d7ad3d3d678cb92d5f7c387d8594b98d3d9f338704db204a(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e7983e6f5ad3b6189d4d6daec8f693b50dedac772c69ecb63a13196ff714f0b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3bd6323563dab699ac4f56a2b8be33bf577eb047b1ad7b648129300e7eaba57(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__340cb8b61867cff10d0f87786f4a341cff5fe7c9dc53e64930e02fe65785c798(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b218cd3c7ad28e135e6494f201ffc4b62b1332a59401b8ad833c813c7ff9109(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcef867bdea5e6ef1b5800b42043e013de4ddb6765f453856d7febe33e461b87(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9524f9ed559fd633bd91a0b86c39e5f5a6d07331db60925db048195db1add97d(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c87603fb324b8b9768432501e47e47aa25028284d613ae1f69d1f58ba57da505(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26e992d2e8922ca401097743ec0c3a2a582ade57aeb4570a2bc14e099629d256(
    *,
    usage_dimension: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b48c7fd38dd1f0cb7c228d8f0149ebdd7e4624db6dcf3b5f04ac311ca16a47d4(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a677826a5d01bc22ddf14d35068e5a795395e0d453105e9311ef16a8e59c34f9(
    *,
    associated_license_asset_ruleset_arns: typing.Sequence[builtins.str],
    license_asset_group_configurations: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetGroup.LicenseAssetGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetGroup.LicenseAssetGroupPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba952316268af1b26957b51d696b1aa8286e141cf7553db6307ec657096189f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    rules: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.LicenseAssetRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac108e2d28cc654bdf6815e52119293486a87fbf16ef9db3c23627d9d831950b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6399b21f17aa776fc304c94465c25edf876170b90e49f08f31f8fca7bd9d3b78(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51170ec63a26912fbad280745bb3f562c60b672319da63b9e45c0c5df343fe97(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__525fd9dbe8cb0b4e5b67ba0b86a261c2521eac2baf72015a61b48e6486e0c83d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97dfd6a5a6871608f5bc0744d456839b806943055976e35981d7fbcd2c2a454(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLicenseAssetRuleSet.LicenseAssetRuleProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9abf4c54fba904f0a35e19401bd078be267956935a54d9ff60582ab955135ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc128a7be3b437201333f3b6713bc566c0df84f0e23a9da3991ccaf7faea26c5(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96a98025e44f891863a710cec51b576e4360ddda6b145b5d1d5cffcdcca98b1(
    *,
    matching_rule_statements: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.MatchingRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bcc9a22c99817e2a9e86bd95e15419f2233ada65496bfc9db7d4a26d0c157b4(
    *,
    and_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.AndRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    matching_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.MatchingRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    or_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.OrRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30834bcde461fec39215a36939067432618a26c99b5fa09d6350a0636664f47b(
    *,
    rule_statement: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.RuleStatementProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dde005b953b1c1cb411f34985858f76a2810b64878dd1d36534214161008fe7(
    *,
    and_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.AndRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    matching_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.MatchingRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    or_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.OrRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e8ef7dc20d4de655c8fb6e0d29e2aebd58bc58e2d8059e08b1a901cd4af5a42(
    *,
    and_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.AndRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    matching_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.MatchingRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    or_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.OrRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f56f947b615ee02a8b5cca0182a5fcd8cefb2725a1fe87cf9df9c73b6d348a0(
    *,
    constraint: builtins.str,
    key_to_match: builtins.str,
    value_to_match: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__803a611726146d376227fde8148339ba44283ba51ecc9ea0873dfc44542684aa(
    *,
    matching_rule_statements: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.MatchingRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__077fd612350f2737baba6535b61919be84e60223a74345b4f15b888d80095bff(
    *,
    instance_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.InstanceRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    license_configuration_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.LicenseConfigurationRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    license_rule_statement: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.LicenseRuleStatementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c715e4e583b24c76ec87ab806ef270df3fcb252fd77e33889db896b624e3575f(
    *,
    name: builtins.str,
    rules: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicenseAssetRuleSet.LicenseAssetRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d549419287a5a545bf5eecdc65cd6b52387eb01953f3d4ff24a43da333c424(
    *,
    beneficiary: builtins.str,
    consumption_configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.ConsumptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    entitlements: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.EntitlementProperty, typing.Dict[builtins.str, typing.Any]]]]],
    home_region: builtins.str,
    issuer: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.IssuerDataProperty, typing.Dict[builtins.str, typing.Any]]],
    license_name: builtins.str,
    product_name: builtins.str,
    product_sku: builtins.str,
    validity: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.ValidityDateFormatProperty, typing.Dict[builtins.str, typing.Any]]],
    license_metadata: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLicense.MetadataProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
