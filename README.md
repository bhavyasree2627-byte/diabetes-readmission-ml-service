# Diabetes Readmission Prediction Service

## Overview

This project predicts whether a patient is likely to be readmitted within 30 days based on hospital encounter information. The solution uses a Random Forest machine learning model trained on the Diabetes 130-US Hospitals dataset and exposes predictions through a FastAPI REST API.

## Dataset

Source: UCI Machine Learning Repository - Diabetes 130-US Hospitals Dataset

Dataset Size:

* 101,766 patient encounters
* 50 attributes

Target Variable:

* readmitted
* Converted to binary classification:

  * 1 = Readmitted within 30 days
  * 0 = Otherwise

## Project Structure

src/

* api
* data
* features
* models
* utils

tests/

* API tests

artifacts/

* Trained model artifact

data/

* Raw dataset

## Model

Algorithm:

* Random Forest Classifier

Features Used:

* time_in_hospital
* num_lab_procedures
* num_procedures
* num_medications
* number_outpatient
* number_emergency
* number_inpatient

Model Accuracy:

* 86.94%

## Running the Application

Create virtual environment:

python3 -m venv venv

Activate:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Train model:

PYTHONPATH=. python src/models/train.py

Run API:

uvicorn src.api.main:app --reload

Swagger:

http://127.0.0.1:8000/docs

## Running Tests

PYTHONPATH=. pytest -v

## Logging

Prediction requests and prediction results are logged using Python logging.

## Future Improvements

* Hyperparameter tuning
* MLflow integration
* Docker deployment
* CI/CD automation
* Drift monitoring

## Assumptions

- Readmitted within 30 days is treated as the positive class.
- Seven numerical features were selected for baseline modeling.
- Random Forest was chosen as the baseline model.
- Missing values were handled during preprocessing.

## Limitations

- Only a subset of available dataset features was used.
- No hyperparameter tuning was performed.
- Model performance may vary on unseen data.
- No model drift monitoring is implemented.

## Design Decisions

- FastAPI was selected to expose REST endpoints.
- Random Forest was selected because it provides strong baseline performance.
- Joblib was used for model serialization.
- Docker was used for containerized deployment.
- Pytest was used for automated testing.