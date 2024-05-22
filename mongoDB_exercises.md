## Mongodb Exercises:

First make sure you have documented the simple commands we did as a class in your markdown. Once one, move on to the exercises, make sure to use online resources to help you.

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
- Add documents:
```
db.films.insertOne({title: "John Wick", release_date: "10. April 2015", main_actor: "Keanu Reeves", genre: "Action"})

db.films.insertMany([{title: "Titanic", release_date: "23. January 1998", main_actor: "Leonardo DiCaprio", genre: "Romance"},
{title: "We're the Millers", release_date: "23. August 2013", main_actor: "Jennifer Aniston", genre: "Comedy"}])
```
### Exercise 2

Add a new document to the collection, add a new field to that document, remove that field and then remove the document entirely.

#### Answer:
- Add document with new field:
```
db.films.updateOne({title: "We're the Millers"}, {$set: {director: "Rawson Marshall Thurber"}})
```
- Remove the new field:
```
db.films.updateOne({title: "We're the Millers"}, {$unset: {director: null}})
```
- Remove the entire document:
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
db.characters.find({name: "Luke Skywalker"})
```
Return the value of name and eye_colour only, from the "chewbacca" document:

```
db.characters.findOne({name: "chewbacca"}, {name: 1, eye_colour: 1, _id: 0})
```

Find a way to check the species name of admiral ackbar, this is in an embedded document ("Species"):


### Exercise 6 

Write a query that gives us only the names + homeworld names of humans in the database?

### Exercise 7

Write a query that gives us all the entries that have an eye_colour of either "yellow" or "orange"

### Exercise 8

You can combine filters using $and or $ or

Write a query that filter for characters that have both blue eyes and are female
Then write a query that filters for characters that have either blue eyes or are female

### Exercise 9

You can use comparison operators in your queries

Write a query that finds characters with a height over 200cm

Note, Height has been recorded as a string and there are some missing a height value entirely. Can you find out how to convert all the height strings to ints?

Run your initial height query again to confirm your solution works.

### Exercise 10

Experiment with the following operators. What does each do?

$eq
$gt
$gte
$in
$lt
$lte
$ne
$nin