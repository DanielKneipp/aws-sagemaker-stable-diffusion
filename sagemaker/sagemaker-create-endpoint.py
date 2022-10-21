from sagemaker.huggingface.model import HuggingFaceModel

import conf

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(**conf.MODEL_PARAMS)

# deploy the endpoint endpoint
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.g4dn.xlarge",
    endpoint_name=conf.RESOURCE_NAME,
)
