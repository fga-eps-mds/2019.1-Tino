import requests 
import json
from flask import Flask 
from flask import request
from flask import Response
import pandas as pd
import pymongo
from pymongo import MongoClient
import json
from flask import jsonify
from urllib import request as rq
import os
import ssl
import json as js
import time

app = Flask(__name__)

MONGO_USER = os.environ['MONGO_USER']
MONGO_USER = str(MONGO_USER)
MONGO_PASSWORD = os.environ['MONGO_PASSWORD']
MONGO_PASSWORD = str(MONGO_PASSWORD)


# accept telegram messages
@app.route('/',methods=['POST','GET'])
def index():
    if(request.method == 'POST'):
        return Response('ok',status=200)
    else:
        collection = get_intercampi_collection()
        #get data from fga site
        intercampi_dados = get_from_fga_site()

       #data must exists to insert a new in mongo
        if(len(intercampi_dados) != 0):
            collection.delete_many({})#delete old files in collection
            #insert each element on db    
            for element in intercampi_dados:
                collection.insert_one(element)
        json = []
        #find inserted elements on db
        for y in collection.find():
            print(y['_id'])
            del y['_id']
            json.append(y)

    return jsonify(json)

def get_intercampi_collection():
    client = MongoClient('e4b07ec50c05:27017', username=MONGO_USER,password=MONGO_PASSWORD)          
    db = client.admin
    collection = db['intercampi-horario']

    return collection

def get_from_fga_site():
    html = get_ssl_certificate()
    tables = pd.read_html(html, header=0)
    first_table = tables[0]
    #convert to dataframe
    first_table = pd.DataFrame(first_table)
    first_table = first_table.to_json(orient='values')
    # convert string to json
    first_table = js.loads(first_table)
    
    json = []
    #for each item,create a element and put on json list
    for item in first_table:
        element = {}
        element = {'horario_saida' : item[0],'destino' : item[2] ,'origem' : item[1] }
        json.append(element)

    print(json)
      
    return json



def get_ssl_certificate():
    
    url="https://fga.unb.br/guia-fga/horario-dos-onibus-intercampi"
    context = ssl._create_unverified_context()
    response = rq.urlopen(url, context=context)
    html = response.read()

    return html

@app.route("/darcy") ##########-----DARCY PATH-----#############

def get_from_darcy():
    collection = get_intercampi_collection()

    json =[]
    for y in collection.find():
        if(y['origem'] == "Darcy Ribeiro"):
            del y['_id']
            json.append(y)
        

    return jsonify(json)

@app.route("/gama") ##########-----GAMA PATH-----#############

def get_from_gama():
    collection = get_intercampi_collection()

    json =[]
    for y in collection.find():
        if(y['origem'] == "Gama"):
            del y['_id']
            json.append(y)
        

    return jsonify(json)

@app.route("/ceilandia") ##########-----CEILÂNDIA PATH-----#############

def get_from_ceilandia():
    collection = get_intercampi_collection()

    json =[]
    for y in collection.find():
        if(y['origem'] == "Ceilândia"):
            del y['_id']
            json.append(y)
        

    return jsonify(json)

@app.route("/planaltina") ##########-----PLANALTINA PATH-----#############

def get_from_planaltina():
    collection = get_intercampi_collection()

    json =[]
    for y in collection.find():
        if(y['origem'] == "Planaltina"):
            del y['_id']
            json.append(y)
        

    return jsonify(json)   

if(__name__ ==  '__main__'):
    app.run(debug=True, host='0.0.0.0')