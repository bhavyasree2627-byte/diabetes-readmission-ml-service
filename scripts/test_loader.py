import sys
import os

sys.path.append(os.path.abspath("."))

from src.data.data_loader import load_data

df = load_data("data/raw/diabetic_data.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())