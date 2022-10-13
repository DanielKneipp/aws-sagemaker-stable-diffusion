import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "./stable-diffusion-v1-4", torch_dtype=torch.float16, revision="fp16"
)
pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars. VFX, octane renderer"

with torch.autocast("cuda"):
    image = pipe(prompt).images[0]

image.save("output/output.png")
