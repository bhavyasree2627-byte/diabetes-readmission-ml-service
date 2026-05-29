from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PatientRequest(BaseModel):
    age: int
    num_medications: int
    time_in_hospital: int


@app.get("/")
def home():
    return {
        "status": "healthy",
        "service": "diabetes-readmission-ml-service"
    }


@app.post("/predict")
def predict(request: PatientRequest):

    score = (
        request.age
        + request.num_medications
        + request.time_in_hospital
    )

    prediction = 1 if score > 50 else 0

    return {
        "prediction": prediction,
        "readmitted": bool(prediction)
    }