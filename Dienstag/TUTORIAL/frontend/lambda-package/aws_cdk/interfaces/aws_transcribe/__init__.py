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
    jsii_type="aws-cdk-lib.interfaces.aws_transcribe.CallAnalyticsCategoryReference",
    jsii_struct_bases=[],
    name_mapping={"call_analytics_category_arn": "callAnalyticsCategoryArn"},
)
class CallAnalyticsCategoryReference:
    def __init__(self, *, call_analytics_category_arn: builtins.str) -> None:
        '''A reference to a CallAnalyticsCategory resource.

        :param call_analytics_category_arn: The Arn of the CallAnalyticsCategory resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transcribe as interfaces_transcribe
            
            call_analytics_category_reference = interfaces_transcribe.CallAnalyticsCategoryReference(
                call_analytics_category_arn="callAnalyticsCategoryArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__82162e0c8afff7fc9dcab005046872ea658067e7b0360cc4030785c17c2e2c0c)
            check_type(argname="argument call_analytics_category_arn", value=call_analytics_category_arn, expected_type=type_hints["call_analytics_category_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "call_analytics_category_arn": call_analytics_category_arn,
        }

    @builtins.property
    def call_analytics_category_arn(self) -> builtins.str:
        '''The Arn of the CallAnalyticsCategory resource.'''
        result = self._values.get("call_analytics_category_arn")
        assert result is not None, "Required property 'call_analytics_category_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CallAnalyticsCategoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_transcribe.ICallAnalyticsCategoryRef"
)
class ICallAnalyticsCategoryRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CallAnalyticsCategory.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="callAnalyticsCategoryRef")
    def call_analytics_category_ref(self) -> "CallAnalyticsCategoryReference":
        '''(experimental) A reference to a CallAnalyticsCategory resource.

        :stability: experimental
        '''
        ...


class _ICallAnalyticsCategoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CallAnalyticsCategory.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transcribe.ICallAnalyticsCategoryRef"

    @builtins.property
    @jsii.member(jsii_name="callAnalyticsCategoryRef")
    def call_analytics_category_ref(self) -> "CallAnalyticsCategoryReference":
        '''(experimental) A reference to a CallAnalyticsCategory resource.

        :stability: experimental
        '''
        return typing.cast("CallAnalyticsCategoryReference", jsii.get(self, "callAnalyticsCategoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICallAnalyticsCategoryRef).__jsii_proxy_class__ = lambda : _ICallAnalyticsCategoryRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_transcribe.IMedicalVocabularyRef"
)
class IMedicalVocabularyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MedicalVocabulary.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="medicalVocabularyRef")
    def medical_vocabulary_ref(self) -> "MedicalVocabularyReference":
        '''(experimental) A reference to a MedicalVocabulary resource.

        :stability: experimental
        '''
        ...


class _IMedicalVocabularyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MedicalVocabulary.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transcribe.IMedicalVocabularyRef"

    @builtins.property
    @jsii.member(jsii_name="medicalVocabularyRef")
    def medical_vocabulary_ref(self) -> "MedicalVocabularyReference":
        '''(experimental) A reference to a MedicalVocabulary resource.

        :stability: experimental
        '''
        return typing.cast("MedicalVocabularyReference", jsii.get(self, "medicalVocabularyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMedicalVocabularyRef).__jsii_proxy_class__ = lambda : _IMedicalVocabularyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transcribe.IVocabularyFilterRef")
class IVocabularyFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VocabularyFilter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vocabularyFilterRef")
    def vocabulary_filter_ref(self) -> "VocabularyFilterReference":
        '''(experimental) A reference to a VocabularyFilter resource.

        :stability: experimental
        '''
        ...


class _IVocabularyFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VocabularyFilter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transcribe.IVocabularyFilterRef"

    @builtins.property
    @jsii.member(jsii_name="vocabularyFilterRef")
    def vocabulary_filter_ref(self) -> "VocabularyFilterReference":
        '''(experimental) A reference to a VocabularyFilter resource.

        :stability: experimental
        '''
        return typing.cast("VocabularyFilterReference", jsii.get(self, "vocabularyFilterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVocabularyFilterRef).__jsii_proxy_class__ = lambda : _IVocabularyFilterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transcribe.IVocabularyRef")
class IVocabularyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Vocabulary.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vocabularyRef")
    def vocabulary_ref(self) -> "VocabularyReference":
        '''(experimental) A reference to a Vocabulary resource.

        :stability: experimental
        '''
        ...


class _IVocabularyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Vocabulary.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transcribe.IVocabularyRef"

    @builtins.property
    @jsii.member(jsii_name="vocabularyRef")
    def vocabulary_ref(self) -> "VocabularyReference":
        '''(experimental) A reference to a Vocabulary resource.

        :stability: experimental
        '''
        return typing.cast("VocabularyReference", jsii.get(self, "vocabularyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVocabularyRef).__jsii_proxy_class__ = lambda : _IVocabularyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transcribe.MedicalVocabularyReference",
    jsii_struct_bases=[],
    name_mapping={"medical_vocabulary_arn": "medicalVocabularyArn"},
)
class MedicalVocabularyReference:
    def __init__(self, *, medical_vocabulary_arn: builtins.str) -> None:
        '''A reference to a MedicalVocabulary resource.

        :param medical_vocabulary_arn: The Arn of the MedicalVocabulary resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transcribe as interfaces_transcribe
            
            medical_vocabulary_reference = interfaces_transcribe.MedicalVocabularyReference(
                medical_vocabulary_arn="medicalVocabularyArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f06a907b769f9db9a5ce36dc7e5a097a556a46fc109b61feebba64d048300b46)
            check_type(argname="argument medical_vocabulary_arn", value=medical_vocabulary_arn, expected_type=type_hints["medical_vocabulary_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "medical_vocabulary_arn": medical_vocabulary_arn,
        }

    @builtins.property
    def medical_vocabulary_arn(self) -> builtins.str:
        '''The Arn of the MedicalVocabulary resource.'''
        result = self._values.get("medical_vocabulary_arn")
        assert result is not None, "Required property 'medical_vocabulary_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedicalVocabularyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transcribe.VocabularyFilterReference",
    jsii_struct_bases=[],
    name_mapping={"vocabulary_filter_arn": "vocabularyFilterArn"},
)
class VocabularyFilterReference:
    def __init__(self, *, vocabulary_filter_arn: builtins.str) -> None:
        '''A reference to a VocabularyFilter resource.

        :param vocabulary_filter_arn: The Arn of the VocabularyFilter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transcribe as interfaces_transcribe
            
            vocabulary_filter_reference = interfaces_transcribe.VocabularyFilterReference(
                vocabulary_filter_arn="vocabularyFilterArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__582efec5c1b8cc6f8fc29d3a057121fb149398b5d6c637b114509b7b274c6ae9)
            check_type(argname="argument vocabulary_filter_arn", value=vocabulary_filter_arn, expected_type=type_hints["vocabulary_filter_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vocabulary_filter_arn": vocabulary_filter_arn,
        }

    @builtins.property
    def vocabulary_filter_arn(self) -> builtins.str:
        '''The Arn of the VocabularyFilter resource.'''
        result = self._values.get("vocabulary_filter_arn")
        assert result is not None, "Required property 'vocabulary_filter_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VocabularyFilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transcribe.VocabularyReference",
    jsii_struct_bases=[],
    name_mapping={"vocabulary_arn": "vocabularyArn"},
)
class VocabularyReference:
    def __init__(self, *, vocabulary_arn: builtins.str) -> None:
        '''A reference to a Vocabulary resource.

        :param vocabulary_arn: The Arn of the Vocabulary resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transcribe as interfaces_transcribe
            
            vocabulary_reference = interfaces_transcribe.VocabularyReference(
                vocabulary_arn="vocabularyArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__fbd78f5b9e2d84b8df4c8e60ff3586a759b63b1b05d9502469ebae03db36d036)
            check_type(argname="argument vocabulary_arn", value=vocabulary_arn, expected_type=type_hints["vocabulary_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vocabulary_arn": vocabulary_arn,
        }

    @builtins.property
    def vocabulary_arn(self) -> builtins.str:
        '''The Arn of the Vocabulary resource.'''
        result = self._values.get("vocabulary_arn")
        assert result is not None, "Required property 'vocabulary_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VocabularyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CallAnalyticsCategoryReference",
    "ICallAnalyticsCategoryRef",
    "IMedicalVocabularyRef",
    "IVocabularyFilterRef",
    "IVocabularyRef",
    "MedicalVocabularyReference",
    "VocabularyFilterReference",
    "VocabularyReference",
]

publication.publish()

def _typecheckingstub__82162e0c8afff7fc9dcab005046872ea658067e7b0360cc4030785c17c2e2c0c(
    *,
    call_analytics_category_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f06a907b769f9db9a5ce36dc7e5a097a556a46fc109b61feebba64d048300b46(
    *,
    medical_vocabulary_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__582efec5c1b8cc6f8fc29d3a057121fb149398b5d6c637b114509b7b274c6ae9(
    *,
    vocabulary_filter_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd78f5b9e2d84b8df4c8e60ff3586a759b63b1b05d9502469ebae03db36d036(
    *,
    vocabulary_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICallAnalyticsCategoryRef, IMedicalVocabularyRef, IVocabularyFilterRef, IVocabularyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
