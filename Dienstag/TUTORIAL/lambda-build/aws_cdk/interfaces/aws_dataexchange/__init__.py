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
    jsii_type="aws-cdk-lib.interfaces.aws_dataexchange.DataSetReference",
    jsii_struct_bases=[],
    name_mapping={"data_set_arn": "dataSetArn"},
)
class DataSetReference:
    def __init__(self, *, data_set_arn: builtins.str) -> None:
        '''A reference to a DataSet resource.

        :param data_set_arn: The Arn of the DataSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dataexchange as interfaces_dataexchange
            
            data_set_reference = interfaces_dataexchange.DataSetReference(
                data_set_arn="dataSetArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__93dd07d39a190b2021c06174d3600df567f34e2c365f1a5d00aec1294ce7602b)
            check_type(argname="argument data_set_arn", value=data_set_arn, expected_type=type_hints["data_set_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_set_arn": data_set_arn,
        }

    @builtins.property
    def data_set_arn(self) -> builtins.str:
        '''The Arn of the DataSet resource.'''
        result = self._values.get("data_set_arn")
        assert result is not None, "Required property 'data_set_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_dataexchange.EventActionReference",
    jsii_struct_bases=[],
    name_mapping={"event_action_arn": "eventActionArn"},
)
class EventActionReference:
    def __init__(self, *, event_action_arn: builtins.str) -> None:
        '''A reference to a EventAction resource.

        :param event_action_arn: The Arn of the EventAction resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dataexchange as interfaces_dataexchange
            
            event_action_reference = interfaces_dataexchange.EventActionReference(
                event_action_arn="eventActionArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__df29bae6e4f44f8981a69b4da8427e79df8e73f7decc24442de1b4c110465278)
            check_type(argname="argument event_action_arn", value=event_action_arn, expected_type=type_hints["event_action_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_action_arn": event_action_arn,
        }

    @builtins.property
    def event_action_arn(self) -> builtins.str:
        '''The Arn of the EventAction resource.'''
        result = self._values.get("event_action_arn")
        assert result is not None, "Required property 'event_action_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventActionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dataexchange.IDataSetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dataexchange.IDataSetRef"

    @builtins.property
    @jsii.member(jsii_name="dataSetRef")
    def data_set_ref(self) -> "DataSetReference":
        '''(experimental) A reference to a DataSet resource.

        :stability: experimental
        '''
        return typing.cast("DataSetReference", jsii.get(self, "dataSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSetRef).__jsii_proxy_class__ = lambda : _IDataSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dataexchange.IEventActionRef")
class IEventActionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventAction.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventActionRef")
    def event_action_ref(self) -> "EventActionReference":
        '''(experimental) A reference to a EventAction resource.

        :stability: experimental
        '''
        ...


class _IEventActionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventAction.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dataexchange.IEventActionRef"

    @builtins.property
    @jsii.member(jsii_name="eventActionRef")
    def event_action_ref(self) -> "EventActionReference":
        '''(experimental) A reference to a EventAction resource.

        :stability: experimental
        '''
        return typing.cast("EventActionReference", jsii.get(self, "eventActionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventActionRef).__jsii_proxy_class__ = lambda : _IEventActionRefProxy


__all__ = [
    "DataSetReference",
    "EventActionReference",
    "IDataSetRef",
    "IEventActionRef",
]

publication.publish()

def _typecheckingstub__93dd07d39a190b2021c06174d3600df567f34e2c365f1a5d00aec1294ce7602b(
    *,
    data_set_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df29bae6e4f44f8981a69b4da8427e79df8e73f7decc24442de1b4c110465278(
    *,
    event_action_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDataSetRef, IEventActionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
