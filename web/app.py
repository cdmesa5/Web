from datetime import datetime

from statistics import mode

from flask import Flask, jsonify, request, render_template

from flask_cors import CORS

import requests

app = Flask(__name__, template_folder="templates")
CORS(app)

terrenos_list = ['Planicie', 'Ladera', 'Cenagoso', ' Desértico']

predio_list = [
    {"codigo" :1698457, "latitud" :"3867 22°", "longitud" :"2563 15°", "terreno" : "Planicie", "area" :1958.00},
    {"codigo" :3246366, "latitud" :"28765 14°", "longitud" :"3457 18°", "terreno" : "Ladera", "area" :8565.00},
    {"codigo" :8587344, "latitud" :"9853 29°", "longitud" :"2335 94°", "terreno" : "Cenagoso", "area" :5496.00}
]

@app.route("/crearPredio", methods=['GET'])
def crearPredio():
    return render_template('crearPredio.html', listaTipos = terrenos_list)

@app.route("/listarPredio", methods=['GET'])
def listarPredio():
    predio_list = requests.get('http://localhost:5000/predios').json()
    return render_template('listarPredio.html', lista = predio_list)

@app.route("/guardarPredio", methods=['POST'])
def guardarPredio():
    predio = dict(request.values)
    predio['area'] = int(predio['area'])
    predio['codigo'] = int(predio['codigo'])
    requests.post('http://localhost:5000/predios', json=predio)
    return(listarPredio())
