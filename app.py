# Importation des librairies
from flask import Flask, request, render_template, send_file
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Fonction pour charger le modèle depuis le fichier .pkl
def load_model():
    model = joblib.load('model.pkl')
    return model

# Route pour afficher la page d'acceuil du formulaire 
@app.route('/')
def index():
    return render_template('index.html')

# Route pour traiter les pédictions
@app.route('/predict', methods=['POST'])
def predict():
    # Charger le modèle
    model = load_model()
    # Récupérer les données du formulaire
    try: 
         crim = float(request.form['crim'])
         zn = float(request.form['zn'])
         indus = float(request.form['indus'])
         chas = float(request.form['chas'])
         nox = float(request.form['nox'])
         rm = float(request.form['rm'])
         age = float(request.form['age'])
         dis = float(request.form['dis'])
         tax = float(request.form['tax'])
         ptratio = float(request.form['ptratio'])
         b = float(request.form['b'])
         lstat = float(request.form['lstat'])
    except ValueError:
         return "Erreur dans la saisie. Veuillez entrer des valeurs numériques." 

    # Préparer les données pour la prédiction
    data = np.array([[crim, zn, indus, chas, nox, rm, age, dis, tax, ptratio, b, lstat]])
    # Faire la prédiction
    prediction = model.predict(data)
   
    # Retourner le résultat dans la page HTML
    return render_template('index.html', prediction=prediction)
if __name__ == '__main__':
    app.run(debug=True, port=5000)