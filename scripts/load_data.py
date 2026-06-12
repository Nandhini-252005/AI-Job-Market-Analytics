import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/jobs.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())