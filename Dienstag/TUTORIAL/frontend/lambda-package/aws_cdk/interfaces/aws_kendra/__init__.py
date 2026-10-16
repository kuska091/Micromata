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
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_arn": "dataSourceArn",
        "data_source_id": "dataSourceId",
        "index_id": "indexId",
    },
)
class DataSourceReference:
    def __init__(
        self,
        *,
        data_source_arn: builtins.str,
        data_source_id: builtins.str,
        index_id: builtins.str,
    ) -> None:
        '''A reference to a DataSource resource.

        :param data_source_arn: The ARN of the DataSource resource.
        :param data_source_id: The Id of the DataSource resource.
        :param index_id: The IndexId of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            data_source_reference = interfaces_kendra.DataSourceReference(
                data_source_arn="dataSourceArn",
                data_source_id="dataSourceId",
                index_id="indexId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__26a2266da96cc0a7063425a169455c1a15681197af9c6cf20fadd6cea5b1aef5)
            check_type(argname="argument data_source_arn", value=data_source_arn, expected_type=type_hints["data_source_arn"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_arn": data_source_arn,
            "data_source_id": data_source_id,
            "index_id": index_id,
        }

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The ARN of the DataSource resource.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The Id of the DataSource resource.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The IndexId of the DataSource resource.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.FaqReference",
    jsii_struct_bases=[],
    name_mapping={"faq_arn": "faqArn", "faq_id": "faqId", "index_id": "indexId"},
)
class FaqReference:
    def __init__(
        self,
        *,
        faq_arn: builtins.str,
        faq_id: builtins.str,
        index_id: builtins.str,
    ) -> None:
        '''A reference to a Faq resource.

        :param faq_arn: The ARN of the Faq resource.
        :param faq_id: The Id of the Faq resource.
        :param index_id: The IndexId of the Faq resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            faq_reference = interfaces_kendra.FaqReference(
                faq_arn="faqArn",
                faq_id="faqId",
                index_id="indexId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7625e62231fe84325a87668fc4fd70f592af31757a95bd7b6a61041391e98537)
            check_type(argname="argument faq_arn", value=faq_arn, expected_type=type_hints["faq_arn"])
            check_type(argname="argument faq_id", value=faq_id, expected_type=type_hints["faq_id"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "faq_arn": faq_arn,
            "faq_id": faq_id,
            "index_id": index_id,
        }

    @builtins.property
    def faq_arn(self) -> builtins.str:
        '''The ARN of the Faq resource.'''
        result = self._values.get("faq_arn")
        assert result is not None, "Required property 'faq_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def faq_id(self) -> builtins.str:
        '''The Id of the Faq resource.'''
        result = self._values.get("faq_id")
        assert result is not None, "Required property 'faq_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The IndexId of the Faq resource.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FaqReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.FeaturedResultsSetReference",
    jsii_struct_bases=[],
    name_mapping={"featured_results_set_arn": "featuredResultsSetArn"},
)
class FeaturedResultsSetReference:
    def __init__(self, *, featured_results_set_arn: builtins.str) -> None:
        '''A reference to a FeaturedResultsSet resource.

        :param featured_results_set_arn: The Arn of the FeaturedResultsSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            featured_results_set_reference = interfaces_kendra.FeaturedResultsSetReference(
                featured_results_set_arn="featuredResultsSetArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__844fb35ab5ca11cfbfd20a9f155c511e8ac35d01cab5565a72a15ac933f7fd8a)
            check_type(argname="argument featured_results_set_arn", value=featured_results_set_arn, expected_type=type_hints["featured_results_set_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "featured_results_set_arn": featured_results_set_arn,
        }

    @builtins.property
    def featured_results_set_arn(self) -> builtins.str:
        '''The Arn of the FeaturedResultsSet resource.'''
        result = self._values.get("featured_results_set_arn")
        assert result is not None, "Required property 'featured_results_set_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FeaturedResultsSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendra.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendra.IFaqRef")
class IFaqRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Faq.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="faqRef")
    def faq_ref(self) -> "FaqReference":
        '''(experimental) A reference to a Faq resource.

        :stability: experimental
        '''
        ...


class _IFaqRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Faq.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IFaqRef"

    @builtins.property
    @jsii.member(jsii_name="faqRef")
    def faq_ref(self) -> "FaqReference":
        '''(experimental) A reference to a Faq resource.

        :stability: experimental
        '''
        return typing.cast("FaqReference", jsii.get(self, "faqRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFaqRef).__jsii_proxy_class__ = lambda : _IFaqRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendra.IFeaturedResultsSetRef")
class IFeaturedResultsSetRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FeaturedResultsSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="featuredResultsSetRef")
    def featured_results_set_ref(self) -> "FeaturedResultsSetReference":
        '''(experimental) A reference to a FeaturedResultsSet resource.

        :stability: experimental
        '''
        ...


class _IFeaturedResultsSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FeaturedResultsSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IFeaturedResultsSetRef"

    @builtins.property
    @jsii.member(jsii_name="featuredResultsSetRef")
    def featured_results_set_ref(self) -> "FeaturedResultsSetReference":
        '''(experimental) A reference to a FeaturedResultsSet resource.

        :stability: experimental
        '''
        return typing.cast("FeaturedResultsSetReference", jsii.get(self, "featuredResultsSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFeaturedResultsSetRef).__jsii_proxy_class__ = lambda : _IFeaturedResultsSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendra.IIndexRef")
class IIndexRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        ...


class _IIndexRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IIndexRef"

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        return typing.cast("IndexReference", jsii.get(self, "indexRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIndexRef).__jsii_proxy_class__ = lambda : _IIndexRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.IQuerySuggestionsBlockListRef"
)
class IQuerySuggestionsBlockListRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QuerySuggestionsBlockList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="querySuggestionsBlockListRef")
    def query_suggestions_block_list_ref(self) -> "QuerySuggestionsBlockListReference":
        '''(experimental) A reference to a QuerySuggestionsBlockList resource.

        :stability: experimental
        '''
        ...


class _IQuerySuggestionsBlockListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QuerySuggestionsBlockList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IQuerySuggestionsBlockListRef"

    @builtins.property
    @jsii.member(jsii_name="querySuggestionsBlockListRef")
    def query_suggestions_block_list_ref(self) -> "QuerySuggestionsBlockListReference":
        '''(experimental) A reference to a QuerySuggestionsBlockList resource.

        :stability: experimental
        '''
        return typing.cast("QuerySuggestionsBlockListReference", jsii.get(self, "querySuggestionsBlockListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQuerySuggestionsBlockListRef).__jsii_proxy_class__ = lambda : _IQuerySuggestionsBlockListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendra.IThesaurusRef")
class IThesaurusRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Thesaurus.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="thesaurusRef")
    def thesaurus_ref(self) -> "ThesaurusReference":
        '''(experimental) A reference to a Thesaurus resource.

        :stability: experimental
        '''
        ...


class _IThesaurusRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Thesaurus.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendra.IThesaurusRef"

    @builtins.property
    @jsii.member(jsii_name="thesaurusRef")
    def thesaurus_ref(self) -> "ThesaurusReference":
        '''(experimental) A reference to a Thesaurus resource.

        :stability: experimental
        '''
        return typing.cast("ThesaurusReference", jsii.get(self, "thesaurusRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThesaurusRef).__jsii_proxy_class__ = lambda : _IThesaurusRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.IndexReference",
    jsii_struct_bases=[],
    name_mapping={"index_arn": "indexArn", "index_id": "indexId"},
)
class IndexReference:
    def __init__(self, *, index_arn: builtins.str, index_id: builtins.str) -> None:
        '''A reference to a Index resource.

        :param index_arn: The ARN of the Index resource.
        :param index_id: The Id of the Index resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            index_reference = interfaces_kendra.IndexReference(
                index_arn="indexArn",
                index_id="indexId"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__90cd6d290fb63a85515086873543ef20c61d2faa02b3955c1c27c28708e952c4)
            check_type(argname="argument index_arn", value=index_arn, expected_type=type_hints["index_arn"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_arn": index_arn,
            "index_id": index_id,
        }

    @builtins.property
    def index_arn(self) -> builtins.str:
        '''The ARN of the Index resource.'''
        result = self._values.get("index_arn")
        assert result is not None, "Required property 'index_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The Id of the Index resource.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IndexReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.QuerySuggestionsBlockListReference",
    jsii_struct_bases=[],
    name_mapping={"query_suggestions_block_list_arn": "querySuggestionsBlockListArn"},
)
class QuerySuggestionsBlockListReference:
    def __init__(self, *, query_suggestions_block_list_arn: builtins.str) -> None:
        '''A reference to a QuerySuggestionsBlockList resource.

        :param query_suggestions_block_list_arn: The Arn of the QuerySuggestionsBlockList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            query_suggestions_block_list_reference = interfaces_kendra.QuerySuggestionsBlockListReference(
                query_suggestions_block_list_arn="querySuggestionsBlockListArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3cd164c2542e3f3d69a0c3786f4c34b507541cc2e0ff5af22805b95a4abe5490)
            check_type(argname="argument query_suggestions_block_list_arn", value=query_suggestions_block_list_arn, expected_type=type_hints["query_suggestions_block_list_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_suggestions_block_list_arn": query_suggestions_block_list_arn,
        }

    @builtins.property
    def query_suggestions_block_list_arn(self) -> builtins.str:
        '''The Arn of the QuerySuggestionsBlockList resource.'''
        result = self._values.get("query_suggestions_block_list_arn")
        assert result is not None, "Required property 'query_suggestions_block_list_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuerySuggestionsBlockListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kendra.ThesaurusReference",
    jsii_struct_bases=[],
    name_mapping={"thesaurus_arn": "thesaurusArn"},
)
class ThesaurusReference:
    def __init__(self, *, thesaurus_arn: builtins.str) -> None:
        '''A reference to a Thesaurus resource.

        :param thesaurus_arn: The Arn of the Thesaurus resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendra as interfaces_kendra
            
            thesaurus_reference = interfaces_kendra.ThesaurusReference(
                thesaurus_arn="thesaurusArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__87761e4ee89c383eafe612f2a14a47629565230e0e54cc12c5e7dea61c3387d2)
            check_type(argname="argument thesaurus_arn", value=thesaurus_arn, expected_type=type_hints["thesaurus_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "thesaurus_arn": thesaurus_arn,
        }

    @builtins.property
    def thesaurus_arn(self) -> builtins.str:
        '''The Arn of the Thesaurus resource.'''
        result = self._values.get("thesaurus_arn")
        assert result is not None, "Required property 'thesaurus_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThesaurusReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataSourceReference",
    "FaqReference",
    "FeaturedResultsSetReference",
    "IDataSourceRef",
    "IFaqRef",
    "IFeaturedResultsSetRef",
    "IIndexRef",
    "IQuerySuggestionsBlockListRef",
    "IThesaurusRef",
    "IndexReference",
    "QuerySuggestionsBlockListReference",
    "ThesaurusReference",
]

publication.publish()

def _typecheckingstub__26a2266da96cc0a7063425a169455c1a15681197af9c6cf20fadd6cea5b1aef5(
    *,
    data_source_arn: builtins.str,
    data_source_id: builtins.str,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7625e62231fe84325a87668fc4fd70f592af31757a95bd7b6a61041391e98537(
    *,
    faq_arn: builtins.str,
    faq_id: builtins.str,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844fb35ab5ca11cfbfd20a9f155c511e8ac35d01cab5565a72a15ac933f7fd8a(
    *,
    featured_results_set_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90cd6d290fb63a85515086873543ef20c61d2faa02b3955c1c27c28708e952c4(
    *,
    index_arn: builtins.str,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd164c2542e3f3d69a0c3786f4c34b507541cc2e0ff5af22805b95a4abe5490(
    *,
    query_suggestions_block_list_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87761e4ee89c383eafe612f2a14a47629565230e0e54cc12c5e7dea61c3387d2(
    *,
    thesaurus_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDataSourceRef, IFaqRef, IFeaturedResultsSetRef, IIndexRef, IQuerySuggestionsBlockListRef, IThesaurusRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
