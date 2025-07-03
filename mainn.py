
from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

Mongouri = os.getenv("MONGO_URI")
mongodb = os.getenv("MONGODB")

client = MongoClient(Mongouri)
db = client[mongodb] 
collection = db["jobcollection"]

app = FastAPI()

@app.get("/jobs")
def getjob():
    jobs = list(collection.find({},  {"_id": 0}))
    return jobs    