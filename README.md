# CDK TF Pipline

Remove `assume_role` and `role_arn` as these role already assume in pipeline.

From:
```python
reate_records_zone(
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
```

To:

```python
create_records_zone(
    path="groupedRecords.json",
    app=app,
    provider=providerAwsFactory(
        region=REGION,
        assume_role=None),
    maxGroupSize=100,
    zoneId=ZONE_ID,
    s3BackendRecord=s3BackendFactory(
        region=REGION,
        role_arn=None,
        bucket=TF_STATE_BUCKET,
        keyPath=f"terraform/{ZONE_NAME}"),
    route53stack="route53",
)
```

Change `ref:` from `dev` to `main` in pipeline:
```yml
- name: Checkout route53 records package
      uses: actions/checkout@v5
      with:
        repository: BNGUYENLAB/rdm-route53-records-package
        ref: main
        path: route53-records-package
```