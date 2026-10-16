r'''
# AWS::NetworkFlowMonitor Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_networkflowmonitor as networkflowmonitor
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NetworkFlowMonitor construct libraries](https://constructs.dev/search?q=networkflowmonitor)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NetworkFlowMonitor resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkFlowMonitor.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NetworkFlowMonitor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkFlowMonitor.html).

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
    import aws_cdk.interfaces.aws_networkflowmonitor as _aws_networkflowmonitor_dc43c334
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_networkflowmonitor_dc43c334 = _LazyImport("aws_cdk.interfaces.aws_networkflowmonitor")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_networkflowmonitor_dc43c334.IMonitorRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnMonitor(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnMonitor",
):
    '''Creates a monitor for specific network flows between local and remote resources to monitor network performance for workloads.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-monitor.html
    :cloudformationResource: AWS::NetworkFlowMonitor::Monitor
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkflowmonitor as networkflowmonitor
        
        cfn_monitor = networkflowmonitor.CfnMonitor(self, "MyCfnMonitor",
            local_resources=[networkflowmonitor.CfnMonitor.MonitorLocalResourceProperty(
                identifier="identifier",
                type="type"
            )],
            monitor_name="monitorName",
        
            # the properties below are optional
            remote_resources=[networkflowmonitor.CfnMonitor.MonitorRemoteResourceProperty(
                identifier="identifier",
                type="type"
            )],
            scope_arn="scopeArn",
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
        local_resources: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMonitor.MonitorLocalResourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        monitor_name: builtins.str,
        remote_resources: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMonitor.MonitorRemoteResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        scope_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkFlowMonitor::Monitor``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param local_resources: The local resources to monitor.
        :param monitor_name: The name of the monitor.
        :param remote_resources: The remote resources to monitor.
        :param scope_arn: The Amazon Resource Name (ARN) of the scope for the monitor.
        :param tags: The tags for the monitor.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0c78480b0628ac116a71cd6dd5cf146cb444871811c16cef23ddf4be09f86c5f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMonitorProps(
            local_resources=local_resources,
            monitor_name=monitor_name,
            remote_resources=remote_resources,
            scope_arn=scope_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForMonitor")
    @builtins.classmethod
    def arn_for_monitor(
        cls,
        resource: "_aws_networkflowmonitor_dc43c334.IMonitorRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aa115ff6e30a814d81e0a6c4e3baf288aece89dfe807d2c4df44fd0f7f2d9920)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForMonitor", [resource]))

    @jsii.member(jsii_name="isCfnMonitor")
    @builtins.classmethod
    def is_cfn_monitor(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnMonitor.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e142d71bd35fe4ad7b75393bdf4c0b02964bdd7824140ffe690da6e65551d644)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnMonitor", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__650cc04a8d186c8d7d7e6be41333dde038387cdd609ce123a06f8f4822273131)
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
            type_hints = cached_type_hints(_typecheckingstub__050c5c7837ef0b8c4c7d89c5be5e43dc2e120ebf3d9919615a89d00a82a2d9e6)
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
        '''The Amazon Resource Name (ARN) of the monitor.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time when the monitor was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''The date and time when the monitor was last modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrMonitorStatus")
    def attr_monitor_status(self) -> builtins.str:
        '''The status of the monitor.

        :cloudformationAttribute: MonitorStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMonitorStatus"))

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
    @jsii.member(jsii_name="monitorRef")
    def monitor_ref(self) -> "_aws_networkflowmonitor_dc43c334.MonitorReference":
        '''A reference to a Monitor resource.'''
        return typing.cast("_aws_networkflowmonitor_dc43c334.MonitorReference", jsii.get(self, "monitorRef"))

    @builtins.property
    @jsii.member(jsii_name="localResources")
    def local_resources(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorLocalResourceProperty"]]]:
        '''The local resources to monitor.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorLocalResourceProperty"]]], jsii.get(self, "localResources"))

    @local_resources.setter
    def local_resources(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorLocalResourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6233cbd9810e0b715510025cae76f9402639117e6b198d1734d70f117483cc34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localResources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="monitorName")
    def monitor_name(self) -> builtins.str:
        '''The name of the monitor.'''
        return typing.cast(builtins.str, jsii.get(self, "monitorName"))

    @monitor_name.setter
    def monitor_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9a962683b28941b0269643216e55bc7b4ed15136dc2a2a56b71973930ce0a2b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="remoteResources")
    def remote_resources(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorRemoteResourceProperty"]]]]:
        '''The remote resources to monitor.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorRemoteResourceProperty"]]]], jsii.get(self, "remoteResources"))

    @remote_resources.setter
    def remote_resources(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorRemoteResourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fe55d218c1a3e1060b77730feb2fe5ee6972eecd325005a96d6ea585ba365082)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteResources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scopeArn")
    def scope_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the scope for the monitor.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeArn"))

    @scope_arn.setter
    def scope_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__05b8ae09fc15f836ebbb6f8bb4d42b88d6a06c63659ceaef56a4dc98da1cf02b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the monitor.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__75a6ab8f7d617cdcd7f3478b8338d995b686397bdca099639734e5a38bca9b08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnMonitor.MonitorLocalResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"identifier": "identifier", "type": "type"},
    )
    class MonitorLocalResourceProperty:
        def __init__(self, *, identifier: builtins.str, type: builtins.str) -> None:
            '''A local resource is the host where the agent is installed.

            :param identifier: The identifier of the local resource.
            :param type: The type of the local resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-monitor-monitorlocalresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkflowmonitor as networkflowmonitor
                
                monitor_local_resource_property = networkflowmonitor.CfnMonitor.MonitorLocalResourceProperty(
                    identifier="identifier",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__de6c604c043758f5e32e6792726b519a294a6a702e101fcd006dea87ff834268)
                check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "identifier": identifier,
                "type": type,
            }

        @builtins.property
        def identifier(self) -> builtins.str:
            '''The identifier of the local resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-monitor-monitorlocalresource.html#cfn-networkflowmonitor-monitor-monitorlocalresource-identifier
            '''
            result = self._values.get("identifier")
            assert result is not None, "Required property 'identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the local resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-monitor-monitorlocalresource.html#cfn-networkflowmonitor-monitor-monitorlocalresource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitorLocalResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnMonitor.MonitorRemoteResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"identifier": "identifier", "type": "type"},
    )
    class MonitorRemoteResourceProperty:
        def __init__(self, *, identifier: builtins.str, type: builtins.str) -> None:
            '''A remote resource is the other endpoint in a network flow.

            :param identifier: The identifier of the remote resource.
            :param type: The type of the remote resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-monitor-monitorremoteresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkflowmonitor as networkflowmonitor
                
                monitor_remote_resource_property = networkflowmonitor.CfnMonitor.MonitorRemoteResourceProperty(
                    identifier="identifier",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__69cb74d6880cd96411d08ec1b25359027497d64be67fd3b722293020e668e2c0)
                check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "identifier": identifier,
                "type": type,
            }

        @builtins.property
        def identifier(self) -> builtins.str:
            '''The identifier of the remote resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-monitor-monitorremoteresource.html#cfn-networkflowmonitor-monitor-monitorremoteresource-identifier
            '''
            result = self._values.get("identifier")
            assert result is not None, "Required property 'identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the remote resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-monitor-monitorremoteresource.html#cfn-networkflowmonitor-monitor-monitorremoteresource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitorRemoteResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnMonitorProps",
    jsii_struct_bases=[],
    name_mapping={
        "local_resources": "localResources",
        "monitor_name": "monitorName",
        "remote_resources": "remoteResources",
        "scope_arn": "scopeArn",
        "tags": "tags",
    },
)
class CfnMonitorProps:
    def __init__(
        self,
        *,
        local_resources: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMonitor.MonitorLocalResourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        monitor_name: builtins.str,
        remote_resources: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnMonitor.MonitorRemoteResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        scope_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMonitor``.

        :param local_resources: The local resources to monitor.
        :param monitor_name: The name of the monitor.
        :param remote_resources: The remote resources to monitor.
        :param scope_arn: The Amazon Resource Name (ARN) of the scope for the monitor.
        :param tags: The tags for the monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-monitor.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkflowmonitor as networkflowmonitor
            
            cfn_monitor_props = networkflowmonitor.CfnMonitorProps(
                local_resources=[networkflowmonitor.CfnMonitor.MonitorLocalResourceProperty(
                    identifier="identifier",
                    type="type"
                )],
                monitor_name="monitorName",
            
                # the properties below are optional
                remote_resources=[networkflowmonitor.CfnMonitor.MonitorRemoteResourceProperty(
                    identifier="identifier",
                    type="type"
                )],
                scope_arn="scopeArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aaba5e9a617d9e5a70c634c1390669ebe7b339723a3f91b2ee9cd1539b08f615)
            check_type(argname="argument local_resources", value=local_resources, expected_type=type_hints["local_resources"])
            check_type(argname="argument monitor_name", value=monitor_name, expected_type=type_hints["monitor_name"])
            check_type(argname="argument remote_resources", value=remote_resources, expected_type=type_hints["remote_resources"])
            check_type(argname="argument scope_arn", value=scope_arn, expected_type=type_hints["scope_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "local_resources": local_resources,
            "monitor_name": monitor_name,
        }
        if remote_resources is not None:
            self._values["remote_resources"] = remote_resources
        if scope_arn is not None:
            self._values["scope_arn"] = scope_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def local_resources(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorLocalResourceProperty"]]]:
        '''The local resources to monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-monitor.html#cfn-networkflowmonitor-monitor-localresources
        '''
        result = self._values.get("local_resources")
        assert result is not None, "Required property 'local_resources' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorLocalResourceProperty"]]], result)

    @builtins.property
    def monitor_name(self) -> builtins.str:
        '''The name of the monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-monitor.html#cfn-networkflowmonitor-monitor-monitorname
        '''
        result = self._values.get("monitor_name")
        assert result is not None, "Required property 'monitor_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remote_resources(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorRemoteResourceProperty"]]]]:
        '''The remote resources to monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-monitor.html#cfn-networkflowmonitor-monitor-remoteresources
        '''
        result = self._values.get("remote_resources")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnMonitor.MonitorRemoteResourceProperty"]]]], result)

    @builtins.property
    def scope_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the scope for the monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-monitor.html#cfn-networkflowmonitor-monitor-scopearn
        '''
        result = self._values.get("scope_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-monitor.html#cfn-networkflowmonitor-monitor-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMonitorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_networkflowmonitor_dc43c334.IScopeRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnScope(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnScope",
):
    '''Resource Type definition for AWS::NetworkFlowMonitor::Scope.

    Creates a scope to define the resources that Network Flow Monitor monitors for network performance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-scope.html
    :cloudformationResource: AWS::NetworkFlowMonitor::Scope
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkflowmonitor as networkflowmonitor
        
        cfn_scope = networkflowmonitor.CfnScope(self, "MyCfnScope",
            targets=[networkflowmonitor.CfnScope.TargetResourceProperty(
                region="region",
                target_identifier=networkflowmonitor.CfnScope.TargetIdentifierProperty(
                    target_id=networkflowmonitor.CfnScope.TargetIdProperty(
                        account_id="accountId"
                    ),
                    target_type="targetType"
                )
            )],
        
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
        targets: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnScope.TargetResourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkFlowMonitor::Scope``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param targets: The targets for the scope.
        :param tags: The tags for the scope.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f7120895ccab0dd04a503d7dbdffb480e2de7e49eb0a3d237462ed44e74371d5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScopeProps(targets=targets, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForScope")
    @builtins.classmethod
    def arn_for_scope(
        cls,
        resource: "_aws_networkflowmonitor_dc43c334.IScopeRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__82d5da986e1c56b77948bcc6ff72245eb7c3e3f18753236fc1a7e6831b7f521b)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForScope", [resource]))

    @jsii.member(jsii_name="isCfnScope")
    @builtins.classmethod
    def is_cfn_scope(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnScope.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6dd519a6ecf86da703555985f589ddaec6c87cf598b53e379feee0d30f1972e6)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnScope", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7b6ceaed5ca64cf615c59f112548904727c225e68be81d71a5cbf8df949914ec)
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
            type_hints = cached_type_hints(_typecheckingstub__0a877ad202408faba65fe4cf00da49ca6b2cf6cf94901ed36b448049edd8cb04)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrScopeArn")
    def attr_scope_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the scope.

        :cloudformationAttribute: ScopeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScopeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrScopeId")
    def attr_scope_id(self) -> builtins.str:
        '''The identifier for the scope.

        :cloudformationAttribute: ScopeId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScopeId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the scope.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="scopeRef")
    def scope_ref(self) -> "_aws_networkflowmonitor_dc43c334.ScopeReference":
        '''A reference to a Scope resource.'''
        return typing.cast("_aws_networkflowmonitor_dc43c334.ScopeReference", jsii.get(self, "scopeRef"))

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetResourceProperty"]]]:
        '''The targets for the scope.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetResourceProperty"]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetResourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bbf6606bfaba1b18e072cde1af4217f25ea4696e754d35ce9fe6a6247d2dcd9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the scope.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c4dcbae5a5109fbaa3520c62631ac2b7b2a956d8fde01a74890684675a1392cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnScope.TargetIdProperty",
        jsii_struct_bases=[],
        name_mapping={"account_id": "accountId"},
    )
    class TargetIdProperty:
        def __init__(self, *, account_id: builtins.str) -> None:
            '''A target ID is an internally-generated identifier for a target.

            :param account_id: The account ID for the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-scope-targetid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkflowmonitor as networkflowmonitor
                
                target_id_property = networkflowmonitor.CfnScope.TargetIdProperty(
                    account_id="accountId"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2e5264ec5cb57c104aba370fc7876b78547ef988894beb1833b41963cd6eebb3)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_id": account_id,
            }

        @builtins.property
        def account_id(self) -> builtins.str:
            '''The account ID for the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-scope-targetid.html#cfn-networkflowmonitor-scope-targetid-accountid
            '''
            result = self._values.get("account_id")
            assert result is not None, "Required property 'account_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnScope.TargetIdentifierProperty",
        jsii_struct_bases=[],
        name_mapping={"target_id": "targetId", "target_type": "targetType"},
    )
    class TargetIdentifierProperty:
        def __init__(
            self,
            *,
            target_id: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnScope.TargetIdProperty", typing.Dict[builtins.str, typing.Any]]],
            target_type: builtins.str,
        ) -> None:
            '''A target identifier is a pair of identifying information for a scope target.

            :param target_id: A target ID is an internally-generated identifier for a target.
            :param target_type: The type of the target. Currently always ACCOUNT.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-scope-targetidentifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkflowmonitor as networkflowmonitor
                
                target_identifier_property = networkflowmonitor.CfnScope.TargetIdentifierProperty(
                    target_id=networkflowmonitor.CfnScope.TargetIdProperty(
                        account_id="accountId"
                    ),
                    target_type="targetType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d80d0f78ae30a91c7e9facfb5eaae8b4b481ab1306fdbb510637971a7ee8d00d)
                check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
                check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_id": target_id,
                "target_type": target_type,
            }

        @builtins.property
        def target_id(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetIdProperty"]:
            '''A target ID is an internally-generated identifier for a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-scope-targetidentifier.html#cfn-networkflowmonitor-scope-targetidentifier-targetid
            '''
            result = self._values.get("target_id")
            assert result is not None, "Required property 'target_id' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetIdProperty"], result)

        @builtins.property
        def target_type(self) -> builtins.str:
            '''The type of the target.

            Currently always ACCOUNT.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-scope-targetidentifier.html#cfn-networkflowmonitor-scope-targetidentifier-targettype
            '''
            result = self._values.get("target_type")
            assert result is not None, "Required property 'target_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetIdentifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnScope.TargetResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"region": "region", "target_identifier": "targetIdentifier"},
    )
    class TargetResourceProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            target_identifier: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnScope.TargetIdentifierProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A target resource in a scope, identified by a Region and target identifier.

            :param region: The AWS Region for the target resource.
            :param target_identifier: A target identifier is a pair of identifying information for a scope target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-scope-targetresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkflowmonitor as networkflowmonitor
                
                target_resource_property = networkflowmonitor.CfnScope.TargetResourceProperty(
                    region="region",
                    target_identifier=networkflowmonitor.CfnScope.TargetIdentifierProperty(
                        target_id=networkflowmonitor.CfnScope.TargetIdProperty(
                            account_id="accountId"
                        ),
                        target_type="targetType"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__b5d950c901a742149b496086ca034e6b12e9174adc2fbc4f4cbc53070ab44f79)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument target_identifier", value=target_identifier, expected_type=type_hints["target_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
                "target_identifier": target_identifier,
            }

        @builtins.property
        def region(self) -> builtins.str:
            '''The AWS Region for the target resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-scope-targetresource.html#cfn-networkflowmonitor-scope-targetresource-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_identifier(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetIdentifierProperty"]:
            '''A target identifier is a pair of identifying information for a scope target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkflowmonitor-scope-targetresource.html#cfn-networkflowmonitor-scope-targetresource-targetidentifier
            '''
            result = self._values.get("target_identifier")
            assert result is not None, "Required property 'target_identifier' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetIdentifierProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkflowmonitor.CfnScopeProps",
    jsii_struct_bases=[],
    name_mapping={"targets": "targets", "tags": "tags"},
)
class CfnScopeProps:
    def __init__(
        self,
        *,
        targets: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnScope.TargetResourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScope``.

        :param targets: The targets for the scope.
        :param tags: The tags for the scope.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-scope.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkflowmonitor as networkflowmonitor
            
            cfn_scope_props = networkflowmonitor.CfnScopeProps(
                targets=[networkflowmonitor.CfnScope.TargetResourceProperty(
                    region="region",
                    target_identifier=networkflowmonitor.CfnScope.TargetIdentifierProperty(
                        target_id=networkflowmonitor.CfnScope.TargetIdProperty(
                            account_id="accountId"
                        ),
                        target_type="targetType"
                    )
                )],
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bf66d8316767fa3789d879ba26556cd15742c3b75e4b9e6d402cf13b74e72242)
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "targets": targets,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def targets(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetResourceProperty"]]]:
        '''The targets for the scope.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-scope.html#cfn-networkflowmonitor-scope-targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnScope.TargetResourceProperty"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags for the scope.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkflowmonitor-scope.html#cfn-networkflowmonitor-scope-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScopeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMonitor",
    "CfnMonitorProps",
    "CfnScope",
    "CfnScopeProps",
]

