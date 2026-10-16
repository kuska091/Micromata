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
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.DocumentClassifierEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"document_classifier_endpoint_arn": "documentClassifierEndpointArn"},
)
class DocumentClassifierEndpointReference:
    def __init__(self, *, document_classifier_endpoint_arn: builtins.str) -> None:
        '''A reference to a DocumentClassifierEndpoint resource.

        :param document_classifier_endpoint_arn: The Arn of the DocumentClassifierEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_comprehend as interfaces_comprehend
            
            document_classifier_endpoint_reference = interfaces_comprehend.DocumentClassifierEndpointReference(
                document_classifier_endpoint_arn="documentClassifierEndpointArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__98648d83ddeda88755f02a206442084b18e0e70317b38c3f5cfa7ef45d447311)
            check_type(argname="argument document_classifier_endpoint_arn", value=document_classifier_endpoint_arn, expected_type=type_hints["document_classifier_endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "document_classifier_endpoint_arn": document_classifier_endpoint_arn,
        }

    @builtins.property
    def document_classifier_endpoint_arn(self) -> builtins.str:
        '''The Arn of the DocumentClassifierEndpoint resource.'''
        result = self._values.get("document_classifier_endpoint_arn")
        assert result is not None, "Required property 'document_classifier_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocumentClassifierEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.DocumentClassifierReference",
    jsii_struct_bases=[],
    name_mapping={"document_classifier_arn": "documentClassifierArn"},
)
class DocumentClassifierReference:
    def __init__(self, *, document_classifier_arn: builtins.str) -> None:
        '''A reference to a DocumentClassifier resource.

        :param document_classifier_arn: The Arn of the DocumentClassifier resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_comprehend as interfaces_comprehend
            
            document_classifier_reference = interfaces_comprehend.DocumentClassifierReference(
                document_classifier_arn="documentClassifierArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__e9fa934fd61e384a4f96df7d216e90fb61ab7b36d10b061f5c8f65018a486c69)
            check_type(argname="argument document_classifier_arn", value=document_classifier_arn, expected_type=type_hints["document_classifier_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "document_classifier_arn": document_classifier_arn,
        }

    @builtins.property
    def document_classifier_arn(self) -> builtins.str:
        '''The Arn of the DocumentClassifier resource.'''
        result = self._values.get("document_classifier_arn")
        assert result is not None, "Required property 'document_classifier_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocumentClassifierReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.EntityRecognizerReference",
    jsii_struct_bases=[],
    name_mapping={"entity_recognizer_arn": "entityRecognizerArn"},
)
class EntityRecognizerReference:
    def __init__(self, *, entity_recognizer_arn: builtins.str) -> None:
        '''A reference to a EntityRecognizer resource.

        :param entity_recognizer_arn: The Arn of the EntityRecognizer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_comprehend as interfaces_comprehend
            
            entity_recognizer_reference = interfaces_comprehend.EntityRecognizerReference(
                entity_recognizer_arn="entityRecognizerArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8058319a7aa0d849f49e70c29d60222b84a006f0d5e30a888a886df7f07fee79)
            check_type(argname="argument entity_recognizer_arn", value=entity_recognizer_arn, expected_type=type_hints["entity_recognizer_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entity_recognizer_arn": entity_recognizer_arn,
        }

    @builtins.property
    def entity_recognizer_arn(self) -> builtins.str:
        '''The Arn of the EntityRecognizer resource.'''
        result = self._values.get("entity_recognizer_arn")
        assert result is not None, "Required property 'entity_recognizer_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EntityRecognizerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.FlywheelReference",
    jsii_struct_bases=[],
    name_mapping={"flywheel_arn": "flywheelArn"},
)
class FlywheelReference:
    def __init__(self, *, flywheel_arn: builtins.str) -> None:
        '''A reference to a Flywheel resource.

        :param flywheel_arn: The Arn of the Flywheel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_comprehend as interfaces_comprehend
            
            flywheel_reference = interfaces_comprehend.FlywheelReference(
                flywheel_arn="flywheelArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__324b0a4251a268a7d0e2108be6b77682a5cf7efd9bb727770aa1bb1d59102a8f)
            check_type(argname="argument flywheel_arn", value=flywheel_arn, expected_type=type_hints["flywheel_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flywheel_arn": flywheel_arn,
        }

    @builtins.property
    def flywheel_arn(self) -> builtins.str:
        '''The Arn of the Flywheel resource.'''
        result = self._values.get("flywheel_arn")
        assert result is not None, "Required property 'flywheel_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlywheelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.IDocumentClassifierEndpointRef"
)
class IDocumentClassifierEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentClassifierEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="documentClassifierEndpointRef")
    def document_classifier_endpoint_ref(self) -> "DocumentClassifierEndpointReference":
        '''(experimental) A reference to a DocumentClassifierEndpoint resource.

        :stability: experimental
        '''
        ...


class _IDocumentClassifierEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentClassifierEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_comprehend.IDocumentClassifierEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="documentClassifierEndpointRef")
    def document_classifier_endpoint_ref(self) -> "DocumentClassifierEndpointReference":
        '''(experimental) A reference to a DocumentClassifierEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("DocumentClassifierEndpointReference", jsii.get(self, "documentClassifierEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDocumentClassifierEndpointRef).__jsii_proxy_class__ = lambda : _IDocumentClassifierEndpointRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.IDocumentClassifierRef"
)
class IDocumentClassifierRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentClassifier.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="documentClassifierRef")
    def document_classifier_ref(self) -> "DocumentClassifierReference":
        '''(experimental) A reference to a DocumentClassifier resource.

        :stability: experimental
        '''
        ...


class _IDocumentClassifierRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentClassifier.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_comprehend.IDocumentClassifierRef"

    @builtins.property
    @jsii.member(jsii_name="documentClassifierRef")
    def document_classifier_ref(self) -> "DocumentClassifierReference":
        '''(experimental) A reference to a DocumentClassifier resource.

        :stability: experimental
        '''
        return typing.cast("DocumentClassifierReference", jsii.get(self, "documentClassifierRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDocumentClassifierRef).__jsii_proxy_class__ = lambda : _IDocumentClassifierRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_comprehend.IEntityRecognizerRef")
class IEntityRecognizerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EntityRecognizer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="entityRecognizerRef")
    def entity_recognizer_ref(self) -> "EntityRecognizerReference":
        '''(experimental) A reference to a EntityRecognizer resource.

        :stability: experimental
        '''
        ...


class _IEntityRecognizerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EntityRecognizer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_comprehend.IEntityRecognizerRef"

    @builtins.property
    @jsii.member(jsii_name="entityRecognizerRef")
    def entity_recognizer_ref(self) -> "EntityRecognizerReference":
        '''(experimental) A reference to a EntityRecognizer resource.

        :stability: experimental
        '''
        return typing.cast("EntityRecognizerReference", jsii.get(self, "entityRecognizerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEntityRecognizerRef).__jsii_proxy_class__ = lambda : _IEntityRecognizerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_comprehend.IFlywheelRef")
class IFlywheelRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Flywheel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flywheelRef")
    def flywheel_ref(self) -> "FlywheelReference":
        '''(experimental) A reference to a Flywheel resource.

        :stability: experimental
        '''
        ...


class _IFlywheelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Flywheel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_comprehend.IFlywheelRef"

    @builtins.property
    @jsii.member(jsii_name="flywheelRef")
    def flywheel_ref(self) -> "FlywheelReference":
        '''(experimental) A reference to a Flywheel resource.

        :stability: experimental
        '''
        return typing.cast("FlywheelReference", jsii.get(self, "flywheelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlywheelRef).__jsii_proxy_class__ = lambda : _IFlywheelRefProxy


__all__ = [
    "DocumentClassifierEndpointReference",
    "DocumentClassifierReference",
    "EntityRecognizerReference",
    "FlywheelReference",
    "IDocumentClassifierEndpointRef",
    "IDocumentClassifierRef",
    "IEntityRecognizerRef",
    "IFlywheelRef",
]

publication.publish()

def _typecheckingstub__98648d83ddeda88755f02a206442084b18e0e70317b38c3f5cfa7ef45d447311(
    *,
    document_classifier_endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9fa934fd61e384a4f96df7d216e90fb61ab7b36d10b061f5c8f65018a486c69(
    *,
    document_classifier_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8058319a7aa0d849f49e70c29d60222b84a006f0d5e30a888a886df7f07fee79(
    *,
    entity_recognizer_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324b0a4251a268a7d0e2108be6b77682a5cf7efd9bb727770aa1bb1d59102a8f(
    *,
    flywheel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDocumentClassifierEndpointRef, IDocumentClassifierRef, IEntityRecognizerRef, IFlywheelRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
