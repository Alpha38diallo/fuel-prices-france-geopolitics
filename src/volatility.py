import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/carburants_2021_2025.csv")

volatilite = (
    df.groupby("carburant")["prix"]
      .std()
      .sort_values(ascending=False)
)

print("\n=== VOLATILITÉ DES CARBURANTS ===")
print(volatilite)

plt.figure(figsize=(8,5))

volatilite.plot(
    kind="bar",
    color="orange"
)

plt.title("Volatilité des prix par carburant")
plt.xlabel("Carburant")
plt.ylabel("Écart-type")

plt.tight_layout()

plt.savefig("outputs/volatilite_carburants.png")

plt.show()

print("\nGraphique créé : outputs/volatilite_carburants.png")