r'''
# AWS::ServerlessRepo Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_serverlessrepo as serverlessrepo
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ServerlessRepo construct libraries](https://constructs.dev/search?q=serverlessrepo)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ServerlessRepo resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ServerlessRepo.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ServerlessRepo](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ServerlessRepo.html).

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
    import aws_cdk.interfaces.aws_serverlessrepo as _aws_serverlessrepo_a87f50ed
    import constructs as _constructs_77d1e7e8
else:

    _aws_cdk_0cae9daa = _LazyImport("aws_cdk")
    _aws_serverlessrepo_a87f50ed = _LazyImport("aws_cdk.interfaces.aws_serverlessrepo")
    _constructs_77d1e7e8 = _LazyImport("constructs")


@jsii.implements(_aws_cdk_0cae9daa.IInspectable, _aws_serverlessrepo_a87f50ed.IApplicationRef)
class CfnApplication(
    _aws_cdk_0cae9daa.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_serverlessrepo.CfnApplication",
):
    '''Resource type definition for an AWS Serverless Application Repository application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html
    :cloudformationResource: AWS::ServerlessRepo::Application
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_serverlessrepo as serverlessrepo
        
        cfn_application = serverlessrepo.CfnApplication(self, "MyCfnApplication",
            author="author",
            description="description",
            name="name",
        
            # the properties below are optional
            home_page_url="homePageUrl",
            labels=["labels"],
            license_body="licenseBody",
            readme_body="readmeBody",
            semantic_version="semanticVersion",
            source_code_url="sourceCodeUrl",
            spdx_license_id="spdxLicenseId",
            template_body="templateBody"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        author: builtins.str,
        description: builtins.str,
        name: builtins.str,
        home_page_url: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        license_body: typing.Optional[builtins.str] = None,
        readme_body: typing.Optional[builtins.str] = None,
        semantic_version: typing.Optional[builtins.str] = None,
        source_code_url: typing.Optional[builtins.str] = None,
        spdx_license_id: typing.Optional[builtins.str] = None,
        template_body: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServerlessRepo::Application``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param author: The name of the author publishing the app.
        :param description: The description of the application.
        :param name: The name of the application.
        :param home_page_url: A URL with more information about the application.
        :param labels: Labels to improve discovery of apps in search results.
        :param license_body: A local text file that contains the license of the app.
        :param readme_body: A text readme file in Markdown language that contains a more detailed description of the application.
        :param semantic_version: The semantic version of the application.
        :param source_code_url: A link to a public repository for the source code of your application.
        :param spdx_license_id: A valid identifier from https://spdx.org/licenses/.
        :param template_body: The local raw packaged AWS SAM template file of your application.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__39de71b5461f635c465d2a66c016d561c0e62a82489630daf1b6dba5053eb2fb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            author=author,
            description=description,
            name=name,
            home_page_url=home_page_url,
            labels=labels,
            license_body=license_body,
            readme_body=readme_body,
            semantic_version=semantic_version,
            source_code_url=source_code_url,
            spdx_license_id=spdx_license_id,
            template_body=template_body,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnApplication")
    @builtins.classmethod
    def is_cfn_application(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnApplication.

        :param x: -
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d6eaeafdd7fe004d04410a5b15210e2aab591957d62fa741094c47922d09a787)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnApplication", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_aws_cdk_0cae9daa.TreeInspector") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__03c757b8b9078321692b64cdbe9b0516d375c27a8229c8c3a739a1cbf4f1a3bd)
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
            type_hints = cached_type_hints(_typecheckingstub__5e12601aeff39229929b45ce43aebfa12ec76aa772deefc36b732d08da3257ec)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "_aws_serverlessrepo_a87f50ed.ApplicationReference":
        '''A reference to a Application resource.'''
        return typing.cast("_aws_serverlessrepo_a87f50ed.ApplicationReference", jsii.get(self, "applicationRef"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the application.

        :cloudformationAttribute: ApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The date and time this resource was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrIsVerifiedAuthor")
    def attr_is_verified_author(self) -> "_aws_cdk_0cae9daa.IResolvable":
        '''Whether the author of this application has been verified.

        :cloudformationAttribute: IsVerifiedAuthor
        '''
        return typing.cast("_aws_cdk_0cae9daa.IResolvable", jsii.get(self, "attrIsVerifiedAuthor"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="cfnPropertyNames")
    def _cfn_property_names(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "cfnPropertyNames"))

    @builtins.property
    @jsii.member(jsii_name="author")
    def author(self) -> builtins.str:
        '''The name of the author publishing the app.'''
        return typing.cast(builtins.str, jsii.get(self, "author"))

    @author.setter
    def author(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__bc8c3f552a7438c21eafef8b0e43abecebdd5821ba5ca507ac5da374e39b8d34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "author", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9910b85b41a651c7376a10ea4ad990585535596a1af34d42c7b28caf817e5db1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__96ac8ae4a03288f1d108f3b920e712963af2f9842ddc0258307e5c02716528d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="homePageUrl")
    def home_page_url(self) -> typing.Optional[builtins.str]:
        '''A URL with more information about the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homePageUrl"))

    @home_page_url.setter
    def home_page_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__9491193b759a5c867754a2fca2d1fa86ac9fec2ef02f3773ce8fa76fb81a4c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homePageUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Labels to improve discovery of apps in search results.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__eabdf636bbe95db771d1011ca34b92b42aadd3c258b46b55816a2f1c8d5f4405)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licenseBody")
    def license_body(self) -> typing.Optional[builtins.str]:
        '''A local text file that contains the license of the app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseBody"))

    @license_body.setter
    def license_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__0dd114d6a7c8c90fbafb5fe5325822a2e7c6c2f329a4bb94e6388d862e7225a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseBody", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readmeBody")
    def readme_body(self) -> typing.Optional[builtins.str]:
        '''A text readme file in Markdown language that contains a more detailed description of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readmeBody"))

    @readme_body.setter
    def readme_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__d82d24714ae68bc3ff62f053ad913f853ea3efe34071a4da052ea59f779d74a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readmeBody", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="semanticVersion")
    def semantic_version(self) -> typing.Optional[builtins.str]:
        '''The semantic version of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "semanticVersion"))

    @semantic_version.setter
    def semantic_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__893f570a5570e775fb89a26dc4bbcd48eabd6365a61eeb01fe8b85d73fa27531)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "semanticVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceCodeUrl")
    def source_code_url(self) -> typing.Optional[builtins.str]:
        '''A link to a public repository for the source code of your application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceCodeUrl"))

    @source_code_url.setter
    def source_code_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__44adbd938bbc00c80db2841716fb0cbd589da0203b73dc67138de1bece5baea2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceCodeUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spdxLicenseId")
    def spdx_license_id(self) -> typing.Optional[builtins.str]:
        '''A valid identifier from https://spdx.org/licenses/.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spdxLicenseId"))

    @spdx_license_id.setter
    def spdx_license_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__2131f87db6f45bf5f24176cf5b4889472409e25f7ce08856d75361c8824571ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spdxLicenseId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> typing.Optional[builtins.str]:
        '''The local raw packaged AWS SAM template file of your application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7ee4001d68a2d0805a28aace5df34f7a5db7072caee34d1de63db4cf2550a136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_serverlessrepo.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "author": "author",
        "description": "description",
        "name": "name",
        "home_page_url": "homePageUrl",
        "labels": "labels",
        "license_body": "licenseBody",
        "readme_body": "readmeBody",
        "semantic_version": "semanticVersion",
        "source_code_url": "sourceCodeUrl",
        "spdx_license_id": "spdxLicenseId",
        "template_body": "templateBody",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        author: builtins.str,
        description: builtins.str,
        name: builtins.str,
        home_page_url: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        license_body: typing.Optional[builtins.str] = None,
        readme_body: typing.Optional[builtins.str] = None,
        semantic_version: typing.Optional[builtins.str] = None,
        source_code_url: typing.Optional[builtins.str] = None,
        spdx_license_id: typing.Optional[builtins.str] = None,
        template_body: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param author: The name of the author publishing the app.
        :param description: The description of the application.
        :param name: The name of the application.
        :param home_page_url: A URL with more information about the application.
        :param labels: Labels to improve discovery of apps in search results.
        :param license_body: A local text file that contains the license of the app.
        :param readme_body: A text readme file in Markdown language that contains a more detailed description of the application.
        :param semantic_version: The semantic version of the application.
        :param source_code_url: A link to a public repository for the source code of your application.
        :param spdx_license_id: A valid identifier from https://spdx.org/licenses/.
        :param template_body: The local raw packaged AWS SAM template file of your application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_serverlessrepo as serverlessrepo
            
            cfn_application_props = serverlessrepo.CfnApplicationProps(
                author="author",
                description="description",
                name="name",
            
                # the properties below are optional
                home_page_url="homePageUrl",
                labels=["labels"],
                license_body="licenseBody",
                readme_body="readmeBody",
                semantic_version="semanticVersion",
                source_code_url="sourceCodeUrl",
                spdx_license_id="spdxLicenseId",
                template_body="templateBody"
            )
        '''
        if __debug__:
            type_hints = cached_type_hints(_typecheckingstub__7a326381b99d6bd35c41729bb199fff156f7679687cb68a92987633bc3ce1348)
            check_type(argname="argument author", value=author, expected_type=type_hints["author"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument home_page_url", value=home_page_url, expected_type=type_hints["home_page_url"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument license_body", value=license_body, expected_type=type_hints["license_body"])
            check_type(argname="argument readme_body", value=readme_body, expected_type=type_hints["readme_body"])
            check_type(argname="argument semantic_version", value=semantic_version, expected_type=type_hints["semantic_version"])
            check_type(argname="argument source_code_url", value=source_code_url, expected_type=type_hints["source_code_url"])
            check_type(argname="argument spdx_license_id", value=spdx_license_id, expected_type=type_hints["spdx_license_id"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "author": author,
            "description": description,
            "name": name,
        }
        if home_page_url is not None:
            self._values["home_page_url"] = home_page_url
        if labels is not None:
            self._values["labels"] = labels
        if license_body is not None:
            self._values["license_body"] = license_body
        if readme_body is not None:
            self._values["readme_body"] = readme_body
        if semantic_version is not None:
            self._values["semantic_version"] = semantic_version
        if source_code_url is not None:
            self._values["source_code_url"] = source_code_url
        if spdx_license_id is not None:
            self._values["spdx_license_id"] = spdx_license_id
        if template_body is not None:
            self._values["template_body"] = template_body

    @builtins.property
    def author(self) -> builtins.str:
        '''The name of the author publishing the app.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-author
        '''
        result = self._values.get("author")
        assert result is not None, "Required property 'author' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def home_page_url(self) -> typing.Optional[builtins.str]:
        '''A URL with more information about the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-homepageurl
        '''
        result = self._values.get("home_page_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Labels to improve discovery of apps in search results.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def license_body(self) -> typing.Optional[builtins.str]:
        '''A local text file that contains the license of the app.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-licensebody
        '''
        result = self._values.get("license_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readme_body(self) -> typing.Optional[builtins.str]:
        '''A text readme file in Markdown language that contains a more detailed description of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-readmebody
        '''
        result = self._values.get("readme_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def semantic_version(self) -> typing.Optional[builtins.str]:
        '''The semantic version of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-semanticversion
        '''
        result = self._values.get("semantic_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_code_url(self) -> typing.Optional[builtins.str]:
        '''A link to a public repository for the source code of your application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-sourcecodeurl
        '''
        result = self._values.get("source_code_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spdx_license_id(self) -> typing.Optional[builtins.str]:
        '''A valid identifier from https://spdx.org/licenses/.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-spdxlicenseid
        '''
        result = self._values.get("spdx_license_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''The local raw packaged AWS SAM template file of your application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverlessrepo-application.html#cfn-serverlessrepo-application-templatebody
        '''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
]

publication.publish()

def _typecheckingstub__39de71b5461f635c465d2a66c016d561c0e62a82489630daf1b6dba5053eb2fb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    author: builtins.str,
    description: builtins.str,
    name: builtins.str,
    home_page_url: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    license_body: typing.Optional[builtins.str] = None,
    readme_body: typing.Optional[builtins.str] = None,
    semantic_version: typing.Optional[builtins.str] = None,
    source_code_url: typing.Optional[builtins.str] = None,
    spdx_license_id: typing.Optional[builtins.str] = None,
    template_body: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6eaeafdd7fe004d04410a5b15210e2aab591957d62fa741094c47922d09a787(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c757b8b9078321692b64cdbe9b0516d375c27a8229c8c3a739a1cbf4f1a3bd(
    inspector: _aws_cdk_0cae9daa.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e12601aeff39229929b45ce43aebfa12ec76aa772deefc36b732d08da3257ec(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc8c3f552a7438c21eafef8b0e43abecebdd5821ba5ca507ac5da374e39b8d34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9910b85b41a651c7376a10ea4ad990585535596a1af34d42c7b28caf817e5db1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96ac8ae4a03288f1d108f3b920e712963af2f9842ddc0258307e5c02716528d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9491193b759a5c867754a2fca2d1fa86ac9fec2ef02f3773ce8fa76fb81a4c4a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eabdf636bbe95db771d1011ca34b92b42aadd3c258b46b55816a2f1c8d5f4405(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd114d6a7c8c90fbafb5fe5325822a2e7c6c2f329a4bb94e6388d862e7225a8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d82d24714ae68bc3ff62f053ad913f853ea3efe34071a4da052ea59f779d74a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__893f570a5570e775fb89a26dc4bbcd48eabd6365a61eeb01fe8b85d73fa27531(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44adbd938bbc00c80db2841716fb0cbd589da0203b73dc67138de1bece5baea2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2131f87db6f45bf5f24176cf5b4889472409e25f7ce08856d75361c8824571ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ee4001d68a2d0805a28aace5df34f7a5db7072caee34d1de63db4cf2550a136(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a326381b99d6bd35c41729bb199fff156f7679687cb68a92987633bc3ce1348(
    *,
    author: builtins.str,
    description: builtins.str,
    name: builtins.str,
    home_page_url: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    license_body: typing.Optional[builtins.str] = None,
    readme_body: typing.Optional[builtins.str] = None,
    semantic_version: typing.Optional[builtins.str] = None,
    source_code_url: typing.Optional[builtins.str] = None,
    spdx_license_id: typing.Optional[builtins.str] = None,
    template_body: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
