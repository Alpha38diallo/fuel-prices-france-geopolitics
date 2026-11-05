# ⛽ Fuel Prices France Geopolitics

## 📖 Présentation

Ce projet analyse l'évolution des prix des carburants en France entre 2021 et 2025 à partir des données publiques gouvernementales.

L'objectif est de comprendre comment les événements économiques, énergétiques et géopolitiques ont influencé les prix des carburants durant cette période.

L'étude s'appuie sur plus de 20 millions d'enregistrements collectés, nettoyés et analysés avec Python.

---

## 🌍 Contexte géopolitique

La période 2021-2025 a été marquée par plusieurs événements majeurs ayant fortement influencé les marchés de l'énergie à l'échelle mondiale.

Parmi les principaux facteurs :

- La reprise économique mondiale après la pandémie de Covid‑19.
- L'augmentation rapide de la demande mondiale en énergie.
- Les tensions persistantes sur les marchés pétroliers internationaux.
- Le déclenchement de la guerre en Ukraine en février 2022.
- Les sanctions économiques et les perturbations des approvisionnements énergétiques européens.
- Les tensions géopolitiques au Moyen‑Orient, notamment entre Israël et l'Iran.
- L'implication des États‑Unis dans les équilibres énergétiques mondiaux et la stabilité des marchés pétroliers.

Ces événements ont contribué à une forte volatilité des prix de l'énergie et ont eu un impact direct sur les prix des carburants observés en France entre 2022 et 2023.

---

## 🎯 Objectifs du projet

- Collecter et exploiter des données publiques sur les carburants.
- Nettoyer et transformer des données brutes XML.
- Étudier l'évolution des prix dans le temps.
- Identifier les périodes de hausse et de baisse.
- Comparer les différents types de carburants.
- Mesurer la volatilité des prix.
- Relier les observations aux événements économiques et géopolitiques majeurs.
- Produire des visualisations facilitant l'interprétation des résultats.

---

## 🛠 Technologies utilisées

- Python
- Pandas
- Matplotlib
- XML
- CSV
- SQL
- Git
- GitHub

---

## 📂 Structure du projet

```text
fuel-prices-france-geopolitics/
│
├── archive/
│   ├── check_data.py
│   ├── check_years.py
│   └── inspect_xml.py
│
├── data/
│   └── processed/
│
├── outputs/
│   ├── evolution_prix_carburants.png
│   ├── prix_moyen_annuel.png
│   ├── prix_moyen_carburant.png
│   ├── top_10_mois_plus_chers.png
│   ├── volatilite_carburants.png
│   └── resume_analyse.txt
│
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── analyze.py
│   ├── visualize.py
│   ├── compare_fuels.py
│   ├── volatility.py
│   ├── region_analysis.py
│   └── load.py
│
├── requirements.txt
└── README.md
```

---

## 📊 Données

### Source

Données ouvertes gouvernementales sur les prix des carburants en France.

### Période étudiée

- 2021
- 2022
- 2023
- 2024
- 2025

### Volume de données

Après nettoyage et transformation :

- Plus de 20 millions d'enregistrements analysés.
- Données consolidées dans un format exploitable pour les analyses statistiques.
- Création d'un jeu de données unique couvrant cinq années d'observation.

---

## ⚙️ Pipeline de traitement

### 1. Extraction

Le script `extract.py` extrait les informations depuis les fichiers XML :

- Date
- Type de carburant
- Prix

### 2. Transformation

Le script `transform.py` :

- Nettoie les données.
- Convertit les dates.
- Supprime les anomalies.
- Prépare les datasets d'analyse.

### 3. Analyse

Le script `analyze.py` calcule :

- Le prix moyen par année.
- Le prix moyen par carburant.
- Les mois les plus chers.
- Les carburants les plus volatils.
- Le carburant le plus cher.
- Le carburant le moins cher.

### 4. Visualisation

Le script `visualize.py` génère les graphiques du projet avec Matplotlib.

---

# 📈 Résultats

## Prix moyens par année

| Année | Prix moyen (€ / litre) |
|--------|--------:|
| 2021 | 1.546 |
| 2022 | 1.851 |
| 2023 | 1.878 |
| 2024 | 1.800 |
| 2025 | 1.722 |

### Analyse

