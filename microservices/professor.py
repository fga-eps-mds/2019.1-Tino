from flask import Flask
from pymongo import MongoClient
import csv

app = Flask(__name__)


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

# try:
header = ['name', 'room', 'email']

# Header file validation
if reader.fieldnames[0] != 'name' or reader.fieldnames[1] != 'room' or reader.fieldnames[2] != 'email':
    print("O cabecalho do CSV esta incorreto.")

errado = 0 
for each in reader:
    row = {}
    for field in header:
     
     try:
         assert each[field] != ""
         row[field] = each[field]
     except AssertionError as e:
         errado = errado+1
         print("Ha  espacos em branco.")
         
    if (errado==0):
        collection.insert_one(row)
    
total = collection.count('professor-contato')

print("Foram adicionado(s) {} professore(s)".format(total))

