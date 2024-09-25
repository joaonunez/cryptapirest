from flask import Flask, jsonify
from flask_cors import CORS
import os

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Habilitar CORS en la aplicación
CORS(app)

# Definir un endpoint de API para saludar
@app.route('/', methods=['GET'])
def home():
    return "<h1>hOLA </h1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
