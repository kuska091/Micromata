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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apptest.ITestCaseRef")
class ITestCaseRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TestCase.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="testCaseRef")
    def test_case_ref(self) -> "TestCaseReference":
        '''(experimental) A reference to a TestCase resource.

        :stability: experimental
        '''
        ...


class _ITestCaseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TestCase.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apptest.ITestCaseRef"

    @builtins.property
    @jsii.member(jsii_name="testCaseRef")
    def test_case_ref(self) -> "TestCaseReference":
        '''(experimental) A reference to a TestCase resource.

        :stability: experimental
        '''
        return typing.cast("TestCaseReference", jsii.get(self, "testCaseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITestCaseRef).__jsii_proxy_class__ = lambda : _ITestCaseRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apptest.TestCaseReference",
    jsii_struct_bases=[],
    name_mapping={"test_case_arn": "testCaseArn", "test_case_id": "testCaseId"},
)
class TestCaseReference:
    def __init__(
        self,
        *,
        test_case_arn: builtins.str,
        test_case_id: builtins.str,
    ) -> None:
        '''A reference to a TestCase resource.

        :param test_case_arn: The ARN of the TestCase resource.
        :param test_case_id: The TestCaseId of the TestCase resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apptest as interfaces_apptest
            
            test_case_reference = interfaces_apptest.TestCaseReference(
                test_case_arn="testCaseArn",
                test_case_id="testCaseId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0ec1d75b67174e712d5b78d0eca254b067a11f6de3f1b9b017d95b7a38311832)
            check_type(argname="argument test_case_arn", value=test_case_arn, expected_type=type_hints["test_case_arn"])
            check_type(argname="argument test_case_id", value=test_case_id, expected_type=type_hints["test_case_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "test_case_arn": test_case_arn,
            "test_case_id": test_case_id,
        }

    @builtins.property
    def test_case_arn(self) -> builtins.str:
        '''The ARN of the TestCase resource.'''
        result = self._values.get("test_case_arn")
        assert result is not None, "Required property 'test_case_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def test_case_id(self) -> builtins.str:
        '''The TestCaseId of the TestCase resource.'''
        result = self._values.get("test_case_id")
        assert result is not None, "Required property 'test_case_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TestCaseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ITestCaseRef",
    "TestCaseReference",
]

publication.publish()

def _typecheckingstub__0ec1d75b67174e712d5b78d0eca254b067a11f6de3f1b9b017d95b7a38311832(
    *,
    test_case_arn: builtins.str,
    test_case_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ITestCaseRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
