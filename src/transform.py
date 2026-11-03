import pandas as pd

INPUT = "data/processed/carburants_2021_2025.csv"
OUTPUT = "data/processed/carburants_clean.csv"

print("Lecture du fichier...")

df = pd.read_csv(
    INPUT,
    usecols=["date", "carburant", "prix"]
)

df["date"] = pd.to_datetime(df["date"])

# Conservation des prix réalistes
df = df[(df["prix"] >= 1) & (df["prix"] <= 3)]

print("Lignes conservées :", len(df))

df["mois"] = df["date"].dt.to_period("M")

monthly = (
    df.groupby(["mois", "carburant"])["prix"]
      .mean()
      .reset_index()
)

monthly["mois"] = monthly["mois"].astype(str)

monthly.to_csv(OUTPUT, index=False)

print(monthly.head())
print(monthly.shape)