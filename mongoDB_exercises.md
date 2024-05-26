## MongoDB Exercises:

First make sure you have documented the simple commands we did as a class in your markdown. Once done, move on to the exercises, make sure to use online resources to help you.

### Simple Commands:
- Create database:
```
use databaseName
```

- Create collection:
```
db.createCollection("collectionName")
```

- Add document to a collection:
```
db.collectionName.insertOne({key: value})
```

- Insert multiple documents:
```
db.collectionName.insertMany([{key:value, key:value},{key:value, key:value}])
```

- Return all documents from a collection:
```
db.collectionName.find({})
```

- Update a document:
```
db.collectionName.updateOne({key:value}, {$set: {key:NewValue, NewKey: Value}})
```

- Update all documents:
```
db.collectionName.updateMany({}, {$set: {key:NewValue}})
```

- Delete a document:
```
db.collectionName.deleteOne({key:value})
```

### Exercise 1

Create a collection to store information about your favourite films. Add appropriate validation rules, then insert at least 3 documents. Practice using both .insertOne() and .insertMany(). You may want to type commands into a text editor then paste into the shell.

#### Answer:
- Create collection:
```
db.createCollection("films")
```

- Add validation rules:
```
{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'title',
      'release_date',
      'main_actor',
      'genre'
    ]
  }
}
```
- Add documents using 'insertOne()' to only add one document or 'insertMany()' to add multiple documents:
```
db.films.insertOne({title: "John Wick", release_date: "10. April 2015", main_actor: "Keanu Reeves", genre: "Action"})

db.films.insertMany([{title: "Titanic", release_date: "23. January 1998", main_actor: "Leonardo DiCaprio", genre: "Romance"},
{title: "We're the Millers", release_date: "23. August 2013", main_actor: "Jennifer Aniston", genre: "Comedy"}])
```
### Exercise 2

Add a new document to the collection, add a new field to that document, remove that field and then remove the document entirely.

#### Answer:
- Add document with new field using '$set':
```
db.films.updateOne({title: "We're the Millers"}, {$set: {director: "Rawson Marshall Thurber"}})
```
- Remove the new field using '$unset':
```
db.films.updateOne({title: "We're the Millers"}, {$unset: {director: null}})
```
- Remove the entire document using 'deleteOne()':
```
db.films.deleteOne({title: "We're the Millers"})
```

### Exercise 3

Install mongotools. Add the path to it's bin folder to the PATH variable (will be inside MongoDB folder)


### Exercise 4

Download StarWars.zip. Extract it in a reasonable location. In the terminal (not mongosh) navigate to the folder, make sure it is the one that has all of the json file. Then run the following command to add each to a new db called "starwars"

for i in *.json; do
    mongoimport --db starwars --collection characters --jsonArray --file "$i"
done

### Exercise 5

Write a query that finds the Luke Skywalker document:
```
# Returning a specific document using 'find()' and passing through the known key-value pair, in order to locate the specific document

db.characters.find({name: "Luke Skywalker"})
```

Return the value of name and eye_colour only, from the "chewbacca" document:
```
# Locating the document with the name 'Chewbacca' and returning the 'name' and the 'eye_color'.
# The _id gets returned automatically - in order for it not to be returned, we need to specify this by adding'_id: 0'.

db.characters.findOne({name: "Chewbacca"}, {name: 1, eye_color: 1, _id: 0})
```

Find a way to check the species name of admiral ackbar, this is in an embedded document ("Species"):
```
# Locating the document with the name 'Ackbar' and returning the 'species name' only.
# As the species name is embedded, we need to use the dot notation to access it.
# Make sure to wrap the key around quotes when using dot notation.
 
db.characters.findOne({name: "Ackbar"}, {"species.name": 1, _id:0})
```

### Exercise 6 

Write a query that gives us only the names + homeworld names of humans in the database:
```
# Locating documents which are human by using {"species.name": "Human"}
# Returning 'name' and 'homeworld.name' only.

db.characters.find({"species.name": "Human"}, {name: 1, "homeworld.name": 1, _id:0})
```

### Exercise 7

Write a query that gives us all the entries that have an eye_colour of either "yellow" or "orange":
```
# Locating documents with the eye_colour of either yellow or orange.
# '$in' selects the documents where the eye_color equals any value in the specified array.

db.characters.find({eye_color: {$in: ["yellow", "orange"]}})
```

### Exercise 8

You can combine filters using $and or $or.

Write a query that filter for characters that have both blue eyes and are female:
```
# '$and' operator selects the documents that satisfy all the expressions specified in the array.

db.characters.find({$and: [{eye_color: "blue"}, {gender: "female"}]})
```

Then write a query that filters for characters that have either blue eyes or are female
```
# '$or' operator selects the documents that satisfy at least one of the expressions specified in the array.

db.characters.find({$or: [{eye_color: "blue"}, {gender: "female"}]})
```

### Exercise 9

You can use comparison operators in your queries.

Write a query that finds characters with a height over 200cm:
```
# '$gt' operator selects the documents that have a height greater than 200.

db.characters.find({height: {$gt: 200}})
```
Note, Height has been recorded as a string and there are some missing a height value entirely. Can you find out how to convert all the height strings to ints?
```
# Locating the documents with 'unknown' heights, in order to update the values to 'null' instead.

db.characters.updateMany({height: "unknown"}, {$set: {height: null}})


# Updating the data type of 'height' from str to int using '$toInt'.
# Make sure to use a square bracket around the entire '$set' operator as otherwise MongoDB will create an embedded subdocument instead.

db.characters.updateMany({}, [{$set: {height: {$toInt: "$height"}}}])
```

