"""
app_gradio.py — Interface de démonstration pour AgriPredict

Permet à un utilisateur de saisir les caractéristiques d'un terrain
(nutriments du sol, climat, culture) et d'obtenir une prédiction
de rendement (kg/ha) grâce au modèle entraîné.
"""

import gradio as gr
import joblib
import pandas as pd

# Chargement du modèle et de la liste des colonnes attendues
# (sauvegardés depuis le notebook à l'étape précédente)
modele = joblib.load('../models/best_model.pkl')
colonnes_modele = joblib.load('../models/colonnes.pkl')

# Liste des cultures disponibles (doit correspondre à celles du dataset d'entraînement)
cultures = [
    'rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans',
    'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango',
    'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya',
    'coconut', 'cotton', 'jute', 'coffee'
]


def predire_rendement(culture, N, P, K, temperature, humidity, ph, rainfall):
    """
    Prend les caractéristiques saisies par l'utilisateur et retourne
    le rendement prédit en kg/ha.
    """
    # On construit une ligne de données avec les valeurs saisies
    input_data = pd.DataFrame([{
        'N': N, 'P': P, 'K': K,
        'temperature': temperature, 'humidity': humidity,
        'ph': ph, 'rainfall': rainfall
    }])

    # On ajoute les colonnes one-hot pour la culture (toutes à 0 sauf celle choisie)
    for c in cultures:
        input_data[f'label_{c}'] = 1 if c == culture else 0

    # On réordonne les colonnes pour qu'elles correspondent exactement
    # à ce que le modèle attend (même ordre que X_train)
    input_data = input_data[colonnes_modele]

    prediction = modele.predict(input_data)[0]

    return f"Rendement prédit : {prediction:.1f} kg/ha"


# Construction de l'interface Gradio
interface = gr.Interface(
    fn=predire_rendement,
    inputs=[
        gr.Dropdown(choices=cultures, label="Culture"),
        gr.Slider(0, 140, label="Azote (N)"),
        gr.Slider(0, 145, label="Phosphore (P)"),
        gr.Slider(0, 205, label="Potassium (K)"),
        gr.Slider(8, 44, label="Température (°C)"),
        gr.Slider(14, 100, label="Humidité (%)"),
        gr.Slider(3.5, 10, label="pH"),
        gr.Slider(20, 300, label="Pluviométrie (mm)"),
    ],
    outputs="text",
    title="AgriPredict — Prédiction de rendement céréalier",
    description="Renseignez les caractéristiques du sol et du climat pour estimer le rendement attendu (kg/ha).",
    theme=gr.themes.Soft(primary_hue="green", secondary_hue="emerald")
)

if __name__ == "__main__":
    interface.launch()