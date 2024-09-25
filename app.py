from flask import Flask, jsonify

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta de ejemplo
@app.route('/api/saludo', methods=['GET'])
def saludo():
    """
    Un endpoint simple para saludar.
    """
    mensaje = {
        "saludo": "¡Hola! Bienvenido a mi API."
    }
    return jsonify(mensaje)

# Verificar si se ejecuta como el archivo principal
if __name__ == '__main__':
    app.run(debug=True)
