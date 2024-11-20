from pymongo import MongoClient
# uri = "mongodb://localhost:27017/"
url = "mongodb+srv://patilharshad:gn3eeXP1Bul4ckQ7@usersdata.rdnnb.mongodb.net/"
myclient = MongoClient(url)
mydb = myclient['streamspot']