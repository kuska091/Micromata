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
    jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.CisScanConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"cis_scan_configuration_arn": "cisScanConfigurationArn"},
)
class CisScanConfigurationReference:
    def __init__(self, *, cis_scan_configuration_arn: builtins.str) -> None:
        '''A reference to a CisScanConfiguration resource.

        :param cis_scan_configuration_arn: The Arn of the CisScanConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_inspectorv2 as interfaces_inspectorv2
            
            cis_scan_configuration_reference = interfaces_inspectorv2.CisScanConfigurationReference(
                cis_scan_configuration_arn="cisScanConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e8c6ca42b2cb2f22c6a3f6574ad741867e080c104c02ebe2f65f4e8fd0554455)
            check_type(argname="argument cis_scan_configuration_arn", value=cis_scan_configuration_arn, expected_type=type_hints["cis_scan_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cis_scan_configuration_arn": cis_scan_configuration_arn,
        }

    @builtins.property
    def cis_scan_configuration_arn(self) -> builtins.str:
        '''The Arn of the CisScanConfiguration resource.'''
        result = self._values.get("cis_scan_configuration_arn")
        assert result is not None, "Required property 'cis_scan_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CisScanConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.CodeSecurityIntegrationReference",
    jsii_struct_bases=[],
    name_mapping={"code_security_integration_arn": "codeSecurityIntegrationArn"},
)
class CodeSecurityIntegrationReference:
    def __init__(self, *, code_security_integration_arn: builtins.str) -> None:
        '''A reference to a CodeSecurityIntegration resource.

        :param code_security_integration_arn: The Arn of the CodeSecurityIntegration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_inspectorv2 as interfaces_inspectorv2
            
            code_security_integration_reference = interfaces_inspectorv2.CodeSecurityIntegrationReference(
                code_security_integration_arn="codeSecurityIntegrationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__da77a51776e223751633183c4b62dde16af89862fbe1d362bff26ed70b7e43ad)
            check_type(argname="argument code_security_integration_arn", value=code_security_integration_arn, expected_type=type_hints["code_security_integration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code_security_integration_arn": code_security_integration_arn,
        }

    @builtins.property
    def code_security_integration_arn(self) -> builtins.str:
        '''The Arn of the CodeSecurityIntegration resource.'''
        result = self._values.get("code_security_integration_arn")
        assert result is not None, "Required property 'code_security_integration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeSecurityIntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.CodeSecurityScanConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "code_security_scan_configuration_arn": "codeSecurityScanConfigurationArn",
    },
)
class CodeSecurityScanConfigurationReference:
    def __init__(self, *, code_security_scan_configuration_arn: builtins.str) -> None:
        '''A reference to a CodeSecurityScanConfiguration resource.

        :param code_security_scan_configuration_arn: The Arn of the CodeSecurityScanConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_inspectorv2 as interfaces_inspectorv2
            
            code_security_scan_configuration_reference = interfaces_inspectorv2.CodeSecurityScanConfigurationReference(
                code_security_scan_configuration_arn="codeSecurityScanConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cfc5c5ab99b9158cd9f76bb7e3f86c7cdbddb797d7acdefb4ca433dfdc4e3546)
            check_type(argname="argument code_security_scan_configuration_arn", value=code_security_scan_configuration_arn, expected_type=type_hints["code_security_scan_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code_security_scan_configuration_arn": code_security_scan_configuration_arn,
        }

    @builtins.property
    def code_security_scan_configuration_arn(self) -> builtins.str:
        '''The Arn of the CodeSecurityScanConfiguration resource.'''
        result = self._values.get("code_security_scan_configuration_arn")
        assert result is not None, "Required property 'code_security_scan_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeSecurityScanConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.ConnectorReference",
    jsii_struct_bases=[],
    name_mapping={"connector_arn": "connectorArn"},
)
class ConnectorReference:
    def __init__(self, *, connector_arn: builtins.str) -> None:
        '''A reference to a Connector resource.

        :param connector_arn: The ConnectorArn of the Connector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_inspectorv2 as interfaces_inspectorv2
            
            connector_reference = interfaces_inspectorv2.ConnectorReference(
                connector_arn="connectorArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__cd5aac99b8cfd06040bf0e708607534bee7e62733c1f55d21fe1804213a4a24c)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The ConnectorArn of the Connector resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.FilterReference",
    jsii_struct_bases=[],
    name_mapping={"filter_arn": "filterArn"},
)
class FilterReference:
    def __init__(self, *, filter_arn: builtins.str) -> None:
        '''A reference to a Filter resource.

        :param filter_arn: The Arn of the Filter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_inspectorv2 as interfaces_inspectorv2
            
            filter_reference = interfaces_inspectorv2.FilterReference(
                filter_arn="filterArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3e730087b3717be91203803efc70ad6680e99acc083efab494cd35190a0553d9)
            check_type(argname="argument filter_arn", value=filter_arn, expected_type=type_hints["filter_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_arn": filter_arn,
        }

    @builtins.property
    def filter_arn(self) -> builtins.str:
        '''The Arn of the Filter resource.'''
        result = self._values.get("filter_arn")
        assert result is not None, "Required property 'filter_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.ICisScanConfigurationRef"
)
class ICisScanConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CisScanConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cisScanConfigurationRef")
    def cis_scan_configuration_ref(self) -> "CisScanConfigurationReference":
        '''(experimental) A reference to a CisScanConfiguration resource.

        :stability: experimental
        '''
        ...


class _ICisScanConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CisScanConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_inspectorv2.ICisScanConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="cisScanConfigurationRef")
    def cis_scan_configuration_ref(self) -> "CisScanConfigurationReference":
        '''(experimental) A reference to a CisScanConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("CisScanConfigurationReference", jsii.get(self, "cisScanConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICisScanConfigurationRef).__jsii_proxy_class__ = lambda : _ICisScanConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.ICodeSecurityIntegrationRef"
)
class ICodeSecurityIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CodeSecurityIntegration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="codeSecurityIntegrationRef")
    def code_security_integration_ref(self) -> "CodeSecurityIntegrationReference":
        '''(experimental) A reference to a CodeSecurityIntegration resource.

        :stability: experimental
        '''
        ...


