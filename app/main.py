from flask import Flask
import os

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    os.environ.get("NOMBRE", "Sin nombre")
    return f"Hola Mundo, soy Python!, y mi variable NOMBRE={NOMBRE}"

@app.route('/bye')
def bye_world():
    return ("Adios mundo cruel")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
