r'''
# AWS::Invoicing Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_invoicing as invoicing
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Invoicing construct libraries](https://constructs.dev/search?q=invoicing)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Invoicing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Invoicing.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Invoicing](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Invoicing.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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

    import aws_cdk as _aws_cdk_0cae9daa
    import aws_cdk.interfaces.aws_invoicing as _aws_invoicing_2e0dcac4
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_invoicing_2e0dcac4 = _LazyImport("aws_cdk.interfaces.aws_invoicing")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_invoicing_2e0dcac4.IInvoiceUnitRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnInvoiceUnit(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_invoicing.CfnInvoiceUnit",
):
    '''An invoice unit is a set of mutually exclusive account that correspond to your business entity.

    Invoice units allow you separate AWS account costs and configures your invoice for each business entity going forward.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html
    :cloudformationResource: AWS::Invoicing::InvoiceUnit
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_invoicing as invoicing
        
        cfn_invoice_unit = invoicing.CfnInvoiceUnit(self, "MyCfnInvoiceUnit",
            invoice_receiver="invoiceReceiver",
            name="name",
            rule=invoicing.CfnInvoiceUnit.RuleProperty(
                linked_accounts=["linkedAccounts"]
            ),
        
            # the properties below are optional
            description="description",
            resource_tags=[invoicing.CfnInvoiceUnit.ResourceTagProperty(
                key="key",
                value="value"
            )],
            tax_inheritance_disabled=False
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        invoice_receiver: builtins.str,
        name: builtins.str,
        rule: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnInvoiceUnit.RuleProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Sequence[typing.Union["CfnInvoiceUnit.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tax_inheritance_disabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
    ) -> None:
        '''Create a new ``AWS::Invoicing::InvoiceUnit``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param invoice_receiver: The account that receives invoices related to the invoice unit.
        :param name: A unique name that is distinctive within your AWS .
        :param rule: An ``InvoiceUnitRule`` object used the categorize invoice units.
        :param description: The assigned description for an invoice unit. This information can't be modified or deleted.
        :param resource_tags: The tag structure that contains a tag key and value.
        :param tax_inheritance_disabled: Whether the invoice unit based tax inheritance is/ should be enabled or disabled.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ec21d6093b38a709121aa7ff8c0297fdced84c912861970ec02e3bc317566bc6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInvoiceUnitProps(
            invoice_receiver=invoice_receiver,
            name=name,
            rule=rule,
            description=description,
            resource_tags=resource_tags,
            tax_inheritance_disabled=tax_inheritance_disabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForInvoiceUnit")
    @builtins.classmethod
    def arn_for_invoice_unit(
        cls,
        resource: "_aws_invoicing_2e0dcac4.IInvoiceUnitRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__da43b69b71c31ed78101f0716e31477bd305068db757443e4b0bfe0a5e113036)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForInvoiceUnit", [resource]))

    @jsii.member(jsii_name="isCfnInvoiceUnit")
    @builtins.classmethod
    def is_cfn_invoice_unit(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnInvoiceUnit.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__f97e5d0e05825f59a4f670e04661e7a2360b8e39fa20004da63e2812f003323d)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnInvoiceUnit", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__adc114041b1663662392e373664cbecf8821f20a78009df2b54077dc4acd4a4f)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__107a105e04f9f1089e314bd557a043d7c27143f765a9e1ea9ee1881882b1c045)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrInvoiceUnitArn")
    def attr_invoice_unit_arn(self) -> builtins.str:
        '''The ARN to identify an invoice unit.

        This information can't be modified or deleted.

        :cloudformationAttribute: InvoiceUnitArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInvoiceUnitArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModified")
    def attr_last_modified(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''The last time the invoice unit was updated.

        This is important to determine the version of invoice unit configuration used to create the invoices. Any invoice created after this modified time will use this invoice unit configuration.

        :cloudformationAttribute: LastModified
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrLastModified"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="invoiceUnitRef")
    def invoice_unit_ref(self) -> "_aws_invoicing_2e0dcac4.InvoiceUnitReference":
        '''A reference to a InvoiceUnit resource.'''
        return typing.cast("_aws_invoicing_2e0dcac4.InvoiceUnitReference", jsii.get(self, "invoiceUnitRef"))

    @builtins.property
    @jsii.member(jsii_name="invoiceReceiver")
    def invoice_receiver(self) -> builtins.str:
        '''The account that receives invoices related to the invoice unit.'''
        return typing.cast(builtins.str, jsii.get(self, "invoiceReceiver"))

    @invoice_receiver.setter
    def invoice_receiver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__696a83d1411656063bc2e9712df3268ed2ef2248e55f5547394f8f5e78942d54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invoiceReceiver", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A unique name that is distinctive within your AWS .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d3aae9f9b97db34c63c2be162b2b82f9e0ec45cb8225187a2e441c3d9df5fc6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnInvoiceUnit.RuleProperty"]:
        '''An ``InvoiceUnitRule`` object used the categorize invoice units.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnInvoiceUnit.RuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnInvoiceUnit.RuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__11bd3886ac3007b56aa51fb96bae09bccc9e9cc9c0abd45264540df233a478a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The assigned description for an invoice unit.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__076923c02da9e54ceab543bf61c811c9f8f6d99b2e479b043a782db5a4b4fa76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.List["CfnInvoiceUnit.ResourceTagProperty"]]:
        '''The tag structure that contains a tag key and value.'''
        return typing.cast(typing.Optional[typing.List["CfnInvoiceUnit.ResourceTagProperty"]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.List["CfnInvoiceUnit.ResourceTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3778014062d8d17e79b38d529c3fb3bb66de99f01976014103eaa0ec3100ef9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="taxInheritanceDisabled")
    def tax_inheritance_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether the invoice unit based tax inheritance is/ should be enabled or disabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], jsii.get(self, "taxInheritanceDisabled"))

    @tax_inheritance_disabled.setter
    def tax_inheritance_disabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__42f1928e769bc3f0a10f5fa89984b4cfd7df0a60a619ce30e6135776c65ea23b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taxInheritanceDisabled", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_invoicing.CfnInvoiceUnit.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ResourceTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The tag structure that contains a tag key and value.

            :param key: The object key of your of your resource tag.
            :param value: The specific value of the resource tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-resourcetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                resource_tag_property = invoicing.CfnInvoiceUnit.ResourceTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__859a6df074320cbe1a9099b42236f7d3759a4ce5419adf8bb3c001155a98ed4f)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The object key of your of your resource tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-resourcetag.html#cfn-invoicing-invoiceunit-resourcetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The specific value of the resource tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-resourcetag.html#cfn-invoicing-invoiceunit-resourcetag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_invoicing.CfnInvoiceUnit.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={"linked_accounts": "linkedAccounts"},
    )
    class RuleProperty:
        def __init__(self, *, linked_accounts: typing.Sequence[builtins.str]) -> None:
            '''The ``InvoiceUnitRule`` object used to update invoice units.

            :param linked_accounts: The list of ``LINKED_ACCOUNT`` IDs where charges are included within the invoice unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                rule_property = invoicing.CfnInvoiceUnit.RuleProperty(
                    linked_accounts=["linkedAccounts"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8558be1d7f9b75065f54979d9fa00436e977578b77550f4c1d3e32a6b46a4bea)
                check_type(argname="argument linked_accounts", value=linked_accounts, expected_type=type_hints["linked_accounts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "linked_accounts": linked_accounts,
            }

        @builtins.property
        def linked_accounts(self) -> typing.List[builtins.str]:
            '''The list of ``LINKED_ACCOUNT`` IDs where charges are included within the invoice unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-rule.html#cfn-invoicing-invoiceunit-rule-linkedaccounts
            '''
            result = self._values.get("linked_accounts")
            assert result is not None, "Required property 'linked_accounts' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_invoicing.CfnInvoiceUnitProps",
    jsii_struct_bases=[],
    name_mapping={
        "invoice_receiver": "invoiceReceiver",
        "name": "name",
        "rule": "rule",
        "description": "description",
        "resource_tags": "resourceTags",
        "tax_inheritance_disabled": "taxInheritanceDisabled",
    },
)
class CfnInvoiceUnitProps:
    def __init__(
        self,
        *,
        invoice_receiver: builtins.str,
        name: builtins.str,
        rule: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnInvoiceUnit.RuleProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Sequence[typing.Union["CfnInvoiceUnit.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tax_inheritance_disabled: typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInvoiceUnit``.

        :param invoice_receiver: The account that receives invoices related to the invoice unit.
        :param name: A unique name that is distinctive within your AWS .
        :param rule: An ``InvoiceUnitRule`` object used the categorize invoice units.
        :param description: The assigned description for an invoice unit. This information can't be modified or deleted.
        :param resource_tags: The tag structure that contains a tag key and value.
        :param tax_inheritance_disabled: Whether the invoice unit based tax inheritance is/ should be enabled or disabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_invoicing as invoicing
            
            cfn_invoice_unit_props = invoicing.CfnInvoiceUnitProps(
                invoice_receiver="invoiceReceiver",
                name="name",
                rule=invoicing.CfnInvoiceUnit.RuleProperty(
                    linked_accounts=["linkedAccounts"]
                ),
            
                # the properties below are optional
                description="description",
                resource_tags=[invoicing.CfnInvoiceUnit.ResourceTagProperty(
                    key="key",
                    value="value"
                )],
                tax_inheritance_disabled=False
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a4fdf29b8c64b38c209320f998b71b0ce2601c2ac744bde28886f66b3cefdce6)
            check_type(argname="argument invoice_receiver", value=invoice_receiver, expected_type=type_hints["invoice_receiver"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            check_type(argname="argument tax_inheritance_disabled", value=tax_inheritance_disabled, expected_type=type_hints["tax_inheritance_disabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "invoice_receiver": invoice_receiver,
            "name": name,
            "rule": rule,
        }
        if description is not None:
            self._values["description"] = description
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if tax_inheritance_disabled is not None:
            self._values["tax_inheritance_disabled"] = tax_inheritance_disabled

    @builtins.property
    def invoice_receiver(self) -> builtins.str:
        '''The account that receives invoices related to the invoice unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-invoicereceiver
        '''
        result = self._values.get("invoice_receiver")
        assert result is not None, "Required property 'invoice_receiver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique name that is distinctive within your AWS .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnInvoiceUnit.RuleProperty"]:
        '''An ``InvoiceUnitRule`` object used the categorize invoice units.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnInvoiceUnit.RuleProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The assigned description for an invoice unit.

        This information can't be modified or deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.List["CfnInvoiceUnit.ResourceTagProperty"]]:
        '''The tag structure that contains a tag key and value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.List["CfnInvoiceUnit.ResourceTagProperty"]], result)

    @builtins.property
    def tax_inheritance_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]]:
        '''Whether the invoice unit based tax inheritance is/ should be enabled or disabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-taxinheritancedisabled
        '''
        result = self._values.get("tax_inheritance_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInvoiceUnitProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_invoicing_2e0dcac4.IProcurementPortalPreferenceRef, _aws_cdk_0cae9daa.ITaggableV2)
class CfnProcurementPortalPreference(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_invoicing.CfnProcurementPortalPreference",
):
    '''Creates and manages a procurement portal preference configuration for e-invoice delivery and purchase order retrieval.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html
    :cloudformationResource: AWS::Invoicing::ProcurementPortalPreference
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_invoicing as invoicing
        
        cfn_procurement_portal_preference = invoicing.CfnProcurementPortalPreference(self, "MyCfnProcurementPortalPreference",
            buyer_domain="buyerDomain",
            buyer_identifier="buyerIdentifier",
            contacts=[invoicing.CfnProcurementPortalPreference.ContactProperty(
                email="email",
                name="name"
            )],
            einvoice_delivery_enabled=False,
            procurement_portal_name="procurementPortalName",
            purchase_order_retrieval_enabled=False,
            supplier_domain="supplierDomain",
            supplier_identifier="supplierIdentifier",
        
            # the properties below are optional
            einvoice_delivery_preference=invoicing.CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty(
                connection_testing_method="connectionTestingMethod",
                einvoice_delivery_activation_date="einvoiceDeliveryActivationDate",
                einvoice_delivery_attachment_types=["einvoiceDeliveryAttachmentTypes"],
                einvoice_delivery_document_types=["einvoiceDeliveryDocumentTypes"],
                protocol="protocol",
                purchase_order_data_sources=[invoicing.CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty(
                    einvoice_delivery_document_type="einvoiceDeliveryDocumentType",
                    purchase_order_data_source_type="purchaseOrderDataSourceType"
                )]
            ),
            procurement_portal_instance_endpoint="procurementPortalInstanceEndpoint",
            procurement_portal_shared_secret="procurementPortalSharedSecret",
            selector=invoicing.CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty(
                invoice_unit_arns=["invoiceUnitArns"]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            test_env_preference=invoicing.CfnProcurementPortalPreference.TestEnvPreferenceProperty(
                buyer_domain="buyerDomain",
                buyer_identifier="buyerIdentifier",
                procurement_portal_instance_endpoint="procurementPortalInstanceEndpoint",
                procurement_portal_shared_secret="procurementPortalSharedSecret",
                supplier_domain="supplierDomain",
                supplier_identifier="supplierIdentifier"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        buyer_domain: builtins.str,
        buyer_identifier: builtins.str,
        contacts: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.ContactProperty", typing.Dict[builtins.str, typing.Any]]]]],
        einvoice_delivery_enabled: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
        procurement_portal_name: builtins.str,
        purchase_order_retrieval_enabled: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
        supplier_domain: builtins.str,
        supplier_identifier: builtins.str,
        einvoice_delivery_preference: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        procurement_portal_instance_endpoint: typing.Optional[builtins.str] = None,
        procurement_portal_shared_secret: typing.Optional[builtins.str] = None,
        selector: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        test_env_preference: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.TestEnvPreferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Invoicing::ProcurementPortalPreference``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param buyer_domain: The domain identifier for the buyer in the procurement portal.
        :param buyer_identifier: The unique identifier for the buyer in the procurement portal.
        :param contacts: List of contact information for portal administrators and technical contacts.
        :param einvoice_delivery_enabled: Indicates whether e-invoice delivery is enabled for this procurement portal preference.
        :param procurement_portal_name: The name of the procurement portal.
        :param purchase_order_retrieval_enabled: Indicates whether purchase order retrieval is enabled for this procurement portal preference.
        :param supplier_domain: The domain identifier for the supplier in the procurement portal.
        :param supplier_identifier: The unique identifier for the supplier in the procurement portal.
        :param einvoice_delivery_preference: Specifies the preferences for e-invoice delivery.
        :param procurement_portal_instance_endpoint: The endpoint URL where e-invoices are delivered to the procurement portal.
        :param procurement_portal_shared_secret: The shared secret or authentication credential used for secure communication with the procurement portal.
        :param selector: Specifies criteria for selecting which invoices should be processed.
        :param tags: The tags associated with this procurement portal preference.
        :param test_env_preference: Configuration settings for the test environment of the procurement portal.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__029bdd0e6dfff8bc7bf5c49c51804c97e0b1d0537540ea47dc09cd25752a22ff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProcurementPortalPreferenceProps(
            buyer_domain=buyer_domain,
            buyer_identifier=buyer_identifier,
            contacts=contacts,
            einvoice_delivery_enabled=einvoice_delivery_enabled,
            procurement_portal_name=procurement_portal_name,
            purchase_order_retrieval_enabled=purchase_order_retrieval_enabled,
            supplier_domain=supplier_domain,
            supplier_identifier=supplier_identifier,
            einvoice_delivery_preference=einvoice_delivery_preference,
            procurement_portal_instance_endpoint=procurement_portal_instance_endpoint,
            procurement_portal_shared_secret=procurement_portal_shared_secret,
            selector=selector,
            tags=tags,
            test_env_preference=test_env_preference,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForProcurementPortalPreference")
    @builtins.classmethod
    def arn_for_procurement_portal_preference(
        cls,
        resource: "_aws_invoicing_2e0dcac4.IProcurementPortalPreferenceRef",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__8a079b8608c7dac4312263bab6e0f2695f6ed99143c7834d2b550b80ca597ac3)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForProcurementPortalPreference", [resource]))

    @jsii.member(jsii_name="isCfnProcurementPortalPreference")
    @builtins.classmethod
    def is_cfn_procurement_portal_preference(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnProcurementPortalPreference.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__edc77f26abe3d5e4805cbabb0b048b298f6571b03f4cd2c55c76f697cc3a68ca)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnProcurementPortalPreference", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__68ff8ba49e62e93bb37bdeb3f85558ee79de35d30d2939d243d15ddb1f6a5bfb)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b8a366d2ee022ece1d7f5bec490a857b7aa51ef31adb97dba0d0c3bab9a70328)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''The AWS account ID associated with this procurement portal preference.

        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateDate")
    def attr_create_date(self) -> builtins.str:
        '''The date and time when the procurement portal preference was created.

        :cloudformationAttribute: CreateDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateDate"))

    @builtins.property
    @jsii.member(jsii_name="attrEinvoiceDeliveryPreferenceStatus")
    def attr_einvoice_delivery_preference_status(self) -> builtins.str:
        '''The current status of the e-invoice delivery preference.

        :cloudformationAttribute: EinvoiceDeliveryPreferenceStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEinvoiceDeliveryPreferenceStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdateDate")
    def attr_last_update_date(self) -> builtins.str:
        '''The date and time when the procurement portal preference was last updated.

        :cloudformationAttribute: LastUpdateDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdateDate"))

    @builtins.property
    @jsii.member(jsii_name="attrProcurementPortalPreferenceArn")
    def attr_procurement_portal_preference_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the procurement portal preference.

        :cloudformationAttribute: ProcurementPortalPreferenceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProcurementPortalPreferenceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPurchaseOrderRetrievalEndpoint")
    def attr_purchase_order_retrieval_endpoint(self) -> builtins.str:
        '''The endpoint URL used for retrieving purchase orders from the procurement portal.

        :cloudformationAttribute: PurchaseOrderRetrievalEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPurchaseOrderRetrievalEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrPurchaseOrderRetrievalPreferenceStatus")
    def attr_purchase_order_retrieval_preference_status(self) -> builtins.str:
        '''The current status of the purchase order retrieval preference.

        :cloudformationAttribute: PurchaseOrderRetrievalPreferenceStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPurchaseOrderRetrievalPreferenceStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> jsii.Number:
        '''The version number of the procurement portal preference configuration.

        :cloudformationAttribute: Version
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVersion"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_aws_cdk_0cae9daa.TagManager":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_aws_cdk_0cae9daa.TagManager", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="procurementPortalPreferenceRef")
    def procurement_portal_preference_ref(
        self,
    ) -> "_aws_invoicing_2e0dcac4.ProcurementPortalPreferenceReference":
        '''A reference to a ProcurementPortalPreference resource.'''
        return typing.cast("_aws_invoicing_2e0dcac4.ProcurementPortalPreferenceReference", jsii.get(self, "procurementPortalPreferenceRef"))

    @builtins.property
    @jsii.member(jsii_name="buyerDomain")
    def buyer_domain(self) -> builtins.str:
        '''The domain identifier for the buyer in the procurement portal.'''
        return typing.cast(builtins.str, jsii.get(self, "buyerDomain"))

    @buyer_domain.setter
    def buyer_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__b1d10d0bb1fcdcbebd2b4dd7222f1ccb9b1383aa534abd4e682d735c76b28d27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buyerDomain", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="buyerIdentifier")
    def buyer_identifier(self) -> builtins.str:
        '''The unique identifier for the buyer in the procurement portal.'''
        return typing.cast(builtins.str, jsii.get(self, "buyerIdentifier"))

    @buyer_identifier.setter
    def buyer_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__07b9eea162bd558acac2aa573f0c0e835a04819658a7052a0cab2c488e6bc209)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buyerIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contacts")
    def contacts(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ContactProperty"]]]:
        '''List of contact information for portal administrators and technical contacts.'''
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ContactProperty"]]], jsii.get(self, "contacts"))

    @contacts.setter
    def contacts(
        self,
        value: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ContactProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6dedf6ac8d3e460f3f57e46a81176da4201c77eab83727f01d05060f3cfb2189)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contacts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="einvoiceDeliveryEnabled")
    def einvoice_delivery_enabled(
        self,
    ) -> typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]:
        '''Indicates whether e-invoice delivery is enabled for this procurement portal preference.'''
        return typing.cast(typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"], jsii.get(self, "einvoiceDeliveryEnabled"))

    @einvoice_delivery_enabled.setter
    def einvoice_delivery_enabled(
        self,
        value: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__4f0630b9d1d9245d17b1b968adf76015952d211333e694d20b0e160742ff7075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "einvoiceDeliveryEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="procurementPortalName")
    def procurement_portal_name(self) -> builtins.str:
        '''The name of the procurement portal.'''
        return typing.cast(builtins.str, jsii.get(self, "procurementPortalName"))

    @procurement_portal_name.setter
    def procurement_portal_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__825e59078e44b0e1ffad2567eb65e09f52b7597da77a9e14b5e0248590d11061)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "procurementPortalName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="purchaseOrderRetrievalEnabled")
    def purchase_order_retrieval_enabled(
        self,
    ) -> typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]:
        '''Indicates whether purchase order retrieval is enabled for this procurement portal preference.'''
        return typing.cast(typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"], jsii.get(self, "purchaseOrderRetrievalEnabled"))

    @purchase_order_retrieval_enabled.setter
    def purchase_order_retrieval_enabled(
        self,
        value: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__45bc22f9a03fb9f6b9c3460c174ea3fcda86a367c9707a671fcb466b64b1ab4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purchaseOrderRetrievalEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="supplierDomain")
    def supplier_domain(self) -> builtins.str:
        '''The domain identifier for the supplier in the procurement portal.'''
        return typing.cast(builtins.str, jsii.get(self, "supplierDomain"))

    @supplier_domain.setter
    def supplier_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__436ee13eb12f20dab661d2c3f4a6a8e816f01bb5fbb2753bff73f1e126c0b3f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supplierDomain", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="supplierIdentifier")
    def supplier_identifier(self) -> builtins.str:
        '''The unique identifier for the supplier in the procurement portal.'''
        return typing.cast(builtins.str, jsii.get(self, "supplierIdentifier"))

    @supplier_identifier.setter
    def supplier_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__659606ff1885d2dd3c4b062d6de991a45d8409f7bbe34249ca9411e37dc7126c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supplierIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="einvoiceDeliveryPreference")
    def einvoice_delivery_preference(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty"]]:
        '''Specifies the preferences for e-invoice delivery.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty"]], jsii.get(self, "einvoiceDeliveryPreference"))

    @einvoice_delivery_preference.setter
    def einvoice_delivery_preference(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__5c417dd9f3a753cbe47a2526aae096a2a67b3d29f1ba3eadaed8a15344b6c39a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "einvoiceDeliveryPreference", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="procurementPortalInstanceEndpoint")
    def procurement_portal_instance_endpoint(self) -> typing.Optional[builtins.str]:
        '''The endpoint URL where e-invoices are delivered to the procurement portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "procurementPortalInstanceEndpoint"))

    @procurement_portal_instance_endpoint.setter
    def procurement_portal_instance_endpoint(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__a1de909d1d637bfdc2e0f32272c29403ff98cbe6a8e0f7a52e6d7a76fb3fc4cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "procurementPortalInstanceEndpoint", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="procurementPortalSharedSecret")
    def procurement_portal_shared_secret(self) -> typing.Optional[builtins.str]:
        '''The shared secret or authentication credential used for secure communication with the procurement portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "procurementPortalSharedSecret"))

    @procurement_portal_shared_secret.setter
    def procurement_portal_shared_secret(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__6e2961867c3abc32458e0d520b0cb27f1d70ae9190cd9b5ffa89c58bef618f1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "procurementPortalSharedSecret", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty"]]:
        '''Specifies criteria for selecting which invoices should be processed.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty"]], jsii.get(self, "selector"))

    @selector.setter
    def selector(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__ce2827a48efd72c21d5eb05540e59dde3e013ee0ab32f2d4c77548beaa82532c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags associated with this procurement portal preference.'''
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7fec4d5f6fcb8ade8160add8328999ef970036b6bd084c98fca41ba08a59938e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="testEnvPreference")
    def test_env_preference(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.TestEnvPreferenceProperty"]]:
        '''Configuration settings for the test environment of the procurement portal.'''
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.TestEnvPreferenceProperty"]], jsii.get(self, "testEnvPreference"))

    @test_env_preference.setter
    def test_env_preference(
        self,
        value: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.TestEnvPreferenceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9bc37498ffbb8d3cb91b4f290310eefc777983bea95938ccf28884a0f9310c8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testEnvPreference", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_invoicing.CfnProcurementPortalPreference.ContactProperty",
        jsii_struct_bases=[],
        name_mapping={"email": "email", "name": "name"},
    )
    class ContactProperty:
        def __init__(
            self,
            *,
            email: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contact information for a person or role associated with the procurement portal preference.

            :param email: The email address of the contact person or role.
            :param name: The name of the contact person or role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-contact.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                contact_property = invoicing.CfnProcurementPortalPreference.ContactProperty(
                    email="email",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__618a1e684c24b646908bde431602e86d8fb08e95700960a893509ae60dde79bf)
                check_type(argname="argument email", value=email, expected_type=type_hints["email"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email is not None:
                self._values["email"] = email
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def email(self) -> typing.Optional[builtins.str]:
            '''The email address of the contact person or role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-contact.html#cfn-invoicing-procurementportalpreference-contact-email
            '''
            result = self._values.get("email")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the contact person or role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-contact.html#cfn-invoicing-procurementportalpreference-contact-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContactProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_invoicing.CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_testing_method": "connectionTestingMethod",
            "einvoice_delivery_activation_date": "einvoiceDeliveryActivationDate",
            "einvoice_delivery_attachment_types": "einvoiceDeliveryAttachmentTypes",
            "einvoice_delivery_document_types": "einvoiceDeliveryDocumentTypes",
            "protocol": "protocol",
            "purchase_order_data_sources": "purchaseOrderDataSources",
        },
    )
    class EinvoiceDeliveryPreferenceProperty:
        def __init__(
            self,
            *,
            connection_testing_method: typing.Optional[builtins.str] = None,
            einvoice_delivery_activation_date: typing.Optional[builtins.str] = None,
            einvoice_delivery_attachment_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            einvoice_delivery_document_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            protocol: typing.Optional[builtins.str] = None,
            purchase_order_data_sources: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies the preferences for e-invoice delivery.

            :param connection_testing_method: The method to use for testing the connection to the procurement portal.
            :param einvoice_delivery_activation_date: The ISO 8601 date-time when e-invoice delivery should be activated.
            :param einvoice_delivery_attachment_types: The types of attachments to include with the e-invoice delivery.
            :param einvoice_delivery_document_types: The types of e-invoice documents to be delivered.
            :param protocol: The communication protocol to use for e-invoice delivery.
            :param purchase_order_data_sources: The sources of purchase order data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                einvoice_delivery_preference_property = invoicing.CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty(
                    connection_testing_method="connectionTestingMethod",
                    einvoice_delivery_activation_date="einvoiceDeliveryActivationDate",
                    einvoice_delivery_attachment_types=["einvoiceDeliveryAttachmentTypes"],
                    einvoice_delivery_document_types=["einvoiceDeliveryDocumentTypes"],
                    protocol="protocol",
                    purchase_order_data_sources=[invoicing.CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty(
                        einvoice_delivery_document_type="einvoiceDeliveryDocumentType",
                        purchase_order_data_source_type="purchaseOrderDataSourceType"
                    )]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__a0ea2ba7aa7761e8982aa9c2961b13d6808ce833f56badd9547187284b5660bb)
                check_type(argname="argument connection_testing_method", value=connection_testing_method, expected_type=type_hints["connection_testing_method"])
                check_type(argname="argument einvoice_delivery_activation_date", value=einvoice_delivery_activation_date, expected_type=type_hints["einvoice_delivery_activation_date"])
                check_type(argname="argument einvoice_delivery_attachment_types", value=einvoice_delivery_attachment_types, expected_type=type_hints["einvoice_delivery_attachment_types"])
                check_type(argname="argument einvoice_delivery_document_types", value=einvoice_delivery_document_types, expected_type=type_hints["einvoice_delivery_document_types"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument purchase_order_data_sources", value=purchase_order_data_sources, expected_type=type_hints["purchase_order_data_sources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_testing_method is not None:
                self._values["connection_testing_method"] = connection_testing_method
            if einvoice_delivery_activation_date is not None:
                self._values["einvoice_delivery_activation_date"] = einvoice_delivery_activation_date
            if einvoice_delivery_attachment_types is not None:
                self._values["einvoice_delivery_attachment_types"] = einvoice_delivery_attachment_types
            if einvoice_delivery_document_types is not None:
                self._values["einvoice_delivery_document_types"] = einvoice_delivery_document_types
            if protocol is not None:
                self._values["protocol"] = protocol
            if purchase_order_data_sources is not None:
                self._values["purchase_order_data_sources"] = purchase_order_data_sources

        @builtins.property
        def connection_testing_method(self) -> typing.Optional[builtins.str]:
            '''The method to use for testing the connection to the procurement portal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.html#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-connectiontestingmethod
            '''
            result = self._values.get("connection_testing_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def einvoice_delivery_activation_date(self) -> typing.Optional[builtins.str]:
            '''The ISO 8601 date-time when e-invoice delivery should be activated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.html#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliveryactivationdate
            '''
            result = self._values.get("einvoice_delivery_activation_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def einvoice_delivery_attachment_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The types of attachments to include with the e-invoice delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.html#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliveryattachmenttypes
            '''
            result = self._values.get("einvoice_delivery_attachment_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def einvoice_delivery_document_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The types of e-invoice documents to be delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.html#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliverydocumenttypes
            '''
            result = self._values.get("einvoice_delivery_document_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The communication protocol to use for e-invoice delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.html#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def purchase_order_data_sources(
            self,
        ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty"]]]]:
            '''The sources of purchase order data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.html#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-purchaseorderdatasources
            '''
            result = self._values.get("purchase_order_data_sources")
            return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EinvoiceDeliveryPreferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_invoicing.CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"invoice_unit_arns": "invoiceUnitArns"},
    )
    class ProcurementPortalPreferenceSelectorProperty:
        def __init__(
            self,
            *,
            invoice_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies criteria for selecting which invoices should be processed.

            :param invoice_unit_arns: The Amazon Resource Name (ARN) of invoice unit identifiers to which this preference applies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-procurementportalpreferenceselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                procurement_portal_preference_selector_property = invoicing.CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty(
                    invoice_unit_arns=["invoiceUnitArns"]
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__ce433272ae1534e13389226c4f92f6df75571b6820bfcee07e03ab330a888482)
                check_type(argname="argument invoice_unit_arns", value=invoice_unit_arns, expected_type=type_hints["invoice_unit_arns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if invoice_unit_arns is not None:
                self._values["invoice_unit_arns"] = invoice_unit_arns

        @builtins.property
        def invoice_unit_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Amazon Resource Name (ARN) of invoice unit identifiers to which this preference applies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-procurementportalpreferenceselector.html#cfn-invoicing-procurementportalpreference-procurementportalpreferenceselector-invoiceunitarns
            '''
            result = self._values.get("invoice_unit_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcurementPortalPreferenceSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_invoicing.CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "einvoice_delivery_document_type": "einvoiceDeliveryDocumentType",
            "purchase_order_data_source_type": "purchaseOrderDataSourceType",
        },
    )
    class PurchaseOrderDataSourceProperty:
        def __init__(
            self,
            *,
            einvoice_delivery_document_type: typing.Optional[builtins.str] = None,
            purchase_order_data_source_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the source configuration for retrieving purchase order data.

            :param einvoice_delivery_document_type: The type of e-invoice document that requires purchase order data.
            :param purchase_order_data_source_type: The type of source for purchase order data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                purchase_order_data_source_property = invoicing.CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty(
                    einvoice_delivery_document_type="einvoiceDeliveryDocumentType",
                    purchase_order_data_source_type="purchaseOrderDataSourceType"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__41ac73008d2a40cf91fd6f0d925a51acd1bb18398c6970f991cf31dea38eb01e)
                check_type(argname="argument einvoice_delivery_document_type", value=einvoice_delivery_document_type, expected_type=type_hints["einvoice_delivery_document_type"])
                check_type(argname="argument purchase_order_data_source_type", value=purchase_order_data_source_type, expected_type=type_hints["purchase_order_data_source_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if einvoice_delivery_document_type is not None:
                self._values["einvoice_delivery_document_type"] = einvoice_delivery_document_type
            if purchase_order_data_source_type is not None:
                self._values["purchase_order_data_source_type"] = purchase_order_data_source_type

        @builtins.property
        def einvoice_delivery_document_type(self) -> typing.Optional[builtins.str]:
            '''The type of e-invoice document that requires purchase order data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource.html#cfn-invoicing-procurementportalpreference-purchaseorderdatasource-einvoicedeliverydocumenttype
            '''
            result = self._values.get("einvoice_delivery_document_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def purchase_order_data_source_type(self) -> typing.Optional[builtins.str]:
            '''The type of source for purchase order data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource.html#cfn-invoicing-procurementportalpreference-purchaseorderdatasource-purchaseorderdatasourcetype
            '''
            result = self._values.get("purchase_order_data_source_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PurchaseOrderDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_invoicing.CfnProcurementPortalPreference.TestEnvPreferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "buyer_domain": "buyerDomain",
            "buyer_identifier": "buyerIdentifier",
            "procurement_portal_instance_endpoint": "procurementPortalInstanceEndpoint",
            "procurement_portal_shared_secret": "procurementPortalSharedSecret",
            "supplier_domain": "supplierDomain",
            "supplier_identifier": "supplierIdentifier",
        },
    )
    class TestEnvPreferenceProperty:
        def __init__(
            self,
            *,
            buyer_domain: typing.Optional[builtins.str] = None,
            buyer_identifier: typing.Optional[builtins.str] = None,
            procurement_portal_instance_endpoint: typing.Optional[builtins.str] = None,
            procurement_portal_shared_secret: typing.Optional[builtins.str] = None,
            supplier_domain: typing.Optional[builtins.str] = None,
            supplier_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration settings for the test environment of the procurement portal.

            :param buyer_domain: The domain identifier for the buyer in the test environment.
            :param buyer_identifier: The unique identifier for the buyer in the test environment.
            :param procurement_portal_instance_endpoint: The endpoint URL for e-invoice delivery in the test environment.
            :param procurement_portal_shared_secret: The shared secret for secure communication in the test environment.
            :param supplier_domain: The domain identifier for the supplier in the test environment.
            :param supplier_identifier: The unique identifier for the supplier in the test environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-testenvpreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                test_env_preference_property = invoicing.CfnProcurementPortalPreference.TestEnvPreferenceProperty(
                    buyer_domain="buyerDomain",
                    buyer_identifier="buyerIdentifier",
                    procurement_portal_instance_endpoint="procurementPortalInstanceEndpoint",
                    procurement_portal_shared_secret="procurementPortalSharedSecret",
                    supplier_domain="supplierDomain",
                    supplier_identifier="supplierIdentifier"
                )
            '''
            if __debug__:
                type_hints = cached_type_hints(_typecheckingstub__8c38bcb34298aa687714fe0d6d649b953d3e390e0e43bdfc2fe6ec7873d84f50)
                check_type(argname="argument buyer_domain", value=buyer_domain, expected_type=type_hints["buyer_domain"])
                check_type(argname="argument buyer_identifier", value=buyer_identifier, expected_type=type_hints["buyer_identifier"])
                check_type(argname="argument procurement_portal_instance_endpoint", value=procurement_portal_instance_endpoint, expected_type=type_hints["procurement_portal_instance_endpoint"])
                check_type(argname="argument procurement_portal_shared_secret", value=procurement_portal_shared_secret, expected_type=type_hints["procurement_portal_shared_secret"])
                check_type(argname="argument supplier_domain", value=supplier_domain, expected_type=type_hints["supplier_domain"])
                check_type(argname="argument supplier_identifier", value=supplier_identifier, expected_type=type_hints["supplier_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if buyer_domain is not None:
                self._values["buyer_domain"] = buyer_domain
            if buyer_identifier is not None:
                self._values["buyer_identifier"] = buyer_identifier
            if procurement_portal_instance_endpoint is not None:
                self._values["procurement_portal_instance_endpoint"] = procurement_portal_instance_endpoint
            if procurement_portal_shared_secret is not None:
                self._values["procurement_portal_shared_secret"] = procurement_portal_shared_secret
            if supplier_domain is not None:
                self._values["supplier_domain"] = supplier_domain
            if supplier_identifier is not None:
                self._values["supplier_identifier"] = supplier_identifier

        @builtins.property
        def buyer_domain(self) -> typing.Optional[builtins.str]:
            '''The domain identifier for the buyer in the test environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-testenvpreference.html#cfn-invoicing-procurementportalpreference-testenvpreference-buyerdomain
            '''
            result = self._values.get("buyer_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def buyer_identifier(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for the buyer in the test environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-testenvpreference.html#cfn-invoicing-procurementportalpreference-testenvpreference-buyeridentifier
            '''
            result = self._values.get("buyer_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def procurement_portal_instance_endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint URL for e-invoice delivery in the test environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-testenvpreference.html#cfn-invoicing-procurementportalpreference-testenvpreference-procurementportalinstanceendpoint
            '''
            result = self._values.get("procurement_portal_instance_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def procurement_portal_shared_secret(self) -> typing.Optional[builtins.str]:
            '''The shared secret for secure communication in the test environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-testenvpreference.html#cfn-invoicing-procurementportalpreference-testenvpreference-procurementportalsharedsecret
            '''
            result = self._values.get("procurement_portal_shared_secret")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def supplier_domain(self) -> typing.Optional[builtins.str]:
            '''The domain identifier for the supplier in the test environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-testenvpreference.html#cfn-invoicing-procurementportalpreference-testenvpreference-supplierdomain
            '''
            result = self._values.get("supplier_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def supplier_identifier(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for the supplier in the test environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-procurementportalpreference-testenvpreference.html#cfn-invoicing-procurementportalpreference-testenvpreference-supplieridentifier
            '''
            result = self._values.get("supplier_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TestEnvPreferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_invoicing.CfnProcurementPortalPreferenceProps",
    jsii_struct_bases=[],
    name_mapping={
        "buyer_domain": "buyerDomain",
        "buyer_identifier": "buyerIdentifier",
        "contacts": "contacts",
        "einvoice_delivery_enabled": "einvoiceDeliveryEnabled",
        "procurement_portal_name": "procurementPortalName",
        "purchase_order_retrieval_enabled": "purchaseOrderRetrievalEnabled",
        "supplier_domain": "supplierDomain",
        "supplier_identifier": "supplierIdentifier",
        "einvoice_delivery_preference": "einvoiceDeliveryPreference",
        "procurement_portal_instance_endpoint": "procurementPortalInstanceEndpoint",
        "procurement_portal_shared_secret": "procurementPortalSharedSecret",
        "selector": "selector",
        "tags": "tags",
        "test_env_preference": "testEnvPreference",
    },
)
class CfnProcurementPortalPreferenceProps:
    def __init__(
        self,
        *,
        buyer_domain: builtins.str,
        buyer_identifier: builtins.str,
        contacts: typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Sequence[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.ContactProperty", typing.Dict[builtins.str, typing.Any]]]]],
        einvoice_delivery_enabled: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
        procurement_portal_name: builtins.str,
        purchase_order_retrieval_enabled: typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"],
        supplier_domain: builtins.str,
        supplier_identifier: builtins.str,
        einvoice_delivery_preference: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        procurement_portal_instance_endpoint: typing.Optional[builtins.str] = None,
        procurement_portal_shared_secret: typing.Optional[builtins.str] = None,
        selector: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_aws_cdk_0cae9daa.CfnTag", typing.Dict[builtins.str, typing.Any]]]] = None,
        test_env_preference: typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.Union["CfnProcurementPortalPreference.TestEnvPreferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProcurementPortalPreference``.

        :param buyer_domain: The domain identifier for the buyer in the procurement portal.
        :param buyer_identifier: The unique identifier for the buyer in the procurement portal.
        :param contacts: List of contact information for portal administrators and technical contacts.
        :param einvoice_delivery_enabled: Indicates whether e-invoice delivery is enabled for this procurement portal preference.
        :param procurement_portal_name: The name of the procurement portal.
        :param purchase_order_retrieval_enabled: Indicates whether purchase order retrieval is enabled for this procurement portal preference.
        :param supplier_domain: The domain identifier for the supplier in the procurement portal.
        :param supplier_identifier: The unique identifier for the supplier in the procurement portal.
        :param einvoice_delivery_preference: Specifies the preferences for e-invoice delivery.
        :param procurement_portal_instance_endpoint: The endpoint URL where e-invoices are delivered to the procurement portal.
        :param procurement_portal_shared_secret: The shared secret or authentication credential used for secure communication with the procurement portal.
        :param selector: Specifies criteria for selecting which invoices should be processed.
        :param tags: The tags associated with this procurement portal preference.
        :param test_env_preference: Configuration settings for the test environment of the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_invoicing as invoicing
            
            cfn_procurement_portal_preference_props = invoicing.CfnProcurementPortalPreferenceProps(
                buyer_domain="buyerDomain",
                buyer_identifier="buyerIdentifier",
                contacts=[invoicing.CfnProcurementPortalPreference.ContactProperty(
                    email="email",
                    name="name"
                )],
                einvoice_delivery_enabled=False,
                procurement_portal_name="procurementPortalName",
                purchase_order_retrieval_enabled=False,
                supplier_domain="supplierDomain",
                supplier_identifier="supplierIdentifier",
            
                # the properties below are optional
                einvoice_delivery_preference=invoicing.CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty(
                    connection_testing_method="connectionTestingMethod",
                    einvoice_delivery_activation_date="einvoiceDeliveryActivationDate",
                    einvoice_delivery_attachment_types=["einvoiceDeliveryAttachmentTypes"],
                    einvoice_delivery_document_types=["einvoiceDeliveryDocumentTypes"],
                    protocol="protocol",
                    purchase_order_data_sources=[invoicing.CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty(
                        einvoice_delivery_document_type="einvoiceDeliveryDocumentType",
                        purchase_order_data_source_type="purchaseOrderDataSourceType"
                    )]
                ),
                procurement_portal_instance_endpoint="procurementPortalInstanceEndpoint",
                procurement_portal_shared_secret="procurementPortalSharedSecret",
                selector=invoicing.CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty(
                    invoice_unit_arns=["invoiceUnitArns"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                test_env_preference=invoicing.CfnProcurementPortalPreference.TestEnvPreferenceProperty(
                    buyer_domain="buyerDomain",
                    buyer_identifier="buyerIdentifier",
                    procurement_portal_instance_endpoint="procurementPortalInstanceEndpoint",
                    procurement_portal_shared_secret="procurementPortalSharedSecret",
                    supplier_domain="supplierDomain",
                    supplier_identifier="supplierIdentifier"
                )
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__3b1800f373ce231d966275771ded23b747067f0d5961aa491d3f555214d3a207)
            check_type(argname="argument buyer_domain", value=buyer_domain, expected_type=type_hints["buyer_domain"])
            check_type(argname="argument buyer_identifier", value=buyer_identifier, expected_type=type_hints["buyer_identifier"])
            check_type(argname="argument contacts", value=contacts, expected_type=type_hints["contacts"])
            check_type(argname="argument einvoice_delivery_enabled", value=einvoice_delivery_enabled, expected_type=type_hints["einvoice_delivery_enabled"])
            check_type(argname="argument procurement_portal_name", value=procurement_portal_name, expected_type=type_hints["procurement_portal_name"])
            check_type(argname="argument purchase_order_retrieval_enabled", value=purchase_order_retrieval_enabled, expected_type=type_hints["purchase_order_retrieval_enabled"])
            check_type(argname="argument supplier_domain", value=supplier_domain, expected_type=type_hints["supplier_domain"])
            check_type(argname="argument supplier_identifier", value=supplier_identifier, expected_type=type_hints["supplier_identifier"])
            check_type(argname="argument einvoice_delivery_preference", value=einvoice_delivery_preference, expected_type=type_hints["einvoice_delivery_preference"])
            check_type(argname="argument procurement_portal_instance_endpoint", value=procurement_portal_instance_endpoint, expected_type=type_hints["procurement_portal_instance_endpoint"])
            check_type(argname="argument procurement_portal_shared_secret", value=procurement_portal_shared_secret, expected_type=type_hints["procurement_portal_shared_secret"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument test_env_preference", value=test_env_preference, expected_type=type_hints["test_env_preference"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "buyer_domain": buyer_domain,
            "buyer_identifier": buyer_identifier,
            "contacts": contacts,
            "einvoice_delivery_enabled": einvoice_delivery_enabled,
            "procurement_portal_name": procurement_portal_name,
            "purchase_order_retrieval_enabled": purchase_order_retrieval_enabled,
            "supplier_domain": supplier_domain,
            "supplier_identifier": supplier_identifier,
        }
        if einvoice_delivery_preference is not None:
            self._values["einvoice_delivery_preference"] = einvoice_delivery_preference
        if procurement_portal_instance_endpoint is not None:
            self._values["procurement_portal_instance_endpoint"] = procurement_portal_instance_endpoint
        if procurement_portal_shared_secret is not None:
            self._values["procurement_portal_shared_secret"] = procurement_portal_shared_secret
        if selector is not None:
            self._values["selector"] = selector
        if tags is not None:
            self._values["tags"] = tags
        if test_env_preference is not None:
            self._values["test_env_preference"] = test_env_preference

    @builtins.property
    def buyer_domain(self) -> builtins.str:
        '''The domain identifier for the buyer in the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-buyerdomain
        '''
        result = self._values.get("buyer_domain")
        assert result is not None, "Required property 'buyer_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buyer_identifier(self) -> builtins.str:
        '''The unique identifier for the buyer in the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-buyeridentifier
        '''
        result = self._values.get("buyer_identifier")
        assert result is not None, "Required property 'buyer_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contacts(
        self,
    ) -> typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ContactProperty"]]]:
        '''List of contact information for portal administrators and technical contacts.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-contacts
        '''
        result = self._values.get("contacts")
        assert result is not None, "Required property 'contacts' is missing"
        return typing.cast(typing.Union["_aws_cdk_0cae9daa.IResolvable", typing.List[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ContactProperty"]]], result)

    @builtins.property
    def einvoice_delivery_enabled(
        self,
    ) -> typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]:
        '''Indicates whether e-invoice delivery is enabled for this procurement portal preference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-einvoicedeliveryenabled
        '''
        result = self._values.get("einvoice_delivery_enabled")
        assert result is not None, "Required property 'einvoice_delivery_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"], result)

    @builtins.property
    def procurement_portal_name(self) -> builtins.str:
        '''The name of the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-procurementportalname
        '''
        result = self._values.get("procurement_portal_name")
        assert result is not None, "Required property 'procurement_portal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def purchase_order_retrieval_enabled(
        self,
    ) -> typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"]:
        '''Indicates whether purchase order retrieval is enabled for this procurement portal preference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-purchaseorderretrievalenabled
        '''
        result = self._values.get("purchase_order_retrieval_enabled")
        assert result is not None, "Required property 'purchase_order_retrieval_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, "_aws_cdk_0cae9daa.IResolvable"], result)

    @builtins.property
    def supplier_domain(self) -> builtins.str:
        '''The domain identifier for the supplier in the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-supplierdomain
        '''
        result = self._values.get("supplier_domain")
        assert result is not None, "Required property 'supplier_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def supplier_identifier(self) -> builtins.str:
        '''The unique identifier for the supplier in the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-supplieridentifier
        '''
        result = self._values.get("supplier_identifier")
        assert result is not None, "Required property 'supplier_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def einvoice_delivery_preference(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty"]]:
        '''Specifies the preferences for e-invoice delivery.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference
        '''
        result = self._values.get("einvoice_delivery_preference")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty"]], result)

    @builtins.property
    def procurement_portal_instance_endpoint(self) -> typing.Optional[builtins.str]:
        '''The endpoint URL where e-invoices are delivered to the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-procurementportalinstanceendpoint
        '''
        result = self._values.get("procurement_portal_instance_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def procurement_portal_shared_secret(self) -> typing.Optional[builtins.str]:
        '''The shared secret or authentication credential used for secure communication with the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-procurementportalsharedsecret
        '''
        result = self._values.get("procurement_portal_shared_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty"]]:
        '''Specifies criteria for selecting which invoices should be processed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]]:
        '''The tags associated with this procurement portal preference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_aws_cdk_0cae9daa.CfnTag"]], result)

    @builtins.property
    def test_env_preference(
        self,
    ) -> typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.TestEnvPreferenceProperty"]]:
        '''Configuration settings for the test environment of the procurement portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-procurementportalpreference.html#cfn-invoicing-procurementportalpreference-testenvpreference
        '''
        result = self._values.get("test_env_preference")
        return typing.cast(typing.Optional[typing.Union["_aws_cdk_0cae9daa.IResolvable", "CfnProcurementPortalPreference.TestEnvPreferenceProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProcurementPortalPreferenceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnInvoiceUnit",
    "CfnInvoiceUnitProps",
    "CfnProcurementPortalPreference",
    "CfnProcurementPortalPreferenceProps",
]

publication.publish()

def _typecheckingstub__ec21d6093b38a709121aa7ff8c0297fdced84c912861970ec02e3bc317566bc6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    invoice_receiver: builtins.str,
    name: builtins.str,
    rule: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnInvoiceUnit.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Sequence[typing.Union[CfnInvoiceUnit.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tax_inheritance_disabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da43b69b71c31ed78101f0716e31477bd305068db757443e4b0bfe0a5e113036(
    resource: _aws_invoicing_2e0dcac4.IInvoiceUnitRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f97e5d0e05825f59a4f670e04661e7a2360b8e39fa20004da63e2812f003323d(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc114041b1663662392e373664cbecf8821f20a78009df2b54077dc4acd4a4f(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__107a105e04f9f1089e314bd557a043d7c27143f765a9e1ea9ee1881882b1c045(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__696a83d1411656063bc2e9712df3268ed2ef2248e55f5547394f8f5e78942d54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3aae9f9b97db34c63c2be162b2b82f9e0ec45cb8225187a2e441c3d9df5fc6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11bd3886ac3007b56aa51fb96bae09bccc9e9cc9c0abd45264540df233a478a8(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnInvoiceUnit.RuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076923c02da9e54ceab543bf61c811c9f8f6d99b2e479b043a782db5a4b4fa76(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3778014062d8d17e79b38d529c3fb3bb66de99f01976014103eaa0ec3100ef9a(
    value: typing.Optional[typing.List[CfnInvoiceUnit.ResourceTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f1928e769bc3f0a10f5fa89984b4cfd7df0a60a619ce30e6135776c65ea23b(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859a6df074320cbe1a9099b42236f7d3759a4ce5419adf8bb3c001155a98ed4f(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8558be1d7f9b75065f54979d9fa00436e977578b77550f4c1d3e32a6b46a4bea(
    *,
    linked_accounts: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4fdf29b8c64b38c209320f998b71b0ce2601c2ac744bde28886f66b3cefdce6(
    *,
    invoice_receiver: builtins.str,
    name: builtins.str,
    rule: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnInvoiceUnit.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Sequence[typing.Union[CfnInvoiceUnit.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tax_inheritance_disabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__029bdd0e6dfff8bc7bf5c49c51804c97e0b1d0537540ea47dc09cd25752a22ff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    buyer_domain: builtins.str,
    buyer_identifier: builtins.str,
    contacts: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.ContactProperty, typing.Dict[builtins.str, typing.Any]]]]],
    einvoice_delivery_enabled: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
    procurement_portal_name: builtins.str,
    purchase_order_retrieval_enabled: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
    supplier_domain: builtins.str,
    supplier_identifier: builtins.str,
    einvoice_delivery_preference: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    procurement_portal_instance_endpoint: typing.Optional[builtins.str] = None,
    procurement_portal_shared_secret: typing.Optional[builtins.str] = None,
    selector: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    test_env_preference: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.TestEnvPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a079b8608c7dac4312263bab6e0f2695f6ed99143c7834d2b550b80ca597ac3(
    resource: _aws_invoicing_2e0dcac4.IProcurementPortalPreferenceRef,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edc77f26abe3d5e4805cbabb0b048b298f6571b03f4cd2c55c76f697cc3a68ca(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68ff8ba49e62e93bb37bdeb3f85558ee79de35d30d2939d243d15ddb1f6a5bfb(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a366d2ee022ece1d7f5bec490a857b7aa51ef31adb97dba0d0c3bab9a70328(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d10d0bb1fcdcbebd2b4dd7222f1ccb9b1383aa534abd4e682d735c76b28d27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b9eea162bd558acac2aa573f0c0e835a04819658a7052a0cab2c488e6bc209(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dedf6ac8d3e460f3f57e46a81176da4201c77eab83727f01d05060f3cfb2189(
    value: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.List[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnProcurementPortalPreference.ContactProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f0630b9d1d9245d17b1b968adf76015952d211333e694d20b0e160742ff7075(
    value: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__825e59078e44b0e1ffad2567eb65e09f52b7597da77a9e14b5e0248590d11061(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45bc22f9a03fb9f6b9c3460c174ea3fcda86a367c9707a671fcb466b64b1ab4f(
    value: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436ee13eb12f20dab661d2c3f4a6a8e816f01bb5fbb2753bff73f1e126c0b3f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659606ff1885d2dd3c4b062d6de991a45d8409f7bbe34249ca9411e37dc7126c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c417dd9f3a753cbe47a2526aae096a2a67b3d29f1ba3eadaed8a15344b6c39a(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1de909d1d637bfdc2e0f32272c29403ff98cbe6a8e0f7a52e6d7a76fb3fc4cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2961867c3abc32458e0d520b0cb27f1d70ae9190cd9b5ffa89c58bef618f1c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2827a48efd72c21d5eb05540e59dde3e013ee0ab32f2d4c77548beaa82532c(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fec4d5f6fcb8ade8160add8328999ef970036b6bd084c98fca41ba08a59938e(
    value: typing.Optional[typing.List[_aws_cdk_0cae9daa.CfnTag]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bc37498ffbb8d3cb91b4f290310eefc777983bea95938ccf28884a0f9310c8e(
    value: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, CfnProcurementPortalPreference.TestEnvPreferenceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618a1e684c24b646908bde431602e86d8fb08e95700960a893509ae60dde79bf(
    *,
    email: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ea2ba7aa7761e8982aa9c2961b13d6808ce833f56badd9547187284b5660bb(
    *,
    connection_testing_method: typing.Optional[builtins.str] = None,
    einvoice_delivery_activation_date: typing.Optional[builtins.str] = None,
    einvoice_delivery_attachment_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    einvoice_delivery_document_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    protocol: typing.Optional[builtins.str] = None,
    purchase_order_data_sources: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.PurchaseOrderDataSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce433272ae1534e13389226c4f92f6df75571b6820bfcee07e03ab330a888482(
    *,
    invoice_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41ac73008d2a40cf91fd6f0d925a51acd1bb18398c6970f991cf31dea38eb01e(
    *,
    einvoice_delivery_document_type: typing.Optional[builtins.str] = None,
    purchase_order_data_source_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c38bcb34298aa687714fe0d6d649b953d3e390e0e43bdfc2fe6ec7873d84f50(
    *,
    buyer_domain: typing.Optional[builtins.str] = None,
    buyer_identifier: typing.Optional[builtins.str] = None,
    procurement_portal_instance_endpoint: typing.Optional[builtins.str] = None,
    procurement_portal_shared_secret: typing.Optional[builtins.str] = None,
    supplier_domain: typing.Optional[builtins.str] = None,
    supplier_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b1800f373ce231d966275771ded23b747067f0d5961aa491d3f555214d3a207(
    *,
    buyer_domain: builtins.str,
    buyer_identifier: builtins.str,
    contacts: typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Sequence[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.ContactProperty, typing.Dict[builtins.str, typing.Any]]]]],
    einvoice_delivery_enabled: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
    procurement_portal_name: builtins.str,
    purchase_order_retrieval_enabled: typing.Union[builtins.bool, _aws_cdk_0cae9daa.IResolvable],
    supplier_domain: builtins.str,
    supplier_identifier: builtins.str,
    einvoice_delivery_preference: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.EinvoiceDeliveryPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    procurement_portal_instance_endpoint: typing.Optional[builtins.str] = None,
    procurement_portal_shared_secret: typing.Optional[builtins.str] = None,
    selector: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.ProcurementPortalPreferenceSelectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_0cae9daa.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    test_env_preference: typing.Optional[typing.Union[_aws_cdk_0cae9daa.IResolvable, typing.Union[CfnProcurementPortalPreference.TestEnvPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
