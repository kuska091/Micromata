using Amazon.CDK;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.S3.Deployment;
using Constructs;

namespace Infra
{
    public class InfraStack : Stack
    {
        internal InfraStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // 1. Deinen S3-Bucket erstellen
            var myBucket = new Bucket(this, "MyFirstBucketConstruct", new BucketProps
            {
                BucketName = "mbulut-demo-bucket-2026",
                RemovalPolicy = RemovalPolicy.DESTROY,
                AutoDeleteObjects = true
            });

            // 2. Tagebuch aus dem Ordner "montag" hochladen
            new BucketDeployment(this, "DeployMontagTagebuch", new BucketDeploymentProps
            {
                Sources = new[] { Source.Asset("/Users/mbulut/Documents/Micromata/montag") },
                DestinationBucket = myBucket
            });
        }
    }
}