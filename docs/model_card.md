# Model Card

## Model Name

Diabetes Readmission Prediction Model

## Model Version

v1

## Algorithm

Random Forest Classifier

## Purpose

Predict whether a patient encounter is likely to result in readmission within 30 days.

## Training Dataset

Diabetes 130-US Hospitals for Years 1999–2008 Dataset

## Features Used

* time_in_hospital
* num_lab_procedures
* num_procedures
* num_medications
* number_outpatient
* number_emergency
* number_inpatient

## Performance

Accuracy: 86.94%

## Intended Use

This model is intended for educational, demonstration, and ML engineering evaluation purposes.

## Limitations

* Uses a limited subset of available dataset features.
* No fairness analysis was performed.
* No drift detection is implemented.
* Not validated for real-world clinical deployment.

## Risks

Prediction errors may occur due to incomplete information, changing patient populations, or differences between training and production data.

## Future Improvements

* Hyperparameter tuning
* Additional feature engineering
* Model monitoring
* Experiment tracking integration
* Fairness and bias evaluation
