import sqlite3
import pandas as pd

INPUT_FILE = "data/processed/carburants_clean.csv"
DB_FILE = "data/processed/carburants.db"

print("Lecture des données transformées...")

df = pd.read_csv(INPUT_FILE)

print(f"{len(df)} lignes à charger.")

conn = sqlite3.connect(DB_FILE)

df.to_sql(
    "carburants",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(f"Base SQLite créée : {DB_FILE}")
print("Chargement terminé.")