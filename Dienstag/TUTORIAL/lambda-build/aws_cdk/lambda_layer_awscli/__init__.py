r'''
# AWS Lambda Layer with AWS CLI

This module exports a single class called `AwsCliLayer` which is a `lambda.Layer` that bundles the AWS CLI.

Any Lambda Function that uses this layer must use a Python 3.x runtime.

Usage:

```python
# AwsCliLayer bundles the AWS CLI in a lambda layer
from aws_cdk.lambda_layer_awscli import AwsCliLayer

# fn: lambda.Function

fn.add_layers(AwsCliLayer(self, "AwsCliLayer"))
```

The CLI will be installed under `/opt/awscli/aws`.

## Alternatives

This module bundles AWS cli v1. To use AWS cli v2, you can use the
external module [awscdk-asset-awscli](https://github.com/cdklabs/awscdk-asset-awscli/tree/awscli-v2/main).
'''
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


from .._jsii import *

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

    import aws_cdk.aws_lambda as _aws_lambda_b8f2f472
    import constructs as _constructs_77d1e7e8
else:

    _aws_lambda_b8f2f472 = _LazyImport("aws_cdk.aws_lambda")
    _constructs_77d1e7e8 = _LazyImport("constructs")


class AwsCliLayer(
    _aws_lambda_b8f2f472.LayerVersion,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.lambda_layer_awscli.AwsCliLayer",
):
    '''An AWS Lambda layer that includes the AWS CLI.

    :exampleMetadata: infused

    Example::

        # AwsCliLayer bundles the AWS CLI in a lambda layer
        from aws_cdk.lambda_layer_awscli import AwsCliLayer
        
        # fn: lambda.Function
        
        fn.add_layers(AwsCliLayer(self, "AwsCliLayer"))
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6c4c04a3bd0e81227b6f6cea95381918fe1a67f2603e9459f027659f8bcf0bd6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))


__all__ = [
    "AwsCliLayer",
]

publication.publish()

def _typecheckingstub__6c4c04a3bd0e81227b6f6cea95381918fe1a67f2603e9459f027659f8bcf0bd6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
