from flask import Flask, jsonify
from flask_cors import CORS

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Habilitar CORS en la aplicación
CORS(app)

# Definir un endpoint de API para saludar
@app.route('/api/saludo', methods=['GET'])
def saludo():
    """
    Un endpoint simple para saludar.
    """
    mensaje = {
        "saludo": "¡Hola! Bienvenido a mi API."
    }
    return jsonify(mensaje)
