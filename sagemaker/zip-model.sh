#!/usr/bin/env bash

set -e

BUCKET_NAME="$(cat ../terraform/bucket-name.txt)"

cd ../

cp -r sagemaker/code stable-diffusion-v1-4

cd stable-diffusion-v1-4
rm model.tar.gz 2> /dev/null || true
tar cvf model.tar.gz --use-compress-program=pigz ./*
aws s3 cp model.tar.gz "s3://${BUCKET_NAME}/sdv1-4_model.tar.gz"
rm model.tar.gz

cd ../sagemaker
