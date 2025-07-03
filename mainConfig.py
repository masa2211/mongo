from fastapi import FastAPI
from pymongo import MongoClient
import configparser

app=FastAPI()

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    mongouri = config['database']['uri']
    db = config['database']['name']
    hostapp= config['app']['host']
    portt=config ['app']['port']

    client =MongoClient(mongouri) 
    database = client[db]
    global collection
    collection= database["jobcollection"]
    
    import uvicorn
    uvicorn.run(app, host=hostapp, port=portt)

@app.get("/jobs")
def getjob():
    jobs = list(collection.find({},  {"_id": 0}))
    return jobs    
    

if __name__=="__main__":
     main()
