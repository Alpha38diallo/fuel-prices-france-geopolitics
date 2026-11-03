import pandas as pd

df = pd.read_csv(
    "data/processed/carburants_2021_2025.csv",
    usecols=["date", "carburant", "prix"]
)

print("Shape :", df.shape)
print("Date min :", df["date"].min())
print("Date max :", df["date"].max())