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
    jsii_type="aws-cdk-lib.interfaces.aws_accessanalyzer.AnalyzerReference",
    jsii_struct_bases=[],
    name_mapping={"analyzer_arn": "analyzerArn"},
)
class AnalyzerReference:
    def __init__(self, *, analyzer_arn: builtins.str) -> None:
        '''A reference to a Analyzer resource.

        :param analyzer_arn: The Arn of the Analyzer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_accessanalyzer as interfaces_accessanalyzer
            
            analyzer_reference = interfaces_accessanalyzer.AnalyzerReference(
                analyzer_arn="analyzerArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d4d375974cd2ef13d3347c0db5ce73a696e350281dee5af93d3a748a4376541c)
            check_type(argname="argument analyzer_arn", value=analyzer_arn, expected_type=type_hints["analyzer_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "analyzer_arn": analyzer_arn,
        }

    @builtins.property
    def analyzer_arn(self) -> builtins.str:
        '''The Arn of the Analyzer resource.'''
        result = self._values.get("analyzer_arn")
        assert result is not None, "Required property 'analyzer_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalyzerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_accessanalyzer.ArchiveRuleReference",
    jsii_struct_bases=[],
    name_mapping={"archive_rule_arn": "archiveRuleArn"},
)
class ArchiveRuleReference:
    def __init__(self, *, archive_rule_arn: builtins.str) -> None:
        '''A reference to a ArchiveRule resource.

        :param archive_rule_arn: The Arn of the ArchiveRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_accessanalyzer as interfaces_accessanalyzer
            
            archive_rule_reference = interfaces_accessanalyzer.ArchiveRuleReference(
                archive_rule_arn="archiveRuleArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6242d39b99a5b626f657e476f23494a24574da5367d3d1f79f6f21c0cb36cfab)
            check_type(argname="argument archive_rule_arn", value=archive_rule_arn, expected_type=type_hints["archive_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "archive_rule_arn": archive_rule_arn,
        }

    @builtins.property
    def archive_rule_arn(self) -> builtins.str:
        '''The Arn of the ArchiveRule resource.'''
        result = self._values.get("archive_rule_arn")
        assert result is not None, "Required property 'archive_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArchiveRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_accessanalyzer.IAnalyzerRef")
class IAnalyzerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Analyzer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="analyzerRef")
    def analyzer_ref(self) -> "AnalyzerReference":
        '''(experimental) A reference to a Analyzer resource.

        :stability: experimental
        '''
        ...


class _IAnalyzerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Analyzer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_accessanalyzer.IAnalyzerRef"

    @builtins.property
    @jsii.member(jsii_name="analyzerRef")
    def analyzer_ref(self) -> "AnalyzerReference":
        '''(experimental) A reference to a Analyzer resource.

        :stability: experimental
        '''
        return typing.cast("AnalyzerReference", jsii.get(self, "analyzerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnalyzerRef).__jsii_proxy_class__ = lambda : _IAnalyzerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_accessanalyzer.IArchiveRuleRef")
class IArchiveRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ArchiveRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="archiveRuleRef")
    def archive_rule_ref(self) -> "ArchiveRuleReference":
        '''(experimental) A reference to a ArchiveRule resource.

        :stability: experimental
        '''
        ...


class _IArchiveRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ArchiveRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_accessanalyzer.IArchiveRuleRef"

    @builtins.property
    @jsii.member(jsii_name="archiveRuleRef")
    def archive_rule_ref(self) -> "ArchiveRuleReference":
        '''(experimental) A reference to a ArchiveRule resource.

        :stability: experimental
        '''
        return typing.cast("ArchiveRuleReference", jsii.get(self, "archiveRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IArchiveRuleRef).__jsii_proxy_class__ = lambda : _IArchiveRuleRefProxy


__all__ = [
    "AnalyzerReference",
    "ArchiveRuleReference",
    "IAnalyzerRef",
    "IArchiveRuleRef",
]

publication.publish()

def _typecheckingstub__d4d375974cd2ef13d3347c0db5ce73a696e350281dee5af93d3a748a4376541c(
    *,
    analyzer_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6242d39b99a5b626f657e476f23494a24574da5367d3d1f79f6f21c0cb36cfab(
    *,
    archive_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAnalyzerRef, IArchiveRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
