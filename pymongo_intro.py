import pymongo

# Connecting to MongoDB
client = pymongo.MongoClient()
db = client["starwars"]

# Retrieve a document from the database
luke = db.characters.find_one({"name": "Luke Skywalker"})
print(luke)

# Getting only certain fields
luke_short = db.characters.find_one({"name": "Luke Skywalker"},
                                    {"name": 1, "eye_color": 1, "_id": 0})
print(luke_short)

# Iterating through multiple records/documents
droids = db.characters.find({"species.name": "Droid"})
print(droids)
for droid in droids:
    print(droid["name"])


# PYMONGO - BASICS

# Exercise 1 - Find the height of Darth Vader, only return results for the name and the height.
height_darth = db.characters.find_one({"name": "Darth Vader"}, {"name": 1, "height": 1, "_id": 0})
print(height_darth)

# Exercise 2 - Find all characters with yellow eyes, only return results for the names of the characters.
yellow_eyes = db.characters.find({"eye_color": "yellow"})
for character in yellow_eyes:
    print(character["name"])

# Exercise 3 - Find male characters. Limit your results to only show the first 3.
male = db.characters.find({"gender": "male"}).limit(3)
for character in male:
    print(character["name"])

# Exercise 4 -Find the names of all the humans whose homeworld is Alderaan.
alderaan = db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"})
for human in alderaan:
    print(human["name"])


# PYMONGO AGGREGATION

# Exercise 1 - What is the average height of female characters?
avg_height = [{"$match": {"gender": "female", "height": {"$ne": None}}},
              {"$group": {"_id": None, "avgHeight": {"$avg": "$height"}}}]

result = db.characters.aggregate(avg_height)
for character in result:
    print("{:.2f}".format(character["avgHeight"]))

# Exercise 2 - Which character is the tallest?
max_height = db.characters.aggregate([{"$group": {"_id": None, "maxHeight": {"$max": "$height"}}}]).next()["maxHeight"]

result_max_height = db.characters.find({"height": max_height})
for tallest in result_max_height:
    print(tallest["name"], tallest["height"])
