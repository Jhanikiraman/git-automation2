import boto3
import os
import time


def lambda_handler(event, context):
    distribution_id = os.environ["DISTRIBUTION_ID"]
    cf = boto3.client("cloudfront")

    response = cf.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            "Paths": {
                "Quantity": 1,
                "Items": ["/*"],
            },
            "CallerReference": str(time.time()),
        },
    )

    invalidation_id = response["Invalidation"]["Id"]
    status = response["Invalidation"]["Status"]
    print(f"Invalidation created: {invalidation_id} — status: {status}")

    return {
        "statusCode": 200,
        "body": f"Invalidation {invalidation_id} created successfully",
    }