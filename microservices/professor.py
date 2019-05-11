from flask import Flask
from pymongo import MongoClient
import csv

app = Flask(name)

# Set db settings
client = MongoClient('localhost:27017', username='rasa', password='rasa')
db = client['admin']

collection = db['professor-contato']
collection.delete_many({})

try:
    # Open CSV file in /csv directory
    csv_professor = open('../csv/professores.csv', 'r')
    reader = csv.DictReader(csv_professor)
except IOError:
    print("Houve um erro na abertura do CSV.")

reader = csv.DictReader(csv_professor)
header = ['name', 'room', 'email']

# Header file validation
if reader.fieldnames[0] != 'name' or reader.fieldnames[1] != 'room' or reader.fieldnames[2] != 'email':
    print("O cabecalho do CSV esta incorreto.")


for each in reader:
    row = {}
    for field in header:
     row[field] = each[field]
     try:
        assert each[field] != ""
        print("Tudo Certo ")
       
     except AssertionError as e:
        print("Ha um espaco em branco.") 

    collection.insert_one(row)
     
