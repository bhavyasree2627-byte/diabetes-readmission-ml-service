import joblib

model = joblib.load("artifacts/readmission_model.pkl")


def predict_readmission(features):
    prediction = model.predict([features])
    return int(prediction[0])