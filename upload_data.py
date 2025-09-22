from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://Vikas:FHs98rBBpN65GxzX@cluster0.hdn9wuj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connect to server
client=MongoClient(uri)

#create database name and collection name
DATABASE_NAME="ml_project"
COLLECTION_NAME="waferfault"

df=pd.read_csv("C:\Users\vikas\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)