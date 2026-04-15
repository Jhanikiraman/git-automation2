import boto3, time

def lambda_handler(event, context):
    cf = boto3.client('cloudfront')
    cf.create_invalidation(
        DistributionId="YOUR_DIST_ID",
        InvalidationBatch={
            'Paths': {'Quantity':1,'Items':['/*']},
            'CallerReference': str(time.time())
        }
    )