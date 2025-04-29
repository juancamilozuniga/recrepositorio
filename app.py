from flask import Flask, render_template, session, jsonify, flash
from flask_mongoengine import MongoEngine
from models.usuario import Usuario
from models.oficina import Oficina
from models.visitante import Visitante
from flask_cors import CORS
from flask import session, flash
import os
from dotenv import load_dotenv


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})  # permite todas las rutas desde cualquier origen

uri3 = os.environ.get("MONGO_URI")
secreto = os.environ.get("SECRET_KEY")
app.secret_key = secreto



app.config['MONGODB_SETTINGS'] = [{
    "db": "visitantesbd",
    "host": uri3,

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