publication.publish()

def _typecheckingstub__0c78480b0628ac116a71cd6dd5cf146cb444871811c16cef23ddf4be09f86c5f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    local_resources: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMonitor.MonitorLocalResourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    monitor_name: builtins.str,
    remote_resources: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMonitor.MonitorRemoteResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    scope_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa115ff6e30a814d81e0a6c4e3baf288aece89dfe807d2c4df44fd0f7f2d9920(
    resource: _aws_networkflowmonitor_dc43c334.IMonitorRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e142d71bd35fe4ad7b75393bdf4c0b02964bdd7824140ffe690da6e65551d644(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__650cc04a8d186c8d7d7e6be41333dde038387cdd609ce123a06f8f4822273131(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__050c5c7837ef0b8c4c7d89c5be5e43dc2e120ebf3d9919615a89d00a82a2d9e6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6233cbd9810e0b715510025cae76f9402639117e6b198d1734d70f117483cc34(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnMonitor.MonitorLocalResourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a962683b28941b0269643216e55bc7b4ed15136dc2a2a56b71973930ce0a2b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe55d218c1a3e1060b77730feb2fe5ee6972eecd325005a96d6ea585ba365082(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnMonitor.MonitorRemoteResourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b8ae09fc15f836ebbb6f8bb4d42b88d6a06c63659ceaef56a4dc98da1cf02b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a6ab8f7d617cdcd7f3478b8338d995b686397bdca099639734e5a38bca9b08(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6c604c043758f5e32e6792726b519a294a6a702e101fcd006dea87ff834268(
    *,
    identifier: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69cb74d6880cd96411d08ec1b25359027497d64be67fd3b722293020e668e2c0(
    *,
    identifier: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaba5e9a617d9e5a70c634c1390669ebe7b339723a3f91b2ee9cd1539b08f615(
    *,
    local_resources: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMonitor.MonitorLocalResourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    monitor_name: builtins.str,
    remote_resources: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnMonitor.MonitorRemoteResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    scope_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7120895ccab0dd04a503d7dbdffb480e2de7e49eb0a3d237462ed44e74371d5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    targets: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnScope.TargetResourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82d5da986e1c56b77948bcc6ff72245eb7c3e3f18753236fc1a7e6831b7f521b(
    resource: _aws_networkflowmonitor_dc43c334.IScopeRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd519a6ecf86da703555985f589ddaec6c87cf598b53e379feee0d30f1972e6(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b6ceaed5ca64cf615c59f112548904727c225e68be81d71a5cbf8df949914ec(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a877ad202408faba65fe4cf00da49ca6b2cf6cf94901ed36b448049edd8cb04(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf6606bfaba1b18e072cde1af4217f25ea4696e754d35ce9fe6a6247d2dcd9b(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnScope.TargetResourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4dcbae5a5109fbaa3520c62631ac2b7b2a956d8fde01a74890684675a1392cf(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5264ec5cb57c104aba370fc7876b78547ef988894beb1833b41963cd6eebb3(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d80d0f78ae30a91c7e9facfb5eaae8b4b481ab1306fdbb510637971a7ee8d00d(
    *,
    target_id: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnScope.TargetIdProperty, typing.Dict[builtins.str, typing.Any]]],
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5d950c901a742149b496086ca034e6b12e9174adc2fbc4f4cbc53070ab44f79(
    *,
    region: builtins.str,
    target_identifier: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnScope.TargetIdentifierProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf66d8316767fa3789d879ba26556cd15742c3b75e4b9e6d402cf13b74e72242(
    *,
    targets: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnScope.TargetResourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
