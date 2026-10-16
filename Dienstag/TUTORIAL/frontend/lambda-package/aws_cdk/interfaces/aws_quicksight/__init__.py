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
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ActionConnectorReference",
    jsii_struct_bases=[],
    name_mapping={
        "action_connector_arn": "actionConnectorArn",
        "action_connector_id": "actionConnectorId",
        "aws_account_id": "awsAccountId",
    },
)
class ActionConnectorReference:
    def __init__(
        self,
        *,
        action_connector_arn: builtins.str,
        action_connector_id: builtins.str,
        aws_account_id: builtins.str,
    ) -> None:
        '''A reference to a ActionConnector resource.

        :param action_connector_arn: The ARN of the ActionConnector resource.
        :param action_connector_id: The ActionConnectorId of the ActionConnector resource.
        :param aws_account_id: The AwsAccountId of the ActionConnector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            action_connector_reference = interfaces_quicksight.ActionConnectorReference(
                action_connector_arn="actionConnectorArn",
                action_connector_id="actionConnectorId",
                aws_account_id="awsAccountId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__31055bc274e952c4fc3166d11f0fbbc107ed08b00575ccf7d73fa07a9e5f9f9f)
            check_type(argname="argument action_connector_arn", value=action_connector_arn, expected_type=type_hints["action_connector_arn"])
            check_type(argname="argument action_connector_id", value=action_connector_id, expected_type=type_hints["action_connector_id"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_connector_arn": action_connector_arn,
            "action_connector_id": action_connector_id,
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def action_connector_arn(self) -> builtins.str:
        '''The ARN of the ActionConnector resource.'''
        result = self._values.get("action_connector_arn")
        assert result is not None, "Required property 'action_connector_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_connector_id(self) -> builtins.str:
        '''The ActionConnectorId of the ActionConnector resource.'''
        result = self._values.get("action_connector_id")
        assert result is not None, "Required property 'action_connector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the ActionConnector resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.AgentReference",
    jsii_struct_bases=[],
    name_mapping={
        "agent_arn": "agentArn",
        "agent_id": "agentId",
        "aws_account_id": "awsAccountId",
    },
)
class AgentReference:
    def __init__(
        self,
        *,
        agent_arn: builtins.str,
        agent_id: builtins.str,
        aws_account_id: builtins.str,
    ) -> None:
        '''A reference to a Agent resource.

        :param agent_arn: The ARN of the Agent resource.
        :param agent_id: The AgentId of the Agent resource.
        :param aws_account_id: The AwsAccountId of the Agent resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            agent_reference = interfaces_quicksight.AgentReference(
                agent_arn="agentArn",
                agent_id="agentId",
                aws_account_id="awsAccountId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2c7989ae50557fc5538eafdbe0d391cb4802a256e6d4c33f2143c1bbab8b3e24)
            check_type(argname="argument agent_arn", value=agent_arn, expected_type=type_hints["agent_arn"])
            check_type(argname="argument agent_id", value=agent_id, expected_type=type_hints["agent_id"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arn": agent_arn,
            "agent_id": agent_id,
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def agent_arn(self) -> builtins.str:
        '''The ARN of the Agent resource.'''
        result = self._values.get("agent_arn")
        assert result is not None, "Required property 'agent_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_id(self) -> builtins.str:
        '''The AgentId of the Agent resource.'''
        result = self._values.get("agent_id")
        assert result is not None, "Required property 'agent_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Agent resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.AnalysisReference",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_arn": "analysisArn",
        "analysis_id": "analysisId",
        "aws_account_id": "awsAccountId",
    },
)
class AnalysisReference:
    def __init__(
        self,
        *,
        analysis_arn: builtins.str,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
    ) -> None:
        '''A reference to a Analysis resource.

        :param analysis_arn: The ARN of the Analysis resource.
        :param analysis_id: The AnalysisId of the Analysis resource.
        :param aws_account_id: The AwsAccountId of the Analysis resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            analysis_reference = interfaces_quicksight.AnalysisReference(
                analysis_arn="analysisArn",
                analysis_id="analysisId",
                aws_account_id="awsAccountId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__79dd570d6da6d3fe7b5ab82dcad552abbb17b11f076a26256bed0f162c545988)
            check_type(argname="argument analysis_arn", value=analysis_arn, expected_type=type_hints["analysis_arn"])
            check_type(argname="argument analysis_id", value=analysis_id, expected_type=type_hints["analysis_id"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "analysis_arn": analysis_arn,
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def analysis_arn(self) -> builtins.str:
        '''The ARN of the Analysis resource.'''
        result = self._values.get("analysis_arn")
        assert result is not None, "Required property 'analysis_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The AnalysisId of the Analysis resource.'''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Analysis resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalysisReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ApprovalPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_arn": "policyArn", "policy_id": "policyId"},
)
class ApprovalPolicyReference:
    def __init__(self, *, policy_arn: builtins.str, policy_id: builtins.str) -> None:
        '''A reference to a ApprovalPolicy resource.

        :param policy_arn: The ARN of the ApprovalPolicy resource.
        :param policy_id: The PolicyId of the ApprovalPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            approval_policy_reference = interfaces_quicksight.ApprovalPolicyReference(
                policy_arn="policyArn",
                policy_id="policyId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8878a7f31995e6d02338f2326e2f0bb99ed5c1a6419c6f06a22e3313710dd0dc)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
            "policy_id": policy_id,
        }

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''The ARN of the ApprovalPolicy resource.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_id(self) -> builtins.str:
        '''The PolicyId of the ApprovalPolicy resource.'''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprovalPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.CustomPermissionsReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "custom_permissions_arn": "customPermissionsArn",
        "custom_permissions_name": "customPermissionsName",
    },
)
class CustomPermissionsReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        custom_permissions_arn: builtins.str,
        custom_permissions_name: builtins.str,
    ) -> None:
        '''A reference to a CustomPermissions resource.

        :param aws_account_id: The AwsAccountId of the CustomPermissions resource.
        :param custom_permissions_arn: The ARN of the CustomPermissions resource.
        :param custom_permissions_name: The CustomPermissionsName of the CustomPermissions resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            custom_permissions_reference = interfaces_quicksight.CustomPermissionsReference(
                aws_account_id="awsAccountId",
                custom_permissions_arn="customPermissionsArn",
                custom_permissions_name="customPermissionsName"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bcbb01a6ae4003c466f2c9facde86b4a9228b2947e8db14b07e90c8828b892fc)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument custom_permissions_arn", value=custom_permissions_arn, expected_type=type_hints["custom_permissions_arn"])
            check_type(argname="argument custom_permissions_name", value=custom_permissions_name, expected_type=type_hints["custom_permissions_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "custom_permissions_arn": custom_permissions_arn,
            "custom_permissions_name": custom_permissions_name,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the CustomPermissions resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_permissions_arn(self) -> builtins.str:
        '''The ARN of the CustomPermissions resource.'''
        result = self._values.get("custom_permissions_arn")
        assert result is not None, "Required property 'custom_permissions_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_permissions_name(self) -> builtins.str:
        '''The CustomPermissionsName of the CustomPermissions resource.'''
        result = self._values.get("custom_permissions_name")
        assert result is not None, "Required property 'custom_permissions_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomPermissionsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.CustomizationReference",
    jsii_struct_bases=[],
    name_mapping={"customization_arn": "customizationArn"},
)
class CustomizationReference:
    def __init__(self, *, customization_arn: builtins.str) -> None:
        '''A reference to a Customization resource.

        :param customization_arn: The Arn of the Customization resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            customization_reference = interfaces_quicksight.CustomizationReference(
                customization_arn="customizationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c257248476b0173740cab6e66d5bbcf2c1ca87301d2164a8c23210eb9699e667)
            check_type(argname="argument customization_arn", value=customization_arn, expected_type=type_hints["customization_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "customization_arn": customization_arn,
        }

    @builtins.property
    def customization_arn(self) -> builtins.str:
        '''The Arn of the Customization resource.'''
        result = self._values.get("customization_arn")
        assert result is not None, "Required property 'customization_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomizationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.DLPSettingReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dlp_setting_arn": "dlpSettingArn",
        "dlp_setting_id": "dlpSettingId",
    },
)
class DLPSettingReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dlp_setting_arn: builtins.str,
        dlp_setting_id: builtins.str,
    ) -> None:
        '''A reference to a DLPSetting resource.

        :param aws_account_id: The AwsAccountId of the DLPSetting resource.
        :param dlp_setting_arn: The ARN of the DLPSetting resource.
        :param dlp_setting_id: The DlpSettingId of the DLPSetting resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            d_lp_setting_reference = interfaces_quicksight.DLPSettingReference(
                aws_account_id="awsAccountId",
                dlp_setting_arn="dlpSettingArn",
                dlp_setting_id="dlpSettingId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ddc0996ef050bdea6f249d0e582110ceff50188ab0a8e1b7d6fbf603c5ebcb98)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument dlp_setting_arn", value=dlp_setting_arn, expected_type=type_hints["dlp_setting_arn"])
            check_type(argname="argument dlp_setting_id", value=dlp_setting_id, expected_type=type_hints["dlp_setting_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dlp_setting_arn": dlp_setting_arn,
            "dlp_setting_id": dlp_setting_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the DLPSetting resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dlp_setting_arn(self) -> builtins.str:
        '''The ARN of the DLPSetting resource.'''
        result = self._values.get("dlp_setting_arn")
        assert result is not None, "Required property 'dlp_setting_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dlp_setting_id(self) -> builtins.str:
        '''The DlpSettingId of the DLPSetting resource.'''
        result = self._values.get("dlp_setting_id")
        assert result is not None, "Required property 'dlp_setting_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DLPSettingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.DashboardReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_arn": "dashboardArn",
        "dashboard_id": "dashboardId",
    },
)
class DashboardReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_arn: builtins.str,
        dashboard_id: builtins.str,
    ) -> None:
        '''A reference to a Dashboard resource.

        :param aws_account_id: The AwsAccountId of the Dashboard resource.
        :param dashboard_arn: The ARN of the Dashboard resource.
        :param dashboard_id: The DashboardId of the Dashboard resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            dashboard_reference = interfaces_quicksight.DashboardReference(
                aws_account_id="awsAccountId",
                dashboard_arn="dashboardArn",
                dashboard_id="dashboardId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6e1998cd35473accee4a1dd066f5d4e4af29b9cdfdf78293c732f43e8ae1071f)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument dashboard_arn", value=dashboard_arn, expected_type=type_hints["dashboard_arn"])
            check_type(argname="argument dashboard_id", value=dashboard_id, expected_type=type_hints["dashboard_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_arn": dashboard_arn,
            "dashboard_id": dashboard_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Dashboard resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_arn(self) -> builtins.str:
        '''The ARN of the Dashboard resource.'''
        result = self._values.get("dashboard_arn")
        assert result is not None, "Required property 'dashboard_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The DashboardId of the Dashboard resource.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.DataSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_arn": "dataSetArn",
        "data_set_id": "dataSetId",
    },
)
class DataSetReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_arn: builtins.str,
        data_set_id: builtins.str,
    ) -> None:
        '''A reference to a DataSet resource.

        :param aws_account_id: The AwsAccountId of the DataSet resource.
        :param data_set_arn: The ARN of the DataSet resource.
        :param data_set_id: The DataSetId of the DataSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            data_set_reference = interfaces_quicksight.DataSetReference(
                aws_account_id="awsAccountId",
                data_set_arn="dataSetArn",
                data_set_id="dataSetId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__39696e8afe9ffe21ed7b01deb7349ba2563b8d2cdae5e74d20ee2a0e637d3f7f)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument data_set_arn", value=data_set_arn, expected_type=type_hints["data_set_arn"])
            check_type(argname="argument data_set_id", value=data_set_id, expected_type=type_hints["data_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_arn": data_set_arn,
            "data_set_id": data_set_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the DataSet resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_arn(self) -> builtins.str:
        '''The ARN of the DataSet resource.'''
        result = self._values.get("data_set_arn")
        assert result is not None, "Required property 'data_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The DataSetId of the DataSet resource.'''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_source_arn": "dataSourceArn",
        "data_source_id": "dataSourceId",
    },
)
class DataSourceReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_source_arn: builtins.str,
        data_source_id: builtins.str,
    ) -> None:
        '''A reference to a DataSource resource.

        :param aws_account_id: The AwsAccountId of the DataSource resource.
        :param data_source_arn: The ARN of the DataSource resource.
        :param data_source_id: The DataSourceId of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            data_source_reference = interfaces_quicksight.DataSourceReference(
                aws_account_id="awsAccountId",
                data_source_arn="dataSourceArn",
                data_source_id="dataSourceId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__70b8fb657688960b4dae12c4a8f205b2a58737c1dd982d8e201b45cf5cb10c90)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument data_source_arn", value=data_source_arn, expected_type=type_hints["data_source_arn"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_source_arn": data_source_arn,
            "data_source_id": data_source_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the DataSource resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The ARN of the DataSource resource.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The DataSourceId of the DataSource resource.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.FlowReference",
    jsii_struct_bases=[],
    name_mapping={"flow_arn": "flowArn"},
)
class FlowReference:
    def __init__(self, *, flow_arn: builtins.str) -> None:
        '''A reference to a Flow resource.

        :param flow_arn: The Arn of the Flow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            flow_reference = interfaces_quicksight.FlowReference(
                flow_arn="flowArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__470eb9fd2b4da5c9e387310ce01fafebaef9834aa0f831affc5f726fd1583c13)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The Arn of the Flow resource.'''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.FolderReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "folder_arn": "folderArn",
        "folder_id": "folderId",
    },
)
class FolderReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        folder_arn: builtins.str,
        folder_id: builtins.str,
    ) -> None:
        '''A reference to a Folder resource.

        :param aws_account_id: The AwsAccountId of the Folder resource.
        :param folder_arn: The ARN of the Folder resource.
        :param folder_id: The FolderId of the Folder resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            folder_reference = interfaces_quicksight.FolderReference(
                aws_account_id="awsAccountId",
                folder_arn="folderArn",
                folder_id="folderId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__68d11833d18be618b7ec87af3be2a77728a162bc466dd4aaa5584c1b4c7d4012)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument folder_arn", value=folder_arn, expected_type=type_hints["folder_arn"])
            check_type(argname="argument folder_id", value=folder_id, expected_type=type_hints["folder_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "folder_arn": folder_arn,
            "folder_id": folder_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Folder resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def folder_arn(self) -> builtins.str:
        '''The ARN of the Folder resource.'''
        result = self._values.get("folder_arn")
        assert result is not None, "Required property 'folder_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def folder_id(self) -> builtins.str:
        '''The FolderId of the Folder resource.'''
        result = self._values.get("folder_id")
        assert result is not None, "Required property 'folder_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FolderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IActionConnectorRef")
class IActionConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ActionConnector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="actionConnectorRef")
    def action_connector_ref(self) -> "ActionConnectorReference":
        '''(experimental) A reference to a ActionConnector resource.

        :stability: experimental
        '''
        ...


class _IActionConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ActionConnector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IActionConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="actionConnectorRef")
    def action_connector_ref(self) -> "ActionConnectorReference":
        '''(experimental) A reference to a ActionConnector resource.

        :stability: experimental
        '''
        return typing.cast("ActionConnectorReference", jsii.get(self, "actionConnectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IActionConnectorRef).__jsii_proxy_class__ = lambda : _IActionConnectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IAgentRef")
class IAgentRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Agent.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentRef")
    def agent_ref(self) -> "AgentReference":
        '''(experimental) A reference to a Agent resource.

        :stability: experimental
        '''
        ...


class _IAgentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Agent.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IAgentRef"

    @builtins.property
    @jsii.member(jsii_name="agentRef")
    def agent_ref(self) -> "AgentReference":
        '''(experimental) A reference to a Agent resource.

        :stability: experimental
        '''
        return typing.cast("AgentReference", jsii.get(self, "agentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentRef).__jsii_proxy_class__ = lambda : _IAgentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IAnalysisRef")
class IAnalysisRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Analysis.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="analysisRef")
    def analysis_ref(self) -> "AnalysisReference":
        '''(experimental) A reference to a Analysis resource.

        :stability: experimental
        '''
        ...


class _IAnalysisRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Analysis.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IAnalysisRef"

    @builtins.property
    @jsii.member(jsii_name="analysisRef")
    def analysis_ref(self) -> "AnalysisReference":
        '''(experimental) A reference to a Analysis resource.

        :stability: experimental
        '''
        return typing.cast("AnalysisReference", jsii.get(self, "analysisRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnalysisRef).__jsii_proxy_class__ = lambda : _IAnalysisRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IApprovalPolicyRef")
class IApprovalPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApprovalPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="approvalPolicyRef")
    def approval_policy_ref(self) -> "ApprovalPolicyReference":
        '''(experimental) A reference to a ApprovalPolicy resource.

        :stability: experimental
        '''
        ...


class _IApprovalPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApprovalPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IApprovalPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="approvalPolicyRef")
    def approval_policy_ref(self) -> "ApprovalPolicyReference":
        '''(experimental) A reference to a ApprovalPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ApprovalPolicyReference", jsii.get(self, "approvalPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApprovalPolicyRef).__jsii_proxy_class__ = lambda : _IApprovalPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ICustomPermissionsRef"
)
class ICustomPermissionsRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomPermissions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customPermissionsRef")
    def custom_permissions_ref(self) -> "CustomPermissionsReference":
        '''(experimental) A reference to a CustomPermissions resource.

        :stability: experimental
        '''
        ...


