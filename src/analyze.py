import pandas as pd

# Lecture des données
df = pd.read_csv("data/processed/carburants_2021_2025.csv")

# Conversion date
df["date"] = pd.to_datetime(df["date"])
df["annee"] = df["date"].dt.year
df["mois"] = df["date"].dt.to_period("M")

print("\n=== PRIX MOYENS PAR ANNÉE ===")
print(
    df.groupby("annee")["prix"]
    .mean()
    .round(3)
)

print("\n=== PRIX MOYENS PAR CARBURANT ===")
print(
    df.groupby("carburant")["prix"]
    .mean()
    .sort_values(ascending=False)
    .round(3)
)

print("\n=== TOP 10 MOIS LES PLUS CHERS ===")
print(
    df.groupby("mois")["prix"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .round(3)
)

print("\n=== VOLATILITÉ DES CARBURANTS ===")
print(
    df.groupby("carburant")["prix"]
    .std()
    .sort_values(ascending=False)
    .round(3)
)

print("\n=== CARBURANT LE PLUS CHER ===")
print(
    df.groupby("carburant")["prix"]
    .mean()
    .sort_values(ascending=False)
    .head(1)
    .round(3)
)

print("\n=== CARBURANT LE MOINS CHER ===")
print(
    df.groupby("carburant")["prix"]
    .mean()
    .sort_values()
    .head(1)
    .round(3)
)

print("\n=== ANNÉE LA PLUS CHÈRE ===")
print(
    df.groupby("annee")["prix"]
    .mean()
    .sort_values(ascending=False)
    .head(1)
    .round(3)
)

print("\n=== ANNÉE LA MOINS CHÈRE ===")
print(
    df.groupby("annee")["prix"]
    .mean()
    .sort_values()
    .head(1)
    .round(3)
)