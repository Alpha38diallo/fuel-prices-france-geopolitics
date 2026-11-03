import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path

DATA_DIR = Path("data/raw")
OUTPUT = Path("data/processed/carburants_2021_2025.csv")

fuel_types = ["Gazole", "SP95", "SP98", "E10"]

rows = []

xml_files = sorted(DATA_DIR.glob("PrixCarburants_annuel_*.xml"))

for xml_file in xml_files:
    print(f"Lecture : {xml_file.name}")

    context = ET.iterparse(xml_file, events=("end",))

    current_station = {}

    for event, elem in context:

        if elem.tag == "pdv":
            current_station = {
                "cp": elem.attrib.get("cp"),
                "latitude": elem.attrib.get("latitude"),
                "longitude": elem.attrib.get("longitude"),
            }

        elif elem.tag == "prix":

            fuel = elem.attrib.get("nom")

            if fuel in fuel_types:
                valeur = float(elem.attrib.get("valeur"))

                # Archives 2021 : prix stockés en millièmes
                # Archives 2022-2025 : prix déjà en euros
                if valeur > 10:
                   valeur = valeur / 1000

                rows.append({
                    "date": elem.attrib.get("maj"),
                    "carburant": fuel,
                    "prix": valeur,
                    "cp": current_station.get("cp"),
                    "latitude": current_station.get("latitude"),
                    "longitude": current_station.get("longitude")
                })

            elem.clear()

df = pd.DataFrame(rows)

OUTPUT.parent.mkdir(exist_ok=True)

df.to_csv(OUTPUT, index=False)

print("\nTerminé")
print(df.head())
print(df.shape)
print(f"\nFichier créé : {OUTPUT}")