class _ICustomPermissionsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomPermissions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ICustomPermissionsRef"

    @builtins.property
    @jsii.member(jsii_name="customPermissionsRef")
    def custom_permissions_ref(self) -> "CustomPermissionsReference":
        '''(experimental) A reference to a CustomPermissions resource.

        :stability: experimental
        '''
        return typing.cast("CustomPermissionsReference", jsii.get(self, "customPermissionsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomPermissionsRef).__jsii_proxy_class__ = lambda : _ICustomPermissionsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ICustomizationRef")
class ICustomizationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Customization.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customizationRef")
    def customization_ref(self) -> "CustomizationReference":
        '''(experimental) A reference to a Customization resource.

        :stability: experimental
        '''
        ...


class _ICustomizationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Customization.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ICustomizationRef"

    @builtins.property
    @jsii.member(jsii_name="customizationRef")
    def customization_ref(self) -> "CustomizationReference":
        '''(experimental) A reference to a Customization resource.

        :stability: experimental
        '''
        return typing.cast("CustomizationReference", jsii.get(self, "customizationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomizationRef).__jsii_proxy_class__ = lambda : _ICustomizationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IDLPSettingRef")
class IDLPSettingRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DLPSetting.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dlpSettingRef")
    def dlp_setting_ref(self) -> "DLPSettingReference":
        '''(experimental) A reference to a DLPSetting resource.

        :stability: experimental
        '''
        ...


class _IDLPSettingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DLPSetting.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IDLPSettingRef"

    @builtins.property
    @jsii.member(jsii_name="dlpSettingRef")
    def dlp_setting_ref(self) -> "DLPSettingReference":
        '''(experimental) A reference to a DLPSetting resource.

        :stability: experimental
        '''
        return typing.cast("DLPSettingReference", jsii.get(self, "dlpSettingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDLPSettingRef).__jsii_proxy_class__ = lambda : _IDLPSettingRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IDashboardRef")
class IDashboardRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Dashboard.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        ...


class _IDashboardRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Dashboard.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IDashboardRef"

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        return typing.cast("DashboardReference", jsii.get(self, "dashboardRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDashboardRef).__jsii_proxy_class__ = lambda : _IDashboardRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IDataSetRef")
class IDataSetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSetRef")
    def data_set_ref(self) -> "DataSetReference":
        '''(experimental) A reference to a DataSet resource.

        :stability: experimental
        '''
        ...


class _IDataSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IDataSetRef"

    @builtins.property
    @jsii.member(jsii_name="dataSetRef")
    def data_set_ref(self) -> "DataSetReference":
        '''(experimental) A reference to a DataSet resource.

        :stability: experimental
        '''
        return typing.cast("DataSetReference", jsii.get(self, "dataSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSetRef).__jsii_proxy_class__ = lambda : _IDataSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IFlowRef")
class IFlowRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Flow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowRef")
    def flow_ref(self) -> "FlowReference":
        '''(experimental) A reference to a Flow resource.

        :stability: experimental
        '''
        ...


class _IFlowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Flow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IFlowRef"

    @builtins.property
    @jsii.member(jsii_name="flowRef")
    def flow_ref(self) -> "FlowReference":
        '''(experimental) A reference to a Flow resource.

        :stability: experimental
        '''
        return typing.cast("FlowReference", jsii.get(self, "flowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowRef).__jsii_proxy_class__ = lambda : _IFlowRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IFolderRef")
class IFolderRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Folder.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="folderRef")
    def folder_ref(self) -> "FolderReference":
        '''(experimental) A reference to a Folder resource.

        :stability: experimental
        '''
        ...


class _IFolderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Folder.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IFolderRef"

    @builtins.property
    @jsii.member(jsii_name="folderRef")
    def folder_ref(self) -> "FolderReference":
        '''(experimental) A reference to a Folder resource.

        :stability: experimental
        '''
        return typing.cast("FolderReference", jsii.get(self, "folderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFolderRef).__jsii_proxy_class__ = lambda : _IFolderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IKnowledgeBaseRef")
class IKnowledgeBaseRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a KnowledgeBase.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="knowledgeBaseRef")
    def knowledge_base_ref(self) -> "KnowledgeBaseReference":
        '''(experimental) A reference to a KnowledgeBase resource.

        :stability: experimental
        '''
        ...


class _IKnowledgeBaseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a KnowledgeBase.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IKnowledgeBaseRef"

    @builtins.property
    @jsii.member(jsii_name="knowledgeBaseRef")
    def knowledge_base_ref(self) -> "KnowledgeBaseReference":
        '''(experimental) A reference to a KnowledgeBase resource.

        :stability: experimental
        '''
        return typing.cast("KnowledgeBaseReference", jsii.get(self, "knowledgeBaseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKnowledgeBaseRef).__jsii_proxy_class__ = lambda : _IKnowledgeBaseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ILimitsProfileRef")
class ILimitsProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LimitsProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="limitsProfileRef")
    def limits_profile_ref(self) -> "LimitsProfileReference":
        '''(experimental) A reference to a LimitsProfile resource.

        :stability: experimental
        '''
        ...


class _ILimitsProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LimitsProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ILimitsProfileRef"

    @builtins.property
    @jsii.member(jsii_name="limitsProfileRef")
    def limits_profile_ref(self) -> "LimitsProfileReference":
        '''(experimental) A reference to a LimitsProfile resource.

        :stability: experimental
        '''
        return typing.cast("LimitsProfileReference", jsii.get(self, "limitsProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILimitsProfileRef).__jsii_proxy_class__ = lambda : _ILimitsProfileRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IOAuthClientApplicationRef"
)
class IOAuthClientApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OAuthClientApplication.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="oAuthClientApplicationRef")
    def o_auth_client_application_ref(self) -> "OAuthClientApplicationReference":
        '''(experimental) A reference to a OAuthClientApplication resource.

        :stability: experimental
        '''
        ...


class _IOAuthClientApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OAuthClientApplication.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IOAuthClientApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="oAuthClientApplicationRef")
    def o_auth_client_application_ref(self) -> "OAuthClientApplicationReference":
        '''(experimental) A reference to a OAuthClientApplication resource.

        :stability: experimental
        '''
        return typing.cast("OAuthClientApplicationReference", jsii.get(self, "oAuthClientApplicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOAuthClientApplicationRef).__jsii_proxy_class__ = lambda : _IOAuthClientApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IRefreshScheduleRef")
class IRefreshScheduleRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RefreshSchedule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="refreshScheduleRef")
    def refresh_schedule_ref(self) -> "RefreshScheduleReference":
        '''(experimental) A reference to a RefreshSchedule resource.

        :stability: experimental
        '''
        ...


class _IRefreshScheduleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RefreshSchedule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IRefreshScheduleRef"

    @builtins.property
    @jsii.member(jsii_name="refreshScheduleRef")
    def refresh_schedule_ref(self) -> "RefreshScheduleReference":
        '''(experimental) A reference to a RefreshSchedule resource.

        :stability: experimental
        '''
        return typing.cast("RefreshScheduleReference", jsii.get(self, "refreshScheduleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRefreshScheduleRef).__jsii_proxy_class__ = lambda : _IRefreshScheduleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ISpaceRef")
class ISpaceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Space.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="spaceRef")
    def space_ref(self) -> "SpaceReference":
        '''(experimental) A reference to a Space resource.

        :stability: experimental
        '''
        ...


class _ISpaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Space.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ISpaceRef"

    @builtins.property
    @jsii.member(jsii_name="spaceRef")
    def space_ref(self) -> "SpaceReference":
        '''(experimental) A reference to a Space resource.

        :stability: experimental
        '''
        return typing.cast("SpaceReference", jsii.get(self, "spaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISpaceRef).__jsii_proxy_class__ = lambda : _ISpaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ITemplateRef")
class ITemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Template.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "TemplateReference":
        '''(experimental) A reference to a Template resource.

        :stability: experimental
        '''
        ...


class _ITemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Template.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ITemplateRef"

    @builtins.property
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "TemplateReference":
        '''(experimental) A reference to a Template resource.

        :stability: experimental
        '''
        return typing.cast("TemplateReference", jsii.get(self, "templateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITemplateRef).__jsii_proxy_class__ = lambda : _ITemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IThemeRef")
class IThemeRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Theme.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="themeRef")
    def theme_ref(self) -> "ThemeReference":
        '''(experimental) A reference to a Theme resource.

        :stability: experimental
        '''
        ...


class _IThemeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Theme.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IThemeRef"

    @builtins.property
    @jsii.member(jsii_name="themeRef")
    def theme_ref(self) -> "ThemeReference":
        '''(experimental) A reference to a Theme resource.

        :stability: experimental
        '''
        return typing.cast("ThemeReference", jsii.get(self, "themeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThemeRef).__jsii_proxy_class__ = lambda : _IThemeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ITopicRef")
class ITopicRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Topic.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicRef")
    def topic_ref(self) -> "TopicReference":
        '''(experimental) A reference to a Topic resource.

        :stability: experimental
        '''
        ...


class _ITopicRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Topic.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ITopicRef"

    @builtins.property
    @jsii.member(jsii_name="topicRef")
    def topic_ref(self) -> "TopicReference":
        '''(experimental) A reference to a Topic resource.

        :stability: experimental
        '''
        return typing.cast("TopicReference", jsii.get(self, "topicRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicRef).__jsii_proxy_class__ = lambda : _ITopicRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ITopicV2Ref")
class ITopicV2Ref(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TopicV2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicV2Ref")
    def topic_v2_ref(self) -> "TopicV2Reference":
        '''(experimental) A reference to a TopicV2 resource.

        :stability: experimental
        '''
        ...


class _ITopicV2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TopicV2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ITopicV2Ref"

    @builtins.property
    @jsii.member(jsii_name="topicV2Ref")
    def topic_v2_ref(self) -> "TopicV2Reference":
        '''(experimental) A reference to a TopicV2 resource.

        :stability: experimental
        '''
        return typing.cast("TopicV2Reference", jsii.get(self, "topicV2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicV2Ref).__jsii_proxy_class__ = lambda : _ITopicV2RefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IVPCConnectionRef")
class IVPCConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionRef")
    def vpc_connection_ref(self) -> "VPCConnectionReference":
        '''(experimental) A reference to a VPCConnection resource.

        :stability: experimental
        '''
        ...


class _IVPCConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IVPCConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionRef")
    def vpc_connection_ref(self) -> "VPCConnectionReference":
        '''(experimental) A reference to a VPCConnection resource.

        :stability: experimental
        '''
        return typing.cast("VPCConnectionReference", jsii.get(self, "vpcConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCConnectionRef).__jsii_proxy_class__ = lambda : _IVPCConnectionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.KnowledgeBaseReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "knowledge_base_arn": "knowledgeBaseArn",
        "knowledge_base_id": "knowledgeBaseId",
    },
)
class KnowledgeBaseReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        knowledge_base_arn: builtins.str,
        knowledge_base_id: builtins.str,
    ) -> None:
        '''A reference to a KnowledgeBase resource.

        :param aws_account_id: The AwsAccountId of the KnowledgeBase resource.
        :param knowledge_base_arn: The ARN of the KnowledgeBase resource.
        :param knowledge_base_id: The KnowledgeBaseId of the KnowledgeBase resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            knowledge_base_reference = interfaces_quicksight.KnowledgeBaseReference(
                aws_account_id="awsAccountId",
                knowledge_base_arn="knowledgeBaseArn",
                knowledge_base_id="knowledgeBaseId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__07a0f8327fdaffd076e0cc9273c2f7696c8754a0777dfaf05186eecba824c3b3)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument knowledge_base_arn", value=knowledge_base_arn, expected_type=type_hints["knowledge_base_arn"])
            check_type(argname="argument knowledge_base_id", value=knowledge_base_id, expected_type=type_hints["knowledge_base_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "knowledge_base_arn": knowledge_base_arn,
            "knowledge_base_id": knowledge_base_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the KnowledgeBase resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def knowledge_base_arn(self) -> builtins.str:
        '''The ARN of the KnowledgeBase resource.'''
        result = self._values.get("knowledge_base_arn")
        assert result is not None, "Required property 'knowledge_base_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def knowledge_base_id(self) -> builtins.str:
        '''The KnowledgeBaseId of the KnowledgeBase resource.'''
        result = self._values.get("knowledge_base_id")
        assert result is not None, "Required property 'knowledge_base_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KnowledgeBaseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.LimitsProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "limits_profile_arn": "limitsProfileArn",
        "profile_id": "profileId",
    },
)
class LimitsProfileReference:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        limits_profile_arn: builtins.str,
        profile_id: builtins.str,
    ) -> None:
        '''A reference to a LimitsProfile resource.

        :param account_id: The AccountId of the LimitsProfile resource.
        :param limits_profile_arn: The ARN of the LimitsProfile resource.
        :param profile_id: The ProfileId of the LimitsProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            limits_profile_reference = interfaces_quicksight.LimitsProfileReference(
                account_id="accountId",
                limits_profile_arn="limitsProfileArn",
                profile_id="profileId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8eac14628a5885e08f823d34eaa64e07b8f15f154a5128cf72ca80163f431df9)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument limits_profile_arn", value=limits_profile_arn, expected_type=type_hints["limits_profile_arn"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "limits_profile_arn": limits_profile_arn,
            "profile_id": profile_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the LimitsProfile resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def limits_profile_arn(self) -> builtins.str:
        '''The ARN of the LimitsProfile resource.'''
        result = self._values.get("limits_profile_arn")
        assert result is not None, "Required property 'limits_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''The ProfileId of the LimitsProfile resource.'''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LimitsProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.OAuthClientApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"o_auth_client_application_arn": "oAuthClientApplicationArn"},
)
class OAuthClientApplicationReference:
    def __init__(self, *, o_auth_client_application_arn: builtins.str) -> None:
        '''A reference to a OAuthClientApplication resource.

        :param o_auth_client_application_arn: The Arn of the OAuthClientApplication resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            o_auth_client_application_reference = interfaces_quicksight.OAuthClientApplicationReference(
                o_auth_client_application_arn="oAuthClientApplicationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__1da0f0dbb95217952fac925b01457b1c48d3db3d3961d62ab097ab0defadb3a3)
            check_type(argname="argument o_auth_client_application_arn", value=o_auth_client_application_arn, expected_type=type_hints["o_auth_client_application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "o_auth_client_application_arn": o_auth_client_application_arn,
        }

    @builtins.property
    def o_auth_client_application_arn(self) -> builtins.str:
        '''The Arn of the OAuthClientApplication resource.'''
        result = self._values.get("o_auth_client_application_arn")
        assert result is not None, "Required property 'o_auth_client_application_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OAuthClientApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.RefreshScheduleReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "refresh_schedule_arn": "refreshScheduleArn",
        "schedule_id": "scheduleId",
    },
)
class RefreshScheduleReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        refresh_schedule_arn: builtins.str,
        schedule_id: builtins.str,
    ) -> None:
        '''A reference to a RefreshSchedule resource.

        :param aws_account_id: The AwsAccountId of the RefreshSchedule resource.
        :param data_set_id: The DataSetId of the RefreshSchedule resource.
        :param refresh_schedule_arn: The ARN of the RefreshSchedule resource.
        :param schedule_id: The Schedule/ScheduleId of the RefreshSchedule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            refresh_schedule_reference = interfaces_quicksight.RefreshScheduleReference(
                aws_account_id="awsAccountId",
                data_set_id="dataSetId",
                refresh_schedule_arn="refreshScheduleArn",
                schedule_id="scheduleId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8723d097fe811477bf46d6e8328f08cbc18d550832e45dfd85d0a290a2e9c9ea)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument data_set_id", value=data_set_id, expected_type=type_hints["data_set_id"])
            check_type(argname="argument refresh_schedule_arn", value=refresh_schedule_arn, expected_type=type_hints["refresh_schedule_arn"])
            check_type(argname="argument schedule_id", value=schedule_id, expected_type=type_hints["schedule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
            "refresh_schedule_arn": refresh_schedule_arn,
            "schedule_id": schedule_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the RefreshSchedule resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The DataSetId of the RefreshSchedule resource.'''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def refresh_schedule_arn(self) -> builtins.str:
        '''The ARN of the RefreshSchedule resource.'''
        result = self._values.get("refresh_schedule_arn")
        assert result is not None, "Required property 'refresh_schedule_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_id(self) -> builtins.str:
        '''The Schedule/ScheduleId of the RefreshSchedule resource.'''
        result = self._values.get("schedule_id")
        assert result is not None, "Required property 'schedule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RefreshScheduleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.SpaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "space_arn": "spaceArn",
        "space_id": "spaceId",
    },
)
class SpaceReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        space_arn: builtins.str,
        space_id: builtins.str,
    ) -> None:
        '''A reference to a Space resource.

        :param aws_account_id: The AwsAccountId of the Space resource.
        :param space_arn: The ARN of the Space resource.
        :param space_id: The SpaceId of the Space resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            space_reference = interfaces_quicksight.SpaceReference(
                aws_account_id="awsAccountId",
                space_arn="spaceArn",
                space_id="spaceId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__70f0e10ebaa10a2ba10c7da7f214b875b35636c85f9db3760e0154a44f74a710)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument space_arn", value=space_arn, expected_type=type_hints["space_arn"])
            check_type(argname="argument space_id", value=space_id, expected_type=type_hints["space_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "space_arn": space_arn,
            "space_id": space_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Space resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def space_arn(self) -> builtins.str:
        '''The ARN of the Space resource.'''
        result = self._values.get("space_arn")
        assert result is not None, "Required property 'space_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def space_id(self) -> builtins.str:
        '''The SpaceId of the Space resource.'''
        result = self._values.get("space_id")
        assert result is not None, "Required property 'space_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.TemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_arn": "templateArn",
        "template_id": "templateId",
    },
)
class TemplateReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_arn: builtins.str,
        template_id: builtins.str,
    ) -> None:
        '''A reference to a Template resource.

        :param aws_account_id: The AwsAccountId of the Template resource.
        :param template_arn: The ARN of the Template resource.
        :param template_id: The TemplateId of the Template resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            template_reference = interfaces_quicksight.TemplateReference(
                aws_account_id="awsAccountId",
                template_arn="templateArn",
                template_id="templateId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__c5bef292799a30d68c18b479c9372960c83ce75f740acf6872746b1c68a4f4be)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
            check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_arn": template_arn,
            "template_id": template_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Template resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_arn(self) -> builtins.str:
        '''The ARN of the Template resource.'''
        result = self._values.get("template_arn")
        assert result is not None, "Required property 'template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The TemplateId of the Template resource.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ThemeReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_arn": "themeArn",
        "theme_id": "themeId",
    },
)
class ThemeReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_arn: builtins.str,
        theme_id: builtins.str,
    ) -> None:
        '''A reference to a Theme resource.

        :param aws_account_id: The AwsAccountId of the Theme resource.
        :param theme_arn: The ARN of the Theme resource.
        :param theme_id: The ThemeId of the Theme resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            theme_reference = interfaces_quicksight.ThemeReference(
                aws_account_id="awsAccountId",
                theme_arn="themeArn",
                theme_id="themeId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__145097322a7b346d435b378f4f5398ed66d47436afe9e55c22372eab8a112c87)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument theme_arn", value=theme_arn, expected_type=type_hints["theme_arn"])
            check_type(argname="argument theme_id", value=theme_id, expected_type=type_hints["theme_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_arn": theme_arn,
            "theme_id": theme_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Theme resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_arn(self) -> builtins.str:
        '''The ARN of the Theme resource.'''
        result = self._values.get("theme_arn")
        assert result is not None, "Required property 'theme_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ThemeId of the Theme resource.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.TopicReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "topic_arn": "topicArn",
        "topic_id": "topicId",
    },
)
class TopicReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        topic_arn: builtins.str,
        topic_id: builtins.str,
    ) -> None:
        '''A reference to a Topic resource.

        :param aws_account_id: The AwsAccountId of the Topic resource.
        :param topic_arn: The ARN of the Topic resource.
        :param topic_id: The TopicId of the Topic resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            topic_reference = interfaces_quicksight.TopicReference(
                aws_account_id="awsAccountId",
                topic_arn="topicArn",
                topic_id="topicId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__644dc61611189aa4ef3678efd6b78c7718549c2efda0dd7842ca761132bca1a7)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            check_type(argname="argument topic_id", value=topic_id, expected_type=type_hints["topic_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "topic_arn": topic_arn,
            "topic_id": topic_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Topic resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''The ARN of the Topic resource.'''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_id(self) -> builtins.str:
        '''The TopicId of the Topic resource.'''
        result = self._values.get("topic_id")
        assert result is not None, "Required property 'topic_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.TopicV2Reference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "topic_id": "topicId",
        "topic_v2_arn": "topicV2Arn",
    },
)
class TopicV2Reference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        topic_id: builtins.str,
        topic_v2_arn: builtins.str,
    ) -> None:
        '''A reference to a TopicV2 resource.

        :param aws_account_id: The AwsAccountId of the TopicV2 resource.
        :param topic_id: The TopicId of the TopicV2 resource.
        :param topic_v2_arn: The ARN of the TopicV2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            topic_v2_reference = interfaces_quicksight.TopicV2Reference(
                aws_account_id="awsAccountId",
                topic_id="topicId",
                topic_v2_arn="topicV2Arn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f5fe054ceeed99a1709f63c16203c219ab1fdcba55a664f52c6a3bf246447d8d)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument topic_id", value=topic_id, expected_type=type_hints["topic_id"])
            check_type(argname="argument topic_v2_arn", value=topic_v2_arn, expected_type=type_hints["topic_v2_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "topic_id": topic_id,
            "topic_v2_arn": topic_v2_arn,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the TopicV2 resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_id(self) -> builtins.str:
        '''The TopicId of the TopicV2 resource.'''
        result = self._values.get("topic_id")
        assert result is not None, "Required property 'topic_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_v2_arn(self) -> builtins.str:
        '''The ARN of the TopicV2 resource.'''
        result = self._values.get("topic_v2_arn")
        assert result is not None, "Required property 'topic_v2_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicV2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.VPCConnectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "vpc_connection_arn": "vpcConnectionArn",
        "vpc_connection_id": "vpcConnectionId",
    },
)
class VPCConnectionReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        vpc_connection_arn: builtins.str,
        vpc_connection_id: builtins.str,
    ) -> None:
        '''A reference to a VPCConnection resource.

        :param aws_account_id: The AwsAccountId of the VPCConnection resource.
        :param vpc_connection_arn: The ARN of the VPCConnection resource.
        :param vpc_connection_id: The VPCConnectionId of the VPCConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            v_pc_connection_reference = interfaces_quicksight.VPCConnectionReference(
                aws_account_id="awsAccountId",
                vpc_connection_arn="vpcConnectionArn",
                vpc_connection_id="vpcConnectionId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8a94c806f9f5d8f329e5fe8025b2cd7112ef5f8d032fce0a9cf2e9f64bafb27b)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument vpc_connection_arn", value=vpc_connection_arn, expected_type=type_hints["vpc_connection_arn"])
            check_type(argname="argument vpc_connection_id", value=vpc_connection_id, expected_type=type_hints["vpc_connection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "vpc_connection_arn": vpc_connection_arn,
            "vpc_connection_id": vpc_connection_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the VPCConnection resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_connection_arn(self) -> builtins.str:
        '''The ARN of the VPCConnection resource.'''
        result = self._values.get("vpc_connection_arn")
        assert result is not None, "Required property 'vpc_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_connection_id(self) -> builtins.str:
        '''The VPCConnectionId of the VPCConnection resource.'''
        result = self._values.get("vpc_connection_id")
        assert result is not None, "Required property 'vpc_connection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ActionConnectorReference",
    "AgentReference",
    "AnalysisReference",
    "ApprovalPolicyReference",
    "CustomPermissionsReference",
    "CustomizationReference",
    "DLPSettingReference",
    "DashboardReference",
    "DataSetReference",
    "DataSourceReference",
    "FlowReference",
    "FolderReference",
    "IActionConnectorRef",
    "IAgentRef",
    "IAnalysisRef",
    "IApprovalPolicyRef",
    "ICustomPermissionsRef",
    "ICustomizationRef",
    "IDLPSettingRef",
    "IDashboardRef",
    "IDataSetRef",
    "IDataSourceRef",
    "IFlowRef",
    "IFolderRef",
    "IKnowledgeBaseRef",
    "ILimitsProfileRef",
    "IOAuthClientApplicationRef",
    "IRefreshScheduleRef",
    "ISpaceRef",
    "ITemplateRef",
    "IThemeRef",
    "ITopicRef",
    "ITopicV2Ref",
    "IVPCConnectionRef",
    "KnowledgeBaseReference",
    "LimitsProfileReference",
    "OAuthClientApplicationReference",
    "RefreshScheduleReference",
    "SpaceReference",
    "TemplateReference",
    "ThemeReference",
    "TopicReference",
    "TopicV2Reference",
    "VPCConnectionReference",
]

publication.publish()

def _typecheckingstub__31055bc274e952c4fc3166d11f0fbbc107ed08b00575ccf7d73fa07a9e5f9f9f(
    *,
    action_connector_arn: builtins.str,
    action_connector_id: builtins.str,
    aws_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7989ae50557fc5538eafdbe0d391cb4802a256e6d4c33f2143c1bbab8b3e24(
    *,
    agent_arn: builtins.str,
    agent_id: builtins.str,
    aws_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79dd570d6da6d3fe7b5ab82dcad552abbb17b11f076a26256bed0f162c545988(
    *,
    analysis_arn: builtins.str,
    analysis_id: builtins.str,
    aws_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8878a7f31995e6d02338f2326e2f0bb99ed5c1a6419c6f06a22e3313710dd0dc(
    *,
    policy_arn: builtins.str,
    policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcbb01a6ae4003c466f2c9facde86b4a9228b2947e8db14b07e90c8828b892fc(
    *,
    aws_account_id: builtins.str,
    custom_permissions_arn: builtins.str,
    custom_permissions_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c257248476b0173740cab6e66d5bbcf2c1ca87301d2164a8c23210eb9699e667(
    *,
    customization_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc0996ef050bdea6f249d0e582110ceff50188ab0a8e1b7d6fbf603c5ebcb98(
    *,
    aws_account_id: builtins.str,
    dlp_setting_arn: builtins.str,
    dlp_setting_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1998cd35473accee4a1dd066f5d4e4af29b9cdfdf78293c732f43e8ae1071f(
    *,
    aws_account_id: builtins.str,
    dashboard_arn: builtins.str,
    dashboard_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39696e8afe9ffe21ed7b01deb7349ba2563b8d2cdae5e74d20ee2a0e637d3f7f(
    *,
    aws_account_id: builtins.str,
    data_set_arn: builtins.str,
    data_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b8fb657688960b4dae12c4a8f205b2a58737c1dd982d8e201b45cf5cb10c90(
    *,
    aws_account_id: builtins.str,
    data_source_arn: builtins.str,
    data_source_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470eb9fd2b4da5c9e387310ce01fafebaef9834aa0f831affc5f726fd1583c13(
    *,
    flow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d11833d18be618b7ec87af3be2a77728a162bc466dd4aaa5584c1b4c7d4012(
    *,
    aws_account_id: builtins.str,
    folder_arn: builtins.str,
    folder_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a0f8327fdaffd076e0cc9273c2f7696c8754a0777dfaf05186eecba824c3b3(
    *,
    aws_account_id: builtins.str,
    knowledge_base_arn: builtins.str,
    knowledge_base_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eac14628a5885e08f823d34eaa64e07b8f15f154a5128cf72ca80163f431df9(
    *,
    account_id: builtins.str,
    limits_profile_arn: builtins.str,
    profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da0f0dbb95217952fac925b01457b1c48d3db3d3961d62ab097ab0defadb3a3(
    *,
    o_auth_client_application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8723d097fe811477bf46d6e8328f08cbc18d550832e45dfd85d0a290a2e9c9ea(
    *,
    aws_account_id: builtins.str,
    data_set_id: builtins.str,
    refresh_schedule_arn: builtins.str,
    schedule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f0e10ebaa10a2ba10c7da7f214b875b35636c85f9db3760e0154a44f74a710(
    *,
    aws_account_id: builtins.str,
    space_arn: builtins.str,
    space_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5bef292799a30d68c18b479c9372960c83ce75f740acf6872746b1c68a4f4be(
    *,
    aws_account_id: builtins.str,
    template_arn: builtins.str,
    template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145097322a7b346d435b378f4f5398ed66d47436afe9e55c22372eab8a112c87(
    *,
    aws_account_id: builtins.str,
    theme_arn: builtins.str,
    theme_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__644dc61611189aa4ef3678efd6b78c7718549c2efda0dd7842ca761132bca1a7(
    *,
    aws_account_id: builtins.str,
    topic_arn: builtins.str,
    topic_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5fe054ceeed99a1709f63c16203c219ab1fdcba55a664f52c6a3bf246447d8d(
    *,
    aws_account_id: builtins.str,
    topic_id: builtins.str,
    topic_v2_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a94c806f9f5d8f329e5fe8025b2cd7112ef5f8d032fce0a9cf2e9f64bafb27b(
    *,
    aws_account_id: builtins.str,
    vpc_connection_arn: builtins.str,
    vpc_connection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IActionConnectorRef, IAgentRef, IAnalysisRef, IApprovalPolicyRef, ICustomPermissionsRef, ICustomizationRef, IDLPSettingRef, IDashboardRef, IDataSetRef, IDataSourceRef, IFlowRef, IFolderRef, IKnowledgeBaseRef, ILimitsProfileRef, IOAuthClientApplicationRef, IRefreshScheduleRef, ISpaceRef, ITemplateRef, IThemeRef, ITopicRef, ITopicV2Ref, IVPCConnectionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
