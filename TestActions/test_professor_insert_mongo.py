from pymongo import MongoClient
import csv
import os

mongo_host = 'localhost'     #os.environ['MONGO_ID']
mongo_host = mongo_host + ':27017'

def get_mongo_collection():
    client = MongoClient(mongo_host, username='rasa', password='rasa')
    db = client['admin']
    collection = db['professor-contato']

    return collection

def csv_open_read():
    csv_professor = open('../csv/professores.csv', 'r')
    reader = csv.DictReader(csv_professor)
    
    return reader   

def test_mongo_connect_professor_collection():
# Set db settings
    connection_status = "OK"
    try:
        collection = get_mongo_collection()
        collection.delete_many({})
    except MongoClient.errors.ServerSelectionTimeoutError as err:
        connection_status = err
    assert connection_status == "OK"

def test_csv_read():
    try:
        # Open CSV file in /csv directory
        
        reader = csv_open_read()
        csv_status = "Leitura do csv realizada com sucesso"
    except IOError:
        csv_status = "Houve um erro na abertura do CSV"
    assert csv_status == "Leitura do csv realizada com sucesso"

def test_csv_header():
    # Check if CSV header is valid
    reader = csv_open_read()     
    header_status = "Sem erros"
    if reader.fieldnames[0] != 'name' or reader.fieldnames[1] != 'room' \
    or reader.fieldnames[2] != 'email' or reader.fieldnames[3] \
    != 'coordination':
        header_status = "Cabeçalho Inválido"
    assert header_status == "Sem erros"

def test_csv_pofessor_count():
    count = 0
    reader = csv_open_read()
    collection = get_mongo_collection()
    
    for each in reader:
        row = {}
        # Fields requireds
        if each['name'] != "" and each['room'] != "" \
        and each['coordination'] != "":
            row = each
            collection.insert_one(row)
            count = count + 1
        else:
            continue
    assert count == 110        

