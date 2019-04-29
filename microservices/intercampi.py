import json
from flask import Flask
from flask import request
from flask import Response
import pandas as pd
from pymongo import MongoClient
from flask import jsonify
from urllib import request as rq
import os
import ssl

app = Flask(__name__)

MONGO_USER = os.environ['MONGO_USER']    
MONGO_USER = str(MONGO_USER)
MONGO_PASSWORD = os.environ['MONGO_PASSWORD']
MONGO_PASSWORD = str(MONGO_PASSWORD)
MONGO_HOSTNAME = os.environ['MONGO_ID']
MONGO_HOSTNAME = MONGO_HOSTNAME + ':27017'

# accept telegram messages
@app.route('/', methods=['POST', 'GET'])  # ###----ALL PATH----####
def index():
    if(request.method == 'POST'):
        return Response('ok', status=200)
    else:
        intercampi_dados = ""
        try:
            collection = get_intercampi_collection()
        except Exception as error:
            print(error)
        # Get data from FGA site
        try:
            intercampi_dados = get_from_fga_site()
        except Exception as error:
            print(error)

        # Data must exists to insert a new in mongo
        print(intercampi_dados)
        if(intercampi_dados != ""):
            print('deletando')
            collection.delete_many({})      # Delete old files in collection
            # Insert each element on db
            for element in intercampi_dados:
                collection.insert_one(element)
        json = []

        # Find inserted elements on db
        for y in collection.find():
            print(y['_id'])
            del y['_id']        # Delete the '_id' attribute.
            json.append(y)      # Add the register in json list.

    return jsonify(json)


def get_intercampi_collection():
    # acess mongo database
    client = MongoClient(MONGO_HOSTNAME, username=MONGO_USER,
                         password=MONGO_PASSWORD)
    db = client.admin
    collection = db['intercampi-horario']

    return collection


def get_from_fga_site():
    html = get_ssl_certificate()
    tables = pd.read_html(html, header=0)
    first_table = tables[0]
    # convert to dataframe
    first_table = pd.DataFrame(first_table)
    first_table = first_table.to_json(orient='values')
    # convert string to json
    first_table = json.loads(first_table)

    result = []
    # for each item,create a element and put on json list
    for item in first_table:
        element = {}
        element = {'horario_saida': item[0], 'destino': item[2],
                   'origem': item[1]}
        result.append(element)

    print(result)

    return result


def get_ssl_certificate():
    url = "https://fga.unb.br/guia-fga/horario-dos-onibus-intercampi"
    context = ssl._create_unverified_context()
    response = rq.urlopen(url, context=context)
    html = response.read()

    return html


@app.route("/darcy")  # ###-----DARCY PATH-----####
def get_from_darcy():
    collection = get_intercampi_collection()

    json = []
    for y in collection.find():
        # Filter the registers with origem 'Darcy Ribeiro'.
        if(y['origem'] == "Darcy Ribeiro"):
            # Delete the '_id' attribute.
            del y['_id']
            # Add the register in json list.
            json.append(y)

    return jsonify(json)


@app.route("/gama")  # #########-----GAMA PATH-----#############
def get_from_gama():
    collection = get_intercampi_collection()

    json = []
    for y in collection.find():
        if(y['origem'] == "Gama"):
            del y['_id']
            json.append(y)

    return jsonify(json)


@app.route("/ceilandia")  # #####-----CEILÂNDIA PATH-----######
def get_from_ceilandia():
    collection = get_intercampi_collection()

    json = []
    for y in collection.find():
        if(y['origem'] == "Ceilândia"):
            del y['_id']
            json.append(y)

    return jsonify(json)


@app.route("/planaltina")  # #########-----PLANALTINA PATH-----#############
def get_from_planaltina():
    collection = get_intercampi_collection()

    json = []
    for y in collection.find():
        if(y['origem'] == "Planaltina"):
            del y['_id']
            json.append(y)

    return jsonify(json)


if(__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')
