r'''
# AWS::EMRContainers Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_emrcontainers as emrcontainers
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EMRContainers construct libraries](https://constructs.dev/search?q=emrcontainers)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EMRContainers resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRContainers.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EMRContainers](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRContainers.html).

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
    import aws_cdk.interfaces.aws_emrcontainers as _aws_emrcontainers_6ec331d9
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_emrcontainers_6ec331d9 = _LazyImport("aws_cdk.interfaces.aws_emrcontainers")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_emrcontainers_6ec331d9.IEndpointRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnEndpoint(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint",
):
    '''Resource Schema of AWS::EMRContainers::Endpoint Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html
    :cloudformationResource: AWS::EMRContainers::Endpoint
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrcontainers as emrcontainers
        
        # e_mreks_configuration_property_: emrcontainers.CfnEndpoint.EMREKSConfigurationProperty
        
        cfn_endpoint = emrcontainers.CfnEndpoint(self, "MyCfnEndpoint",
            execution_role_arn="executionRoleArn",
            release_label="releaseLabel",
            type="type",
            virtual_cluster_id="virtualClusterId",
        
            # the properties below are optional
            configuration_overrides=emrcontainers.CfnEndpoint.ConfigurationOverridesProperty(
                application_configuration=[emrcontainers.CfnEndpoint.EMREKSConfigurationProperty(
                    classification="classification",
        
                    # the properties below are optional
                    configurations=[e_mreks_configuration_property_],
                    properties={
                        "properties_key": "properties"
                    }
                )],
                monitoring_configuration=emrcontainers.CfnEndpoint.MonitoringConfigurationProperty(
                    cloud_watch_monitoring_configuration=emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                        log_group_name="logGroupName",
        
                        # the properties below are optional
                        log_stream_name_prefix="logStreamNamePrefix"
                    ),
                    container_log_rotation_configuration=emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                        max_files_to_keep=123,
                        rotation_size="rotationSize"
                    ),
                    persistent_app_ui="persistentAppUi",
                    s3_monitoring_configuration=emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                        log_uri="logUri"
                    )
                )
            ),
            name="name",
            session_idle_timeout_in_minutes=123,
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
        execution_role_arn: builtins.str,
        release_label: builtins.str,
        type: builtins.str,
        virtual_cluster_id: builtins.str,
        configuration_overrides: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEndpoint.ConfigurationOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        session_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::Endpoint``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param execution_role_arn: The execution role ARN for the managed endpoint.
        :param release_label: The Amazon EMR release label.
        :param type: The type of the managed endpoint.
        :param virtual_cluster_id: The ID of the virtual cluster for which the managed endpoint is created.
        :param configuration_overrides: 
        :param name: The name of the managed endpoint.
        :param session_idle_timeout_in_minutes: The idle timeout in minutes for sessions on the managed endpoint.
        :param tags: An array of key-value pairs to apply to this managed endpoint.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__23b89c74ef5fd6a5347927e915b67a755f92f55810673773d86745b94ec9ce0c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointProps(
            execution_role_arn=execution_role_arn,
            release_label=release_label,
            type=type,
            virtual_cluster_id=virtual_cluster_id,
            configuration_overrides=configuration_overrides,
            name=name,
            session_idle_timeout_in_minutes=session_idle_timeout_in_minutes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForEndpoint")
    @builtins.classmethod
    def arn_for_endpoint(
        cls,
        resource: "_aws_emrcontainers_6ec331d9.IEndpointRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4d0893eaff59c12b7e6dd4dfd799d44a31fa49362dec8ba203c7f8e79029bff9)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForEndpoint", [resource]))

    @jsii.member(jsii_name="isCfnEndpoint")
    @builtins.classmethod
    def is_cfn_endpoint(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnEndpoint.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__635096970c8f6988b319790d01d10b7af1624a2bd87a8fd19d2f526067565d38)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnEndpoint", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4f81524f5f031b60202ef5750c9c53a9e8e5e0357685aef97a068e09c19a1d5d)
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
            type_hints = cached_type_hints(_typecheckingstub__22395c6c2f1b0a694a9e0faf2c896173a496cbdf51ca26ecd7214a44487b981e)
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
        '''The ARN of the managed endpoint.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAuthProxyUrl")
    def attr_auth_proxy_url(self) -> builtins.str:
        '''The auth proxy URL for Spark Connect connections.

        :cloudformationAttribute: AuthProxyUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAuthProxyUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrCertificateAuthority")
    def attr_certificate_authority(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''
        :cloudformationAttribute: CertificateAuthority
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrCertificateAuthority"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time when the managed endpoint was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for a failed managed endpoint.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the managed endpoint.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSecurityGroup")
    def attr_security_group(self) -> builtins.str:
        '''The security group associated with the managed endpoint.

        :cloudformationAttribute: SecurityGroup
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSecurityGroup"))

    @builtins.property
    @jsii.member(jsii_name="attrServerUrl")
    def attr_server_url(self) -> builtins.str:
        '''The server URL of the managed endpoint.

        :cloudformationAttribute: ServerUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the managed endpoint.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrStateDetails")
    def attr_state_details(self) -> builtins.str:
        '''Additional details about the state of the managed endpoint.

        :cloudformationAttribute: StateDetails
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateDetails"))

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
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "_aws_emrcontainers_6ec331d9.EndpointReference":
        '''A reference to a Endpoint resource.'''
        return typing.cast("_aws_emrcontainers_6ec331d9.EndpointReference", jsii.get(self, "endpointRef"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        '''The execution role ARN for the managed endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__82adad35327e5af1f867ea3ce6b09d9cf8bf066d4f3f0c3a297e3425583291ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> builtins.str:
        '''The Amazon EMR release label.'''
        return typing.cast(builtins.str, jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2fdfe64e097ccd04046eb25d75f28e5f90eca1ce0eda856ca0f77cf38cdb414e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the managed endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5e3365f1d0529739a9e96ac4af19a8abe17480deaa11498dbba4db6c1eb52a61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="virtualClusterId")
    def virtual_cluster_id(self) -> builtins.str:
        '''The ID of the virtual cluster for which the managed endpoint is created.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualClusterId"))

    @virtual_cluster_id.setter
    def virtual_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0b0a84d01612790328a1ecc8558a579f74f52fa1a781ed7197676c50fce5a6e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualClusterId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configurationOverrides")
    def configuration_overrides(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.ConfigurationOverridesProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.ConfigurationOverridesProperty"]], jsii.get(self, "configurationOverrides"))

    @configuration_overrides.setter
    def configuration_overrides(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.ConfigurationOverridesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7e0c8197e58a0f1f00521e2589c5fe3688295bc923b51b75d41f29f6aec64d3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationOverrides", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the managed endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2ff6a672ee7bf784cfbde2614d2f6cae307ce23728014e1a8bb6736b2020c7c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sessionIdleTimeoutInMinutes")
    def session_idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The idle timeout in minutes for sessions on the managed endpoint.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionIdleTimeoutInMinutes"))

    @session_idle_timeout_in_minutes.setter
    def session_idle_timeout_in_minutes(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e130186ac0641d5db5870b89171b366bc2c58acd32460ae6419a099b3796f5a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionIdleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this managed endpoint.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ea06eef637e8c0a25b829a6c624ac3e00fd1f47e5a0dc21e18b827b60481aa0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.CertificateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "certificate_data": "certificateData",
        },
    )
    class CertificateProperty:
        def __init__(
            self,
            *,
            certificate_arn: typing.Optional[builtins.str] = None,
            certificate_data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param certificate_arn: 
            :param certificate_data: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-certificate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                certificate_property = emrcontainers.CfnEndpoint.CertificateProperty(
                    certificate_arn="certificateArn",
                    certificate_data="certificateData"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0753442657548325e3bd0a9ec7c567fdf41626466b3e89bfed14dee1c6cec778)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument certificate_data", value=certificate_data, expected_type=type_hints["certificate_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_arn is not None:
                self._values["certificate_arn"] = certificate_arn
            if certificate_data is not None:
                self._values["certificate_data"] = certificate_data

        @builtins.property
        def certificate_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-certificate.html#cfn-emrcontainers-endpoint-certificate-certificatearn
            '''
            result = self._values.get("certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def certificate_data(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-certificate.html#cfn-emrcontainers-endpoint-certificate-certificatedata
            '''
            result = self._values.get("certificate_data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_group_name": "logGroupName",
            "log_stream_name_prefix": "logStreamNamePrefix",
        },
    )
    class CloudWatchMonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_name: builtins.str,
            log_stream_name_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group_name: 
            :param log_stream_name_prefix: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                cloud_watch_monitoring_configuration_property = emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                    log_group_name="logGroupName",
                
                    # the properties below are optional
                    log_stream_name_prefix="logStreamNamePrefix"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8ecb22ba4d8b0faedcb5f445667dd4c14b1bb238ebfc25811866bc27bb2f9f29)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_stream_name_prefix", value=log_stream_name_prefix, expected_type=type_hints["log_stream_name_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_name": log_group_name,
            }
            if log_stream_name_prefix is not None:
                self._values["log_stream_name_prefix"] = log_stream_name_prefix

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration.html#cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_stream_name_prefix(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration.html#cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-logstreamnameprefix
            '''
            result = self._values.get("log_stream_name_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchMonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.ConfigurationOverridesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_configuration": "applicationConfiguration",
            "monitoring_configuration": "monitoringConfiguration",
        },
    )
    class ConfigurationOverridesProperty:
        def __init__(
            self,
            *,
            application_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEndpoint.EMREKSConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            monitoring_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEndpoint.MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param application_configuration: 
            :param monitoring_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-configurationoverrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                # e_mreks_configuration_property_: emrcontainers.CfnEndpoint.EMREKSConfigurationProperty
                
                configuration_overrides_property = emrcontainers.CfnEndpoint.ConfigurationOverridesProperty(
                    application_configuration=[emrcontainers.CfnEndpoint.EMREKSConfigurationProperty(
                        classification="classification",
                
                        # the properties below are optional
                        configurations=[e_mreks_configuration_property_],
                        properties={
                            "properties_key": "properties"
                        }
                    )],
                    monitoring_configuration=emrcontainers.CfnEndpoint.MonitoringConfigurationProperty(
                        cloud_watch_monitoring_configuration=emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                            log_group_name="logGroupName",
                
                            # the properties below are optional
                            log_stream_name_prefix="logStreamNamePrefix"
                        ),
                        container_log_rotation_configuration=emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                            max_files_to_keep=123,
                            rotation_size="rotationSize"
                        ),
                        persistent_app_ui="persistentAppUi",
                        s3_monitoring_configuration=emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                            log_uri="logUri"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__46f984090360c20eea47211457bc59ba0064e851b8407461cf578437814aeb01)
                check_type(argname="argument application_configuration", value=application_configuration, expected_type=type_hints["application_configuration"])
                check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_configuration is not None:
                self._values["application_configuration"] = application_configuration
            if monitoring_configuration is not None:
                self._values["monitoring_configuration"] = monitoring_configuration

        @builtins.property
        def application_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.EMREKSConfigurationProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-configurationoverrides.html#cfn-emrcontainers-endpoint-configurationoverrides-applicationconfiguration
            '''
            result = self._values.get("application_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.EMREKSConfigurationProperty"]]]], result)

        @builtins.property
        def monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.MonitoringConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-configurationoverrides.html#cfn-emrcontainers-endpoint-configurationoverrides-monitoringconfiguration
            '''
            result = self._values.get("monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.MonitoringConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationOverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_files_to_keep": "maxFilesToKeep",
            "rotation_size": "rotationSize",
        },
    )
    class ContainerLogRotationConfigurationProperty:
        def __init__(
            self,
            *,
            max_files_to_keep: jsii.Number,
            rotation_size: builtins.str,
        ) -> None:
            '''
            :param max_files_to_keep: 
            :param rotation_size: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-containerlogrotationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_log_rotation_configuration_property = emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                    max_files_to_keep=123,
                    rotation_size="rotationSize"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__817b097d9818e8dbd56314bb022a526176ef9e0a159ab0fbb93fd2ba36f723a2)
                check_type(argname="argument max_files_to_keep", value=max_files_to_keep, expected_type=type_hints["max_files_to_keep"])
                check_type(argname="argument rotation_size", value=rotation_size, expected_type=type_hints["rotation_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_files_to_keep": max_files_to_keep,
                "rotation_size": rotation_size,
            }

        @builtins.property
        def max_files_to_keep(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-containerlogrotationconfiguration.html#cfn-emrcontainers-endpoint-containerlogrotationconfiguration-maxfilestokeep
            '''
            result = self._values.get("max_files_to_keep")
            assert result is not None, "Required property 'max_files_to_keep' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rotation_size(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-containerlogrotationconfiguration.html#cfn-emrcontainers-endpoint-containerlogrotationconfiguration-rotationsize
            '''
            result = self._values.get("rotation_size")
            assert result is not None, "Required property 'rotation_size' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerLogRotationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.EMREKSConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configurations": "configurations",
            "properties": "properties",
        },
    )
    class EMREKSConfigurationProperty:
        def __init__(
            self,
            *,
            classification: builtins.str,
            configurations: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEndpoint.EMREKSConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            properties: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''
            :param classification: 
            :param configurations: 
            :param properties: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-emreksconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                # e_mreks_configuration_property_: emrcontainers.CfnEndpoint.EMREKSConfigurationProperty
                
                e_mreks_configuration_property = emrcontainers.CfnEndpoint.EMREKSConfigurationProperty(
                    classification="classification",
                
                    # the properties below are optional
                    configurations=[e_mreks_configuration_property_],
                    properties={
                        "properties_key": "properties"
                    }
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a5e05064bc37ba71915107a21d96057346160606aa8cdc19d7293f9c9037b47a)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "classification": classification,
            }
            if configurations is not None:
                self._values["configurations"] = configurations
            if properties is not None:
                self._values["properties"] = properties

        @builtins.property
        def classification(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-emreksconfiguration.html#cfn-emrcontainers-endpoint-emreksconfiguration-classification
            '''
            result = self._values.get("classification")
            assert result is not None, "Required property 'classification' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.EMREKSConfigurationProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-emreksconfiguration.html#cfn-emrcontainers-endpoint-emreksconfiguration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.EMREKSConfigurationProperty"]]]], result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-emreksconfiguration.html#cfn-emrcontainers-endpoint-emreksconfiguration-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EMREKSConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_monitoring_configuration": "cloudWatchMonitoringConfiguration",
            "container_log_rotation_configuration": "containerLogRotationConfiguration",
            "persistent_app_ui": "persistentAppUi",
            "s3_monitoring_configuration": "s3MonitoringConfiguration",
        },
    )
    class MonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_monitoring_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEndpoint.CloudWatchMonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            container_log_rotation_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEndpoint.ContainerLogRotationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            persistent_app_ui: typing.Optional[builtins.str] = None,
            s3_monitoring_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEndpoint.S3MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param cloud_watch_monitoring_configuration: 
            :param container_log_rotation_configuration: 
            :param persistent_app_ui: 
            :param s3_monitoring_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                monitoring_configuration_property = emrcontainers.CfnEndpoint.MonitoringConfigurationProperty(
                    cloud_watch_monitoring_configuration=emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                        log_group_name="logGroupName",
                
                        # the properties below are optional
                        log_stream_name_prefix="logStreamNamePrefix"
                    ),
                    container_log_rotation_configuration=emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                        max_files_to_keep=123,
                        rotation_size="rotationSize"
                    ),
                    persistent_app_ui="persistentAppUi",
                    s3_monitoring_configuration=emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                        log_uri="logUri"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8a0503e26d3c8fcf0703183603081e1b7a18027a03a980ed33b0bb37c14dff86)
                check_type(argname="argument cloud_watch_monitoring_configuration", value=cloud_watch_monitoring_configuration, expected_type=type_hints["cloud_watch_monitoring_configuration"])
                check_type(argname="argument container_log_rotation_configuration", value=container_log_rotation_configuration, expected_type=type_hints["container_log_rotation_configuration"])
                check_type(argname="argument persistent_app_ui", value=persistent_app_ui, expected_type=type_hints["persistent_app_ui"])
                check_type(argname="argument s3_monitoring_configuration", value=s3_monitoring_configuration, expected_type=type_hints["s3_monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_monitoring_configuration is not None:
                self._values["cloud_watch_monitoring_configuration"] = cloud_watch_monitoring_configuration
            if container_log_rotation_configuration is not None:
                self._values["container_log_rotation_configuration"] = container_log_rotation_configuration
            if persistent_app_ui is not None:
                self._values["persistent_app_ui"] = persistent_app_ui
            if s3_monitoring_configuration is not None:
                self._values["s3_monitoring_configuration"] = s3_monitoring_configuration

        @builtins.property
        def cloud_watch_monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.CloudWatchMonitoringConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html#cfn-emrcontainers-endpoint-monitoringconfiguration-cloudwatchmonitoringconfiguration
            '''
            result = self._values.get("cloud_watch_monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.CloudWatchMonitoringConfigurationProperty"]], result)

        @builtins.property
        def container_log_rotation_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.ContainerLogRotationConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html#cfn-emrcontainers-endpoint-monitoringconfiguration-containerlogrotationconfiguration
            '''
            result = self._values.get("container_log_rotation_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.ContainerLogRotationConfigurationProperty"]], result)

        @builtins.property
        def persistent_app_ui(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html#cfn-emrcontainers-endpoint-monitoringconfiguration-persistentappui
            '''
            result = self._values.get("persistent_app_ui")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.S3MonitoringConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html#cfn-emrcontainers-endpoint-monitoringconfiguration-s3monitoringconfiguration
            '''
            result = self._values.get("s3_monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.S3MonitoringConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_uri": "logUri"},
    )
    class S3MonitoringConfigurationProperty:
        def __init__(self, *, log_uri: builtins.str) -> None:
            '''
            :param log_uri: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-s3monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                s3_monitoring_configuration_property = emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                    log_uri="logUri"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d2e089a4b5c6bf3faf983bfe03d5042364c4f68c554cd62834b53e7101c615e6)
                check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_uri": log_uri,
            }

        @builtins.property
        def log_uri(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-s3monitoringconfiguration.html#cfn-emrcontainers-endpoint-s3monitoringconfiguration-loguri
            '''
            result = self._values.get("log_uri")
            assert result is not None, "Required property 'log_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role_arn": "executionRoleArn",
        "release_label": "releaseLabel",
        "type": "type",
        "virtual_cluster_id": "virtualClusterId",
        "configuration_overrides": "configurationOverrides",
        "name": "name",
        "session_idle_timeout_in_minutes": "sessionIdleTimeoutInMinutes",
        "tags": "tags",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        execution_role_arn: builtins.str,
        release_label: builtins.str,
        type: builtins.str,
        virtual_cluster_id: builtins.str,
        configuration_overrides: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnEndpoint.ConfigurationOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        session_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpoint``.

        :param execution_role_arn: The execution role ARN for the managed endpoint.
        :param release_label: The Amazon EMR release label.
        :param type: The type of the managed endpoint.
        :param virtual_cluster_id: The ID of the virtual cluster for which the managed endpoint is created.
        :param configuration_overrides: 
        :param name: The name of the managed endpoint.
        :param session_idle_timeout_in_minutes: The idle timeout in minutes for sessions on the managed endpoint.
        :param tags: An array of key-value pairs to apply to this managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrcontainers as emrcontainers
            
            # e_mreks_configuration_property_: emrcontainers.CfnEndpoint.EMREKSConfigurationProperty
            
            cfn_endpoint_props = emrcontainers.CfnEndpointProps(
                execution_role_arn="executionRoleArn",
                release_label="releaseLabel",
                type="type",
                virtual_cluster_id="virtualClusterId",
            
                # the properties below are optional
                configuration_overrides=emrcontainers.CfnEndpoint.ConfigurationOverridesProperty(
                    application_configuration=[emrcontainers.CfnEndpoint.EMREKSConfigurationProperty(
                        classification="classification",
            
                        # the properties below are optional
                        configurations=[e_mreks_configuration_property_],
                        properties={
                            "properties_key": "properties"
                        }
                    )],
                    monitoring_configuration=emrcontainers.CfnEndpoint.MonitoringConfigurationProperty(
                        cloud_watch_monitoring_configuration=emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                            log_group_name="logGroupName",
            
                            # the properties below are optional
                            log_stream_name_prefix="logStreamNamePrefix"
                        ),
                        container_log_rotation_configuration=emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                            max_files_to_keep=123,
                            rotation_size="rotationSize"
                        ),
                        persistent_app_ui="persistentAppUi",
                        s3_monitoring_configuration=emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                            log_uri="logUri"
                        )
                    )
                ),
                name="name",
                session_idle_timeout_in_minutes=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cdf3149ecf1698607ceb24e9bbca6c307d3e7ef064cb79d95651abb2c6d47065)
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument virtual_cluster_id", value=virtual_cluster_id, expected_type=type_hints["virtual_cluster_id"])
            check_type(argname="argument configuration_overrides", value=configuration_overrides, expected_type=type_hints["configuration_overrides"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument session_idle_timeout_in_minutes", value=session_idle_timeout_in_minutes, expected_type=type_hints["session_idle_timeout_in_minutes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "execution_role_arn": execution_role_arn,
            "release_label": release_label,
            "type": type,
            "virtual_cluster_id": virtual_cluster_id,
        }
        if configuration_overrides is not None:
            self._values["configuration_overrides"] = configuration_overrides
        if name is not None:
            self._values["name"] = name
        if session_idle_timeout_in_minutes is not None:
            self._values["session_idle_timeout_in_minutes"] = session_idle_timeout_in_minutes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''The execution role ARN for the managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def release_label(self) -> builtins.str:
        '''The Amazon EMR release label.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-releaselabel
        '''
        result = self._values.get("release_label")
        assert result is not None, "Required property 'release_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_cluster_id(self) -> builtins.str:
        '''The ID of the virtual cluster for which the managed endpoint is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-virtualclusterid
        '''
        result = self._values.get("virtual_cluster_id")
        assert result is not None, "Required property 'virtual_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_overrides(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.ConfigurationOverridesProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-configurationoverrides
        '''
        result = self._values.get("configuration_overrides")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnEndpoint.ConfigurationOverridesProperty"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The idle timeout in minutes for sessions on the managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-sessionidletimeoutinminutes
        '''
        result = self._values.get("session_idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_emrcontainers_6ec331d9.IJobTemplateRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnJobTemplate(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate",
):
    '''Represents an Amazon EMR on EKS job template.

    A job template stores the values of a StartJobRun API request in a reusable template, so they can be used to start a job run or to enforce certain values in a StartJobRun API request.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-jobtemplate.html
    :cloudformationResource: AWS::EMRContainers::JobTemplate
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrcontainers as emrcontainers
        
        # configuration_property_: emrcontainers.CfnJobTemplate.ConfigurationProperty
        
        cfn_job_template = emrcontainers.CfnJobTemplate(self, "MyCfnJobTemplate",
            job_template_data=emrcontainers.CfnJobTemplate.JobTemplateDataProperty(
                execution_role_arn="executionRoleArn",
                job_driver=emrcontainers.CfnJobTemplate.JobDriverProperty(
                    spark_sql_job_driver=emrcontainers.CfnJobTemplate.SparkSqlJobDriverProperty(
                        entry_point="entryPoint",
                        spark_sql_parameters="sparkSqlParameters"
                    ),
                    spark_submit_job_driver=emrcontainers.CfnJobTemplate.SparkSubmitJobDriverProperty(
                        entry_point="entryPoint",
        
                        # the properties below are optional
                        entry_point_arguments=["entryPointArguments"],
                        spark_submit_parameters="sparkSubmitParameters"
                    )
                ),
                release_label="releaseLabel",
        
                # the properties below are optional
                configuration_overrides=emrcontainers.CfnJobTemplate.ParametricConfigurationOverridesProperty(
                    application_configuration=[emrcontainers.CfnJobTemplate.ConfigurationProperty(
                        classification="classification",
        
                        # the properties below are optional
                        configurations=[configuration_property_],
                        properties={
                            "properties_key": "properties"
                        }
                    )],
                    monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricMonitoringConfigurationProperty(
                        cloud_watch_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty(
                            log_group_name="logGroupName",
                            log_stream_name_prefix="logStreamNamePrefix"
                        ),
                        persistent_app_ui="persistentAppUi",
                        s3_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricS3MonitoringConfigurationProperty(
                            log_uri="logUri"
                        )
                    )
                ),
                job_tags={
                    "job_tags_key": "jobTags"
                },
                parameter_configuration={
                    "parameter_configuration_key": emrcontainers.CfnJobTemplate.TemplateParameterConfigurationProperty(
                        default_value="defaultValue",
                        type="type"
                    )
                }
            ),
            name="name",
        
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
        job_template_data: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.JobTemplateDataProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::JobTemplate``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param job_template_data: The values of a StartJobRun API request used in job runs started using the job template.
        :param name: The specified name of the job template.
        :param tags: The tags that are associated with the job template.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f6c029a2e31e8024de8be1d7d6cc3164b0c4d242cdaa1e78e8152aa39ef297d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobTemplateProps(
            job_template_data=job_template_data, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForJobTemplate")
    @builtins.classmethod
    def arn_for_job_template(
        cls,
        resource: "_aws_emrcontainers_6ec331d9.IJobTemplateRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d1213684e48ba2ff226bf53a018eb8e22032bf66dc3b8fe2f7726727ccfaf17c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForJobTemplate", [resource]))

    @jsii.member(jsii_name="isCfnJobTemplate")
    @builtins.classmethod
    def is_cfn_job_template(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnJobTemplate.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ef61bbeea56cb835cf288985902b03d2ce3397c18d79451812a3afabe72d771b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnJobTemplate", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5fac5ed807f28c92b34b59474a24387d74ed0a6c77074e3e4da0476148fe5b99)
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
            type_hints = cached_type_hints(_typecheckingstub__0561a43529d97a11acf97d0c2115c911dc5c3e4e3abbbf8b3457e4d218c1a8e5)
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
        '''The ARN of the job template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time when the job template was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The user who created the job template.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the job template.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="jobTemplateRef")
    def job_template_ref(self) -> "_aws_emrcontainers_6ec331d9.JobTemplateReference":
        '''A reference to a JobTemplate resource.'''
        return typing.cast("_aws_emrcontainers_6ec331d9.JobTemplateReference", jsii.get(self, "jobTemplateRef"))

    @builtins.property
    @jsii.member(jsii_name="jobTemplateData")
    def job_template_data(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.JobTemplateDataProperty"]:
        '''The values of a StartJobRun API request used in job runs started using the job template.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.JobTemplateDataProperty"], jsii.get(self, "jobTemplateData"))

    @job_template_data.setter
    def job_template_data(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.JobTemplateDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__32317f0a78421d5632e7bc6574dda9ffbfcb0256a5946e6ee690d70dac4c3356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobTemplateData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The specified name of the job template.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7b7c793a65240af6e7ad92176cb6a473c8e8c548c0a0023cd5ae280287fcf21f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags that are associated with the job template.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__56b41299b65ce9b702f45b330d4070751ff8c0770b49288ef2e475935df515b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configurations": "configurations",
            "properties": "properties",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            classification: builtins.str,
            configurations: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            properties: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''A configuration specification to be used when provisioning virtual clusters, which can include configurations for applications and software bundled with Amazon EMR on EKS.

            :param classification: The classification within a configuration.
            :param configurations: 
            :param properties: A set of properties specified within a configuration classification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                # configuration_property_: emrcontainers.CfnJobTemplate.ConfigurationProperty
                
                configuration_property = emrcontainers.CfnJobTemplate.ConfigurationProperty(
                    classification="classification",
                
                    # the properties below are optional
                    configurations=[configuration_property_],
                    properties={
                        "properties_key": "properties"
                    }
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__b22b73396a3e46a6548256a211ad34a4fca6efd9179dc495c01be7ffb9a11862)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "classification": classification,
            }
            if configurations is not None:
                self._values["configurations"] = configurations
            if properties is not None:
                self._values["properties"] = properties

        @builtins.property
        def classification(self) -> builtins.str:
            '''The classification within a configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-configuration.html#cfn-emrcontainers-jobtemplate-configuration-classification
            '''
            result = self._values.get("classification")
            assert result is not None, "Required property 'classification' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ConfigurationProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-configuration.html#cfn-emrcontainers-jobtemplate-configuration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ConfigurationProperty"]]]], result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''A set of properties specified within a configuration classification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-configuration.html#cfn-emrcontainers-jobtemplate-configuration-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.JobDriverProperty",
        jsii_struct_bases=[],
        name_mapping={
            "spark_sql_job_driver": "sparkSqlJobDriver",
            "spark_submit_job_driver": "sparkSubmitJobDriver",
        },
    )
    class JobDriverProperty:
        def __init__(
            self,
            *,
            spark_sql_job_driver: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.SparkSqlJobDriverProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            spark_submit_job_driver: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.SparkSubmitJobDriverProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specify the driver that the job runs on.

            Exactly one of the two available job drivers is required, either SparkSqlJobDriver or SparkSubmitJobDriver.

            :param spark_sql_job_driver: The job driver for job type.
            :param spark_submit_job_driver: The information about job driver for Spark submit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobdriver.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                job_driver_property = emrcontainers.CfnJobTemplate.JobDriverProperty(
                    spark_sql_job_driver=emrcontainers.CfnJobTemplate.SparkSqlJobDriverProperty(
                        entry_point="entryPoint",
                        spark_sql_parameters="sparkSqlParameters"
                    ),
                    spark_submit_job_driver=emrcontainers.CfnJobTemplate.SparkSubmitJobDriverProperty(
                        entry_point="entryPoint",
                
                        # the properties below are optional
                        entry_point_arguments=["entryPointArguments"],
                        spark_submit_parameters="sparkSubmitParameters"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__1c21790543c1028a1851da37b5b1f0984fe52d70bcf238cd7a5c62b7eede1793)
                check_type(argname="argument spark_sql_job_driver", value=spark_sql_job_driver, expected_type=type_hints["spark_sql_job_driver"])
                check_type(argname="argument spark_submit_job_driver", value=spark_submit_job_driver, expected_type=type_hints["spark_submit_job_driver"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if spark_sql_job_driver is not None:
                self._values["spark_sql_job_driver"] = spark_sql_job_driver
            if spark_submit_job_driver is not None:
                self._values["spark_submit_job_driver"] = spark_submit_job_driver

        @builtins.property
        def spark_sql_job_driver(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.SparkSqlJobDriverProperty"]]:
            '''The job driver for job type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobdriver.html#cfn-emrcontainers-jobtemplate-jobdriver-sparksqljobdriver
            '''
            result = self._values.get("spark_sql_job_driver")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.SparkSqlJobDriverProperty"]], result)

        @builtins.property
        def spark_submit_job_driver(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.SparkSubmitJobDriverProperty"]]:
            '''The information about job driver for Spark submit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobdriver.html#cfn-emrcontainers-jobtemplate-jobdriver-sparksubmitjobdriver
            '''
            result = self._values.get("spark_submit_job_driver")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.SparkSubmitJobDriverProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobDriverProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.JobTemplateDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_role_arn": "executionRoleArn",
            "job_driver": "jobDriver",
            "release_label": "releaseLabel",
            "configuration_overrides": "configurationOverrides",
            "job_tags": "jobTags",
            "parameter_configuration": "parameterConfiguration",
        },
    )
    class JobTemplateDataProperty:
        def __init__(
            self,
            *,
            execution_role_arn: builtins.str,
            job_driver: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.JobDriverProperty", typing.Dict[builtins.str, typing.Any]]],
            release_label: builtins.str,
            configuration_overrides: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.ParametricConfigurationOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            job_tags: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
            parameter_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.TemplateParameterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The values of a StartJobRun API request used in job runs started using the job template.

            :param execution_role_arn: The execution role ARN of the job run, or a template parameter reference.
            :param job_driver: Specify the driver that the job runs on. Exactly one of the two available job drivers is required, either SparkSqlJobDriver or SparkSubmitJobDriver.
            :param release_label: The release version of Amazon EMR, or a template parameter reference.
            :param configuration_overrides: A configuration specification to be used to override existing configurations. This data type allows job template parameters to be specified within.
            :param job_tags: The tags assigned to jobs started using the job template.
            :param parameter_configuration: The configuration of parameters existing in the job template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobtemplatedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                # configuration_property_: emrcontainers.CfnJobTemplate.ConfigurationProperty
                
                job_template_data_property = emrcontainers.CfnJobTemplate.JobTemplateDataProperty(
                    execution_role_arn="executionRoleArn",
                    job_driver=emrcontainers.CfnJobTemplate.JobDriverProperty(
                        spark_sql_job_driver=emrcontainers.CfnJobTemplate.SparkSqlJobDriverProperty(
                            entry_point="entryPoint",
                            spark_sql_parameters="sparkSqlParameters"
                        ),
                        spark_submit_job_driver=emrcontainers.CfnJobTemplate.SparkSubmitJobDriverProperty(
                            entry_point="entryPoint",
                
                            # the properties below are optional
                            entry_point_arguments=["entryPointArguments"],
                            spark_submit_parameters="sparkSubmitParameters"
                        )
                    ),
                    release_label="releaseLabel",
                
                    # the properties below are optional
                    configuration_overrides=emrcontainers.CfnJobTemplate.ParametricConfigurationOverridesProperty(
                        application_configuration=[emrcontainers.CfnJobTemplate.ConfigurationProperty(
                            classification="classification",
                
                            # the properties below are optional
                            configurations=[configuration_property_],
                            properties={
                                "properties_key": "properties"
                            }
                        )],
                        monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricMonitoringConfigurationProperty(
                            cloud_watch_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty(
                                log_group_name="logGroupName",
                                log_stream_name_prefix="logStreamNamePrefix"
                            ),
                            persistent_app_ui="persistentAppUi",
                            s3_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricS3MonitoringConfigurationProperty(
                                log_uri="logUri"
                            )
                        )
                    ),
                    job_tags={
                        "job_tags_key": "jobTags"
                    },
                    parameter_configuration={
                        "parameter_configuration_key": emrcontainers.CfnJobTemplate.TemplateParameterConfigurationProperty(
                            default_value="defaultValue",
                            type="type"
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__795c32821cadb799a4fb4fbfd3bdce984d0531111086ba2e4f67dfbf1c2428b4)
                check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
                check_type(argname="argument job_driver", value=job_driver, expected_type=type_hints["job_driver"])
                check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
                check_type(argname="argument configuration_overrides", value=configuration_overrides, expected_type=type_hints["configuration_overrides"])
                check_type(argname="argument job_tags", value=job_tags, expected_type=type_hints["job_tags"])
                check_type(argname="argument parameter_configuration", value=parameter_configuration, expected_type=type_hints["parameter_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "execution_role_arn": execution_role_arn,
                "job_driver": job_driver,
                "release_label": release_label,
            }
            if configuration_overrides is not None:
                self._values["configuration_overrides"] = configuration_overrides
            if job_tags is not None:
                self._values["job_tags"] = job_tags
            if parameter_configuration is not None:
                self._values["parameter_configuration"] = parameter_configuration

        @builtins.property
        def execution_role_arn(self) -> builtins.str:
            '''The execution role ARN of the job run, or a template parameter reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobtemplatedata.html#cfn-emrcontainers-jobtemplate-jobtemplatedata-executionrolearn
            '''
            result = self._values.get("execution_role_arn")
            assert result is not None, "Required property 'execution_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def job_driver(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.JobDriverProperty"]:
            '''Specify the driver that the job runs on.

            Exactly one of the two available job drivers is required, either SparkSqlJobDriver or SparkSubmitJobDriver.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobtemplatedata.html#cfn-emrcontainers-jobtemplate-jobtemplatedata-jobdriver
            '''
            result = self._values.get("job_driver")
            assert result is not None, "Required property 'job_driver' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.JobDriverProperty"], result)

        @builtins.property
        def release_label(self) -> builtins.str:
            '''The release version of Amazon EMR, or a template parameter reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobtemplatedata.html#cfn-emrcontainers-jobtemplate-jobtemplatedata-releaselabel
            '''
            result = self._values.get("release_label")
            assert result is not None, "Required property 'release_label' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def configuration_overrides(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ParametricConfigurationOverridesProperty"]]:
            '''A configuration specification to be used to override existing configurations.

            This data type allows job template parameters to be specified within.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobtemplatedata.html#cfn-emrcontainers-jobtemplate-jobtemplatedata-configurationoverrides
            '''
            result = self._values.get("configuration_overrides")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ParametricConfigurationOverridesProperty"]], result)

        @builtins.property
        def job_tags(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''The tags assigned to jobs started using the job template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobtemplatedata.html#cfn-emrcontainers-jobtemplate-jobtemplatedata-jobtags
            '''
            result = self._values.get("job_tags")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def parameter_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.TemplateParameterConfigurationProperty"]]]]:
            '''The configuration of parameters existing in the job template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-jobtemplatedata.html#cfn-emrcontainers-jobtemplate-jobtemplatedata-parameterconfiguration
            '''
            result = self._values.get("parameter_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.TemplateParameterConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobTemplateDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_group_name": "logGroupName",
            "log_stream_name_prefix": "logStreamNamePrefix",
        },
    )
    class ParametricCloudWatchMonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
            log_stream_name_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A configuration for CloudWatch monitoring.

            This data type allows job template parameters to be specified within.

            :param log_group_name: The name of the log group for log publishing, or a template parameter reference.
            :param log_stream_name_prefix: The specified name prefix for log streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                parametric_cloud_watch_monitoring_configuration_property = emrcontainers.CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty(
                    log_group_name="logGroupName",
                    log_stream_name_prefix="logStreamNamePrefix"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__c62e7a0a0f8bf638323db721f046500c4c5835ae9de13cc405a7ad3cdfe8a2c2)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_stream_name_prefix", value=log_stream_name_prefix, expected_type=type_hints["log_stream_name_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_stream_name_prefix is not None:
                self._values["log_stream_name_prefix"] = log_stream_name_prefix

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The name of the log group for log publishing, or a template parameter reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration.html#cfn-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_stream_name_prefix(self) -> typing.Optional[builtins.str]:
            '''The specified name prefix for log streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration.html#cfn-emrcontainers-jobtemplate-parametriccloudwatchmonitoringconfiguration-logstreamnameprefix
            '''
            result = self._values.get("log_stream_name_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametricCloudWatchMonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.ParametricConfigurationOverridesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_configuration": "applicationConfiguration",
            "monitoring_configuration": "monitoringConfiguration",
        },
    )
    class ParametricConfigurationOverridesProperty:
        def __init__(
            self,
            *,
            application_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            monitoring_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.ParametricMonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A configuration specification to be used to override existing configurations.

            This data type allows job template parameters to be specified within.

            :param application_configuration: 
            :param monitoring_configuration: Configuration setting for monitoring. This data type allows job template parameters to be specified within.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                # configuration_property_: emrcontainers.CfnJobTemplate.ConfigurationProperty
                
                parametric_configuration_overrides_property = emrcontainers.CfnJobTemplate.ParametricConfigurationOverridesProperty(
                    application_configuration=[emrcontainers.CfnJobTemplate.ConfigurationProperty(
                        classification="classification",
                
                        # the properties below are optional
                        configurations=[configuration_property_],
                        properties={
                            "properties_key": "properties"
                        }
                    )],
                    monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricMonitoringConfigurationProperty(
                        cloud_watch_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty(
                            log_group_name="logGroupName",
                            log_stream_name_prefix="logStreamNamePrefix"
                        ),
                        persistent_app_ui="persistentAppUi",
                        s3_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricS3MonitoringConfigurationProperty(
                            log_uri="logUri"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e1861b199e8dd763443b960028c0df4e34bb4f5294d46210e36d3637722fc7f4)
                check_type(argname="argument application_configuration", value=application_configuration, expected_type=type_hints["application_configuration"])
                check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_configuration is not None:
                self._values["application_configuration"] = application_configuration
            if monitoring_configuration is not None:
                self._values["monitoring_configuration"] = monitoring_configuration

        @builtins.property
        def application_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ConfigurationProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides.html#cfn-emrcontainers-jobtemplate-parametricconfigurationoverrides-applicationconfiguration
            '''
            result = self._values.get("application_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ConfigurationProperty"]]]], result)

        @builtins.property
        def monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ParametricMonitoringConfigurationProperty"]]:
            '''Configuration setting for monitoring.

            This data type allows job template parameters to be specified within.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides.html#cfn-emrcontainers-jobtemplate-parametricconfigurationoverrides-monitoringconfiguration
            '''
            result = self._values.get("monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ParametricMonitoringConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametricConfigurationOverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.ParametricMonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_monitoring_configuration": "cloudWatchMonitoringConfiguration",
            "persistent_app_ui": "persistentAppUi",
            "s3_monitoring_configuration": "s3MonitoringConfiguration",
        },
    )
    class ParametricMonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_monitoring_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            persistent_app_ui: typing.Optional[builtins.str] = None,
            s3_monitoring_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.ParametricS3MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration setting for monitoring.

            This data type allows job template parameters to be specified within.

            :param cloud_watch_monitoring_configuration: A configuration for CloudWatch monitoring. This data type allows job template parameters to be specified within.
            :param persistent_app_ui: Monitoring configurations for the persistent application UI, or a template parameter reference.
            :param s3_monitoring_configuration: Amazon S3 configuration for monitoring log publishing. This data type allows job template parameters to be specified within.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                parametric_monitoring_configuration_property = emrcontainers.CfnJobTemplate.ParametricMonitoringConfigurationProperty(
                    cloud_watch_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty(
                        log_group_name="logGroupName",
                        log_stream_name_prefix="logStreamNamePrefix"
                    ),
                    persistent_app_ui="persistentAppUi",
                    s3_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricS3MonitoringConfigurationProperty(
                        log_uri="logUri"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d3f8c8bf13509d313157c1a5d5cc47e5eaef673acbdcc737fbb4ab54c97f97e3)
                check_type(argname="argument cloud_watch_monitoring_configuration", value=cloud_watch_monitoring_configuration, expected_type=type_hints["cloud_watch_monitoring_configuration"])
                check_type(argname="argument persistent_app_ui", value=persistent_app_ui, expected_type=type_hints["persistent_app_ui"])
                check_type(argname="argument s3_monitoring_configuration", value=s3_monitoring_configuration, expected_type=type_hints["s3_monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_monitoring_configuration is not None:
                self._values["cloud_watch_monitoring_configuration"] = cloud_watch_monitoring_configuration
            if persistent_app_ui is not None:
                self._values["persistent_app_ui"] = persistent_app_ui
            if s3_monitoring_configuration is not None:
                self._values["s3_monitoring_configuration"] = s3_monitoring_configuration

        @builtins.property
        def cloud_watch_monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty"]]:
            '''A configuration for CloudWatch monitoring.

            This data type allows job template parameters to be specified within.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration.html#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-cloudwatchmonitoringconfiguration
            '''
            result = self._values.get("cloud_watch_monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty"]], result)

        @builtins.property
        def persistent_app_ui(self) -> typing.Optional[builtins.str]:
            '''Monitoring configurations for the persistent application UI, or a template parameter reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration.html#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-persistentappui
            '''
            result = self._values.get("persistent_app_ui")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ParametricS3MonitoringConfigurationProperty"]]:
            '''Amazon S3 configuration for monitoring log publishing.

            This data type allows job template parameters to be specified within.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametricmonitoringconfiguration.html#cfn-emrcontainers-jobtemplate-parametricmonitoringconfiguration-s3monitoringconfiguration
            '''
            result = self._values.get("s3_monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.ParametricS3MonitoringConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametricMonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.ParametricS3MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_uri": "logUri"},
    )
    class ParametricS3MonitoringConfigurationProperty:
        def __init__(self, *, log_uri: typing.Optional[builtins.str] = None) -> None:
            '''Amazon S3 configuration for monitoring log publishing.

            This data type allows job template parameters to be specified within.

            :param log_uri: Amazon S3 destination URI for log publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametrics3monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                parametric_s3_monitoring_configuration_property = emrcontainers.CfnJobTemplate.ParametricS3MonitoringConfigurationProperty(
                    log_uri="logUri"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__aded8a9f274f5fe815114276681a17f8ec3ecfcfe12cabde3177611d95292001)
                check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_uri is not None:
                self._values["log_uri"] = log_uri

        @builtins.property
        def log_uri(self) -> typing.Optional[builtins.str]:
            '''Amazon S3 destination URI for log publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-parametrics3monitoringconfiguration.html#cfn-emrcontainers-jobtemplate-parametrics3monitoringconfiguration-loguri
            '''
            result = self._values.get("log_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametricS3MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.SparkSqlJobDriverProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entry_point": "entryPoint",
            "spark_sql_parameters": "sparkSqlParameters",
        },
    )
    class SparkSqlJobDriverProperty:
        def __init__(
            self,
            *,
            entry_point: typing.Optional[builtins.str] = None,
            spark_sql_parameters: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The job driver for job type.

            :param entry_point: 
            :param spark_sql_parameters: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-sparksqljobdriver.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                spark_sql_job_driver_property = emrcontainers.CfnJobTemplate.SparkSqlJobDriverProperty(
                    entry_point="entryPoint",
                    spark_sql_parameters="sparkSqlParameters"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d7cd0fb159db94a8f48f1d6bb8768b53612b8bf72d17ed12757c43cf6b2d534c)
                check_type(argname="argument entry_point", value=entry_point, expected_type=type_hints["entry_point"])
                check_type(argname="argument spark_sql_parameters", value=spark_sql_parameters, expected_type=type_hints["spark_sql_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if entry_point is not None:
                self._values["entry_point"] = entry_point
            if spark_sql_parameters is not None:
                self._values["spark_sql_parameters"] = spark_sql_parameters

        @builtins.property
        def entry_point(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-sparksqljobdriver.html#cfn-emrcontainers-jobtemplate-sparksqljobdriver-entrypoint
            '''
            result = self._values.get("entry_point")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def spark_sql_parameters(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-sparksqljobdriver.html#cfn-emrcontainers-jobtemplate-sparksqljobdriver-sparksqlparameters
            '''
            result = self._values.get("spark_sql_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SparkSqlJobDriverProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.SparkSubmitJobDriverProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entry_point": "entryPoint",
            "entry_point_arguments": "entryPointArguments",
            "spark_submit_parameters": "sparkSubmitParameters",
        },
    )
    class SparkSubmitJobDriverProperty:
        def __init__(
            self,
            *,
            entry_point: builtins.str,
            entry_point_arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
            spark_submit_parameters: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The information about job driver for Spark submit.

            :param entry_point: 
            :param entry_point_arguments: 
            :param spark_submit_parameters: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                spark_submit_job_driver_property = emrcontainers.CfnJobTemplate.SparkSubmitJobDriverProperty(
                    entry_point="entryPoint",
                
                    # the properties below are optional
                    entry_point_arguments=["entryPointArguments"],
                    spark_submit_parameters="sparkSubmitParameters"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__29459080c432b9a9ebd709ae414b163871b5d34f30f0cd30d0bf5d90e14f12c4)
                check_type(argname="argument entry_point", value=entry_point, expected_type=type_hints["entry_point"])
                check_type(argname="argument entry_point_arguments", value=entry_point_arguments, expected_type=type_hints["entry_point_arguments"])
                check_type(argname="argument spark_submit_parameters", value=spark_submit_parameters, expected_type=type_hints["spark_submit_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entry_point": entry_point,
            }
            if entry_point_arguments is not None:
                self._values["entry_point_arguments"] = entry_point_arguments
            if spark_submit_parameters is not None:
                self._values["spark_submit_parameters"] = spark_submit_parameters

        @builtins.property
        def entry_point(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver.html#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-entrypoint
            '''
            result = self._values.get("entry_point")
            assert result is not None, "Required property 'entry_point' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def entry_point_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver.html#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-entrypointarguments
            '''
            result = self._values.get("entry_point_arguments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def spark_submit_parameters(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-sparksubmitjobdriver.html#cfn-emrcontainers-jobtemplate-sparksubmitjobdriver-sparksubmitparameters
            '''
            result = self._values.get("spark_submit_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SparkSubmitJobDriverProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplate.TemplateParameterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"default_value": "defaultValue", "type": "type"},
    )
    class TemplateParameterConfigurationProperty:
        def __init__(
            self,
            *,
            default_value: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration of a job template parameter.

            :param default_value: The default value for the job template parameter.
            :param type: The type of the job template parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                template_parameter_configuration_property = emrcontainers.CfnJobTemplate.TemplateParameterConfigurationProperty(
                    default_value="defaultValue",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__cf4b4e0e699e8b16d67c152a60c3cc26a460376cfe5eaa8f1394dde60fd2d1f5)
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default_value is not None:
                self._values["default_value"] = default_value
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''The default value for the job template parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration.html#cfn-emrcontainers-jobtemplate-templateparameterconfiguration-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of the job template parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration.html#cfn-emrcontainers-jobtemplate-templateparameterconfiguration-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateParameterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnJobTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_template_data": "jobTemplateData",
        "name": "name",
        "tags": "tags",
    },
)
class CfnJobTemplateProps:
    def __init__(
        self,
        *,
        job_template_data: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnJobTemplate.JobTemplateDataProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnJobTemplate``.

        :param job_template_data: The values of a StartJobRun API request used in job runs started using the job template.
        :param name: The specified name of the job template.
        :param tags: The tags that are associated with the job template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-jobtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrcontainers as emrcontainers
            
            # configuration_property_: emrcontainers.CfnJobTemplate.ConfigurationProperty
            
            cfn_job_template_props = emrcontainers.CfnJobTemplateProps(
                job_template_data=emrcontainers.CfnJobTemplate.JobTemplateDataProperty(
                    execution_role_arn="executionRoleArn",
                    job_driver=emrcontainers.CfnJobTemplate.JobDriverProperty(
                        spark_sql_job_driver=emrcontainers.CfnJobTemplate.SparkSqlJobDriverProperty(
                            entry_point="entryPoint",
                            spark_sql_parameters="sparkSqlParameters"
                        ),
                        spark_submit_job_driver=emrcontainers.CfnJobTemplate.SparkSubmitJobDriverProperty(
                            entry_point="entryPoint",
            
                            # the properties below are optional
                            entry_point_arguments=["entryPointArguments"],
                            spark_submit_parameters="sparkSubmitParameters"
                        )
                    ),
                    release_label="releaseLabel",
            
                    # the properties below are optional
                    configuration_overrides=emrcontainers.CfnJobTemplate.ParametricConfigurationOverridesProperty(
                        application_configuration=[emrcontainers.CfnJobTemplate.ConfigurationProperty(
                            classification="classification",
            
                            # the properties below are optional
                            configurations=[configuration_property_],
                            properties={
                                "properties_key": "properties"
                            }
                        )],
                        monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricMonitoringConfigurationProperty(
                            cloud_watch_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty(
                                log_group_name="logGroupName",
                                log_stream_name_prefix="logStreamNamePrefix"
                            ),
                            persistent_app_ui="persistentAppUi",
                            s3_monitoring_configuration=emrcontainers.CfnJobTemplate.ParametricS3MonitoringConfigurationProperty(
                                log_uri="logUri"
                            )
                        )
                    ),
                    job_tags={
                        "job_tags_key": "jobTags"
                    },
                    parameter_configuration={
                        "parameter_configuration_key": emrcontainers.CfnJobTemplate.TemplateParameterConfigurationProperty(
                            default_value="defaultValue",
                            type="type"
                        )
                    }
                ),
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__98f248117f09ba0f9c281be5d42a29508083a37a5fbe109b20ee6cde5ff705a3)
            check_type(argname="argument job_template_data", value=job_template_data, expected_type=type_hints["job_template_data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_template_data": job_template_data,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_template_data(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.JobTemplateDataProperty"]:
        '''The values of a StartJobRun API request used in job runs started using the job template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-jobtemplate.html#cfn-emrcontainers-jobtemplate-jobtemplatedata
        '''
        result = self._values.get("job_template_data")
        assert result is not None, "Required property 'job_template_data' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnJobTemplate.JobTemplateDataProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The specified name of the job template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-jobtemplate.html#cfn-emrcontainers-jobtemplate-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags that are associated with the job template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-jobtemplate.html#cfn-emrcontainers-jobtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_emrcontainers_6ec331d9.ISecurityConfigurationRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnSecurityConfiguration(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration",
):
    '''Resource Schema of AWS::EMRContainers::SecurityConfiguration Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html
    :cloudformationResource: AWS::EMRContainers::SecurityConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrcontainers as emrcontainers
        
        cfn_security_configuration = emrcontainers.CfnSecurityConfiguration(self, "MyCfnSecurityConfiguration",
            security_configuration_data=emrcontainers.CfnSecurityConfiguration.SecurityConfigurationDataProperty(
                authentication_configuration=emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty(
                    iam_configuration={
                        "system_role": "systemRole"
                    },
                    identity_center_configuration=emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                        enable_identity_center=False,
                        identity_center_application_assignment_required=False,
                        identity_center_instance_arn="identityCenterInstanceArn"
                    )
                ),
                authorization_configuration=emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty(
                    lake_formation_configuration=emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                        authorized_session_tag_value="authorizedSessionTagValue",
                        query_access_control_enabled=False,
                        query_engine_role_arn="queryEngineRoleArn",
                        secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                            cluster_id="clusterId",
                            namespace="namespace"
                        )
                    )
                ),
                encryption_configuration=emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                    at_rest_encryption_configuration=emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                        local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                            aws_kms_key_id="awsKmsKeyId",
                            encryption_key_provider_type="encryptionKeyProviderType"
                        ),
                        s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                            encryption_option="encryptionOption",
                            kms_key_id="kmsKeyId"
                        )
                    ),
                    in_transit_encryption_configuration=emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                        tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                            certificate_provider_type="certificateProviderType",
                            private_key_secret_arn="privateKeySecretArn",
                            public_key_secret_arn="publicKeySecretArn"
                        )
                    )
                )
            ),
        
            # the properties below are optional
            container_provider=emrcontainers.CfnSecurityConfiguration.ContainerProviderProperty(
                id="id",
                type="type",
        
                # the properties below are optional
                info=emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                        namespace="namespace"
                    )
                )
            ),
            name="name",
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
        security_configuration_data: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.SecurityConfigurationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        container_provider: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::SecurityConfiguration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_configuration_data: Security configuration data containing encryption and authorization settings.
        :param container_provider: Container provider information.
        :param name: The name of the security configuration.
        :param tags: An array of key-value pairs to apply to this security configuration.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6854e9fbbee664e2db7e06fdaa2e3ba6c9701b0e2bce486f38e57890c884e5af)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityConfigurationProps(
            security_configuration_data=security_configuration_data,
            container_provider=container_provider,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSecurityConfiguration")
    @builtins.classmethod
    def arn_for_security_configuration(
        cls,
        resource: "_aws_emrcontainers_6ec331d9.ISecurityConfigurationRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cd681409fc29491c4c7e38d95888109a4646290c7d21b905a648c8e49a16cc2f)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSecurityConfiguration", [resource]))

    @jsii.member(jsii_name="isCfnSecurityConfiguration")
    @builtins.classmethod
    def is_cfn_security_configuration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSecurityConfiguration.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__660efc2daaa24d4382b34d964b39452ea882396bad4388acc85c9310c23989b7)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSecurityConfiguration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__adb0191ab4815b507e015b9e53d9a0db9a4b2cee4d58e694160b44a0afe9de56)
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
            type_hints = cached_type_hints(_typecheckingstub__1af0cddd893391660a5e37e50121ea37e58f057538ee52904d314b61aa41e9f8)
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
        '''The ARN of the security configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the security configuration.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(
        self,
    ) -> "_aws_emrcontainers_6ec331d9.SecurityConfigurationReference":
        '''A reference to a SecurityConfiguration resource.'''
        return typing.cast("_aws_emrcontainers_6ec331d9.SecurityConfigurationReference", jsii.get(self, "securityConfigurationRef"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationData")
    def security_configuration_data(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"]:
        '''Security configuration data containing encryption and authorization settings.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"], jsii.get(self, "securityConfigurationData"))

    @security_configuration_data.setter
    def security_configuration_data(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f26dc902c9625031a3359860f64fc2c50df8f76bad05bb460ecddf60a8aef53f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfigurationData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerProvider")
    def container_provider(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.ContainerProviderProperty"]]:
        '''Container provider information.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.ContainerProviderProperty"]], jsii.get(self, "containerProvider"))

    @container_provider.setter
    def container_provider(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.ContainerProviderProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e042738064d96ccff993bc56cc79c7f46ec050b950127cf902598481c68cc9ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerProvider", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__53a52be55c2ce7be9e3a6ef926bc4d573b86d29f190210e5a9df93e655aaa102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this security configuration.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8c1399f0742e46b06a814da734363ceffaf363d4e01a9b76b7506306a813a9c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_disk_encryption_configuration": "localDiskEncryptionConfiguration",
            "s3_encryption_configuration": "s3EncryptionConfiguration",
        },
    )
    class AtRestEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            local_disk_encryption_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_encryption_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.S3EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''At-rest encryption configuration.

            :param local_disk_encryption_configuration: Local disk encryption configuration.
            :param s3_encryption_configuration: S3 encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                at_rest_encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                    local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                        aws_kms_key_id="awsKmsKeyId",
                        encryption_key_provider_type="encryptionKeyProviderType"
                    ),
                    s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                        encryption_option="encryptionOption",
                        kms_key_id="kmsKeyId"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d89332cbba1127be6b8fe5491bceeed96e052518779c07ad4e4adacc05f75a31)
                check_type(argname="argument local_disk_encryption_configuration", value=local_disk_encryption_configuration, expected_type=type_hints["local_disk_encryption_configuration"])
                check_type(argname="argument s3_encryption_configuration", value=s3_encryption_configuration, expected_type=type_hints["s3_encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if local_disk_encryption_configuration is not None:
                self._values["local_disk_encryption_configuration"] = local_disk_encryption_configuration
            if s3_encryption_configuration is not None:
                self._values["s3_encryption_configuration"] = s3_encryption_configuration

        @builtins.property
        def local_disk_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty"]]:
            '''Local disk encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-localdiskencryptionconfiguration
            '''
            result = self._values.get("local_disk_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty"]], result)

        @builtins.property
        def s3_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.S3EncryptionConfigurationProperty"]]:
            '''S3 encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-s3encryptionconfiguration
            '''
            result = self._values.get("s3_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.S3EncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AtRestEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iam_configuration": "iamConfiguration",
            "identity_center_configuration": "identityCenterConfiguration",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            iam_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.IAMConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            identity_center_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.IdentityCenterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Authentication configuration for the security configuration.

            :param iam_configuration: IAM configuration.
            :param identity_center_configuration: Identity Center configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                authentication_configuration_property = emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty(
                    iam_configuration={
                        "system_role": "systemRole"
                    },
                    identity_center_configuration=emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                        enable_identity_center=False,
                        identity_center_application_assignment_required=False,
                        identity_center_instance_arn="identityCenterInstanceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__b3caee46c3c428a38039046963627b08574e1358dac5ece585461aababf8e4ef)
                check_type(argname="argument iam_configuration", value=iam_configuration, expected_type=type_hints["iam_configuration"])
                check_type(argname="argument identity_center_configuration", value=identity_center_configuration, expected_type=type_hints["identity_center_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam_configuration is not None:
                self._values["iam_configuration"] = iam_configuration
            if identity_center_configuration is not None:
                self._values["identity_center_configuration"] = identity_center_configuration

        @builtins.property
        def iam_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.IAMConfigurationProperty"]]:
            '''IAM configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration.html#cfn-emrcontainers-securityconfiguration-authenticationconfiguration-iamconfiguration
            '''
            result = self._values.get("iam_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.IAMConfigurationProperty"]], result)

        @builtins.property
        def identity_center_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.IdentityCenterConfigurationProperty"]]:
            '''Identity Center configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration.html#cfn-emrcontainers-securityconfiguration-authenticationconfiguration-identitycenterconfiguration
            '''
            result = self._values.get("identity_center_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.IdentityCenterConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lake_formation_configuration": "lakeFormationConfiguration"},
    )
    class AuthorizationConfigurationProperty:
        def __init__(
            self,
            *,
            lake_formation_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.LakeFormationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Authorization configuration for the security configuration.

            :param lake_formation_configuration: Lake Formation configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                authorization_configuration_property = emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty(
                    lake_formation_configuration=emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                        authorized_session_tag_value="authorizedSessionTagValue",
                        query_access_control_enabled=False,
                        query_engine_role_arn="queryEngineRoleArn",
                        secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                            cluster_id="clusterId",
                            namespace="namespace"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__76bfe5c6bd23193313bfe6dec8fbee6bf437673f2b46dac54b11ef0689913eab)
                check_type(argname="argument lake_formation_configuration", value=lake_formation_configuration, expected_type=type_hints["lake_formation_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lake_formation_configuration is not None:
                self._values["lake_formation_configuration"] = lake_formation_configuration

        @builtins.property
        def lake_formation_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.LakeFormationConfigurationProperty"]]:
            '''Lake Formation configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration.html#cfn-emrcontainers-securityconfiguration-authorizationconfiguration-lakeformationconfiguration
            '''
            result = self._values.get("lake_formation_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.LakeFormationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_info": "eksInfo"},
    )
    class ContainerInfoProperty:
        def __init__(
            self,
            *,
            eks_info: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.EksInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Container information.

            :param eks_info: EKS information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_info_property = emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                        namespace="namespace"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e0c51a22b843b82d3a2f70b24e8095308dd8fdfb79690f5b0cd87fd63c28654d)
                check_type(argname="argument eks_info", value=eks_info, expected_type=type_hints["eks_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if eks_info is not None:
                self._values["eks_info"] = eks_info

        @builtins.property
        def eks_info(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.EksInfoProperty"]]:
            '''EKS information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerinfo.html#cfn-emrcontainers-securityconfiguration-containerinfo-eksinfo
            '''
            result = self._values.get("eks_info")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.EksInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.ContainerProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "type": "type", "info": "info"},
    )
    class ContainerProviderProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            type: builtins.str,
            info: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.ContainerInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Container provider information.

            :param id: The container provider ID.
            :param type: The container provider type.
            :param info: Container information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_provider_property = emrcontainers.CfnSecurityConfiguration.ContainerProviderProperty(
                    id="id",
                    type="type",
                
                    # the properties below are optional
                    info=emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                            namespace="namespace"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__7defba1afab8843e36776150f6c12baad1d8fceaa1fd92112cabce82147e94e2)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument info", value=info, expected_type=type_hints["info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "type": type,
            }
            if info is not None:
                self._values["info"] = info

        @builtins.property
        def id(self) -> builtins.str:
            '''The container provider ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerprovider.html#cfn-emrcontainers-securityconfiguration-containerprovider-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The container provider type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerprovider.html#cfn-emrcontainers-securityconfiguration-containerprovider-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def info(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.ContainerInfoProperty"]]:
            '''Container information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerprovider.html#cfn-emrcontainers-securityconfiguration-containerprovider-info
            '''
            result = self._values.get("info")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.ContainerInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.EksInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace"},
    )
    class EksInfoProperty:
        def __init__(self, *, namespace: typing.Optional[builtins.str] = None) -> None:
            '''EKS information.

            :param namespace: The EKS namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-eksinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                eks_info_property = emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__5e7712fd7b4a2a053327b1eea8a52f21d3d1f1d9e7efa9b2397fcd486b8eaeb2)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The EKS namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-eksinfo.html#cfn-emrcontainers-securityconfiguration-eksinfo-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "at_rest_encryption_configuration": "atRestEncryptionConfiguration",
            "in_transit_encryption_configuration": "inTransitEncryptionConfiguration",
        },
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            at_rest_encryption_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            in_transit_encryption_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Encryption configuration for the security configuration.

            :param at_rest_encryption_configuration: At-rest encryption configuration.
            :param in_transit_encryption_configuration: In-transit encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                    at_rest_encryption_configuration=emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                        local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                            aws_kms_key_id="awsKmsKeyId",
                            encryption_key_provider_type="encryptionKeyProviderType"
                        ),
                        s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                            encryption_option="encryptionOption",
                            kms_key_id="kmsKeyId"
                        )
                    ),
                    in_transit_encryption_configuration=emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                        tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                            certificate_provider_type="certificateProviderType",
                            private_key_secret_arn="privateKeySecretArn",
                            public_key_secret_arn="publicKeySecretArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f41c637d9cbed4eeb23e20c4bd7928d0c1cf31163ac17153b7e304db762c1128)
                check_type(argname="argument at_rest_encryption_configuration", value=at_rest_encryption_configuration, expected_type=type_hints["at_rest_encryption_configuration"])
                check_type(argname="argument in_transit_encryption_configuration", value=in_transit_encryption_configuration, expected_type=type_hints["in_transit_encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if at_rest_encryption_configuration is not None:
                self._values["at_rest_encryption_configuration"] = at_rest_encryption_configuration
            if in_transit_encryption_configuration is not None:
                self._values["in_transit_encryption_configuration"] = in_transit_encryption_configuration

        @builtins.property
        def at_rest_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty"]]:
            '''At-rest encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-encryptionconfiguration-atrestencryptionconfiguration
            '''
            result = self._values.get("at_rest_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty"]], result)

        @builtins.property
        def in_transit_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty"]]:
            '''In-transit encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-encryptionconfiguration-intransitencryptionconfiguration
            '''
            result = self._values.get("in_transit_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.IAMConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"system_role": "systemRole"},
    )
    class IAMConfigurationProperty:
        def __init__(
            self,
            *,
            system_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''IAM configuration.

            :param system_role: The system role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-iamconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                i_am_configuration_property = {
                    "system_role": "systemRole"
                }
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__496b9118a2747d1a2075cedbe8d8eb5f5ac83784984ccc18bef308ce389d64e5)
                check_type(argname="argument system_role", value=system_role, expected_type=type_hints["system_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if system_role is not None:
                self._values["system_role"] = system_role

        @builtins.property
        def system_role(self) -> typing.Optional[builtins.str]:
            '''The system role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-iamconfiguration.html#cfn-emrcontainers-securityconfiguration-iamconfiguration-systemrole
            '''
            result = self._values.get("system_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IAMConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_identity_center": "enableIdentityCenter",
            "identity_center_application_assignment_required": "identityCenterApplicationAssignmentRequired",
            "identity_center_instance_arn": "identityCenterInstanceArn",
        },
    )
    class IdentityCenterConfigurationProperty:
        def __init__(
            self,
            *,
            enable_identity_center: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            identity_center_application_assignment_required: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            identity_center_instance_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Identity Center configuration.

            :param enable_identity_center: Whether to enable Identity Center integration.
            :param identity_center_application_assignment_required: Whether Identity Center application assignment is required.
            :param identity_center_instance_arn: The ARN of the Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                identity_center_configuration_property = emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                    enable_identity_center=False,
                    identity_center_application_assignment_required=False,
                    identity_center_instance_arn="identityCenterInstanceArn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f599ccca334d667e8c2151ff1efb55fe1a5722a9cef6e6b8e3ad7fc64f6fcb70)
                check_type(argname="argument enable_identity_center", value=enable_identity_center, expected_type=type_hints["enable_identity_center"])
                check_type(argname="argument identity_center_application_assignment_required", value=identity_center_application_assignment_required, expected_type=type_hints["identity_center_application_assignment_required"])
                check_type(argname="argument identity_center_instance_arn", value=identity_center_instance_arn, expected_type=type_hints["identity_center_instance_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_identity_center is not None:
                self._values["enable_identity_center"] = enable_identity_center
            if identity_center_application_assignment_required is not None:
                self._values["identity_center_application_assignment_required"] = identity_center_application_assignment_required
            if identity_center_instance_arn is not None:
                self._values["identity_center_instance_arn"] = identity_center_instance_arn

        @builtins.property
        def enable_identity_center(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether to enable Identity Center integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-enableidentitycenter
            '''
            result = self._values.get("enable_identity_center")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def identity_center_application_assignment_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether Identity Center application assignment is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterapplicationassignmentrequired
            '''
            result = self._values.get("identity_center_application_assignment_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def identity_center_instance_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterinstancearn
            '''
            result = self._values.get("identity_center_instance_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityCenterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"tls_certificate_configuration": "tlsCertificateConfiguration"},
    )
    class InTransitEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            tls_certificate_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.TLSCertificateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''In-transit encryption configuration.

            :param tls_certificate_configuration: TLS certificate configuration for in-transit encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                in_transit_encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                    tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                        certificate_provider_type="certificateProviderType",
                        private_key_secret_arn="privateKeySecretArn",
                        public_key_secret_arn="publicKeySecretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8a9664211c1bd9e53f5b1ef1ea8cf192b0fc36da061879adc5e0f50d83df33bb)
                check_type(argname="argument tls_certificate_configuration", value=tls_certificate_configuration, expected_type=type_hints["tls_certificate_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if tls_certificate_configuration is not None:
                self._values["tls_certificate_configuration"] = tls_certificate_configuration

        @builtins.property
        def tls_certificate_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.TLSCertificateConfigurationProperty"]]:
            '''TLS certificate configuration for in-transit encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-intransitencryptionconfiguration-tlscertificateconfiguration
            '''
            result = self._values.get("tls_certificate_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.TLSCertificateConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InTransitEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorized_session_tag_value": "authorizedSessionTagValue",
            "query_access_control_enabled": "queryAccessControlEnabled",
            "query_engine_role_arn": "queryEngineRoleArn",
            "secure_namespace_info": "secureNamespaceInfo",
        },
    )
    class LakeFormationConfigurationProperty:
        def __init__(
            self,
            *,
            authorized_session_tag_value: typing.Optional[builtins.str] = None,
            query_access_control_enabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            query_engine_role_arn: typing.Optional[builtins.str] = None,
            secure_namespace_info: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.SecureNamespaceInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Lake Formation configuration.

            :param authorized_session_tag_value: The session tag to authorize Lake Formation access.
            :param query_access_control_enabled: Whether query access control is enabled.
            :param query_engine_role_arn: The ARN of the query engine role.
            :param secure_namespace_info: Secure namespace information for Lake Formation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                lake_formation_configuration_property = emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                    authorized_session_tag_value="authorizedSessionTagValue",
                    query_access_control_enabled=False,
                    query_engine_role_arn="queryEngineRoleArn",
                    secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                        cluster_id="clusterId",
                        namespace="namespace"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__28a87784f85f0e663cd90e1e0ab8f0457d68b1df23a29ec1815efffb1fd76efd)
                check_type(argname="argument authorized_session_tag_value", value=authorized_session_tag_value, expected_type=type_hints["authorized_session_tag_value"])
                check_type(argname="argument query_access_control_enabled", value=query_access_control_enabled, expected_type=type_hints["query_access_control_enabled"])
                check_type(argname="argument query_engine_role_arn", value=query_engine_role_arn, expected_type=type_hints["query_engine_role_arn"])
                check_type(argname="argument secure_namespace_info", value=secure_namespace_info, expected_type=type_hints["secure_namespace_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorized_session_tag_value is not None:
                self._values["authorized_session_tag_value"] = authorized_session_tag_value
            if query_access_control_enabled is not None:
                self._values["query_access_control_enabled"] = query_access_control_enabled
            if query_engine_role_arn is not None:
                self._values["query_engine_role_arn"] = query_engine_role_arn
            if secure_namespace_info is not None:
                self._values["secure_namespace_info"] = secure_namespace_info

        @builtins.property
        def authorized_session_tag_value(self) -> typing.Optional[builtins.str]:
            '''The session tag to authorize Lake Formation access.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-authorizedsessiontagvalue
            '''
            result = self._values.get("authorized_session_tag_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_access_control_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Whether query access control is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryaccesscontrolenabled
            '''
            result = self._values.get("query_access_control_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def query_engine_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the query engine role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryenginerolearn
            '''
            result = self._values.get("query_engine_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secure_namespace_info(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.SecureNamespaceInfoProperty"]]:
            '''Secure namespace information for Lake Formation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-securenamespaceinfo
            '''
            result = self._values.get("secure_namespace_info")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.SecureNamespaceInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LakeFormationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_kms_key_id": "awsKmsKeyId",
            "encryption_key_provider_type": "encryptionKeyProviderType",
        },
    )
    class LocalDiskEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            aws_kms_key_id: typing.Optional[builtins.str] = None,
            encryption_key_provider_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Local disk encryption configuration.

            :param aws_kms_key_id: The AWS KMS key ID.
            :param encryption_key_provider_type: The encryption key provider type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                local_disk_encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                    aws_kms_key_id="awsKmsKeyId",
                    encryption_key_provider_type="encryptionKeyProviderType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__4511400021d1afa893531440e558c9b57d99a8e63fbbae50c1a5f5360e1eff2d)
                check_type(argname="argument aws_kms_key_id", value=aws_kms_key_id, expected_type=type_hints["aws_kms_key_id"])
                check_type(argname="argument encryption_key_provider_type", value=encryption_key_provider_type, expected_type=type_hints["encryption_key_provider_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_kms_key_id is not None:
                self._values["aws_kms_key_id"] = aws_kms_key_id
            if encryption_key_provider_type is not None:
                self._values["encryption_key_provider_type"] = encryption_key_provider_type

        @builtins.property
        def aws_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The AWS KMS key ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-awskmskeyid
            '''
            result = self._values.get("aws_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_key_provider_type(self) -> typing.Optional[builtins.str]:
            '''The encryption key provider type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-encryptionkeyprovidertype
            '''
            result = self._values.get("encryption_key_provider_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalDiskEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_option": "encryptionOption",
            "kms_key_id": "kmsKeyId",
        },
    )
    class S3EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_option: typing.Optional[builtins.str] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''S3 encryption configuration.

            :param encryption_option: The S3 encryption option.
            :param kms_key_id: The KMS key ID for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                s3_encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                    encryption_option="encryptionOption",
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__dd8412be690034fa6d1270d9b5c028c8a5a0b2b83defe7f3c1a7d21b32790a48)
                check_type(argname="argument encryption_option", value=encryption_option, expected_type=type_hints["encryption_option"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption_option is not None:
                self._values["encryption_option"] = encryption_option
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def encryption_option(self) -> typing.Optional[builtins.str]:
            '''The S3 encryption option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-encryptionoption
            '''
            result = self._values.get("encryption_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS key ID for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_id": "clusterId", "namespace": "namespace"},
    )
    class SecureNamespaceInfoProperty:
        def __init__(
            self,
            *,
            cluster_id: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Secure namespace information for Lake Formation.

            :param cluster_id: The ID of the cluster.
            :param namespace: The namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                secure_namespace_info_property = emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                    cluster_id="clusterId",
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__3759e01f350e1d397915bd4d597987fa0422a4123e65b626ce60a9961e8df11c)
                check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cluster_id is not None:
                self._values["cluster_id"] = cluster_id
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def cluster_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo.html#cfn-emrcontainers-securityconfiguration-securenamespaceinfo-clusterid
            '''
            result = self._values.get("cluster_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo.html#cfn-emrcontainers-securityconfiguration-securenamespaceinfo-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecureNamespaceInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.SecurityConfigurationDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "authorization_configuration": "authorizationConfiguration",
            "encryption_configuration": "encryptionConfiguration",
        },
    )
    class SecurityConfigurationDataProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.AuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            authorization_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.AuthorizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            encryption_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Security configuration data containing encryption and authorization settings.

            :param authentication_configuration: Authentication configuration for the security configuration.
            :param authorization_configuration: Authorization configuration for the security configuration.
            :param encryption_configuration: Encryption configuration for the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                security_configuration_data_property = emrcontainers.CfnSecurityConfiguration.SecurityConfigurationDataProperty(
                    authentication_configuration=emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty(
                        iam_configuration={
                            "system_role": "systemRole"
                        },
                        identity_center_configuration=emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                            enable_identity_center=False,
                            identity_center_application_assignment_required=False,
                            identity_center_instance_arn="identityCenterInstanceArn"
                        )
                    ),
                    authorization_configuration=emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty(
                        lake_formation_configuration=emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                            authorized_session_tag_value="authorizedSessionTagValue",
                            query_access_control_enabled=False,
                            query_engine_role_arn="queryEngineRoleArn",
                            secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                                cluster_id="clusterId",
                                namespace="namespace"
                            )
                        )
                    ),
                    encryption_configuration=emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                        at_rest_encryption_configuration=emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                            local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                                aws_kms_key_id="awsKmsKeyId",
                                encryption_key_provider_type="encryptionKeyProviderType"
                            ),
                            s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                                encryption_option="encryptionOption",
                                kms_key_id="kmsKeyId"
                            )
                        ),
                        in_transit_encryption_configuration=emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                            tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                                certificate_provider_type="certificateProviderType",
                                private_key_secret_arn="privateKeySecretArn",
                                public_key_secret_arn="publicKeySecretArn"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f493d86970b0aa105efd09d9ecac31f88dcd70be4b4008d89647b65c9b717653)
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument authorization_configuration", value=authorization_configuration, expected_type=type_hints["authorization_configuration"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if authorization_configuration is not None:
                self._values["authorization_configuration"] = authorization_configuration
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.AuthenticationConfigurationProperty"]]:
            '''Authentication configuration for the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.AuthenticationConfigurationProperty"]], result)

        @builtins.property
        def authorization_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.AuthorizationConfigurationProperty"]]:
            '''Authorization configuration for the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authorizationconfiguration
            '''
            result = self._values.get("authorization_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.AuthorizationConfigurationProperty"]], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.EncryptionConfigurationProperty"]]:
            '''Encryption configuration for the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.EncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecurityConfigurationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_provider_type": "certificateProviderType",
            "private_key_secret_arn": "privateKeySecretArn",
            "public_key_secret_arn": "publicKeySecretArn",
        },
    )
    class TLSCertificateConfigurationProperty:
        def __init__(
            self,
            *,
            certificate_provider_type: typing.Optional[builtins.str] = None,
            private_key_secret_arn: typing.Optional[builtins.str] = None,
            public_key_secret_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''TLS certificate configuration for in-transit encryption.

            :param certificate_provider_type: The certificate provider type.
            :param private_key_secret_arn: The ARN of the secret containing the private key.
            :param public_key_secret_arn: The ARN of the secret containing the public key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                t_ls_certificate_configuration_property = emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                    certificate_provider_type="certificateProviderType",
                    private_key_secret_arn="privateKeySecretArn",
                    public_key_secret_arn="publicKeySecretArn"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__7f48594c857b1e3ec68169c0a14e6791998c57deb66a4337a04f55c5cd650e7e)
                check_type(argname="argument certificate_provider_type", value=certificate_provider_type, expected_type=type_hints["certificate_provider_type"])
                check_type(argname="argument private_key_secret_arn", value=private_key_secret_arn, expected_type=type_hints["private_key_secret_arn"])
                check_type(argname="argument public_key_secret_arn", value=public_key_secret_arn, expected_type=type_hints["public_key_secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_provider_type is not None:
                self._values["certificate_provider_type"] = certificate_provider_type
            if private_key_secret_arn is not None:
                self._values["private_key_secret_arn"] = private_key_secret_arn
            if public_key_secret_arn is not None:
                self._values["public_key_secret_arn"] = public_key_secret_arn

        @builtins.property
        def certificate_provider_type(self) -> typing.Optional[builtins.str]:
            '''The certificate provider type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-certificateprovidertype
            '''
            result = self._values.get("certificate_provider_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_key_secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret containing the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-privatekeysecretarn
            '''
            result = self._values.get("private_key_secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def public_key_secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret containing the public key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-publickeysecretarn
            '''
            result = self._values.get("public_key_secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TLSCertificateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_configuration_data": "securityConfigurationData",
        "container_provider": "containerProvider",
        "name": "name",
        "tags": "tags",
    },
)
class CfnSecurityConfigurationProps:
    def __init__(
        self,
        *,
        security_configuration_data: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.SecurityConfigurationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        container_provider: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSecurityConfiguration.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityConfiguration``.

        :param security_configuration_data: Security configuration data containing encryption and authorization settings.
        :param container_provider: Container provider information.
        :param name: The name of the security configuration.
        :param tags: An array of key-value pairs to apply to this security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrcontainers as emrcontainers
            
            cfn_security_configuration_props = emrcontainers.CfnSecurityConfigurationProps(
                security_configuration_data=emrcontainers.CfnSecurityConfiguration.SecurityConfigurationDataProperty(
                    authentication_configuration=emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty(
                        iam_configuration={
                            "system_role": "systemRole"
                        },
                        identity_center_configuration=emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                            enable_identity_center=False,
                            identity_center_application_assignment_required=False,
                            identity_center_instance_arn="identityCenterInstanceArn"
                        )
                    ),
                    authorization_configuration=emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty(
                        lake_formation_configuration=emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                            authorized_session_tag_value="authorizedSessionTagValue",
                            query_access_control_enabled=False,
                            query_engine_role_arn="queryEngineRoleArn",
                            secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                                cluster_id="clusterId",
                                namespace="namespace"
                            )
                        )
                    ),
                    encryption_configuration=emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                        at_rest_encryption_configuration=emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                            local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                                aws_kms_key_id="awsKmsKeyId",
                                encryption_key_provider_type="encryptionKeyProviderType"
                            ),
                            s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                                encryption_option="encryptionOption",
                                kms_key_id="kmsKeyId"
                            )
                        ),
                        in_transit_encryption_configuration=emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                            tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                                certificate_provider_type="certificateProviderType",
                                private_key_secret_arn="privateKeySecretArn",
                                public_key_secret_arn="publicKeySecretArn"
                            )
                        )
                    )
                ),
            
                # the properties below are optional
                container_provider=emrcontainers.CfnSecurityConfiguration.ContainerProviderProperty(
                    id="id",
                    type="type",
            
                    # the properties below are optional
                    info=emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                            namespace="namespace"
                        )
                    )
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aac200d052b6d8b5d83eb4ae9a2c63aeb84f4e4ce7bc48d47327fc9874cfba98)
            check_type(argname="argument security_configuration_data", value=security_configuration_data, expected_type=type_hints["security_configuration_data"])
            check_type(argname="argument container_provider", value=container_provider, expected_type=type_hints["container_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_configuration_data": security_configuration_data,
        }
        if container_provider is not None:
            self._values["container_provider"] = container_provider
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def security_configuration_data(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"]:
        '''Security configuration data containing encryption and authorization settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html#cfn-emrcontainers-securityconfiguration-securityconfigurationdata
        '''
        result = self._values.get("security_configuration_data")
        assert result is not None, "Required property 'security_configuration_data' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"], result)

    @builtins.property
    def container_provider(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.ContainerProviderProperty"]]:
        '''Container provider information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html#cfn-emrcontainers-securityconfiguration-containerprovider
        '''
        result = self._values.get("container_provider")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSecurityConfiguration.ContainerProviderProperty"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html#cfn-emrcontainers-securityconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html#cfn-emrcontainers-securityconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_emrcontainers_6ec331d9.IVirtualClusterRef, _aws_cdk_0cae9daa.ITaggable)
class CfnVirtualCluster(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster",
):
    '''The ``AWS::EMRContainers::VirtualCluster`` resource specifies a virtual cluster.

    A virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list, and delete virtual clusters. They do not consume any additional resources in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
    :cloudformationResource: AWS::EMRContainers::VirtualCluster
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrcontainers as emrcontainers
        
        cfn_virtual_cluster = emrcontainers.CfnVirtualCluster(self, "MyCfnVirtualCluster",
            container_provider=emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                id="id",
                info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                        namespace="namespace"
                    )
                ),
                type="type"
            ),
            name="name",
        
            # the properties below are optional
            security_configuration_id="securityConfigurationId",
            session_enabled=False,
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
        container_provider: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnVirtualCluster.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        security_configuration_id: typing.Optional[builtins.str] = None,
        session_enabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::VirtualCluster``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param container_provider: The container provider of the virtual cluster.
        :param name: The name of the virtual cluster.
        :param security_configuration_id: The ID of the security configuration.
        :param session_enabled: Whether the virtual cluster is session-enabled for Spark Connect.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a06dc2760ceb0de7a449a23941f15987094157d1a540c30fa67c9e49a3e06101)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVirtualClusterProps(
            container_provider=container_provider,
            name=name,
            security_configuration_id=security_configuration_id,
            session_enabled=session_enabled,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVirtualCluster")
    @builtins.classmethod
    def arn_for_virtual_cluster(
        cls,
        resource: "_aws_emrcontainers_6ec331d9.IVirtualClusterRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__516f2f16964e7ef220cab41225b3b7c3e3c0a9ee6b852252c3f1a1871264629c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVirtualCluster", [resource]))

    @jsii.member(jsii_name="fromVirtualClusterArn")
    @builtins.classmethod
    def from_virtual_cluster_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_aws_emrcontainers_6ec331d9.IVirtualClusterRef":
        '''Creates a new IVirtualClusterRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0d7111433bac0bf3eef5f3ffc73c4e649ef41bf63a44cfbc891a7f06a1b9be4b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_aws_emrcontainers_6ec331d9.IVirtualClusterRef", jsii.sinvoke(cls, "fromVirtualClusterArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromVirtualClusterId")
    @builtins.classmethod
    def from_virtual_cluster_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        virtual_cluster_id: builtins.str,
    ) -> "_aws_emrcontainers_6ec331d9.IVirtualClusterRef":
        '''Creates a new IVirtualClusterRef from a virtualClusterId.

        :param scope: -
        :param id: -
        :param virtual_cluster_id: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fcaea2c30abe44238307f21b3c8a59222637a0fd52fab165c6272df6fa333e6a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument virtual_cluster_id", value=virtual_cluster_id, expected_type=type_hints["virtual_cluster_id"])
        return typing.cast("_aws_emrcontainers_6ec331d9.IVirtualClusterRef", jsii.sinvoke(cls, "fromVirtualClusterId", [scope, id, virtual_cluster_id]))

    @jsii.member(jsii_name="isCfnVirtualCluster")
    @builtins.classmethod
    def is_cfn_virtual_cluster(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVirtualCluster.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7c9228b7a5165151302a3840836f9259f95d9a03c7684570914df3c5f40c23a7)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVirtualCluster", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__802f118bbdec329d651201f6f69836e8e9523c47d32a262a55c4813747ccf78c)
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
            type_hints = cached_type_hints(_typecheckingstub__3035614e8641a59d4a7600ad906f142054401a42e6c1ca14df8b5d57d08f0823)
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
        '''The Amazon Resource Name (ARN) of the project, such as ``arn:aws:emr-containers:us-east-1:123456789012:/virtualclusters/ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the virtual cluster, such as ``ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="virtualClusterRef")
    def virtual_cluster_ref(
        self,
    ) -> "_aws_emrcontainers_6ec331d9.VirtualClusterReference":
        '''A reference to a VirtualCluster resource.'''
        return typing.cast("_aws_emrcontainers_6ec331d9.VirtualClusterReference", jsii.get(self, "virtualClusterRef"))

    @builtins.property
    @jsii.member(jsii_name="containerProvider")
    def container_provider(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.ContainerProviderProperty"]:
        '''The container provider of the virtual cluster.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.ContainerProviderProperty"], jsii.get(self, "containerProvider"))

    @container_provider.setter
    def container_provider(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.ContainerProviderProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__617f2c6bc289034f068a4b514139fc0bee8f6455f589c3e2de7ee7fb7a3a92e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerProvider", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the virtual cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aea4d0052a5a6cb82d57b5655349988466e02d75bbcc22aec370e6810b4c382d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationId")
    def security_configuration_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the security configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfigurationId"))

    @security_configuration_id.setter
    def security_configuration_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d05d102efa2c9eb1d454519ceade8e11615a54a4a6a9f26f4883e2051aa27414)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfigurationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sessionEnabled")
    def session_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether the virtual cluster is session-enabled for Spark Connect.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "sessionEnabled"))

    @session_enabled.setter
    def session_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dafc8c819a71b8bba3743ac1d1856e48dfcde0282939e418f00798f9c7c33fb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionEnabled", value) # pyright: ignore[reportArgumentType]

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
            type_hints = cached_type_hints(_typecheckingstub__b3436f23ae2ca4313aacb96519980906e71e5bc37e7a466a53353480f948e674)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.ContainerInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_info": "eksInfo"},
    )
    class ContainerInfoProperty:
        def __init__(
            self,
            *,
            eks_info: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnVirtualCluster.EksInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The information about the container used for a job run or a managed endpoint.

            :param eks_info: The information about the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_info_property = emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                        namespace="namespace"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8e5baf7a38335e2eb8733f2aa2d96a9593d774d095fb8a05dcf1d8bd22323050)
                check_type(argname="argument eks_info", value=eks_info, expected_type=type_hints["eks_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "eks_info": eks_info,
            }

        @builtins.property
        def eks_info(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.EksInfoProperty"]:
            '''The information about the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html#cfn-emrcontainers-virtualcluster-containerinfo-eksinfo
            '''
            result = self._values.get("eks_info")
            assert result is not None, "Required property 'eks_info' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.EksInfoProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.ContainerProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "info": "info", "type": "type"},
    )
    class ContainerProviderProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            info: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnVirtualCluster.ContainerInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''The information about the container provider.

            :param id: The ID of the container cluster. *Minimum* : 1 *Maximum* : 100 *Pattern* : ``^[0-9A-Za-z][A-Za-z0-9\\-_]*``
            :param info: The information about the container cluster.
            :param type: The type of the container provider. Amazon EKS is the only supported type as of now.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_provider_property = emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                    id="id",
                    info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                            namespace="namespace"
                        )
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__19801d68aea5b7c69bfd60c7d9c690e62c4643fe80fcda956e884f367b8b1dcf)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument info", value=info, expected_type=type_hints["info"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "info": info,
                "type": type,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The ID of the container cluster.

            *Minimum* : 1

            *Maximum* : 100

            *Pattern* : ``^[0-9A-Za-z][A-Za-z0-9\\-_]*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def info(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.ContainerInfoProperty"]:
            '''The information about the container cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-info
            '''
            result = self._values.get("info")
            assert result is not None, "Required property 'info' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.ContainerInfoProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the container provider.

            Amazon EKS is the only supported type as of now.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.EksInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace"},
    )
    class EksInfoProperty:
        def __init__(self, *, namespace: builtins.str) -> None:
            '''The information about the Amazon EKS cluster.

            :param namespace: The namespaces of the EKS cluster. *Minimum* : 1 *Maximum* : 63 *Pattern* : ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                eks_info_property = emrcontainers.CfnVirtualCluster.EksInfoProperty(
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__26be72236c14a8878e3d92d7b17397aa49c8a844f85e9e98c958600dd7a08c8f)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "namespace": namespace,
            }

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespaces of the EKS cluster.

            *Minimum* : 1

            *Maximum* : 63

            *Pattern* : ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html#cfn-emrcontainers-virtualcluster-eksinfo-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_provider": "containerProvider",
        "name": "name",
        "security_configuration_id": "securityConfigurationId",
        "session_enabled": "sessionEnabled",
        "tags": "tags",
    },
)
class CfnVirtualClusterProps:
    def __init__(
        self,
        *,
        container_provider: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnVirtualCluster.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        security_configuration_id: typing.Optional[builtins.str] = None,
        session_enabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVirtualCluster``.

        :param container_provider: The container provider of the virtual cluster.
        :param name: The name of the virtual cluster.
        :param security_configuration_id: The ID of the security configuration.
        :param session_enabled: Whether the virtual cluster is session-enabled for Spark Connect.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrcontainers as emrcontainers
            
            cfn_virtual_cluster_props = emrcontainers.CfnVirtualClusterProps(
                container_provider=emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                    id="id",
                    info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                            namespace="namespace"
                        )
                    ),
                    type="type"
                ),
                name="name",
            
                # the properties below are optional
                security_configuration_id="securityConfigurationId",
                session_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__79f93ead2a436b8c5a2fc364fff5d9da849a851543aa1433cd7ab649d79d55f9)
            check_type(argname="argument container_provider", value=container_provider, expected_type=type_hints["container_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument security_configuration_id", value=security_configuration_id, expected_type=type_hints["security_configuration_id"])
            check_type(argname="argument session_enabled", value=session_enabled, expected_type=type_hints["session_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_provider": container_provider,
            "name": name,
        }
        if security_configuration_id is not None:
            self._values["security_configuration_id"] = security_configuration_id
        if session_enabled is not None:
            self._values["session_enabled"] = session_enabled
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def container_provider(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.ContainerProviderProperty"]:
        '''The container provider of the virtual cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-containerprovider
        '''
        result = self._values.get("container_provider")
        assert result is not None, "Required property 'container_provider' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVirtualCluster.ContainerProviderProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the virtual cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_configuration_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-securityconfigurationid
        '''
        result = self._values.get("security_configuration_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether the virtual cluster is session-enabled for Spark Connect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-sessionenabled
        '''
        result = self._values.get("session_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEndpoint",
    "CfnEndpointProps",
    "CfnJobTemplate",
    "CfnJobTemplateProps",
    "CfnSecurityConfiguration",
    "CfnSecurityConfigurationProps",
    "CfnVirtualCluster",
    "CfnVirtualClusterProps",
]

publication.publish()

def _typecheckingstub__23b89c74ef5fd6a5347927e915b67a755f92f55810673773d86745b94ec9ce0c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    execution_role_arn: builtins.str,
    release_label: builtins.str,
    type: builtins.str,
    virtual_cluster_id: builtins.str,
    configuration_overrides: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEndpoint.ConfigurationOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    session_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0893eaff59c12b7e6dd4dfd799d44a31fa49362dec8ba203c7f8e79029bff9(
    resource: _aws_emrcontainers_6ec331d9.IEndpointRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__635096970c8f6988b319790d01d10b7af1624a2bd87a8fd19d2f526067565d38(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f81524f5f031b60202ef5750c9c53a9e8e5e0357685aef97a068e09c19a1d5d(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22395c6c2f1b0a694a9e0faf2c896173a496cbdf51ca26ecd7214a44487b981e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82adad35327e5af1f867ea3ce6b09d9cf8bf066d4f3f0c3a297e3425583291ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fdfe64e097ccd04046eb25d75f28e5f90eca1ce0eda856ca0f77cf38cdb414e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e3365f1d0529739a9e96ac4af19a8abe17480deaa11498dbba4db6c1eb52a61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b0a84d01612790328a1ecc8558a579f74f52fa1a781ed7197676c50fce5a6e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0c8197e58a0f1f00521e2589c5fe3688295bc923b51b75d41f29f6aec64d3e(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnEndpoint.ConfigurationOverridesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff6a672ee7bf784cfbde2614d2f6cae307ce23728014e1a8bb6736b2020c7c0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e130186ac0641d5db5870b89171b366bc2c58acd32460ae6419a099b3796f5a6(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea06eef637e8c0a25b829a6c624ac3e00fd1f47e5a0dc21e18b827b60481aa0c(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0753442657548325e3bd0a9ec7c567fdf41626466b3e89bfed14dee1c6cec778(
    *,
    certificate_arn: typing.Optional[builtins.str] = None,
    certificate_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ecb22ba4d8b0faedcb5f445667dd4c14b1bb238ebfc25811866bc27bb2f9f29(
    *,
    log_group_name: builtins.str,
    log_stream_name_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46f984090360c20eea47211457bc59ba0064e851b8407461cf578437814aeb01(
    *,
    application_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEndpoint.EMREKSConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEndpoint.MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__817b097d9818e8dbd56314bb022a526176ef9e0a159ab0fbb93fd2ba36f723a2(
    *,
    max_files_to_keep: jsii.Number,
    rotation_size: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e05064bc37ba71915107a21d96057346160606aa8cdc19d7293f9c9037b47a(
    *,
    classification: builtins.str,
    configurations: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEndpoint.EMREKSConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    properties: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a0503e26d3c8fcf0703183603081e1b7a18027a03a980ed33b0bb37c14dff86(
    *,
    cloud_watch_monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEndpoint.CloudWatchMonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    container_log_rotation_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEndpoint.ContainerLogRotationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    persistent_app_ui: typing.Optional[builtins.str] = None,
    s3_monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEndpoint.S3MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e089a4b5c6bf3faf983bfe03d5042364c4f68c554cd62834b53e7101c615e6(
    *,
    log_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf3149ecf1698607ceb24e9bbca6c307d3e7ef064cb79d95651abb2c6d47065(
    *,
    execution_role_arn: builtins.str,
    release_label: builtins.str,
    type: builtins.str,
    virtual_cluster_id: builtins.str,
    configuration_overrides: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnEndpoint.ConfigurationOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    session_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c029a2e31e8024de8be1d7d6cc3164b0c4d242cdaa1e78e8152aa39ef297d2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    job_template_data: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.JobTemplateDataProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1213684e48ba2ff226bf53a018eb8e22032bf66dc3b8fe2f7726727ccfaf17c(
    resource: _aws_emrcontainers_6ec331d9.IJobTemplateRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef61bbeea56cb835cf288985902b03d2ce3397c18d79451812a3afabe72d771b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fac5ed807f28c92b34b59474a24387d74ed0a6c77074e3e4da0476148fe5b99(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0561a43529d97a11acf97d0c2115c911dc5c3e4e3abbbf8b3457e4d218c1a8e5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32317f0a78421d5632e7bc6574dda9ffbfcb0256a5946e6ee690d70dac4c3356(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnJobTemplate.JobTemplateDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b7c793a65240af6e7ad92176cb6a473c8e8c548c0a0023cd5ae280287fcf21f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b41299b65ce9b702f45b330d4070751ff8c0770b49288ef2e475935df515b8(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b22b73396a3e46a6548256a211ad34a4fca6efd9179dc495c01be7ffb9a11862(
    *,
    classification: builtins.str,
    configurations: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    properties: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c21790543c1028a1851da37b5b1f0984fe52d70bcf238cd7a5c62b7eede1793(
    *,
    spark_sql_job_driver: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.SparkSqlJobDriverProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    spark_submit_job_driver: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.SparkSubmitJobDriverProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795c32821cadb799a4fb4fbfd3bdce984d0531111086ba2e4f67dfbf1c2428b4(
    *,
    execution_role_arn: builtins.str,
    job_driver: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.JobDriverProperty, typing.Dict[builtins.str, typing.Any]]],
    release_label: builtins.str,
    configuration_overrides: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.ParametricConfigurationOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_tags: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    parameter_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.TemplateParameterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c62e7a0a0f8bf638323db721f046500c4c5835ae9de13cc405a7ad3cdfe8a2c2(
    *,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1861b199e8dd763443b960028c0df4e34bb4f5294d46210e36d3637722fc7f4(
    *,
    application_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.ParametricMonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3f8c8bf13509d313157c1a5d5cc47e5eaef673acbdcc737fbb4ab54c97f97e3(
    *,
    cloud_watch_monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.ParametricCloudWatchMonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    persistent_app_ui: typing.Optional[builtins.str] = None,
    s3_monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.ParametricS3MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aded8a9f274f5fe815114276681a17f8ec3ecfcfe12cabde3177611d95292001(
    *,
    log_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7cd0fb159db94a8f48f1d6bb8768b53612b8bf72d17ed12757c43cf6b2d534c(
    *,
    entry_point: typing.Optional[builtins.str] = None,
    spark_sql_parameters: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29459080c432b9a9ebd709ae414b163871b5d34f30f0cd30d0bf5d90e14f12c4(
    *,
    entry_point: builtins.str,
    entry_point_arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
    spark_submit_parameters: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4b4e0e699e8b16d67c152a60c3cc26a460376cfe5eaa8f1394dde60fd2d1f5(
    *,
    default_value: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f248117f09ba0f9c281be5d42a29508083a37a5fbe109b20ee6cde5ff705a3(
    *,
    job_template_data: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnJobTemplate.JobTemplateDataProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6854e9fbbee664e2db7e06fdaa2e3ba6c9701b0e2bce486f38e57890c884e5af(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_configuration_data: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.SecurityConfigurationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    container_provider: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd681409fc29491c4c7e38d95888109a4646290c7d21b905a648c8e49a16cc2f(
    resource: _aws_emrcontainers_6ec331d9.ISecurityConfigurationRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660efc2daaa24d4382b34d964b39452ea882396bad4388acc85c9310c23989b7(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb0191ab4815b507e015b9e53d9a0db9a4b2cee4d58e694160b44a0afe9de56(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af0cddd893391660a5e37e50121ea37e58f057538ee52904d314b61aa41e9f8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26dc902c9625031a3359860f64fc2c50df8f76bad05bb460ecddf60a8aef53f(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSecurityConfiguration.SecurityConfigurationDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e042738064d96ccff993bc56cc79c7f46ec050b950127cf902598481c68cc9ca(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSecurityConfiguration.ContainerProviderProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53a52be55c2ce7be9e3a6ef926bc4d573b86d29f190210e5a9df93e655aaa102(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c1399f0742e46b06a814da734363ceffaf363d4e01a9b76b7506306a813a9c7(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d89332cbba1127be6b8fe5491bceeed96e052518779c07ad4e4adacc05f75a31(
    *,
    local_disk_encryption_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_encryption_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.S3EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3caee46c3c428a38039046963627b08574e1358dac5ece585461aababf8e4ef(
    *,
    iam_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.IAMConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_center_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.IdentityCenterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76bfe5c6bd23193313bfe6dec8fbee6bf437673f2b46dac54b11ef0689913eab(
    *,
    lake_formation_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.LakeFormationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c51a22b843b82d3a2f70b24e8095308dd8fdfb79690f5b0cd87fd63c28654d(
    *,
    eks_info: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.EksInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7defba1afab8843e36776150f6c12baad1d8fceaa1fd92112cabce82147e94e2(
    *,
    id: builtins.str,
    type: builtins.str,
    info: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.ContainerInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7712fd7b4a2a053327b1eea8a52f21d3d1f1d9e7efa9b2397fcd486b8eaeb2(
    *,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41c637d9cbed4eeb23e20c4bd7928d0c1cf31163ac17153b7e304db762c1128(
    *,
    at_rest_encryption_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    in_transit_encryption_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__496b9118a2747d1a2075cedbe8d8eb5f5ac83784984ccc18bef308ce389d64e5(
    *,
    system_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f599ccca334d667e8c2151ff1efb55fe1a5722a9cef6e6b8e3ad7fc64f6fcb70(
    *,
    enable_identity_center: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    identity_center_application_assignment_required: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    identity_center_instance_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a9664211c1bd9e53f5b1ef1ea8cf192b0fc36da061879adc5e0f50d83df33bb(
    *,
    tls_certificate_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.TLSCertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28a87784f85f0e663cd90e1e0ab8f0457d68b1df23a29ec1815efffb1fd76efd(
    *,
    authorized_session_tag_value: typing.Optional[builtins.str] = None,
    query_access_control_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    query_engine_role_arn: typing.Optional[builtins.str] = None,
    secure_namespace_info: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.SecureNamespaceInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4511400021d1afa893531440e558c9b57d99a8e63fbbae50c1a5f5360e1eff2d(
    *,
    aws_kms_key_id: typing.Optional[builtins.str] = None,
    encryption_key_provider_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd8412be690034fa6d1270d9b5c028c8a5a0b2b83defe7f3c1a7d21b32790a48(
    *,
    encryption_option: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3759e01f350e1d397915bd4d597987fa0422a4123e65b626ce60a9961e8df11c(
    *,
    cluster_id: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f493d86970b0aa105efd09d9ecac31f88dcd70be4b4008d89647b65c9b717653(
    *,
    authentication_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    authorization_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.AuthorizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f48594c857b1e3ec68169c0a14e6791998c57deb66a4337a04f55c5cd650e7e(
    *,
    certificate_provider_type: typing.Optional[builtins.str] = None,
    private_key_secret_arn: typing.Optional[builtins.str] = None,
    public_key_secret_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac200d052b6d8b5d83eb4ae9a2c63aeb84f4e4ce7bc48d47327fc9874cfba98(
    *,
    security_configuration_data: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.SecurityConfigurationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    container_provider: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSecurityConfiguration.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06dc2760ceb0de7a449a23941f15987094157d1a540c30fa67c9e49a3e06101(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    container_provider: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    security_configuration_id: typing.Optional[builtins.str] = None,
    session_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__516f2f16964e7ef220cab41225b3b7c3e3c0a9ee6b852252c3f1a1871264629c(
    resource: _aws_emrcontainers_6ec331d9.IVirtualClusterRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7111433bac0bf3eef5f3ffc73c4e649ef41bf63a44cfbc891a7f06a1b9be4b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcaea2c30abe44238307f21b3c8a59222637a0fd52fab165c6272df6fa333e6a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    virtual_cluster_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c9228b7a5165151302a3840836f9259f95d9a03c7684570914df3c5f40c23a7(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802f118bbdec329d651201f6f69836e8e9523c47d32a262a55c4813747ccf78c(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3035614e8641a59d4a7600ad906f142054401a42e6c1ca14df8b5d57d08f0823(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__617f2c6bc289034f068a4b514139fc0bee8f6455f589c3e2de7ee7fb7a3a92e3(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnVirtualCluster.ContainerProviderProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea4d0052a5a6cb82d57b5655349988466e02d75bbcc22aec370e6810b4c382d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d05d102efa2c9eb1d454519ceade8e11615a54a4a6a9f26f4883e2051aa27414(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dafc8c819a71b8bba3743ac1d1856e48dfcde0282939e418f00798f9c7c33fb8(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3436f23ae2ca4313aacb96519980906e71e5bc37e7a466a53353480f948e674(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5baf7a38335e2eb8733f2aa2d96a9593d774d095fb8a05dcf1d8bd22323050(
    *,
    eks_info: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnVirtualCluster.EksInfoProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19801d68aea5b7c69bfd60c7d9c690e62c4643fe80fcda956e884f367b8b1dcf(
    *,
    id: builtins.str,
    info: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnVirtualCluster.ContainerInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26be72236c14a8878e3d92d7b17397aa49c8a844f85e9e98c958600dd7a08c8f(
    *,
    namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f93ead2a436b8c5a2fc364fff5d9da849a851543aa1433cd7ab649d79d55f9(
    *,
    container_provider: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    security_configuration_id: typing.Optional[builtins.str] = None,
    session_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
