import os
from sagemaker.huggingface.model import HuggingFacePredictor

with open('endpoint-name.txt', 'r') as f:
    endpoint_name = f.read()

predictor = HuggingFacePredictor(endpoint_name=endpoint_name)
predictor.delete_model()
predictor.delete_endpoint()

os.remove('endpoint-name.txt')
