# app.py
from flask import Flask, request, jsonify
from utils import load_model, predict_species

app = Flask(__name__)

# Load model once
model = load_model()

@app.route("/")
def home():
    return "🌸 Iris Classifier API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Missing 'features' key in JSON"}), 400

    features = data["features"]
    if len(features) != 4:
        return jsonify({"error": "Features must be a list of 4 numbers"}), 400

    species = predict_species(model, features)
    return jsonify({"prediction": species})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
