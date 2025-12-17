from flask import Flask, request, jsonify, render_template
from utils import load_model


app = Flask(__name__)


# Load model once at startup
model = load_model()


SPECIES = ["setosa", "versicolor", "virginica"]


@app.route("/")
def home():
return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
data = request.get_json()


if not data or "features" not in data:
return jsonify({"success": False, "error": "Missing 'features' in request"}), 400


features = data["features"]


if len(features) != 4:
return jsonify({"success": False, "error": "Exactly 4 features are required"}), 400


prediction = model.predict([features])[0]
species = SPECIES[int(prediction)]


return jsonify({
"success": True,
"prediction": species
})


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000, debug=True)
