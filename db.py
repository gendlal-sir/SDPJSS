from pymongo import MongoClient

client = MongoClient("mongodb+srv://anushka:2-Anushka@cluster0.iwhn3p3.mongodb.net/")
db = client['mydb']
collection = db['users']


