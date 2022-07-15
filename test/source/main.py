#!/usr/bin/env python3

# =========== General imports ===========

import json
import os
import webbrowser
from flask import Flask, request, Response, render_template, abort, url_for, send_from_directory
from werkzeug.utils import secure_filename


# =========== Port to use on Flask Server ===========
PORT = 8000
DEBUG = False

app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.json']
app.config['UPLOAD_PATH'] = 'source/uploads'

# =========== Home ===========
@app.route("/home", methods=['GET'])
def home():
    status_code = Response("Analítica Digital - TEST", status=200)
    return status_code

# =========== TEST ===========
#
@app.route('/string/<word>')
def string(word : str):

    #***Aqui puedes poner tu codigo***,(se puede eliminar el codigo de ejemplo)
    #recibiendo como parametro un string, contar cuantas letras de letra uno existe,  y que nos retorne el resultado en el navegador web.
    #ejemplo cienciadedatos
    #return:
    #a=2 c=2 d=2 e=2 i=2 s=1 t=1 o=1

    counting = {
        char: word.count(char) #hace el conteo por caractér y suma si es el mismo caractér
        for char in set(word)  #con set() hacemos la lista por caractér
    }
    return counting 

        
    
# =========== TEST 2 ===========
#
@app.route('/fibonacci/<entero>')
def fibonacci(entero : int):

    #***Aqui puedes poner tu codigo***,(se puede eliminar el codigo de ejemplo)
    #recibiendo como parametro un entero, calcular la sucesión de Fibonacci. y que nos retorne el resultado en el navegador web.
    #Ejemplo 6
    #return:
    #5
    
    a = 0
    b = 1

    for i in range(int(entero)-1):
        c = b+a
        a = b
        b = c

    sucesion = {
        
        "Respuesta" : a
    }
    return sucesion
    
 
# EJERCICIO OPCIONAL
#Crear una funcion con metodo POST que introduciendo cualquier archivo json, nos regrese en el navegador web todo pegado como string ó cadena de texto.
#{"regiones_telcel": [
#            {
#                "id": "1",
#                "numciudadtelcel": "607",
#                "nomciudadtelcel": "EJIDO 43",
#                "numciudadcoppel": "226",
#                "nomestado": "BAJA CALIFORNIA",
#               "numplaza": "3",
#                "numlada": "686",
#                "numregion": "1"
#            }
#			]
#			} 
# resultado:
# {"regiones_telcel": [{ "id": "1", "numciudadtelcel": "607",  "nomciudadtelcel": "EJIDO 43", "numciudadcoppel": "226",     "nomestado": "BAJA CALIFORNIA", "numplaza": "3", "numlada": "686", "numregion": "1"}]} 

@app.route('/json', methods = ['GET', 'POST'])
def upload_files():

    if request.method == 'POST': 
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        with open(os.path.join(app.config['UPLOAD_PATH'], filename)) as json_file:
            data= json.load(json_file)
            json_string = json.dumps(data)
            return render_template('form.html', content=json_string)
        

    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('input.html', files = files) 



@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)    
    
#@app.route('/postjson', methods = ['GET', 'POST'])
#def postjson():    
 #       json_data = request.json
  #      json_string = json.dumps(json_data)
   #     return render_template('form.html', content=json_string)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
