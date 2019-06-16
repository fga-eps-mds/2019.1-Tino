from pymongo import MongoClient
import requests
import json

url_prof_count = 'https://25a22b51.ngrok.io' # intercampi local ngrok url 5002
url_prof_count = url_prof_count + '/profcount'
mongo_host_prod = ''    #production mongo ip 
mongo_host_prod = 'mongodb://' + mongo_host_prod + ':27017'
total_professors_registred = 110

def get_professor_local_count():
    return requests.get(url_prof_count).json()

def test_local_professor_count():
    obj = get_professor_local_count()
    count = obj['profcount']

    assert count == total_professors_registred

# def connect_prod_mongo_db():
#     client = MongoClient(mongo_host_prod, username='rasa', password='rasa')
#     db = client.admin

#     return db

    

# def test_prod_professor_count():

#     db = connect_prod_mongo_db()
#     collection = db['professor-contato']
#     count = collection.count_documents({})
        

        
#     assert count == 110