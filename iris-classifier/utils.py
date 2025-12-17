import joblib
import numpy as np


def load_model(model_path="model.joblib"):
return joblib.load(model_path)

def predict_species(model, features):
    prediction = model.predict([features])[0]
    return int(prediction)   # 👈 convert numpy.int64 → Python int





