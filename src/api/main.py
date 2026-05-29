from fastapi import FastAPI
from pydantic import BaseModel

from src.models.predict import predict_readmission

app = FastAPI()


class PatientRequest(BaseModel):
    time_in_hospital: int
    num_lab_procedures: int
    num_procedures: int
    num_medications: int
    number_outpatient: int
    number_emergency: int
    number_inpatient: int


@app.get("/")
def home():
    return {
        "status": "healthy",
        "service": "diabetes-readmission-ml-service"
    }


@app.post("/predict")
def predict(request: PatientRequest):

    features = [
        request.time_in_hospital,
        request.num_lab_procedures,
        request.num_procedures,
        request.num_medications,
        request.number_outpatient,
        request.number_emergency,
        request.number_inpatient
    ]

    prediction = predict_readmission(features)

    return {
        "prediction": prediction,
        "readmitted": bool(prediction)
    }