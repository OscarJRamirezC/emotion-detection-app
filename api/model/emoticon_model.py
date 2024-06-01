import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import base64
from io import BytesIO
from PIL import Image

def load_model():
    model = tf.keras.models.load_model('emotion_detection_model.h5')
    return model

def predict_emotion(model, image_data):
    img = Image.open(BytesIO(base64.b64decode(image_data)))
    img = img.resize((150, 150))
    img = img.convert('RGB')  
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=-1)  # Add the channel dimension
    
    predictions = model.predict(img)
    emotion = np.argmax(predictions)
    emotions = ['Disgust','Angry', 'Happy', 'Fear' ,'Neutral', 'Surprise', 'Sad']
    return emotions[emotion]
