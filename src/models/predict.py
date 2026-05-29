import joblib

from src.utils.logger import logger

model = joblib.load(
    "artifacts/readmission_model.pkl"
)


def predict_readmission(features):

    logger.info(
        f"Prediction request received: {features}"
    )

    prediction = model.predict(
        [features]
    )

    logger.info(
        f"Prediction result: {prediction[0]}"
    )

    return int(prediction[0])