Run your initial height query again to confirm your solution works.
```
db.characters.find({height: {$gt: 200}})
```

### Exercise 10

Experiment with the following operators. What does each do?

- $eq:
  - matches documents where the value of a field equals the specified value.
```
db.collectionName.find({height: {$eq: 180}})
```
- $gt:
  - selects those documents where the value of the specified field is greater than (>) the specified value.
```
db.collectionName.find({height: {$gt: 100}})
```
- $gte: 
  - selects the documents where the value of the specified field is greater than or equal to (>=) a specified value.
```
db.collectionName.find({height: {$gte: 100}})
```
- $in:
  - selects the documents where the value of a field equals any value in the specified array.
```
db.collectionName.find({height: {$in: [100, 200]}})
```
- $lt:
  - selects the documents where the value of the field is less than (<) the specified value.
```
db.collectionName.find({height: {$lt: 100}})
```
- $lte: 
  - selects the documents where the value of the field is less than or equal to (<=) the specified value.
```
db.collectionName.find({height: {$lte: 150}})
```
- $ne: 
  - selects the documents where the value of the field is not equal to the specified value.
```
db.collectionName.find({height: {$ne: 180}})
```
- $nin:
  - selects the documents where the specified field value is not in the specified array or the specified field does not exist.
```
db.collectionName.find({height: {$nin: [180, 200]}})
```

## MongoDB Advanced Exercises

### Exercise 1

Research aggregation in Mongodb. How does it work?

Write a query that finds the total (sum) of the height of all human characters in the db
```
db.characters.aggregate([
  {$match: {"species.name": "Human"}}, 
  {$group: {_id: null, totalHeight: {$sum: "$height"}}}
  ])
# totalHeight: 5476
```
Sum all heights and group by gender:
```
db.characters.aggregate([
  {$match: {"species.name": "Human"}},
  {$group: {_id: "$gender", total: {$sum: "$height"}}}
  ])
```

Write a query that finds the max height per homeworld
```
db.characters.aggregate([
  {$group: {_id: "$homeworld.name", maxHeight: {$max: "$height"}}}
  ])
```

Write a query that finds the mass and count per species. Filter out null values and sort by average mass (ascending order):
```
db.characters.updateMany(
  {mass: "unknown"}, 
  {$set: {mass: null}}
  )
  
db.characters.updateMany(
  {}, 
  [{$set: {mass: {$toInt: "$mass"}}}
  ])
  
db.characters.aggregate([
  {$match: {mass: {$ne: null}}}, 
  {$group: {_id: "species", totalMass: {$sum: "$mass"}, 
  count: {$sum: 1}, averageMass: {$avg: "$mass"}}},
  {$sort: {averageMass: 1}}
  ])

```

### Exercise 2

Some aggregation doesn't require the .aggregate() method.

Use .distinct() to find a list of all species names in the database:
```
db.characters.distinct("species.name")
```

Use .count() or .countDocuments() to get a count of the amount of humans in the database:
```
db.characters.countDocuments({"species.name": "Human"})
```

What does .estimatedDocumentCount({}) do?
```
# Returns the count of all documents in a collection.

db.characters.estimatedDocumentCount({})
```

### Exercise 3

The starwars database uses embedded documents for things like spicies and homeworld. Another option would be to use references.

Find the ObjectID for Darth Vader in the collection. Copy the output to your clipboard.
```
db.characters.findOne(
  {name: "Darth Vader"}, 
  {_id: 1}
  )
# Output: _id: ObjectId('664efb9e65349eadb174183e')
```
Create a collection in starwars called "starships"

Add Darth Vader's Tie-Fighter to that collection. Importantly we need to reference him being the pilot. Code is below:
```
db.createCollection("starships")

db.starships.insertOne({
  name: "TIE Advanced x1",
  model: "Twin Ion Engine Advanced x1",
  manufacturer: "Sienar Fleet Systems",
  length: 9.2,
  max_atmosphering_speed: 1200,
  crew: 1,
  passengers: 0,
  pilot: ObjectId("664efb9e65349eadb174183e")
  })
```

We can then use $lookup within an aggregate pipeline in order to add a field corresponding to the joined data:
```
db.starships.aggregate([
  { $lookup: {
    from: "characters",
    localField: "pilot",
    foreignField: "_id",
    as: "matched_pilot"
  } }
])
```
Now, add the Millenium Falcon to the starships collection. Look up the data or make it up. The pilot must take an array with multiple ObjectIDs though.
```
db.starships.insertOne({
    name: "Millennium Falcon",
    model: "YT-1300 light freighter",
    manufacturer: "Corellian Engineering Corporation",
    length: 34.37,
    max_atmosphering_speed: 1050,
    crew: 4,
    passengers: 6,
    pilot:[
        ObjectId("664efb9b4a637d9a738c5a44"),
        ObjectId("664efba83763d83d4d944e3a"),
        ObjectId("664efbb08d1e891c400a5000"),
        ObjectId("664efbb65e30be68b0773839")
    ]})
```

We could then use the same lookup as before - it works with ObjectIds in arrays too. But we'll get a huge amount of information back. To restrict it to certain fields, we could add a $project step to the pipeline, which projects certain data to the next step:
```
db.starships.aggregate([
  { $lookup: {
    from: "characters",
    localField: "pilot",
    foreignField: "_id",
    as: "matched_pilot"
  } },
  { $project: {name: 1, model: 1, "matched_pilot.name": 1}}
])
```

When first inserting documents that might have references, you can generate a new ObjectId and assign it to a variable var id = ObjectId(). That variable can then be set as the _id of the primary document and as the reference for the referencing document.
