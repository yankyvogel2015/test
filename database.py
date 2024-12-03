from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# Debugging: Print database collections to verify the connection
print("Connected to MongoDB!")
print("Collections:", db.list_collection_names())