# AgriPredict

Prédiction du rendement céréalier par fusion de données climatiques et pédologiques — Projet certificat IA.
**Dépôt GitHub** : [github.com/AliouneBadaraMedouneDiene/AgriPredict](https://github.com/AliouneBadaraMedouneDiene/AgriPredict)

## Contexte

Le changement climatique rend les cycles agricoles imprévisibles. Ce projet simule un outil destiné à des conseillers agricoles pour anticiper le rendement d'une culture (en kg/hectare) en fonction des conditions du sol et du climat, afin d'orienter les agriculteurs vers les cultures les plus prometteuses.

## Objectif

Développer un modèle de régression capable de prédire le rendement d'une culture à partir de :
- Nutriments du sol : azote (N), phosphore (P), potassium (K), pH
- Conditions climatiques : température, humidité, pluviométrie

## Dataset

- **Source** : [Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) (Kaggle, licence CC0)
- **Taille** : 2200 lignes, 22 cultures (100 lignes chacune)
- **Variables** : N, P, K, temperature, humidity, ph, rainfall, label (culture)

> ⚠️ Le dataset original ne contient pas de variable de rendement (`yield`). Une colonne `yield_kg_ha` a donc été **générée synthétiquement** à partir d'une combinaison pondérée des variables du sol et du climat (N, P, K, rainfall, humidity), avec un bruit aléatoire ajouté pour simuler la variabilité naturelle. Les poids utilisés sont arbitraires et n'ont pas de validité agronomique précise ; cette limite est documentée en détail dans le rapport technique.

Le fichier `data/Crop_recommendation.csv` est directement inclus dans ce dépôt (fichier léger, quelques centaines de Ko) : aucun téléchargement supplémentaire n'est nécessaire pour reproduire le projet.

## Structure du projet

```
AgriPredict/
├── README.md
├── requirements.txt
├── notebooks/
│   └── agripredict_pipeline.ipynb   # pipeline complet (EDA, modélisation, évaluation)
├── data/
│   └── Crop_recommendation.csv      # dataset inclus dans le dépôt
├── models/
│   ├── best_model.pkl               # modèle entraîné (régression linéaire, généré par le notebook)
│   └── colonnes.pkl                 # liste des colonnes attendues par le modèle
├── app/
│   └── app_gradio.py                # interface de démonstration
└── report/
    └── Rapport_technique_AgriPredict.pdf   # rapport technique (5-10 pages)
```

## Installation

```bash
# Créer et activer un environnement (conda)
conda create -n agripredict python=3.11 -y
conda activate agripredict

# Installer les dépendances
conda install pandas numpy scikit-learn matplotlib seaborn jupyter -y
pip install xgboost gradio
```

## Utilisation

1. Ouvrir `notebooks/agripredict_pipeline.ipynb`
2. Exécuter les cellules dans l'ordre (le notebook est conçu pour être reproductible de bout en bout ; le dataset est déjà inclus dans `data/`)
3. Lancer l'interface de démonstration :
```bash
cd app
python app_gradio.py
```
Un lien local (`http://127.0.0.1:7860`) s'ouvre alors dans le navigateur.

## Méthodologie

1. **Analyse exploratoire (EDA)** : distributions, matrice de corrélation, détection des valeurs aberrantes
2. **Prétraitement** : encodage One-Hot de la variable culture, séparation X/y, split train/test (80/20)
3. **Modélisation** : comparaison d'un modèle baseline (régression linéaire) et d'un modèle avancé (Random Forest)
4. **Évaluation** : MAE, RMSE, R², analyse des erreurs par culture
5. **Déploiement** : interface interactive Gradio (thème Ocean)

Le modèle retenu au final est la **régression linéaire**, qui obtient de meilleurs résultats que le Random Forest sur ce jeu de données (voir le rapport technique pour l'explication détaillée).

## Limites et considérations éthiques

- La variable cible `yield_kg_ha` est simulée, pas réelle (voir section Dataset ci-dessus) — les résultats du modèle doivent être interprétés comme un exercice pédagogique, pas comme une prédiction agronomique fiable.
- Le modèle peut ne pas être applicable à des régions géographiques non représentées dans le dataset source.
- Ces prédictions ne doivent pas être utilisées pour des décisions agricoles ou financières réelles sans validation agronomique experte.

## Auteur

Projet réalisé dans le cadre du Certificat en Intelligence Artificielle.