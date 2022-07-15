import pymongo

client = pymongo.MongoClient()

mydb=client["mydb"]


mycol=mydb["people"]

data={"name" : "blabla" , "test" : "wep"}

mycol.insert_one(data)