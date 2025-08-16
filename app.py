from flask import Flask
from routes.main import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://anushka:2-Anushka@cluster0.mongodb.net/mydb?retryWrites=true&w=majority")
db = client['mydb']
collection = db['users']

@app.route('/')
def index():
    user = collection.find_one({}, {'_id': 0})
    return f"Hello, {user['name']}!"
