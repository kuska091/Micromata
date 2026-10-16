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
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.DatasetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_group_arn": "datasetGroupArn"},
)
class DatasetGroupReference:
    def __init__(self, *, dataset_group_arn: builtins.str) -> None:
        '''A reference to a DatasetGroup resource.

        :param dataset_group_arn: The DatasetGroupArn of the DatasetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            dataset_group_reference = interfaces_personalize.DatasetGroupReference(
                dataset_group_arn="datasetGroupArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9bd607e866ffb5f894ee4515b429500888071106bbb3684630b35c3f634570cb)
            check_type(argname="argument dataset_group_arn", value=dataset_group_arn, expected_type=type_hints["dataset_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_group_arn": dataset_group_arn,
        }

    @builtins.property
    def dataset_group_arn(self) -> builtins.str:
        '''The DatasetGroupArn of the DatasetGroup resource.'''
        result = self._values.get("dataset_group_arn")
        assert result is not None, "Required property 'dataset_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.DatasetReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_arn": "datasetArn"},
)
class DatasetReference:
    def __init__(self, *, dataset_arn: builtins.str) -> None:
        '''A reference to a Dataset resource.

        :param dataset_arn: The DatasetArn of the Dataset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            dataset_reference = interfaces_personalize.DatasetReference(
                dataset_arn="datasetArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8259ee192b97f65bb1bfb7dd2c09770b403cad7400c4318eae4c7d5c897451f3)
            check_type(argname="argument dataset_arn", value=dataset_arn, expected_type=type_hints["dataset_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_arn": dataset_arn,
        }

    @builtins.property
    def dataset_arn(self) -> builtins.str:
        '''The DatasetArn of the Dataset resource.'''
        result = self._values.get("dataset_arn")
        assert result is not None, "Required property 'dataset_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.EventTrackerReference",
    jsii_struct_bases=[],
    name_mapping={"event_tracker_arn": "eventTrackerArn"},
)
class EventTrackerReference:
    def __init__(self, *, event_tracker_arn: builtins.str) -> None:
        '''A reference to a EventTracker resource.

        :param event_tracker_arn: The EventTrackerArn of the EventTracker resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            event_tracker_reference = interfaces_personalize.EventTrackerReference(
                event_tracker_arn="eventTrackerArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6d8d144771c9767d2eb402aa1c45874e15c7a7f3d7d9b725488105373beccc9a)
            check_type(argname="argument event_tracker_arn", value=event_tracker_arn, expected_type=type_hints["event_tracker_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_tracker_arn": event_tracker_arn,
        }

    @builtins.property
    def event_tracker_arn(self) -> builtins.str:
        '''The EventTrackerArn of the EventTracker resource.'''
        result = self._values.get("event_tracker_arn")
        assert result is not None, "Required property 'event_tracker_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventTrackerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.FilterReference",
    jsii_struct_bases=[],
    name_mapping={"filter_arn": "filterArn"},
)
class FilterReference:
    def __init__(self, *, filter_arn: builtins.str) -> None:
        '''A reference to a Filter resource.

        :param filter_arn: The FilterArn of the Filter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            filter_reference = interfaces_personalize.FilterReference(
                filter_arn="filterArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0c6ebb1a85f9ff6cfef36e8c6e0bab3bfbb80f6a4e3394aa47dd50f10f91738c)
            check_type(argname="argument filter_arn", value=filter_arn, expected_type=type_hints["filter_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_arn": filter_arn,
        }

    @builtins.property
    def filter_arn(self) -> builtins.str:
        '''The FilterArn of the Filter resource.'''
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.IDatasetGroupRef")
class IDatasetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DatasetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="datasetGroupRef")
    def dataset_group_ref(self) -> "DatasetGroupReference":
        '''(experimental) A reference to a DatasetGroup resource.

        :stability: experimental
        '''
        ...


class _IDatasetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DatasetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.IDatasetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="datasetGroupRef")
    def dataset_group_ref(self) -> "DatasetGroupReference":
        '''(experimental) A reference to a DatasetGroup resource.

        :stability: experimental
        '''
        return typing.cast("DatasetGroupReference", jsii.get(self, "datasetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetGroupRef).__jsii_proxy_class__ = lambda : _IDatasetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.IDatasetRef")
class IDatasetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Dataset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        ...


class _IDatasetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Dataset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.IDatasetRef"

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        return typing.cast("DatasetReference", jsii.get(self, "datasetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetRef).__jsii_proxy_class__ = lambda : _IDatasetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.IEventTrackerRef")
class IEventTrackerRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventTracker.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventTrackerRef")
    def event_tracker_ref(self) -> "EventTrackerReference":
        '''(experimental) A reference to a EventTracker resource.

        :stability: experimental
        '''
        ...


class _IEventTrackerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventTracker.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.IEventTrackerRef"

    @builtins.property
    @jsii.member(jsii_name="eventTrackerRef")
    def event_tracker_ref(self) -> "EventTrackerReference":
        '''(experimental) A reference to a EventTracker resource.

        :stability: experimental
        '''
        return typing.cast("EventTrackerReference", jsii.get(self, "eventTrackerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventTrackerRef).__jsii_proxy_class__ = lambda : _IEventTrackerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.IFilterRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.IFilterRef"

    @builtins.property
    @jsii.member(jsii_name="filterRef")
    def filter_ref(self) -> "FilterReference":
        '''(experimental) A reference to a Filter resource.

        :stability: experimental
        '''
        return typing.cast("FilterReference", jsii.get(self, "filterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFilterRef).__jsii_proxy_class__ = lambda : _IFilterRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.IMetricAttributionRef"
)
class IMetricAttributionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MetricAttribution.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="metricAttributionRef")
    def metric_attribution_ref(self) -> "MetricAttributionReference":
        '''(experimental) A reference to a MetricAttribution resource.

        :stability: experimental
        '''
        ...


class _IMetricAttributionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MetricAttribution.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.IMetricAttributionRef"

    @builtins.property
    @jsii.member(jsii_name="metricAttributionRef")
    def metric_attribution_ref(self) -> "MetricAttributionReference":
        '''(experimental) A reference to a MetricAttribution resource.

        :stability: experimental
        '''
        return typing.cast("MetricAttributionReference", jsii.get(self, "metricAttributionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMetricAttributionRef).__jsii_proxy_class__ = lambda : _IMetricAttributionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.ISchemaRef")
class ISchemaRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        ...


class _ISchemaRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.ISchemaRef"

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        return typing.cast("SchemaReference", jsii.get(self, "schemaRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaRef).__jsii_proxy_class__ = lambda : _ISchemaRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.ISolutionRef")
class ISolutionRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Solution.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="solutionRef")
    def solution_ref(self) -> "SolutionReference":
        '''(experimental) A reference to a Solution resource.

        :stability: experimental
        '''
        ...


class _ISolutionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Solution.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.ISolutionRef"

    @builtins.property
    @jsii.member(jsii_name="solutionRef")
    def solution_ref(self) -> "SolutionReference":
        '''(experimental) A reference to a Solution resource.

        :stability: experimental
        '''
        return typing.cast("SolutionReference", jsii.get(self, "solutionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISolutionRef).__jsii_proxy_class__ = lambda : _ISolutionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.MetricAttributionReference",
    jsii_struct_bases=[],
    name_mapping={"metric_attribution_arn": "metricAttributionArn"},
)
class MetricAttributionReference:
    def __init__(self, *, metric_attribution_arn: builtins.str) -> None:
        '''A reference to a MetricAttribution resource.

        :param metric_attribution_arn: The MetricAttributionArn of the MetricAttribution resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            metric_attribution_reference = interfaces_personalize.MetricAttributionReference(
                metric_attribution_arn="metricAttributionArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f901034fd37d74f86a1f352aac6f6ff15fc0b4e1c2eefd635246f849663fd5a0)
            check_type(argname="argument metric_attribution_arn", value=metric_attribution_arn, expected_type=type_hints["metric_attribution_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_attribution_arn": metric_attribution_arn,
        }

    @builtins.property
    def metric_attribution_arn(self) -> builtins.str:
        '''The MetricAttributionArn of the MetricAttribution resource.'''
        result = self._values.get("metric_attribution_arn")
        assert result is not None, "Required property 'metric_attribution_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricAttributionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.SchemaReference",
    jsii_struct_bases=[],
    name_mapping={"schema_arn": "schemaArn"},
)
class SchemaReference:
    def __init__(self, *, schema_arn: builtins.str) -> None:
        '''A reference to a Schema resource.

        :param schema_arn: The SchemaArn of the Schema resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            schema_reference = interfaces_personalize.SchemaReference(
                schema_arn="schemaArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a6cd5ef72a7892e6fc2e89c44ce2a2108abd8cb5fa5db53e6d641fbf75e6fd0e)
            check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_arn": schema_arn,
        }

    @builtins.property
    def schema_arn(self) -> builtins.str:
        '''The SchemaArn of the Schema resource.'''
        result = self._values.get("schema_arn")
        assert result is not None, "Required property 'schema_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.SolutionReference",
    jsii_struct_bases=[],
    name_mapping={"solution_arn": "solutionArn"},
)
class SolutionReference:
    def __init__(self, *, solution_arn: builtins.str) -> None:
        '''A reference to a Solution resource.

        :param solution_arn: The SolutionArn of the Solution resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            solution_reference = interfaces_personalize.SolutionReference(
                solution_arn="solutionArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4eb7000ac778c9296a1bcf604536bc2f9b85654eafa6d8acf1a30e8d4a677c4d)
            check_type(argname="argument solution_arn", value=solution_arn, expected_type=type_hints["solution_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "solution_arn": solution_arn,
        }

    @builtins.property
    def solution_arn(self) -> builtins.str:
        '''The SolutionArn of the Solution resource.'''
        result = self._values.get("solution_arn")
        assert result is not None, "Required property 'solution_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SolutionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatasetGroupReference",
    "DatasetReference",
    "EventTrackerReference",
    "FilterReference",
    "IDatasetGroupRef",
    "IDatasetRef",
    "IEventTrackerRef",
    "IFilterRef",
    "IMetricAttributionRef",
    "ISchemaRef",
    "ISolutionRef",
    "MetricAttributionReference",
    "SchemaReference",
    "SolutionReference",
]

publication.publish()

def _typecheckingstub__9bd607e866ffb5f894ee4515b429500888071106bbb3684630b35c3f634570cb(
    *,
    dataset_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8259ee192b97f65bb1bfb7dd2c09770b403cad7400c4318eae4c7d5c897451f3(
    *,
    dataset_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d8d144771c9767d2eb402aa1c45874e15c7a7f3d7d9b725488105373beccc9a(
    *,
    event_tracker_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c6ebb1a85f9ff6cfef36e8c6e0bab3bfbb80f6a4e3394aa47dd50f10f91738c(
    *,
    filter_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f901034fd37d74f86a1f352aac6f6ff15fc0b4e1c2eefd635246f849663fd5a0(
    *,
    metric_attribution_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6cd5ef72a7892e6fc2e89c44ce2a2108abd8cb5fa5db53e6d641fbf75e6fd0e(
    *,
    schema_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb7000ac778c9296a1bcf604536bc2f9b85654eafa6d8acf1a30e8d4a677c4d(
    *,
    solution_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDatasetGroupRef, IDatasetRef, IEventTrackerRef, IFilterRef, IMetricAttributionRef, ISchemaRef, ISolutionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
