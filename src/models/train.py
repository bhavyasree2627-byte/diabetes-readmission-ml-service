import joblib
from src.utils.logger import logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.data.data_loader import load_data
from src.features.feature_engineering import prepare_features


def train_model():

    df = load_data("data/raw/diabetic_data.csv")

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    logger.info(f"Model Accuracy: {accuracy:.4f}")

    joblib.dump(
        model,
        "artifacts/readmission_model.pkl"
    )

    logger.info("Model saved successfully")


if __name__ == "__main__":
    train_model()