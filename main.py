#!/usr/bin/env python
from zone_records_json.main import (
    create_records_zone,
    providerAwsFactory,
    s3BackendFactory,
)
from cdktf import App
# from imports.aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.provider import AwsProviderAssumeRole

REGION = "ap-southeast-1"
ZONE_NAME = "ducloi.local"
ZONE_NAME_UNDERSCORE = ZONE_NAME.replace(".", "_")
ASSUME_ROLE_ARN = f"arn:aws:iam::849864070883:role/{ZONE_NAME_UNDERSCORE}"
ZONE_ID = "Z04310523PE6MMFQSSP6Z"
TF_STATE_BUCKET = "tf-state-ak-dns-prod"

app = App()

create_records_zone(
    path="groupedRecords.json",
    app=app,
    provider=providerAwsFactory(
        region=REGION,
        assume_role=[AwsProviderAssumeRole(role_arn=ASSUME_ROLE_ARN)]),
    maxGroupSize=100,
    zoneId=ZONE_ID,
    s3BackendRecord=s3BackendFactory(
        region=REGION,
        role_arn=ASSUME_ROLE_ARN,
        bucket=TF_STATE_BUCKET,
        keyPath=f"terraform/{ZONE_NAME}"),
    route53stack="route53",
)

app.synth()
