#!/usr/bin/env bash

set -e

BUCKET_NAME="$(cat ../terraform/bucket-name.txt)"

aws s3 rm "s3://${BUCKET_NAME}/sdv1-4_model.tar.gz"
