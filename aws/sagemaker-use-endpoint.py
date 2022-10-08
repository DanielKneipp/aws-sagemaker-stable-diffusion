from sagemaker.huggingface.model import HuggingFacePredictor
import base64


with open('endpoint-name.txt', 'r') as f:
    endpoint_name = f.read()

predictor = HuggingFacePredictor(endpoint_name=endpoint_name)

data = {
#   "prompt": "the mesmerizing performances of the leads keep the film grounded and keep the audience riveted"
}

res = predictor.predict(data=data)

print(f'prompt used: {res["prompt"]}')
image_bytes = base64.b64decode(res['data'])

with open('res.txt', 'w') as f:
    f.write(str(res))

with open('image.jpg', 'wb') as f:
    f.write(image_bytes)
