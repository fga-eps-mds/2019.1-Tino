from pymongo import MongoClient
import requests
import json

url_count = 'https://7c0eb0b6.ngrok.io'  # intercampi local ngrok url 5002
url_count = url_count + '/count'
mongo_host_prod = ''    # production mongo ip
mongo_host_prod = 'mongodb://' + mongo_host_prod + ':27017'
total_professors_registred = 110
total_intercampi_lines = 16

# Este teste é usado para assegurar a quantidade correta dos documentos
# dentro de cada coleção no mongo.
# This test is used to assert the documents counting inside each
# mongo collection.



# ###PROD MONGO TESTS
# def connect_prod_mongo_db():
#     client = MongoClient(mongo_host_prod, username='rasa', password='rasa')
#     db = client.admin

#     return db


# def test_prod_professor_count():

#     db = connect_prod_mongo_db()
#     collection = db['professor-contato']
#     count = collection.count_documents({})
#     assert count == 110