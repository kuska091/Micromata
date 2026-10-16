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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3vectors.IIndexRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3vectors.IIndexRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_s3vectors.IVectorBucketPolicyRef"
)
class IVectorBucketPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VectorBucketPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vectorBucketPolicyRef")
    def vector_bucket_policy_ref(self) -> "VectorBucketPolicyReference":
        '''(experimental) A reference to a VectorBucketPolicy resource.

        :stability: experimental
        '''
        ...


class _IVectorBucketPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VectorBucketPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3vectors.IVectorBucketPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="vectorBucketPolicyRef")
    def vector_bucket_policy_ref(self) -> "VectorBucketPolicyReference":
        '''(experimental) A reference to a VectorBucketPolicy resource.

        :stability: experimental
        '''
        return typing.cast("VectorBucketPolicyReference", jsii.get(self, "vectorBucketPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVectorBucketPolicyRef).__jsii_proxy_class__ = lambda : _IVectorBucketPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3vectors.IVectorBucketRef")
class IVectorBucketRef(
    _constructs_77d1e7e8.IConstruct,
    _interfaces_8ca7e747.IEnvironmentAware,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VectorBucket.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vectorBucketRef")
    def vector_bucket_ref(self) -> "VectorBucketReference":
        '''(experimental) A reference to a VectorBucket resource.

        :stability: experimental
        '''
        ...


class _IVectorBucketRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_interfaces_8ca7e747.IEnvironmentAware), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VectorBucket.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3vectors.IVectorBucketRef"

    @builtins.property
    @jsii.member(jsii_name="vectorBucketRef")
    def vector_bucket_ref(self) -> "VectorBucketReference":
        '''(experimental) A reference to a VectorBucket resource.

        :stability: experimental
        '''
        return typing.cast("VectorBucketReference", jsii.get(self, "vectorBucketRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVectorBucketRef).__jsii_proxy_class__ = lambda : _IVectorBucketRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3vectors.IndexReference",
    jsii_struct_bases=[],
    name_mapping={"index_arn": "indexArn"},
)
class IndexReference:
    def __init__(self, *, index_arn: builtins.str) -> None:
        '''A reference to a Index resource.

        :param index_arn: The IndexArn of the Index resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3vectors as interfaces_s3vectors
            
            index_reference = interfaces_s3vectors.IndexReference(
                index_arn="indexArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__dd5325790756b7b0c545be692f8fa367526b4d3150393988c9438e95e7c3851a)
            check_type(argname="argument index_arn", value=index_arn, expected_type=type_hints["index_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_arn": index_arn,
        }

    @builtins.property
    def index_arn(self) -> builtins.str:
        '''The IndexArn of the Index resource.'''
        result = self._values.get("index_arn")
        assert result is not None, "Required property 'index_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_s3vectors.VectorBucketPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"vector_bucket_arn": "vectorBucketArn"},
)
class VectorBucketPolicyReference:
    def __init__(self, *, vector_bucket_arn: builtins.str) -> None:
        '''A reference to a VectorBucketPolicy resource.

        :param vector_bucket_arn: The VectorBucketArn of the VectorBucketPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3vectors as interfaces_s3vectors
            
            vector_bucket_policy_reference = interfaces_s3vectors.VectorBucketPolicyReference(
                vector_bucket_arn="vectorBucketArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__acd0fbf5253b3d6db9ec7c833a7a8e578f1989eb4481d6934f0badcbd30d4d61)
            check_type(argname="argument vector_bucket_arn", value=vector_bucket_arn, expected_type=type_hints["vector_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vector_bucket_arn": vector_bucket_arn,
        }

    @builtins.property
    def vector_bucket_arn(self) -> builtins.str:
        '''The VectorBucketArn of the VectorBucketPolicy resource.'''
        result = self._values.get("vector_bucket_arn")
        assert result is not None, "Required property 'vector_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VectorBucketPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3vectors.VectorBucketReference",
    jsii_struct_bases=[],
    name_mapping={"vector_bucket_arn": "vectorBucketArn"},
)
class VectorBucketReference:
    def __init__(self, *, vector_bucket_arn: builtins.str) -> None:
        '''A reference to a VectorBucket resource.

        :param vector_bucket_arn: The VectorBucketArn of the VectorBucket resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3vectors as interfaces_s3vectors
            
            vector_bucket_reference = interfaces_s3vectors.VectorBucketReference(
                vector_bucket_arn="vectorBucketArn"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__67191fb919d60fb26c1c53010dd5ab8d079a8232c1fefbd12b0dd1d1e8b25c5c)
            check_type(argname="argument vector_bucket_arn", value=vector_bucket_arn, expected_type=type_hints["vector_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vector_bucket_arn": vector_bucket_arn,
        }

    @builtins.property
    def vector_bucket_arn(self) -> builtins.str:
        '''The VectorBucketArn of the VectorBucket resource.'''
        result = self._values.get("vector_bucket_arn")
        assert result is not None, "Required property 'vector_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VectorBucketReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IIndexRef",
    "IVectorBucketPolicyRef",
    "IVectorBucketRef",
    "IndexReference",
    "VectorBucketPolicyReference",
    "VectorBucketReference",
]

publication.publish()

def _typecheckingstub__dd5325790756b7b0c545be692f8fa367526b4d3150393988c9438e95e7c3851a(
    *,
    index_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acd0fbf5253b3d6db9ec7c833a7a8e578f1989eb4481d6934f0badcbd30d4d61(
    *,
    vector_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67191fb919d60fb26c1c53010dd5ab8d079a8232c1fefbd12b0dd1d1e8b25c5c(
    *,
    vector_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IIndexRef, IVectorBucketPolicyRef, IVectorBucketRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
