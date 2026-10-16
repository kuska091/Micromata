r'''
# AWS Lambda Layer with the NPM dependency proxy-agent

This module exports a single class called `NodeProxyAgentLayer` which is a `lambda.Layer` that bundles the NPM dependency [`proxy-agent`](https://www.npmjs.com/package/proxy-agent).

> * proxy-agent Version: 5.0.0

Usage:

```python
from aws_cdk.lambda_layer_node_proxy_agent import NodeProxyAgentLayer
import aws_cdk.aws_lambda as lambda_

# fn: lambda.Function

fn.add_layers(NodeProxyAgentLayer(self, "NodeProxyAgentLayer"))
```

[`proxy-agent`](https://www.npmjs.com/package/proxy-agent) will be installed under `/nodejs/node_modules`.
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


class NodeProxyAgentLayer(
    _aws_lambda_b8f2f472.LayerVersion,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.lambda_layer_node_proxy_agent.NodeProxyAgentLayer",
):
    '''An AWS Lambda layer that includes the NPM dependency ``proxy-agent``.

    :exampleMetadata: infused

    Example::

        from aws_cdk.lambda_layer_node_proxy_agent import NodeProxyAgentLayer
        import aws_cdk.aws_lambda as lambda_
        
        # fn: lambda.Function
        
        fn.add_layers(NodeProxyAgentLayer(self, "NodeProxyAgentLayer"))
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
            type_hints = cached_type_hints(_typecheckingstub__7aa82807bd4f7add65a429f8c2ea3f82e19def82222c33ec0b8b731b45dfab22)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))


__all__ = [
    "NodeProxyAgentLayer",
]

publication.publish()

def _typecheckingstub__7aa82807bd4f7add65a429f8c2ea3f82e19def82222c33ec0b8b731b45dfab22(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
