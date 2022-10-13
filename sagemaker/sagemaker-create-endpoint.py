import os
from pathlib import Path

from sagemaker.huggingface.model import HuggingFaceModel

CURR_PATH = Path(os.path.dirname(os.path.realpath(__file__)))

with open(CURR_PATH / ".." / "terraform" / "sagemaker-role-arn.txt", "r") as f:
    sagemaker_role = f.read()

with open(CURR_PATH / ".." / "terraform" / "bucket-name.txt", "r") as f:
    bucket_name = f.read()


# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
    model_data=f"s3://{bucket_name}/sdv1-4_model.tar.gz",
    role=sagemaker_role,
    transformers_version="4.12",
    pytorch_version="1.9",
    py_version="py38",
)

# deploy the endpoint endpoint
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.g4dn.xlarge",
    endpoint_name="huggingface-pytorch-inference",
)

with open("endpoint-name.txt", "w") as f:
    f.write(predictor.endpoint_name)
