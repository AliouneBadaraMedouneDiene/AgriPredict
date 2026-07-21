# AgriPredict

Prédiction du rendement céréalier par fusion de données climatiques et pédologiques — Projet certificat IA.

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

### Télécharger le dataset

Le fichier CSV n'est pas inclus dans ce dépôt (voir `.gitignore`). Pour l'obtenir :
1. Télécharger `Crop_recommendation.csv` depuis [Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
2. Placer le fichier dans le dossier `data/`

## Structure du projet

```
AgriPredict/
├── README.md
├── requirements.txt
├── notebooks/
│   └── agripredict_pipeline.ipynb   # pipeline complet (EDA, modélisation, évaluation)
├── data/
│   └── Crop_recommendation.csv      # à télécharger (non versionné)
├── models/
│   └── best_model.pkl               # modèle entraîné (généré par le notebook)
├── app/
│   └── app_gradio.py                # interface de démonstration
└── report/
    └── rapport_technique.pdf        # rapport technique (5-10 pages)
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
2. Exécuter les cellules dans l'ordre (le notebook est conçu pour être reproductible de bout en bout)
3. Lancer l'interface de démonstration :
```bash
python app/app_gradio.py
```

## Méthodologie

1. **Analyse exploratoire (EDA)** : distributions, matrice de corrélation, détection des valeurs aberrantes
2. **Prétraitement** : encodage de la variable culture, normalisation, split train/test (80/20)
3. **Modélisation** : comparaison d'un modèle baseline (régression linéaire) et d'un modèle avancé (Random Forest / XGBoost)
4. **Évaluation** : MAE, RMSE, R², analyse des erreurs par type de culture
5. **Déploiement** : interface interactive Gradio

## Limites et considérations éthiques

- La variable cible `yield_kg_ha` est simulée, pas réelle (voir section Dataset ci-dessus) — les résultats du modèle doivent être interprétés comme un exercice pédagogique, pas comme une prédiction agronomique fiable.
- Le modèle peut ne pas être applicable à des régions géographiques non représentées dans le dataset source.
- Ces prédictions ne doivent pas être utilisées pour des décisions agricoles ou financières réelles sans validation agronomique experte.

## Auteur

Projet réalisé dans le cadre du Certificat en Intelligence Artificielle.