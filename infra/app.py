#!/usr/bin/env python3.12
import aws_cdk as cdk
from stacks.website.websiteStack import WebsiteStack

app = cdk.App()

websiteStack = WebsiteStack(
    app, 
    "WebsiteStack",
    bucket_name="mbulut-website-demo-2026"
)

## stack 2

## stack 3

## stack 4

# Gibt den direkt anklickbaren Website-URL-Link im Terminal aus:
cdk.CfnOutput(
    websiteStack, 
    "WebsiteURL", 
    value=websiteStack.bucket.bucket_website_url
)

app.synth()
