from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from model.emoticon_model import load_model, predict_emotion
from utils.imagen_utils import preprocess_image

app = FastAPI()

model = load_model()

@app.post("/predict-emotion/")
async def predict_emotion_endpoint(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        processed_image = preprocess_image(image_data)
        prediction = predict_emotion(model, processed_image)
        return JSONResponse(content={"emotion": prediction})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
