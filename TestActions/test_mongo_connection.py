from pymongo import MongoClient

mongo_host = 'e77d4c94.ngrok.io'    #URL ./ngrok http 27017
mongo_host = 'mongodb://' + mongo_host + ':27017'

def get_mongo_collection():
    client = MongoClient(mongo_host, username='rasa', password='rasa')
    db = client['admin']
    collection = db['professor-contato']

    return collection

def test_mongo_connect_professor_collection():
# Set db settings
    connection_status = "OK"
    try:
        collection = get_mongo_collection()
    except:
        connection_status = "ERROR"
    assert connection_status == "OK"