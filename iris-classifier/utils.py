import joblib
import numpy as np

def load_model(model_path="model.joblib"):
    model = joblib.load(model_path)
    return model

def predict_species(model, features):
    prediction = model.predict([features])[0]
    return int(prediction)   # 👈 convert numpy.int64 → Python int

