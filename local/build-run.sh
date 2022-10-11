#!/usr/bin/env bash
set -e

cd ../
docker build -t stable-difusion:latest -f local/Dockerfile .
cd local/

docker run --gpus=all -v "$(pwd)/output:/app/output" stable-difusion:latest
