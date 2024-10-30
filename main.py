# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diffusers import DiffusionPipeline
from io import BytesIO
from PIL import Image
import torch
import base64

# Initialize the FastAPI app
app = FastAPI()

# Device setup
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the pipeline
model_id = "stable-diffusion-v1-5/stable-diffusion-v1-5"
pipeline = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=True)
pipeline = pipeline.to(device)



# Define the request model
class PromptRequest(BaseModel):
    prompt: str

# API endpoint to generate image
@app.post("/generate_image")
async def generate_image(request: PromptRequest):
    prompt = request.prompt
    generator = torch.Generator(device).manual_seed(0)

    # Run the Stable Diffusion pipeline
    try:
        image = pipeline(prompt, generator=generator).images[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Image generation failed: " + str(e))

    # Convert the image to base64 for transmission
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Return base64 string of the image
    return {"image": img_str}
