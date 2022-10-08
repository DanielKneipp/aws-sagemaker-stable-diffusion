from sagemaker.huggingface.model import HuggingFaceModel


# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
    model_data="s3://dkneipp-sagemaker/sdv1-4_model.tar.gz", # path to your model and script
    role='arn:aws:iam::????????????:role/sagemaker-admin',   # iam role with permissions to create an Endpoint
    transformers_version="4.12",                             # transformers version used
    pytorch_version="1.9",                                   # pytorch version used
    py_version="py38",                                       # python version used
)

# deploy the endpoint endpoint
predictor = huggingface_model.deploy(
    initial_instance_count=1, instance_type="ml.g4dn.xlarge"
)

with open('endpoint-name.txt', 'w') as f:
    f.write(predictor.endpoint_name)