class _ICodeSecurityIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CodeSecurityIntegration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_inspectorv2.ICodeSecurityIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="codeSecurityIntegrationRef")
    def code_security_integration_ref(self) -> "CodeSecurityIntegrationReference":
        '''(experimental) A reference to a CodeSecurityIntegration resource.

        :stability: experimental
        '''
        return typing.cast("CodeSecurityIntegrationReference", jsii.get(self, "codeSecurityIntegrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICodeSecurityIntegrationRef).__jsii_proxy_class__ = lambda : _ICodeSecurityIntegrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.ICodeSecurityScanConfigurationRef"
)
class ICodeSecurityScanConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CodeSecurityScanConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="codeSecurityScanConfigurationRef")
    def code_security_scan_configuration_ref(
        self,
    ) -> "CodeSecurityScanConfigurationReference":
        '''(experimental) A reference to a CodeSecurityScanConfiguration resource.

        :stability: experimental
        '''
        ...


class _ICodeSecurityScanConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CodeSecurityScanConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_inspectorv2.ICodeSecurityScanConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="codeSecurityScanConfigurationRef")
    def code_security_scan_configuration_ref(
        self,
    ) -> "CodeSecurityScanConfigurationReference":
        '''(experimental) A reference to a CodeSecurityScanConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("CodeSecurityScanConfigurationReference", jsii.get(self, "codeSecurityScanConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICodeSecurityScanConfigurationRef).__jsii_proxy_class__ = lambda : _ICodeSecurityScanConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.IConnectorRef")
class IConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        ...


class _IConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_inspectorv2.IConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorReference", jsii.get(self, "connectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorRef).__jsii_proxy_class__ = lambda : _IConnectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_inspectorv2.IFilterRef")
class IFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Filter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="filterRef")
    def filter_ref(self) -> "FilterReference":
        '''(experimental) A reference to a Filter resource.

        :stability: experimental
        '''
        ...


class _IFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Filter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_inspectorv2.IFilterRef"

    @builtins.property
    @jsii.member(jsii_name="filterRef")
    def filter_ref(self) -> "FilterReference":
        '''(experimental) A reference to a Filter resource.

        :stability: experimental
        '''
        return typing.cast("FilterReference", jsii.get(self, "filterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFilterRef).__jsii_proxy_class__ = lambda : _IFilterRefProxy


__all__ = [
    "CisScanConfigurationReference",
    "CodeSecurityIntegrationReference",
    "CodeSecurityScanConfigurationReference",
    "ConnectorReference",
    "FilterReference",
    "ICisScanConfigurationRef",
    "ICodeSecurityIntegrationRef",
    "ICodeSecurityScanConfigurationRef",
    "IConnectorRef",
    "IFilterRef",
]

publication.publish()

def _typecheckingstub__e8c6ca42b2cb2f22c6a3f6574ad741867e080c104c02ebe2f65f4e8fd0554455(
    *,
    cis_scan_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da77a51776e223751633183c4b62dde16af89862fbe1d362bff26ed70b7e43ad(
    *,
    code_security_integration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc5c5ab99b9158cd9f76bb7e3f86c7cdbddb797d7acdefb4ca433dfdc4e3546(
    *,
    code_security_scan_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5aac99b8cfd06040bf0e708607534bee7e62733c1f55d21fe1804213a4a24c(
    *,
    connector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e730087b3717be91203803efc70ad6680e99acc083efab494cd35190a0553d9(
    *,
    filter_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICisScanConfigurationRef, ICodeSecurityIntegrationRef, ICodeSecurityScanConfigurationRef, IConnectorRef, IFilterRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
