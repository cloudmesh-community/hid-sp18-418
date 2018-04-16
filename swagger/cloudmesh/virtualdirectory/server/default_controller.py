import connexion
import six
import json
from swagger_server import util
#importing pymongo for working with MongoDB 
from pymongo import MongoClient

# Connecting to the local MongoDB host
client = MongoClient('localhost',27017)

def get_database_names():  # noqa: E501
	x = client.database_names()
	#Returning the list of Database names in the MongoDB as JSON objects
	return json.dumps(x)
