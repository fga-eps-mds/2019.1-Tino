from flask import Flask
from pymongo import MongoClient
import csv

app = Flask(__name__)

client = MongoClient('localhost:27017', username='rasa', password='rasa')
db = client['admin']

csv_professor = open('../csv/professores.csv', 'r')
reader = csv.DictReader(csv_professor)

collection = db['professor-contato']
collection.delete_many({})

header = ['name', 'room', 'email']

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]
    collection.insert_one(row)
