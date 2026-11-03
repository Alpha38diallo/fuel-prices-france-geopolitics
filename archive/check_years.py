import pandas as pd

df = pd.read_csv("data/processed/carburants_2021_2025.csv")

for year in [2021, 2022, 2023, 2024, 2025]:
    tmp = df[df["date"].str.startswith(str(year))]

    print(f"\n===== {year} =====")
    print(tmp["prix"].describe())