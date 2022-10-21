import os
from pathlib import Path

CURR_PATH = Path(os.path.dirname(os.path.realpath(__file__)))

with open(CURR_PATH / ".." / "terraform" / "sagemaker-role-arn.txt", "r") as f:
    sagemaker_role = f.read()

with open(CURR_PATH / ".." / "terraform" / "bucket-name.txt", "r") as f:
    bucket_name = f.read()

RESOURCE_NAME = "huggingface-pytorch-inference"

MODEL_PARAMS = {
    "model_data": f"s3://{bucket_name}/sdv1-4_model.tar.gz",
    "name": RESOURCE_NAME,
    "role": sagemaker_role,
    "transformers_version": "4.12",
    "pytorch_version": "1.9",
    "py_version": "py38",
}
