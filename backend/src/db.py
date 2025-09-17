import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = MONGO_CONNECTION_STRING="mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client.get_database("Zoaient")
characters_collection = db.get_collection("Personnages")
messages_collection = db.get_collection("Conversations")
gamestates_collection = db.get_collection("Gamestates")