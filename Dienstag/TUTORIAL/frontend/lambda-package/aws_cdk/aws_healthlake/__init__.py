r'''
# AWS::HealthLake Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_healthlake as healthlake
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for HealthLake construct libraries](https://constructs.dev/search?q=healthlake)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::HealthLake resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_HealthLake.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::HealthLake](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_HealthLake.html).

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
    import aws_cdk.interfaces.aws_healthlake as _aws_healthlake_d03fc20c
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_healthlake_d03fc20c = _LazyImport("aws_cdk.interfaces.aws_healthlake")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_healthlake_d03fc20c.IDataTransformationProfileRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnDataTransformationProfile(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_healthlake.CfnDataTransformationProfile",
):
    '''Creates a Data Transformation Profile in AWS HealthLake that converts healthcare data from a source format (such as C-CDA or CSV) into FHIR R4.

    A profile is immutable once created; to change its template content, replace the resource. Only its tags can be updated in place.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-datatransformationprofile.html
    :cloudformationResource: AWS::HealthLake::DataTransformationProfile
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_healthlake as healthlake
        
        cfn_data_transformation_profile = healthlake.CfnDataTransformationProfile(self, "MyCfnDataTransformationProfile",
            profile_name="profileName",
            source_format="sourceFormat",
        
            # the properties below are optional
            kms_key_id="kmsKeyId",
            profile_description="profileDescription",
            source=healthlake.CfnDataTransformationProfile.SourceProperty(
                existing_versioned_profile_id=healthlake.CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty(
                    profile_id="profileId",
                    version=123
                ),
                profile_mapping=healthlake.CfnDataTransformationProfile.ProfileMappingSourceProperty(
                    profile_mapping={
                        "profile_mapping_key": "profileMapping"
                    }
                ),
                starter_profile=healthlake.CfnDataTransformationProfile.StarterProfileSourceProperty(
                    starter_profile_name="starterProfileName"
                )
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
        profile_name: builtins.str,
        source_format: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        profile_description: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataTransformationProfile.SourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::HealthLake::DataTransformationProfile``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param profile_name: The human-readable name of the profile.
        :param source_format: The source format that this profile converts from.
        :param kms_key_id: The identifier (key ID or ARN) of a customer-managed KMS key used to encrypt the profile's template content at rest. If omitted, an AWS owned key is used.
        :param profile_description: A human-readable description of the profile's purpose.
        :param source: The source from which to create the profile's initial template content. Exactly one of the members must be specified. Use StarterProfile (C-CDA only), ProfileMapping (C-CDA or CSV), or ExistingVersionedProfileId to clone an existing profile. Each produces a published profile.
        :param tags: An array of key-value pairs to apply to this profile.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ffa7f40a55c908b5c71d8b021cb4bc5def1f3d33e73427064b902fe2f00f5cd5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataTransformationProfileProps(
            profile_name=profile_name,
            source_format=source_format,
            kms_key_id=kms_key_id,
            profile_description=profile_description,
            source=source,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDataTransformationProfile")
    @builtins.classmethod
    def arn_for_data_transformation_profile(
        cls,
        resource: "_aws_healthlake_d03fc20c.IDataTransformationProfileRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ba9ba7186101ad3636b33a3380dbbf50e17791493b400773d1f51dac14d23ddc)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDataTransformationProfile", [resource]))

    @jsii.member(jsii_name="isCfnDataTransformationProfile")
    @builtins.classmethod
    def is_cfn_data_transformation_profile(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDataTransformationProfile.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d96bb697a4df81a1f6f068354d53364d470246af42304fec6d76824cebd19fb1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDataTransformationProfile", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__17fe2cefd9247d79f84504fd1bb7c4dd592b3257d789e6bf240e7b6b533763f8)
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
            type_hints = cached_type_hints(_typecheckingstub__91abd016be8ce2f2a2a6f50f134f4bbfa65013218ced141348e8e50dad36f145)
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
        '''The Amazon Resource Name (ARN) of the data transformation profile.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileId")
    def attr_profile_id(self) -> builtins.str:
        '''The unique, server-generated identifier of the profile (32-character lowercase hexadecimal).

        :cloudformationAttribute: ProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileId"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetFormat")
    def attr_target_format(self) -> builtins.str:
        '''The target format that this profile converts to.

        Always FHIR_R4.

        :cloudformationAttribute: TargetFormat
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetFormat"))

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
    @jsii.member(jsii_name="dataTransformationProfileRef")
    def data_transformation_profile_ref(
        self,
    ) -> "_aws_healthlake_d03fc20c.DataTransformationProfileReference":
        '''A reference to a DataTransformationProfile resource.'''
        return typing.cast("_aws_healthlake_d03fc20c.DataTransformationProfileReference", jsii.get(self, "dataTransformationProfileRef"))

    @builtins.property
    @jsii.member(jsii_name="profileName")
    def profile_name(self) -> builtins.str:
        '''The human-readable name of the profile.'''
        return typing.cast(builtins.str, jsii.get(self, "profileName"))

    @profile_name.setter
    def profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9ebc07ff74a99d99b611bf1ccdf04f15b0439f0941af32a0d3f29788ccd1b98e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceFormat")
    def source_format(self) -> builtins.str:
        '''The source format that this profile converts from.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceFormat"))

    @source_format.setter
    def source_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__15c904204562f714f3203e7b9697e0b749faa45d018ec8fcf28958a8a8a99056)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier (key ID or ARN) of a customer-managed KMS key used to encrypt the profile's template content at rest.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a0295dd98c6aed49aaf7df89c6d4a3e2ff56e0dbaa8ec41340be48fd349e4b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="profileDescription")
    def profile_description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the profile's purpose.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileDescription"))

    @profile_description.setter
    def profile_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__07be715f497b62f1ea6f103ef6fea6b01a1c3265134bef46ef3a2dbc49d2948b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.SourceProperty"]]:
        '''The source from which to create the profile's initial template content.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.SourceProperty"]], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.SourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0634fb098e12ecb4f06c1a886cb10ec45fdc1789d44fbefa8babca15e9440cb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this profile.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bcd46233cb0eecf58baa705df6c53ad8c03fa75cd42a5011e9e49f0e82b0839a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"profile_id": "profileId", "version": "version"},
    )
    class ExistingVersionedProfileSourceProperty:
        def __init__(self, *, profile_id: builtins.str, version: jsii.Number) -> None:
            '''Create the profile by cloning a specific version of an existing profile.

            :param profile_id: The unique identifier of the source profile to clone.
            :param version: The version number of the source profile to clone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                existing_versioned_profile_source_property = healthlake.CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty(
                    profile_id="profileId",
                    version=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__70d021157bc45cc79c2c24f0227d22c35e4e523115d5be9d2677db6747bbb1b8)
                check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "profile_id": profile_id,
                "version": version,
            }

        @builtins.property
        def profile_id(self) -> builtins.str:
            '''The unique identifier of the source profile to clone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource.html#cfn-healthlake-datatransformationprofile-existingversionedprofilesource-profileid
            '''
            result = self._values.get("profile_id")
            assert result is not None, "Required property 'profile_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> jsii.Number:
            '''The version number of the source profile to clone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-existingversionedprofilesource.html#cfn-healthlake-datatransformationprofile-existingversionedprofilesource-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExistingVersionedProfileSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnDataTransformationProfile.ProfileMappingSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"profile_mapping": "profileMapping"},
    )
    class ProfileMappingSourceProperty:
        def __init__(
            self,
            *,
            profile_mapping: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]],
        ) -> None:
            '''Create the profile from raw Velocity template mapping content.

            :param profile_mapping: Map of template file paths to their Velocity template content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-profilemappingsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                profile_mapping_source_property = healthlake.CfnDataTransformationProfile.ProfileMappingSourceProperty(
                    profile_mapping={
                        "profile_mapping_key": "profileMapping"
                    }
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__21589af684261b5e206ff0002a218cd1f07462e63c1dad79bbca931e75dbee5f)
                check_type(argname="argument profile_mapping", value=profile_mapping, expected_type=type_hints["profile_mapping"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "profile_mapping": profile_mapping,
            }

        @builtins.property
        def profile_mapping(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]:
            '''Map of template file paths to their Velocity template content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-profilemappingsource.html#cfn-healthlake-datatransformationprofile-profilemappingsource-profilemapping
            '''
            result = self._values.get("profile_mapping")
            assert result is not None, "Required property 'profile_mapping' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProfileMappingSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnDataTransformationProfile.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "existing_versioned_profile_id": "existingVersionedProfileId",
            "profile_mapping": "profileMapping",
            "starter_profile": "starterProfile",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            existing_versioned_profile_id: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            profile_mapping: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataTransformationProfile.ProfileMappingSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            starter_profile: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataTransformationProfile.StarterProfileSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source from which to create the profile's initial template content.

            Exactly one of the members must be specified. Use StarterProfile (C-CDA only), ProfileMapping (C-CDA or CSV), or ExistingVersionedProfileId to clone an existing profile. Each produces a published profile.

            :param existing_versioned_profile_id: Create the profile by cloning a specific version of an existing profile.
            :param profile_mapping: Create the profile from raw Velocity template mapping content.
            :param starter_profile: Create the profile from a predefined starter profile of transformation templates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                source_property = healthlake.CfnDataTransformationProfile.SourceProperty(
                    existing_versioned_profile_id=healthlake.CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty(
                        profile_id="profileId",
                        version=123
                    ),
                    profile_mapping=healthlake.CfnDataTransformationProfile.ProfileMappingSourceProperty(
                        profile_mapping={
                            "profile_mapping_key": "profileMapping"
                        }
                    ),
                    starter_profile=healthlake.CfnDataTransformationProfile.StarterProfileSourceProperty(
                        starter_profile_name="starterProfileName"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__9f6738e7624c37b9b0601248d91777f2bcadb7e16c0567df96df6b4c183ecaf0)
                check_type(argname="argument existing_versioned_profile_id", value=existing_versioned_profile_id, expected_type=type_hints["existing_versioned_profile_id"])
                check_type(argname="argument profile_mapping", value=profile_mapping, expected_type=type_hints["profile_mapping"])
                check_type(argname="argument starter_profile", value=starter_profile, expected_type=type_hints["starter_profile"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if existing_versioned_profile_id is not None:
                self._values["existing_versioned_profile_id"] = existing_versioned_profile_id
            if profile_mapping is not None:
                self._values["profile_mapping"] = profile_mapping
            if starter_profile is not None:
                self._values["starter_profile"] = starter_profile

        @builtins.property
        def existing_versioned_profile_id(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty"]]:
            '''Create the profile by cloning a specific version of an existing profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-source.html#cfn-healthlake-datatransformationprofile-source-existingversionedprofileid
            '''
            result = self._values.get("existing_versioned_profile_id")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty"]], result)

        @builtins.property
        def profile_mapping(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.ProfileMappingSourceProperty"]]:
            '''Create the profile from raw Velocity template mapping content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-source.html#cfn-healthlake-datatransformationprofile-source-profilemapping
            '''
            result = self._values.get("profile_mapping")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.ProfileMappingSourceProperty"]], result)

        @builtins.property
        def starter_profile(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.StarterProfileSourceProperty"]]:
            '''Create the profile from a predefined starter profile of transformation templates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-source.html#cfn-healthlake-datatransformationprofile-source-starterprofile
            '''
            result = self._values.get("starter_profile")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.StarterProfileSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnDataTransformationProfile.StarterProfileSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"starter_profile_name": "starterProfileName"},
    )
    class StarterProfileSourceProperty:
        def __init__(self, *, starter_profile_name: builtins.str) -> None:
            '''Create the profile from a predefined starter profile of transformation templates.

            :param starter_profile_name: The name of the starter profile to seed the profile from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-starterprofilesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                starter_profile_source_property = healthlake.CfnDataTransformationProfile.StarterProfileSourceProperty(
                    starter_profile_name="starterProfileName"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__3b61a87dcbbda68f6695fa1aad8fd146ca983dcebd45fb4810fcda352a0c05ad)
                check_type(argname="argument starter_profile_name", value=starter_profile_name, expected_type=type_hints["starter_profile_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "starter_profile_name": starter_profile_name,
            }

        @builtins.property
        def starter_profile_name(self) -> builtins.str:
            '''The name of the starter profile to seed the profile from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-datatransformationprofile-starterprofilesource.html#cfn-healthlake-datatransformationprofile-starterprofilesource-starterprofilename
            '''
            result = self._values.get("starter_profile_name")
            assert result is not None, "Required property 'starter_profile_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StarterProfileSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_healthlake.CfnDataTransformationProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "profile_name": "profileName",
        "source_format": "sourceFormat",
        "kms_key_id": "kmsKeyId",
        "profile_description": "profileDescription",
        "source": "source",
        "tags": "tags",
    },
)
class CfnDataTransformationProfileProps:
    def __init__(
        self,
        *,
        profile_name: builtins.str,
        source_format: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        profile_description: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnDataTransformationProfile.SourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataTransformationProfile``.

        :param profile_name: The human-readable name of the profile.
        :param source_format: The source format that this profile converts from.
        :param kms_key_id: The identifier (key ID or ARN) of a customer-managed KMS key used to encrypt the profile's template content at rest. If omitted, an AWS owned key is used.
        :param profile_description: A human-readable description of the profile's purpose.
        :param source: The source from which to create the profile's initial template content. Exactly one of the members must be specified. Use StarterProfile (C-CDA only), ProfileMapping (C-CDA or CSV), or ExistingVersionedProfileId to clone an existing profile. Each produces a published profile.
        :param tags: An array of key-value pairs to apply to this profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-datatransformationprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_healthlake as healthlake
            
            cfn_data_transformation_profile_props = healthlake.CfnDataTransformationProfileProps(
                profile_name="profileName",
                source_format="sourceFormat",
            
                # the properties below are optional
                kms_key_id="kmsKeyId",
                profile_description="profileDescription",
                source=healthlake.CfnDataTransformationProfile.SourceProperty(
                    existing_versioned_profile_id=healthlake.CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty(
                        profile_id="profileId",
                        version=123
                    ),
                    profile_mapping=healthlake.CfnDataTransformationProfile.ProfileMappingSourceProperty(
                        profile_mapping={
                            "profile_mapping_key": "profileMapping"
                        }
                    ),
                    starter_profile=healthlake.CfnDataTransformationProfile.StarterProfileSourceProperty(
                        starter_profile_name="starterProfileName"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__76ec0f2eb8014f6283a9cedab74d21e354d4017d5caa09bc38c8c7e3338c2a49)
            check_type(argname="argument profile_name", value=profile_name, expected_type=type_hints["profile_name"])
            check_type(argname="argument source_format", value=source_format, expected_type=type_hints["source_format"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument profile_description", value=profile_description, expected_type=type_hints["profile_description"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_name": profile_name,
            "source_format": source_format,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if profile_description is not None:
            self._values["profile_description"] = profile_description
        if source is not None:
            self._values["source"] = source
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def profile_name(self) -> builtins.str:
        '''The human-readable name of the profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-datatransformationprofile.html#cfn-healthlake-datatransformationprofile-profilename
        '''
        result = self._values.get("profile_name")
        assert result is not None, "Required property 'profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_format(self) -> builtins.str:
        '''The source format that this profile converts from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-datatransformationprofile.html#cfn-healthlake-datatransformationprofile-sourceformat
        '''
        result = self._values.get("source_format")
        assert result is not None, "Required property 'source_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier (key ID or ARN) of a customer-managed KMS key used to encrypt the profile's template content at rest.

        If omitted, an AWS owned key is used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-datatransformationprofile.html#cfn-healthlake-datatransformationprofile-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile_description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the profile's purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-datatransformationprofile.html#cfn-healthlake-datatransformationprofile-profiledescription
        '''
        result = self._values.get("profile_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.SourceProperty"]]:
        '''The source from which to create the profile's initial template content.

        Exactly one of the members must be specified. Use StarterProfile (C-CDA only), ProfileMapping (C-CDA or CSV), or ExistingVersionedProfileId to clone an existing profile. Each produces a published profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-datatransformationprofile.html#cfn-healthlake-datatransformationprofile-source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnDataTransformationProfile.SourceProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-datatransformationprofile.html#cfn-healthlake-datatransformationprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataTransformationProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_healthlake_d03fc20c.IFHIRDatastoreRef, _aws_cdk_0cae9daa.ITaggable)
class CfnFHIRDatastore(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore",
):
    '''Creates a Data Store that can ingest and export FHIR formatted data.

    .. epigraph::

       Please note that when a user tries to do an Update operation via CloudFormation, changes to the Data Store name, Type Version, PreloadDataConfig, or SSEConfiguration will delete their existing Data Store for the stack and create a new one. This will lead to potential loss of data.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html
    :cloudformationResource: AWS::HealthLake::FHIRDatastore
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_healthlake as healthlake
        
        cfn_fhir_datastore = healthlake.CfnFHIRDatastore(self, "MyCfnFHIRDatastore",
            datastore_type_version="datastoreTypeVersion",
        
            # the properties below are optional
            datastore_name="datastoreName",
            identity_provider_configuration=healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty(
                authorization_strategy="authorizationStrategy",
        
                # the properties below are optional
                fine_grained_authorization_enabled=False,
                idp_lambda_arn="idpLambdaArn",
                metadata="metadata"
            ),
            preload_data_config=healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                preload_data_type="preloadDataType"
            ),
            sse_configuration=healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                    cmk_type="cmkType",
        
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
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
        datastore_type_version: builtins.str,
        datastore_name: typing.Optional[builtins.str] = None,
        identity_provider_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFHIRDatastore.IdentityProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        preload_data_config: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFHIRDatastore.PreloadDataConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFHIRDatastore.SseConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::HealthLake::FHIRDatastore``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param datastore_type_version: The FHIR release version supported by the data store. Current support is for version ``R4`` .
        :param datastore_name: The data store name (user-generated).
        :param identity_provider_configuration: The identity provider configuration selected when the data store was created.
        :param preload_data_config: The preloaded Synthea data configuration for the data store.
        :param sse_configuration: The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5a84066c5df4c48a34d687987d48edfe8b65e8bda26e4da5f30db9c938e54b90)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFHIRDatastoreProps(
            datastore_type_version=datastore_type_version,
            datastore_name=datastore_name,
            identity_provider_configuration=identity_provider_configuration,
            preload_data_config=preload_data_config,
            sse_configuration=sse_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForFHIRDatastore")
    @builtins.classmethod
    def arn_for_fhir_datastore(
        cls,
        resource: "_aws_healthlake_d03fc20c.IFHIRDatastoreRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3f0cb1aa981e44d9252c4ccb23e5e4300e3380368e5dead8a05fb5dd9f413b00)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForFHIRDatastore", [resource]))

    @jsii.member(jsii_name="fromDatastoreId")
    @builtins.classmethod
    def from_datastore_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        datastore_id: builtins.str,
    ) -> "_aws_healthlake_d03fc20c.IFHIRDatastoreRef":
        '''Creates a new IFHIRDatastoreRef from a datastoreId.

        :param scope: -
        :param id: -
        :param datastore_id: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1aca17223f33eab4c3c32fe59502f6e15af4d519ea58e4d602d2408ce0b1dfa4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument datastore_id", value=datastore_id, expected_type=type_hints["datastore_id"])
        return typing.cast("_aws_healthlake_d03fc20c.IFHIRDatastoreRef", jsii.sinvoke(cls, "fromDatastoreId", [scope, id, datastore_id]))

    @jsii.member(jsii_name="fromFHIRDatastoreArn")
    @builtins.classmethod
    def from_fhir_datastore_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_aws_healthlake_d03fc20c.IFHIRDatastoreRef":
        '''Creates a new IFHIRDatastoreRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fb13a8ddb4107ab5128d62b9ccef2aef1a010a8f819b0cbe0bd1abf0438e0d22)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_aws_healthlake_d03fc20c.IFHIRDatastoreRef", jsii.sinvoke(cls, "fromFHIRDatastoreArn", [scope, id, arn]))

    @jsii.member(jsii_name="isCfnFHIRDatastore")
    @builtins.classmethod
    def is_cfn_fhir_datastore(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFHIRDatastore.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__67828597c6b23eb59e180c8c9477691634e8d3539e804a608e5af42e84fe8bc8)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFHIRDatastore", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f9041dc50c8109815f2c8dd04e804c6471002a65ab5f8f21a4695f6a237e3703)
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
            type_hints = cached_type_hints(_typecheckingstub__98c34e70b6ec2df3b888529b3c31e66d8c6bede9b01bd8e9f59661918d44ba4f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''The time that a Data Store was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAtNanos")
    def attr_created_at_nanos(self) -> jsii.Number:
        '''
        :cloudformationAttribute: CreatedAt.Nanos
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreatedAtNanos"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAtSeconds")
    def attr_created_at_seconds(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt.Seconds
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAtSeconds"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreArn")
    def attr_datastore_arn(self) -> builtins.str:
        '''The Data Store ARN is generated during the creation of the Data Store and can be found in the output from the initial Data Store creation request.

        :cloudformationAttribute: DatastoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreEndpoint")
    def attr_datastore_endpoint(self) -> builtins.str:
        '''The endpoint for the created Data Store.

        :cloudformationAttribute: DatastoreEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreId")
    def attr_datastore_id(self) -> builtins.str:
        '''The Amazon generated Data Store id.

        This id is in the output from the initial Data Store creation call.

        :cloudformationAttribute: DatastoreId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreId"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreStatus")
    def attr_datastore_status(self) -> builtins.str:
        '''The status of the FHIR Data Store.

        Possible statuses are ‘CREATING’, ‘ACTIVE’, ‘DELETING’, ‘DELETED’.

        :cloudformationAttribute: DatastoreStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="fhirDatastoreRef")
    def fhir_datastore_ref(self) -> "_aws_healthlake_d03fc20c.FHIRDatastoreReference":
        '''A reference to a FHIRDatastore resource.'''
        return typing.cast("_aws_healthlake_d03fc20c.FHIRDatastoreReference", jsii.get(self, "fhirDatastoreRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="datastoreTypeVersion")
    def datastore_type_version(self) -> builtins.str:
        '''The FHIR release version supported by the data store.'''
        return typing.cast(builtins.str, jsii.get(self, "datastoreTypeVersion"))

    @datastore_type_version.setter
    def datastore_type_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5808500ce498cbcd60021c25c05f2f5ec6982551bc42bc79b3964a61257718e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreTypeVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="datastoreName")
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''The data store name (user-generated).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datastoreName"))

    @datastore_name.setter
    def datastore_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7a3d86ac6fd32fffececf8454df94145383c2e779b9b5f1a30896102278cd1a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="identityProviderConfiguration")
    def identity_provider_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.IdentityProviderConfigurationProperty"]]:
        '''The identity provider configuration selected when the data store was created.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.IdentityProviderConfigurationProperty"]], jsii.get(self, "identityProviderConfiguration"))

    @identity_provider_configuration.setter
    def identity_provider_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.IdentityProviderConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__612b8cf4bba44e8e4744db8a7c2eaefe0b9bd601172c067d2c5a9feeb75cb14f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="preloadDataConfig")
    def preload_data_config(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.PreloadDataConfigProperty"]]:
        '''The preloaded Synthea data configuration for the data store.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.PreloadDataConfigProperty"]], jsii.get(self, "preloadDataConfig"))

    @preload_data_config.setter
    def preload_data_config(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.PreloadDataConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4b4d362bc0e9c9065e9f83741b0f46cfc52f253212d6a4551c7a2d9e4fd7e630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preloadDataConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sseConfiguration")
    def sse_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.SseConfigurationProperty"]]:
        '''The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.SseConfigurationProperty"]], jsii.get(self, "sseConfiguration"))

    @sse_configuration.setter
    def sse_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.SseConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d21d284c17f3b1e178b27b28fe912e0eaebeaa7ca9612eff81512c42f71c29d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__28ffa2ce0bad1140b8ffa060738f5e180bc7033b7f2e9f274ce2d1d871b5d620)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.CreatedAtProperty",
        jsii_struct_bases=[],
        name_mapping={"nanos": "nanos", "seconds": "seconds"},
    )
    class CreatedAtProperty:
        def __init__(self, *, nanos: jsii.Number, seconds: builtins.str) -> None:
            '''The time that a Data Store was created.

            :param nanos: Nanoseconds.
            :param seconds: Seconds since epoch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                created_at_property = healthlake.CfnFHIRDatastore.CreatedAtProperty(
                    nanos=123,
                    seconds="seconds"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__914232fa94e4874b18f9fa312fe19be92103d3c527212c1cc7038dd05916c72f)
                check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
                check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "nanos": nanos,
                "seconds": seconds,
            }

        @builtins.property
        def nanos(self) -> jsii.Number:
            '''Nanoseconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html#cfn-healthlake-fhirdatastore-createdat-nanos
            '''
            result = self._values.get("nanos")
            assert result is not None, "Required property 'nanos' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def seconds(self) -> builtins.str:
            '''Seconds since epoch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html#cfn-healthlake-fhirdatastore-createdat-seconds
            '''
            result = self._values.get("seconds")
            assert result is not None, "Required property 'seconds' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreatedAtProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_strategy": "authorizationStrategy",
            "fine_grained_authorization_enabled": "fineGrainedAuthorizationEnabled",
            "idp_lambda_arn": "idpLambdaArn",
            "metadata": "metadata",
        },
    )
    class IdentityProviderConfigurationProperty:
        def __init__(
            self,
            *,
            authorization_strategy: builtins.str,
            fine_grained_authorization_enabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            idp_lambda_arn: typing.Optional[builtins.str] = None,
            metadata: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The identity provider configuration selected when the data store was created.

            :param authorization_strategy: The authorization strategy selected when the HealthLake data store is created. .. epigraph:: HealthLake provides support for both SMART on FHIR V1 and V2 as described below. - ``SMART_ON_FHIR_V1`` – Support for only SMART on FHIR V1, which includes ``read`` (read/search) and ``write`` (create/update/delete) permissions. - ``SMART_ON_FHIR`` – Support for both SMART on FHIR V1 and V2, which includes ``create`` , ``read`` , ``update`` , ``delete`` , and ``search`` permissions. - ``AWS_AUTH`` – The default HealthLake authorization strategy; not affiliated with SMART on FHIR.
            :param fine_grained_authorization_enabled: The parameter to enable SMART on FHIR fine-grained authorization for the data store.
            :param idp_lambda_arn: The Amazon Resource Name (ARN) of the Lambda function to use to decode the access token created by the authorization server.
            :param metadata: The JSON metadata elements to use in your identity provider configuration. Required elements are listed based on the launch specification of the SMART application. For more information on all possible elements, see `Metadata <https://docs.aws.amazon.com/https://build.fhir.org/ig/HL7/smart-app-launch/conformance.html#metadata>`_ in SMART's App Launch specification. ``authorization_endpoint`` : The URL to the OAuth2 authorization endpoint. ``grant_types_supported`` : An array of grant types that are supported at the token endpoint. You must provide at least one grant type option. Valid options are ``authorization_code`` and ``client_credentials`` . ``token_endpoint`` : The URL to the OAuth2 token endpoint. ``capabilities`` : An array of strings of the SMART capabilities that the authorization server supports. ``code_challenge_methods_supported`` : An array of strings of supported PKCE code challenge methods. You must include the ``S256`` method in the array of PKCE code challenge methods.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                identity_provider_configuration_property = healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty(
                    authorization_strategy="authorizationStrategy",
                
                    # the properties below are optional
                    fine_grained_authorization_enabled=False,
                    idp_lambda_arn="idpLambdaArn",
                    metadata="metadata"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0f028d556a7a738b78a7fbfb130c7243f69ba20b6367ea5c21f2e6bcc60445fb)
                check_type(argname="argument authorization_strategy", value=authorization_strategy, expected_type=type_hints["authorization_strategy"])
                check_type(argname="argument fine_grained_authorization_enabled", value=fine_grained_authorization_enabled, expected_type=type_hints["fine_grained_authorization_enabled"])
                check_type(argname="argument idp_lambda_arn", value=idp_lambda_arn, expected_type=type_hints["idp_lambda_arn"])
                check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorization_strategy": authorization_strategy,
            }
            if fine_grained_authorization_enabled is not None:
                self._values["fine_grained_authorization_enabled"] = fine_grained_authorization_enabled
            if idp_lambda_arn is not None:
                self._values["idp_lambda_arn"] = idp_lambda_arn
            if metadata is not None:
                self._values["metadata"] = metadata

        @builtins.property
        def authorization_strategy(self) -> builtins.str:
            '''The authorization strategy selected when the HealthLake data store is created.

            .. epigraph::

               HealthLake provides support for both SMART on FHIR V1 and V2 as described below.

               - ``SMART_ON_FHIR_V1`` – Support for only SMART on FHIR V1, which includes ``read`` (read/search) and ``write`` (create/update/delete) permissions.
               - ``SMART_ON_FHIR`` – Support for both SMART on FHIR V1 and V2, which includes ``create`` , ``read`` , ``update`` , ``delete`` , and ``search`` permissions.
               - ``AWS_AUTH`` – The default HealthLake authorization strategy; not affiliated with SMART on FHIR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-authorizationstrategy
            '''
            result = self._values.get("authorization_strategy")
            assert result is not None, "Required property 'authorization_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fine_grained_authorization_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''The parameter to enable SMART on FHIR fine-grained authorization for the data store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-finegrainedauthorizationenabled
            '''
            result = self._values.get("fine_grained_authorization_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def idp_lambda_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Lambda function to use to decode the access token created by the authorization server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-idplambdaarn
            '''
            result = self._values.get("idp_lambda_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metadata(self) -> typing.Optional[builtins.str]:
            '''The JSON metadata elements to use in your identity provider configuration.

            Required elements are listed based on the launch specification of the SMART application. For more information on all possible elements, see `Metadata <https://docs.aws.amazon.com/https://build.fhir.org/ig/HL7/smart-app-launch/conformance.html#metadata>`_ in SMART's App Launch specification.

            ``authorization_endpoint`` : The URL to the OAuth2 authorization endpoint.

            ``grant_types_supported`` : An array of grant types that are supported at the token endpoint. You must provide at least one grant type option. Valid options are ``authorization_code`` and ``client_credentials`` .

            ``token_endpoint`` : The URL to the OAuth2 token endpoint.

            ``capabilities`` : An array of strings of the SMART capabilities that the authorization server supports.

            ``code_challenge_methods_supported`` : An array of strings of supported PKCE code challenge methods. You must include the ``S256`` method in the array of PKCE code challenge methods.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-metadata
            '''
            result = self._values.get("metadata")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityProviderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"cmk_type": "cmkType", "kms_key_id": "kmsKeyId"},
    )
    class KmsEncryptionConfigProperty:
        def __init__(
            self,
            *,
            cmk_type: builtins.str,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The customer-managed-key(CMK) used when creating a Data Store.

            If a customer owned key is not specified, an Amazon owned key will be used for encryption.

            :param cmk_type: The type of customer-managed-key(CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and Amazon owned CMKs. For more information on CMK types, see `KmsEncryptionConfig <https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html#HealthLake-Type-KmsEncryptionConfig-CmkType>`_ .
            :param kms_key_id: The Key Management Service (KMS) encryption key id/alias used to encrypt the data store contents at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                kms_encryption_config_property = healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                    cmk_type="cmkType",
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a204f0ae0d6b5a9246c0ce66e5f12f0873c70941743ebe67b84b3bf96c81207a)
                check_type(argname="argument cmk_type", value=cmk_type, expected_type=type_hints["cmk_type"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cmk_type": cmk_type,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def cmk_type(self) -> builtins.str:
            '''The type of customer-managed-key(CMK) used for encryption.

            The two types of supported CMKs are customer owned CMKs and Amazon owned CMKs. For more information on CMK types, see `KmsEncryptionConfig <https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html#HealthLake-Type-KmsEncryptionConfig-CmkType>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype
            '''
            result = self._values.get("cmk_type")
            assert result is not None, "Required property 'cmk_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The Key Management Service (KMS) encryption key id/alias used to encrypt the data store contents at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KmsEncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.PreloadDataConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"preload_data_type": "preloadDataType"},
    )
    class PreloadDataConfigProperty:
        def __init__(self, *, preload_data_type: builtins.str) -> None:
            '''An optional parameter to preload (import) open source Synthea FHIR data upon creation of the data store.

            :param preload_data_type: The type of preloaded data. Only Synthea preloaded data is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                preload_data_config_property = healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                    preload_data_type="preloadDataType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2807add39d82212bb123d916748097e974e9ff969a2403ee51221376730abb77)
                check_type(argname="argument preload_data_type", value=preload_data_type, expected_type=type_hints["preload_data_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "preload_data_type": preload_data_type,
            }

        @builtins.property
        def preload_data_type(self) -> builtins.str:
            '''The type of preloaded data.

            Only Synthea preloaded data is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html#cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype
            '''
            result = self._values.get("preload_data_type")
            assert result is not None, "Required property 'preload_data_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PreloadDataConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.SseConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_encryption_config": "kmsEncryptionConfig"},
    )
    class SseConfigurationProperty:
        def __init__(
            self,
            *,
            kms_encryption_config: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFHIRDatastore.KmsEncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The server-side encryption key configuration for a customer-provided encryption key.

            :param kms_encryption_config: The server-side encryption key configuration for a customer provided encryption key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                sse_configuration_property = healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                    kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                        cmk_type="cmkType",
                
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ddeddf28afa132e70cf3cdeca1b03ad8c2e5de2f7786f5db94037eb39e61032d)
                check_type(argname="argument kms_encryption_config", value=kms_encryption_config, expected_type=type_hints["kms_encryption_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kms_encryption_config": kms_encryption_config,
            }

        @builtins.property
        def kms_encryption_config(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.KmsEncryptionConfigProperty"]:
            '''The server-side encryption key configuration for a customer provided encryption key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html#cfn-healthlake-fhirdatastore-sseconfiguration-kmsencryptionconfig
            '''
            result = self._values.get("kms_encryption_config")
            assert result is not None, "Required property 'kms_encryption_config' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.KmsEncryptionConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "datastore_type_version": "datastoreTypeVersion",
        "datastore_name": "datastoreName",
        "identity_provider_configuration": "identityProviderConfiguration",
        "preload_data_config": "preloadDataConfig",
        "sse_configuration": "sseConfiguration",
        "tags": "tags",
    },
)
class CfnFHIRDatastoreProps:
    def __init__(
        self,
        *,
        datastore_type_version: builtins.str,
        datastore_name: typing.Optional[builtins.str] = None,
        identity_provider_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFHIRDatastore.IdentityProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        preload_data_config: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFHIRDatastore.PreloadDataConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFHIRDatastore.SseConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFHIRDatastore``.

        :param datastore_type_version: The FHIR release version supported by the data store. Current support is for version ``R4`` .
        :param datastore_name: The data store name (user-generated).
        :param identity_provider_configuration: The identity provider configuration selected when the data store was created.
        :param preload_data_config: The preloaded Synthea data configuration for the data store.
        :param sse_configuration: The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_healthlake as healthlake
            
            cfn_fhir_datastore_props = healthlake.CfnFHIRDatastoreProps(
                datastore_type_version="datastoreTypeVersion",
            
                # the properties below are optional
                datastore_name="datastoreName",
                identity_provider_configuration=healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty(
                    authorization_strategy="authorizationStrategy",
            
                    # the properties below are optional
                    fine_grained_authorization_enabled=False,
                    idp_lambda_arn="idpLambdaArn",
                    metadata="metadata"
                ),
                preload_data_config=healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                    preload_data_type="preloadDataType"
                ),
                sse_configuration=healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                    kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                        cmk_type="cmkType",
            
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0f7e172077b0d6f3f4825d2eeb030b9523f0239350078a907c09cabc7ce33420)
            check_type(argname="argument datastore_type_version", value=datastore_type_version, expected_type=type_hints["datastore_type_version"])
            check_type(argname="argument datastore_name", value=datastore_name, expected_type=type_hints["datastore_name"])
            check_type(argname="argument identity_provider_configuration", value=identity_provider_configuration, expected_type=type_hints["identity_provider_configuration"])
            check_type(argname="argument preload_data_config", value=preload_data_config, expected_type=type_hints["preload_data_config"])
            check_type(argname="argument sse_configuration", value=sse_configuration, expected_type=type_hints["sse_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datastore_type_version": datastore_type_version,
        }
        if datastore_name is not None:
            self._values["datastore_name"] = datastore_name
        if identity_provider_configuration is not None:
            self._values["identity_provider_configuration"] = identity_provider_configuration
        if preload_data_config is not None:
            self._values["preload_data_config"] = preload_data_config
        if sse_configuration is not None:
            self._values["sse_configuration"] = sse_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def datastore_type_version(self) -> builtins.str:
        '''The FHIR release version supported by the data store.

        Current support is for version ``R4`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastoretypeversion
        '''
        result = self._values.get("datastore_type_version")
        assert result is not None, "Required property 'datastore_type_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''The data store name (user-generated).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastorename
        '''
        result = self._values.get("datastore_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.IdentityProviderConfigurationProperty"]]:
        '''The identity provider configuration selected when the data store was created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration
        '''
        result = self._values.get("identity_provider_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.IdentityProviderConfigurationProperty"]], result)

    @builtins.property
    def preload_data_config(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.PreloadDataConfigProperty"]]:
        '''The preloaded Synthea data configuration for the data store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-preloaddataconfig
        '''
        result = self._values.get("preload_data_config")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.PreloadDataConfigProperty"]], result)

    @builtins.property
    def sse_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.SseConfigurationProperty"]]:
        '''The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-sseconfiguration
        '''
        result = self._values.get("sse_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFHIRDatastore.SseConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFHIRDatastoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataTransformationProfile",
    "CfnDataTransformationProfileProps",
    "CfnFHIRDatastore",
    "CfnFHIRDatastoreProps",
]

publication.publish()

def _typecheckingstub__ffa7f40a55c908b5c71d8b021cb4bc5def1f3d33e73427064b902fe2f00f5cd5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    profile_name: builtins.str,
    source_format: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
    profile_description: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataTransformationProfile.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba9ba7186101ad3636b33a3380dbbf50e17791493b400773d1f51dac14d23ddc(
    resource: _aws_healthlake_d03fc20c.IDataTransformationProfileRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d96bb697a4df81a1f6f068354d53364d470246af42304fec6d76824cebd19fb1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17fe2cefd9247d79f84504fd1bb7c4dd592b3257d789e6bf240e7b6b533763f8(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91abd016be8ce2f2a2a6f50f134f4bbfa65013218ced141348e8e50dad36f145(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ebc07ff74a99d99b611bf1ccdf04f15b0439f0941af32a0d3f29788ccd1b98e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c904204562f714f3203e7b9697e0b749faa45d018ec8fcf28958a8a8a99056(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0295dd98c6aed49aaf7df89c6d4a3e2ff56e0dbaa8ec41340be48fd349e4b54(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07be715f497b62f1ea6f103ef6fea6b01a1c3265134bef46ef3a2dbc49d2948b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0634fb098e12ecb4f06c1a886cb10ec45fdc1789d44fbefa8babca15e9440cb4(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnDataTransformationProfile.SourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcd46233cb0eecf58baa705df6c53ad8c03fa75cd42a5011e9e49f0e82b0839a(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d021157bc45cc79c2c24f0227d22c35e4e523115d5be9d2677db6747bbb1b8(
    *,
    profile_id: builtins.str,
    version: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21589af684261b5e206ff0002a218cd1f07462e63c1dad79bbca931e75dbee5f(
    *,
    profile_mapping: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f6738e7624c37b9b0601248d91777f2bcadb7e16c0567df96df6b4c183ecaf0(
    *,
    existing_versioned_profile_id: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataTransformationProfile.ExistingVersionedProfileSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile_mapping: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataTransformationProfile.ProfileMappingSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    starter_profile: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataTransformationProfile.StarterProfileSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b61a87dcbbda68f6695fa1aad8fd146ca983dcebd45fb4810fcda352a0c05ad(
    *,
    starter_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ec0f2eb8014f6283a9cedab74d21e354d4017d5caa09bc38c8c7e3338c2a49(
    *,
    profile_name: builtins.str,
    source_format: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
    profile_description: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnDataTransformationProfile.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a84066c5df4c48a34d687987d48edfe8b65e8bda26e4da5f30db9c938e54b90(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    datastore_type_version: builtins.str,
    datastore_name: typing.Optional[builtins.str] = None,
    identity_provider_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFHIRDatastore.IdentityProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    preload_data_config: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFHIRDatastore.SseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f0cb1aa981e44d9252c4ccb23e5e4300e3380368e5dead8a05fb5dd9f413b00(
    resource: _aws_healthlake_d03fc20c.IFHIRDatastoreRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aca17223f33eab4c3c32fe59502f6e15af4d519ea58e4d602d2408ce0b1dfa4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    datastore_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb13a8ddb4107ab5128d62b9ccef2aef1a010a8f819b0cbe0bd1abf0438e0d22(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67828597c6b23eb59e180c8c9477691634e8d3539e804a608e5af42e84fe8bc8(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9041dc50c8109815f2c8dd04e804c6471002a65ab5f8f21a4695f6a237e3703(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c34e70b6ec2df3b888529b3c31e66d8c6bede9b01bd8e9f59661918d44ba4f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5808500ce498cbcd60021c25c05f2f5ec6982551bc42bc79b3964a61257718e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3d86ac6fd32fffececf8454df94145383c2e779b9b5f1a30896102278cd1a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__612b8cf4bba44e8e4744db8a7c2eaefe0b9bd601172c067d2c5a9feeb75cb14f(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnFHIRDatastore.IdentityProviderConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b4d362bc0e9c9065e9f83741b0f46cfc52f253212d6a4551c7a2d9e4fd7e630(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnFHIRDatastore.PreloadDataConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d21d284c17f3b1e178b27b28fe912e0eaebeaa7ca9612eff81512c42f71c29d2(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnFHIRDatastore.SseConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ffa2ce0bad1140b8ffa060738f5e180bc7033b7f2e9f274ce2d1d871b5d620(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__914232fa94e4874b18f9fa312fe19be92103d3c527212c1cc7038dd05916c72f(
    *,
    nanos: jsii.Number,
    seconds: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f028d556a7a738b78a7fbfb130c7243f69ba20b6367ea5c21f2e6bcc60445fb(
    *,
    authorization_strategy: builtins.str,
    fine_grained_authorization_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    idp_lambda_arn: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a204f0ae0d6b5a9246c0ce66e5f12f0873c70941743ebe67b84b3bf96c81207a(
    *,
    cmk_type: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2807add39d82212bb123d916748097e974e9ff969a2403ee51221376730abb77(
    *,
    preload_data_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddeddf28afa132e70cf3cdeca1b03ad8c2e5de2f7786f5db94037eb39e61032d(
    *,
    kms_encryption_config: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFHIRDatastore.KmsEncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f7e172077b0d6f3f4825d2eeb030b9523f0239350078a907c09cabc7ce33420(
    *,
    datastore_type_version: builtins.str,
    datastore_name: typing.Optional[builtins.str] = None,
    identity_provider_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFHIRDatastore.IdentityProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    preload_data_config: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFHIRDatastore.SseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
