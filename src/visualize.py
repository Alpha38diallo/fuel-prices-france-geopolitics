import pandas as pd
import matplotlib.pyplot as plt

# Lecture des données agrégées
df = pd.read_csv("data/processed/carburants_clean.csv")

# Conversion de la date
df["mois"] = pd.to_datetime(df["mois"])

plt.figure(figsize=(14, 7))

# Tracé des carburants
for carburant in ["Gazole", "SP95", "SP98", "E10"]:
    subset = df[df["carburant"] == carburant]

    plt.plot(
        subset["mois"],
        subset["prix"],
        linewidth=2,
        label=carburant
    )

# Guerre Ukraine
plt.axvline(
    pd.Timestamp("2022-02-24"),
    color="red",
    linestyle="--",
    linewidth=2,
    label="Guerre Ukraine"
)

# Israël-Hamas
plt.axvline(
    pd.Timestamp("2023-10-07"),
    color="orange",
    linestyle="--",
    linewidth=2,
    label="Israël-Hamas"
)

plt.title(
    "Evolution des prix des carburants en France (2021-2025)"
)

plt.xlabel("Date")
plt.ylabel("Prix moyen (€ / litre)")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "outputs/evolution_prix_crises.png",
    dpi=300
)

print("Graphique créé : outputs/evolution_prix_crises.png")