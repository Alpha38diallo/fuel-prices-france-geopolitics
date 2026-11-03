# ⛽ Analyse des Prix des Carburants en France (2021-2025)

## 📌 Contexte du projet

Ce projet analyse l'évolution des prix des carburants en France entre 2021 et 2025 à partir des données publiques gouvernementales.

L'objectif est d'identifier les tendances de prix, mesurer l'impact des crises énergétiques récentes et comparer les différents types de carburants.

Ce projet a été réalisé dans le cadre du développement de compétences en Data Analytics avec Python.

---

## 🎯 Objectifs

- Extraire et exploiter plusieurs années de données carburants.
- Nettoyer et transformer un volume important de données.
- Réaliser des analyses statistiques pertinentes.
- Produire des visualisations claires des tendances observées.
- Construire un projet complet de portfolio Data Analyst.

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
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── outputs/
│   ├── evolution_prix_carburants.png
│   ├── prix_moyen_annuel.png
│   ├── prix_moyen_carburant.png
│   ├── top_10_mois_plus_chers.png
│   ├── volatilite_carburants.png
│   └── resume_analyse.txt
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── analyze.py
│   ├── visualize.py
│   ├── volatility.py
│   └── compare_fuels.py
│
└── README.md
```

---

## 🛠️ Technologies utilisées

- Python 3
- Pandas
- Matplotlib
- XML
- CSV
- Git
- GitHub

---

## 📊 Données

Source :

- Données publiques des prix des carburants en France
- Format XML
- Période étudiée : 2021 à 2025

Après nettoyage et transformation :

- Plus de 20 millions d'enregistrements analysés
- Dataset final : `carburants_2021_2025.csv`

---

## ⚙️ Pipeline de traitement

### 1. Extraction

Le script `extract.py` lit les fichiers XML annuels et extrait :

- Date
- Type de carburant
- Prix

### 2. Transformation

Le script `transform.py` :

- Convertit les dates
- Supprime les valeurs aberrantes
- Normalise les données
- Crée les variables temporelles

### 3. Analyse

Le script `analyze.py` calcule :

- Prix moyen par année
- Prix moyen par carburant
- Top 10 des mois les plus chers
- Carburant le plus cher
- Carburant le moins cher
- Volatilité des carburants

### 4. Visualisation

Les graphiques sont générés automatiquement avec Matplotlib.

---

# 📈 Résultats

## Prix moyens par année

| Année | Prix moyen (€ / litre) |
|---------|---------:|
| 2021 | 1.546 |
| 2022 | 1.851 |
| 2023 | 1.878 |
| 2024 | 1.800 |
| 2025 | 1.722 |

### Observation

- 2023 est l'année la plus chère.
- 2021 est l'année la moins chère.
- Les prix augmentent fortement entre 2021 et 2023 puis diminuent progressivement.

---

## Prix moyens par carburant

| Carburant | Prix moyen (€ / litre) |
|------------|---------:|
| SP98 | 1.841 |
| SP95 | 1.771 |
| E10 | 1.748 |
| Gazole | 1.710 |

### Observation

- Le SP98 est le carburant le plus cher.
- Le Gazole est le carburant le moins cher sur la période analysée.

---

## Top 10 des mois les plus chers

Les trois premiers sont :

| Mois | Prix moyen (€ / litre) |
|---------|---------:|
| Juin 2022 | 2.122 |
| Mars 2022 | 2.021 |
| Juillet 2022 | 1.986 |

### Observation

Les pics de prix sont principalement concentrés durant la crise énergétique de 2022.

---

## Volatilité des carburants

| Carburant | Volatilité |
|------------|---------:|
| Gazole | 0.189 |
| SP98 | 0.166 |
| E10 | 0.161 |
| SP95 | 0.160 |

### Observation

Le Gazole présente la plus forte volatilité sur la période étudiée.

---

## 📉 Graphiques générés

- Evolution des prix des carburants
- Prix moyen annuel
- Prix moyen par carburant
- Top 10 des mois les plus chers
- Volatilité des carburants

Les visuels sont disponibles dans le dossier :

```text
outputs/
```

---

## 🚀 Exécution du projet

### Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/fuel-prices-france-geopolitics.git
```

### Installer les dépendances

```bash
pip install pandas matplotlib
```

### Lancer la transformation

```bash
python3 src/transform.py
```

### Lancer les analyses

```bash
python3 src/analyze.py
```

### Générer les graphiques

```bash
python3 src/visualize.py
```

---

## ✅ Conclusions

Cette étude met en évidence un impact majeur de la crise énergétique sur les prix des carburants en France.

Les principaux enseignements sont :

- Hausse importante des prix entre 2021 et 2023.
- Pic historique observé en juin 2022.
- SP98 reste le carburant le plus coûteux.
- Gazole présente la plus forte volatilité.
- Les prix diminuent progressivement à partir de 2024 sans retrouver les niveaux observés en 2021.

---

## 👨‍💻 Auteur

Alpha Diallo

Projet réalisé dans le cadre de la préparation à un poste de Data Analyst / Data Engineer Junior.