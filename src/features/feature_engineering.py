import pandas as pd


def prepare_features(df):
    """
    Basic feature engineering
    """

    df = df.copy()

    # Create target variable
    df["readmitted_binary"] = df["readmitted"].apply(
        lambda x: 1 if x == "<30" else 0
    )

    # Select simple features
    features = [
        "time_in_hospital",
        "num_lab_procedures",
        "num_procedures",
        "num_medications",
        "number_outpatient",
        "number_emergency",
        "number_inpatient"
    ]

    X = df[features]

    y = df["readmitted_binary"]

    return X, y