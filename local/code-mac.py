# From https://huggingface.co/docs/diffusers/optimization/mps

from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("../stable-diffusion-v1-4")
pipe = pipe.to("mps")
pipe.safety_checker = lambda images, clip_input: (images, False)

prompt = "a photo of an astronaut riding a horse on mars"

# First-time "warmup" pass (see explanation above)
_ = pipe(prompt, num_inference_steps=1)

# Results match those from the CPU device after the warmup pass.
image = pipe(prompt).images[0]

image.save("output/output-mac.png")
