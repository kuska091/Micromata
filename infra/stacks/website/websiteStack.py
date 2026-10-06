from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
)
from constructs import Construct

class WebsiteStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, bucket_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. S3-Bucket für öffentliche Website-Nutzung freischalten
        self.bucket = s3.Bucket(
            self, 
            "MyWebsiteBucket",
            bucket_name=bucket_name,
            website_index_document="index.html",
            public_read_access=True,
            # Hier lag das Problem: Wir deaktivieren das Blockieren öffentlicher Policies für diesen Bucket
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=False,
                block_public_policy=False,
                ignore_public_acls=False,
                restrict_public_buckets=False
            ),
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # 2. Dateien aus dem Ordner "./site" hochladen
        s3deploy.BucketDeployment(
            self,
            "DeployWebsite",
            sources=[s3deploy.Source.asset("./site")],
            destination_bucket=self.bucket
        )