import streamlit as st
import pickle
import pandas as pd
from predict import predict

# Load the model
model_path = "model.pkl"
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Le fichier modèle '{model_path}' est introuvable. Assurez-vous qu'il est dans le répertoire.")

# Streamlit app
st.title("Prédiction de prix pour les annonces Airbnb")

st.markdown("""
Cette application utilise un modèle de machine learning pour prédire le prix d'une annonce Airbnb en fonction des caractéristiques fournies.
Veuillez entrer les informations ci-dessous :
""")

# User inputs
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=40.7128, step=0.0001)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=-74.0060, step=0.0001)
minimum_nights = st.number_input("Nombre minimum de nuits", min_value=1, value=3, step=1)
room_type = st.selectbox("Type de chambre", ["Entire home/apt", "Private room", "Shared room"])
availability_365 = st.number_input("Disponibilité sur 365 jours", min_value=0, max_value=365, value=200, step=1)
number_of_reviews = st.number_input("Nombre de commentaires", min_value=0, value=50, step=1)

# Prediction button
if st.button("Prédire le prix"):
    try:
        # Call the predict function
        predicted_price = predict(
            latitude=latitude,
            longitude=longitude,
            minimum_nights=minimum_nights,
            room_type=room_type,
            availability_365=availability_365,
            number_of_reviews=number_of_reviews,
            model=model
        )
        st.success(f"Le prix prédit pour cette annonce est : ${predicted_price:.2f}")
    except ValueError as e:
        st.error(f"Erreur : {e}")
    except Exception as e:
        st.error(f"Une erreur inattendue s'est produite : {e}")