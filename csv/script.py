import pandas as pd
import csv
#import pymongo
#from pymongo import MongoClient

csv_professor = open('professores.csv', 'r')
reader = csv.DictReader(csv_professor)

header = ['name', 'room', 'email']

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
        print(row)
        
