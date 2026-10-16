r'''
# AWS::MediaTailor Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mediatailor as mediatailor
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MediaTailor construct libraries](https://constructs.dev/search?q=mediatailor)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MediaTailor resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaTailor.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MediaTailor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaTailor.html).

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
    import aws_cdk.interfaces.aws_mediatailor as _aws_mediatailor_60404695
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_mediatailor_60404695 = _LazyImport("aws_cdk.interfaces.aws_mediatailor")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_mediatailor_60404695.IChannelRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnChannel(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannel",
):
    '''The configuration parameters for a channel.

    For information about MediaTailor channels, see `Working with channels <https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html>`_ in the *MediaTailor User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html
    :cloudformationResource: AWS::MediaTailor::Channel
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        cfn_channel = mediatailor.CfnChannel(self, "MyCfnChannel",
            channel_name="channelName",
            outputs=[mediatailor.CfnChannel.RequestOutputItemProperty(
                manifest_name="manifestName",
                source_group="sourceGroup",
        
                # the properties below are optional
                dash_playlist_settings=mediatailor.CfnChannel.DashPlaylistSettingsProperty(
                    manifest_window_seconds=123,
                    min_buffer_time_seconds=123,
                    min_update_period_seconds=123,
                    suggested_presentation_delay_seconds=123
                ),
                hls_playlist_settings=mediatailor.CfnChannel.HlsPlaylistSettingsProperty(
                    ad_markup_type=["adMarkupType"],
                    manifest_window_seconds=123
                )
            )],
            playback_mode="playbackMode",
        
            # the properties below are optional
            audiences=["audiences"],
            filler_slate=mediatailor.CfnChannel.SlateSourceProperty(
                source_location_name="sourceLocationName",
                vod_source_name="vodSourceName"
            ),
            log_configuration=mediatailor.CfnChannel.LogConfigurationForChannelProperty(
                log_types=["logTypes"]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            tier="tier",
            time_shift_configuration=mediatailor.CfnChannel.TimeShiftConfigurationProperty(
                max_time_delay_seconds=123
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        channel_name: builtins.str,
        outputs: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.RequestOutputItemProperty", typing.Dict[builtins.str, typing.Any]]]]],
        playback_mode: builtins.str,
        audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        filler_slate: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.SlateSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.LogConfigurationForChannelProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        tier: typing.Optional[builtins.str] = None,
        time_shift_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.TimeShiftConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::Channel``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_name: The name of the channel.
        :param outputs: The channel's output properties.
        :param playback_mode: The type of playback mode for this channel. ``LINEAR`` - Programs play back-to-back only once. ``LOOP`` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.
        :param audiences: The list of audiences defined in channel.
        :param filler_slate: The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the ``LINEAR`` ``PlaybackMode`` . MediaTailor doesn't support filler slate for channels using the ``LOOP`` ``PlaybackMode`` .
        :param log_configuration: The log configuration.
        :param tags: The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .
        :param tier: The tier for this channel. STANDARD tier channels can contain live programs.
        :param time_shift_configuration: The configuration for time-shifted viewing.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__95afc802641850838d7d754c58072c279165a93bff5fc055789c1090a21b9714)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelProps(
            channel_name=channel_name,
            outputs=outputs,
            playback_mode=playback_mode,
            audiences=audiences,
            filler_slate=filler_slate,
            log_configuration=log_configuration,
            tags=tags,
            tier=tier,
            time_shift_configuration=time_shift_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForChannel")
    @builtins.classmethod
    def arn_for_channel(
        cls,
        resource: "_aws_mediatailor_60404695.IChannelRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__418fb2485d366f3c8a7b8a95c0dcf780cd3d97d1eacd74f40d7d10b930f2ab95)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForChannel", [resource]))

    @jsii.member(jsii_name="fromChannelArn")
    @builtins.classmethod
    def from_channel_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_aws_mediatailor_60404695.IChannelRef":
        '''Creates a new IChannelRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4d19144d331ba31edd24b53fe62ecd68291785594e4276f682970808562a8790)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_aws_mediatailor_60404695.IChannelRef", jsii.sinvoke(cls, "fromChannelArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromChannelName")
    @builtins.classmethod
    def from_channel_name(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        channel_name: builtins.str,
    ) -> "_aws_mediatailor_60404695.IChannelRef":
        '''Creates a new IChannelRef from a channelName.

        :param scope: -
        :param id: -
        :param channel_name: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__08ab9dccb4a244c93c8642dce766e1e9ee544479257409b787228df15d5435d7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
        return typing.cast("_aws_mediatailor_60404695.IChannelRef", jsii.sinvoke(cls, "fromChannelName", [scope, id, channel_name]))

    @jsii.member(jsii_name="isCfnChannel")
    @builtins.classmethod
    def is_cfn_channel(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnChannel.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b40a7b4e84fbe554602e7462685b4c9b4a1175e608e5fd8e878b86fe361400ea)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnChannel", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d632b023994803b26caa2590748766e0dabab5ba299874fe587fa9f37c926bda)
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
            type_hints = cached_type_hints(_typecheckingstub__fd05180cbc64f9ab36b59c9143ba4df4683bae47e98fe90c0d0bacdd9fbb8fae)
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
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "_aws_mediatailor_60404695.ChannelReference":
        '''A reference to a Channel resource.'''
        return typing.cast("_aws_mediatailor_60404695.ChannelReference", jsii.get(self, "channelRef"))

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        '''The name of the channel.'''
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__414356f19e6a1e142f58fb20d5aa3f44fd76f93ad6f9a944f9177c71e65bd031)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.RequestOutputItemProperty"]]]:
        '''The channel's output properties.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.RequestOutputItemProperty"]]], jsii.get(self, "outputs"))

    @outputs.setter
    def outputs(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.RequestOutputItemProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f6c205b75797f1a6f80dab721b03fc96335f8bd384f7c63aab656bd3136a90ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="playbackMode")
    def playback_mode(self) -> builtins.str:
        '''The type of playback mode for this channel.'''
        return typing.cast(builtins.str, jsii.get(self, "playbackMode"))

    @playback_mode.setter
    def playback_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0f01c3b2a4d663235632876690f021c08885e2683808fd8f8354ec563a6cdbcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "playbackMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="audiences")
    def audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of audiences defined in channel.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "audiences"))

    @audiences.setter
    def audiences(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__978734f277fe2347cb97632bb681ac7a90ce350df65be207f74234337bd3d49b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audiences", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fillerSlate")
    def filler_slate(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.SlateSourceProperty"]]:
        '''The slate used to fill gaps between programs in the schedule.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.SlateSourceProperty"]], jsii.get(self, "fillerSlate"))

    @filler_slate.setter
    def filler_slate(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.SlateSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bb99598f2b90f05f74078bf9dbab5d32c9f963ec0c7f60fc84c741cd7f7a72d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fillerSlate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.LogConfigurationForChannelProperty"]]:
        '''The log configuration.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.LogConfigurationForChannelProperty"]], jsii.get(self, "logConfiguration"))

    @log_configuration.setter
    def log_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.LogConfigurationForChannelProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__272cdcfa3dd55bace9d7517c474b5f20801108c57ec19149b84a6595215b1252)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags to assign to the channel.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3bde4918e4d23e04040b87adfc6739660dba537c84b0ca2f813daacbf009f298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> typing.Optional[builtins.str]:
        '''The tier for this channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__35198b30b0429365e601c60c11c6bb80791a3176a301d1fac563832c0e0edd38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeShiftConfiguration")
    def time_shift_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.TimeShiftConfigurationProperty"]]:
        '''The configuration for time-shifted viewing.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.TimeShiftConfigurationProperty"]], jsii.get(self, "timeShiftConfiguration"))

    @time_shift_configuration.setter
    def time_shift_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.TimeShiftConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5b3c40cad99c53a2773855f4cd98f257598efcf21fd51b6bb734064a33f180c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeShiftConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannel.DashPlaylistSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_window_seconds": "manifestWindowSeconds",
            "min_buffer_time_seconds": "minBufferTimeSeconds",
            "min_update_period_seconds": "minUpdatePeriodSeconds",
            "suggested_presentation_delay_seconds": "suggestedPresentationDelaySeconds",
        },
    )
    class DashPlaylistSettingsProperty:
        def __init__(
            self,
            *,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
            min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
            min_update_period_seconds: typing.Optional[jsii.Number] = None,
            suggested_presentation_delay_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Dash manifest configuration parameters.

            :param manifest_window_seconds: The total duration (in seconds) of each manifest. Minimum value: ``30`` seconds. Maximum value: ``3600`` seconds.
            :param min_buffer_time_seconds: Minimum amount of content (measured in seconds) that a player must keep available in the buffer. Minimum value: ``2`` seconds. Maximum value: ``60`` seconds.
            :param min_update_period_seconds: Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest. Minimum value: ``2`` seconds. Maximum value: ``60`` seconds.
            :param suggested_presentation_delay_seconds: Amount of time (in seconds) that the player should be from the live point at the end of the manifest. Minimum value: ``2`` seconds. Maximum value: ``60`` seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                dash_playlist_settings_property = mediatailor.CfnChannel.DashPlaylistSettingsProperty(
                    manifest_window_seconds=123,
                    min_buffer_time_seconds=123,
                    min_update_period_seconds=123,
                    suggested_presentation_delay_seconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e53b76fce032c9b5b0b3ab03b03ec40f7f01e061c77ffbd9e3b0101056eecfb5)
                check_type(argname="argument manifest_window_seconds", value=manifest_window_seconds, expected_type=type_hints["manifest_window_seconds"])
                check_type(argname="argument min_buffer_time_seconds", value=min_buffer_time_seconds, expected_type=type_hints["min_buffer_time_seconds"])
                check_type(argname="argument min_update_period_seconds", value=min_update_period_seconds, expected_type=type_hints["min_update_period_seconds"])
                check_type(argname="argument suggested_presentation_delay_seconds", value=suggested_presentation_delay_seconds, expected_type=type_hints["suggested_presentation_delay_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds
            if min_buffer_time_seconds is not None:
                self._values["min_buffer_time_seconds"] = min_buffer_time_seconds
            if min_update_period_seconds is not None:
                self._values["min_update_period_seconds"] = min_update_period_seconds
            if suggested_presentation_delay_seconds is not None:
                self._values["suggested_presentation_delay_seconds"] = suggested_presentation_delay_seconds

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''The total duration (in seconds) of each manifest.

            Minimum value: ``30`` seconds. Maximum value: ``3600`` seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html#cfn-mediatailor-channel-dashplaylistsettings-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_buffer_time_seconds(self) -> typing.Optional[jsii.Number]:
            '''Minimum amount of content (measured in seconds) that a player must keep available in the buffer.

            Minimum value: ``2`` seconds. Maximum value: ``60`` seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html#cfn-mediatailor-channel-dashplaylistsettings-minbuffertimeseconds
            '''
            result = self._values.get("min_buffer_time_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_update_period_seconds(self) -> typing.Optional[jsii.Number]:
            '''Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.

            Minimum value: ``2`` seconds. Maximum value: ``60`` seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html#cfn-mediatailor-channel-dashplaylistsettings-minupdateperiodseconds
            '''
            result = self._values.get("min_update_period_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def suggested_presentation_delay_seconds(self) -> typing.Optional[jsii.Number]:
            '''Amount of time (in seconds) that the player should be from the live point at the end of the manifest.

            Minimum value: ``2`` seconds. Maximum value: ``60`` seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html#cfn-mediatailor-channel-dashplaylistsettings-suggestedpresentationdelayseconds
            '''
            result = self._values.get("suggested_presentation_delay_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashPlaylistSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannel.HlsPlaylistSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_markup_type": "adMarkupType",
            "manifest_window_seconds": "manifestWindowSeconds",
        },
    )
    class HlsPlaylistSettingsProperty:
        def __init__(
            self,
            *,
            ad_markup_type: typing.Optional[typing.Sequence[builtins.str]] = None,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''HLS playlist configuration parameters.

            :param ad_markup_type: Determines the type of SCTE 35 tags to use in ad markup. Specify ``DATERANGE`` to use ``DATERANGE`` tags (for live or VOD content). Specify ``SCTE35_ENHANCED`` to use ``EXT-X-CUE-OUT`` and ``EXT-X-CUE-IN`` tags (for VOD content only).
            :param manifest_window_seconds: The total duration (in seconds) of each manifest. Minimum value: ``30`` seconds. Maximum value: ``3600`` seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-hlsplaylistsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                hls_playlist_settings_property = mediatailor.CfnChannel.HlsPlaylistSettingsProperty(
                    ad_markup_type=["adMarkupType"],
                    manifest_window_seconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e31cc39cb17d92681c3726ed02355f545c95afa6883032b1e93af1c43179acc2)
                check_type(argname="argument ad_markup_type", value=ad_markup_type, expected_type=type_hints["ad_markup_type"])
                check_type(argname="argument manifest_window_seconds", value=manifest_window_seconds, expected_type=type_hints["manifest_window_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_markup_type is not None:
                self._values["ad_markup_type"] = ad_markup_type
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds

        @builtins.property
        def ad_markup_type(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Determines the type of SCTE 35 tags to use in ad markup.

            Specify ``DATERANGE`` to use ``DATERANGE`` tags (for live or VOD content). Specify ``SCTE35_ENHANCED`` to use ``EXT-X-CUE-OUT`` and ``EXT-X-CUE-IN`` tags (for VOD content only).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-hlsplaylistsettings.html#cfn-mediatailor-channel-hlsplaylistsettings-admarkuptype
            '''
            result = self._values.get("ad_markup_type")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''The total duration (in seconds) of each manifest.

            Minimum value: ``30`` seconds. Maximum value: ``3600`` seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-hlsplaylistsettings.html#cfn-mediatailor-channel-hlsplaylistsettings-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsPlaylistSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannel.LogConfigurationForChannelProperty",
        jsii_struct_bases=[],
        name_mapping={"log_types": "logTypes"},
    )
    class LogConfigurationForChannelProperty:
        def __init__(
            self,
            *,
            log_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The log configuration for the channel.

            :param log_types: The log types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-logconfigurationforchannel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                log_configuration_for_channel_property = mediatailor.CfnChannel.LogConfigurationForChannelProperty(
                    log_types=["logTypes"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e5a7e7699e2937a5b57a4d1b83f5129fa2b21541bc55e1f79a1ca106377c5300)
                check_type(argname="argument log_types", value=log_types, expected_type=type_hints["log_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_types is not None:
                self._values["log_types"] = log_types

        @builtins.property
        def log_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The log types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-logconfigurationforchannel.html#cfn-mediatailor-channel-logconfigurationforchannel-logtypes
            '''
            result = self._values.get("log_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationForChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannel.RequestOutputItemProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_name": "manifestName",
            "source_group": "sourceGroup",
            "dash_playlist_settings": "dashPlaylistSettings",
            "hls_playlist_settings": "hlsPlaylistSettings",
        },
    )
    class RequestOutputItemProperty:
        def __init__(
            self,
            *,
            manifest_name: builtins.str,
            source_group: builtins.str,
            dash_playlist_settings: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.DashPlaylistSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hls_playlist_settings: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.HlsPlaylistSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The output configuration for this channel.

            :param manifest_name: The name of the manifest for the channel. The name appears in the ``PlaybackUrl`` .
            :param source_group: A string used to match which ``HttpPackageConfiguration`` is used for each ``VodSource`` .
            :param dash_playlist_settings: DASH manifest configuration parameters.
            :param hls_playlist_settings: HLS playlist configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                request_output_item_property = mediatailor.CfnChannel.RequestOutputItemProperty(
                    manifest_name="manifestName",
                    source_group="sourceGroup",
                
                    # the properties below are optional
                    dash_playlist_settings=mediatailor.CfnChannel.DashPlaylistSettingsProperty(
                        manifest_window_seconds=123,
                        min_buffer_time_seconds=123,
                        min_update_period_seconds=123,
                        suggested_presentation_delay_seconds=123
                    ),
                    hls_playlist_settings=mediatailor.CfnChannel.HlsPlaylistSettingsProperty(
                        ad_markup_type=["adMarkupType"],
                        manifest_window_seconds=123
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__f1d4c3a316ddc28d5db9dbd943c872960619d5643164875a0009ce4f4639f744)
                check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
                check_type(argname="argument source_group", value=source_group, expected_type=type_hints["source_group"])
                check_type(argname="argument dash_playlist_settings", value=dash_playlist_settings, expected_type=type_hints["dash_playlist_settings"])
                check_type(argname="argument hls_playlist_settings", value=hls_playlist_settings, expected_type=type_hints["hls_playlist_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "manifest_name": manifest_name,
                "source_group": source_group,
            }
            if dash_playlist_settings is not None:
                self._values["dash_playlist_settings"] = dash_playlist_settings
            if hls_playlist_settings is not None:
                self._values["hls_playlist_settings"] = hls_playlist_settings

        @builtins.property
        def manifest_name(self) -> builtins.str:
            '''The name of the manifest for the channel.

            The name appears in the ``PlaybackUrl`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html#cfn-mediatailor-channel-requestoutputitem-manifestname
            '''
            result = self._values.get("manifest_name")
            assert result is not None, "Required property 'manifest_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_group(self) -> builtins.str:
            '''A string used to match which ``HttpPackageConfiguration`` is used for each ``VodSource`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html#cfn-mediatailor-channel-requestoutputitem-sourcegroup
            '''
            result = self._values.get("source_group")
            assert result is not None, "Required property 'source_group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dash_playlist_settings(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.DashPlaylistSettingsProperty"]]:
            '''DASH manifest configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html#cfn-mediatailor-channel-requestoutputitem-dashplaylistsettings
            '''
            result = self._values.get("dash_playlist_settings")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.DashPlaylistSettingsProperty"]], result)

        @builtins.property
        def hls_playlist_settings(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.HlsPlaylistSettingsProperty"]]:
            '''HLS playlist configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html#cfn-mediatailor-channel-requestoutputitem-hlsplaylistsettings
            '''
            result = self._values.get("hls_playlist_settings")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.HlsPlaylistSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RequestOutputItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannel.SlateSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_location_name": "sourceLocationName",
            "vod_source_name": "vodSourceName",
        },
    )
    class SlateSourceProperty:
        def __init__(
            self,
            *,
            source_location_name: typing.Optional[builtins.str] = None,
            vod_source_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Slate VOD source configuration.

            :param source_location_name: The name of the source location where the slate VOD source is stored.
            :param vod_source_name: The slate VOD source name. The VOD source must already exist in a source location before it can be used for slate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-slatesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                slate_source_property = mediatailor.CfnChannel.SlateSourceProperty(
                    source_location_name="sourceLocationName",
                    vod_source_name="vodSourceName"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__87bdd7eb43c3b69dcc5175fbdbdf3f64ecc1bea153e89e341c467115c5854c1e)
                check_type(argname="argument source_location_name", value=source_location_name, expected_type=type_hints["source_location_name"])
                check_type(argname="argument vod_source_name", value=vod_source_name, expected_type=type_hints["vod_source_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source_location_name is not None:
                self._values["source_location_name"] = source_location_name
            if vod_source_name is not None:
                self._values["vod_source_name"] = vod_source_name

        @builtins.property
        def source_location_name(self) -> typing.Optional[builtins.str]:
            '''The name of the source location where the slate VOD source is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-slatesource.html#cfn-mediatailor-channel-slatesource-sourcelocationname
            '''
            result = self._values.get("source_location_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vod_source_name(self) -> typing.Optional[builtins.str]:
            '''The slate VOD source name.

            The VOD source must already exist in a source location before it can be used for slate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-slatesource.html#cfn-mediatailor-channel-slatesource-vodsourcename
            '''
            result = self._values.get("vod_source_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlateSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannel.TimeShiftConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"max_time_delay_seconds": "maxTimeDelaySeconds"},
    )
    class TimeShiftConfigurationProperty:
        def __init__(self, *, max_time_delay_seconds: jsii.Number) -> None:
            '''The configuration for time-shifted viewing.

            :param max_time_delay_seconds: The maximum time delay for time-shifted viewing. The minimum allowed maximum time delay is 0 seconds, and the maximum allowed maximum time delay is 21600 seconds (6 hours).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-timeshiftconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                time_shift_configuration_property = mediatailor.CfnChannel.TimeShiftConfigurationProperty(
                    max_time_delay_seconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__9e6f8310362aba9a6cdbcee3376c31f278a1a77eb2cfdd2c6e322b1b49d57eaa)
                check_type(argname="argument max_time_delay_seconds", value=max_time_delay_seconds, expected_type=type_hints["max_time_delay_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_time_delay_seconds": max_time_delay_seconds,
            }

        @builtins.property
        def max_time_delay_seconds(self) -> jsii.Number:
            '''The maximum time delay for time-shifted viewing.

            The minimum allowed maximum time delay is 0 seconds, and the maximum allowed maximum time delay is 21600 seconds (6 hours).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-timeshiftconfiguration.html#cfn-mediatailor-channel-timeshiftconfiguration-maxtimedelayseconds
            '''
            result = self._values.get("max_time_delay_seconds")
            assert result is not None, "Required property 'max_time_delay_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeShiftConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_mediatailor_60404695.IChannelPolicyRef)
class CfnChannelPolicy(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannelPolicy",
):
    '''Specifies an IAM policy for the channel.

    IAM policies are used to control access to your channel.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channelpolicy.html
    :cloudformationResource: AWS::MediaTailor::ChannelPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        # policy: Any
        
        cfn_channel_policy = mediatailor.CfnChannelPolicy(self, "MyCfnChannelPolicy",
            channel_name="channelName",
            policy=policy
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        channel_name: builtins.str,
        policy: typing.Any,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::ChannelPolicy``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_name: The name of the channel associated with this Channel Policy.
        :param policy: The IAM policy for the channel. IAM policies are used to control access to your channel.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__31394bd173fe2beb5213e9badd5aafc6ea2b160b870f8a0efcdd0c7418364408)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelPolicyProps(channel_name=channel_name, policy=policy)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnChannelPolicy")
    @builtins.classmethod
    def is_cfn_channel_policy(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnChannelPolicy.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__abda8f12a5a6b5f01e1256783fdb08f119d1fa2429aa22f36113b572849fc90e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnChannelPolicy", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9bb5c51872ae1d2e26ab60faf42e8f67d099d72d6182d14f72ac00d2820a1253)
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
            type_hints = cached_type_hints(_typecheckingstub__77acf1b52692f677278f400d1fc6aac28c4f4db4641fe9077e743d4105363c94)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="channelPolicyRef")
    def channel_policy_ref(self) -> "_aws_mediatailor_60404695.ChannelPolicyReference":
        '''A reference to a ChannelPolicy resource.'''
        return typing.cast("_aws_mediatailor_60404695.ChannelPolicyReference", jsii.get(self, "channelPolicyRef"))

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        '''The name of the channel associated with this Channel Policy.'''
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__33c69c2a3ec02545796ab2a280c6251e38cd027ef575f6e9b82b2238d613b8fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''The IAM policy for the channel.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d60990c1542e708efa866295766195f2b5035b80cea3aacc1e22a1d78dd31022)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannelPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"channel_name": "channelName", "policy": "policy"},
)
class CfnChannelPolicyProps:
    def __init__(self, *, channel_name: builtins.str, policy: typing.Any) -> None:
        '''Properties for defining a ``CfnChannelPolicy``.

        :param channel_name: The name of the channel associated with this Channel Policy.
        :param policy: The IAM policy for the channel. IAM policies are used to control access to your channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channelpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            # policy: Any
            
            cfn_channel_policy_props = mediatailor.CfnChannelPolicyProps(
                channel_name="channelName",
                policy=policy
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0760e4c2515aab3aa0d5aa04febae58f777b0b8b02fe135798d73d9cfc228e7d)
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_name": channel_name,
            "policy": policy,
        }

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The name of the channel associated with this Channel Policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channelpolicy.html#cfn-mediatailor-channelpolicy-channelname
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''The IAM policy for the channel.

        IAM policies are used to control access to your channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channelpolicy.html#cfn-mediatailor-channelpolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_name": "channelName",
        "outputs": "outputs",
        "playback_mode": "playbackMode",
        "audiences": "audiences",
        "filler_slate": "fillerSlate",
        "log_configuration": "logConfiguration",
        "tags": "tags",
        "tier": "tier",
        "time_shift_configuration": "timeShiftConfiguration",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        channel_name: builtins.str,
        outputs: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.RequestOutputItemProperty", typing.Dict[builtins.str, typing.Any]]]]],
        playback_mode: builtins.str,
        audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        filler_slate: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.SlateSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.LogConfigurationForChannelProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        tier: typing.Optional[builtins.str] = None,
        time_shift_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnChannel.TimeShiftConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannel``.

        :param channel_name: The name of the channel.
        :param outputs: The channel's output properties.
        :param playback_mode: The type of playback mode for this channel. ``LINEAR`` - Programs play back-to-back only once. ``LOOP`` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.
        :param audiences: The list of audiences defined in channel.
        :param filler_slate: The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the ``LINEAR`` ``PlaybackMode`` . MediaTailor doesn't support filler slate for channels using the ``LOOP`` ``PlaybackMode`` .
        :param log_configuration: The log configuration.
        :param tags: The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .
        :param tier: The tier for this channel. STANDARD tier channels can contain live programs.
        :param time_shift_configuration: The configuration for time-shifted viewing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            cfn_channel_props = mediatailor.CfnChannelProps(
                channel_name="channelName",
                outputs=[mediatailor.CfnChannel.RequestOutputItemProperty(
                    manifest_name="manifestName",
                    source_group="sourceGroup",
            
                    # the properties below are optional
                    dash_playlist_settings=mediatailor.CfnChannel.DashPlaylistSettingsProperty(
                        manifest_window_seconds=123,
                        min_buffer_time_seconds=123,
                        min_update_period_seconds=123,
                        suggested_presentation_delay_seconds=123
                    ),
                    hls_playlist_settings=mediatailor.CfnChannel.HlsPlaylistSettingsProperty(
                        ad_markup_type=["adMarkupType"],
                        manifest_window_seconds=123
                    )
                )],
                playback_mode="playbackMode",
            
                # the properties below are optional
                audiences=["audiences"],
                filler_slate=mediatailor.CfnChannel.SlateSourceProperty(
                    source_location_name="sourceLocationName",
                    vod_source_name="vodSourceName"
                ),
                log_configuration=mediatailor.CfnChannel.LogConfigurationForChannelProperty(
                    log_types=["logTypes"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                tier="tier",
                time_shift_configuration=mediatailor.CfnChannel.TimeShiftConfigurationProperty(
                    max_time_delay_seconds=123
                )
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__34f9c53dfc17c104058553b2c51bffbfeea7885ab9628618cedcaf8634562913)
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument playback_mode", value=playback_mode, expected_type=type_hints["playback_mode"])
            check_type(argname="argument audiences", value=audiences, expected_type=type_hints["audiences"])
            check_type(argname="argument filler_slate", value=filler_slate, expected_type=type_hints["filler_slate"])
            check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument time_shift_configuration", value=time_shift_configuration, expected_type=type_hints["time_shift_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_name": channel_name,
            "outputs": outputs,
            "playback_mode": playback_mode,
        }
        if audiences is not None:
            self._values["audiences"] = audiences
        if filler_slate is not None:
            self._values["filler_slate"] = filler_slate
        if log_configuration is not None:
            self._values["log_configuration"] = log_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tier is not None:
            self._values["tier"] = tier
        if time_shift_configuration is not None:
            self._values["time_shift_configuration"] = time_shift_configuration

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The name of the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-channelname
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.RequestOutputItemProperty"]]]:
        '''The channel's output properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-outputs
        '''
        result = self._values.get("outputs")
        assert result is not None, "Required property 'outputs' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.RequestOutputItemProperty"]]], result)

    @builtins.property
    def playback_mode(self) -> builtins.str:
        '''The type of playback mode for this channel.

        ``LINEAR`` - Programs play back-to-back only once.

        ``LOOP`` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-playbackmode
        '''
        result = self._values.get("playback_mode")
        assert result is not None, "Required property 'playback_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of audiences defined in channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-audiences
        '''
        result = self._values.get("audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def filler_slate(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.SlateSourceProperty"]]:
        '''The slate used to fill gaps between programs in the schedule.

        You must configure filler slate if your channel uses the ``LINEAR`` ``PlaybackMode`` . MediaTailor doesn't support filler slate for channels using the ``LOOP`` ``PlaybackMode`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-fillerslate
        '''
        result = self._values.get("filler_slate")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.SlateSourceProperty"]], result)

    @builtins.property
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.LogConfigurationForChannelProperty"]]:
        '''The log configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-logconfiguration
        '''
        result = self._values.get("log_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.LogConfigurationForChannelProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags to assign to the channel.

        Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''The tier for this channel.

        STANDARD tier channels can contain live programs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-tier
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_shift_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.TimeShiftConfigurationProperty"]]:
        '''The configuration for time-shifted viewing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-timeshiftconfiguration
        '''
        result = self._values.get("time_shift_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnChannel.TimeShiftConfigurationProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_mediatailor_60404695.IFunctionRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnFunction(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnFunction",
):
    '''Resource Type definition for AWS::MediaTailor::Function.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html
    :cloudformationResource: AWS::MediaTailor::Function
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        cfn_function = mediatailor.CfnFunction(self, "MyCfnFunction",
            function_id="functionId",
            function_type="functionType",
        
            # the properties below are optional
            concurrent_executor_configuration=mediatailor.CfnFunction.ConcurrentExecutorConfigurationProperty(
                function_list=[mediatailor.CfnFunction.FunctionRefProperty(
                    alias="alias",
                    function_id="functionId",
                    run_condition="runCondition"
                )],
                max_concurrency=123,
                output={
                    "output_key": "output"
                },
                runtime="runtime",
                timeout_milliseconds=123
            ),
            custom_output_configuration=mediatailor.CfnFunction.CustomOutputConfigurationProperty(
                runtime="runtime",
        
                # the properties below are optional
                output={
                    "output_key": "output"
                }
            ),
            description="description",
            http_request_configuration=mediatailor.CfnFunction.HttpRequestConfigurationProperty(
                method_type="methodType",
                request_timeout_milliseconds=123,
                runtime="runtime",
                url="url",
        
                # the properties below are optional
                body="body",
                headers={
                    "headers_key": "headers"
                },
                output={
                    "output_key": "output"
                }
            ),
            sequential_executor_configuration=mediatailor.CfnFunction.SequentialExecutorConfigurationProperty(
                function_list=[mediatailor.CfnFunction.FunctionRefProperty(
                    alias="alias",
                    function_id="functionId",
                    run_condition="runCondition"
                )],
                runtime="runtime",
                timeout_milliseconds=123,
        
                # the properties below are optional
                output={
                    "output_key": "output"
                }
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
        function_id: builtins.str,
        function_type: builtins.str,
        concurrent_executor_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.ConcurrentExecutorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_output_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.CustomOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        http_request_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.HttpRequestConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sequential_executor_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.SequentialExecutorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::Function``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param function_id: The unique identifier for the function.
        :param function_type: 
        :param concurrent_executor_configuration: The configuration for a CONCURRENT_EXECUTOR function. A CONCURRENT_EXECUTOR runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete. For more information about functions, see Working with functions (https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the MediaTailor User Guide.
        :param custom_output_configuration: Configuration for custom output functions.
        :param description: A description of the function.
        :param http_request_configuration: Configuration for HTTP request functions.
        :param sequential_executor_configuration: The configuration for a SEQUENTIAL_EXECUTOR function. A SEQUENTIAL_EXECUTOR runs an ordered list of child functions one at a time, passing data between them. For more information about functions, see Working with functions (https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the MediaTailor User Guide.
        :param tags: The tags to assign to the function resource.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cd96c58f31f24adb3cea08347b5cb88afb7a1644c1d49acf5ea18ef7e858b6b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFunctionProps(
            function_id=function_id,
            function_type=function_type,
            concurrent_executor_configuration=concurrent_executor_configuration,
            custom_output_configuration=custom_output_configuration,
            description=description,
            http_request_configuration=http_request_configuration,
            sequential_executor_configuration=sequential_executor_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForFunction")
    @builtins.classmethod
    def arn_for_function(
        cls,
        resource: "_aws_mediatailor_60404695.IFunctionRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c1622bc3b9fb588270223d9f7e4597e460a8eb30134a5e06d974142e25db0e60)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForFunction", [resource]))

    @jsii.member(jsii_name="isCfnFunction")
    @builtins.classmethod
    def is_cfn_function(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFunction.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__75251cc24b0becd917928021558ddb9ae78d087dab72897b6c0dd0a109fe49ea)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFunction", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__81d78839ae256142aacfd95c57d31064da1eb11fcf3df6b8c58cab6aef81d452)
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
            type_hints = cached_type_hints(_typecheckingstub__0691ea7e84dd9690413b0c03614038e090ff0deec3c43edc0664a06d3031c7ce)
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
        '''The ARN of the function.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="functionRef")
    def function_ref(self) -> "_aws_mediatailor_60404695.FunctionReference":
        '''A reference to a Function resource.'''
        return typing.cast("_aws_mediatailor_60404695.FunctionReference", jsii.get(self, "functionRef"))

    @builtins.property
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        '''The unique identifier for the function.'''
        return typing.cast(builtins.str, jsii.get(self, "functionId"))

    @function_id.setter
    def function_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e672160af6c70e20c93ee58a3d25e27152153feb541dc68112b2310551674635)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="functionType")
    def function_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionType"))

    @function_type.setter
    def function_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fb28c3052dd431563a7b26a7dce4b50d1c29abc2106f42fa0a5329270452f9c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="concurrentExecutorConfiguration")
    def concurrent_executor_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.ConcurrentExecutorConfigurationProperty"]]:
        '''The configuration for a CONCURRENT_EXECUTOR function.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.ConcurrentExecutorConfigurationProperty"]], jsii.get(self, "concurrentExecutorConfiguration"))

    @concurrent_executor_configuration.setter
    def concurrent_executor_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.ConcurrentExecutorConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7881dd44052d7a7cfe200f4556de1fc9a705e530c1e461e83ad35044d7d4fba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "concurrentExecutorConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customOutputConfiguration")
    def custom_output_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.CustomOutputConfigurationProperty"]]:
        '''Configuration for custom output functions.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.CustomOutputConfigurationProperty"]], jsii.get(self, "customOutputConfiguration"))

    @custom_output_configuration.setter
    def custom_output_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.CustomOutputConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d34312157c19e7408ec3ea1cda432a669a0967161e5df7dda4eab223f9a0b044)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customOutputConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a2219a19201f0a17be79ff6717a47ca2d73b9c0b9ed0432d4890f90b4256b4d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="httpRequestConfiguration")
    def http_request_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.HttpRequestConfigurationProperty"]]:
        '''Configuration for HTTP request functions.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.HttpRequestConfigurationProperty"]], jsii.get(self, "httpRequestConfiguration"))

    @http_request_configuration.setter
    def http_request_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.HttpRequestConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1a807bd0f7ad759c090dcf86e543a221b7023a5c09b76d141eebdf0d9505192e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRequestConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sequentialExecutorConfiguration")
    def sequential_executor_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.SequentialExecutorConfigurationProperty"]]:
        '''The configuration for a SEQUENTIAL_EXECUTOR function.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.SequentialExecutorConfigurationProperty"]], jsii.get(self, "sequentialExecutorConfiguration"))

    @sequential_executor_configuration.setter
    def sequential_executor_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.SequentialExecutorConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__85ad517a9634af2cf1cf7cddd2dd3cecff513a52e7a1bb68e109fc8982897972)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sequentialExecutorConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags to assign to the function resource.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b65b0a9bacbd0f65526afeb7cf1e0c3ca3773c11abb883bbf33a47ef72445de0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnFunction.ConcurrentExecutorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_list": "functionList",
            "max_concurrency": "maxConcurrency",
            "output": "output",
            "runtime": "runtime",
            "timeout_milliseconds": "timeoutMilliseconds",
        },
    )
    class ConcurrentExecutorConfigurationProperty:
        def __init__(
            self,
            *,
            function_list: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.FunctionRefProperty", typing.Dict[builtins.str, typing.Any]]]]],
            max_concurrency: jsii.Number,
            output: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]],
            runtime: builtins.str,
            timeout_milliseconds: jsii.Number,
        ) -> None:
            '''The configuration for a CONCURRENT_EXECUTOR function.

            A CONCURRENT_EXECUTOR runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete. For more information about functions, see Working with functions (https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the MediaTailor User Guide.

            :param function_list: The list of 1 to 10 child functions that MediaTailor runs in parallel. Each entry specifies a child function to execute and an optional run condition expression that controls whether the function runs. Child functions cannot themselves be executors, and each child function's resolved namespace must be unique across the list.
            :param max_concurrency: The maximum number of child functions that MediaTailor runs simultaneously. When the list contains more functions than MaxConcurrency, MediaTailor starts additional functions as running ones complete, so that no more than MaxConcurrency functions run at the same time. Valid values are 1 to 2.
            :param output: A map of output bindings that controls which bindings the executor commits to the session state after all child functions complete. Each key is a namespaced output path, and each value is an expression that MediaTailor evaluates against the combined results of the child functions.
            :param runtime: The expression language used to evaluate expressions in the function configuration. Set this to JSONATA.
            :param timeout_milliseconds: The maximum time, in milliseconds, for all child functions to complete. This timeout covers every function in the list, including any HTTP calls the child functions make. If the executor exceeds this timeout, MediaTailor discards all output from the executor and proceeds with default behavior. Valid values are 100 to 2000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-concurrentexecutorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                concurrent_executor_configuration_property = mediatailor.CfnFunction.ConcurrentExecutorConfigurationProperty(
                    function_list=[mediatailor.CfnFunction.FunctionRefProperty(
                        alias="alias",
                        function_id="functionId",
                        run_condition="runCondition"
                    )],
                    max_concurrency=123,
                    output={
                        "output_key": "output"
                    },
                    runtime="runtime",
                    timeout_milliseconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__178948756e734ee68c9d1fe0aa6ae03bc94447092d71fbf586f1f0c568c19ef9)
                check_type(argname="argument function_list", value=function_list, expected_type=type_hints["function_list"])
                check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
                check_type(argname="argument output", value=output, expected_type=type_hints["output"])
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument timeout_milliseconds", value=timeout_milliseconds, expected_type=type_hints["timeout_milliseconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_list": function_list,
                "max_concurrency": max_concurrency,
                "output": output,
                "runtime": runtime,
                "timeout_milliseconds": timeout_milliseconds,
            }

        @builtins.property
        def function_list(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.FunctionRefProperty"]]]:
            '''The list of 1 to 10 child functions that MediaTailor runs in parallel.

            Each entry specifies a child function to execute and an optional run condition expression that controls whether the function runs. Child functions cannot themselves be executors, and each child function's resolved namespace must be unique across the list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-concurrentexecutorconfiguration.html#cfn-mediatailor-function-concurrentexecutorconfiguration-functionlist
            '''
            result = self._values.get("function_list")
            assert result is not None, "Required property 'function_list' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.FunctionRefProperty"]]], result)

        @builtins.property
        def max_concurrency(self) -> jsii.Number:
            '''The maximum number of child functions that MediaTailor runs simultaneously.

            When the list contains more functions than MaxConcurrency, MediaTailor starts additional functions as running ones complete, so that no more than MaxConcurrency functions run at the same time. Valid values are 1 to 2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-concurrentexecutorconfiguration.html#cfn-mediatailor-function-concurrentexecutorconfiguration-maxconcurrency
            '''
            result = self._values.get("max_concurrency")
            assert result is not None, "Required property 'max_concurrency' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def output(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]:
            '''A map of output bindings that controls which bindings the executor commits to the session state after all child functions complete.

            Each key is a namespaced output path, and each value is an expression that MediaTailor evaluates against the combined results of the child functions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-concurrentexecutorconfiguration.html#cfn-mediatailor-function-concurrentexecutorconfiguration-output
            '''
            result = self._values.get("output")
            assert result is not None, "Required property 'output' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]], result)

        @builtins.property
        def runtime(self) -> builtins.str:
            '''The expression language used to evaluate expressions in the function configuration.

            Set this to JSONATA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-concurrentexecutorconfiguration.html#cfn-mediatailor-function-concurrentexecutorconfiguration-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_milliseconds(self) -> jsii.Number:
            '''The maximum time, in milliseconds, for all child functions to complete.

            This timeout covers every function in the list, including any HTTP calls the child functions make. If the executor exceeds this timeout, MediaTailor discards all output from the executor and proceeds with default behavior. Valid values are 100 to 2000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-concurrentexecutorconfiguration.html#cfn-mediatailor-function-concurrentexecutorconfiguration-timeoutmilliseconds
            '''
            result = self._values.get("timeout_milliseconds")
            assert result is not None, "Required property 'timeout_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConcurrentExecutorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnFunction.CustomOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"runtime": "runtime", "output": "output"},
    )
    class CustomOutputConfigurationProperty:
        def __init__(
            self,
            *,
            runtime: builtins.str,
            output: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Configuration for custom output functions.

            :param runtime: The expression language used to evaluate expressions in the function configuration. Set this to JSONATA.
            :param output: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-customoutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                custom_output_configuration_property = mediatailor.CfnFunction.CustomOutputConfigurationProperty(
                    runtime="runtime",
                
                    # the properties below are optional
                    output={
                        "output_key": "output"
                    }
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__61544711aa26c5056e9b4d3cfab7dee3d6eaa0f011cb57fde19c711b08a922de)
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "runtime": runtime,
            }
            if output is not None:
                self._values["output"] = output

        @builtins.property
        def runtime(self) -> builtins.str:
            '''The expression language used to evaluate expressions in the function configuration.

            Set this to JSONATA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-customoutputconfiguration.html#cfn-mediatailor-function-customoutputconfiguration-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-customoutputconfiguration.html#cfn-mediatailor-function-customoutputconfiguration-output
            '''
            result = self._values.get("output")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnFunction.FunctionRefProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alias": "alias",
            "function_id": "functionId",
            "run_condition": "runCondition",
        },
    )
    class FunctionRefProperty:
        def __init__(
            self,
            *,
            alias: typing.Optional[builtins.str] = None,
            function_id: typing.Optional[builtins.str] = None,
            run_condition: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A reference to a child function within an executor function.

            :param alias: An optional alternate name for the child function within the executor. MediaTailor uses this value as the namespace for the child function's output. If omitted, MediaTailor uses the function identifier. The resolved namespace must be unique across all child functions in the list.
            :param function_id: The identifier of the child function to execute.
            :param run_condition: An optional expression that evaluates to a boolean. MediaTailor evaluates this expression immediately before running the child function, using the accumulated state at that point. If the expression evaluates to false, MediaTailor skips the child function. If omitted, the child function always runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-functionref.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                function_ref_property = mediatailor.CfnFunction.FunctionRefProperty(
                    alias="alias",
                    function_id="functionId",
                    run_condition="runCondition"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__5737ad8fdf57086197584ef5d9e43c62428f917f712bc50c4302371649b0c300)
                check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
                check_type(argname="argument function_id", value=function_id, expected_type=type_hints["function_id"])
                check_type(argname="argument run_condition", value=run_condition, expected_type=type_hints["run_condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alias is not None:
                self._values["alias"] = alias
            if function_id is not None:
                self._values["function_id"] = function_id
            if run_condition is not None:
                self._values["run_condition"] = run_condition

        @builtins.property
        def alias(self) -> typing.Optional[builtins.str]:
            '''An optional alternate name for the child function within the executor.

            MediaTailor uses this value as the namespace for the child function's output. If omitted, MediaTailor uses the function identifier. The resolved namespace must be unique across all child functions in the list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-functionref.html#cfn-mediatailor-function-functionref-alias
            '''
            result = self._values.get("alias")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def function_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the child function to execute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-functionref.html#cfn-mediatailor-function-functionref-functionid
            '''
            result = self._values.get("function_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def run_condition(self) -> typing.Optional[builtins.str]:
            '''An optional expression that evaluates to a boolean.

            MediaTailor evaluates this expression immediately before running the child function, using the accumulated state at that point. If the expression evaluates to false, MediaTailor skips the child function. If omitted, the child function always runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-functionref.html#cfn-mediatailor-function-functionref-runcondition
            '''
            result = self._values.get("run_condition")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionRefProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnFunction.HttpRequestConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "method_type": "methodType",
            "request_timeout_milliseconds": "requestTimeoutMilliseconds",
            "runtime": "runtime",
            "url": "url",
            "body": "body",
            "headers": "headers",
            "output": "output",
        },
    )
    class HttpRequestConfigurationProperty:
        def __init__(
            self,
            *,
            method_type: builtins.str,
            request_timeout_milliseconds: jsii.Number,
            runtime: builtins.str,
            url: builtins.str,
            body: typing.Optional[builtins.str] = None,
            headers: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
            output: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Configuration for HTTP request functions.

            :param method_type: 
            :param request_timeout_milliseconds: The timeout in milliseconds for the HTTP request. Maximum value is 2000.
            :param runtime: The expression language used to evaluate expressions in the function configuration. Set this to JSONATA.
            :param url: The URL endpoint for the HTTP request.
            :param body: The body of the HTTP request.
            :param headers: 
            :param output: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-httprequestconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                http_request_configuration_property = mediatailor.CfnFunction.HttpRequestConfigurationProperty(
                    method_type="methodType",
                    request_timeout_milliseconds=123,
                    runtime="runtime",
                    url="url",
                
                    # the properties below are optional
                    body="body",
                    headers={
                        "headers_key": "headers"
                    },
                    output={
                        "output_key": "output"
                    }
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0f6999ed1a463a1d66432cdff27ee1e9591dc5d3ae4707cd971a7668661f38f8)
                check_type(argname="argument method_type", value=method_type, expected_type=type_hints["method_type"])
                check_type(argname="argument request_timeout_milliseconds", value=request_timeout_milliseconds, expected_type=type_hints["request_timeout_milliseconds"])
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
                check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "method_type": method_type,
                "request_timeout_milliseconds": request_timeout_milliseconds,
                "runtime": runtime,
                "url": url,
            }
            if body is not None:
                self._values["body"] = body
            if headers is not None:
                self._values["headers"] = headers
            if output is not None:
                self._values["output"] = output

        @builtins.property
        def method_type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-httprequestconfiguration.html#cfn-mediatailor-function-httprequestconfiguration-methodtype
            '''
            result = self._values.get("method_type")
            assert result is not None, "Required property 'method_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def request_timeout_milliseconds(self) -> jsii.Number:
            '''The timeout in milliseconds for the HTTP request.

            Maximum value is 2000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-httprequestconfiguration.html#cfn-mediatailor-function-httprequestconfiguration-requesttimeoutmilliseconds
            '''
            result = self._values.get("request_timeout_milliseconds")
            assert result is not None, "Required property 'request_timeout_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def runtime(self) -> builtins.str:
            '''The expression language used to evaluate expressions in the function configuration.

            Set this to JSONATA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-httprequestconfiguration.html#cfn-mediatailor-function-httprequestconfiguration-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def url(self) -> builtins.str:
            '''The URL endpoint for the HTTP request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-httprequestconfiguration.html#cfn-mediatailor-function-httprequestconfiguration-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The body of the HTTP request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-httprequestconfiguration.html#cfn-mediatailor-function-httprequestconfiguration-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def headers(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-httprequestconfiguration.html#cfn-mediatailor-function-httprequestconfiguration-headers
            '''
            result = self._values.get("headers")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def output(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-httprequestconfiguration.html#cfn-mediatailor-function-httprequestconfiguration-output
            '''
            result = self._values.get("output")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpRequestConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnFunction.SequentialExecutorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_list": "functionList",
            "runtime": "runtime",
            "timeout_milliseconds": "timeoutMilliseconds",
            "output": "output",
        },
    )
    class SequentialExecutorConfigurationProperty:
        def __init__(
            self,
            *,
            function_list: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.FunctionRefProperty", typing.Dict[builtins.str, typing.Any]]]]],
            runtime: builtins.str,
            timeout_milliseconds: jsii.Number,
            output: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''The configuration for a SEQUENTIAL_EXECUTOR function.

            A SEQUENTIAL_EXECUTOR runs an ordered list of child functions one at a time, passing data between them. For more information about functions, see Working with functions (https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the MediaTailor User Guide.

            :param function_list: An ordered list of 1 to 10 steps. Each step specifies a child function to execute and an optional run condition expression that controls whether the step runs. MediaTailor executes the steps in order, passing data between steps through temporary data. Each step's resolved namespace must be unique across the list.
            :param runtime: The expression language used to evaluate expressions in the function configuration. Set this to JSONATA.
            :param timeout_milliseconds: The maximum time, in milliseconds, for the entire sequence to complete. This timeout covers all steps, including any HTTP calls made by child functions. If the sequence exceeds this timeout, MediaTailor discards all output from the sequence and proceeds with default behavior. Valid values are 100 to 2000.
            :param output: A map of output bindings that controls which bindings the sequence commits to the session state after all steps complete. Each key is a namespaced output path, and each value is an expression that MediaTailor evaluates against the accumulated results of the steps.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-sequentialexecutorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                sequential_executor_configuration_property = mediatailor.CfnFunction.SequentialExecutorConfigurationProperty(
                    function_list=[mediatailor.CfnFunction.FunctionRefProperty(
                        alias="alias",
                        function_id="functionId",
                        run_condition="runCondition"
                    )],
                    runtime="runtime",
                    timeout_milliseconds=123,
                
                    # the properties below are optional
                    output={
                        "output_key": "output"
                    }
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__500d6a7aa0edd3b223d18e64c8c78d74551a1f7285ddd9f7bcf2f3958acdb83d)
                check_type(argname="argument function_list", value=function_list, expected_type=type_hints["function_list"])
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument timeout_milliseconds", value=timeout_milliseconds, expected_type=type_hints["timeout_milliseconds"])
                check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_list": function_list,
                "runtime": runtime,
                "timeout_milliseconds": timeout_milliseconds,
            }
            if output is not None:
                self._values["output"] = output

        @builtins.property
        def function_list(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.FunctionRefProperty"]]]:
            '''An ordered list of 1 to 10 steps.

            Each step specifies a child function to execute and an optional run condition expression that controls whether the step runs. MediaTailor executes the steps in order, passing data between steps through temporary data. Each step's resolved namespace must be unique across the list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-sequentialexecutorconfiguration.html#cfn-mediatailor-function-sequentialexecutorconfiguration-functionlist
            '''
            result = self._values.get("function_list")
            assert result is not None, "Required property 'function_list' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.FunctionRefProperty"]]], result)

        @builtins.property
        def runtime(self) -> builtins.str:
            '''The expression language used to evaluate expressions in the function configuration.

            Set this to JSONATA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-sequentialexecutorconfiguration.html#cfn-mediatailor-function-sequentialexecutorconfiguration-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_milliseconds(self) -> jsii.Number:
            '''The maximum time, in milliseconds, for the entire sequence to complete.

            This timeout covers all steps, including any HTTP calls made by child functions. If the sequence exceeds this timeout, MediaTailor discards all output from the sequence and proceeds with default behavior. Valid values are 100 to 2000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-sequentialexecutorconfiguration.html#cfn-mediatailor-function-sequentialexecutorconfiguration-timeoutmilliseconds
            '''
            result = self._values.get("timeout_milliseconds")
            assert result is not None, "Required property 'timeout_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def output(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''A map of output bindings that controls which bindings the sequence commits to the session state after all steps complete.

            Each key is a namespaced output path, and each value is an expression that MediaTailor evaluates against the accumulated results of the steps.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-function-sequentialexecutorconfiguration.html#cfn-mediatailor-function-sequentialexecutorconfiguration-output
            '''
            result = self._values.get("output")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SequentialExecutorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_id": "functionId",
        "function_type": "functionType",
        "concurrent_executor_configuration": "concurrentExecutorConfiguration",
        "custom_output_configuration": "customOutputConfiguration",
        "description": "description",
        "http_request_configuration": "httpRequestConfiguration",
        "sequential_executor_configuration": "sequentialExecutorConfiguration",
        "tags": "tags",
    },
)
class CfnFunctionProps:
    def __init__(
        self,
        *,
        function_id: builtins.str,
        function_type: builtins.str,
        concurrent_executor_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.ConcurrentExecutorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_output_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.CustomOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        http_request_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.HttpRequestConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sequential_executor_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnFunction.SequentialExecutorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFunction``.

        :param function_id: The unique identifier for the function.
        :param function_type: 
        :param concurrent_executor_configuration: The configuration for a CONCURRENT_EXECUTOR function. A CONCURRENT_EXECUTOR runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete. For more information about functions, see Working with functions (https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the MediaTailor User Guide.
        :param custom_output_configuration: Configuration for custom output functions.
        :param description: A description of the function.
        :param http_request_configuration: Configuration for HTTP request functions.
        :param sequential_executor_configuration: The configuration for a SEQUENTIAL_EXECUTOR function. A SEQUENTIAL_EXECUTOR runs an ordered list of child functions one at a time, passing data between them. For more information about functions, see Working with functions (https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the MediaTailor User Guide.
        :param tags: The tags to assign to the function resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            cfn_function_props = mediatailor.CfnFunctionProps(
                function_id="functionId",
                function_type="functionType",
            
                # the properties below are optional
                concurrent_executor_configuration=mediatailor.CfnFunction.ConcurrentExecutorConfigurationProperty(
                    function_list=[mediatailor.CfnFunction.FunctionRefProperty(
                        alias="alias",
                        function_id="functionId",
                        run_condition="runCondition"
                    )],
                    max_concurrency=123,
                    output={
                        "output_key": "output"
                    },
                    runtime="runtime",
                    timeout_milliseconds=123
                ),
                custom_output_configuration=mediatailor.CfnFunction.CustomOutputConfigurationProperty(
                    runtime="runtime",
            
                    # the properties below are optional
                    output={
                        "output_key": "output"
                    }
                ),
                description="description",
                http_request_configuration=mediatailor.CfnFunction.HttpRequestConfigurationProperty(
                    method_type="methodType",
                    request_timeout_milliseconds=123,
                    runtime="runtime",
                    url="url",
            
                    # the properties below are optional
                    body="body",
                    headers={
                        "headers_key": "headers"
                    },
                    output={
                        "output_key": "output"
                    }
                ),
                sequential_executor_configuration=mediatailor.CfnFunction.SequentialExecutorConfigurationProperty(
                    function_list=[mediatailor.CfnFunction.FunctionRefProperty(
                        alias="alias",
                        function_id="functionId",
                        run_condition="runCondition"
                    )],
                    runtime="runtime",
                    timeout_milliseconds=123,
            
                    # the properties below are optional
                    output={
                        "output_key": "output"
                    }
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5a7008df40fa116385e225dc9fc11c5a0c3905883fa95cd4742d1f9506eddc5e)
            check_type(argname="argument function_id", value=function_id, expected_type=type_hints["function_id"])
            check_type(argname="argument function_type", value=function_type, expected_type=type_hints["function_type"])
            check_type(argname="argument concurrent_executor_configuration", value=concurrent_executor_configuration, expected_type=type_hints["concurrent_executor_configuration"])
            check_type(argname="argument custom_output_configuration", value=custom_output_configuration, expected_type=type_hints["custom_output_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument http_request_configuration", value=http_request_configuration, expected_type=type_hints["http_request_configuration"])
            check_type(argname="argument sequential_executor_configuration", value=sequential_executor_configuration, expected_type=type_hints["sequential_executor_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_id": function_id,
            "function_type": function_type,
        }
        if concurrent_executor_configuration is not None:
            self._values["concurrent_executor_configuration"] = concurrent_executor_configuration
        if custom_output_configuration is not None:
            self._values["custom_output_configuration"] = custom_output_configuration
        if description is not None:
            self._values["description"] = description
        if http_request_configuration is not None:
            self._values["http_request_configuration"] = http_request_configuration
        if sequential_executor_configuration is not None:
            self._values["sequential_executor_configuration"] = sequential_executor_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def function_id(self) -> builtins.str:
        '''The unique identifier for the function.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html#cfn-mediatailor-function-functionid
        '''
        result = self._values.get("function_id")
        assert result is not None, "Required property 'function_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_type(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html#cfn-mediatailor-function-functiontype
        '''
        result = self._values.get("function_type")
        assert result is not None, "Required property 'function_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def concurrent_executor_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.ConcurrentExecutorConfigurationProperty"]]:
        '''The configuration for a CONCURRENT_EXECUTOR function.

        A CONCURRENT_EXECUTOR runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete. For more information about functions, see Working with functions (https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the MediaTailor User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html#cfn-mediatailor-function-concurrentexecutorconfiguration
        '''
        result = self._values.get("concurrent_executor_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.ConcurrentExecutorConfigurationProperty"]], result)

    @builtins.property
    def custom_output_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.CustomOutputConfigurationProperty"]]:
        '''Configuration for custom output functions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html#cfn-mediatailor-function-customoutputconfiguration
        '''
        result = self._values.get("custom_output_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.CustomOutputConfigurationProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html#cfn-mediatailor-function-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_request_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.HttpRequestConfigurationProperty"]]:
        '''Configuration for HTTP request functions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html#cfn-mediatailor-function-httprequestconfiguration
        '''
        result = self._values.get("http_request_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.HttpRequestConfigurationProperty"]], result)

    @builtins.property
    def sequential_executor_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.SequentialExecutorConfigurationProperty"]]:
        '''The configuration for a SEQUENTIAL_EXECUTOR function.

        A SEQUENTIAL_EXECUTOR runs an ordered list of child functions one at a time, passing data between them. For more information about functions, see Working with functions (https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the MediaTailor User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html#cfn-mediatailor-function-sequentialexecutorconfiguration
        '''
        result = self._values.get("sequential_executor_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnFunction.SequentialExecutorConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags to assign to the function resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-function.html#cfn-mediatailor-function-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_mediatailor_60404695.ILiveSourceRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnLiveSource(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnLiveSource",
):
    '''Live source configuration parameters.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html
    :cloudformationResource: AWS::MediaTailor::LiveSource
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        cfn_live_source = mediatailor.CfnLiveSource(self, "MyCfnLiveSource",
            http_package_configurations=[mediatailor.CfnLiveSource.HttpPackageConfigurationProperty(
                path="path",
                source_group="sourceGroup",
                type="type"
            )],
            live_source_name="liveSourceName",
            source_location_name="sourceLocationName",
        
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
        http_package_configurations: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLiveSource.HttpPackageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        live_source_name: builtins.str,
        source_location_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::LiveSource``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param http_package_configurations: The HTTP package configurations for the live source.
        :param live_source_name: The name that's used to refer to a live source.
        :param source_location_name: The name of the source location.
        :param tags: The tags assigned to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__caad9e925cf2074f54088c0241999fdbc5c194736555867b7765527f3cac0b4a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLiveSourceProps(
            http_package_configurations=http_package_configurations,
            live_source_name=live_source_name,
            source_location_name=source_location_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLiveSource")
    @builtins.classmethod
    def arn_for_live_source(
        cls,
        resource: "_aws_mediatailor_60404695.ILiveSourceRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6b2b664e7ed5590505b220acf48fbfff98a521078fb4767ee5949f9cbd9c0e6a)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForLiveSource", [resource]))

    @jsii.member(jsii_name="isCfnLiveSource")
    @builtins.classmethod
    def is_cfn_live_source(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnLiveSource.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0c51a8418725bfba543ac688a7eb06834d4a3743f7a11753f15ed105923071e2)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnLiveSource", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ed469803ff91fff7fc3040fc3d0bb3fa9a21fd4b59da12961328098a4c73f954)
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
            type_hints = cached_type_hints(_typecheckingstub__a52884dbe2ce928f779cdf8bd2581daa116db94102e6bf411658389d41cc6b49)
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
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="liveSourceRef")
    def live_source_ref(self) -> "_aws_mediatailor_60404695.LiveSourceReference":
        '''A reference to a LiveSource resource.'''
        return typing.cast("_aws_mediatailor_60404695.LiveSourceReference", jsii.get(self, "liveSourceRef"))

    @builtins.property
    @jsii.member(jsii_name="httpPackageConfigurations")
    def http_package_configurations(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLiveSource.HttpPackageConfigurationProperty"]]]:
        '''The HTTP package configurations for the live source.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLiveSource.HttpPackageConfigurationProperty"]]], jsii.get(self, "httpPackageConfigurations"))

    @http_package_configurations.setter
    def http_package_configurations(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLiveSource.HttpPackageConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3fa182da40e12286d6ab8a5538c3092bd85a8ea141d3aa51a69178e242b53eb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPackageConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="liveSourceName")
    def live_source_name(self) -> builtins.str:
        '''The name that's used to refer to a live source.'''
        return typing.cast(builtins.str, jsii.get(self, "liveSourceName"))

    @live_source_name.setter
    def live_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ac1795bf7c4263fcfbd30da5a955ba17d73ac00d7a1fcf627458bef546932345)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "liveSourceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceLocationName")
    def source_location_name(self) -> builtins.str:
        '''The name of the source location.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceLocationName"))

    @source_location_name.setter
    def source_location_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__00b7526b80803bba8c5dd84e954c48ba46ef9972bfff2752568fcf3f83123cdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceLocationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the live source.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b020567a78e7c965d540da779a72d64a6ce4c5d0070398ae50aae2bb69a1b916)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnLiveSource.HttpPackageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path", "source_group": "sourceGroup", "type": "type"},
    )
    class HttpPackageConfigurationProperty:
        def __init__(
            self,
            *,
            path: builtins.str,
            source_group: builtins.str,
            type: builtins.str,
        ) -> None:
            '''The HTTP package configuration properties for the requested VOD source.

            :param path: The relative path to the URL for this VOD source. This is combined with ``SourceLocation::HttpConfiguration::BaseUrl`` to form a valid URL.
            :param source_group: The name of the source group. This has to match one of the ``Channel::Outputs::SourceGroup`` .
            :param type: The streaming protocol for this package configuration. Supported values are ``HLS`` and ``DASH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-livesource-httppackageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                http_package_configuration_property = mediatailor.CfnLiveSource.HttpPackageConfigurationProperty(
                    path="path",
                    source_group="sourceGroup",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__13f0630b3469ba702929b845c7fafefb841b9e63dd48246c3a1e4880161e80e4)
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument source_group", value=source_group, expected_type=type_hints["source_group"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "path": path,
                "source_group": source_group,
                "type": type,
            }

        @builtins.property
        def path(self) -> builtins.str:
            '''The relative path to the URL for this VOD source.

            This is combined with ``SourceLocation::HttpConfiguration::BaseUrl`` to form a valid URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-livesource-httppackageconfiguration.html#cfn-mediatailor-livesource-httppackageconfiguration-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_group(self) -> builtins.str:
            '''The name of the source group.

            This has to match one of the ``Channel::Outputs::SourceGroup`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-livesource-httppackageconfiguration.html#cfn-mediatailor-livesource-httppackageconfiguration-sourcegroup
            '''
            result = self._values.get("source_group")
            assert result is not None, "Required property 'source_group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The streaming protocol for this package configuration.

            Supported values are ``HLS`` and ``DASH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-livesource-httppackageconfiguration.html#cfn-mediatailor-livesource-httppackageconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpPackageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnLiveSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "http_package_configurations": "httpPackageConfigurations",
        "live_source_name": "liveSourceName",
        "source_location_name": "sourceLocationName",
        "tags": "tags",
    },
)
class CfnLiveSourceProps:
    def __init__(
        self,
        *,
        http_package_configurations: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnLiveSource.HttpPackageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        live_source_name: builtins.str,
        source_location_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLiveSource``.

        :param http_package_configurations: The HTTP package configurations for the live source.
        :param live_source_name: The name that's used to refer to a live source.
        :param source_location_name: The name of the source location.
        :param tags: The tags assigned to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            cfn_live_source_props = mediatailor.CfnLiveSourceProps(
                http_package_configurations=[mediatailor.CfnLiveSource.HttpPackageConfigurationProperty(
                    path="path",
                    source_group="sourceGroup",
                    type="type"
                )],
                live_source_name="liveSourceName",
                source_location_name="sourceLocationName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__adc89490043dd5c6acaa08c89f60f172168bb565829b267f04a07c3038db8079)
            check_type(argname="argument http_package_configurations", value=http_package_configurations, expected_type=type_hints["http_package_configurations"])
            check_type(argname="argument live_source_name", value=live_source_name, expected_type=type_hints["live_source_name"])
            check_type(argname="argument source_location_name", value=source_location_name, expected_type=type_hints["source_location_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http_package_configurations": http_package_configurations,
            "live_source_name": live_source_name,
            "source_location_name": source_location_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def http_package_configurations(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLiveSource.HttpPackageConfigurationProperty"]]]:
        '''The HTTP package configurations for the live source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html#cfn-mediatailor-livesource-httppackageconfigurations
        '''
        result = self._values.get("http_package_configurations")
        assert result is not None, "Required property 'http_package_configurations' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnLiveSource.HttpPackageConfigurationProperty"]]], result)

    @builtins.property
    def live_source_name(self) -> builtins.str:
        '''The name that's used to refer to a live source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html#cfn-mediatailor-livesource-livesourcename
        '''
        result = self._values.get("live_source_name")
        assert result is not None, "Required property 'live_source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_location_name(self) -> builtins.str:
        '''The name of the source location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html#cfn-mediatailor-livesource-sourcelocationname
        '''
        result = self._values.get("source_location_name")
        assert result is not None, "Required property 'source_location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the live source.

        Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html#cfn-mediatailor-livesource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLiveSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_mediatailor_60404695.IPlaybackConfigurationRef, _aws_cdk_0cae9daa.ITaggable)
class CfnPlaybackConfiguration(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration",
):
    '''Adds a new playback configuration to AWS Elemental MediaTailor .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html
    :cloudformationResource: AWS::MediaTailor::PlaybackConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        # configuration_aliases: Any
        
        cfn_playback_configuration = mediatailor.CfnPlaybackConfiguration(self, "MyCfnPlaybackConfiguration",
            ad_decision_server_url="adDecisionServerUrl",
            name="name",
            video_content_source_url="videoContentSourceUrl",
        
            # the properties below are optional
            ad_conditioning_configuration=mediatailor.CfnPlaybackConfiguration.AdConditioningConfigurationProperty(
                streaming_media_file_conditioning="streamingMediaFileConditioning"
            ),
            ad_decision_server_configuration=mediatailor.CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty(
                http_request=mediatailor.CfnPlaybackConfiguration.HttpRequestProperty(
                    body="body",
                    compress_request="compressRequest",
                    headers={
                        "headers_key": "headers"
                    },
                    http_method="httpMethod"
                ),
        
                # the properties below are optional
                vast_response=mediatailor.CfnPlaybackConfiguration.VastResponseProperty(
                    ad_sequencing_mode="adSequencingMode"
                )
            ),
            ads_personalization_concurrency=mediatailor.CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty(
                enable_vod_vast_parallelization=False,
                max_concurrent_ads_requests=123
            ),
            ads_personalization_timeouts=mediatailor.CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty(
                ads_request_timeout_milliseconds=123,
                live_maximum_ads_personalization_time_milliseconds=123,
                prefetch_ads_request_timeout_milliseconds=123,
                prefetch_maximum_ads_personalization_time_milliseconds=123,
                vod_maximum_ads_personalization_time_milliseconds=123
            ),
            avail_suppression=mediatailor.CfnPlaybackConfiguration.AvailSuppressionProperty(
                fill_policy="fillPolicy",
                mode="mode",
                value="value"
            ),
            bumper=mediatailor.CfnPlaybackConfiguration.BumperProperty(
                end_url="endUrl",
                start_url="startUrl"
            ),
            cdn_configuration=mediatailor.CfnPlaybackConfiguration.CdnConfigurationProperty(
                ad_segment_url_prefix="adSegmentUrlPrefix",
                content_segment_url_prefix="contentSegmentUrlPrefix"
            ),
            configuration_aliases={
                "configuration_aliases_key": configuration_aliases
            },
            dash_configuration=mediatailor.CfnPlaybackConfiguration.DashConfigurationProperty(
                manifest_endpoint_prefix="manifestEndpointPrefix",
                mpd_location="mpdLocation",
                origin_manifest_type="originManifestType"
            ),
            function_mapping={
                "function_mapping_key": "functionMapping"
            },
            hls_configuration=mediatailor.CfnPlaybackConfiguration.HlsConfigurationProperty(
                manifest_endpoint_prefix="manifestEndpointPrefix"
            ),
            insertion_mode="insertionMode",
            live_pre_roll_configuration=mediatailor.CfnPlaybackConfiguration.LivePreRollConfigurationProperty(
                ad_decision_server_configuration=mediatailor.CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty(
                    vast_response=mediatailor.CfnPlaybackConfiguration.PreRollVastResponseProperty(
                        ad_sequencing_mode="adSequencingMode"
                    )
                ),
                ad_decision_server_url="adDecisionServerUrl",
                max_duration_seconds=123
            ),
            log_configuration=mediatailor.CfnPlaybackConfiguration.LogConfigurationProperty(
                percent_enabled=123,
        
                # the properties below are optional
                ads_interaction_log=mediatailor.CfnPlaybackConfiguration.AdsInteractionLogProperty(
                    exclude_event_types=["excludeEventTypes"],
                    publish_opt_in_event_types=["publishOptInEventTypes"]
                ),
                enabled_logging_strategies=["enabledLoggingStrategies"],
                manifest_service_interaction_log=mediatailor.CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty(
                    exclude_event_types=["excludeEventTypes"]
                )
            ),
            manifest_processing_rules=mediatailor.CfnPlaybackConfiguration.ManifestProcessingRulesProperty(
                ad_marker_passthrough=mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty(
                    enabled=False
                )
            ),
            personalization_threshold_seconds=123,
            slate_ad_url="slateAdUrl",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            transcode_profile_name="transcodeProfileName"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        ad_decision_server_url: builtins.str,
        name: builtins.str,
        video_content_source_url: builtins.str,
        ad_conditioning_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdConditioningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ad_decision_server_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ads_personalization_concurrency: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ads_personalization_timeouts: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        avail_suppression: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AvailSuppressionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        bumper: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.BumperProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cdn_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.CdnConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        configuration_aliases: typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], "_aws_cdk_0cae9daa.IResolvable"]] = None,
        dash_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.DashConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        function_mapping: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        hls_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.HlsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        insertion_mode: typing.Optional[builtins.str] = None,
        live_pre_roll_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.LivePreRollConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        manifest_processing_rules: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.ManifestProcessingRulesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        personalization_threshold_seconds: typing.Optional[jsii.Number] = None,
        slate_ad_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        transcode_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::PlaybackConfiguration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ad_decision_server_url: The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
        :param name: The identifier for the playback configuration.
        :param video_content_source_url: The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
        :param ad_conditioning_configuration: The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.
        :param ad_decision_server_configuration: The configuration for the request to the specified Ad Decision Server URL.
        :param ads_personalization_concurrency: The settings that control how many concurrent requests MediaTailor makes to the ad decision server (ADS).
        :param ads_personalization_timeouts: The ad decision server (ADS) request timeouts and personalization time budgets for live, VOD, and prefetch workflows.
        :param avail_suppression: The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .
        :param bumper: The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .
        :param cdn_configuration: The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
        :param configuration_aliases: The player parameters and aliases used as dynamic variables during session initialization. For more information, see `Domain Variables <https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domain.html>`_ .
        :param dash_configuration: The configuration for a DASH source.
        :param function_mapping: A map of event names to function identifiers for custom processing during session lifecycle events.
        :param hls_configuration: The configuration for HLS content.
        :param insertion_mode: The setting that controls whether players can use stitched or guided ad insertion. The default, ``STITCHED_ONLY`` , forces all player sessions to use stitched (server-side) ad insertion. Choosing ``PLAYER_SELECT`` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.
        :param live_pre_roll_configuration: The configuration for pre-roll ad insertion.
        :param log_configuration: Defines where AWS Elemental MediaTailor sends logs for the playback configuration.
        :param manifest_processing_rules: The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
        :param personalization_threshold_seconds: Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see `Ad Behavior in AWS Elemental MediaTailor <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .
        :param slate_ad_url: The URL for a video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
        :param tags: The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .
        :param transcode_profile_name: The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3dcfb97a898a80ee6a7b069e26028183e8a797f0c48fdbd4fe6ecb8ad6fb6911)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlaybackConfigurationProps(
            ad_decision_server_url=ad_decision_server_url,
            name=name,
            video_content_source_url=video_content_source_url,
            ad_conditioning_configuration=ad_conditioning_configuration,
            ad_decision_server_configuration=ad_decision_server_configuration,
            ads_personalization_concurrency=ads_personalization_concurrency,
            ads_personalization_timeouts=ads_personalization_timeouts,
            avail_suppression=avail_suppression,
            bumper=bumper,
            cdn_configuration=cdn_configuration,
            configuration_aliases=configuration_aliases,
            dash_configuration=dash_configuration,
            function_mapping=function_mapping,
            hls_configuration=hls_configuration,
            insertion_mode=insertion_mode,
            live_pre_roll_configuration=live_pre_roll_configuration,
            log_configuration=log_configuration,
            manifest_processing_rules=manifest_processing_rules,
            personalization_threshold_seconds=personalization_threshold_seconds,
            slate_ad_url=slate_ad_url,
            tags=tags,
            transcode_profile_name=transcode_profile_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForPlaybackConfiguration")
    @builtins.classmethod
    def arn_for_playback_configuration(
        cls,
        resource: "_aws_mediatailor_60404695.IPlaybackConfigurationRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3335a30b563b424b55efc3fb3fba650a85702c1595cf9e59fff9aeeca795f023)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForPlaybackConfiguration", [resource]))

    @jsii.member(jsii_name="isCfnPlaybackConfiguration")
    @builtins.classmethod
    def is_cfn_playback_configuration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPlaybackConfiguration.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b043c094b53206253d6d432de9db2a20fbb0b231bb418d502fed6f0f4914378f)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPlaybackConfiguration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6e8d0bace48ee23b08adfc8cf00f58f43f86ed9fc0b465a4b9dcfaf76c4a0da6)
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
            type_hints = cached_type_hints(_typecheckingstub__2663bd7b40c241aeca662815955b87975e8fe4bc363957cbc451c0b30548ea05)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDashConfigurationManifestEndpointPrefix")
    def attr_dash_configuration_manifest_endpoint_prefix(self) -> builtins.str:
        '''The URL generated by MediaTailor to initiate a playback session.

        The session uses server-side reporting. This setting is ignored in PUT operations.

        :cloudformationAttribute: DashConfiguration.ManifestEndpointPrefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDashConfigurationManifestEndpointPrefix"))

    @builtins.property
    @jsii.member(jsii_name="attrHlsConfigurationManifestEndpointPrefix")
    def attr_hls_configuration_manifest_endpoint_prefix(self) -> builtins.str:
        '''The URL that is used to initiate a playback session for devices that support Apple HLS.

        The session uses server-side reporting.

        :cloudformationAttribute: HlsConfiguration.ManifestEndpointPrefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHlsConfigurationManifestEndpointPrefix"))

    @builtins.property
    @jsii.member(jsii_name="attrPlaybackConfigurationArn")
    def attr_playback_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the playback configuration.

        :cloudformationAttribute: PlaybackConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlaybackConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPlaybackEndpointPrefix")
    def attr_playback_endpoint_prefix(self) -> builtins.str:
        '''The URL that the player accesses to get a manifest from MediaTailor .

        This session will use server-side reporting.

        :cloudformationAttribute: PlaybackEndpointPrefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlaybackEndpointPrefix"))

    @builtins.property
    @jsii.member(jsii_name="attrSessionInitializationEndpointPrefix")
    def attr_session_initialization_endpoint_prefix(self) -> builtins.str:
        '''The URL that the player uses to initialize a session that uses client-side reporting.

        :cloudformationAttribute: SessionInitializationEndpointPrefix
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSessionInitializationEndpointPrefix"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="playbackConfigurationRef")
    def playback_configuration_ref(
        self,
    ) -> "_aws_mediatailor_60404695.PlaybackConfigurationReference":
        '''A reference to a PlaybackConfiguration resource.'''
        return typing.cast("_aws_mediatailor_60404695.PlaybackConfigurationReference", jsii.get(self, "playbackConfigurationRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="adDecisionServerUrl")
    def ad_decision_server_url(self) -> builtins.str:
        '''The URL for the ad decision server (ADS).'''
        return typing.cast(builtins.str, jsii.get(self, "adDecisionServerUrl"))

    @ad_decision_server_url.setter
    def ad_decision_server_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b4b56f24629d4c9547e0b37415660678e3944b62d46a1e55902b5e6c66efe7c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adDecisionServerUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The identifier for the playback configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__77c686fa09a4612a1bcc44cf669fb2ff9905ec398da89167e8b0280d8f86750d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="videoContentSourceUrl")
    def video_content_source_url(self) -> builtins.str:
        '''The URL prefix for the parent manifest for the stream, minus the asset ID.'''
        return typing.cast(builtins.str, jsii.get(self, "videoContentSourceUrl"))

    @video_content_source_url.setter
    def video_content_source_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__75b50d6fe13101dc70996fb19d5c8a163f6176ddcd37a0ebe0b08f5f768c4caf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "videoContentSourceUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="adConditioningConfiguration")
    def ad_conditioning_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdConditioningConfigurationProperty"]]:
        '''The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdConditioningConfigurationProperty"]], jsii.get(self, "adConditioningConfiguration"))

    @ad_conditioning_configuration.setter
    def ad_conditioning_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdConditioningConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bb81abb7826e9e9444261d39e06ed23acbaea73a559203da5ca788273a1bbc94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adConditioningConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="adDecisionServerConfiguration")
    def ad_decision_server_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty"]]:
        '''The configuration for the request to the specified Ad Decision Server URL.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty"]], jsii.get(self, "adDecisionServerConfiguration"))

    @ad_decision_server_configuration.setter
    def ad_decision_server_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__22beebeb31ad301089cab0d08fffbf7d70892dcdea0070ebbc8c036efa8475c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adDecisionServerConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="adsPersonalizationConcurrency")
    def ads_personalization_concurrency(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty"]]:
        '''The settings that control how many concurrent requests MediaTailor makes to the ad decision server (ADS).'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty"]], jsii.get(self, "adsPersonalizationConcurrency"))

    @ads_personalization_concurrency.setter
    def ads_personalization_concurrency(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2a729a919a8e3f978c846240e1014b7c0fec80dd63195aa5866c57644d4451e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adsPersonalizationConcurrency", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="adsPersonalizationTimeouts")
    def ads_personalization_timeouts(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty"]]:
        '''The ad decision server (ADS) request timeouts and personalization time budgets for live, VOD, and prefetch workflows.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty"]], jsii.get(self, "adsPersonalizationTimeouts"))

    @ads_personalization_timeouts.setter
    def ads_personalization_timeouts(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__13ee4b8d1ac254be276c7782458b9e78d24c83f92c6f56af8e12ac5df9cc47fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adsPersonalizationTimeouts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availSuppression")
    def avail_suppression(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AvailSuppressionProperty"]]:
        '''The configuration for avail suppression, also known as ad suppression.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AvailSuppressionProperty"]], jsii.get(self, "availSuppression"))

    @avail_suppression.setter
    def avail_suppression(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AvailSuppressionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ace1eb1809c3c05a0b25523b0f61020aa7d5a69057cdffb522c74d7881b0c1c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availSuppression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bumper")
    def bumper(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.BumperProperty"]]:
        '''The configuration for bumpers.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.BumperProperty"]], jsii.get(self, "bumper"))

    @bumper.setter
    def bumper(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.BumperProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e9796c91ff0edc4be04998ed524be6012eae7fa3574e5c120fe393fab79a2a12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bumper", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cdnConfiguration")
    def cdn_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.CdnConfigurationProperty"]]:
        '''The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.CdnConfigurationProperty"]], jsii.get(self, "cdnConfiguration"))

    @cdn_configuration.setter
    def cdn_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.CdnConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a8cdb9ae7c7cff86d16687474d65af7b5ddb86256dce88926d439a4c82e07acf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configurationAliases")
    def configuration_aliases(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], "_aws_cdk_0cae9daa.IResolvable"]]:
        '''The player parameters and aliases used as dynamic variables during session initialization.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "configurationAliases"))

    @configuration_aliases.setter
    def configuration_aliases(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5e98fdfcc661f8c91728f46bbafe4c5c1160d075338a4b6e66789b7147006439)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationAliases", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dashConfiguration")
    def dash_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.DashConfigurationProperty"]]:
        '''The configuration for a DASH source.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.DashConfigurationProperty"]], jsii.get(self, "dashConfiguration"))

    @dash_configuration.setter
    def dash_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.DashConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e1528a1dd277ec2643ed08e71e4d817660b15a7515d36800d1a4c45be4bdd944)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="functionMapping")
    def function_mapping(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
        '''A map of event names to function identifiers for custom processing during session lifecycle events.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "functionMapping"))

    @function_mapping.setter
    def function_mapping(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7ce9f9a164e16917763fbfce05ef66083a15fe183466a65359b9714cccd1b42c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionMapping", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hlsConfiguration")
    def hls_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.HlsConfigurationProperty"]]:
        '''The configuration for HLS content.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.HlsConfigurationProperty"]], jsii.get(self, "hlsConfiguration"))

    @hls_configuration.setter
    def hls_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.HlsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8c53800db93b8d74956b4a23e4372e79b770aeb9e98d1001196859bcb54e01d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hlsConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="insertionMode")
    def insertion_mode(self) -> typing.Optional[builtins.str]:
        '''The setting that controls whether players can use stitched or guided ad insertion.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insertionMode"))

    @insertion_mode.setter
    def insertion_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8db08ab0a15b5e71226bad5d4d94682032ded680bfe3f777d4f4ef02bad39cbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insertionMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="livePreRollConfiguration")
    def live_pre_roll_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LivePreRollConfigurationProperty"]]:
        '''The configuration for pre-roll ad insertion.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LivePreRollConfigurationProperty"]], jsii.get(self, "livePreRollConfiguration"))

    @live_pre_roll_configuration.setter
    def live_pre_roll_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LivePreRollConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d20db08db40dad827f8fdbbfd9ec60bdd03cf18a0cf5f764aedb5ed9040d782f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "livePreRollConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LogConfigurationProperty"]]:
        '''Defines where AWS Elemental MediaTailor sends logs for the playback configuration.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LogConfigurationProperty"]], jsii.get(self, "logConfiguration"))

    @log_configuration.setter
    def log_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LogConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a6fbfb7358fa4aedc54b5bb197d51ad46d862c18709b40e671060ad3ab400894)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="manifestProcessingRules")
    def manifest_processing_rules(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.ManifestProcessingRulesProperty"]]:
        '''The configuration for manifest processing rules.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.ManifestProcessingRulesProperty"]], jsii.get(self, "manifestProcessingRules"))

    @manifest_processing_rules.setter
    def manifest_processing_rules(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.ManifestProcessingRulesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7ef2be3172d1df94da8603df93c79aa68aa713132917a7f79ee5d67eca13bdc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifestProcessingRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="personalizationThresholdSeconds")
    def personalization_threshold_seconds(self) -> typing.Optional[jsii.Number]:
        '''Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "personalizationThresholdSeconds"))

    @personalization_threshold_seconds.setter
    def personalization_threshold_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cf4368b8d6051e265005679584bc63cae740383861026b06e26c9de1f0954cee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "personalizationThresholdSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="slateAdUrl")
    def slate_ad_url(self) -> typing.Optional[builtins.str]:
        '''The URL for a video asset to transcode and use to fill in time that's not used by ads.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slateAdUrl"))

    @slate_ad_url.setter
    def slate_ad_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__905f1e5f55e6f998cb17136c0f4a82bcebc656a336f14fbf28f45aab3b7ab881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slateAdUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags to assign to the playback configuration.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d76f0247a7421af76c87f40a095ad78f3c6ad9b0a567e02e8daca4c67eee9302)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="transcodeProfileName")
    def transcode_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name that is used to associate this playback configuration with a custom transcode profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transcodeProfileName"))

    @transcode_profile_name.setter
    def transcode_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ab6a880d781d782bb5f703943747735b9af031af290dd1ad2e9ebe2732d26c2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transcodeProfileName", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AdConditioningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "streaming_media_file_conditioning": "streamingMediaFileConditioning",
        },
    )
    class AdConditioningConfigurationProperty:
        def __init__(self, *, streaming_media_file_conditioning: builtins.str) -> None:
            '''The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns.

            :param streaming_media_file_conditioning: For ads that have media files with streaming delivery and supported file extensions, indicates what transcoding action MediaTailor takes when it first receives these ads from the ADS. ``TRANSCODE`` indicates that MediaTailor must transcode the ads. ``NONE`` indicates that you have already transcoded the ads outside of MediaTailor and don't need them transcoded as part of the ad insertion workflow. For more information about ad conditioning see `Using preconditioned ads <https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html>`_ in the AWS Elemental MediaTailor user guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                ad_conditioning_configuration_property = mediatailor.CfnPlaybackConfiguration.AdConditioningConfigurationProperty(
                    streaming_media_file_conditioning="streamingMediaFileConditioning"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__86f7802737ba8294b0aa8d203c7f9bc7ff38b98bf17f1f9066c772b203c711ea)
                check_type(argname="argument streaming_media_file_conditioning", value=streaming_media_file_conditioning, expected_type=type_hints["streaming_media_file_conditioning"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "streaming_media_file_conditioning": streaming_media_file_conditioning,
            }

        @builtins.property
        def streaming_media_file_conditioning(self) -> builtins.str:
            '''For ads that have media files with streaming delivery and supported file extensions, indicates what transcoding action MediaTailor takes when it first receives these ads from the ADS.

            ``TRANSCODE`` indicates that MediaTailor must transcode the ads. ``NONE`` indicates that you have already transcoded the ads outside of MediaTailor and don't need them transcoded as part of the ad insertion workflow. For more information about ad conditioning see `Using preconditioned ads <https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html>`_ in the AWS Elemental MediaTailor user guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adconditioningconfiguration.html#cfn-mediatailor-playbackconfiguration-adconditioningconfiguration-streamingmediafileconditioning
            '''
            result = self._values.get("streaming_media_file_conditioning")
            assert result is not None, "Required property 'streaming_media_file_conditioning' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdConditioningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"http_request": "httpRequest", "vast_response": "vastResponse"},
    )
    class AdDecisionServerConfigurationProperty:
        def __init__(
            self,
            *,
            http_request: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.HttpRequestProperty", typing.Dict[builtins.str, typing.Any]]],
            vast_response: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.VastResponseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration for the request to the specified Ad Decision Server URL.

            :param http_request: The configuration for the request to the Ad Decision Server URL.
            :param vast_response: The configuration for how MediaTailor processes the VAST response returned by the Ad Decision Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                ad_decision_server_configuration_property = mediatailor.CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty(
                    http_request=mediatailor.CfnPlaybackConfiguration.HttpRequestProperty(
                        body="body",
                        compress_request="compressRequest",
                        headers={
                            "headers_key": "headers"
                        },
                        http_method="httpMethod"
                    ),
                
                    # the properties below are optional
                    vast_response=mediatailor.CfnPlaybackConfiguration.VastResponseProperty(
                        ad_sequencing_mode="adSequencingMode"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__be522b7afa0a40f87526bb5baa285488ee37ade9f2edd720c05a21cdcf1ba383)
                check_type(argname="argument http_request", value=http_request, expected_type=type_hints["http_request"])
                check_type(argname="argument vast_response", value=vast_response, expected_type=type_hints["vast_response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "http_request": http_request,
            }
            if vast_response is not None:
                self._values["vast_response"] = vast_response

        @builtins.property
        def http_request(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.HttpRequestProperty"]:
            '''The configuration for the request to the Ad Decision Server URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration.html#cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration-httprequest
            '''
            result = self._values.get("http_request")
            assert result is not None, "Required property 'http_request' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.HttpRequestProperty"], result)

        @builtins.property
        def vast_response(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.VastResponseProperty"]]:
            '''The configuration for how MediaTailor processes the VAST response returned by the Ad Decision Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-addecisionserverconfiguration.html#cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration-vastresponse
            '''
            result = self._values.get("vast_response")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.VastResponseProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdDecisionServerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class AdMarkerPassthroughProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
        ) -> None:
            '''For HLS, when set to ``true`` , MediaTailor passes through ``EXT-X-CUE-IN`` , ``EXT-X-CUE-OUT`` , and ``EXT-X-SPLICEPOINT-SCTE35`` ad markers from the origin manifest to the MediaTailor personalized manifest.

            No logic is applied to these ad markers. For example, if ``EXT-X-CUE-OUT`` has a value of ``60`` , but no ads are filled for that ad break, MediaTailor will not set the value to ``0`` .

            :param enabled: Enables ad marker passthrough for your configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                ad_marker_passthrough_property = mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__c84cc8c470c35ea1870d24a6e58a722cc2d0952d699c858000349755866ccea6)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Enables ad marker passthrough for your configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html#cfn-mediatailor-playbackconfiguration-admarkerpassthrough-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdMarkerPassthroughProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AdsInteractionLogProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exclude_event_types": "excludeEventTypes",
            "publish_opt_in_event_types": "publishOptInEventTypes",
        },
    )
    class AdsInteractionLogProperty:
        def __init__(
            self,
            *,
            exclude_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            publish_opt_in_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).

            For more information about ADS logs, inlcuding descriptions of the event types, see `MediaTailor ADS logs description and event types <https://docs.aws.amazon.com/mediatailor/latest/ug/ads-log-format.html>`_ in AWS Elemental MediaTailor User Guide.

            :param exclude_event_types: Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.
            :param publish_opt_in_event_types: Indicates that MediaTailor emits ``RAW_ADS_RESPONSE`` logs for playback sessions that are initialized with this configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adsinteractionlog.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                ads_interaction_log_property = mediatailor.CfnPlaybackConfiguration.AdsInteractionLogProperty(
                    exclude_event_types=["excludeEventTypes"],
                    publish_opt_in_event_types=["publishOptInEventTypes"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__325f2da032e4a3f14a765ea1c946c8707bfd649b7df813a9bf9d270b2edfcd0f)
                check_type(argname="argument exclude_event_types", value=exclude_event_types, expected_type=type_hints["exclude_event_types"])
                check_type(argname="argument publish_opt_in_event_types", value=publish_opt_in_event_types, expected_type=type_hints["publish_opt_in_event_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclude_event_types is not None:
                self._values["exclude_event_types"] = exclude_event_types
            if publish_opt_in_event_types is not None:
                self._values["publish_opt_in_event_types"] = publish_opt_in_event_types

        @builtins.property
        def exclude_event_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adsinteractionlog.html#cfn-mediatailor-playbackconfiguration-adsinteractionlog-excludeeventtypes
            '''
            result = self._values.get("exclude_event_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def publish_opt_in_event_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''Indicates that MediaTailor emits ``RAW_ADS_RESPONSE`` logs for playback sessions that are initialized with this configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adsinteractionlog.html#cfn-mediatailor-playbackconfiguration-adsinteractionlog-publishoptineventtypes
            '''
            result = self._values.get("publish_opt_in_event_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdsInteractionLogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_vod_vast_parallelization": "enableVodVastParallelization",
            "max_concurrent_ads_requests": "maxConcurrentAdsRequests",
        },
    )
    class AdsPersonalizationConcurrencyProperty:
        def __init__(
            self,
            *,
            enable_vod_vast_parallelization: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
            max_concurrent_ads_requests: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The settings that control how many concurrent requests MediaTailor makes to the ad decision server (ADS).

            :param enable_vod_vast_parallelization: Enables parallel processing of ADS requests in VOD workflows when the ADS returns VAST responses. The default is false.
            :param max_concurrent_ads_requests: The maximum number of simultaneous requests that MediaTailor makes to the ADS for each manifest request. The default is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                ads_personalization_concurrency_property = mediatailor.CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty(
                    enable_vod_vast_parallelization=False,
                    max_concurrent_ads_requests=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__c54804620edf90d6d14b94d837c502afb0350e36766d359c51c934fb9de93d10)
                check_type(argname="argument enable_vod_vast_parallelization", value=enable_vod_vast_parallelization, expected_type=type_hints["enable_vod_vast_parallelization"])
                check_type(argname="argument max_concurrent_ads_requests", value=max_concurrent_ads_requests, expected_type=type_hints["max_concurrent_ads_requests"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_vod_vast_parallelization is not None:
                self._values["enable_vod_vast_parallelization"] = enable_vod_vast_parallelization
            if max_concurrent_ads_requests is not None:
                self._values["max_concurrent_ads_requests"] = max_concurrent_ads_requests

        @builtins.property
        def enable_vod_vast_parallelization(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
            '''Enables parallel processing of ADS requests in VOD workflows when the ADS returns VAST responses.

            The default is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency.html#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency-enablevodvastparallelization
            '''
            result = self._values.get("enable_vod_vast_parallelization")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

        @builtins.property
        def max_concurrent_ads_requests(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of simultaneous requests that MediaTailor makes to the ADS for each manifest request.

            The default is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationconcurrency.html#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency-maxconcurrentadsrequests
            '''
            result = self._values.get("max_concurrent_ads_requests")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdsPersonalizationConcurrencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ads_request_timeout_milliseconds": "adsRequestTimeoutMilliseconds",
            "live_maximum_ads_personalization_time_milliseconds": "liveMaximumAdsPersonalizationTimeMilliseconds",
            "prefetch_ads_request_timeout_milliseconds": "prefetchAdsRequestTimeoutMilliseconds",
            "prefetch_maximum_ads_personalization_time_milliseconds": "prefetchMaximumAdsPersonalizationTimeMilliseconds",
            "vod_maximum_ads_personalization_time_milliseconds": "vodMaximumAdsPersonalizationTimeMilliseconds",
        },
    )
    class AdsPersonalizationTimeoutsProperty:
        def __init__(
            self,
            *,
            ads_request_timeout_milliseconds: typing.Optional[jsii.Number] = None,
            live_maximum_ads_personalization_time_milliseconds: typing.Optional[jsii.Number] = None,
            prefetch_ads_request_timeout_milliseconds: typing.Optional[jsii.Number] = None,
            prefetch_maximum_ads_personalization_time_milliseconds: typing.Optional[jsii.Number] = None,
            vod_maximum_ads_personalization_time_milliseconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ad decision server (ADS) request timeouts and personalization time budgets for live, VOD, and prefetch workflows.

            :param ads_request_timeout_milliseconds: The maximum time, in milliseconds, that MediaTailor waits for a single ADS response during live or VOD playback. The default is 3000.
            :param live_maximum_ads_personalization_time_milliseconds: The maximum total time, in milliseconds, that MediaTailor spends on ADS activity for live manifests. The default is 10000.
            :param prefetch_ads_request_timeout_milliseconds: The maximum time, in milliseconds, that MediaTailor waits for a single ADS response during prefetch retrieval. If not set, MediaTailor uses the AdsRequestTimeoutMilliseconds value.
            :param prefetch_maximum_ads_personalization_time_milliseconds: The maximum total time, in milliseconds, that MediaTailor spends on ADS activity during prefetch retrieval.
            :param vod_maximum_ads_personalization_time_milliseconds: The maximum total time, in milliseconds, that MediaTailor spends on ADS activity for VOD manifests. The default is 10000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                ads_personalization_timeouts_property = mediatailor.CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty(
                    ads_request_timeout_milliseconds=123,
                    live_maximum_ads_personalization_time_milliseconds=123,
                    prefetch_ads_request_timeout_milliseconds=123,
                    prefetch_maximum_ads_personalization_time_milliseconds=123,
                    vod_maximum_ads_personalization_time_milliseconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__081de2ae59707e39bdb75d2de6531849e92a0be4913aa6286dd36f4fce70bbee)
                check_type(argname="argument ads_request_timeout_milliseconds", value=ads_request_timeout_milliseconds, expected_type=type_hints["ads_request_timeout_milliseconds"])
                check_type(argname="argument live_maximum_ads_personalization_time_milliseconds", value=live_maximum_ads_personalization_time_milliseconds, expected_type=type_hints["live_maximum_ads_personalization_time_milliseconds"])
                check_type(argname="argument prefetch_ads_request_timeout_milliseconds", value=prefetch_ads_request_timeout_milliseconds, expected_type=type_hints["prefetch_ads_request_timeout_milliseconds"])
                check_type(argname="argument prefetch_maximum_ads_personalization_time_milliseconds", value=prefetch_maximum_ads_personalization_time_milliseconds, expected_type=type_hints["prefetch_maximum_ads_personalization_time_milliseconds"])
                check_type(argname="argument vod_maximum_ads_personalization_time_milliseconds", value=vod_maximum_ads_personalization_time_milliseconds, expected_type=type_hints["vod_maximum_ads_personalization_time_milliseconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ads_request_timeout_milliseconds is not None:
                self._values["ads_request_timeout_milliseconds"] = ads_request_timeout_milliseconds
            if live_maximum_ads_personalization_time_milliseconds is not None:
                self._values["live_maximum_ads_personalization_time_milliseconds"] = live_maximum_ads_personalization_time_milliseconds
            if prefetch_ads_request_timeout_milliseconds is not None:
                self._values["prefetch_ads_request_timeout_milliseconds"] = prefetch_ads_request_timeout_milliseconds
            if prefetch_maximum_ads_personalization_time_milliseconds is not None:
                self._values["prefetch_maximum_ads_personalization_time_milliseconds"] = prefetch_maximum_ads_personalization_time_milliseconds
            if vod_maximum_ads_personalization_time_milliseconds is not None:
                self._values["vod_maximum_ads_personalization_time_milliseconds"] = vod_maximum_ads_personalization_time_milliseconds

        @builtins.property
        def ads_request_timeout_milliseconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum time, in milliseconds, that MediaTailor waits for a single ADS response during live or VOD playback.

            The default is 3000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts.html#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-adsrequesttimeoutmilliseconds
            '''
            result = self._values.get("ads_request_timeout_milliseconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def live_maximum_ads_personalization_time_milliseconds(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum total time, in milliseconds, that MediaTailor spends on ADS activity for live manifests.

            The default is 10000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts.html#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-livemaximumadspersonalizationtimemilliseconds
            '''
            result = self._values.get("live_maximum_ads_personalization_time_milliseconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def prefetch_ads_request_timeout_milliseconds(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum time, in milliseconds, that MediaTailor waits for a single ADS response during prefetch retrieval.

            If not set, MediaTailor uses the AdsRequestTimeoutMilliseconds value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts.html#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-prefetchadsrequesttimeoutmilliseconds
            '''
            result = self._values.get("prefetch_ads_request_timeout_milliseconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def prefetch_maximum_ads_personalization_time_milliseconds(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum total time, in milliseconds, that MediaTailor spends on ADS activity during prefetch retrieval.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts.html#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-prefetchmaximumadspersonalizationtimemilliseconds
            '''
            result = self._values.get("prefetch_maximum_ads_personalization_time_milliseconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vod_maximum_ads_personalization_time_milliseconds(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum total time, in milliseconds, that MediaTailor spends on ADS activity for VOD manifests.

            The default is 10000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-adspersonalizationtimeouts.html#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts-vodmaximumadspersonalizationtimemilliseconds
            '''
            result = self._values.get("vod_maximum_ads_personalization_time_milliseconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdsPersonalizationTimeoutsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.AvailSuppressionProperty",
        jsii_struct_bases=[],
        name_mapping={"fill_policy": "fillPolicy", "mode": "mode", "value": "value"},
    )
    class AvailSuppressionProperty:
        def __init__(
            self,
            *,
            fill_policy: typing.Optional[builtins.str] = None,
            mode: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for avail suppression, also known as ad suppression.

            For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .

            :param fill_policy: Defines the policy to apply to the avail suppression mode. ``BEHIND_LIVE_EDGE`` will always use the full avail suppression policy. ``AFTER_LIVE_EDGE`` mode can be used to invoke partial ad break fills when a session starts mid-break.
            :param mode: Sets the ad suppression mode. By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to ``BEHIND_LIVE_EDGE`` , ad suppression is active and MediaTailor won't fill ad breaks on or behind the ad suppression Value time in the manifest lookback window. When Mode is set to ``AFTER_LIVE_EDGE`` , ad suppression is active and MediaTailor won't fill ad breaks that are within the live edge plus the avail suppression value.
            :param value: A live edge offset time in HH:MM:SS. MediaTailor won't fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor won't fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor won't fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but won't fill ad breaks on or behind 45 minutes behind the live edge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                avail_suppression_property = mediatailor.CfnPlaybackConfiguration.AvailSuppressionProperty(
                    fill_policy="fillPolicy",
                    mode="mode",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8b4195a89a44a68af7fade1bdaaea19a0b3104ca5fc40a34ac2c5440a8d5f1d0)
                check_type(argname="argument fill_policy", value=fill_policy, expected_type=type_hints["fill_policy"])
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if fill_policy is not None:
                self._values["fill_policy"] = fill_policy
            if mode is not None:
                self._values["mode"] = mode
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def fill_policy(self) -> typing.Optional[builtins.str]:
            '''Defines the policy to apply to the avail suppression mode.

            ``BEHIND_LIVE_EDGE`` will always use the full avail suppression policy. ``AFTER_LIVE_EDGE`` mode can be used to invoke partial ad break fills when a session starts mid-break.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html#cfn-mediatailor-playbackconfiguration-availsuppression-fillpolicy
            '''
            result = self._values.get("fill_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''Sets the ad suppression mode.

            By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to ``BEHIND_LIVE_EDGE`` , ad suppression is active and MediaTailor won't fill ad breaks on or behind the ad suppression Value time in the manifest lookback window. When Mode is set to ``AFTER_LIVE_EDGE`` , ad suppression is active and MediaTailor won't fill ad breaks that are within the live edge plus the avail suppression value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html#cfn-mediatailor-playbackconfiguration-availsuppression-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''A live edge offset time in HH:MM:SS.

            MediaTailor won't fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor won't fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor won't fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but won't fill ad breaks on or behind 45 minutes behind the live edge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html#cfn-mediatailor-playbackconfiguration-availsuppression-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailSuppressionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.BumperProperty",
        jsii_struct_bases=[],
        name_mapping={"end_url": "endUrl", "start_url": "startUrl"},
    )
    class BumperProperty:
        def __init__(
            self,
            *,
            end_url: typing.Optional[builtins.str] = None,
            start_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for bumpers.

            Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .

            :param end_url: The URL for the end bumper asset.
            :param start_url: The URL for the start bumper asset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                bumper_property = mediatailor.CfnPlaybackConfiguration.BumperProperty(
                    end_url="endUrl",
                    start_url="startUrl"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__d4d8e62c25a38e7667cc4c7f67e131b03585a6b02ccb1e6956572e91491c2565)
                check_type(argname="argument end_url", value=end_url, expected_type=type_hints["end_url"])
                check_type(argname="argument start_url", value=start_url, expected_type=type_hints["start_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if end_url is not None:
                self._values["end_url"] = end_url
            if start_url is not None:
                self._values["start_url"] = start_url

        @builtins.property
        def end_url(self) -> typing.Optional[builtins.str]:
            '''The URL for the end bumper asset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html#cfn-mediatailor-playbackconfiguration-bumper-endurl
            '''
            result = self._values.get("end_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_url(self) -> typing.Optional[builtins.str]:
            '''The URL for the start bumper asset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html#cfn-mediatailor-playbackconfiguration-bumper-starturl
            '''
            result = self._values.get("start_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BumperProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.CdnConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_segment_url_prefix": "adSegmentUrlPrefix",
            "content_segment_url_prefix": "contentSegmentUrlPrefix",
        },
    )
    class CdnConfigurationProperty:
        def __init__(
            self,
            *,
            ad_segment_url_prefix: typing.Optional[builtins.str] = None,
            content_segment_url_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

            :param ad_segment_url_prefix: A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the origin ads.mediatailor. ** .amazonaws.com. Then specify the rule's name in this ``AdSegmentUrlPrefix`` . When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
            :param content_segment_url_prefix: A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this ``ContentSegmentUrlPrefix`` . When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                cdn_configuration_property = mediatailor.CfnPlaybackConfiguration.CdnConfigurationProperty(
                    ad_segment_url_prefix="adSegmentUrlPrefix",
                    content_segment_url_prefix="contentSegmentUrlPrefix"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__11ed9c00b014872bf1ce7a32f613cee3497f59c3a8f8ed7c34d59e731f7a30a1)
                check_type(argname="argument ad_segment_url_prefix", value=ad_segment_url_prefix, expected_type=type_hints["ad_segment_url_prefix"])
                check_type(argname="argument content_segment_url_prefix", value=content_segment_url_prefix, expected_type=type_hints["content_segment_url_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_segment_url_prefix is not None:
                self._values["ad_segment_url_prefix"] = ad_segment_url_prefix
            if content_segment_url_prefix is not None:
                self._values["content_segment_url_prefix"] = content_segment_url_prefix

        @builtins.property
        def ad_segment_url_prefix(self) -> typing.Optional[builtins.str]:
            '''A non-default content delivery network (CDN) to serve ad segments.

            By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the origin ads.mediatailor. ** .amazonaws.com. Then specify the rule's name in this ``AdSegmentUrlPrefix`` . When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration-adsegmenturlprefix
            '''
            result = self._values.get("ad_segment_url_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def content_segment_url_prefix(self) -> typing.Optional[builtins.str]:
            '''A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server.

            First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this ``ContentSegmentUrlPrefix`` . When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration-contentsegmenturlprefix
            '''
            result = self._values.get("content_segment_url_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CdnConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.DashConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_endpoint_prefix": "manifestEndpointPrefix",
            "mpd_location": "mpdLocation",
            "origin_manifest_type": "originManifestType",
        },
    )
    class DashConfigurationProperty:
        def __init__(
            self,
            *,
            manifest_endpoint_prefix: typing.Optional[builtins.str] = None,
            mpd_location: typing.Optional[builtins.str] = None,
            origin_manifest_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for DASH content.

            :param manifest_endpoint_prefix: The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations.
            :param mpd_location: The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are ``DISABLED`` and ``EMT_DEFAULT`` . The ``EMT_DEFAULT`` setting enables the inclusion of the tag and is the default value.
            :param origin_manifest_type: The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to ``SINGLE_PERIOD`` . The default setting is ``MULTI_PERIOD`` . For multi-period manifests, omit this setting or set it to ``MULTI_PERIOD`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                dash_configuration_property = mediatailor.CfnPlaybackConfiguration.DashConfigurationProperty(
                    manifest_endpoint_prefix="manifestEndpointPrefix",
                    mpd_location="mpdLocation",
                    origin_manifest_type="originManifestType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ed436176dc8bad043834221f15764e2997c06a895bb8dc9c71dc24d9d4c62fe8)
                check_type(argname="argument manifest_endpoint_prefix", value=manifest_endpoint_prefix, expected_type=type_hints["manifest_endpoint_prefix"])
                check_type(argname="argument mpd_location", value=mpd_location, expected_type=type_hints["mpd_location"])
                check_type(argname="argument origin_manifest_type", value=origin_manifest_type, expected_type=type_hints["origin_manifest_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if manifest_endpoint_prefix is not None:
                self._values["manifest_endpoint_prefix"] = manifest_endpoint_prefix
            if mpd_location is not None:
                self._values["mpd_location"] = mpd_location
            if origin_manifest_type is not None:
                self._values["origin_manifest_type"] = origin_manifest_type

        @builtins.property
        def manifest_endpoint_prefix(self) -> typing.Optional[builtins.str]:
            '''The URL generated by MediaTailor to initiate a playback session.

            The session uses server-side reporting. This setting is ignored in PUT operations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-manifestendpointprefix
            '''
            result = self._values.get("manifest_endpoint_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mpd_location(self) -> typing.Optional[builtins.str]:
            '''The setting that controls whether MediaTailor includes the Location tag in DASH manifests.

            MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are ``DISABLED`` and ``EMT_DEFAULT`` . The ``EMT_DEFAULT`` setting enables the inclusion of the tag and is the default value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-mpdlocation
            '''
            result = self._values.get("mpd_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def origin_manifest_type(self) -> typing.Optional[builtins.str]:
            '''The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests.

            If your origin server produces single-period manifests, set this to ``SINGLE_PERIOD`` . The default setting is ``MULTI_PERIOD`` . For multi-period manifests, omit this setting or set it to ``MULTI_PERIOD`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-originmanifesttype
            '''
            result = self._values.get("origin_manifest_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.HlsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"manifest_endpoint_prefix": "manifestEndpointPrefix"},
    )
    class HlsConfigurationProperty:
        def __init__(
            self,
            *,
            manifest_endpoint_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for HLS content.

            :param manifest_endpoint_prefix: The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                hls_configuration_property = mediatailor.CfnPlaybackConfiguration.HlsConfigurationProperty(
                    manifest_endpoint_prefix="manifestEndpointPrefix"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__cc73c21d5b8ef9a10443ded7266b5dc44c0980daadbc5f8f5a49b9793967e1ed)
                check_type(argname="argument manifest_endpoint_prefix", value=manifest_endpoint_prefix, expected_type=type_hints["manifest_endpoint_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if manifest_endpoint_prefix is not None:
                self._values["manifest_endpoint_prefix"] = manifest_endpoint_prefix

        @builtins.property
        def manifest_endpoint_prefix(self) -> typing.Optional[builtins.str]:
            '''The URL that is used to initiate a playback session for devices that support Apple HLS.

            The session uses server-side reporting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html#cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix
            '''
            result = self._values.get("manifest_endpoint_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.HttpRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "body": "body",
            "compress_request": "compressRequest",
            "headers": "headers",
            "http_method": "httpMethod",
        },
    )
    class HttpRequestProperty:
        def __init__(
            self,
            *,
            body: typing.Optional[builtins.str] = None,
            compress_request: typing.Optional[builtins.str] = None,
            headers: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
            http_method: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for the request to the Ad Decision Server URL.

            :param body: The body of the request to the Ad Decision Server URL. The maximum length is 100,000 characters.
            :param compress_request: The compression type of the request sent to the Ad Decision Server URL. Only the POST HTTP Method permits compression other than NONE.
            :param headers: The headers in the request sent to the Ad Decision Server URL. The max length is 10,000 characters.
            :param http_method: Supported HTTP Methods for the request to the Ad Decision Server URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-httprequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                http_request_property = mediatailor.CfnPlaybackConfiguration.HttpRequestProperty(
                    body="body",
                    compress_request="compressRequest",
                    headers={
                        "headers_key": "headers"
                    },
                    http_method="httpMethod"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__7a1a27fdd711151047a9a372fb7f330c24afc446e3e97dd914e66a4a4a637017)
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument compress_request", value=compress_request, expected_type=type_hints["compress_request"])
                check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
                check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if body is not None:
                self._values["body"] = body
            if compress_request is not None:
                self._values["compress_request"] = compress_request
            if headers is not None:
                self._values["headers"] = headers
            if http_method is not None:
                self._values["http_method"] = http_method

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''The body of the request to the Ad Decision Server URL.

            The maximum length is 100,000 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-httprequest.html#cfn-mediatailor-playbackconfiguration-httprequest-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compress_request(self) -> typing.Optional[builtins.str]:
            '''The compression type of the request sent to the Ad Decision Server URL.

            Only the POST HTTP Method permits compression other than NONE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-httprequest.html#cfn-mediatailor-playbackconfiguration-httprequest-compressrequest
            '''
            result = self._values.get("compress_request")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def headers(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''The headers in the request sent to the Ad Decision Server URL.

            The max length is 10,000 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-httprequest.html#cfn-mediatailor-playbackconfiguration-httprequest-headers
            '''
            result = self._values.get("headers")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def http_method(self) -> typing.Optional[builtins.str]:
            '''Supported HTTP Methods for the request to the Ad Decision Server URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-httprequest.html#cfn-mediatailor-playbackconfiguration-httprequest-httpmethod
            '''
            result = self._values.get("http_method")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.LivePreRollConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_decision_server_configuration": "adDecisionServerConfiguration",
            "ad_decision_server_url": "adDecisionServerUrl",
            "max_duration_seconds": "maxDurationSeconds",
        },
    )
    class LivePreRollConfigurationProperty:
        def __init__(
            self,
            *,
            ad_decision_server_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ad_decision_server_url: typing.Optional[builtins.str] = None,
            max_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The configuration for pre-roll ad insertion.

            :param ad_decision_server_configuration: The configuration for the request to the pre-roll Ad Decision Server.
            :param ad_decision_server_url: The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
            :param max_duration_seconds: The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                live_pre_roll_configuration_property = mediatailor.CfnPlaybackConfiguration.LivePreRollConfigurationProperty(
                    ad_decision_server_configuration=mediatailor.CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty(
                        vast_response=mediatailor.CfnPlaybackConfiguration.PreRollVastResponseProperty(
                            ad_sequencing_mode="adSequencingMode"
                        )
                    ),
                    ad_decision_server_url="adDecisionServerUrl",
                    max_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__be1326ff9046a5c3b87adfaac42a0610149574f9d367d1c04949ccf8a48d1a93)
                check_type(argname="argument ad_decision_server_configuration", value=ad_decision_server_configuration, expected_type=type_hints["ad_decision_server_configuration"])
                check_type(argname="argument ad_decision_server_url", value=ad_decision_server_url, expected_type=type_hints["ad_decision_server_url"])
                check_type(argname="argument max_duration_seconds", value=max_duration_seconds, expected_type=type_hints["max_duration_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_decision_server_configuration is not None:
                self._values["ad_decision_server_configuration"] = ad_decision_server_configuration
            if ad_decision_server_url is not None:
                self._values["ad_decision_server_url"] = ad_decision_server_url
            if max_duration_seconds is not None:
                self._values["max_duration_seconds"] = max_duration_seconds

        @builtins.property
        def ad_decision_server_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty"]]:
            '''The configuration for the request to the pre-roll Ad Decision Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverconfiguration
            '''
            result = self._values.get("ad_decision_server_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty"]], result)

        @builtins.property
        def ad_decision_server_url(self) -> typing.Optional[builtins.str]:
            '''The URL for the ad decision server (ADS) for pre-roll ads.

            This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverurl
            '''
            result = self._values.get("ad_decision_server_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum allowed duration for the pre-roll ad avail.

            AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-maxdurationseconds
            '''
            result = self._values.get("max_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LivePreRollConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "percent_enabled": "percentEnabled",
            "ads_interaction_log": "adsInteractionLog",
            "enabled_logging_strategies": "enabledLoggingStrategies",
            "manifest_service_interaction_log": "manifestServiceInteractionLog",
        },
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            percent_enabled: jsii.Number,
            ads_interaction_log: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdsInteractionLogProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enabled_logging_strategies: typing.Optional[typing.Sequence[builtins.str]] = None,
            manifest_service_interaction_log: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines where AWS Elemental MediaTailor sends logs for the playback configuration.

            :param percent_enabled: The percentage of session logs that MediaTailor sends to your configured log destination. For example, if your playback configuration has 1000 sessions and ``percentEnabled`` is set to ``60`` , MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the `debug log mode <https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html>`_ . Valid values: ``0`` - ``100``
            :param ads_interaction_log: Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).
            :param enabled_logging_strategies: The method used for collecting logs from AWS Elemental MediaTailor. ``LEGACY_CLOUDWATCH`` indicates that MediaTailor is sending logs directly to Amazon CloudWatch Logs. ``VENDED_LOGS`` indicates that MediaTailor is sending logs to CloudWatch, which then vends the logs to your destination of choice. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.
            :param manifest_service_interaction_log: Settings for customizing what events are included in logs for interactions with the origin server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-logconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                log_configuration_property = mediatailor.CfnPlaybackConfiguration.LogConfigurationProperty(
                    percent_enabled=123,
                
                    # the properties below are optional
                    ads_interaction_log=mediatailor.CfnPlaybackConfiguration.AdsInteractionLogProperty(
                        exclude_event_types=["excludeEventTypes"],
                        publish_opt_in_event_types=["publishOptInEventTypes"]
                    ),
                    enabled_logging_strategies=["enabledLoggingStrategies"],
                    manifest_service_interaction_log=mediatailor.CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty(
                        exclude_event_types=["excludeEventTypes"]
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0b1a16aa41d90a41939aee256096b129464d60c87f4e8ac32c6ce9c43de9dcfd)
                check_type(argname="argument percent_enabled", value=percent_enabled, expected_type=type_hints["percent_enabled"])
                check_type(argname="argument ads_interaction_log", value=ads_interaction_log, expected_type=type_hints["ads_interaction_log"])
                check_type(argname="argument enabled_logging_strategies", value=enabled_logging_strategies, expected_type=type_hints["enabled_logging_strategies"])
                check_type(argname="argument manifest_service_interaction_log", value=manifest_service_interaction_log, expected_type=type_hints["manifest_service_interaction_log"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "percent_enabled": percent_enabled,
            }
            if ads_interaction_log is not None:
                self._values["ads_interaction_log"] = ads_interaction_log
            if enabled_logging_strategies is not None:
                self._values["enabled_logging_strategies"] = enabled_logging_strategies
            if manifest_service_interaction_log is not None:
                self._values["manifest_service_interaction_log"] = manifest_service_interaction_log

        @builtins.property
        def percent_enabled(self) -> jsii.Number:
            '''The percentage of session logs that MediaTailor sends to your configured log destination.

            For example, if your playback configuration has 1000 sessions and ``percentEnabled`` is set to ``60`` , MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the `debug log mode <https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html>`_ .

            Valid values: ``0`` - ``100``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-logconfiguration.html#cfn-mediatailor-playbackconfiguration-logconfiguration-percentenabled
            '''
            result = self._values.get("percent_enabled")
            assert result is not None, "Required property 'percent_enabled' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def ads_interaction_log(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsInteractionLogProperty"]]:
            '''Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-logconfiguration.html#cfn-mediatailor-playbackconfiguration-logconfiguration-adsinteractionlog
            '''
            result = self._values.get("ads_interaction_log")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsInteractionLogProperty"]], result)

        @builtins.property
        def enabled_logging_strategies(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The method used for collecting logs from AWS Elemental MediaTailor.

            ``LEGACY_CLOUDWATCH`` indicates that MediaTailor is sending logs directly to Amazon CloudWatch Logs. ``VENDED_LOGS`` indicates that MediaTailor is sending logs to CloudWatch, which then vends the logs to your destination of choice. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-logconfiguration.html#cfn-mediatailor-playbackconfiguration-logconfiguration-enabledloggingstrategies
            '''
            result = self._values.get("enabled_logging_strategies")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def manifest_service_interaction_log(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty"]]:
            '''Settings for customizing what events are included in logs for interactions with the origin server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-logconfiguration.html#cfn-mediatailor-playbackconfiguration-logconfiguration-manifestserviceinteractionlog
            '''
            result = self._values.get("manifest_service_interaction_log")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.ManifestProcessingRulesProperty",
        jsii_struct_bases=[],
        name_mapping={"ad_marker_passthrough": "adMarkerPassthrough"},
    )
    class ManifestProcessingRulesProperty:
        def __init__(
            self,
            *,
            ad_marker_passthrough: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdMarkerPassthroughProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration for manifest processing rules.

            Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

            :param ad_marker_passthrough: For HLS, when set to ``true`` , MediaTailor passes through ``EXT-X-CUE-IN`` , ``EXT-X-CUE-OUT`` , and ``EXT-X-SPLICEPOINT-SCTE35`` ad markers from the origin manifest to the MediaTailor personalized manifest. No logic is applied to these ad markers. For example, if ``EXT-X-CUE-OUT`` has a value of ``60`` , but no ads are filled for that ad break, MediaTailor will not set the value to ``0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                manifest_processing_rules_property = mediatailor.CfnPlaybackConfiguration.ManifestProcessingRulesProperty(
                    ad_marker_passthrough=mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ef5bb7a5b9697fa8ca9b867a5d8f7f8c6041a353ed9fad8ec9b06f14fd300d73)
                check_type(argname="argument ad_marker_passthrough", value=ad_marker_passthrough, expected_type=type_hints["ad_marker_passthrough"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_marker_passthrough is not None:
                self._values["ad_marker_passthrough"] = ad_marker_passthrough

        @builtins.property
        def ad_marker_passthrough(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdMarkerPassthroughProperty"]]:
            '''For HLS, when set to ``true`` , MediaTailor passes through ``EXT-X-CUE-IN`` , ``EXT-X-CUE-OUT`` , and ``EXT-X-SPLICEPOINT-SCTE35`` ad markers from the origin manifest to the MediaTailor personalized manifest.

            No logic is applied to these ad markers. For example, if ``EXT-X-CUE-OUT`` has a value of ``60`` , but no ads are filled for that ad break, MediaTailor will not set the value to ``0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html#cfn-mediatailor-playbackconfiguration-manifestprocessingrules-admarkerpassthrough
            '''
            result = self._values.get("ad_marker_passthrough")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdMarkerPassthroughProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManifestProcessingRulesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty",
        jsii_struct_bases=[],
        name_mapping={"exclude_event_types": "excludeEventTypes"},
    )
    class ManifestServiceInteractionLogProperty:
        def __init__(
            self,
            *,
            exclude_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Settings for customizing what events are included in logs for interactions with the origin server.

            For more information about manifest service logs, including descriptions of the event types, see `MediaTailor manifest logs description and event types <https://docs.aws.amazon.com/mediatailor/latest/ug/log-types.html>`_ in AWS Elemental MediaTailor User Guide.

            :param exclude_event_types: Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                manifest_service_interaction_log_property = mediatailor.CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty(
                    exclude_event_types=["excludeEventTypes"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__877d8a60ce1cb5812848b2604b2ff4a34e5662596f05cca7a6a335a5facd5374)
                check_type(argname="argument exclude_event_types", value=exclude_event_types, expected_type=type_hints["exclude_event_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclude_event_types is not None:
                self._values["exclude_event_types"] = exclude_event_types

        @builtins.property
        def exclude_event_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog.html#cfn-mediatailor-playbackconfiguration-manifestserviceinteractionlog-excludeeventtypes
            '''
            result = self._values.get("exclude_event_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManifestServiceInteractionLogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vast_response": "vastResponse"},
    )
    class PreRollAdDecisionServerConfigurationProperty:
        def __init__(
            self,
            *,
            vast_response: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.PreRollVastResponseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration for the request to the pre-roll Ad Decision Server.

            :param vast_response: The configuration for how MediaTailor processes the VAST response returned by the pre-roll Ad Decision Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                pre_roll_ad_decision_server_configuration_property = mediatailor.CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty(
                    vast_response=mediatailor.CfnPlaybackConfiguration.PreRollVastResponseProperty(
                        ad_sequencing_mode="adSequencingMode"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__c891247344a5816c5f6036ffe8b027890782702417987f5fe28421b1757a52f5)
                check_type(argname="argument vast_response", value=vast_response, expected_type=type_hints["vast_response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vast_response is not None:
                self._values["vast_response"] = vast_response

        @builtins.property
        def vast_response(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.PreRollVastResponseProperty"]]:
            '''The configuration for how MediaTailor processes the VAST response returned by the pre-roll Ad Decision Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration.html#cfn-mediatailor-playbackconfiguration-prerolladdecisionserverconfiguration-vastresponse
            '''
            result = self._values.get("vast_response")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.PreRollVastResponseProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PreRollAdDecisionServerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.PreRollVastResponseProperty",
        jsii_struct_bases=[],
        name_mapping={"ad_sequencing_mode": "adSequencingMode"},
    )
    class PreRollVastResponseProperty:
        def __init__(
            self,
            *,
            ad_sequencing_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for how MediaTailor processes the VAST response returned by the pre-roll Ad Decision Server.

            :param ad_sequencing_mode: Determines how MediaTailor sequences ads returned in the pre-roll VAST response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-prerollvastresponse.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                pre_roll_vast_response_property = mediatailor.CfnPlaybackConfiguration.PreRollVastResponseProperty(
                    ad_sequencing_mode="adSequencingMode"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__770bca0bb4db614052f95822f0ce3e52f118ce264f511205bda617ca7797829a)
                check_type(argname="argument ad_sequencing_mode", value=ad_sequencing_mode, expected_type=type_hints["ad_sequencing_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_sequencing_mode is not None:
                self._values["ad_sequencing_mode"] = ad_sequencing_mode

        @builtins.property
        def ad_sequencing_mode(self) -> typing.Optional[builtins.str]:
            '''Determines how MediaTailor sequences ads returned in the pre-roll VAST response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-prerollvastresponse.html#cfn-mediatailor-playbackconfiguration-prerollvastresponse-adsequencingmode
            '''
            result = self._values.get("ad_sequencing_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PreRollVastResponseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfiguration.VastResponseProperty",
        jsii_struct_bases=[],
        name_mapping={"ad_sequencing_mode": "adSequencingMode"},
    )
    class VastResponseProperty:
        def __init__(
            self,
            *,
            ad_sequencing_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for how MediaTailor processes the VAST response returned by the Ad Decision Server.

            :param ad_sequencing_mode: Determines how MediaTailor sequences ads returned in the VAST response from the Ad Decision Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-vastresponse.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                vast_response_property = mediatailor.CfnPlaybackConfiguration.VastResponseProperty(
                    ad_sequencing_mode="adSequencingMode"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__b5eccc314698469708f3b54b63cf366c2cda8be0723d3d1b1140bc18e7ffe980)
                check_type(argname="argument ad_sequencing_mode", value=ad_sequencing_mode, expected_type=type_hints["ad_sequencing_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_sequencing_mode is not None:
                self._values["ad_sequencing_mode"] = ad_sequencing_mode

        @builtins.property
        def ad_sequencing_mode(self) -> typing.Optional[builtins.str]:
            '''Determines how MediaTailor sequences ads returned in the VAST response from the Ad Decision Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-vastresponse.html#cfn-mediatailor-playbackconfiguration-vastresponse-adsequencingmode
            '''
            result = self._values.get("ad_sequencing_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VastResponseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnPlaybackConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "ad_decision_server_url": "adDecisionServerUrl",
        "name": "name",
        "video_content_source_url": "videoContentSourceUrl",
        "ad_conditioning_configuration": "adConditioningConfiguration",
        "ad_decision_server_configuration": "adDecisionServerConfiguration",
        "ads_personalization_concurrency": "adsPersonalizationConcurrency",
        "ads_personalization_timeouts": "adsPersonalizationTimeouts",
        "avail_suppression": "availSuppression",
        "bumper": "bumper",
        "cdn_configuration": "cdnConfiguration",
        "configuration_aliases": "configurationAliases",
        "dash_configuration": "dashConfiguration",
        "function_mapping": "functionMapping",
        "hls_configuration": "hlsConfiguration",
        "insertion_mode": "insertionMode",
        "live_pre_roll_configuration": "livePreRollConfiguration",
        "log_configuration": "logConfiguration",
        "manifest_processing_rules": "manifestProcessingRules",
        "personalization_threshold_seconds": "personalizationThresholdSeconds",
        "slate_ad_url": "slateAdUrl",
        "tags": "tags",
        "transcode_profile_name": "transcodeProfileName",
    },
)
class CfnPlaybackConfigurationProps:
    def __init__(
        self,
        *,
        ad_decision_server_url: builtins.str,
        name: builtins.str,
        video_content_source_url: builtins.str,
        ad_conditioning_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdConditioningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ad_decision_server_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ads_personalization_concurrency: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ads_personalization_timeouts: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        avail_suppression: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.AvailSuppressionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        bumper: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.BumperProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cdn_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.CdnConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        configuration_aliases: typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], "_aws_cdk_0cae9daa.IResolvable"]] = None,
        dash_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.DashConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        function_mapping: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        hls_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.HlsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        insertion_mode: typing.Optional[builtins.str] = None,
        live_pre_roll_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.LivePreRollConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        manifest_processing_rules: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPlaybackConfiguration.ManifestProcessingRulesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        personalization_threshold_seconds: typing.Optional[jsii.Number] = None,
        slate_ad_url: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        transcode_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlaybackConfiguration``.

        :param ad_decision_server_url: The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
        :param name: The identifier for the playback configuration.
        :param video_content_source_url: The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
        :param ad_conditioning_configuration: The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.
        :param ad_decision_server_configuration: The configuration for the request to the specified Ad Decision Server URL.
        :param ads_personalization_concurrency: The settings that control how many concurrent requests MediaTailor makes to the ad decision server (ADS).
        :param ads_personalization_timeouts: The ad decision server (ADS) request timeouts and personalization time budgets for live, VOD, and prefetch workflows.
        :param avail_suppression: The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .
        :param bumper: The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .
        :param cdn_configuration: The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
        :param configuration_aliases: The player parameters and aliases used as dynamic variables during session initialization. For more information, see `Domain Variables <https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domain.html>`_ .
        :param dash_configuration: The configuration for a DASH source.
        :param function_mapping: A map of event names to function identifiers for custom processing during session lifecycle events.
        :param hls_configuration: The configuration for HLS content.
        :param insertion_mode: The setting that controls whether players can use stitched or guided ad insertion. The default, ``STITCHED_ONLY`` , forces all player sessions to use stitched (server-side) ad insertion. Choosing ``PLAYER_SELECT`` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.
        :param live_pre_roll_configuration: The configuration for pre-roll ad insertion.
        :param log_configuration: Defines where AWS Elemental MediaTailor sends logs for the playback configuration.
        :param manifest_processing_rules: The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
        :param personalization_threshold_seconds: Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see `Ad Behavior in AWS Elemental MediaTailor <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .
        :param slate_ad_url: The URL for a video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
        :param tags: The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .
        :param transcode_profile_name: The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            # configuration_aliases: Any
            
            cfn_playback_configuration_props = mediatailor.CfnPlaybackConfigurationProps(
                ad_decision_server_url="adDecisionServerUrl",
                name="name",
                video_content_source_url="videoContentSourceUrl",
            
                # the properties below are optional
                ad_conditioning_configuration=mediatailor.CfnPlaybackConfiguration.AdConditioningConfigurationProperty(
                    streaming_media_file_conditioning="streamingMediaFileConditioning"
                ),
                ad_decision_server_configuration=mediatailor.CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty(
                    http_request=mediatailor.CfnPlaybackConfiguration.HttpRequestProperty(
                        body="body",
                        compress_request="compressRequest",
                        headers={
                            "headers_key": "headers"
                        },
                        http_method="httpMethod"
                    ),
            
                    # the properties below are optional
                    vast_response=mediatailor.CfnPlaybackConfiguration.VastResponseProperty(
                        ad_sequencing_mode="adSequencingMode"
                    )
                ),
                ads_personalization_concurrency=mediatailor.CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty(
                    enable_vod_vast_parallelization=False,
                    max_concurrent_ads_requests=123
                ),
                ads_personalization_timeouts=mediatailor.CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty(
                    ads_request_timeout_milliseconds=123,
                    live_maximum_ads_personalization_time_milliseconds=123,
                    prefetch_ads_request_timeout_milliseconds=123,
                    prefetch_maximum_ads_personalization_time_milliseconds=123,
                    vod_maximum_ads_personalization_time_milliseconds=123
                ),
                avail_suppression=mediatailor.CfnPlaybackConfiguration.AvailSuppressionProperty(
                    fill_policy="fillPolicy",
                    mode="mode",
                    value="value"
                ),
                bumper=mediatailor.CfnPlaybackConfiguration.BumperProperty(
                    end_url="endUrl",
                    start_url="startUrl"
                ),
                cdn_configuration=mediatailor.CfnPlaybackConfiguration.CdnConfigurationProperty(
                    ad_segment_url_prefix="adSegmentUrlPrefix",
                    content_segment_url_prefix="contentSegmentUrlPrefix"
                ),
                configuration_aliases={
                    "configuration_aliases_key": configuration_aliases
                },
                dash_configuration=mediatailor.CfnPlaybackConfiguration.DashConfigurationProperty(
                    manifest_endpoint_prefix="manifestEndpointPrefix",
                    mpd_location="mpdLocation",
                    origin_manifest_type="originManifestType"
                ),
                function_mapping={
                    "function_mapping_key": "functionMapping"
                },
                hls_configuration=mediatailor.CfnPlaybackConfiguration.HlsConfigurationProperty(
                    manifest_endpoint_prefix="manifestEndpointPrefix"
                ),
                insertion_mode="insertionMode",
                live_pre_roll_configuration=mediatailor.CfnPlaybackConfiguration.LivePreRollConfigurationProperty(
                    ad_decision_server_configuration=mediatailor.CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty(
                        vast_response=mediatailor.CfnPlaybackConfiguration.PreRollVastResponseProperty(
                            ad_sequencing_mode="adSequencingMode"
                        )
                    ),
                    ad_decision_server_url="adDecisionServerUrl",
                    max_duration_seconds=123
                ),
                log_configuration=mediatailor.CfnPlaybackConfiguration.LogConfigurationProperty(
                    percent_enabled=123,
            
                    # the properties below are optional
                    ads_interaction_log=mediatailor.CfnPlaybackConfiguration.AdsInteractionLogProperty(
                        exclude_event_types=["excludeEventTypes"],
                        publish_opt_in_event_types=["publishOptInEventTypes"]
                    ),
                    enabled_logging_strategies=["enabledLoggingStrategies"],
                    manifest_service_interaction_log=mediatailor.CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty(
                        exclude_event_types=["excludeEventTypes"]
                    )
                ),
                manifest_processing_rules=mediatailor.CfnPlaybackConfiguration.ManifestProcessingRulesProperty(
                    ad_marker_passthrough=mediatailor.CfnPlaybackConfiguration.AdMarkerPassthroughProperty(
                        enabled=False
                    )
                ),
                personalization_threshold_seconds=123,
                slate_ad_url="slateAdUrl",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                transcode_profile_name="transcodeProfileName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__935886ab495203cc213786b925e7fd8fe4acd3f9db5864d4f1f5c011539346f8)
            check_type(argname="argument ad_decision_server_url", value=ad_decision_server_url, expected_type=type_hints["ad_decision_server_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument video_content_source_url", value=video_content_source_url, expected_type=type_hints["video_content_source_url"])
            check_type(argname="argument ad_conditioning_configuration", value=ad_conditioning_configuration, expected_type=type_hints["ad_conditioning_configuration"])
            check_type(argname="argument ad_decision_server_configuration", value=ad_decision_server_configuration, expected_type=type_hints["ad_decision_server_configuration"])
            check_type(argname="argument ads_personalization_concurrency", value=ads_personalization_concurrency, expected_type=type_hints["ads_personalization_concurrency"])
            check_type(argname="argument ads_personalization_timeouts", value=ads_personalization_timeouts, expected_type=type_hints["ads_personalization_timeouts"])
            check_type(argname="argument avail_suppression", value=avail_suppression, expected_type=type_hints["avail_suppression"])
            check_type(argname="argument bumper", value=bumper, expected_type=type_hints["bumper"])
            check_type(argname="argument cdn_configuration", value=cdn_configuration, expected_type=type_hints["cdn_configuration"])
            check_type(argname="argument configuration_aliases", value=configuration_aliases, expected_type=type_hints["configuration_aliases"])
            check_type(argname="argument dash_configuration", value=dash_configuration, expected_type=type_hints["dash_configuration"])
            check_type(argname="argument function_mapping", value=function_mapping, expected_type=type_hints["function_mapping"])
            check_type(argname="argument hls_configuration", value=hls_configuration, expected_type=type_hints["hls_configuration"])
            check_type(argname="argument insertion_mode", value=insertion_mode, expected_type=type_hints["insertion_mode"])
            check_type(argname="argument live_pre_roll_configuration", value=live_pre_roll_configuration, expected_type=type_hints["live_pre_roll_configuration"])
            check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
            check_type(argname="argument manifest_processing_rules", value=manifest_processing_rules, expected_type=type_hints["manifest_processing_rules"])
            check_type(argname="argument personalization_threshold_seconds", value=personalization_threshold_seconds, expected_type=type_hints["personalization_threshold_seconds"])
            check_type(argname="argument slate_ad_url", value=slate_ad_url, expected_type=type_hints["slate_ad_url"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transcode_profile_name", value=transcode_profile_name, expected_type=type_hints["transcode_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ad_decision_server_url": ad_decision_server_url,
            "name": name,
            "video_content_source_url": video_content_source_url,
        }
        if ad_conditioning_configuration is not None:
            self._values["ad_conditioning_configuration"] = ad_conditioning_configuration
        if ad_decision_server_configuration is not None:
            self._values["ad_decision_server_configuration"] = ad_decision_server_configuration
        if ads_personalization_concurrency is not None:
            self._values["ads_personalization_concurrency"] = ads_personalization_concurrency
        if ads_personalization_timeouts is not None:
            self._values["ads_personalization_timeouts"] = ads_personalization_timeouts
        if avail_suppression is not None:
            self._values["avail_suppression"] = avail_suppression
        if bumper is not None:
            self._values["bumper"] = bumper
        if cdn_configuration is not None:
            self._values["cdn_configuration"] = cdn_configuration
        if configuration_aliases is not None:
            self._values["configuration_aliases"] = configuration_aliases
        if dash_configuration is not None:
            self._values["dash_configuration"] = dash_configuration
        if function_mapping is not None:
            self._values["function_mapping"] = function_mapping
        if hls_configuration is not None:
            self._values["hls_configuration"] = hls_configuration
        if insertion_mode is not None:
            self._values["insertion_mode"] = insertion_mode
        if live_pre_roll_configuration is not None:
            self._values["live_pre_roll_configuration"] = live_pre_roll_configuration
        if log_configuration is not None:
            self._values["log_configuration"] = log_configuration
        if manifest_processing_rules is not None:
            self._values["manifest_processing_rules"] = manifest_processing_rules
        if personalization_threshold_seconds is not None:
            self._values["personalization_threshold_seconds"] = personalization_threshold_seconds
        if slate_ad_url is not None:
            self._values["slate_ad_url"] = slate_ad_url
        if tags is not None:
            self._values["tags"] = tags
        if transcode_profile_name is not None:
            self._values["transcode_profile_name"] = transcode_profile_name

    @builtins.property
    def ad_decision_server_url(self) -> builtins.str:
        '''The URL for the ad decision server (ADS).

        This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-addecisionserverurl
        '''
        result = self._values.get("ad_decision_server_url")
        assert result is not None, "Required property 'ad_decision_server_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The identifier for the playback configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def video_content_source_url(self) -> builtins.str:
        '''The URL prefix for the parent manifest for the stream, minus the asset ID.

        The maximum length is 512 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-videocontentsourceurl
        '''
        result = self._values.get("video_content_source_url")
        assert result is not None, "Required property 'video_content_source_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ad_conditioning_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdConditioningConfigurationProperty"]]:
        '''The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-adconditioningconfiguration
        '''
        result = self._values.get("ad_conditioning_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdConditioningConfigurationProperty"]], result)

    @builtins.property
    def ad_decision_server_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty"]]:
        '''The configuration for the request to the specified Ad Decision Server URL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-addecisionserverconfiguration
        '''
        result = self._values.get("ad_decision_server_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty"]], result)

    @builtins.property
    def ads_personalization_concurrency(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty"]]:
        '''The settings that control how many concurrent requests MediaTailor makes to the ad decision server (ADS).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-adspersonalizationconcurrency
        '''
        result = self._values.get("ads_personalization_concurrency")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty"]], result)

    @builtins.property
    def ads_personalization_timeouts(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty"]]:
        '''The ad decision server (ADS) request timeouts and personalization time budgets for live, VOD, and prefetch workflows.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-adspersonalizationtimeouts
        '''
        result = self._values.get("ads_personalization_timeouts")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty"]], result)

    @builtins.property
    def avail_suppression(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AvailSuppressionProperty"]]:
        '''The configuration for avail suppression, also known as ad suppression.

        For more information about ad suppression, see `Ad Suppression <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-availsuppression
        '''
        result = self._values.get("avail_suppression")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.AvailSuppressionProperty"]], result)

    @builtins.property
    def bumper(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.BumperProperty"]]:
        '''The configuration for bumpers.

        Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see `Bumpers <https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-bumper
        '''
        result = self._values.get("bumper")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.BumperProperty"]], result)

    @builtins.property
    def cdn_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.CdnConfigurationProperty"]]:
        '''The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration
        '''
        result = self._values.get("cdn_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.CdnConfigurationProperty"]], result)

    @builtins.property
    def configuration_aliases(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], "_aws_cdk_0cae9daa.IResolvable"]]:
        '''The player parameters and aliases used as dynamic variables during session initialization.

        For more information, see `Domain Variables <https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domain.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-configurationaliases
        '''
        result = self._values.get("configuration_aliases")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], "_aws_cdk_0cae9daa.IResolvable"]], result)

    @builtins.property
    def dash_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.DashConfigurationProperty"]]:
        '''The configuration for a DASH source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration
        '''
        result = self._values.get("dash_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.DashConfigurationProperty"]], result)

    @builtins.property
    def function_mapping(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
        '''A map of event names to function identifiers for custom processing during session lifecycle events.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-functionmapping
        '''
        result = self._values.get("function_mapping")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def hls_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.HlsConfigurationProperty"]]:
        '''The configuration for HLS content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-hlsconfiguration
        '''
        result = self._values.get("hls_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.HlsConfigurationProperty"]], result)

    @builtins.property
    def insertion_mode(self) -> typing.Optional[builtins.str]:
        '''The setting that controls whether players can use stitched or guided ad insertion.

        The default, ``STITCHED_ONLY`` , forces all player sessions to use stitched (server-side) ad insertion. Choosing ``PLAYER_SELECT`` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-insertionmode
        '''
        result = self._values.get("insertion_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def live_pre_roll_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LivePreRollConfigurationProperty"]]:
        '''The configuration for pre-roll ad insertion.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration
        '''
        result = self._values.get("live_pre_roll_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LivePreRollConfigurationProperty"]], result)

    @builtins.property
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LogConfigurationProperty"]]:
        '''Defines where AWS Elemental MediaTailor sends logs for the playback configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-logconfiguration
        '''
        result = self._values.get("log_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.LogConfigurationProperty"]], result)

    @builtins.property
    def manifest_processing_rules(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.ManifestProcessingRulesProperty"]]:
        '''The configuration for manifest processing rules.

        Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-manifestprocessingrules
        '''
        result = self._values.get("manifest_processing_rules")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPlaybackConfiguration.ManifestProcessingRulesProperty"]], result)

    @builtins.property
    def personalization_threshold_seconds(self) -> typing.Optional[jsii.Number]:
        '''Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break.

        If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see `Ad Behavior in AWS Elemental MediaTailor <https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-personalizationthresholdseconds
        '''
        result = self._values.get("personalization_threshold_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def slate_ad_url(self) -> typing.Optional[builtins.str]:
        '''The URL for a video asset to transcode and use to fill in time that's not used by ads.

        AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-slateadurl
        '''
        result = self._values.get("slate_ad_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags to assign to the playback configuration.

        Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def transcode_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name that is used to associate this playback configuration with a custom transcode profile.

        This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-transcodeprofilename
        '''
        result = self._values.get("transcode_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlaybackConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_mediatailor_60404695.IPrefetchScheduleRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnPrefetchSchedule(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule",
):
    '''Definition of AWS::MediaTailor::PrefetchSchedule Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html
    :cloudformationResource: AWS::MediaTailor::PrefetchSchedule
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        cfn_prefetch_schedule = mediatailor.CfnPrefetchSchedule(self, "MyCfnPrefetchSchedule",
            name="name",
            playback_configuration_name="playbackConfigurationName",
        
            # the properties below are optional
            consumption=mediatailor.CfnPrefetchSchedule.PrefetchConsumptionProperty(
                end_time="endTime",
        
                # the properties below are optional
                avail_matching_criteria=[mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty(
                    dynamic_variable="dynamicVariable",
                    operator="operator"
                )],
                start_time="startTime"
            ),
            recurring_prefetch_configuration=mediatailor.CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty(
                end_time="endTime",
                recurring_consumption=mediatailor.CfnPrefetchSchedule.RecurringConsumptionProperty(
                    avail_matching_criteria=[mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty(
                        dynamic_variable="dynamicVariable",
                        operator="operator"
                    )],
                    retrieved_ad_expiration_seconds=123
                ),
                recurring_retrieval=mediatailor.CfnPrefetchSchedule.RecurringRetrievalProperty(
                    delay_after_avail_end_seconds=123,
                    dynamic_variables={
                        "dynamic_variables_key": "dynamicVariables"
                    },
                    traffic_shaping_retrieval_window=mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty(
                        retrieval_window_duration_seconds=123
                    ),
                    traffic_shaping_tps_configuration=mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty(
                        peak_concurrent_users=123,
                        peak_tps=123
                    ),
                    traffic_shaping_type="trafficShapingType"
                ),
        
                # the properties below are optional
                start_time="startTime"
            ),
            retrieval=mediatailor.CfnPrefetchSchedule.PrefetchRetrievalProperty(
                end_time="endTime",
        
                # the properties below are optional
                dynamic_variables={
                    "dynamic_variables_key": "dynamicVariables"
                },
                start_time="startTime",
                traffic_shaping_retrieval_window=mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty(
                    retrieval_window_duration_seconds=123
                ),
                traffic_shaping_tps_configuration=mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty(
                    peak_concurrent_users=123,
                    peak_tps=123
                ),
                traffic_shaping_type="trafficShapingType"
            ),
            schedule_type="scheduleType",
            stream_id="streamId",
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
        playback_configuration_name: builtins.str,
        consumption: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.PrefetchConsumptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        recurring_prefetch_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        retrieval: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.PrefetchRetrievalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule_type: typing.Optional[builtins.str] = None,
        stream_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::PrefetchSchedule``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name to assign to the prefetch schedule.
        :param playback_configuration_name: The name of the playback configuration.
        :param consumption: 
        :param recurring_prefetch_configuration: 
        :param retrieval: 
        :param schedule_type: The frequency that MediaTailor creates prefetch schedules.
        :param stream_id: An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration.
        :param tags: The tags assigned to the prefetch schedule.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cda230bb96c6a9dde0582b55cf131524f9dfc5b99d2f757c2fc0d3232e38bf74)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrefetchScheduleProps(
            name=name,
            playback_configuration_name=playback_configuration_name,
            consumption=consumption,
            recurring_prefetch_configuration=recurring_prefetch_configuration,
            retrieval=retrieval,
            schedule_type=schedule_type,
            stream_id=stream_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForPrefetchSchedule")
    @builtins.classmethod
    def arn_for_prefetch_schedule(
        cls,
        resource: "_aws_mediatailor_60404695.IPrefetchScheduleRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e9494a130ab023cb8f1efc4abac0a1a99f59b2235691c53eb96ba51ecebaa725)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForPrefetchSchedule", [resource]))

    @jsii.member(jsii_name="isCfnPrefetchSchedule")
    @builtins.classmethod
    def is_cfn_prefetch_schedule(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPrefetchSchedule.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e7b415e15129c07ef912c53b46ad5b2fef8f90e537665ed39a283b8dbf7e3ba2)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPrefetchSchedule", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0bff129f6ff7e96dfe9ed305243681d972d3a5078f8e1f8bd03dfc7a6bd77e51)
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
            type_hints = cached_type_hints(_typecheckingstub__50bf6fc42f5a3633ecf526f1a716df7113700d9218eaa290702d12ba126775e8)
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
        '''The Amazon Resource Name (ARN) of the prefetch schedule.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="prefetchScheduleRef")
    def prefetch_schedule_ref(
        self,
    ) -> "_aws_mediatailor_60404695.PrefetchScheduleReference":
        '''A reference to a PrefetchSchedule resource.'''
        return typing.cast("_aws_mediatailor_60404695.PrefetchScheduleReference", jsii.get(self, "prefetchScheduleRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name to assign to the prefetch schedule.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dd8fc0fd997068a5a9913c04ff0cfc0f761c7da140916bf37f02b29f5cc7742a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="playbackConfigurationName")
    def playback_configuration_name(self) -> builtins.str:
        '''The name of the playback configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "playbackConfigurationName"))

    @playback_configuration_name.setter
    def playback_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9dabe2e2008888c9c945448e0d661fbdd8564f685ee56d6a1779e29d4cad4ec4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "playbackConfigurationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="consumption")
    def consumption(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchConsumptionProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchConsumptionProperty"]], jsii.get(self, "consumption"))

    @consumption.setter
    def consumption(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchConsumptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c2b6374edcf95c8a9b4cce6071faefac50f1526b162dfaf0479417803056905d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recurringPrefetchConfiguration")
    def recurring_prefetch_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty"]], jsii.get(self, "recurringPrefetchConfiguration"))

    @recurring_prefetch_configuration.setter
    def recurring_prefetch_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d4dceeb4970cc6d2cadedc0218d4ac6586f2d7683ae6a1b0268ddce2f6705f92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurringPrefetchConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retrieval")
    def retrieval(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchRetrievalProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchRetrievalProperty"]], jsii.get(self, "retrieval"))

    @retrieval.setter
    def retrieval(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchRetrievalProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a8b1ee3296f2489c46c64734a0363c25b87a5d06c5571dee7c59e32959a089c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retrieval", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scheduleType")
    def schedule_type(self) -> typing.Optional[builtins.str]:
        '''The frequency that MediaTailor creates prefetch schedules.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleType"))

    @schedule_type.setter
    def schedule_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__98ea4297602a4c698f4a7a596e39444f37df263a76058421ef00d6ab44adc7e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a1d1ce3c2153a851f8bc18f289d2e3c3b7e8626f0492a8b9c5007908df5d1248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the prefetch schedule.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2898d6ee5d6cf5febc03f59aedc49d2edbe5e8595ca50d955206285ca9833352)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"dynamic_variable": "dynamicVariable", "operator": "operator"},
    )
    class AvailMatchingCriteriaProperty:
        def __init__(
            self,
            *,
            dynamic_variable: builtins.str,
            operator: builtins.str,
        ) -> None:
            '''
            :param dynamic_variable: The dynamic variable(s) that MediaTailor should use as avail matching criteria.
            :param operator: For the DynamicVariable specified in AvailMatchingCriteria, the Operator that is used for the comparison.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-availmatchingcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                avail_matching_criteria_property = mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty(
                    dynamic_variable="dynamicVariable",
                    operator="operator"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__e58a7f144bd17d3319e9ad03250010949871dc8836ac9ac67237335d03084d7c)
                check_type(argname="argument dynamic_variable", value=dynamic_variable, expected_type=type_hints["dynamic_variable"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dynamic_variable": dynamic_variable,
                "operator": operator,
            }

        @builtins.property
        def dynamic_variable(self) -> builtins.str:
            '''The dynamic variable(s) that MediaTailor should use as avail matching criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-availmatchingcriteria.html#cfn-mediatailor-prefetchschedule-availmatchingcriteria-dynamicvariable
            '''
            result = self._values.get("dynamic_variable")
            assert result is not None, "Required property 'dynamic_variable' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def operator(self) -> builtins.str:
            '''For the DynamicVariable specified in AvailMatchingCriteria, the Operator that is used for the comparison.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-availmatchingcriteria.html#cfn-mediatailor-prefetchschedule-availmatchingcriteria-operator
            '''
            result = self._values.get("operator")
            assert result is not None, "Required property 'operator' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AvailMatchingCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule.PrefetchConsumptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_time": "endTime",
            "avail_matching_criteria": "availMatchingCriteria",
            "start_time": "startTime",
        },
    )
    class PrefetchConsumptionProperty:
        def __init__(
            self,
            *,
            end_time: builtins.str,
            avail_matching_criteria: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.AvailMatchingCriteriaProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            start_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param end_time: The time when MediaTailor no longer considers the prefetched ads for use in an ad break, as an ISO 8601 date-time.
            :param avail_matching_criteria: If you only want MediaTailor to insert prefetched ads into avails that match specific dynamic variables, set the avail matching criteria.
            :param start_time: The time when prefetched ads are considered for use in an ad break, as an ISO 8601 date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchconsumption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                prefetch_consumption_property = mediatailor.CfnPrefetchSchedule.PrefetchConsumptionProperty(
                    end_time="endTime",
                
                    # the properties below are optional
                    avail_matching_criteria=[mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty(
                        dynamic_variable="dynamicVariable",
                        operator="operator"
                    )],
                    start_time="startTime"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__18c177a23efbd7d3f4f9690a9e27fa151a0a90be1132ce2f4efab08eabda9232)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument avail_matching_criteria", value=avail_matching_criteria, expected_type=type_hints["avail_matching_criteria"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_time": end_time,
            }
            if avail_matching_criteria is not None:
                self._values["avail_matching_criteria"] = avail_matching_criteria
            if start_time is not None:
                self._values["start_time"] = start_time

        @builtins.property
        def end_time(self) -> builtins.str:
            '''The time when MediaTailor no longer considers the prefetched ads for use in an ad break, as an ISO 8601 date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchconsumption.html#cfn-mediatailor-prefetchschedule-prefetchconsumption-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def avail_matching_criteria(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.AvailMatchingCriteriaProperty"]]]]:
            '''If you only want MediaTailor to insert prefetched ads into avails that match specific dynamic variables, set the avail matching criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchconsumption.html#cfn-mediatailor-prefetchschedule-prefetchconsumption-availmatchingcriteria
            '''
            result = self._values.get("avail_matching_criteria")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.AvailMatchingCriteriaProperty"]]]], result)

        @builtins.property
        def start_time(self) -> typing.Optional[builtins.str]:
            '''The time when prefetched ads are considered for use in an ad break, as an ISO 8601 date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchconsumption.html#cfn-mediatailor-prefetchschedule-prefetchconsumption-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrefetchConsumptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule.PrefetchRetrievalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_time": "endTime",
            "dynamic_variables": "dynamicVariables",
            "start_time": "startTime",
            "traffic_shaping_retrieval_window": "trafficShapingRetrievalWindow",
            "traffic_shaping_tps_configuration": "trafficShapingTpsConfiguration",
            "traffic_shaping_type": "trafficShapingType",
        },
    )
    class PrefetchRetrievalProperty:
        def __init__(
            self,
            *,
            end_time: builtins.str,
            dynamic_variables: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
            start_time: typing.Optional[builtins.str] = None,
            traffic_shaping_retrieval_window: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            traffic_shaping_tps_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            traffic_shaping_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param end_time: The time when prefetch retrieval ends for the ad break, as an ISO 8601 date-time.
            :param dynamic_variables: The dynamic variables to use for substitution during prefetch requests to the ad decision server (ADS).
            :param start_time: The time when prefetch retrievals can start for this break, as an ISO 8601 date-time.
            :param traffic_shaping_retrieval_window: 
            :param traffic_shaping_tps_configuration: 
            :param traffic_shaping_type: Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchretrieval.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                prefetch_retrieval_property = mediatailor.CfnPrefetchSchedule.PrefetchRetrievalProperty(
                    end_time="endTime",
                
                    # the properties below are optional
                    dynamic_variables={
                        "dynamic_variables_key": "dynamicVariables"
                    },
                    start_time="startTime",
                    traffic_shaping_retrieval_window=mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty(
                        retrieval_window_duration_seconds=123
                    ),
                    traffic_shaping_tps_configuration=mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty(
                        peak_concurrent_users=123,
                        peak_tps=123
                    ),
                    traffic_shaping_type="trafficShapingType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__00c2ecb75839a35994f3696a2d7c3d544f3638146358e28982fb7c42826178f3)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument dynamic_variables", value=dynamic_variables, expected_type=type_hints["dynamic_variables"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
                check_type(argname="argument traffic_shaping_retrieval_window", value=traffic_shaping_retrieval_window, expected_type=type_hints["traffic_shaping_retrieval_window"])
                check_type(argname="argument traffic_shaping_tps_configuration", value=traffic_shaping_tps_configuration, expected_type=type_hints["traffic_shaping_tps_configuration"])
                check_type(argname="argument traffic_shaping_type", value=traffic_shaping_type, expected_type=type_hints["traffic_shaping_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_time": end_time,
            }
            if dynamic_variables is not None:
                self._values["dynamic_variables"] = dynamic_variables
            if start_time is not None:
                self._values["start_time"] = start_time
            if traffic_shaping_retrieval_window is not None:
                self._values["traffic_shaping_retrieval_window"] = traffic_shaping_retrieval_window
            if traffic_shaping_tps_configuration is not None:
                self._values["traffic_shaping_tps_configuration"] = traffic_shaping_tps_configuration
            if traffic_shaping_type is not None:
                self._values["traffic_shaping_type"] = traffic_shaping_type

        @builtins.property
        def end_time(self) -> builtins.str:
            '''The time when prefetch retrieval ends for the ad break, as an ISO 8601 date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchretrieval.html#cfn-mediatailor-prefetchschedule-prefetchretrieval-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dynamic_variables(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''The dynamic variables to use for substitution during prefetch requests to the ad decision server (ADS).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchretrieval.html#cfn-mediatailor-prefetchschedule-prefetchretrieval-dynamicvariables
            '''
            result = self._values.get("dynamic_variables")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def start_time(self) -> typing.Optional[builtins.str]:
            '''The time when prefetch retrievals can start for this break, as an ISO 8601 date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchretrieval.html#cfn-mediatailor-prefetchschedule-prefetchretrieval-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def traffic_shaping_retrieval_window(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchretrieval.html#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingretrievalwindow
            '''
            result = self._values.get("traffic_shaping_retrieval_window")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty"]], result)

        @builtins.property
        def traffic_shaping_tps_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchretrieval.html#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingtpsconfiguration
            '''
            result = self._values.get("traffic_shaping_tps_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty"]], result)

        @builtins.property
        def traffic_shaping_type(self) -> typing.Optional[builtins.str]:
            '''Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-prefetchretrieval.html#cfn-mediatailor-prefetchschedule-prefetchretrieval-trafficshapingtype
            '''
            result = self._values.get("traffic_shaping_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrefetchRetrievalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule.RecurringConsumptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "avail_matching_criteria": "availMatchingCriteria",
            "retrieved_ad_expiration_seconds": "retrievedAdExpirationSeconds",
        },
    )
    class RecurringConsumptionProperty:
        def __init__(
            self,
            *,
            avail_matching_criteria: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.AvailMatchingCriteriaProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            retrieved_ad_expiration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param avail_matching_criteria: The configuration for the dynamic variables that determine which ad breaks that MediaTailor inserts prefetched ads in.
            :param retrieved_ad_expiration_seconds: The number of seconds that an ad is available for insertion after it was prefetched.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringconsumption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                recurring_consumption_property = mediatailor.CfnPrefetchSchedule.RecurringConsumptionProperty(
                    avail_matching_criteria=[mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty(
                        dynamic_variable="dynamicVariable",
                        operator="operator"
                    )],
                    retrieved_ad_expiration_seconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__b2a371af0ad0c1d79415ae11b9755cca464c7035c6f622d511446260cef06603)
                check_type(argname="argument avail_matching_criteria", value=avail_matching_criteria, expected_type=type_hints["avail_matching_criteria"])
                check_type(argname="argument retrieved_ad_expiration_seconds", value=retrieved_ad_expiration_seconds, expected_type=type_hints["retrieved_ad_expiration_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if avail_matching_criteria is not None:
                self._values["avail_matching_criteria"] = avail_matching_criteria
            if retrieved_ad_expiration_seconds is not None:
                self._values["retrieved_ad_expiration_seconds"] = retrieved_ad_expiration_seconds

        @builtins.property
        def avail_matching_criteria(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.AvailMatchingCriteriaProperty"]]]]:
            '''The configuration for the dynamic variables that determine which ad breaks that MediaTailor inserts prefetched ads in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringconsumption.html#cfn-mediatailor-prefetchschedule-recurringconsumption-availmatchingcriteria
            '''
            result = self._values.get("avail_matching_criteria")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.AvailMatchingCriteriaProperty"]]]], result)

        @builtins.property
        def retrieved_ad_expiration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds that an ad is available for insertion after it was prefetched.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringconsumption.html#cfn-mediatailor-prefetchschedule-recurringconsumption-retrievedadexpirationseconds
            '''
            result = self._values.get("retrieved_ad_expiration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecurringConsumptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_time": "endTime",
            "recurring_consumption": "recurringConsumption",
            "recurring_retrieval": "recurringRetrieval",
            "start_time": "startTime",
        },
    )
    class RecurringPrefetchConfigurationProperty:
        def __init__(
            self,
            *,
            end_time: builtins.str,
            recurring_consumption: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.RecurringConsumptionProperty", typing.Dict[builtins.str, typing.Any]]],
            recurring_retrieval: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.RecurringRetrievalProperty", typing.Dict[builtins.str, typing.Any]]],
            start_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param end_time: The end time for the window that MediaTailor prefetches and inserts ads in a live event, as an ISO 8601 date-time.
            :param recurring_consumption: 
            :param recurring_retrieval: 
            :param start_time: The start time for the window that MediaTailor prefetches and inserts ads in a live event, as an ISO 8601 date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                recurring_prefetch_configuration_property = mediatailor.CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty(
                    end_time="endTime",
                    recurring_consumption=mediatailor.CfnPrefetchSchedule.RecurringConsumptionProperty(
                        avail_matching_criteria=[mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty(
                            dynamic_variable="dynamicVariable",
                            operator="operator"
                        )],
                        retrieved_ad_expiration_seconds=123
                    ),
                    recurring_retrieval=mediatailor.CfnPrefetchSchedule.RecurringRetrievalProperty(
                        delay_after_avail_end_seconds=123,
                        dynamic_variables={
                            "dynamic_variables_key": "dynamicVariables"
                        },
                        traffic_shaping_retrieval_window=mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty(
                            retrieval_window_duration_seconds=123
                        ),
                        traffic_shaping_tps_configuration=mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty(
                            peak_concurrent_users=123,
                            peak_tps=123
                        ),
                        traffic_shaping_type="trafficShapingType"
                    ),
                
                    # the properties below are optional
                    start_time="startTime"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__05bd8652a49c8686098c037ea3c9547bb9a1f7c2a92b033cc181e6fdf0428f4d)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument recurring_consumption", value=recurring_consumption, expected_type=type_hints["recurring_consumption"])
                check_type(argname="argument recurring_retrieval", value=recurring_retrieval, expected_type=type_hints["recurring_retrieval"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_time": end_time,
                "recurring_consumption": recurring_consumption,
                "recurring_retrieval": recurring_retrieval,
            }
            if start_time is not None:
                self._values["start_time"] = start_time

        @builtins.property
        def end_time(self) -> builtins.str:
            '''The end time for the window that MediaTailor prefetches and inserts ads in a live event, as an ISO 8601 date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration.html#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def recurring_consumption(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringConsumptionProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration.html#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-recurringconsumption
            '''
            result = self._values.get("recurring_consumption")
            assert result is not None, "Required property 'recurring_consumption' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringConsumptionProperty"], result)

        @builtins.property
        def recurring_retrieval(
            self,
        ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringRetrievalProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration.html#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-recurringretrieval
            '''
            result = self._values.get("recurring_retrieval")
            assert result is not None, "Required property 'recurring_retrieval' is missing"
            return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringRetrievalProperty"], result)

        @builtins.property
        def start_time(self) -> typing.Optional[builtins.str]:
            '''The start time for the window that MediaTailor prefetches and inserts ads in a live event, as an ISO 8601 date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringprefetchconfiguration.html#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecurringPrefetchConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule.RecurringRetrievalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delay_after_avail_end_seconds": "delayAfterAvailEndSeconds",
            "dynamic_variables": "dynamicVariables",
            "traffic_shaping_retrieval_window": "trafficShapingRetrievalWindow",
            "traffic_shaping_tps_configuration": "trafficShapingTpsConfiguration",
            "traffic_shaping_type": "trafficShapingType",
        },
    )
    class RecurringRetrievalProperty:
        def __init__(
            self,
            *,
            delay_after_avail_end_seconds: typing.Optional[jsii.Number] = None,
            dynamic_variables: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
            traffic_shaping_retrieval_window: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            traffic_shaping_tps_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            traffic_shaping_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param delay_after_avail_end_seconds: The number of seconds that MediaTailor waits after an ad avail before prefetching ads for the next avail.
            :param dynamic_variables: The dynamic variables to use for substitution during prefetch requests to the ADS.
            :param traffic_shaping_retrieval_window: 
            :param traffic_shaping_tps_configuration: 
            :param traffic_shaping_type: Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringretrieval.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                recurring_retrieval_property = mediatailor.CfnPrefetchSchedule.RecurringRetrievalProperty(
                    delay_after_avail_end_seconds=123,
                    dynamic_variables={
                        "dynamic_variables_key": "dynamicVariables"
                    },
                    traffic_shaping_retrieval_window=mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty(
                        retrieval_window_duration_seconds=123
                    ),
                    traffic_shaping_tps_configuration=mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty(
                        peak_concurrent_users=123,
                        peak_tps=123
                    ),
                    traffic_shaping_type="trafficShapingType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__00104803c0902da691a3e7ce3c7070e8259a6ffed7ee23a85b48e3f039e8f0f2)
                check_type(argname="argument delay_after_avail_end_seconds", value=delay_after_avail_end_seconds, expected_type=type_hints["delay_after_avail_end_seconds"])
                check_type(argname="argument dynamic_variables", value=dynamic_variables, expected_type=type_hints["dynamic_variables"])
                check_type(argname="argument traffic_shaping_retrieval_window", value=traffic_shaping_retrieval_window, expected_type=type_hints["traffic_shaping_retrieval_window"])
                check_type(argname="argument traffic_shaping_tps_configuration", value=traffic_shaping_tps_configuration, expected_type=type_hints["traffic_shaping_tps_configuration"])
                check_type(argname="argument traffic_shaping_type", value=traffic_shaping_type, expected_type=type_hints["traffic_shaping_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delay_after_avail_end_seconds is not None:
                self._values["delay_after_avail_end_seconds"] = delay_after_avail_end_seconds
            if dynamic_variables is not None:
                self._values["dynamic_variables"] = dynamic_variables
            if traffic_shaping_retrieval_window is not None:
                self._values["traffic_shaping_retrieval_window"] = traffic_shaping_retrieval_window
            if traffic_shaping_tps_configuration is not None:
                self._values["traffic_shaping_tps_configuration"] = traffic_shaping_tps_configuration
            if traffic_shaping_type is not None:
                self._values["traffic_shaping_type"] = traffic_shaping_type

        @builtins.property
        def delay_after_avail_end_seconds(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds that MediaTailor waits after an ad avail before prefetching ads for the next avail.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringretrieval.html#cfn-mediatailor-prefetchschedule-recurringretrieval-delayafteravailendseconds
            '''
            result = self._values.get("delay_after_avail_end_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dynamic_variables(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
            '''The dynamic variables to use for substitution during prefetch requests to the ADS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringretrieval.html#cfn-mediatailor-prefetchschedule-recurringretrieval-dynamicvariables
            '''
            result = self._values.get("dynamic_variables")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def traffic_shaping_retrieval_window(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringretrieval.html#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingretrievalwindow
            '''
            result = self._values.get("traffic_shaping_retrieval_window")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty"]], result)

        @builtins.property
        def traffic_shaping_tps_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringretrieval.html#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingtpsconfiguration
            '''
            result = self._values.get("traffic_shaping_tps_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty"]], result)

        @builtins.property
        def traffic_shaping_type(self) -> typing.Optional[builtins.str]:
            '''Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-recurringretrieval.html#cfn-mediatailor-prefetchschedule-recurringretrieval-trafficshapingtype
            '''
            result = self._values.get("traffic_shaping_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecurringRetrievalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty",
        jsii_struct_bases=[],
        name_mapping={
            "retrieval_window_duration_seconds": "retrievalWindowDurationSeconds",
        },
    )
    class TrafficShapingRetrievalWindowProperty:
        def __init__(
            self,
            *,
            retrieval_window_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param retrieval_window_duration_seconds: The amount of time, in seconds, that MediaTailor spreads prefetch requests to the ADS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                traffic_shaping_retrieval_window_property = mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty(
                    retrieval_window_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__72ad8a6953ae3d4cd6c48d9ff13d2d032668dfad2a83cd1e697b0fa6669d7b40)
                check_type(argname="argument retrieval_window_duration_seconds", value=retrieval_window_duration_seconds, expected_type=type_hints["retrieval_window_duration_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if retrieval_window_duration_seconds is not None:
                self._values["retrieval_window_duration_seconds"] = retrieval_window_duration_seconds

        @builtins.property
        def retrieval_window_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, that MediaTailor spreads prefetch requests to the ADS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-trafficshapingretrievalwindow.html#cfn-mediatailor-prefetchschedule-trafficshapingretrievalwindow-retrievalwindowdurationseconds
            '''
            result = self._values.get("retrieval_window_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrafficShapingRetrievalWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "peak_concurrent_users": "peakConcurrentUsers",
            "peak_tps": "peakTps",
        },
    )
    class TrafficShapingTpsConfigurationProperty:
        def __init__(
            self,
            *,
            peak_concurrent_users: typing.Optional[jsii.Number] = None,
            peak_tps: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param peak_concurrent_users: The expected peak number of concurrent viewers for your content.
            :param peak_tps: The maximum number of transactions per second (TPS) that your ad decision server (ADS) can handle.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                traffic_shaping_tps_configuration_property = mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty(
                    peak_concurrent_users=123,
                    peak_tps=123
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__75d12d072deb9d1c155a01a6845b704c9e65ffe9d4675dab270978f29c3881b5)
                check_type(argname="argument peak_concurrent_users", value=peak_concurrent_users, expected_type=type_hints["peak_concurrent_users"])
                check_type(argname="argument peak_tps", value=peak_tps, expected_type=type_hints["peak_tps"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if peak_concurrent_users is not None:
                self._values["peak_concurrent_users"] = peak_concurrent_users
            if peak_tps is not None:
                self._values["peak_tps"] = peak_tps

        @builtins.property
        def peak_concurrent_users(self) -> typing.Optional[jsii.Number]:
            '''The expected peak number of concurrent viewers for your content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration.html#cfn-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-peakconcurrentusers
            '''
            result = self._values.get("peak_concurrent_users")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def peak_tps(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of transactions per second (TPS) that your ad decision server (ADS) can handle.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-prefetchschedule-trafficshapingtpsconfiguration.html#cfn-mediatailor-prefetchschedule-trafficshapingtpsconfiguration-peaktps
            '''
            result = self._values.get("peak_tps")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrafficShapingTpsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnPrefetchScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "playback_configuration_name": "playbackConfigurationName",
        "consumption": "consumption",
        "recurring_prefetch_configuration": "recurringPrefetchConfiguration",
        "retrieval": "retrieval",
        "schedule_type": "scheduleType",
        "stream_id": "streamId",
        "tags": "tags",
    },
)
class CfnPrefetchScheduleProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        playback_configuration_name: builtins.str,
        consumption: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.PrefetchConsumptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        recurring_prefetch_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        retrieval: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnPrefetchSchedule.PrefetchRetrievalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule_type: typing.Optional[builtins.str] = None,
        stream_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrefetchSchedule``.

        :param name: The name to assign to the prefetch schedule.
        :param playback_configuration_name: The name of the playback configuration.
        :param consumption: 
        :param recurring_prefetch_configuration: 
        :param retrieval: 
        :param schedule_type: The frequency that MediaTailor creates prefetch schedules.
        :param stream_id: An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration.
        :param tags: The tags assigned to the prefetch schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            cfn_prefetch_schedule_props = mediatailor.CfnPrefetchScheduleProps(
                name="name",
                playback_configuration_name="playbackConfigurationName",
            
                # the properties below are optional
                consumption=mediatailor.CfnPrefetchSchedule.PrefetchConsumptionProperty(
                    end_time="endTime",
            
                    # the properties below are optional
                    avail_matching_criteria=[mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty(
                        dynamic_variable="dynamicVariable",
                        operator="operator"
                    )],
                    start_time="startTime"
                ),
                recurring_prefetch_configuration=mediatailor.CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty(
                    end_time="endTime",
                    recurring_consumption=mediatailor.CfnPrefetchSchedule.RecurringConsumptionProperty(
                        avail_matching_criteria=[mediatailor.CfnPrefetchSchedule.AvailMatchingCriteriaProperty(
                            dynamic_variable="dynamicVariable",
                            operator="operator"
                        )],
                        retrieved_ad_expiration_seconds=123
                    ),
                    recurring_retrieval=mediatailor.CfnPrefetchSchedule.RecurringRetrievalProperty(
                        delay_after_avail_end_seconds=123,
                        dynamic_variables={
                            "dynamic_variables_key": "dynamicVariables"
                        },
                        traffic_shaping_retrieval_window=mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty(
                            retrieval_window_duration_seconds=123
                        ),
                        traffic_shaping_tps_configuration=mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty(
                            peak_concurrent_users=123,
                            peak_tps=123
                        ),
                        traffic_shaping_type="trafficShapingType"
                    ),
            
                    # the properties below are optional
                    start_time="startTime"
                ),
                retrieval=mediatailor.CfnPrefetchSchedule.PrefetchRetrievalProperty(
                    end_time="endTime",
            
                    # the properties below are optional
                    dynamic_variables={
                        "dynamic_variables_key": "dynamicVariables"
                    },
                    start_time="startTime",
                    traffic_shaping_retrieval_window=mediatailor.CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty(
                        retrieval_window_duration_seconds=123
                    ),
                    traffic_shaping_tps_configuration=mediatailor.CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty(
                        peak_concurrent_users=123,
                        peak_tps=123
                    ),
                    traffic_shaping_type="trafficShapingType"
                ),
                schedule_type="scheduleType",
                stream_id="streamId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__51933737a0a3bf5f476a73e634bbeb2dfebf67ef8c85c29f58466fd17df23d63)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument playback_configuration_name", value=playback_configuration_name, expected_type=type_hints["playback_configuration_name"])
            check_type(argname="argument consumption", value=consumption, expected_type=type_hints["consumption"])
            check_type(argname="argument recurring_prefetch_configuration", value=recurring_prefetch_configuration, expected_type=type_hints["recurring_prefetch_configuration"])
            check_type(argname="argument retrieval", value=retrieval, expected_type=type_hints["retrieval"])
            check_type(argname="argument schedule_type", value=schedule_type, expected_type=type_hints["schedule_type"])
            check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
        }
        if consumption is not None:
            self._values["consumption"] = consumption
        if recurring_prefetch_configuration is not None:
            self._values["recurring_prefetch_configuration"] = recurring_prefetch_configuration
        if retrieval is not None:
            self._values["retrieval"] = retrieval
        if schedule_type is not None:
            self._values["schedule_type"] = schedule_type
        if stream_id is not None:
            self._values["stream_id"] = stream_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name to assign to the prefetch schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html#cfn-mediatailor-prefetchschedule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def playback_configuration_name(self) -> builtins.str:
        '''The name of the playback configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html#cfn-mediatailor-prefetchschedule-playbackconfigurationname
        '''
        result = self._values.get("playback_configuration_name")
        assert result is not None, "Required property 'playback_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consumption(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchConsumptionProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html#cfn-mediatailor-prefetchschedule-consumption
        '''
        result = self._values.get("consumption")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchConsumptionProperty"]], result)

    @builtins.property
    def recurring_prefetch_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html#cfn-mediatailor-prefetchschedule-recurringprefetchconfiguration
        '''
        result = self._values.get("recurring_prefetch_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty"]], result)

    @builtins.property
    def retrieval(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchRetrievalProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html#cfn-mediatailor-prefetchschedule-retrieval
        '''
        result = self._values.get("retrieval")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnPrefetchSchedule.PrefetchRetrievalProperty"]], result)

    @builtins.property
    def schedule_type(self) -> typing.Optional[builtins.str]:
        '''The frequency that MediaTailor creates prefetch schedules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html#cfn-mediatailor-prefetchschedule-scheduletype
        '''
        result = self._values.get("schedule_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html#cfn-mediatailor-prefetchschedule-streamid
        '''
        result = self._values.get("stream_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the prefetch schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-prefetchschedule.html#cfn-mediatailor-prefetchschedule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrefetchScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_mediatailor_60404695.ISourceLocationRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnSourceLocation(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnSourceLocation",
):
    '''A source location is a container for sources.

    For more information about source locations, see `Working with source locations <https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html>`_ in the *MediaTailor User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html
    :cloudformationResource: AWS::MediaTailor::SourceLocation
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        cfn_source_location = mediatailor.CfnSourceLocation(self, "MyCfnSourceLocation",
            http_configuration=mediatailor.CfnSourceLocation.HttpConfigurationProperty(
                base_url="baseUrl"
            ),
            source_location_name="sourceLocationName",
        
            # the properties below are optional
            access_configuration=mediatailor.CfnSourceLocation.AccessConfigurationProperty(
                access_type="accessType",
                secrets_manager_access_token_configuration=mediatailor.CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty(
                    header_name="headerName",
                    secret_arn="secretArn",
                    secret_string_key="secretStringKey"
                )
            ),
            default_segment_delivery_configuration=mediatailor.CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty(
                base_url="baseUrl"
            ),
            segment_delivery_configurations=[mediatailor.CfnSourceLocation.SegmentDeliveryConfigurationProperty(
                base_url="baseUrl",
                name="name"
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
        http_configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.HttpConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        source_location_name: builtins.str,
        access_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.AccessConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_segment_delivery_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        segment_delivery_configurations: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.SegmentDeliveryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::SourceLocation``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param http_configuration: The HTTP configuration for the source location.
        :param source_location_name: The name of the source location.
        :param access_configuration: The access configuration for the source location.
        :param default_segment_delivery_configuration: The default segment delivery configuration.
        :param segment_delivery_configurations: The segment delivery configurations for the source location.
        :param tags: The tags assigned to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dd693d384196965a6e6e42aa969746fa450f3a5099e7be68c145dcc9f5f7e59d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSourceLocationProps(
            http_configuration=http_configuration,
            source_location_name=source_location_name,
            access_configuration=access_configuration,
            default_segment_delivery_configuration=default_segment_delivery_configuration,
            segment_delivery_configurations=segment_delivery_configurations,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSourceLocation")
    @builtins.classmethod
    def arn_for_source_location(
        cls,
        resource: "_aws_mediatailor_60404695.ISourceLocationRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a0d17f619c660f9b6fd1fb2b7aeb5e9f11758a50027ed09924fa2715dfe61616)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSourceLocation", [resource]))

    @jsii.member(jsii_name="isCfnSourceLocation")
    @builtins.classmethod
    def is_cfn_source_location(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSourceLocation.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__28b271fcaa782dcce30289b4d3e9cd1597cc2e403d5decad01698ce3810fc642)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSourceLocation", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a8a67b4bd9eabe7dff32771e3855c5f4b09c52cc321708cd63f64f1f290488c1)
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
            type_hints = cached_type_hints(_typecheckingstub__d9c819cfa165355742944ead86f157d5e4fe520ec150ce7cb7367ac66b39c700)
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
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="sourceLocationRef")
    def source_location_ref(
        self,
    ) -> "_aws_mediatailor_60404695.SourceLocationReference":
        '''A reference to a SourceLocation resource.'''
        return typing.cast("_aws_mediatailor_60404695.SourceLocationReference", jsii.get(self, "sourceLocationRef"))

    @builtins.property
    @jsii.member(jsii_name="httpConfiguration")
    def http_configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.HttpConfigurationProperty"]:
        '''The HTTP configuration for the source location.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.HttpConfigurationProperty"], jsii.get(self, "httpConfiguration"))

    @http_configuration.setter
    def http_configuration(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.HttpConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__be0faeec30de7aa74e972fa9be4f5ef1134314ff5984d14b00fc6e2596ceb488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceLocationName")
    def source_location_name(self) -> builtins.str:
        '''The name of the source location.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceLocationName"))

    @source_location_name.setter
    def source_location_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f3bd8c206592bff1adae3d34013e03de975c95df7847310b70d730fb7b9498b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceLocationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="accessConfiguration")
    def access_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.AccessConfigurationProperty"]]:
        '''The access configuration for the source location.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.AccessConfigurationProperty"]], jsii.get(self, "accessConfiguration"))

    @access_configuration.setter
    def access_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.AccessConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c1bc53fb2d4148510df3244898b3da3e4ac17d9faee3835bc73da5ad63931214)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultSegmentDeliveryConfiguration")
    def default_segment_delivery_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty"]]:
        '''The default segment delivery configuration.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty"]], jsii.get(self, "defaultSegmentDeliveryConfiguration"))

    @default_segment_delivery_configuration.setter
    def default_segment_delivery_configuration(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7b431a09702c35ab502bf465075ac7a7d86895d1cc20d16caec630b4e0a366dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSegmentDeliveryConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="segmentDeliveryConfigurations")
    def segment_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.SegmentDeliveryConfigurationProperty"]]]]:
        '''The segment delivery configurations for the source location.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.SegmentDeliveryConfigurationProperty"]]]], jsii.get(self, "segmentDeliveryConfigurations"))

    @segment_delivery_configurations.setter
    def segment_delivery_configurations(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.SegmentDeliveryConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__725f16ab7057c1a2a01a0de087479721b15670cf708ed95838c4271ad45c009a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segmentDeliveryConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the source location.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__af85fa3fdd92d33488c46dc70861bcea3919f31a13ab83bd91920e11557a0620)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnSourceLocation.AccessConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_type": "accessType",
            "secrets_manager_access_token_configuration": "secretsManagerAccessTokenConfiguration",
        },
    )
    class AccessConfigurationProperty:
        def __init__(
            self,
            *,
            access_type: typing.Optional[builtins.str] = None,
            secrets_manager_access_token_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Access configuration parameters.

            :param access_type: The type of authentication used to access content from ``HttpConfiguration::BaseUrl`` on your source location. Accepted value: ``S3_SIGV4`` . ``S3_SIGV4`` - AWS Signature Version 4 authentication for Amazon S3 hosted virtual-style access. If your source location base URL is an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the bucket where your source content is stored. Your MediaTailor source location baseURL must follow the S3 virtual hosted-style request URL format. For example, https://bucket-name.s3.Region.amazonaws.com/key-name. Before you can use ``S3_SIGV4`` , you must meet these requirements: • You must allow MediaTailor to access your S3 bucket by granting mediatailor.amazonaws.com principal access in IAM. For information about configuring access in IAM, see Access management in the IAM User Guide. • The mediatailor.amazonaws.com service principal must have permissions to read all top level manifests referenced by the VodSource packaging configurations. • The caller of the API must have s3:GetObject IAM permissions to read all top level manifests referenced by your MediaTailor VodSource packaging configurations.
            :param secrets_manager_access_token_configuration: AWS Secrets Manager access token configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-accessconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                access_configuration_property = mediatailor.CfnSourceLocation.AccessConfigurationProperty(
                    access_type="accessType",
                    secrets_manager_access_token_configuration=mediatailor.CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty(
                        header_name="headerName",
                        secret_arn="secretArn",
                        secret_string_key="secretStringKey"
                    )
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__df138d384fef8104d70a1dae201bed1b055b8ef01c97ffa764008d6423001711)
                check_type(argname="argument access_type", value=access_type, expected_type=type_hints["access_type"])
                check_type(argname="argument secrets_manager_access_token_configuration", value=secrets_manager_access_token_configuration, expected_type=type_hints["secrets_manager_access_token_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_type is not None:
                self._values["access_type"] = access_type
            if secrets_manager_access_token_configuration is not None:
                self._values["secrets_manager_access_token_configuration"] = secrets_manager_access_token_configuration

        @builtins.property
        def access_type(self) -> typing.Optional[builtins.str]:
            '''The type of authentication used to access content from ``HttpConfiguration::BaseUrl`` on your source location. Accepted value: ``S3_SIGV4`` .

            ``S3_SIGV4`` - AWS Signature Version 4 authentication for Amazon S3 hosted virtual-style access. If your source location base URL is an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the bucket where your source content is stored. Your MediaTailor source location baseURL must follow the S3 virtual hosted-style request URL format. For example, https://bucket-name.s3.Region.amazonaws.com/key-name.

            Before you can use ``S3_SIGV4`` , you must meet these requirements:

            • You must allow MediaTailor to access your S3 bucket by granting mediatailor.amazonaws.com principal access in IAM. For information about configuring access in IAM, see Access management in the IAM User Guide.

            • The mediatailor.amazonaws.com service principal must have permissions to read all top level manifests referenced by the VodSource packaging configurations.

            • The caller of the API must have s3:GetObject IAM permissions to read all top level manifests referenced by your MediaTailor VodSource packaging configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-accessconfiguration.html#cfn-mediatailor-sourcelocation-accessconfiguration-accesstype
            '''
            result = self._values.get("access_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_token_configuration(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty"]]:
            '''AWS Secrets Manager access token configuration parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-accessconfiguration.html#cfn-mediatailor-sourcelocation-accessconfiguration-secretsmanageraccesstokenconfiguration
            '''
            result = self._values.get("secrets_manager_access_token_configuration")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"base_url": "baseUrl"},
    )
    class DefaultSegmentDeliveryConfigurationProperty:
        def __init__(self, *, base_url: typing.Optional[builtins.str] = None) -> None:
            '''The optional configuration for a server that serves segments.

            Use this if you want the segment delivery server to be different from the source location server. For example, you can configure your source location server to be an origination server, such as MediaPackage, and the segment delivery server to be a content delivery network (CDN), such as CloudFront. If you don't specify a segment delivery server, then the source location server is used.

            :param base_url: The hostname of the server that will be used to serve segments. This string must include the protocol, such as *https://* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                default_segment_delivery_configuration_property = mediatailor.CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty(
                    base_url="baseUrl"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__7c8f2bdbcfd97bfab31281eb19a1cb75bcd15849095da44b410f2703593facdc)
                check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if base_url is not None:
                self._values["base_url"] = base_url

        @builtins.property
        def base_url(self) -> typing.Optional[builtins.str]:
            '''The hostname of the server that will be used to serve segments.

            This string must include the protocol, such as *https://* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration.html#cfn-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration-baseurl
            '''
            result = self._values.get("base_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultSegmentDeliveryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnSourceLocation.HttpConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"base_url": "baseUrl"},
    )
    class HttpConfigurationProperty:
        def __init__(self, *, base_url: builtins.str) -> None:
            '''The HTTP configuration for the source location.

            :param base_url: The base URL for the source location host server. This string must include the protocol, such as *https://* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-httpconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                http_configuration_property = mediatailor.CfnSourceLocation.HttpConfigurationProperty(
                    base_url="baseUrl"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a880194f274158b8a0b3d6dab7716d3a29cb93edfb1f5ef3e8b507eb8379c18a)
                check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "base_url": base_url,
            }

        @builtins.property
        def base_url(self) -> builtins.str:
            '''The base URL for the source location host server.

            This string must include the protocol, such as *https://* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-httpconfiguration.html#cfn-mediatailor-sourcelocation-httpconfiguration-baseurl
            '''
            result = self._values.get("base_url")
            assert result is not None, "Required property 'base_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "header_name": "headerName",
            "secret_arn": "secretArn",
            "secret_string_key": "secretStringKey",
        },
    )
    class SecretsManagerAccessTokenConfigurationProperty:
        def __init__(
            self,
            *,
            header_name: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            secret_string_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''AWS Secrets Manager access token configuration parameters.

            For information about Secrets Manager access token authentication, see `Working with AWS Secrets Manager access token authentication <https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-access-token.html>`_ .

            :param header_name: The name of the HTTP header used to supply the access token in requests to the source location.
            :param secret_arn: The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the access token.
            :param secret_string_key: The AWS Secrets Manager `SecretString <https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html#SecretsManager-CreateSecret-request-SecretString.html>`_ key associated with the access token. MediaTailor uses the key to look up SecretString key and value pair containing the access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                secrets_manager_access_token_configuration_property = mediatailor.CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty(
                    header_name="headerName",
                    secret_arn="secretArn",
                    secret_string_key="secretStringKey"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__2feb4b5d75163b5824572e2ce3caac3c88483a5919f3648703d571fb23723c19)
                check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument secret_string_key", value=secret_string_key, expected_type=type_hints["secret_string_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if header_name is not None:
                self._values["header_name"] = header_name
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if secret_string_key is not None:
                self._values["secret_string_key"] = secret_string_key

        @builtins.property
        def header_name(self) -> typing.Optional[builtins.str]:
            '''The name of the HTTP header used to supply the access token in requests to the source location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html#cfn-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration-headername
            '''
            result = self._values.get("header_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html#cfn-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_string_key(self) -> typing.Optional[builtins.str]:
            '''The AWS Secrets Manager `SecretString <https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html#SecretsManager-CreateSecret-request-SecretString.html>`_ key associated with the access token. MediaTailor uses the key to look up SecretString key and value pair containing the access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html#cfn-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration-secretstringkey
            '''
            result = self._values.get("secret_string_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretsManagerAccessTokenConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnSourceLocation.SegmentDeliveryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"base_url": "baseUrl", "name": "name"},
    )
    class SegmentDeliveryConfigurationProperty:
        def __init__(
            self,
            *,
            base_url: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The segment delivery configuration settings.

            :param base_url: The base URL of the host or path of the segment delivery server that you're using to serve segments. This is typically a content delivery network (CDN). The URL can be absolute or relative. To use an absolute URL include the protocol, such as ``https://example.com/some/path`` . To use a relative URL specify the relative path, such as ``/some/path*`` .
            :param name: A unique identifier used to distinguish between multiple segment delivery configurations in a source location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                segment_delivery_configuration_property = mediatailor.CfnSourceLocation.SegmentDeliveryConfigurationProperty(
                    base_url="baseUrl",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__383b15aa1a1faec4ed8f2f0982e5ba8e88dfe9184d36b17c3b787e66a0c45076)
                check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if base_url is not None:
                self._values["base_url"] = base_url
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def base_url(self) -> typing.Optional[builtins.str]:
            '''The base URL of the host or path of the segment delivery server that you're using to serve segments.

            This is typically a content delivery network (CDN). The URL can be absolute or relative. To use an absolute URL include the protocol, such as ``https://example.com/some/path`` . To use a relative URL specify the relative path, such as ``/some/path*`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration.html#cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-baseurl
            '''
            result = self._values.get("base_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''A unique identifier used to distinguish between multiple segment delivery configurations in a source location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration.html#cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentDeliveryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnSourceLocationProps",
    jsii_struct_bases=[],
    name_mapping={
        "http_configuration": "httpConfiguration",
        "source_location_name": "sourceLocationName",
        "access_configuration": "accessConfiguration",
        "default_segment_delivery_configuration": "defaultSegmentDeliveryConfiguration",
        "segment_delivery_configurations": "segmentDeliveryConfigurations",
        "tags": "tags",
    },
)
class CfnSourceLocationProps:
    def __init__(
        self,
        *,
        http_configuration: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.HttpConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        source_location_name: builtins.str,
        access_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.AccessConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_segment_delivery_configuration: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        segment_delivery_configurations: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnSourceLocation.SegmentDeliveryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSourceLocation``.

        :param http_configuration: The HTTP configuration for the source location.
        :param source_location_name: The name of the source location.
        :param access_configuration: The access configuration for the source location.
        :param default_segment_delivery_configuration: The default segment delivery configuration.
        :param segment_delivery_configurations: The segment delivery configurations for the source location.
        :param tags: The tags assigned to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            cfn_source_location_props = mediatailor.CfnSourceLocationProps(
                http_configuration=mediatailor.CfnSourceLocation.HttpConfigurationProperty(
                    base_url="baseUrl"
                ),
                source_location_name="sourceLocationName",
            
                # the properties below are optional
                access_configuration=mediatailor.CfnSourceLocation.AccessConfigurationProperty(
                    access_type="accessType",
                    secrets_manager_access_token_configuration=mediatailor.CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty(
                        header_name="headerName",
                        secret_arn="secretArn",
                        secret_string_key="secretStringKey"
                    )
                ),
                default_segment_delivery_configuration=mediatailor.CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty(
                    base_url="baseUrl"
                ),
                segment_delivery_configurations=[mediatailor.CfnSourceLocation.SegmentDeliveryConfigurationProperty(
                    base_url="baseUrl",
                    name="name"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cb562c06ea390d62a28e2d88d462a731b39635f142da846f03422a25348fff7c)
            check_type(argname="argument http_configuration", value=http_configuration, expected_type=type_hints["http_configuration"])
            check_type(argname="argument source_location_name", value=source_location_name, expected_type=type_hints["source_location_name"])
            check_type(argname="argument access_configuration", value=access_configuration, expected_type=type_hints["access_configuration"])
            check_type(argname="argument default_segment_delivery_configuration", value=default_segment_delivery_configuration, expected_type=type_hints["default_segment_delivery_configuration"])
            check_type(argname="argument segment_delivery_configurations", value=segment_delivery_configurations, expected_type=type_hints["segment_delivery_configurations"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http_configuration": http_configuration,
            "source_location_name": source_location_name,
        }
        if access_configuration is not None:
            self._values["access_configuration"] = access_configuration
        if default_segment_delivery_configuration is not None:
            self._values["default_segment_delivery_configuration"] = default_segment_delivery_configuration
        if segment_delivery_configurations is not None:
            self._values["segment_delivery_configurations"] = segment_delivery_configurations
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def http_configuration(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.HttpConfigurationProperty"]:
        '''The HTTP configuration for the source location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-httpconfiguration
        '''
        result = self._values.get("http_configuration")
        assert result is not None, "Required property 'http_configuration' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.HttpConfigurationProperty"], result)

    @builtins.property
    def source_location_name(self) -> builtins.str:
        '''The name of the source location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-sourcelocationname
        '''
        result = self._values.get("source_location_name")
        assert result is not None, "Required property 'source_location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.AccessConfigurationProperty"]]:
        '''The access configuration for the source location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-accessconfiguration
        '''
        result = self._values.get("access_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.AccessConfigurationProperty"]], result)

    @builtins.property
    def default_segment_delivery_configuration(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty"]]:
        '''The default segment delivery configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration
        '''
        result = self._values.get("default_segment_delivery_configuration")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty"]], result)

    @builtins.property
    def segment_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.SegmentDeliveryConfigurationProperty"]]]]:
        '''The segment delivery configurations for the source location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-segmentdeliveryconfigurations
        '''
        result = self._values.get("segment_delivery_configurations")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnSourceLocation.SegmentDeliveryConfigurationProperty"]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the source location.

        Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSourceLocationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_mediatailor_60404695.IVodSourceRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnVodSource(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnVodSource",
):
    '''The VOD source configuration parameters.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html
    :cloudformationResource: AWS::MediaTailor::VodSource
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediatailor as mediatailor
        
        cfn_vod_source = mediatailor.CfnVodSource(self, "MyCfnVodSource",
            http_package_configurations=[mediatailor.CfnVodSource.HttpPackageConfigurationProperty(
                path="path",
                source_group="sourceGroup",
                type="type"
            )],
            source_location_name="sourceLocationName",
            vod_source_name="vodSourceName",
        
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
        http_package_configurations: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnVodSource.HttpPackageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        source_location_name: builtins.str,
        vod_source_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaTailor::VodSource``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param http_package_configurations: The HTTP package configurations for the VOD source.
        :param source_location_name: The name of the source location that the VOD source is associated with.
        :param vod_source_name: The name of the VOD source.
        :param tags: The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__456acf01c6ad372c9c8ba7c229fe88f13ceaab57f8599ae26cb522443527fd9d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVodSourceProps(
            http_package_configurations=http_package_configurations,
            source_location_name=source_location_name,
            vod_source_name=vod_source_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVodSource")
    @builtins.classmethod
    def arn_for_vod_source(
        cls,
        resource: "_aws_mediatailor_60404695.IVodSourceRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__224cd199576868d6ca76d7e26d603a6d1c6751f09853b7fb5b817a6eb612797a)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVodSource", [resource]))

    @jsii.member(jsii_name="isCfnVodSource")
    @builtins.classmethod
    def is_cfn_vod_source(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVodSource.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c9fef99885381928f7ba0e402481bee119922885242f232dbc479ebe8869d09e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVodSource", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__09f36c1aa9a889afe2053c87ff538aaf36dd3ae8b29c1a426f2f27df0c755587)
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
            type_hints = cached_type_hints(_typecheckingstub__0fac6a9f7df2b2fa380098721a1683c1b80379d1bf38dc173b47c777a640cc87)
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
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="vodSourceRef")
    def vod_source_ref(self) -> "_aws_mediatailor_60404695.VodSourceReference":
        '''A reference to a VodSource resource.'''
        return typing.cast("_aws_mediatailor_60404695.VodSourceReference", jsii.get(self, "vodSourceRef"))

    @builtins.property
    @jsii.member(jsii_name="httpPackageConfigurations")
    def http_package_configurations(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVodSource.HttpPackageConfigurationProperty"]]]:
        '''The HTTP package configurations for the VOD source.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVodSource.HttpPackageConfigurationProperty"]]], jsii.get(self, "httpPackageConfigurations"))

    @http_package_configurations.setter
    def http_package_configurations(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVodSource.HttpPackageConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1be44ceb1280a35c91079ff378249f514c9df3469b3e1257c192599da563deef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPackageConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceLocationName")
    def source_location_name(self) -> builtins.str:
        '''The name of the source location that the VOD source is associated with.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceLocationName"))

    @source_location_name.setter
    def source_location_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b024f23946c6a28358d006df405f270d55f1f6b4a70a5a588afc68d41cc70624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceLocationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vodSourceName")
    def vod_source_name(self) -> builtins.str:
        '''The name of the VOD source.'''
        return typing.cast(builtins.str, jsii.get(self, "vodSourceName"))

    @vod_source_name.setter
    def vod_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fe11f723e58c9d9e3dfc9ccb7d7fd5b0cd8cb02c57d5f7a45f9877126b0d6460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vodSourceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the VOD source.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0b30548ca419f7047c53d6514a5066199fd7138b99172f58964bdbf0d75d3395)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediatailor.CfnVodSource.HttpPackageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path", "source_group": "sourceGroup", "type": "type"},
    )
    class HttpPackageConfigurationProperty:
        def __init__(
            self,
            *,
            path: builtins.str,
            source_group: builtins.str,
            type: builtins.str,
        ) -> None:
            '''The HTTP package configuration properties for the requested VOD source.

            :param path: The relative path to the URL for this VOD source. This is combined with ``SourceLocation::HttpConfiguration::BaseUrl`` to form a valid URL.
            :param source_group: The name of the source group. This has to match one of the ``Channel::Outputs::SourceGroup`` .
            :param type: The streaming protocol for this package configuration. Supported values are ``HLS`` and ``DASH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediatailor as mediatailor
                
                http_package_configuration_property = mediatailor.CfnVodSource.HttpPackageConfigurationProperty(
                    path="path",
                    source_group="sourceGroup",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__0eb3dfa97b84bfa86c7915674bc55816a5f4e9bec9047c683b97e5bd68f4d997)
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument source_group", value=source_group, expected_type=type_hints["source_group"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "path": path,
                "source_group": source_group,
                "type": type,
            }

        @builtins.property
        def path(self) -> builtins.str:
            '''The relative path to the URL for this VOD source.

            This is combined with ``SourceLocation::HttpConfiguration::BaseUrl`` to form a valid URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html#cfn-mediatailor-vodsource-httppackageconfiguration-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_group(self) -> builtins.str:
            '''The name of the source group.

            This has to match one of the ``Channel::Outputs::SourceGroup`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html#cfn-mediatailor-vodsource-httppackageconfiguration-sourcegroup
            '''
            result = self._values.get("source_group")
            assert result is not None, "Required property 'source_group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The streaming protocol for this package configuration.

            Supported values are ``HLS`` and ``DASH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html#cfn-mediatailor-vodsource-httppackageconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpPackageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediatailor.CfnVodSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "http_package_configurations": "httpPackageConfigurations",
        "source_location_name": "sourceLocationName",
        "vod_source_name": "vodSourceName",
        "tags": "tags",
    },
)
class CfnVodSourceProps:
    def __init__(
        self,
        *,
        http_package_configurations: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnVodSource.HttpPackageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        source_location_name: builtins.str,
        vod_source_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVodSource``.

        :param http_package_configurations: The HTTP package configurations for the VOD source.
        :param source_location_name: The name of the source location that the VOD source is associated with.
        :param vod_source_name: The name of the VOD source.
        :param tags: The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediatailor as mediatailor
            
            cfn_vod_source_props = mediatailor.CfnVodSourceProps(
                http_package_configurations=[mediatailor.CfnVodSource.HttpPackageConfigurationProperty(
                    path="path",
                    source_group="sourceGroup",
                    type="type"
                )],
                source_location_name="sourceLocationName",
                vod_source_name="vodSourceName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4ff95c6173b55a15ec19a7b2a2215e5380dc3d4986fdb2e4c47b40fce1b625d9)
            check_type(argname="argument http_package_configurations", value=http_package_configurations, expected_type=type_hints["http_package_configurations"])
            check_type(argname="argument source_location_name", value=source_location_name, expected_type=type_hints["source_location_name"])
            check_type(argname="argument vod_source_name", value=vod_source_name, expected_type=type_hints["vod_source_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http_package_configurations": http_package_configurations,
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def http_package_configurations(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVodSource.HttpPackageConfigurationProperty"]]]:
        '''The HTTP package configurations for the VOD source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html#cfn-mediatailor-vodsource-httppackageconfigurations
        '''
        result = self._values.get("http_package_configurations")
        assert result is not None, "Required property 'http_package_configurations' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnVodSource.HttpPackageConfigurationProperty"]]], result)

    @builtins.property
    def source_location_name(self) -> builtins.str:
        '''The name of the source location that the VOD source is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html#cfn-mediatailor-vodsource-sourcelocationname
        '''
        result = self._values.get("source_location_name")
        assert result is not None, "Required property 'source_location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vod_source_name(self) -> builtins.str:
        '''The name of the VOD source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html#cfn-mediatailor-vodsource-vodsourcename
        '''
        result = self._values.get("vod_source_name")
        assert result is not None, "Required property 'vod_source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags assigned to the VOD source.

        Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see `Tagging AWS Elemental MediaTailor Resources <https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html#cfn-mediatailor-vodsource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVodSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannel",
    "CfnChannelPolicy",
    "CfnChannelPolicyProps",
    "CfnChannelProps",
    "CfnFunction",
    "CfnFunctionProps",
    "CfnLiveSource",
    "CfnLiveSourceProps",
    "CfnPlaybackConfiguration",
    "CfnPlaybackConfigurationProps",
    "CfnPrefetchSchedule",
    "CfnPrefetchScheduleProps",
    "CfnSourceLocation",
    "CfnSourceLocationProps",
    "CfnVodSource",
    "CfnVodSourceProps",
]

publication.publish()

def _typecheckingstub__95afc802641850838d7d754c58072c279165a93bff5fc055789c1090a21b9714(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_name: builtins.str,
    outputs: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.RequestOutputItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
    playback_mode: builtins.str,
    audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    filler_slate: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.SlateSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.LogConfigurationForChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    tier: typing.Optional[builtins.str] = None,
    time_shift_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.TimeShiftConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__418fb2485d366f3c8a7b8a95c0dcf780cd3d97d1eacd74f40d7d10b930f2ab95(
    resource: _aws_mediatailor_60404695.IChannelRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d19144d331ba31edd24b53fe62ecd68291785594e4276f682970808562a8790(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08ab9dccb4a244c93c8642dce766e1e9ee544479257409b787228df15d5435d7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    channel_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b40a7b4e84fbe554602e7462685b4c9b4a1175e608e5fd8e878b86fe361400ea(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d632b023994803b26caa2590748766e0dabab5ba299874fe587fa9f37c926bda(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd05180cbc64f9ab36b59c9143ba4df4683bae47e98fe90c0d0bacdd9fbb8fae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414356f19e6a1e142f58fb20d5aa3f44fd76f93ad6f9a944f9177c71e65bd031(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c205b75797f1a6f80dab721b03fc96335f8bd384f7c63aab656bd3136a90ed(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnChannel.RequestOutputItemProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f01c3b2a4d663235632876690f021c08885e2683808fd8f8354ec563a6cdbcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978734f277fe2347cb97632bb681ac7a90ce350df65be207f74234337bd3d49b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb99598f2b90f05f74078bf9dbab5d32c9f963ec0c7f60fc84c741cd7f7a72d5(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnChannel.SlateSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272cdcfa3dd55bace9d7517c474b5f20801108c57ec19149b84a6595215b1252(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnChannel.LogConfigurationForChannelProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bde4918e4d23e04040b87adfc6739660dba537c84b0ca2f813daacbf009f298(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35198b30b0429365e601c60c11c6bb80791a3176a301d1fac563832c0e0edd38(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3c40cad99c53a2773855f4cd98f257598efcf21fd51b6bb734064a33f180c7(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnChannel.TimeShiftConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53b76fce032c9b5b0b3ab03b03ec40f7f01e061c77ffbd9e3b0101056eecfb5(
    *,
    manifest_window_seconds: typing.Optional[jsii.Number] = None,
    min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
    min_update_period_seconds: typing.Optional[jsii.Number] = None,
    suggested_presentation_delay_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e31cc39cb17d92681c3726ed02355f545c95afa6883032b1e93af1c43179acc2(
    *,
    ad_markup_type: typing.Optional[typing.Sequence[builtins.str]] = None,
    manifest_window_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a7e7699e2937a5b57a4d1b83f5129fa2b21541bc55e1f79a1ca106377c5300(
    *,
    log_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1d4c3a316ddc28d5db9dbd943c872960619d5643164875a0009ce4f4639f744(
    *,
    manifest_name: builtins.str,
    source_group: builtins.str,
    dash_playlist_settings: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.DashPlaylistSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hls_playlist_settings: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.HlsPlaylistSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87bdd7eb43c3b69dcc5175fbdbdf3f64ecc1bea153e89e341c467115c5854c1e(
    *,
    source_location_name: typing.Optional[builtins.str] = None,
    vod_source_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6f8310362aba9a6cdbcee3376c31f278a1a77eb2cfdd2c6e322b1b49d57eaa(
    *,
    max_time_delay_seconds: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31394bd173fe2beb5213e9badd5aafc6ea2b160b870f8a0efcdd0c7418364408(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_name: builtins.str,
    policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abda8f12a5a6b5f01e1256783fdb08f119d1fa2429aa22f36113b572849fc90e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb5c51872ae1d2e26ab60faf42e8f67d099d72d6182d14f72ac00d2820a1253(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77acf1b52692f677278f400d1fc6aac28c4f4db4641fe9077e743d4105363c94(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33c69c2a3ec02545796ab2a280c6251e38cd027ef575f6e9b82b2238d613b8fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d60990c1542e708efa866295766195f2b5035b80cea3aacc1e22a1d78dd31022(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0760e4c2515aab3aa0d5aa04febae58f777b0b8b02fe135798d73d9cfc228e7d(
    *,
    channel_name: builtins.str,
    policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f9c53dfc17c104058553b2c51bffbfeea7885ab9628618cedcaf8634562913(
    *,
    channel_name: builtins.str,
    outputs: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.RequestOutputItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
    playback_mode: builtins.str,
    audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    filler_slate: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.SlateSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.LogConfigurationForChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    tier: typing.Optional[builtins.str] = None,
    time_shift_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnChannel.TimeShiftConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd96c58f31f24adb3cea08347b5cb88afb7a1644c1d49acf5ea18ef7e858b6b4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    function_id: builtins.str,
    function_type: builtins.str,
    concurrent_executor_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.ConcurrentExecutorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_output_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.CustomOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    http_request_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.HttpRequestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sequential_executor_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.SequentialExecutorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1622bc3b9fb588270223d9f7e4597e460a8eb30134a5e06d974142e25db0e60(
    resource: _aws_mediatailor_60404695.IFunctionRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75251cc24b0becd917928021558ddb9ae78d087dab72897b6c0dd0a109fe49ea(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d78839ae256142aacfd95c57d31064da1eb11fcf3df6b8c58cab6aef81d452(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0691ea7e84dd9690413b0c03614038e090ff0deec3c43edc0664a06d3031c7ce(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e672160af6c70e20c93ee58a3d25e27152153feb541dc68112b2310551674635(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb28c3052dd431563a7b26a7dce4b50d1c29abc2106f42fa0a5329270452f9c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7881dd44052d7a7cfe200f4556de1fc9a705e530c1e461e83ad35044d7d4fba4(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnFunction.ConcurrentExecutorConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d34312157c19e7408ec3ea1cda432a669a0967161e5df7dda4eab223f9a0b044(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnFunction.CustomOutputConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2219a19201f0a17be79ff6717a47ca2d73b9c0b9ed0432d4890f90b4256b4d3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a807bd0f7ad759c090dcf86e543a221b7023a5c09b76d141eebdf0d9505192e(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnFunction.HttpRequestConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ad517a9634af2cf1cf7cddd2dd3cecff513a52e7a1bb68e109fc8982897972(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnFunction.SequentialExecutorConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b65b0a9bacbd0f65526afeb7cf1e0c3ca3773c11abb883bbf33a47ef72445de0(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178948756e734ee68c9d1fe0aa6ae03bc94447092d71fbf586f1f0c568c19ef9(
    *,
    function_list: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.FunctionRefProperty, typing.Dict[builtins.str, typing.Any]]]]],
    max_concurrency: jsii.Number,
    output: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]],
    runtime: builtins.str,
    timeout_milliseconds: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61544711aa26c5056e9b4d3cfab7dee3d6eaa0f011cb57fde19c711b08a922de(
    *,
    runtime: builtins.str,
    output: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5737ad8fdf57086197584ef5d9e43c62428f917f712bc50c4302371649b0c300(
    *,
    alias: typing.Optional[builtins.str] = None,
    function_id: typing.Optional[builtins.str] = None,
    run_condition: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f6999ed1a463a1d66432cdff27ee1e9591dc5d3ae4707cd971a7668661f38f8(
    *,
    method_type: builtins.str,
    request_timeout_milliseconds: jsii.Number,
    runtime: builtins.str,
    url: builtins.str,
    body: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    output: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__500d6a7aa0edd3b223d18e64c8c78d74551a1f7285ddd9f7bcf2f3958acdb83d(
    *,
    function_list: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.FunctionRefProperty, typing.Dict[builtins.str, typing.Any]]]]],
    runtime: builtins.str,
    timeout_milliseconds: jsii.Number,
    output: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7008df40fa116385e225dc9fc11c5a0c3905883fa95cd4742d1f9506eddc5e(
    *,
    function_id: builtins.str,
    function_type: builtins.str,
    concurrent_executor_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.ConcurrentExecutorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_output_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.CustomOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    http_request_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.HttpRequestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sequential_executor_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnFunction.SequentialExecutorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caad9e925cf2074f54088c0241999fdbc5c194736555867b7765527f3cac0b4a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    http_package_configurations: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLiveSource.HttpPackageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    live_source_name: builtins.str,
    source_location_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b2b664e7ed5590505b220acf48fbfff98a521078fb4767ee5949f9cbd9c0e6a(
    resource: _aws_mediatailor_60404695.ILiveSourceRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c51a8418725bfba543ac688a7eb06834d4a3743f7a11753f15ed105923071e2(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed469803ff91fff7fc3040fc3d0bb3fa9a21fd4b59da12961328098a4c73f954(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a52884dbe2ce928f779cdf8bd2581daa116db94102e6bf411658389d41cc6b49(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa182da40e12286d6ab8a5538c3092bd85a8ea141d3aa51a69178e242b53eb9(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnLiveSource.HttpPackageConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1795bf7c4263fcfbd30da5a955ba17d73ac00d7a1fcf627458bef546932345(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b7526b80803bba8c5dd84e954c48ba46ef9972bfff2752568fcf3f83123cdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b020567a78e7c965d540da779a72d64a6ce4c5d0070398ae50aae2bb69a1b916(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13f0630b3469ba702929b845c7fafefb841b9e63dd48246c3a1e4880161e80e4(
    *,
    path: builtins.str,
    source_group: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc89490043dd5c6acaa08c89f60f172168bb565829b267f04a07c3038db8079(
    *,
    http_package_configurations: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnLiveSource.HttpPackageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    live_source_name: builtins.str,
    source_location_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dcfb97a898a80ee6a7b069e26028183e8a797f0c48fdbd4fe6ecb8ad6fb6911(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ad_decision_server_url: builtins.str,
    name: builtins.str,
    video_content_source_url: builtins.str,
    ad_conditioning_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdConditioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ad_decision_server_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ads_personalization_concurrency: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ads_personalization_timeouts: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    avail_suppression: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AvailSuppressionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bumper: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.BumperProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cdn_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.CdnConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    configuration_aliases: typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], _aws_cdk_0cae9daa.IResolvable]] = None,
    dash_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.DashConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    function_mapping: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    hls_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.HlsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    insertion_mode: typing.Optional[builtins.str] = None,
    live_pre_roll_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.LivePreRollConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manifest_processing_rules: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.ManifestProcessingRulesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    personalization_threshold_seconds: typing.Optional[jsii.Number] = None,
    slate_ad_url: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    transcode_profile_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3335a30b563b424b55efc3fb3fba650a85702c1595cf9e59fff9aeeca795f023(
    resource: _aws_mediatailor_60404695.IPlaybackConfigurationRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b043c094b53206253d6d432de9db2a20fbb0b231bb418d502fed6f0f4914378f(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e8d0bace48ee23b08adfc8cf00f58f43f86ed9fc0b465a4b9dcfaf76c4a0da6(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2663bd7b40c241aeca662815955b87975e8fe4bc363957cbc451c0b30548ea05(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4b56f24629d4c9547e0b37415660678e3944b62d46a1e55902b5e6c66efe7c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77c686fa09a4612a1bcc44cf669fb2ff9905ec398da89167e8b0280d8f86750d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75b50d6fe13101dc70996fb19d5c8a163f6176ddcd37a0ebe0b08f5f768c4caf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb81abb7826e9e9444261d39e06ed23acbaea73a559203da5ca788273a1bbc94(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.AdConditioningConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22beebeb31ad301089cab0d08fffbf7d70892dcdea0070ebbc8c036efa8475c2(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a729a919a8e3f978c846240e1014b7c0fec80dd63195aa5866c57644d4451e2(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ee4b8d1ac254be276c7782458b9e78d24c83f92c6f56af8e12ac5df9cc47fb(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace1eb1809c3c05a0b25523b0f61020aa7d5a69057cdffb522c74d7881b0c1c8(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.AvailSuppressionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9796c91ff0edc4be04998ed524be6012eae7fa3574e5c120fe393fab79a2a12(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.BumperProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8cdb9ae7c7cff86d16687474d65af7b5ddb86256dce88926d439a4c82e07acf(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.CdnConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e98fdfcc661f8c91728f46bbafe4c5c1160d075338a4b6e66789b7147006439(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1528a1dd277ec2643ed08e71e4d817660b15a7515d36800d1a4c45be4bdd944(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.DashConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce9f9a164e16917763fbfce05ef66083a15fe183466a65359b9714cccd1b42c(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c53800db93b8d74956b4a23e4372e79b770aeb9e98d1001196859bcb54e01d0(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.HlsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db08ab0a15b5e71226bad5d4d94682032ded680bfe3f777d4f4ef02bad39cbf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d20db08db40dad827f8fdbbfd9ec60bdd03cf18a0cf5f764aedb5ed9040d782f(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.LivePreRollConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6fbfb7358fa4aedc54b5bb197d51ad46d862c18709b40e671060ad3ab400894(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.LogConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef2be3172d1df94da8603df93c79aa68aa713132917a7f79ee5d67eca13bdc5(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPlaybackConfiguration.ManifestProcessingRulesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4368b8d6051e265005679584bc63cae740383861026b06e26c9de1f0954cee(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905f1e5f55e6f998cb17136c0f4a82bcebc656a336f14fbf28f45aab3b7ab881(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76f0247a7421af76c87f40a095ad78f3c6ad9b0a567e02e8daca4c67eee9302(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab6a880d781d782bb5f703943747735b9af031af290dd1ad2e9ebe2732d26c2d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f7802737ba8294b0aa8d203c7f9bc7ff38b98bf17f1f9066c772b203c711ea(
    *,
    streaming_media_file_conditioning: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be522b7afa0a40f87526bb5baa285488ee37ade9f2edd720c05a21cdcf1ba383(
    *,
    http_request: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.HttpRequestProperty, typing.Dict[builtins.str, typing.Any]]],
    vast_response: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.VastResponseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84cc8c470c35ea1870d24a6e58a722cc2d0952d699c858000349755866ccea6(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325f2da032e4a3f14a765ea1c946c8707bfd649b7df813a9bf9d270b2edfcd0f(
    *,
    exclude_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    publish_opt_in_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c54804620edf90d6d14b94d837c502afb0350e36766d359c51c934fb9de93d10(
    *,
    enable_vod_vast_parallelization: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
    max_concurrent_ads_requests: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081de2ae59707e39bdb75d2de6531849e92a0be4913aa6286dd36f4fce70bbee(
    *,
    ads_request_timeout_milliseconds: typing.Optional[jsii.Number] = None,
    live_maximum_ads_personalization_time_milliseconds: typing.Optional[jsii.Number] = None,
    prefetch_ads_request_timeout_milliseconds: typing.Optional[jsii.Number] = None,
    prefetch_maximum_ads_personalization_time_milliseconds: typing.Optional[jsii.Number] = None,
    vod_maximum_ads_personalization_time_milliseconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b4195a89a44a68af7fade1bdaaea19a0b3104ca5fc40a34ac2c5440a8d5f1d0(
    *,
    fill_policy: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4d8e62c25a38e7667cc4c7f67e131b03585a6b02ccb1e6956572e91491c2565(
    *,
    end_url: typing.Optional[builtins.str] = None,
    start_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ed9c00b014872bf1ce7a32f613cee3497f59c3a8f8ed7c34d59e731f7a30a1(
    *,
    ad_segment_url_prefix: typing.Optional[builtins.str] = None,
    content_segment_url_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed436176dc8bad043834221f15764e2997c06a895bb8dc9c71dc24d9d4c62fe8(
    *,
    manifest_endpoint_prefix: typing.Optional[builtins.str] = None,
    mpd_location: typing.Optional[builtins.str] = None,
    origin_manifest_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc73c21d5b8ef9a10443ded7266b5dc44c0980daadbc5f8f5a49b9793967e1ed(
    *,
    manifest_endpoint_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1a27fdd711151047a9a372fb7f330c24afc446e3e97dd914e66a4a4a637017(
    *,
    body: typing.Optional[builtins.str] = None,
    compress_request: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    http_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1326ff9046a5c3b87adfaac42a0610149574f9d367d1c04949ccf8a48d1a93(
    *,
    ad_decision_server_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.PreRollAdDecisionServerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ad_decision_server_url: typing.Optional[builtins.str] = None,
    max_duration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b1a16aa41d90a41939aee256096b129464d60c87f4e8ac32c6ce9c43de9dcfd(
    *,
    percent_enabled: jsii.Number,
    ads_interaction_log: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdsInteractionLogProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enabled_logging_strategies: typing.Optional[typing.Sequence[builtins.str]] = None,
    manifest_service_interaction_log: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.ManifestServiceInteractionLogProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef5bb7a5b9697fa8ca9b867a5d8f7f8c6041a353ed9fad8ec9b06f14fd300d73(
    *,
    ad_marker_passthrough: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdMarkerPassthroughProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__877d8a60ce1cb5812848b2604b2ff4a34e5662596f05cca7a6a335a5facd5374(
    *,
    exclude_event_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c891247344a5816c5f6036ffe8b027890782702417987f5fe28421b1757a52f5(
    *,
    vast_response: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.PreRollVastResponseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__770bca0bb4db614052f95822f0ce3e52f118ce264f511205bda617ca7797829a(
    *,
    ad_sequencing_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5eccc314698469708f3b54b63cf366c2cda8be0723d3d1b1140bc18e7ffe980(
    *,
    ad_sequencing_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935886ab495203cc213786b925e7fd8fe4acd3f9db5864d4f1f5c011539346f8(
    *,
    ad_decision_server_url: builtins.str,
    name: builtins.str,
    video_content_source_url: builtins.str,
    ad_conditioning_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdConditioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ad_decision_server_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdDecisionServerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ads_personalization_concurrency: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdsPersonalizationConcurrencyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ads_personalization_timeouts: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AdsPersonalizationTimeoutsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    avail_suppression: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.AvailSuppressionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bumper: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.BumperProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cdn_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.CdnConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    configuration_aliases: typing.Optional[typing.Union[typing.Mapping[builtins.str, typing.Any], _aws_cdk_0cae9daa.IResolvable]] = None,
    dash_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.DashConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    function_mapping: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    hls_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.HlsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    insertion_mode: typing.Optional[builtins.str] = None,
    live_pre_roll_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.LivePreRollConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manifest_processing_rules: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPlaybackConfiguration.ManifestProcessingRulesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    personalization_threshold_seconds: typing.Optional[jsii.Number] = None,
    slate_ad_url: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    transcode_profile_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda230bb96c6a9dde0582b55cf131524f9dfc5b99d2f757c2fc0d3232e38bf74(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    playback_configuration_name: builtins.str,
    consumption: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.PrefetchConsumptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    recurring_prefetch_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retrieval: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.PrefetchRetrievalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule_type: typing.Optional[builtins.str] = None,
    stream_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9494a130ab023cb8f1efc4abac0a1a99f59b2235691c53eb96ba51ecebaa725(
    resource: _aws_mediatailor_60404695.IPrefetchScheduleRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b415e15129c07ef912c53b46ad5b2fef8f90e537665ed39a283b8dbf7e3ba2(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bff129f6ff7e96dfe9ed305243681d972d3a5078f8e1f8bd03dfc7a6bd77e51(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50bf6fc42f5a3633ecf526f1a716df7113700d9218eaa290702d12ba126775e8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd8fc0fd997068a5a9913c04ff0cfc0f761c7da140916bf37f02b29f5cc7742a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dabe2e2008888c9c945448e0d661fbdd8564f685ee56d6a1779e29d4cad4ec4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b6374edcf95c8a9b4cce6071faefac50f1526b162dfaf0479417803056905d(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPrefetchSchedule.PrefetchConsumptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4dceeb4970cc6d2cadedc0218d4ac6586f2d7683ae6a1b0268ddce2f6705f92(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8b1ee3296f2489c46c64734a0363c25b87a5d06c5571dee7c59e32959a089c5(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnPrefetchSchedule.PrefetchRetrievalProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ea4297602a4c698f4a7a596e39444f37df263a76058421ef00d6ab44adc7e3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d1ce3c2153a851f8bc18f289d2e3c3b7e8626f0492a8b9c5007908df5d1248(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2898d6ee5d6cf5febc03f59aedc49d2edbe5e8595ca50d955206285ca9833352(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e58a7f144bd17d3319e9ad03250010949871dc8836ac9ac67237335d03084d7c(
    *,
    dynamic_variable: builtins.str,
    operator: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18c177a23efbd7d3f4f9690a9e27fa151a0a90be1132ce2f4efab08eabda9232(
    *,
    end_time: builtins.str,
    avail_matching_criteria: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.AvailMatchingCriteriaProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    start_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c2ecb75839a35994f3696a2d7c3d544f3638146358e28982fb7c42826178f3(
    *,
    end_time: builtins.str,
    dynamic_variables: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    start_time: typing.Optional[builtins.str] = None,
    traffic_shaping_retrieval_window: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    traffic_shaping_tps_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    traffic_shaping_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2a371af0ad0c1d79415ae11b9755cca464c7035c6f622d511446260cef06603(
    *,
    avail_matching_criteria: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.AvailMatchingCriteriaProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    retrieved_ad_expiration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05bd8652a49c8686098c037ea3c9547bb9a1f7c2a92b033cc181e6fdf0428f4d(
    *,
    end_time: builtins.str,
    recurring_consumption: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.RecurringConsumptionProperty, typing.Dict[builtins.str, typing.Any]]],
    recurring_retrieval: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.RecurringRetrievalProperty, typing.Dict[builtins.str, typing.Any]]],
    start_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00104803c0902da691a3e7ce3c7070e8259a6ffed7ee23a85b48e3f039e8f0f2(
    *,
    delay_after_avail_end_seconds: typing.Optional[jsii.Number] = None,
    dynamic_variables: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    traffic_shaping_retrieval_window: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.TrafficShapingRetrievalWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    traffic_shaping_tps_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.TrafficShapingTpsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    traffic_shaping_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72ad8a6953ae3d4cd6c48d9ff13d2d032668dfad2a83cd1e697b0fa6669d7b40(
    *,
    retrieval_window_duration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d12d072deb9d1c155a01a6845b704c9e65ffe9d4675dab270978f29c3881b5(
    *,
    peak_concurrent_users: typing.Optional[jsii.Number] = None,
    peak_tps: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51933737a0a3bf5f476a73e634bbeb2dfebf67ef8c85c29f58466fd17df23d63(
    *,
    name: builtins.str,
    playback_configuration_name: builtins.str,
    consumption: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.PrefetchConsumptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    recurring_prefetch_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.RecurringPrefetchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retrieval: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnPrefetchSchedule.PrefetchRetrievalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule_type: typing.Optional[builtins.str] = None,
    stream_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd693d384196965a6e6e42aa969746fa450f3a5099e7be68c145dcc9f5f7e59d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    http_configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.HttpConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    source_location_name: builtins.str,
    access_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.AccessConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_segment_delivery_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_delivery_configurations: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.SegmentDeliveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d17f619c660f9b6fd1fb2b7aeb5e9f11758a50027ed09924fa2715dfe61616(
    resource: _aws_mediatailor_60404695.ISourceLocationRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28b271fcaa782dcce30289b4d3e9cd1597cc2e403d5decad01698ce3810fc642(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a67b4bd9eabe7dff32771e3855c5f4b09c52cc321708cd63f64f1f290488c1(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9c819cfa165355742944ead86f157d5e4fe520ec150ce7cb7367ac66b39c700(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be0faeec30de7aa74e972fa9be4f5ef1134314ff5984d14b00fc6e2596ceb488(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSourceLocation.HttpConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3bd8c206592bff1adae3d34013e03de975c95df7847310b70d730fb7b9498b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1bc53fb2d4148510df3244898b3da3e4ac17d9faee3835bc73da5ad63931214(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSourceLocation.AccessConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b431a09702c35ab502bf465075ac7a7d86895d1cc20d16caec630b4e0a366dc(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__725f16ab7057c1a2a01a0de087479721b15670cf708ed95838c4271ad45c009a(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnSourceLocation.SegmentDeliveryConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af85fa3fdd92d33488c46dc70861bcea3919f31a13ab83bd91920e11557a0620(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df138d384fef8104d70a1dae201bed1b055b8ef01c97ffa764008d6423001711(
    *,
    access_type: typing.Optional[builtins.str] = None,
    secrets_manager_access_token_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.SecretsManagerAccessTokenConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8f2bdbcfd97bfab31281eb19a1cb75bcd15849095da44b410f2703593facdc(
    *,
    base_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a880194f274158b8a0b3d6dab7716d3a29cb93edfb1f5ef3e8b507eb8379c18a(
    *,
    base_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2feb4b5d75163b5824572e2ce3caac3c88483a5919f3648703d571fb23723c19(
    *,
    header_name: typing.Optional[builtins.str] = None,
    secret_arn: typing.Optional[builtins.str] = None,
    secret_string_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__383b15aa1a1faec4ed8f2f0982e5ba8e88dfe9184d36b17c3b787e66a0c45076(
    *,
    base_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb562c06ea390d62a28e2d88d462a731b39635f142da846f03422a25348fff7c(
    *,
    http_configuration: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.HttpConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    source_location_name: builtins.str,
    access_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.AccessConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_segment_delivery_configuration: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.DefaultSegmentDeliveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_delivery_configurations: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnSourceLocation.SegmentDeliveryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__456acf01c6ad372c9c8ba7c229fe88f13ceaab57f8599ae26cb522443527fd9d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    http_package_configurations: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnVodSource.HttpPackageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    source_location_name: builtins.str,
    vod_source_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224cd199576868d6ca76d7e26d603a6d1c6751f09853b7fb5b817a6eb612797a(
    resource: _aws_mediatailor_60404695.IVodSourceRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9fef99885381928f7ba0e402481bee119922885242f232dbc479ebe8869d09e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09f36c1aa9a889afe2053c87ff538aaf36dd3ae8b29c1a426f2f27df0c755587(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fac6a9f7df2b2fa380098721a1683c1b80379d1bf38dc173b47c777a640cc87(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be44ceb1280a35c91079ff378249f514c9df3469b3e1257c192599da563deef(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnVodSource.HttpPackageConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b024f23946c6a28358d006df405f270d55f1f6b4a70a5a588afc68d41cc70624(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe11f723e58c9d9e3dfc9ccb7d7fd5b0cd8cb02c57d5f7a45f9877126b0d6460(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b30548ca419f7047c53d6514a5066199fd7138b99172f58964bdbf0d75d3395(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb3dfa97b84bfa86c7915674bc55816a5f4e9bec9047c683b97e5bd68f4d997(
    *,
    path: builtins.str,
    source_group: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff95c6173b55a15ec19a7b2a2215e5380dc3d4986fdb2e4c47b40fce1b625d9(
    *,
    http_package_configurations: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnVodSource.HttpPackageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    source_location_name: builtins.str,
    vod_source_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
