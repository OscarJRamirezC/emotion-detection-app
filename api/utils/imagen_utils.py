from PIL import Image
import numpy as np
import io

def preprocess_image(image_data):
    image = Image.open(io.BytesIO(image_data)).convert("RGB") 
    return np.array(image)
