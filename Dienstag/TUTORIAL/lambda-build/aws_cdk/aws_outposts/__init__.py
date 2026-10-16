r'''
# AWS::Outposts Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_outposts as outposts
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Outposts construct libraries](https://constructs.dev/search?q=outposts)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Outposts resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Outposts.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Outposts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Outposts.html).

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
    import aws_cdk.interfaces.aws_outposts as _aws_outposts_621ae39e
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_outposts_621ae39e = _LazyImport("aws_cdk.interfaces.aws_outposts")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_outposts_621ae39e.IOutpostRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnOutpost(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_outposts.CfnOutpost",
):
    '''Definition of AWS::Outposts::Outpost Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html
    :cloudformationResource: AWS::Outposts::Outpost
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_outposts as outposts
        
        cfn_outpost = outposts.CfnOutpost(self, "MyCfnOutpost",
            name="name",
            site_id="siteId",
        
            # the properties below are optional
            availability_zone="availabilityZone",
            availability_zone_id="availabilityZoneId",
            description="description",
            supported_hardware_type="supportedHardwareType",
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
        site_id: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        supported_hardware_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Outposts::Outpost``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: 
        :param site_id: 
        :param availability_zone: 
        :param availability_zone_id: 
        :param description: 
        :param supported_hardware_type: 
        :param tags: 
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8971624592e127fd49b80bfd3f7d1773b1a737fe09f1a384044eca07f3debd33)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOutpostProps(
            name=name,
            site_id=site_id,
            availability_zone=availability_zone,
            availability_zone_id=availability_zone_id,
            description=description,
            supported_hardware_type=supported_hardware_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForOutpost")
    @builtins.classmethod
    def arn_for_outpost(
        cls,
        resource: "_aws_outposts_621ae39e.IOutpostRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__61961d4e0566bf05f2597978a460d3a976e7809bc7a0eb487e3151e739032665)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForOutpost", [resource]))

    @jsii.member(jsii_name="isCfnOutpost")
    @builtins.classmethod
    def is_cfn_outpost(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnOutpost.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ec4a5c12c2db8d5527e5117fc089ee107f51ba55fca66a6efa7c61cc2f7d690b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnOutpost", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fc0bfd25164f3247f518e913212c5050d68069062057269d8ef5d0c5b45a460a)
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
            type_hints = cached_type_hints(_typecheckingstub__c268c09db91b390484e524eda84f82b70e6d5e98810828db955c728c9d010f2c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLifeCycleStatus")
    def attr_life_cycle_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: LifeCycleStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLifeCycleStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrOutpostArn")
    def attr_outpost_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: OutpostArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOutpostArn"))

    @builtins.property
    @jsii.member(jsii_name="attrOutpostId")
    def attr_outpost_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: OutpostId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOutpostId"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property
    @jsii.member(jsii_name="attrSiteArn")
    def attr_site_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SiteArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteArn"))

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
    @jsii.member(jsii_name="outpostRef")
    def outpost_ref(self) -> "_aws_outposts_621ae39e.OutpostReference":
        '''A reference to a Outpost resource.'''
        return typing.cast("_aws_outposts_621ae39e.OutpostReference", jsii.get(self, "outpostRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__96878466b18f3fde129ce715176b1a8b6971e0c697710523524e28015fc9e26f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="siteId")
    def site_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "siteId"))

    @site_id.setter
    def site_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__813dc2d433fde86852245dad96c7408426d135ff51aabfc35f5e2e58bdcf7f0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f515cd9608704083448cb4e153fcd2e7fe3b5d04ed3ac905e18982b828eb47c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneId")
    def availability_zone_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneId"))

    @availability_zone_id.setter
    def availability_zone_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__de836b50791de14bc30b6d2267611fea2146dd4fd508dcd9200c6be5695a8214)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3746ec72319677760081ffe1b0c31593a486e124b4bef46a86eaee5834259f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="supportedHardwareType")
    def supported_hardware_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "supportedHardwareType"))

    @supported_hardware_type.setter
    def supported_hardware_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2e5393eba0e1264b7792630bf2941d28ac6590e8a457d5d29010fd84bec24108)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportedHardwareType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__289cf60bd40b5709a59f9ab5a3c84626d213bc19d3400937b7dc798b024dc67e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_outposts.CfnOutpostProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "site_id": "siteId",
        "availability_zone": "availabilityZone",
        "availability_zone_id": "availabilityZoneId",
        "description": "description",
        "supported_hardware_type": "supportedHardwareType",
        "tags": "tags",
    },
)
class CfnOutpostProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        site_id: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        supported_hardware_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOutpost``.

        :param name: 
        :param site_id: 
        :param availability_zone: 
        :param availability_zone_id: 
        :param description: 
        :param supported_hardware_type: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_outposts as outposts
            
            cfn_outpost_props = outposts.CfnOutpostProps(
                name="name",
                site_id="siteId",
            
                # the properties below are optional
                availability_zone="availabilityZone",
                availability_zone_id="availabilityZoneId",
                description="description",
                supported_hardware_type="supportedHardwareType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c560f1fe019e8891a9423ca456866618c21af5d07eb2c1020c2a762fd4752b81)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument site_id", value=site_id, expected_type=type_hints["site_id"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument availability_zone_id", value=availability_zone_id, expected_type=type_hints["availability_zone_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument supported_hardware_type", value=supported_hardware_type, expected_type=type_hints["supported_hardware_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "site_id": site_id,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            self._values["availability_zone_id"] = availability_zone_id
        if description is not None:
            self._values["description"] = description
        if supported_hardware_type is not None:
            self._values["supported_hardware_type"] = supported_hardware_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html#cfn-outposts-outpost-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html#cfn-outposts-outpost-siteid
        '''
        result = self._values.get("site_id")
        assert result is not None, "Required property 'site_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html#cfn-outposts-outpost-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zone_id(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html#cfn-outposts-outpost-availabilityzoneid
        '''
        result = self._values.get("availability_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html#cfn-outposts-outpost-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def supported_hardware_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html#cfn-outposts-outpost-supportedhardwaretype
        '''
        result = self._values.get("supported_hardware_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-outpost.html#cfn-outposts-outpost-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOutpostProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_outposts_621ae39e.ISiteRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnSite(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_outposts.CfnSite",
):
    '''Definition of AWS::Outposts::Site Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html
    :cloudformationResource: AWS::Outposts::Site
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_outposts as outposts
        
        cfn_site = outposts.CfnSite(self, "MyCfnSite",
            name="name",
        
            # the properties below are optional
            description="description",
            notes="notes",
            operating_address=outposts.CfnSite.AddressProperty(
                address_line1="addressLine1",
                city="city",
                contact_name="contactName",
                contact_phone_number="contactPhoneNumber",
                country_code="countryCode",
                postal_code="postalCode",
                state_or_region="stateOrRegion",
        
                # the properties below are optional
                address_line2="addressLine2",
                address_line3="addressLine3",
                district_or_county="districtOrCounty",
                municipality="municipality"
            ),
            rack_physical_properties=outposts.CfnSite.RackPhysicalPropertiesProperty(
                fiber_optic_cable_type="fiberOpticCableType",
                maximum_supported_weight_lbs="maximumSupportedWeightLbs",
                optical_standard="opticalStandard",
                power_connector="powerConnector",
                power_draw_kva="powerDrawKva",
                power_feed_drop="powerFeedDrop",
                power_phase="powerPhase",
                uplink_count="uplinkCount",
                uplink_gbps="uplinkGbps"
            ),
            shipping_address=outposts.CfnSite.AddressProperty(
                address_line1="addressLine1",
                city="city",
                contact_name="contactName",
                contact_phone_number="contactPhoneNumber",
                country_code="countryCode",
                postal_code="postalCode",
                state_or_region="stateOrRegion",
        
                # the properties below are optional
                address_line2="addressLine2",
                address_line3="addressLine3",
                district_or_county="districtOrCounty",
                municipality="municipality"
            ),
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
        description: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        operating_address: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSite.AddressProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        rack_physical_properties: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSite.RackPhysicalPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        shipping_address: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSite.AddressProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Outposts::Site``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: 
        :param description: 
        :param notes: 
        :param operating_address: 
        :param rack_physical_properties: 
        :param shipping_address: 
        :param tags: 
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f3d714077b9a690b88c6fc96e15456f27991a8d901eb70ea9ecb9b46e55b8328)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSiteProps(
            name=name,
            description=description,
            notes=notes,
            operating_address=operating_address,
            rack_physical_properties=rack_physical_properties,
            shipping_address=shipping_address,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSite")
    @builtins.classmethod
    def arn_for_site(cls, resource: "_aws_outposts_621ae39e.ISiteRef") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6373697618d360cefd50c9675ce87f1ada8b9106d9dc21ecd34c64c347292827)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSite", [resource]))

    @jsii.member(jsii_name="isCfnSite")
    @builtins.classmethod
    def is_cfn_site(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSite.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__adf3e014728bbb5b26e4ede2b3f861cac8ac90b7e6e119c27c3a925e369fa19f)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSite", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ce999d4e727c4ebbf4e71f951f5c10eea4ba80282674926a7ee20f1692524180)
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
            type_hints = cached_type_hints(_typecheckingstub__8ad84a7b53d8f4f5ea601b30057d197f581e6c7641a95cff710b72dfc631084a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSiteArn")
    def attr_site_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SiteArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSiteId")
    def attr_site_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SiteId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteId"))

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
    @jsii.member(jsii_name="siteRef")
    def site_ref(self) -> "_aws_outposts_621ae39e.SiteReference":
        '''A reference to a Site resource.'''
        return typing.cast("_aws_outposts_621ae39e.SiteReference", jsii.get(self, "siteRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__170e09c6bdb68519d4260397cf593c572f4ef1be15fb2f4c45fff0bf9823ceaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__60320fde224f99d0ef729abd96d1dc84c0d5b0f87b861e301f13926af4e5a47c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="notes")
    def notes(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notes"))

    @notes.setter
    def notes(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b8f705d86c50955e648aea39f390b415f32cc2a50c3f8364310e00f2cae45f4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="operatingAddress")
    def operating_address(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]], jsii.get(self, "operatingAddress"))

    @operating_address.setter
    def operating_address(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9d30ad0cda0adcf03199c7453890fa9db026c31e062f8da0788d13d7258d1713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rackPhysicalProperties")
    def rack_physical_properties(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.RackPhysicalPropertiesProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.RackPhysicalPropertiesProperty"]], jsii.get(self, "rackPhysicalProperties"))

    @rack_physical_properties.setter
    def rack_physical_properties(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.RackPhysicalPropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4861c8d2f7d3f54a8335886ef48616d24ea53147bfab93f58603d3c34b3c6905)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rackPhysicalProperties", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="shippingAddress")
    def shipping_address(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]], jsii.get(self, "shippingAddress"))

    @shipping_address.setter
    def shipping_address(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b013059e4e57daab1e78b74597803d134aecab91285303ebc1622f2a299a5967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shippingAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4a9eb786cfd3ba4d3ab93d6fcda01d4852ddcfe30cfbd2ab5e3ecad2e3b63503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_outposts.CfnSite.AddressProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address_line1": "addressLine1",
            "city": "city",
            "contact_name": "contactName",
            "contact_phone_number": "contactPhoneNumber",
            "country_code": "countryCode",
            "postal_code": "postalCode",
            "state_or_region": "stateOrRegion",
            "address_line2": "addressLine2",
            "address_line3": "addressLine3",
            "district_or_county": "districtOrCounty",
            "municipality": "municipality",
        },
    )
    class AddressProperty:
        def __init__(
            self,
            *,
            address_line1: builtins.str,
            city: builtins.str,
            contact_name: builtins.str,
            contact_phone_number: builtins.str,
            country_code: builtins.str,
            postal_code: builtins.str,
            state_or_region: builtins.str,
            address_line2: typing.Optional[builtins.str] = None,
            address_line3: typing.Optional[builtins.str] = None,
            district_or_county: typing.Optional[builtins.str] = None,
            municipality: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param address_line1: 
            :param city: 
            :param contact_name: 
            :param contact_phone_number: 
            :param country_code: 
            :param postal_code: 
            :param state_or_region: 
            :param address_line2: 
            :param address_line3: 
            :param district_or_county: 
            :param municipality: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_outposts as outposts
                
                address_property = outposts.CfnSite.AddressProperty(
                    address_line1="addressLine1",
                    city="city",
                    contact_name="contactName",
                    contact_phone_number="contactPhoneNumber",
                    country_code="countryCode",
                    postal_code="postalCode",
                    state_or_region="stateOrRegion",
                
                    # the properties below are optional
                    address_line2="addressLine2",
                    address_line3="addressLine3",
                    district_or_county="districtOrCounty",
                    municipality="municipality"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__47a5383ffcc62bcf8b7d6f719f9da5d9251badec11bd8f4f73523afd80ef6966)
                check_type(argname="argument address_line1", value=address_line1, expected_type=type_hints["address_line1"])
                check_type(argname="argument city", value=city, expected_type=type_hints["city"])
                check_type(argname="argument contact_name", value=contact_name, expected_type=type_hints["contact_name"])
                check_type(argname="argument contact_phone_number", value=contact_phone_number, expected_type=type_hints["contact_phone_number"])
                check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
                check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
                check_type(argname="argument state_or_region", value=state_or_region, expected_type=type_hints["state_or_region"])
                check_type(argname="argument address_line2", value=address_line2, expected_type=type_hints["address_line2"])
                check_type(argname="argument address_line3", value=address_line3, expected_type=type_hints["address_line3"])
                check_type(argname="argument district_or_county", value=district_or_county, expected_type=type_hints["district_or_county"])
                check_type(argname="argument municipality", value=municipality, expected_type=type_hints["municipality"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address_line1": address_line1,
                "city": city,
                "contact_name": contact_name,
                "contact_phone_number": contact_phone_number,
                "country_code": country_code,
                "postal_code": postal_code,
                "state_or_region": state_or_region,
            }
            if address_line2 is not None:
                self._values["address_line2"] = address_line2
            if address_line3 is not None:
                self._values["address_line3"] = address_line3
            if district_or_county is not None:
                self._values["district_or_county"] = district_or_county
            if municipality is not None:
                self._values["municipality"] = municipality

        @builtins.property
        def address_line1(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-addressline1
            '''
            result = self._values.get("address_line1")
            assert result is not None, "Required property 'address_line1' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def city(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-city
            '''
            result = self._values.get("city")
            assert result is not None, "Required property 'city' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def contact_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-contactname
            '''
            result = self._values.get("contact_name")
            assert result is not None, "Required property 'contact_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def contact_phone_number(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-contactphonenumber
            '''
            result = self._values.get("contact_phone_number")
            assert result is not None, "Required property 'contact_phone_number' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def country_code(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-countrycode
            '''
            result = self._values.get("country_code")
            assert result is not None, "Required property 'country_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def postal_code(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-postalcode
            '''
            result = self._values.get("postal_code")
            assert result is not None, "Required property 'postal_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def state_or_region(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-stateorregion
            '''
            result = self._values.get("state_or_region")
            assert result is not None, "Required property 'state_or_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def address_line2(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-addressline2
            '''
            result = self._values.get("address_line2")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def address_line3(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-addressline3
            '''
            result = self._values.get("address_line3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def district_or_county(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-districtorcounty
            '''
            result = self._values.get("district_or_county")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def municipality(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-address.html#cfn-outposts-site-address-municipality
            '''
            result = self._values.get("municipality")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_outposts.CfnSite.RackPhysicalPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fiber_optic_cable_type": "fiberOpticCableType",
            "maximum_supported_weight_lbs": "maximumSupportedWeightLbs",
            "optical_standard": "opticalStandard",
            "power_connector": "powerConnector",
            "power_draw_kva": "powerDrawKva",
            "power_feed_drop": "powerFeedDrop",
            "power_phase": "powerPhase",
            "uplink_count": "uplinkCount",
            "uplink_gbps": "uplinkGbps",
        },
    )
    class RackPhysicalPropertiesProperty:
        def __init__(
            self,
            *,
            fiber_optic_cable_type: typing.Optional[builtins.str] = None,
            maximum_supported_weight_lbs: typing.Optional[builtins.str] = None,
            optical_standard: typing.Optional[builtins.str] = None,
            power_connector: typing.Optional[builtins.str] = None,
            power_draw_kva: typing.Optional[builtins.str] = None,
            power_feed_drop: typing.Optional[builtins.str] = None,
            power_phase: typing.Optional[builtins.str] = None,
            uplink_count: typing.Optional[builtins.str] = None,
            uplink_gbps: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param fiber_optic_cable_type: 
            :param maximum_supported_weight_lbs: 
            :param optical_standard: 
            :param power_connector: 
            :param power_draw_kva: 
            :param power_feed_drop: 
            :param power_phase: 
            :param uplink_count: 
            :param uplink_gbps: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_outposts as outposts
                
                rack_physical_properties_property = outposts.CfnSite.RackPhysicalPropertiesProperty(
                    fiber_optic_cable_type="fiberOpticCableType",
                    maximum_supported_weight_lbs="maximumSupportedWeightLbs",
                    optical_standard="opticalStandard",
                    power_connector="powerConnector",
                    power_draw_kva="powerDrawKva",
                    power_feed_drop="powerFeedDrop",
                    power_phase="powerPhase",
                    uplink_count="uplinkCount",
                    uplink_gbps="uplinkGbps"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0533d2e85b5d50a565e9323d56f74c12909cc0e4bb77d518fd147e861892dc6a)
                check_type(argname="argument fiber_optic_cable_type", value=fiber_optic_cable_type, expected_type=type_hints["fiber_optic_cable_type"])
                check_type(argname="argument maximum_supported_weight_lbs", value=maximum_supported_weight_lbs, expected_type=type_hints["maximum_supported_weight_lbs"])
                check_type(argname="argument optical_standard", value=optical_standard, expected_type=type_hints["optical_standard"])
                check_type(argname="argument power_connector", value=power_connector, expected_type=type_hints["power_connector"])
                check_type(argname="argument power_draw_kva", value=power_draw_kva, expected_type=type_hints["power_draw_kva"])
                check_type(argname="argument power_feed_drop", value=power_feed_drop, expected_type=type_hints["power_feed_drop"])
                check_type(argname="argument power_phase", value=power_phase, expected_type=type_hints["power_phase"])
                check_type(argname="argument uplink_count", value=uplink_count, expected_type=type_hints["uplink_count"])
                check_type(argname="argument uplink_gbps", value=uplink_gbps, expected_type=type_hints["uplink_gbps"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if fiber_optic_cable_type is not None:
                self._values["fiber_optic_cable_type"] = fiber_optic_cable_type
            if maximum_supported_weight_lbs is not None:
                self._values["maximum_supported_weight_lbs"] = maximum_supported_weight_lbs
            if optical_standard is not None:
                self._values["optical_standard"] = optical_standard
            if power_connector is not None:
                self._values["power_connector"] = power_connector
            if power_draw_kva is not None:
                self._values["power_draw_kva"] = power_draw_kva
            if power_feed_drop is not None:
                self._values["power_feed_drop"] = power_feed_drop
            if power_phase is not None:
                self._values["power_phase"] = power_phase
            if uplink_count is not None:
                self._values["uplink_count"] = uplink_count
            if uplink_gbps is not None:
                self._values["uplink_gbps"] = uplink_gbps

        @builtins.property
        def fiber_optic_cable_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-fiberopticcabletype
            '''
            result = self._values.get("fiber_optic_cable_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maximum_supported_weight_lbs(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-maximumsupportedweightlbs
            '''
            result = self._values.get("maximum_supported_weight_lbs")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def optical_standard(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-opticalstandard
            '''
            result = self._values.get("optical_standard")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def power_connector(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-powerconnector
            '''
            result = self._values.get("power_connector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def power_draw_kva(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-powerdrawkva
            '''
            result = self._values.get("power_draw_kva")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def power_feed_drop(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-powerfeeddrop
            '''
            result = self._values.get("power_feed_drop")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def power_phase(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-powerphase
            '''
            result = self._values.get("power_phase")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uplink_count(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-uplinkcount
            '''
            result = self._values.get("uplink_count")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uplink_gbps(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-outposts-site-rackphysicalproperties.html#cfn-outposts-site-rackphysicalproperties-uplinkgbps
            '''
            result = self._values.get("uplink_gbps")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RackPhysicalPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_outposts.CfnSiteProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "notes": "notes",
        "operating_address": "operatingAddress",
        "rack_physical_properties": "rackPhysicalProperties",
        "shipping_address": "shippingAddress",
        "tags": "tags",
    },
)
class CfnSiteProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        operating_address: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSite.AddressProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        rack_physical_properties: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSite.RackPhysicalPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        shipping_address: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSite.AddressProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSite``.

        :param name: 
        :param description: 
        :param notes: 
        :param operating_address: 
        :param rack_physical_properties: 
        :param shipping_address: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_outposts as outposts
            
            cfn_site_props = outposts.CfnSiteProps(
                name="name",
            
                # the properties below are optional
                description="description",
                notes="notes",
                operating_address=outposts.CfnSite.AddressProperty(
                    address_line1="addressLine1",
                    city="city",
                    contact_name="contactName",
                    contact_phone_number="contactPhoneNumber",
                    country_code="countryCode",
                    postal_code="postalCode",
                    state_or_region="stateOrRegion",
            
                    # the properties below are optional
                    address_line2="addressLine2",
                    address_line3="addressLine3",
                    district_or_county="districtOrCounty",
                    municipality="municipality"
                ),
                rack_physical_properties=outposts.CfnSite.RackPhysicalPropertiesProperty(
                    fiber_optic_cable_type="fiberOpticCableType",
                    maximum_supported_weight_lbs="maximumSupportedWeightLbs",
                    optical_standard="opticalStandard",
                    power_connector="powerConnector",
                    power_draw_kva="powerDrawKva",
                    power_feed_drop="powerFeedDrop",
                    power_phase="powerPhase",
                    uplink_count="uplinkCount",
                    uplink_gbps="uplinkGbps"
                ),
                shipping_address=outposts.CfnSite.AddressProperty(
                    address_line1="addressLine1",
                    city="city",
                    contact_name="contactName",
                    contact_phone_number="contactPhoneNumber",
                    country_code="countryCode",
                    postal_code="postalCode",
                    state_or_region="stateOrRegion",
            
                    # the properties below are optional
                    address_line2="addressLine2",
                    address_line3="addressLine3",
                    district_or_county="districtOrCounty",
                    municipality="municipality"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6361d62f51e1c0318f080874935ebe422c3e6ffff51f3ca0d613438c9933f7fa)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument notes", value=notes, expected_type=type_hints["notes"])
            check_type(argname="argument operating_address", value=operating_address, expected_type=type_hints["operating_address"])
            check_type(argname="argument rack_physical_properties", value=rack_physical_properties, expected_type=type_hints["rack_physical_properties"])
            check_type(argname="argument shipping_address", value=shipping_address, expected_type=type_hints["shipping_address"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if notes is not None:
            self._values["notes"] = notes
        if operating_address is not None:
            self._values["operating_address"] = operating_address
        if rack_physical_properties is not None:
            self._values["rack_physical_properties"] = rack_physical_properties
        if shipping_address is not None:
            self._values["shipping_address"] = shipping_address
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html#cfn-outposts-site-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html#cfn-outposts-site-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notes(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html#cfn-outposts-site-notes
        '''
        result = self._values.get("notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_address(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html#cfn-outposts-site-operatingaddress
        '''
        result = self._values.get("operating_address")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]], result)

    @builtins.property
    def rack_physical_properties(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.RackPhysicalPropertiesProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html#cfn-outposts-site-rackphysicalproperties
        '''
        result = self._values.get("rack_physical_properties")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.RackPhysicalPropertiesProperty"]], result)

    @builtins.property
    def shipping_address(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html#cfn-outposts-site-shippingaddress
        '''
        result = self._values.get("shipping_address")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSite.AddressProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-outposts-site.html#cfn-outposts-site-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSiteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnOutpost",
    "CfnOutpostProps",
    "CfnSite",
    "CfnSiteProps",
]

publication.publish()

def _typecheckingstub__8971624592e127fd49b80bfd3f7d1773b1a737fe09f1a384044eca07f3debd33(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    site_id: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    availability_zone_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    supported_hardware_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61961d4e0566bf05f2597978a460d3a976e7809bc7a0eb487e3151e739032665(
    resource: _aws_outposts_621ae39e.IOutpostRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4a5c12c2db8d5527e5117fc089ee107f51ba55fca66a6efa7c61cc2f7d690b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc0bfd25164f3247f518e913212c5050d68069062057269d8ef5d0c5b45a460a(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c268c09db91b390484e524eda84f82b70e6d5e98810828db955c728c9d010f2c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96878466b18f3fde129ce715176b1a8b6971e0c697710523524e28015fc9e26f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813dc2d433fde86852245dad96c7408426d135ff51aabfc35f5e2e58bdcf7f0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f515cd9608704083448cb4e153fcd2e7fe3b5d04ed3ac905e18982b828eb47c4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de836b50791de14bc30b6d2267611fea2146dd4fd508dcd9200c6be5695a8214(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3746ec72319677760081ffe1b0c31593a486e124b4bef46a86eaee5834259f34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5393eba0e1264b7792630bf2941d28ac6590e8a457d5d29010fd84bec24108(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289cf60bd40b5709a59f9ab5a3c84626d213bc19d3400937b7dc798b024dc67e(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c560f1fe019e8891a9423ca456866618c21af5d07eb2c1020c2a762fd4752b81(
    *,
    name: builtins.str,
    site_id: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    availability_zone_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    supported_hardware_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d714077b9a690b88c6fc96e15456f27991a8d901eb70ea9ecb9b46e55b8328(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    notes: typing.Optional[builtins.str] = None,
    operating_address: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSite.AddressProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rack_physical_properties: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSite.RackPhysicalPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    shipping_address: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSite.AddressProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6373697618d360cefd50c9675ce87f1ada8b9106d9dc21ecd34c64c347292827(
    resource: _aws_outposts_621ae39e.ISiteRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf3e014728bbb5b26e4ede2b3f861cac8ac90b7e6e119c27c3a925e369fa19f(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce999d4e727c4ebbf4e71f951f5c10eea4ba80282674926a7ee20f1692524180(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad84a7b53d8f4f5ea601b30057d197f581e6c7641a95cff710b72dfc631084a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170e09c6bdb68519d4260397cf593c572f4ef1be15fb2f4c45fff0bf9823ceaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60320fde224f99d0ef729abd96d1dc84c0d5b0f87b861e301f13926af4e5a47c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f705d86c50955e648aea39f390b415f32cc2a50c3f8364310e00f2cae45f4d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d30ad0cda0adcf03199c7453890fa9db026c31e062f8da0788d13d7258d1713(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSite.AddressProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4861c8d2f7d3f54a8335886ef48616d24ea53147bfab93f58603d3c34b3c6905(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSite.RackPhysicalPropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b013059e4e57daab1e78b74597803d134aecab91285303ebc1622f2a299a5967(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSite.AddressProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9eb786cfd3ba4d3ab93d6fcda01d4852ddcfe30cfbd2ab5e3ecad2e3b63503(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a5383ffcc62bcf8b7d6f719f9da5d9251badec11bd8f4f73523afd80ef6966(
    *,
    address_line1: builtins.str,
    city: builtins.str,
    contact_name: builtins.str,
    contact_phone_number: builtins.str,
    country_code: builtins.str,
    postal_code: builtins.str,
    state_or_region: builtins.str,
    address_line2: typing.Optional[builtins.str] = None,
    address_line3: typing.Optional[builtins.str] = None,
    district_or_county: typing.Optional[builtins.str] = None,
    municipality: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0533d2e85b5d50a565e9323d56f74c12909cc0e4bb77d518fd147e861892dc6a(
    *,
    fiber_optic_cable_type: typing.Optional[builtins.str] = None,
    maximum_supported_weight_lbs: typing.Optional[builtins.str] = None,
    optical_standard: typing.Optional[builtins.str] = None,
    power_connector: typing.Optional[builtins.str] = None,
    power_draw_kva: typing.Optional[builtins.str] = None,
    power_feed_drop: typing.Optional[builtins.str] = None,
    power_phase: typing.Optional[builtins.str] = None,
    uplink_count: typing.Optional[builtins.str] = None,
    uplink_gbps: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6361d62f51e1c0318f080874935ebe422c3e6ffff51f3ca0d613438c9933f7fa(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    notes: typing.Optional[builtins.str] = None,
    operating_address: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSite.AddressProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rack_physical_properties: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSite.RackPhysicalPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    shipping_address: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSite.AddressProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
