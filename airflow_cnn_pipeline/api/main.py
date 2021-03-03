import os
from fastapi import FastAPI

from get_image import download
from predict import get_score

app = FastAPI()

@app.get("/predict/{img_url:path}")
def get_inference(img_url: str):
    # Get the image file from the URL
    local_path = download.fetch(img_url)

    # Get predicted values
    df = get_score(os.path.join(os.path.dirname(__file__), local_path))
    a = df.to_dict()

    # Return the issue & confidence
    return a
