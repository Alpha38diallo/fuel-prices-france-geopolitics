import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "data/processed/carburants_clean.csv"
)

region_prices = (
    df.groupby("Région")["Prix Gazole"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(12,6))
region_prices.plot(kind="barh")

plt.title("Prix moyen du Gazole par région")
plt.xlabel("Prix moyen (€ / litre)")
plt.ylabel("Région")

plt.tight_layout()

plt.savefig(
    BASE_DIR / "outputs/charts/prix_gazole_par_region.png"
)

print("Graphique créé")