from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_home_endpoint():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_predict_endpoint():

    payload = {
        "time_in_hospital": 5,
        "num_lab_procedures": 40,
        "num_procedures": 2,
        "num_medications": 15,
        "number_outpatient": 0,
        "number_emergency": 0,
        "number_inpatient": 0
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert "prediction" in body
    assert "readmitted" in body