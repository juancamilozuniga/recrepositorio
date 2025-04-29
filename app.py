from flask import Flask, render_template, session, jsonify, flash
from flask_mongoengine import MongoEngine
from models.usuario import Usuario
from models.oficina import Oficina
from models.visitante import Visitante
from flask_cors import CORS
from flask import session, flash
import os
from dotenv import load_dotenv


# uri2 = "mongodb+srv://camilo2083:juanca95@cluster0.5b4pn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uriLocal = "mongodb://localhost:27017/visitantesbd"
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})  # permite todas las rutas desde cualquier origen

uri3 = os.environ.get("MONGO_URI")

app.secret_key = "mi_super_secreto_seguro_12354"


app.config['MONGODB_SETTINGS'] = [{
    "db": "visitantesbd",
    "host": uri3,
    #"port": 27017
}]

app.config['CORS_HEADERS'] = 'Content-Type'


db = MongoEngine(app)



@app.route('/')
def inicio():
    return render_template('login.html')
    
from routes.usuarioRuta import *
from routes.visitantesRutas import *
if __name__ == '__main__':
    app.run(debug=True)
