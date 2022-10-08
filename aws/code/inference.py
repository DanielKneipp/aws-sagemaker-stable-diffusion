import io
import base64

import PIL
from diffusers import StableDiffusionPipeline

PROMPT = "a photo of an astronaut riding a horse on mars. VFX, octane renderer"

def model_fn(model_dir):
    pipe = StableDiffusionPipeline.from_pretrained(model_dir)
    pipe = pipe.to("cuda")
    return pipe

def predict_fn(data, pipe):
    prompt = data.pop("prompt", PROMPT)

    print('Starting inference')
    image: PIL.Image.Image = pipe(prompt).images[0]

    buffered = io.BytesIO()
    image.save(buffered, format='JPEG')
    return {'data': base64.b64encode(buffered.getvalue()).decode('utf-8'), 'prompt': prompt}
