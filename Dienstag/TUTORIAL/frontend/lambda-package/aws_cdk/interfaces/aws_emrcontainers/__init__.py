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
    jsii_type="aws-cdk-lib.interfaces.aws_emrcontainers.EndpointReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_arn": "endpointArn"},
)
class EndpointReference:
    def __init__(self, *, endpoint_arn: builtins.str) -> None:
        '''A reference to a Endpoint resource.

        :param endpoint_arn: The Arn of the Endpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emrcontainers as interfaces_emrcontainers
            
            endpoint_reference = interfaces_emrcontainers.EndpointReference(
                endpoint_arn="endpointArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f8da93a42d3292300c35c7d5863b4ecdfabf6c6a48563cb245a43a0393149b50)
            check_type(argname="argument endpoint_arn", value=endpoint_arn, expected_type=type_hints["endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_arn": endpoint_arn,
        }

    @builtins.property
    def endpoint_arn(self) -> builtins.str:
        '''The Arn of the Endpoint resource.'''
        result = self._values.get("endpoint_arn")
        assert result is not None, "Required property 'endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emrcontainers.IEndpointRef")
class IEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        ...


class _IEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emrcontainers.IEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        return typing.cast("EndpointReference", jsii.get(self, "endpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointRef).__jsii_proxy_class__ = lambda : _IEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emrcontainers.IJobTemplateRef")
class IJobTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a JobTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="jobTemplateRef")
    def job_template_ref(self) -> "JobTemplateReference":
        '''(experimental) A reference to a JobTemplate resource.

        :stability: experimental
        '''
        ...


class _IJobTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a JobTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emrcontainers.IJobTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="jobTemplateRef")
    def job_template_ref(self) -> "JobTemplateReference":
        '''(experimental) A reference to a JobTemplate resource.

        :stability: experimental
        '''
        return typing.cast("JobTemplateReference", jsii.get(self, "jobTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJobTemplateRef).__jsii_proxy_class__ = lambda : _IJobTemplateRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_emrcontainers.ISecurityConfigurationRef"
)
class ISecurityConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "SecurityConfigurationReference":
        '''(experimental) A reference to a SecurityConfiguration resource.

        :stability: experimental
        '''
        ...


class _ISecurityConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emrcontainers.ISecurityConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "SecurityConfigurationReference":
        '''(experimental) A reference to a SecurityConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SecurityConfigurationReference", jsii.get(self, "securityConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityConfigurationRef).__jsii_proxy_class__ = lambda : _ISecurityConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_emrcontainers.IVirtualClusterRef"
)
class IVirtualClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="virtualClusterRef")
    def virtual_cluster_ref(self) -> "VirtualClusterReference":
        '''(experimental) A reference to a VirtualCluster resource.

        :stability: experimental
        '''
        ...


