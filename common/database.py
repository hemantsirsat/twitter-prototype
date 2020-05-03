from typing import Dict
import pymongo
import os

class Database:

    URI = 'mongodb://<twitter>:<twitter123>@ds163053.mlab.com:63053/heroku_cp20r344'
    DATABASE = pymongo.MongoClient(URI).get_database()

    def insert(collection:str,data:Dict):
        Database.DATABASE[collection].insert(data)

    def find_one(collection:str,query:Dict):
        return Database.DATABASE[collection].find_one(query)

    def find(collection:str,data:Dict):
        return [post for post in Database.DATABASE[collection].find(data)]

    def remove(collection:str,query:Dict):
        Database.DATABASE[collection].remove(query)