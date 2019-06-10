from pymongo import MongoClient

mongo_host = ''    #URL ./ngrok http 27017
mongo_host = 'mongodb://' + mongo_host + ':27017'
total_professors_registred = 110

# def connect_mongo_db():
#     client = MongoClient(mongo_host, username='rasa', password='rasa')
#     db = client.admin

#     return db

    

# def test_mongo_connect():

#     db = connect_mongo_db()
#     collection = db['professor-contato']
#     count = collection.count_documents({})
        

        
#     assert count == 110


      

  

   