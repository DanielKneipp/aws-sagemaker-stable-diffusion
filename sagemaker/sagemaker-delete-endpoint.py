import sys

import boto3
from sagemaker.huggingface.model import HuggingFacePredictor, HuggingFaceModel

import conf

sagemaker_session = boto3.client("sagemaker")

predictor_delete_ok = False

try:
    predictor = HuggingFacePredictor(endpoint_name=conf.RESOURCE_NAME)
    predictor.delete_endpoint()
    predictor_delete_ok = True
except Exception as e:
    print(
        f"Predictor deletion failed: {e} "
        "Trying to delete the model and endpoint configuration directly",
        file=sys.stderr,
    )

if predictor_delete_ok:
    exit(0)

try:
    model = HuggingFaceModel(**conf.MODEL_PARAMS)
    model.delete_model()
except Exception as e:
    print(f"Model deletion failed: {e}", file=sys.stderr)

try:
    sagemaker_session.delete_endpoint_config(EndpointConfigName=conf.RESOURCE_NAME)
except Exception as e:
    print(f"Endpoint config deletion failed: {e}", file=sys.stderr)
