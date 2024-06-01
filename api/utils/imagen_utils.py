from PIL import Image
import base64
from io import BytesIO

def decode_image(image_data):
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    return image

def encode_image(image):
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")
