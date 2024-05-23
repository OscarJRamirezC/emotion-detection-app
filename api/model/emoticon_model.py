from fer import FER
import numpy as np

def load_model():
    model = FER(mtcnn=True)  # Usar el modelo FER con MTCNN para detección de rostros
    return model

def predict_emotion(model, image):
    # El modelo FER espera una imagen en formato RGB
    predictions = model.detect_emotions(image)
    if predictions:
        top_emotion = max(predictions[0]['emotions'], key=predictions[0]['emotions'].get)
        return top_emotion
    return "No se detectaron emociones"
