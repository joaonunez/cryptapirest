from flask import Flask, jsonify
from flask_cors import CORS
import os

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

if __name__ == '__main__':
    # Ejecutar la aplicación en el puerto especificado
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
