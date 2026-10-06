using Amazon.CDK;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.S3.Deployment;
using Constructs;

namespace WebsiteProject
{
    public class WebsiteProjectStack : Stack
    {
        internal WebsiteProjectStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // The code that defines your stack goes here
            //ich habe hier bucket erstellt
            var siteBucket = new Bucket(this, "StaticWebsiteBucket", new BucketProps
            {
                BucketName = "Website-with-CDK",
                WebsiteIndexDocument = "index.html",
                PublicReadAccess = true,
                BlockPublicAccess = BlockPublicAccess.BLOCK_ACL,
                RemovalPolicy = RemovalPolicy.DESTROY,
                AutoDeleteObjects = true
            });

            //HTML-Dateien aus dem Ordner "site" in den S3-Bucket hochladen

            new BucketDeployment(this, "DeployWebsite", new BucketDeploymentProps
            {
                Sources = new[] { Source.Asset("./site") },
                DestinationBucket = siteBucket
            });

            //S3 url im terminal ausgeben

            new CfnOutput(this, "WebsiteURL", new CfnOutputProps
            {
                Value = siteBucket.BucketWebsiteUrl,
                Description = "URL of the static website hosted on S3",
                ExportName = "WebsiteURL"
            });




        }
    }
}
