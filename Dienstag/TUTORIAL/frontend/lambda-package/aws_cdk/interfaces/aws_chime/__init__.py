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


from ..._jsii import *

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

    import aws_cdk.interfaces as _interfaces_8ca7e747
    import constructs as _constructs_77d1e7e8
else:

    _constructs_77d1e7e8 = _LazyImport("constructs")
    _interfaces_8ca7e747 = _LazyImport("aws_cdk.interfaces")


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.AppInstanceBotReference",
    jsii_struct_bases=[],
    name_mapping={"app_instance_bot_arn": "appInstanceBotArn"},
)
class AppInstanceBotReference:
    def __init__(self, *, app_instance_bot_arn: builtins.str) -> None:
        '''A reference to a AppInstanceBot resource.

        :param app_instance_bot_arn: The AppInstanceBotArn of the AppInstanceBot resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            app_instance_bot_reference = interfaces_chime.AppInstanceBotReference(
                app_instance_bot_arn="appInstanceBotArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d94314e184ef238bc15359652813db5a17decbc7880453c10eebfdb5aee1574b)
            check_type(argname="argument app_instance_bot_arn", value=app_instance_bot_arn, expected_type=type_hints["app_instance_bot_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_instance_bot_arn": app_instance_bot_arn,
        }

    @builtins.property
    def app_instance_bot_arn(self) -> builtins.str:
        '''The AppInstanceBotArn of the AppInstanceBot resource.'''
        result = self._values.get("app_instance_bot_arn")
        assert result is not None, "Required property 'app_instance_bot_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppInstanceBotReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.AppInstanceReference",
    jsii_struct_bases=[],
    name_mapping={"app_instance_arn": "appInstanceArn"},
)
class AppInstanceReference:
    def __init__(self, *, app_instance_arn: builtins.str) -> None:
        '''A reference to a AppInstance resource.

        :param app_instance_arn: The AppInstanceArn of the AppInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            app_instance_reference = interfaces_chime.AppInstanceReference(
                app_instance_arn="appInstanceArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ce7a63f08f74043f81dd278aff7af9a1fbed0722dd9d181168266b0223b7dd9a)
            check_type(argname="argument app_instance_arn", value=app_instance_arn, expected_type=type_hints["app_instance_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_instance_arn": app_instance_arn,
        }

    @builtins.property
    def app_instance_arn(self) -> builtins.str:
        '''The AppInstanceArn of the AppInstance resource.'''
        result = self._values.get("app_instance_arn")
        assert result is not None, "Required property 'app_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.AppInstanceUserReference",
    jsii_struct_bases=[],
    name_mapping={"app_instance_user_arn": "appInstanceUserArn"},
)
class AppInstanceUserReference:
    def __init__(self, *, app_instance_user_arn: builtins.str) -> None:
        '''A reference to a AppInstanceUser resource.

        :param app_instance_user_arn: The AppInstanceUserArn of the AppInstanceUser resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            app_instance_user_reference = interfaces_chime.AppInstanceUserReference(
                app_instance_user_arn="appInstanceUserArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0a21d6b54c1a60d27402b1eed938ae67bfee72c94f33036fdd030210620f2b08)
            check_type(argname="argument app_instance_user_arn", value=app_instance_user_arn, expected_type=type_hints["app_instance_user_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_instance_user_arn": app_instance_user_arn,
        }

    @builtins.property
    def app_instance_user_arn(self) -> builtins.str:
        '''The AppInstanceUserArn of the AppInstanceUser resource.'''
        result = self._values.get("app_instance_user_arn")
        assert result is not None, "Required property 'app_instance_user_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppInstanceUserReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.ChannelFlowReference",
    jsii_struct_bases=[],
    name_mapping={"channel_flow_arn": "channelFlowArn"},
)
class ChannelFlowReference:
    def __init__(self, *, channel_flow_arn: builtins.str) -> None:
        '''A reference to a ChannelFlow resource.

        :param channel_flow_arn: The Arn of the ChannelFlow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            channel_flow_reference = interfaces_chime.ChannelFlowReference(
                channel_flow_arn="channelFlowArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__61d260a072d1387d8809a2f6808a63d6814fb8a1f1a8f87644726b5cbb1a26a5)
            check_type(argname="argument channel_flow_arn", value=channel_flow_arn, expected_type=type_hints["channel_flow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_flow_arn": channel_flow_arn,
        }

    @builtins.property
    def channel_flow_arn(self) -> builtins.str:
        '''The Arn of the ChannelFlow resource.'''
        result = self._values.get("channel_flow_arn")
        assert result is not None, "Required property 'channel_flow_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelFlowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.ChannelReference",
    jsii_struct_bases=[],
    name_mapping={"channel_arn": "channelArn", "chime_bearer": "chimeBearer"},
)
class ChannelReference:
    def __init__(
        self,
        *,
        channel_arn: builtins.str,
        chime_bearer: builtins.str,
    ) -> None:
        '''A reference to a Channel resource.

        :param channel_arn: The Arn of the Channel resource.
        :param chime_bearer: The ChimeBearer of the Channel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            channel_reference = interfaces_chime.ChannelReference(
                channel_arn="channelArn",
                chime_bearer="chimeBearer"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f9a1c6965f18718c33c9cfd586a74d7dae12c1e318133befd47bae0d55b55365)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
            check_type(argname="argument chime_bearer", value=chime_bearer, expected_type=type_hints["chime_bearer"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
        }

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''The Arn of the Channel resource.'''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def chime_bearer(self) -> builtins.str:
        '''The ChimeBearer of the Channel resource.'''
        result = self._values.get("chime_bearer")
        assert result is not None, "Required property 'chime_bearer' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_chime.IAppInstanceBotRef")
class IAppInstanceBotRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AppInstanceBot.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appInstanceBotRef")
    def app_instance_bot_ref(self) -> "AppInstanceBotReference":
        '''(experimental) A reference to a AppInstanceBot resource.

        :stability: experimental
        '''
        ...


class _IAppInstanceBotRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AppInstanceBot.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.IAppInstanceBotRef"

    @builtins.property
    @jsii.member(jsii_name="appInstanceBotRef")
    def app_instance_bot_ref(self) -> "AppInstanceBotReference":
        '''(experimental) A reference to a AppInstanceBot resource.

        :stability: experimental
        '''
        return typing.cast("AppInstanceBotReference", jsii.get(self, "appInstanceBotRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppInstanceBotRef).__jsii_proxy_class__ = lambda : _IAppInstanceBotRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_chime.IAppInstanceRef")
class IAppInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AppInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appInstanceRef")
    def app_instance_ref(self) -> "AppInstanceReference":
        '''(experimental) A reference to a AppInstance resource.

        :stability: experimental
        '''
        ...


class _IAppInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AppInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.IAppInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="appInstanceRef")
    def app_instance_ref(self) -> "AppInstanceReference":
        '''(experimental) A reference to a AppInstance resource.

        :stability: experimental
        '''
        return typing.cast("AppInstanceReference", jsii.get(self, "appInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppInstanceRef).__jsii_proxy_class__ = lambda : _IAppInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_chime.IAppInstanceUserRef")
class IAppInstanceUserRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AppInstanceUser.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appInstanceUserRef")
    def app_instance_user_ref(self) -> "AppInstanceUserReference":
        '''(experimental) A reference to a AppInstanceUser resource.

        :stability: experimental
        '''
        ...


class _IAppInstanceUserRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AppInstanceUser.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.IAppInstanceUserRef"

    @builtins.property
    @jsii.member(jsii_name="appInstanceUserRef")
    def app_instance_user_ref(self) -> "AppInstanceUserReference":
        '''(experimental) A reference to a AppInstanceUser resource.

        :stability: experimental
        '''
        return typing.cast("AppInstanceUserReference", jsii.get(self, "appInstanceUserRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppInstanceUserRef).__jsii_proxy_class__ = lambda : _IAppInstanceUserRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_chime.IChannelFlowRef")
class IChannelFlowRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelFlow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelFlowRef")
    def channel_flow_ref(self) -> "ChannelFlowReference":
        '''(experimental) A reference to a ChannelFlow resource.

        :stability: experimental
        '''
        ...


class _IChannelFlowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelFlow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.IChannelFlowRef"

    @builtins.property
    @jsii.member(jsii_name="channelFlowRef")
    def channel_flow_ref(self) -> "ChannelFlowReference":
        '''(experimental) A reference to a ChannelFlow resource.

        :stability: experimental
        '''
        return typing.cast("ChannelFlowReference", jsii.get(self, "channelFlowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelFlowRef).__jsii_proxy_class__ = lambda : _IChannelFlowRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_chime.IChannelRef")
class IChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Channel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        ...


class _IChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Channel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.IChannelRef"

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        return typing.cast("ChannelReference", jsii.get(self, "channelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelRef).__jsii_proxy_class__ = lambda : _IChannelRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.IMediaInsightsPipelineConfigurationRef"
)
class IMediaInsightsPipelineConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MediaInsightsPipelineConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mediaInsightsPipelineConfigurationRef")
    def media_insights_pipeline_configuration_ref(
        self,
    ) -> "MediaInsightsPipelineConfigurationReference":
        '''(experimental) A reference to a MediaInsightsPipelineConfiguration resource.

        :stability: experimental
        '''
        ...


class _IMediaInsightsPipelineConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MediaInsightsPipelineConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.IMediaInsightsPipelineConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="mediaInsightsPipelineConfigurationRef")
    def media_insights_pipeline_configuration_ref(
        self,
    ) -> "MediaInsightsPipelineConfigurationReference":
        '''(experimental) A reference to a MediaInsightsPipelineConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("MediaInsightsPipelineConfigurationReference", jsii.get(self, "mediaInsightsPipelineConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMediaInsightsPipelineConfigurationRef).__jsii_proxy_class__ = lambda : _IMediaInsightsPipelineConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.IMediaPipelineKinesisVideoStreamPoolRef"
)
class IMediaPipelineKinesisVideoStreamPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MediaPipelineKinesisVideoStreamPool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mediaPipelineKinesisVideoStreamPoolRef")
    def media_pipeline_kinesis_video_stream_pool_ref(
        self,
    ) -> "MediaPipelineKinesisVideoStreamPoolReference":
        '''(experimental) A reference to a MediaPipelineKinesisVideoStreamPool resource.

        :stability: experimental
        '''
        ...


class _IMediaPipelineKinesisVideoStreamPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MediaPipelineKinesisVideoStreamPool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.IMediaPipelineKinesisVideoStreamPoolRef"

    @builtins.property
    @jsii.member(jsii_name="mediaPipelineKinesisVideoStreamPoolRef")
    def media_pipeline_kinesis_video_stream_pool_ref(
        self,
    ) -> "MediaPipelineKinesisVideoStreamPoolReference":
        '''(experimental) A reference to a MediaPipelineKinesisVideoStreamPool resource.

        :stability: experimental
        '''
        return typing.cast("MediaPipelineKinesisVideoStreamPoolReference", jsii.get(self, "mediaPipelineKinesisVideoStreamPoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMediaPipelineKinesisVideoStreamPoolRef).__jsii_proxy_class__ = lambda : _IMediaPipelineKinesisVideoStreamPoolRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_chime.ISipMediaApplicationRef")
class ISipMediaApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SipMediaApplication.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sipMediaApplicationRef")
    def sip_media_application_ref(self) -> "SipMediaApplicationReference":
        '''(experimental) A reference to a SipMediaApplication resource.

        :stability: experimental
        '''
        ...


class _ISipMediaApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SipMediaApplication.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.ISipMediaApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="sipMediaApplicationRef")
    def sip_media_application_ref(self) -> "SipMediaApplicationReference":
        '''(experimental) A reference to a SipMediaApplication resource.

        :stability: experimental
        '''
        return typing.cast("SipMediaApplicationReference", jsii.get(self, "sipMediaApplicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISipMediaApplicationRef).__jsii_proxy_class__ = lambda : _ISipMediaApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_chime.IVoiceConnectorRef")
class IVoiceConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VoiceConnector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="voiceConnectorRef")
    def voice_connector_ref(self) -> "VoiceConnectorReference":
        '''(experimental) A reference to a VoiceConnector resource.

        :stability: experimental
        '''
        ...


class _IVoiceConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VoiceConnector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chime.IVoiceConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="voiceConnectorRef")
    def voice_connector_ref(self) -> "VoiceConnectorReference":
        '''(experimental) A reference to a VoiceConnector resource.

        :stability: experimental
        '''
        return typing.cast("VoiceConnectorReference", jsii.get(self, "voiceConnectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVoiceConnectorRef).__jsii_proxy_class__ = lambda : _IVoiceConnectorRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.MediaInsightsPipelineConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "media_insights_pipeline_configuration_arn": "mediaInsightsPipelineConfigurationArn",
    },
)
class MediaInsightsPipelineConfigurationReference:
    def __init__(
        self,
        *,
        media_insights_pipeline_configuration_arn: builtins.str,
    ) -> None:
        '''A reference to a MediaInsightsPipelineConfiguration resource.

        :param media_insights_pipeline_configuration_arn: The MediaInsightsPipelineConfigurationArn of the MediaInsightsPipelineConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            media_insights_pipeline_configuration_reference = interfaces_chime.MediaInsightsPipelineConfigurationReference(
                media_insights_pipeline_configuration_arn="mediaInsightsPipelineConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ce2497cdb7fb79a6744dfcaf40a220bd30b2631ecab2f45c481f65ff50e686ff)
            check_type(argname="argument media_insights_pipeline_configuration_arn", value=media_insights_pipeline_configuration_arn, expected_type=type_hints["media_insights_pipeline_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "media_insights_pipeline_configuration_arn": media_insights_pipeline_configuration_arn,
        }

    @builtins.property
    def media_insights_pipeline_configuration_arn(self) -> builtins.str:
        '''The MediaInsightsPipelineConfigurationArn of the MediaInsightsPipelineConfiguration resource.'''
        result = self._values.get("media_insights_pipeline_configuration_arn")
        assert result is not None, "Required property 'media_insights_pipeline_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaInsightsPipelineConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.MediaPipelineKinesisVideoStreamPoolReference",
    jsii_struct_bases=[],
    name_mapping={
        "media_pipeline_kinesis_video_stream_pool_arn": "mediaPipelineKinesisVideoStreamPoolArn",
    },
)
class MediaPipelineKinesisVideoStreamPoolReference:
    def __init__(
        self,
        *,
        media_pipeline_kinesis_video_stream_pool_arn: builtins.str,
    ) -> None:
        '''A reference to a MediaPipelineKinesisVideoStreamPool resource.

        :param media_pipeline_kinesis_video_stream_pool_arn: The Arn of the MediaPipelineKinesisVideoStreamPool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            media_pipeline_kinesis_video_stream_pool_reference = interfaces_chime.MediaPipelineKinesisVideoStreamPoolReference(
                media_pipeline_kinesis_video_stream_pool_arn="mediaPipelineKinesisVideoStreamPoolArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__954ac99ba1cbdd1ee071749b2194f42c51081f2c67b5af0ff7a790cd55875130)
            check_type(argname="argument media_pipeline_kinesis_video_stream_pool_arn", value=media_pipeline_kinesis_video_stream_pool_arn, expected_type=type_hints["media_pipeline_kinesis_video_stream_pool_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "media_pipeline_kinesis_video_stream_pool_arn": media_pipeline_kinesis_video_stream_pool_arn,
        }

    @builtins.property
    def media_pipeline_kinesis_video_stream_pool_arn(self) -> builtins.str:
        '''The Arn of the MediaPipelineKinesisVideoStreamPool resource.'''
        result = self._values.get("media_pipeline_kinesis_video_stream_pool_arn")
        assert result is not None, "Required property 'media_pipeline_kinesis_video_stream_pool_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MediaPipelineKinesisVideoStreamPoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.SipMediaApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"sip_media_application_arn": "sipMediaApplicationArn"},
)
class SipMediaApplicationReference:
    def __init__(self, *, sip_media_application_arn: builtins.str) -> None:
        '''A reference to a SipMediaApplication resource.

        :param sip_media_application_arn: The SipMediaApplicationArn of the SipMediaApplication resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            sip_media_application_reference = interfaces_chime.SipMediaApplicationReference(
                sip_media_application_arn="sipMediaApplicationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5319cba8825319c2b284fc1a03a9c5d3505d6227dc30a8e6b7f61565d19f5fdb)
            check_type(argname="argument sip_media_application_arn", value=sip_media_application_arn, expected_type=type_hints["sip_media_application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sip_media_application_arn": sip_media_application_arn,
        }

    @builtins.property
    def sip_media_application_arn(self) -> builtins.str:
        '''The SipMediaApplicationArn of the SipMediaApplication resource.'''
        result = self._values.get("sip_media_application_arn")
        assert result is not None, "Required property 'sip_media_application_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SipMediaApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chime.VoiceConnectorReference",
    jsii_struct_bases=[],
    name_mapping={"voice_connector_arn": "voiceConnectorArn"},
)
class VoiceConnectorReference:
    def __init__(self, *, voice_connector_arn: builtins.str) -> None:
        '''A reference to a VoiceConnector resource.

        :param voice_connector_arn: The VoiceConnectorArn of the VoiceConnector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chime as interfaces_chime
            
            voice_connector_reference = interfaces_chime.VoiceConnectorReference(
                voice_connector_arn="voiceConnectorArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9ad20049d61b130884b2e9047ed6d7e47e4cb96091426ad0da129c6f3a4d188a)
            check_type(argname="argument voice_connector_arn", value=voice_connector_arn, expected_type=type_hints["voice_connector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "voice_connector_arn": voice_connector_arn,
        }

    @builtins.property
    def voice_connector_arn(self) -> builtins.str:
        '''The VoiceConnectorArn of the VoiceConnector resource.'''
        result = self._values.get("voice_connector_arn")
        assert result is not None, "Required property 'voice_connector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VoiceConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppInstanceBotReference",
    "AppInstanceReference",
    "AppInstanceUserReference",
    "ChannelFlowReference",
    "ChannelReference",
    "IAppInstanceBotRef",
    "IAppInstanceRef",
    "IAppInstanceUserRef",
    "IChannelFlowRef",
    "IChannelRef",
    "IMediaInsightsPipelineConfigurationRef",
    "IMediaPipelineKinesisVideoStreamPoolRef",
    "ISipMediaApplicationRef",
    "IVoiceConnectorRef",
    "MediaInsightsPipelineConfigurationReference",
    "MediaPipelineKinesisVideoStreamPoolReference",
    "SipMediaApplicationReference",
    "VoiceConnectorReference",
]

publication.publish()

def _typecheckingstub__d94314e184ef238bc15359652813db5a17decbc7880453c10eebfdb5aee1574b(
    *,
    app_instance_bot_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7a63f08f74043f81dd278aff7af9a1fbed0722dd9d181168266b0223b7dd9a(
    *,
    app_instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a21d6b54c1a60d27402b1eed938ae67bfee72c94f33036fdd030210620f2b08(
    *,
    app_instance_user_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61d260a072d1387d8809a2f6808a63d6814fb8a1f1a8f87644726b5cbb1a26a5(
    *,
    channel_flow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a1c6965f18718c33c9cfd586a74d7dae12c1e318133befd47bae0d55b55365(
    *,
    channel_arn: builtins.str,
    chime_bearer: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2497cdb7fb79a6744dfcaf40a220bd30b2631ecab2f45c481f65ff50e686ff(
    *,
    media_insights_pipeline_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__954ac99ba1cbdd1ee071749b2194f42c51081f2c67b5af0ff7a790cd55875130(
    *,
    media_pipeline_kinesis_video_stream_pool_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5319cba8825319c2b284fc1a03a9c5d3505d6227dc30a8e6b7f61565d19f5fdb(
    *,
    sip_media_application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ad20049d61b130884b2e9047ed6d7e47e4cb96091426ad0da129c6f3a4d188a(
    *,
    voice_connector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAppInstanceBotRef, IAppInstanceRef, IAppInstanceUserRef, IChannelFlowRef, IChannelRef, IMediaInsightsPipelineConfigurationRef, IMediaPipelineKinesisVideoStreamPoolRef, ISipMediaApplicationRef, IVoiceConnectorRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
