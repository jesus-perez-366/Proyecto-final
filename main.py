from flask import Flask, request, render_template
import os
import json
import tools.postdata as pos
import pandas as pd


app = Flask(__name__)

@app.route("/load")
def upload_file():
 # renderiamos la plantilla "formulario.html"
 return render_template('formulario.html')

@app.route("/upload", methods=['POST'])
def uploader():
    
    provincia = request.form['provincia']
    if provincia == '0':
        return 'No coloco la provincia'
    
    
    barrio = request.form['barrio']
    if barrio == "-":
        return 'No coloco el Barrio'
    
    try:
        hab = request.form['Numhab']
    except:
        return 'No selecciono del numer de habitaciones'
    
    try:
        orden = request.form['Orden']
    except:
        return 'No selecciono el orden'

    try:
        top = request.form['Top']
    except:
        return 'No seleccion una opcion del Top'

    try:
        envio= request.form['Envio']
        if envio == '1':
            correo=request.form['Correo']
            if correo=='':
                return 'selecciono que desea enviar la informacion pero falto colacr su correo electronico'
            else:
                pass
        else:
            correo=0
    except:
        return 'No selecciono si deseaba o no enviar la informacion al correo'
    
    c=pos.prueba(provincia, barrio, hab, orden, top, envio, correo)
    if type(c)==str:
        return c
    else:
        return render_template('map.html')

@app.route('/mapa')
def map_func():
	return render_template('map.html')


app.run(debug=True)