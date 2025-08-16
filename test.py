from pymongo import MongoClient

uri = "mongodb+srv://anushka:2-Anushka@cluster0.iwhn3p3.mongodb.net/mydb?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    db = client["mydb"]
    users = db["users"]
    print(users.find_one())
    print("✅ Connection successful!")
except Exception as e:
    print("❌ Connection failed:", e)
