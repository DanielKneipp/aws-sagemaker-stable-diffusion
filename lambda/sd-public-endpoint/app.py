import os
from urllib.parse import unquote

import boto3
from botocore.config import Config
from chalice import Chalice, Response
from sagemaker.session import Session
from essential_generators import DocumentGenerator
from sagemaker.huggingface.model import HuggingFacePredictor

ENDPOINT_NAME = os.environ["ENDPOINT_NAME"]
BODY_TEMPLATE = '<html><head></head><body><img src="data:image/png;base64,IMAGE"/><br><h3>PROMPT</h3></body></html>'

config = Config(read_timeout=30, retries={"max_attempts": 0})
sagemaker_runtime_client = boto3.client("sagemaker-runtime", config=config)
sagemaker_session = Session(sagemaker_runtime_client=sagemaker_runtime_client)
predictor = HuggingFacePredictor(
    endpoint_name=ENDPOINT_NAME, sagemaker_session=sagemaker_session
)
sentence_generator = DocumentGenerator()

app = Chalice(app_name="sd-public-endpoint")


def make_response(res):
    return Response(
        body=BODY_TEMPLATE.replace("IMAGE", res["data"]).replace(
            "PROMPT", res["prompt"]
        ),
        status_code=200,
        headers={"Content-Type": "text/html", "prompt": res["prompt"]},
    )


@app.route("/")
def index():
    return "Online Stable Diffusion"


def inference(prompt=""):
    data = {"prompt": prompt} if prompt else {}

    print(f"Starting inference with {data}")
    res = predictor.predict(data=data)
    print("Inference completed")

    return res


@app.route("/inference/{prompt}")
def inference_with_prompt(prompt):
    prompt = unquote(prompt)
    res = inference(prompt)
    return make_response(res)


@app.route("/inference")
def inference_without_prompt():
    res = inference(sentence_generator.sentence())
    return make_response(res)


@app.route("/inference/default")
def inference_without_prompt():
    res = inference("a photo of an astronaut riding a horse on mars")
    return make_response(res)
