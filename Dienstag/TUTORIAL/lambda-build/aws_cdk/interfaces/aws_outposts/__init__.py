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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_outposts.IOutpostRef")
class IOutpostRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Outpost.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="outpostRef")
    def outpost_ref(self) -> "OutpostReference":
        '''(experimental) A reference to a Outpost resource.

        :stability: experimental
        '''
        ...


class _IOutpostRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Outpost.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_outposts.IOutpostRef"

    @builtins.property
    @jsii.member(jsii_name="outpostRef")
    def outpost_ref(self) -> "OutpostReference":
        '''(experimental) A reference to a Outpost resource.

        :stability: experimental
        '''
        return typing.cast("OutpostReference", jsii.get(self, "outpostRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOutpostRef).__jsii_proxy_class__ = lambda : _IOutpostRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_outposts.ISiteRef")
class ISiteRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Site.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="siteRef")
    def site_ref(self) -> "SiteReference":
        '''(experimental) A reference to a Site resource.

        :stability: experimental
        '''
        ...


class _ISiteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Site.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_outposts.ISiteRef"

    @builtins.property
    @jsii.member(jsii_name="siteRef")
    def site_ref(self) -> "SiteReference":
        '''(experimental) A reference to a Site resource.

        :stability: experimental
        '''
        return typing.cast("SiteReference", jsii.get(self, "siteRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISiteRef).__jsii_proxy_class__ = lambda : _ISiteRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_outposts.OutpostReference",
    jsii_struct_bases=[],
    name_mapping={"outpost_arn": "outpostArn"},
)
class OutpostReference:
    def __init__(self, *, outpost_arn: builtins.str) -> None:
        '''A reference to a Outpost resource.

        :param outpost_arn: The OutpostArn of the Outpost resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_outposts as interfaces_outposts
            
            outpost_reference = interfaces_outposts.OutpostReference(
                outpost_arn="outpostArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e7eb9cbe6b3908fad11ca687c5277bdfea4ca1e9710d3359cad5fac76926b489)
            check_type(argname="argument outpost_arn", value=outpost_arn, expected_type=type_hints["outpost_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "outpost_arn": outpost_arn,
        }

    @builtins.property
    def outpost_arn(self) -> builtins.str:
        '''The OutpostArn of the Outpost resource.'''
        result = self._values.get("outpost_arn")
        assert result is not None, "Required property 'outpost_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OutpostReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_outposts.SiteReference",
    jsii_struct_bases=[],
    name_mapping={"site_arn": "siteArn"},
)
class SiteReference:
    def __init__(self, *, site_arn: builtins.str) -> None:
        '''A reference to a Site resource.

        :param site_arn: The SiteArn of the Site resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_outposts as interfaces_outposts
            
            site_reference = interfaces_outposts.SiteReference(
                site_arn="siteArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fcdf8f5987592f29cdcf77aa6f0b8fe3290f530e8b9efd5aa786994f7f7ffbbc)
            check_type(argname="argument site_arn", value=site_arn, expected_type=type_hints["site_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "site_arn": site_arn,
        }

    @builtins.property
    def site_arn(self) -> builtins.str:
        '''The SiteArn of the Site resource.'''
        result = self._values.get("site_arn")
        assert result is not None, "Required property 'site_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IOutpostRef",
    "ISiteRef",
    "OutpostReference",
    "SiteReference",
]

publication.publish()

def _typecheckingstub__e7eb9cbe6b3908fad11ca687c5277bdfea4ca1e9710d3359cad5fac76926b489(
    *,
    outpost_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcdf8f5987592f29cdcf77aa6f0b8fe3290f530e8b9efd5aa786994f7f7ffbbc(
    *,
    site_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IOutpostRef, ISiteRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
