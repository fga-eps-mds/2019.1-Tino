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
app = Flask(__name__)

# accept telegram messages
@app.route('/',methods=['POST','GET'])
def index():

    if(request.method == 'POST'):
        print('oi')
        return Response('ok',status=200)
    else:
        client = MongoClient('mongodb://localhost:27017/', username='rasa',password='rasa')
                     
        db = client.admin
        print(db)
        print(db.collection_names())
        collection = db['intercampi-horario']
        print(collection)
        json = []
        for y in db['intercampi-horario'].find():
            del y['_id']
            json.append(y)
        
        # json = json.json()

        return jsonify(json)
        # table = pd.read_html('https://fga.unb.br/guia-fga/horario-dos-onibus-intercampi', index_col = 0, header = 0)
        # intercampi = table[0]['Origem'][0]
        # return '<h1>'+intercampi+'</h1>'

# helper function to extract chat id and text

if(__name__ ==  '__main__'):
    app.run(debug=True, host='0.0.0.0:5002')
