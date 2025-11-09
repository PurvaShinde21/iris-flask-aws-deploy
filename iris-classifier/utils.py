import joblib

def load_model(model_path="model.joblib"):
    model = joblib.load(model_path)
    return model

def predict_species(model, features):
    prediction = model.predict([features])
    return prediction[0]
