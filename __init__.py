from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

@app.route('/')
def racine():
    return render_template('hello.html') #Comm



@app.route('/Jeu_Des_Base')
def Jeu_Des_Base():
    return render_template('Jeu_Des_Base.html') #Comm1

@app.route('/bibliotheque_images')
def bibliotheque_images():
    return render_template('Outils_JS.html') #Comm2

@app.route('/Roulette_Russe')
def Roulette_Russe():
    return render_template('Roulette_Russe_Etape_1_Barillet_Vide.html') #Comm3

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)

