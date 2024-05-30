from flask import Flask, render_template, request, jsonify
import requests
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    if "file" not in request.files:
        return jsonify({"error": "No se ha proporcionado ninguna imagen"}), 400

    image = request.files["file"]
    if not image.filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        return jsonify({"error": "El archivo proporcionado no es una imagen válida"}), 400

    encoded_image = base64.b64encode(image.read()).decode("utf-8")

    response = requests.post("http://localhost:8000/predict-emotion/", json={"image": encoded_image})

    if response.status_code != 200:
        return jsonify({"error": "Error al procesar la solicitud del servidor externo"}), response.status_code

    result = response.json()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
