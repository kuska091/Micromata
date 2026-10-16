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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pi.IPerfReportsRef")
class IPerfReportsRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PerfReports.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="perfReportsRef")
    def perf_reports_ref(self) -> "PerfReportsReference":
        '''(experimental) A reference to a PerfReports resource.

        :stability: experimental
        '''
        ...


class _IPerfReportsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PerfReports.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pi.IPerfReportsRef"

    @builtins.property
    @jsii.member(jsii_name="perfReportsRef")
    def perf_reports_ref(self) -> "PerfReportsReference":
        '''(experimental) A reference to a PerfReports resource.

        :stability: experimental
        '''
        return typing.cast("PerfReportsReference", jsii.get(self, "perfReportsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPerfReportsRef).__jsii_proxy_class__ = lambda : _IPerfReportsRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pi.PerfReportsReference",
    jsii_struct_bases=[],
    name_mapping={"perf_reports_arn": "perfReportsArn"},
)
class PerfReportsReference:
    def __init__(self, *, perf_reports_arn: builtins.str) -> None:
        '''A reference to a PerfReports resource.

        :param perf_reports_arn: The Arn of the PerfReports resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pi as interfaces_pi
            
            perf_reports_reference = interfaces_pi.PerfReportsReference(
                perf_reports_arn="perfReportsArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__aa929717f765a3f90b10e9e5f132bccc5df05171cd479e5fb9a8ff2ce5172109)
            check_type(argname="argument perf_reports_arn", value=perf_reports_arn, expected_type=type_hints["perf_reports_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "perf_reports_arn": perf_reports_arn,
        }

    @builtins.property
    def perf_reports_arn(self) -> builtins.str:
        '''The Arn of the PerfReports resource.'''
        result = self._values.get("perf_reports_arn")
        assert result is not None, "Required property 'perf_reports_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PerfReportsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IPerfReportsRef",
    "PerfReportsReference",
]

publication.publish()

def _typecheckingstub__aa929717f765a3f90b10e9e5f132bccc5df05171cd479e5fb9a8ff2ce5172109(
    *,
    perf_reports_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IPerfReportsRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
