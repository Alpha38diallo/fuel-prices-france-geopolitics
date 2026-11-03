import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/carburants_2021_2025.csv")

result = (
    df.groupby("carburant")["prix"]
      .mean()
      .sort_values(ascending=False)
)

print(result)

plt.figure(figsize=(8,5))
result.plot(kind="bar", color="seagreen")

plt.title("Prix moyen par carburant (2021-2025)")
plt.xlabel("Carburant")
plt.ylabel("Prix moyen (€ / L)")

plt.tight_layout()

plt.savefig("outputs/prix_moyen_carburant.png")
plt.show()