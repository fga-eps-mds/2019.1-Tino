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
        client = MongoClient('acc33844053d:27017', username=MONGO_USER,password=MONGO_PASSWORD)
                     
        db = client.admin
        print(db)
        print(db.collection_names())
        collection = db['intercampi-horario']
        print(collection)
        print('oi')
        teste = db['intercampi-horario'].find()
        print(teste)
        json = []
        print('to antes do for')
        for y in db['intercampi-horario'].find():
            print(y['_id'])
            del y['_id']
            json.append(y)
        print('dps do for')

        print(len(json))
        if len(json) == 0:
            json = get_from_fga_site()
            print(json[0])
            print('json maroto {}'.format(json))



        else:
            json = json.json()

        return jsonify(json)
        # table = pd.read_html('https://fga.unb.br/guia-fga/horario-dos-onibus-intercampi', index_col = 0, header = 0)
        # intercampi = table[0]['Origem'][0]
        # return '<h1>'+intercampi+'</h1>'
def get_from_fga_site():
    html = get_ssl_certificate()
    tables = pd.read_html(html, header=0)
    first_table = tables[0]
    #convert to dataframe
    first_table = pd.DataFrame(first_table)
    first_table = first_table.to_json(orient='values')
    # convert string to json
    first_table = js.loads(first_table)
    print(first_table)
    #todo: save on mongo before return to update
    json = []
    for y in first_table:
        json.append(y)
    
    return json



def get_ssl_certificate():
    
    url="https://fga.unb.br/guia-fga/horario-dos-onibus-intercampi"
    context = ssl._create_unverified_context()
    response = rq.urlopen(url, context=context)
    html = response.read()

    return html

# helper function to extract chat id and text

if(__name__ ==  '__main__'):
    app.run(debug=True, host='0.0.0.0')
