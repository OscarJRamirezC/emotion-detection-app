from fer import FER
import numpy as np

def load_model():
    model = FER(mtcnn=True) 
    return model

def predict_emotion(model, image):
    predictions = model.detect_emotions(image)
    if predictions:
        top_emotion = max(predictions[0]['emotions'], key=predictions[0]['emotions'].get)
        return top_emotion
    return "No se detectaron emociones"
