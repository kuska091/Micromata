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
    jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.GrantReference",
    jsii_struct_bases=[],
    name_mapping={"grant_arn": "grantArn"},
)
class GrantReference:
    def __init__(self, *, grant_arn: builtins.str) -> None:
        '''A reference to a Grant resource.

        :param grant_arn: The GrantArn of the Grant resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_licensemanager as interfaces_licensemanager
            
            grant_reference = interfaces_licensemanager.GrantReference(
                grant_arn="grantArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__509345cf0b8df3531dd2233cb8ca72a49893c49948d88feade0b6e134b33772d)
            check_type(argname="argument grant_arn", value=grant_arn, expected_type=type_hints["grant_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "grant_arn": grant_arn,
        }

    @builtins.property
    def grant_arn(self) -> builtins.str:
        '''The GrantArn of the Grant resource.'''
        result = self._values.get("grant_arn")
        assert result is not None, "Required property 'grant_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.IGrantRef")
class IGrantRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Grant.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="grantRef")
    def grant_ref(self) -> "GrantReference":
        '''(experimental) A reference to a Grant resource.

        :stability: experimental
        '''
        ...


class _IGrantRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Grant.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_licensemanager.IGrantRef"

    @builtins.property
    @jsii.member(jsii_name="grantRef")
    def grant_ref(self) -> "GrantReference":
        '''(experimental) A reference to a Grant resource.

        :stability: experimental
        '''
        return typing.cast("GrantReference", jsii.get(self, "grantRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGrantRef).__jsii_proxy_class__ = lambda : _IGrantRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.ILicenseAssetGroupRef"
)
class ILicenseAssetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LicenseAssetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="licenseAssetGroupRef")
    def license_asset_group_ref(self) -> "LicenseAssetGroupReference":
        '''(experimental) A reference to a LicenseAssetGroup resource.

        :stability: experimental
        '''
        ...


class _ILicenseAssetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LicenseAssetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_licensemanager.ILicenseAssetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="licenseAssetGroupRef")
    def license_asset_group_ref(self) -> "LicenseAssetGroupReference":
        '''(experimental) A reference to a LicenseAssetGroup resource.

        :stability: experimental
        '''
        return typing.cast("LicenseAssetGroupReference", jsii.get(self, "licenseAssetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILicenseAssetGroupRef).__jsii_proxy_class__ = lambda : _ILicenseAssetGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.ILicenseAssetRuleSetRef"
)
class ILicenseAssetRuleSetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LicenseAssetRuleSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="licenseAssetRuleSetRef")
    def license_asset_rule_set_ref(self) -> "LicenseAssetRuleSetReference":
        '''(experimental) A reference to a LicenseAssetRuleSet resource.

        :stability: experimental
        '''
        ...


class _ILicenseAssetRuleSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LicenseAssetRuleSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_licensemanager.ILicenseAssetRuleSetRef"

    @builtins.property
    @jsii.member(jsii_name="licenseAssetRuleSetRef")
    def license_asset_rule_set_ref(self) -> "LicenseAssetRuleSetReference":
        '''(experimental) A reference to a LicenseAssetRuleSet resource.

        :stability: experimental
        '''
        return typing.cast("LicenseAssetRuleSetReference", jsii.get(self, "licenseAssetRuleSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILicenseAssetRuleSetRef).__jsii_proxy_class__ = lambda : _ILicenseAssetRuleSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.ILicenseRef")
class ILicenseRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a License.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="licenseRef")
    def license_ref(self) -> "LicenseReference":
        '''(experimental) A reference to a License resource.

        :stability: experimental
        '''
        ...


class _ILicenseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a License.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_licensemanager.ILicenseRef"

    @builtins.property
    @jsii.member(jsii_name="licenseRef")
    def license_ref(self) -> "LicenseReference":
        '''(experimental) A reference to a License resource.

        :stability: experimental
        '''
        return typing.cast("LicenseReference", jsii.get(self, "licenseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILicenseRef).__jsii_proxy_class__ = lambda : _ILicenseRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.LicenseAssetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"license_asset_group_arn": "licenseAssetGroupArn"},
)
class LicenseAssetGroupReference:
    def __init__(self, *, license_asset_group_arn: builtins.str) -> None:
        '''A reference to a LicenseAssetGroup resource.

        :param license_asset_group_arn: The LicenseAssetGroupArn of the LicenseAssetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_licensemanager as interfaces_licensemanager
            
            license_asset_group_reference = interfaces_licensemanager.LicenseAssetGroupReference(
                license_asset_group_arn="licenseAssetGroupArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__59780563bdf44abd42df591c81293dccf84129019e4a6ae293cee0344c060ffd)
            check_type(argname="argument license_asset_group_arn", value=license_asset_group_arn, expected_type=type_hints["license_asset_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "license_asset_group_arn": license_asset_group_arn,
        }

    @builtins.property
    def license_asset_group_arn(self) -> builtins.str:
        '''The LicenseAssetGroupArn of the LicenseAssetGroup resource.'''
        result = self._values.get("license_asset_group_arn")
        assert result is not None, "Required property 'license_asset_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LicenseAssetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.LicenseAssetRuleSetReference",
    jsii_struct_bases=[],
    name_mapping={"license_asset_ruleset_arn": "licenseAssetRulesetArn"},
)
class LicenseAssetRuleSetReference:
    def __init__(self, *, license_asset_ruleset_arn: builtins.str) -> None:
        '''A reference to a LicenseAssetRuleSet resource.

        :param license_asset_ruleset_arn: The LicenseAssetRulesetArn of the LicenseAssetRuleSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_licensemanager as interfaces_licensemanager
            
            license_asset_rule_set_reference = interfaces_licensemanager.LicenseAssetRuleSetReference(
                license_asset_ruleset_arn="licenseAssetRulesetArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__db24271a3c7b0124bc790d44c59879c5714dc1da35ad778acfa7f85886b06e2d)
            check_type(argname="argument license_asset_ruleset_arn", value=license_asset_ruleset_arn, expected_type=type_hints["license_asset_ruleset_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "license_asset_ruleset_arn": license_asset_ruleset_arn,
        }

    @builtins.property
    def license_asset_ruleset_arn(self) -> builtins.str:
        '''The LicenseAssetRulesetArn of the LicenseAssetRuleSet resource.'''
        result = self._values.get("license_asset_ruleset_arn")
        assert result is not None, "Required property 'license_asset_ruleset_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LicenseAssetRuleSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.LicenseReference",
    jsii_struct_bases=[],
    name_mapping={"license_arn": "licenseArn"},
)
class LicenseReference:
    def __init__(self, *, license_arn: builtins.str) -> None:
        '''A reference to a License resource.

        :param license_arn: The LicenseArn of the License resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_licensemanager as interfaces_licensemanager
            
            license_reference = interfaces_licensemanager.LicenseReference(
                license_arn="licenseArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0ce44a0b5c8ac0b1ac5b4c7e7e57091674992170e45de59a47767d1279342850)
            check_type(argname="argument license_arn", value=license_arn, expected_type=type_hints["license_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "license_arn": license_arn,
        }

    @builtins.property
    def license_arn(self) -> builtins.str:
        '''The LicenseArn of the License resource.'''
        result = self._values.get("license_arn")
        assert result is not None, "Required property 'license_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LicenseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GrantReference",
    "IGrantRef",
    "ILicenseAssetGroupRef",
    "ILicenseAssetRuleSetRef",
    "ILicenseRef",
    "LicenseAssetGroupReference",
    "LicenseAssetRuleSetReference",
    "LicenseReference",
]

publication.publish()

def _typecheckingstub__509345cf0b8df3531dd2233cb8ca72a49893c49948d88feade0b6e134b33772d(
    *,
    grant_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59780563bdf44abd42df591c81293dccf84129019e4a6ae293cee0344c060ffd(
    *,
    license_asset_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db24271a3c7b0124bc790d44c59879c5714dc1da35ad778acfa7f85886b06e2d(
    *,
    license_asset_ruleset_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ce44a0b5c8ac0b1ac5b4c7e7e57091674992170e45de59a47767d1279342850(
    *,
    license_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGrantRef, ILicenseAssetGroupRef, ILicenseAssetRuleSetRef, ILicenseRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
