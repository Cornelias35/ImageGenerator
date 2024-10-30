# ImageGenerator

Stable Diffusion pipeline used for creating image locally. For API, FastAPI used and inside of it, "/generate_image" path used for accessing the pipeline. The function takes prompt and return image base64 string format.

## Before Run the Code: 

Create new folder and create virtual Python environtment by using :

python -m venv .venv

After that, activate the python environment ad run pip install "fastapi[standard]"

By this, we initialize our environment and ready to work it.

## Installing Necessary Libraries

To be able to create image, we need to download
* PyTorch (If Nvidia GPU owned, download supported version for cuda)
* HuggingFace Diffusers
* HuggingFace Transformers
* HuggingFace Accelerate (which improves speed for the execution of pipeline)

## main.py

It contains FastAPI code to initialize server and create necesssary functions. "/generate_imae" path contains pipeline functionality and used to create images.

## ImageGenerator.ipynb

This is sample code that takes prompt as input and send it to FastAPI server. The file is .ipynb because of ease of use.