- 2023 est l'année la plus chère de la période étudiée.
- 2021 est l'année la moins chère.
- Une forte augmentation est observée entre 2021 et 2023.
- Les prix diminuent progressivement à partir de 2024.

---

## Prix moyens par carburant

| Carburant | Prix moyen (€ / litre) |
|------------|--------:|
| SP98 | 1.841 |
| SP95 | 1.771 |
| E10 | 1.748 |
| Gazole | 1.710 |

### Analyse

- Le SP98 est le carburant le plus cher.
- Le Gazole est le carburant le moins cher sur la période étudiée.

---

## Top 10 des mois les plus chers

### Top 3

| Mois | Prix moyen (€ / litre) |
|---------|--------:|
| Juin 2022 | 2.122 |
| Mars 2022 | 2.021 |
| Juillet 2022 | 1.986 |

### Analyse

Les périodes les plus coûteuses sont concentrées autour de la crise énergétique mondiale débutée en 2022.

---

## Volatilité des carburants

| Carburant | Écart-type |
|------------|--------:|
| Gazole | 0.189 |
| SP98 | 0.166 |
| E10 | 0.161 |
| SP95 | 0.160 |

### Analyse

Le Gazole est le carburant présentant la plus forte volatilité sur l'ensemble de la période.

---

## 📉 Visualisations

Les graphiques générés sont disponibles dans le dossier :

```text
outputs/
```

Graphiques disponibles :

- Evolution des prix des carburants
- Prix moyen annuel
- Prix moyen par carburant
- Top 10 des mois les plus chers
- Volatilité des carburants

---

## 💡 Principaux enseignements

- Les prix des carburants augmentent fortement entre 2021 et 2023.
- Le pic de prix est observé en juin 2022.
- Le SP98 est le carburant le plus coûteux.
- Le Gazole est le plus volatil.
- Les périodes de hausse coïncident avec des événements géopolitiques majeurs affectant les marchés énergétiques.
- Les résultats illustrent la forte sensibilité du marché français des carburants aux tensions internationales.

---

## ✅ Conclusions

L'analyse met en évidence une relation entre les grandes perturbations géopolitiques internationales et l'évolution des prix des carburants en France.

Le pic observé entre 2022 et 2023 correspond à une période de forte instabilité énergétique mondiale marquée notamment par :

- La guerre en Ukraine.
- Les perturbations des flux énergétiques européens.
- Les tensions sur les marchés mondiaux du pétrole.
- Les risques géopolitiques persistants au Moyen‑Orient.

Même si les prix diminuent progressivement à partir de 2024, ils demeurent supérieurs aux niveaux observés avant les grandes crises énergétiques.

Cette étude démontre l'importance des événements internationaux dans l'évolution des prix de l'énergie et leur impact direct sur les consommateurs français.

---

## 🚀 Exécution du projet

Installation des dépendances :

```bash
pip install -r requirements.txt
```

Transformation des données :

```bash
python3 src/transform.py
```

Analyse :

```bash
python3 src/analyze.py
```

Création des graphiques :

```bash
python3 src/visualize.py
```

---

## Skills Demonstrated

### Data Engineering
- ETL Pipeline Development
- Data Extraction and Processing
- Data Cleaning and Transformation
- SQLite Database Integration
- Pipeline Automation
- Logging and Monitoring
- SQL
- Python
- Pandas

### Data Analytics
- Exploratory Data Analysis (EDA)
- Data Visualization
- Time Series Analysis
- Price Volatility Analysis
- Business and Geopolitical Insights
- Matplotlib

### Tools & Version Control
- Git
- GitHub
- SQLite
---

## 🔮 Perspectives d'amélioration

- Ajout des cours du pétrole brut (Brent).
- Analyse de corrélation entre pétrole et carburants.
- Intégration d'indicateurs géopolitiques externes.
- Construction d'un tableau de bord interactif.
- Stockage des données dans PostgreSQL.
- Automatisation du pipeline avec Airflow.
- Déploiement cloud.

---

## 👨‍💻 Auteur

**Alpha Diallo**

Projet réalisé dans le cadre du développement de compétences en Data Analytics et de la préparation à un poste de Data Analyst / Data Engineer Junior.

🔗 GitHub :

https://github.com/Alpha38diallo/fuel-prices-france-geopolitics