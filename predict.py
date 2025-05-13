import pickle
import pandas as pd

# Charger le modèle sauvegardé
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

def predict(latitude, longitude, minimum_nights, room_type, availability_365, number_of_reviews, model=model):
    """
    Prend en entrée les paramètres nécessaires et retourne une prédiction de prix.
    """
    # Validation des entrées
    if not isinstance(latitude, (int, float)):
        raise ValueError("Latitude doit être un nombre.")
    if not isinstance(longitude, (int, float)):
        raise ValueError("Longitude doit être un nombre.")
    if not isinstance(minimum_nights, int) or minimum_nights <= 0:
        raise ValueError("Minimum_nights doit être un entier positif.")
    if not isinstance(room_type, str) or room_type not in ["Entire home/apt", "Private room", "Shared room"]:
        raise ValueError("Room_type doit être une chaîne valide (Entire home/apt, Private room, Shared room).")
    if not isinstance(availability_365, int) or not (0 <= availability_365 <= 365):
        raise ValueError("Availability_365 doit être un entier entre 0 et 365.")
    if not isinstance(number_of_reviews, int) or number_of_reviews < 0:
        raise ValueError("Number_of_reviews doit être un entier positif ou nul.")
    
    # Préparer les données d'entrée sous forme de DataFrame
    input_data = pd.DataFrame([{
        "latitude": latitude,
        "longitude": longitude,
        "minimum_nights": minimum_nights,
        "room_type": room_type,
        "availability_365": availability_365,
        "number_of_reviews": number_of_reviews
    }])
    
    # Effectuer la prédiction
    prediction = model.predict(input_data)
    
    return prediction[0]

# Exemple d'utilisation
if __name__ == "__main__":
    # Lire les données utilisateur
    latitude = float(input("Latitude : "))
    longitude = float(input("Longitude : "))
    minimum_nights = int(input("Nombre minimum de nuits : "))
    room_type = input("Type de chambre (Entire home/apt, Private room, Shared room) : ")
    availability_365 = int(input("Disponibilité sur 365 jours : "))
    number_of_reviews = int(input("Nombre de commentaires : "))
    
    # Faire une prédiction
    prix_prevu = predict(latitude, longitude, minimum_nights, room_type, availability_365, number_of_reviews)
    
    # Afficher la prédiction
    print(f"Le prix prédit pour cette annonce est : ${prix_prevu:.2f}")