class _IVirtualClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emrcontainers.IVirtualClusterRef"

    @builtins.property
    @jsii.member(jsii_name="virtualClusterRef")
    def virtual_cluster_ref(self) -> "VirtualClusterReference":
        '''(experimental) A reference to a VirtualCluster resource.

        :stability: experimental
        '''
        return typing.cast("VirtualClusterReference", jsii.get(self, "virtualClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualClusterRef).__jsii_proxy_class__ = lambda : _IVirtualClusterRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emrcontainers.JobTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"job_template_arn": "jobTemplateArn"},
)
class JobTemplateReference:
    def __init__(self, *, job_template_arn: builtins.str) -> None:
        '''A reference to a JobTemplate resource.

        :param job_template_arn: The Arn of the JobTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emrcontainers as interfaces_emrcontainers
            
            job_template_reference = interfaces_emrcontainers.JobTemplateReference(
                job_template_arn="jobTemplateArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d3f40689935d4c9d4e53e4aa74e18fb39b8e36ff78362c43824b5e715cb5c516)
            check_type(argname="argument job_template_arn", value=job_template_arn, expected_type=type_hints["job_template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_template_arn": job_template_arn,
        }

    @builtins.property
    def job_template_arn(self) -> builtins.str:
        '''The Arn of the JobTemplate resource.'''
        result = self._values.get("job_template_arn")
        assert result is not None, "Required property 'job_template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emrcontainers.SecurityConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"security_configuration_arn": "securityConfigurationArn"},
)
class SecurityConfigurationReference:
    def __init__(self, *, security_configuration_arn: builtins.str) -> None:
        '''A reference to a SecurityConfiguration resource.

        :param security_configuration_arn: The Arn of the SecurityConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emrcontainers as interfaces_emrcontainers
            
            security_configuration_reference = interfaces_emrcontainers.SecurityConfigurationReference(
                security_configuration_arn="securityConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3409f33831901e890d42039217fd628ed197766106a278a1e5eaf0508873cf0f)
            check_type(argname="argument security_configuration_arn", value=security_configuration_arn, expected_type=type_hints["security_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_configuration_arn": security_configuration_arn,
        }

    @builtins.property
    def security_configuration_arn(self) -> builtins.str:
        '''The Arn of the SecurityConfiguration resource.'''
        result = self._values.get("security_configuration_arn")
        assert result is not None, "Required property 'security_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emrcontainers.VirtualClusterReference",
    jsii_struct_bases=[],
    name_mapping={
        "virtual_cluster_arn": "virtualClusterArn",
        "virtual_cluster_id": "virtualClusterId",
    },
)
class VirtualClusterReference:
    def __init__(
        self,
        *,
        virtual_cluster_arn: builtins.str,
        virtual_cluster_id: builtins.str,
    ) -> None:
        '''A reference to a VirtualCluster resource.

        :param virtual_cluster_arn: The ARN of the VirtualCluster resource.
        :param virtual_cluster_id: The Id of the VirtualCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emrcontainers as interfaces_emrcontainers
            
            virtual_cluster_reference = interfaces_emrcontainers.VirtualClusterReference(
                virtual_cluster_arn="virtualClusterArn",
                virtual_cluster_id="virtualClusterId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b279f868e31527e514f6d252f42aa76ae779c333792720eb24ad65b2884b2923)
            check_type(argname="argument virtual_cluster_arn", value=virtual_cluster_arn, expected_type=type_hints["virtual_cluster_arn"])
            check_type(argname="argument virtual_cluster_id", value=virtual_cluster_id, expected_type=type_hints["virtual_cluster_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_cluster_arn": virtual_cluster_arn,
            "virtual_cluster_id": virtual_cluster_id,
        }

    @builtins.property
    def virtual_cluster_arn(self) -> builtins.str:
        '''The ARN of the VirtualCluster resource.'''
        result = self._values.get("virtual_cluster_arn")
        assert result is not None, "Required property 'virtual_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_cluster_id(self) -> builtins.str:
        '''The Id of the VirtualCluster resource.'''
        result = self._values.get("virtual_cluster_id")
        assert result is not None, "Required property 'virtual_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EndpointReference",
    "IEndpointRef",
    "IJobTemplateRef",
    "ISecurityConfigurationRef",
    "IVirtualClusterRef",
    "JobTemplateReference",
    "SecurityConfigurationReference",
    "VirtualClusterReference",
]

publication.publish()

def _typecheckingstub__f8da93a42d3292300c35c7d5863b4ecdfabf6c6a48563cb245a43a0393149b50(
    *,
    endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3f40689935d4c9d4e53e4aa74e18fb39b8e36ff78362c43824b5e715cb5c516(
    *,
    job_template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3409f33831901e890d42039217fd628ed197766106a278a1e5eaf0508873cf0f(
    *,
    security_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b279f868e31527e514f6d252f42aa76ae779c333792720eb24ad65b2884b2923(
    *,
    virtual_cluster_arn: builtins.str,
    virtual_cluster_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEndpointRef, IJobTemplateRef, ISecurityConfigurationRef, IVirtualClusterRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
