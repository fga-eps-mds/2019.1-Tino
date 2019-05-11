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
if reader.fieldnames[0] != 'name' or reader.fieldnames[1] != 'room' \
   or reader.fieldnames[2] != 'email':
    print("O cabecalho do CSV esta incorreto.")
for each in reader:
    row = {}
    if each['name'] != "" and each['room'] != "" and each['email'] != "":
        row = each
        print(row)
        collection.insert_one(row)
    else:
        continue

total = collection.count('professor-contato')
print("Foram adicionado(s) {} professore(s)".format(total))
