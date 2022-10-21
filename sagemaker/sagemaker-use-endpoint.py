import base64
from pathlib import Path

from sagemaker.huggingface.model import HuggingFacePredictor

import conf

predictor = HuggingFacePredictor(endpoint_name=conf.RESOURCE_NAME)

data = {"prompt": "darth vader dancing on top of the millennium falcon"}

res = predictor.predict(data=data)

print(f'prompt used: {res["prompt"]}')
image_bytes = base64.b64decode(res["data"])


Path("output/").mkdir(exist_ok=True)
with open("output/image.jpg", "wb") as f:
    f.write(image_bytes)
