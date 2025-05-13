import pytest
import pickle
import numpy as np
from predict import predict


@pytest.fixture
def loaded_model():
    # Charger le modèle sauvegardé
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model


def test_predict_valid_input(loaded_model):
    
    # Appeler la fonction predict avec des entrées valides
    result = predict(
        latitude=40.7128,
        longitude=-74.0060,
        minimum_nights=3,
        room_type="Entire home/apt",
        availability_365=200,
        number_of_reviews=50,
        model=loaded_model  # Passer le modèle mocké
    )
    
    # Vérifier que le résultat est correct
    assert result == 225.4351794454667, f"Expected 225.4351794454667 but got {result}"


def test_predict_invalid_input(loaded_model):
    # Tester avec des entrées invalides
    with pytest.raises(ValueError):
        predict(
            latitude="invalid_latitude",  # Valeur invalide
            longitude=-74.0060,
            minimum_nights=3,
            room_type="Entire home/apt",
            availability_365=200,
            number_of_reviews=50,
            model=loaded_model  # Passer le modèle mocké
        )

    with pytest.raises(ValueError):
        predict(
            latitude=40.7128,
            longitude=-74.0060,
            minimum_nights=-1,  # Valeur invalide
            room_type="Entire home/apt",
            availability_365=200,
            number_of_reviews=50,
            model=loaded_model  # Passer le modèle mocké
        )


def test_predict_edge_cases(loaded_model):

    # Tester avec des valeurs limites (par exemple, latitude et longitude aux extrêmes)
    result = predict(
        latitude=90.0,  # Valeur limite
        longitude=180.0,  # Valeur limite
        minimum_nights=1,
        room_type="Private room",
        availability_365=0,
        number_of_reviews=0,
        model=loaded_model  # Passer le modèle mocké
    )
    
    # Vérifier que le résultat est correct
    assert result == 84.57942367061773, f"Expected 84.57942367061773 but got {result}"


def test_predict_wrong_guess(loaded_model):
    
    result = predict(
        latitude=38.0987,  # Valeur limite
        longitude=165.98,  # Valeur limite
        minimum_nights=1,
        room_type="Private room",
        availability_365=0,
        number_of_reviews=0,
        model=loaded_model  # Passer le modèle mocké
    )

    assert result != 123.45, f"Expected an Error"


def test_predict_missing_input(loaded_model):
    # Tester avec des entrées manquantes
    with pytest.raises(TypeError):
        predict(
            latitude=40.7128,
            longitude=-74.0060,
            minimum_nights=3,
            room_type="Entire home/apt",
            availability_365=200,
            # number_of_reviews est manquant
            model=loaded_model  # Passer le modèle mocké
        )
