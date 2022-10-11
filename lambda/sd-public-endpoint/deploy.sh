#!/bin/env bash

set -e

sed 's|<IAM_ROLE_ARN>|'$(cat ../../terraform/lambda-role-arn.txt)'|' .chalice/config-template.json > .chalice/config.json
chalice deploy
