#!/usr/bin/perl

import boto3;

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
        print(bucket.name)


import boto3
s3 = boto3.resource('s3')
s3.Bucket('demouploadfile').upload_file('demofile.pdf', "demo3")
