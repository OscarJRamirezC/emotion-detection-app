from flask import Flask, request, jsonify
from model.emoticon_model import load_model, predict_emotion

app = Flask(__name__)

model = load_model()

@app.route("/predict-emotion/", methods=["POST"])
def predict():
    data = request.get_json()
    if "image" not in data:
        return jsonify({"error": "No image provided"}), 400
    
    image_data = data["image"]
    emotion = predict_emotion(model, image_data)
    return jsonify({"emotion": emotion})

if __name__ == "__main__":
    app.run(port=8000, debug=True)
