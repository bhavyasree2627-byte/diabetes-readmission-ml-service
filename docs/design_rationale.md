# Design Rationale

## Repository Structure

The project follows a modular structure to separate responsibilities across data ingestion, feature engineering, model training, prediction, API serving, utilities, and testing. This separation improves maintainability, testability, and future scalability.

## Model Selection

A Random Forest Classifier was selected because it provides strong baseline performance for tabular healthcare datasets, handles nonlinear relationships, requires minimal feature scaling, and is relatively robust to noisy features.

## Feature Selection

A subset of numerical utilization-based features was selected to build an initial production-ready baseline model. These features include hospital stay duration, medication counts, laboratory procedures, and encounter history.

## Artifact Strategy

The trained model is serialized using Joblib and stored under the artifacts directory. A metadata file is maintained to track model version, training accuracy, and training date. This provides a simple versioning mechanism and supports future model registration workflows.

## API Design

FastAPI was selected because it provides high performance, automatic OpenAPI documentation, request validation through Pydantic models, and a lightweight deployment model suitable for ML inference services.

## Testing Strategy

Pytest is used to validate endpoint behavior and prediction functionality. Tests ensure the service responds correctly and returns expected output structures.

## Deployment Strategy

Docker was used to package the application and its dependencies into a reproducible container. This allows the service to run consistently across environments.

## Trade-Offs

The primary focus of this assignment was production readiness, reproducibility, and maintainability rather than maximizing model accuracy. More sophisticated models and hyperparameter tuning could improve performance but would increase complexity.
