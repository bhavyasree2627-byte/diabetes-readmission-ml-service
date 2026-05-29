import pandas as pd


def prepare_features(df):

    selected_columns = [
        "time_in_hospital",
        "num_lab_procedures",
        "num_procedures",
        "num_medications",
        "number_outpatient",
        "number_emergency",
        "number_inpatient"
    ]

    X = df[selected_columns]

    y = df["readmitted"].apply(
        lambda x: 1 if x == "<30" else 0
    )

    return X, y