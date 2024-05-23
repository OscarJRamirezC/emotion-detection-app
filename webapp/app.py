from flask import Flask, render_template, request, jsonify
import requests
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    image = request.files["file"]
    encoded_image = base64.b64encode(image.read()).decode("utf-8")
    response = requests.post("http://localhost:8000/predict-emotion/", json={"image": encoded_image})
    result = response.json()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
