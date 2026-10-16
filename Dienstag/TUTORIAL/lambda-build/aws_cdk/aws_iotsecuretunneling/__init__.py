r'''
# AWS::IoTSecureTunneling Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotsecuretunneling as iotsecuretunneling
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTSecureTunneling construct libraries](https://constructs.dev/search?q=iotsecuretunneling)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTSecureTunneling resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTSecureTunneling.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTSecureTunneling](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTSecureTunneling.html).

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
    import aws_cdk.interfaces.aws_iotsecuretunneling as _aws_iotsecuretunneling_336f80ae
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_iotsecuretunneling_336f80ae = _LazyImport("aws_cdk.interfaces.aws_iotsecuretunneling")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_iotsecuretunneling_336f80ae.ITunnelRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnTunnel(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsecuretunneling.CfnTunnel",
):
    '''A connection between a source computer and a destination device using AWS IoT Secure Tunneling.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsecuretunneling-tunnel.html
    :cloudformationResource: AWS::IoTSecureTunneling::Tunnel
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsecuretunneling as iotsecuretunneling
        
        cfn_tunnel = iotsecuretunneling.CfnTunnel(self, "MyCfnTunnel",
            description="description",
            destination_config=iotsecuretunneling.CfnTunnel.DestinationConfigProperty(
                services=["services"],
        
                # the properties below are optional
                thing_name="thingName"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            timeout_config=iotsecuretunneling.CfnTunnel.TimeoutConfigProperty(
                max_lifetime_timeout_minutes=123
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        destination_config: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnTunnel.DestinationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        timeout_config: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnTunnel.TimeoutConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTSecureTunneling::Tunnel``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A short text description of the tunnel.
        :param destination_config: The destination configuration.
        :param tags: A collection of tag metadata.
        :param timeout_config: Tunnel timeout configuration.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__faceecd6060d5f5baa851579c3f27ddc08fca39e4c1dddb90976cd6cae1932f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTunnelProps(
            description=description,
            destination_config=destination_config,
            tags=tags,
            timeout_config=timeout_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForTunnel")
    @builtins.classmethod
    def arn_for_tunnel(
        cls,
        resource: "_aws_iotsecuretunneling_336f80ae.ITunnelRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4b50c8729525b091d8027c5879a144c0ba0333e6fcdb30d2c2544ae889794475)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForTunnel", [resource]))

    @jsii.member(jsii_name="isCfnTunnel")
    @builtins.classmethod
    def is_cfn_tunnel(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTunnel.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9c5f9ad8da06f8c4e90363208884472a94797c248815480d8f4b396eb9610b69)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTunnel", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8027a057a5a99a775ee43ecedf4ae683e7db1ba5ea22b09ba5d6d5029872d31e)
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
            type_hints = cached_type_hints(_typecheckingstub__9ba1f184a9cccd78b5cb62ec2a2df8972e7d993ad85302df60eff40de45deb22)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the tunnel.

        Valid values are OPEN and CLOSED.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTunnelArn")
    def attr_tunnel_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the tunnel.

        :cloudformationAttribute: TunnelArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTunnelArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTunnelId")
    def attr_tunnel_id(self) -> builtins.str:
        '''A unique alpha-numeric tunnel ID.

        :cloudformationAttribute: TunnelId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTunnelId"))

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
    @jsii.member(jsii_name="tunnelRef")
    def tunnel_ref(self) -> "_aws_iotsecuretunneling_336f80ae.TunnelReference":
        '''A reference to a Tunnel resource.'''
        return typing.cast("_aws_iotsecuretunneling_336f80ae.TunnelReference", jsii.get(self, "tunnelRef"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A short text description of the tunnel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__93cb9a326430a7dea1d996fcc0cb9946a8491062ca58889fbad511da7a5ceba7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.DestinationConfigProperty"]]:
        '''The destination configuration.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.DestinationConfigProperty"]], jsii.get(self, "destinationConfig"))

    @destination_config.setter
    def destination_config(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.DestinationConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__83251b635e4dd34ebc503bd1e88bc786f6fca7983e8c1ec26cdd12e213dd6f88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A collection of tag metadata.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__eaf5fe1414c62b6af9b1c4dbb6af35b4ba0a08863ded6cf2937942d4aafad9c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeoutConfig")
    def timeout_config(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.TimeoutConfigProperty"]]:
        '''Tunnel timeout configuration.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.TimeoutConfigProperty"]], jsii.get(self, "timeoutConfig"))

    @timeout_config.setter
    def timeout_config(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.TimeoutConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7335f4f23e532c657805ee877131847c988fe2b97db19094ded741c507fe4fe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutConfig", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsecuretunneling.CfnTunnel.DestinationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"services": "services", "thing_name": "thingName"},
    )
    class DestinationConfigProperty:
        def __init__(
            self,
            *,
            services: typing.Sequence[builtins.str],
            thing_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The destination configuration.

            :param services: A list of service names that identify the target application.
            :param thing_name: The name of the IoT thing to which you want to connect.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsecuretunneling-tunnel-destinationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsecuretunneling as iotsecuretunneling
                
                destination_config_property = iotsecuretunneling.CfnTunnel.DestinationConfigProperty(
                    services=["services"],
                
                    # the properties below are optional
                    thing_name="thingName"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__dbd02586430bd262e7c92241fe226b4e312e99a60b7ac39406844161b96d3542)
                check_type(argname="argument services", value=services, expected_type=type_hints["services"])
                check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "services": services,
            }
            if thing_name is not None:
                self._values["thing_name"] = thing_name

        @builtins.property
        def services(self) -> typing.List[builtins.str]:
            '''A list of service names that identify the target application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsecuretunneling-tunnel-destinationconfig.html#cfn-iotsecuretunneling-tunnel-destinationconfig-services
            '''
            result = self._values.get("services")
            assert result is not None, "Required property 'services' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def thing_name(self) -> typing.Optional[builtins.str]:
            '''The name of the IoT thing to which you want to connect.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsecuretunneling-tunnel-destinationconfig.html#cfn-iotsecuretunneling-tunnel-destinationconfig-thingname
            '''
            result = self._values.get("thing_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsecuretunneling.CfnTunnel.TimeoutConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"max_lifetime_timeout_minutes": "maxLifetimeTimeoutMinutes"},
    )
    class TimeoutConfigProperty:
        def __init__(
            self,
            *,
            max_lifetime_timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Tunnel timeout configuration.

            :param max_lifetime_timeout_minutes: The maximum amount of time (in minutes) a tunnel can remain open.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsecuretunneling-tunnel-timeoutconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsecuretunneling as iotsecuretunneling
                
                timeout_config_property = iotsecuretunneling.CfnTunnel.TimeoutConfigProperty(
                    max_lifetime_timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0e9cab7ca87e74bba124077741c1401bf6dc0e670d1279c144717c34dfda45ad)
                check_type(argname="argument max_lifetime_timeout_minutes", value=max_lifetime_timeout_minutes, expected_type=type_hints["max_lifetime_timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_lifetime_timeout_minutes is not None:
                self._values["max_lifetime_timeout_minutes"] = max_lifetime_timeout_minutes

        @builtins.property
        def max_lifetime_timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time (in minutes) a tunnel can remain open.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsecuretunneling-tunnel-timeoutconfig.html#cfn-iotsecuretunneling-tunnel-timeoutconfig-maxlifetimetimeoutminutes
            '''
            result = self._values.get("max_lifetime_timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeoutConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsecuretunneling.CfnTunnelProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "destination_config": "destinationConfig",
        "tags": "tags",
        "timeout_config": "timeoutConfig",
    },
)
class CfnTunnelProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        destination_config: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnTunnel.DestinationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        timeout_config: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnTunnel.TimeoutConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTunnel``.

        :param description: A short text description of the tunnel.
        :param destination_config: The destination configuration.
        :param tags: A collection of tag metadata.
        :param timeout_config: Tunnel timeout configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsecuretunneling-tunnel.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsecuretunneling as iotsecuretunneling
            
            cfn_tunnel_props = iotsecuretunneling.CfnTunnelProps(
                description="description",
                destination_config=iotsecuretunneling.CfnTunnel.DestinationConfigProperty(
                    services=["services"],
            
                    # the properties below are optional
                    thing_name="thingName"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                timeout_config=iotsecuretunneling.CfnTunnel.TimeoutConfigProperty(
                    max_lifetime_timeout_minutes=123
                )
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6ee4749bdc582a5cd68f4ad806b281254ef589144d2892e97313ed6f3a6ff536)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument destination_config", value=destination_config, expected_type=type_hints["destination_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout_config", value=timeout_config, expected_type=type_hints["timeout_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if destination_config is not None:
            self._values["destination_config"] = destination_config
        if tags is not None:
            self._values["tags"] = tags
        if timeout_config is not None:
            self._values["timeout_config"] = timeout_config

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A short text description of the tunnel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsecuretunneling-tunnel.html#cfn-iotsecuretunneling-tunnel-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_config(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.DestinationConfigProperty"]]:
        '''The destination configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsecuretunneling-tunnel.html#cfn-iotsecuretunneling-tunnel-destinationconfig
        '''
        result = self._values.get("destination_config")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.DestinationConfigProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''A collection of tag metadata.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsecuretunneling-tunnel.html#cfn-iotsecuretunneling-tunnel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def timeout_config(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.TimeoutConfigProperty"]]:
        '''Tunnel timeout configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsecuretunneling-tunnel.html#cfn-iotsecuretunneling-tunnel-timeoutconfig
        '''
        result = self._values.get("timeout_config")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnTunnel.TimeoutConfigProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTunnelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnTunnel",
    "CfnTunnelProps",
]

publication.publish()

def _typecheckingstub__faceecd6060d5f5baa851579c3f27ddc08fca39e4c1dddb90976cd6cae1932f4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    destination_config: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnTunnel.DestinationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_config: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnTunnel.TimeoutConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b50c8729525b091d8027c5879a144c0ba0333e6fcdb30d2c2544ae889794475(
    resource: _aws_iotsecuretunneling_336f80ae.ITunnelRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c5f9ad8da06f8c4e90363208884472a94797c248815480d8f4b396eb9610b69(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8027a057a5a99a775ee43ecedf4ae683e7db1ba5ea22b09ba5d6d5029872d31e(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba1f184a9cccd78b5cb62ec2a2df8972e7d993ad85302df60eff40de45deb22(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93cb9a326430a7dea1d996fcc0cb9946a8491062ca58889fbad511da7a5ceba7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83251b635e4dd34ebc503bd1e88bc786f6fca7983e8c1ec26cdd12e213dd6f88(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnTunnel.DestinationConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaf5fe1414c62b6af9b1c4dbb6af35b4ba0a08863ded6cf2937942d4aafad9c2(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7335f4f23e532c657805ee877131847c988fe2b97db19094ded741c507fe4fe9(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnTunnel.TimeoutConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd02586430bd262e7c92241fe226b4e312e99a60b7ac39406844161b96d3542(
    *,
    services: typing.Sequence[builtins.str],
    thing_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e9cab7ca87e74bba124077741c1401bf6dc0e670d1279c144717c34dfda45ad(
    *,
    max_lifetime_timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee4749bdc582a5cd68f4ad806b281254ef589144d2892e97313ed6f3a6ff536(
    *,
    description: typing.Optional[builtins.str] = None,
    destination_config: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnTunnel.DestinationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_config: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnTunnel.TimeoutConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
