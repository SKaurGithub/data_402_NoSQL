# NoSQL and MongoDB

## NoSQL

### What is SQL?
NoSQL is also referred to as “not only SQL” or “non-SQL”, which is an approach to database design that enables the storage and querying of data outside the traditional structures found in relational databases.

### Compare SQL to NoSQL

#### Schema Design
SQL databases are relational, while NoSQL databases are non-relational.
- Relational databases store data in rows and tables. These systems connect information from various tables with keys. You have to use predefined schemas to determine your data structure before you can work with it. All of your data must follow the same structure.
- Non-relational or NoSQL databases have dynamic schemas for unstructured data to store data just like relational databases. However, they don't contain any rows, tables, or keys. This type of database utilizes a storage model based on the type of data it stores. They are more flexible and don’t necessarily require the same rigid structure as SQL. 

#### Language
- Relational databases use Structured Query Language (SQL) to store and retrieve data. 
- Non-relational or distributed databases can use a wide range of programming languages depending on which software is being used.

#### Scalability
- SQL databases are vertically scalable in most situations. That means you can increase the load on a single server by adding more CPU, RAM, or SSD capacity. This is also called scaling up.
- NoSQL databases are horizontally scalable. You can handle higher traffic via a process called sharding (scaling out), which adds more servers to your NoSQL database.

#### Structure
- SQL databases are table-based.
- NoSQL databases are document, key-value, graph, or column stores.

### What language(s) can be used?
NoSQL can use a wide range of programming languages depending on which software is being used.

### NoSQL is scalable. Explain the concept and some benefits of it. Any negatives?
NoSQL databases are horizontally scalable, which means it has the ability to chop the database into smaller parts, which can be distributed to different servers.

#### Benefits
- Workload is distributed across multiple servers
- You can add as many servers as needed
- The performance is higher

#### Disadvantages
- High costs initially
- Multiple servers are harder to maintain than a single server is.
- Backing up your machines may also become a little more complex.

### Types of NoSQL Database
- Key-Value store
- Document database
- Column stores
- Graph stores

## MongoDB

### What is MongoDB?
MongoDB is an open source NoSQL database management program, which is a document database. It is a distributed database at its core, so high availability, horizontal scaling, and geographic distribution are built in and easy to use.

### What are collections in Mongo?
A collection is a grouping of MongoDB documents. A collection is the equivalent of a table in a relational database system. A collection exists within a single database.

### What are Documents?
A record in MongoDB is a document, which is a data structure composed of field and value pairs. MongoDB documents are similar to JSON objects. The values of fields may include other documents, arrays, and arrays of documents.
A document is the equivalent of a row in a relational database system.

### MongoDB Architecture, how does it work? 
MongoDB’s architecture design involves several important parts that work together to create a strong and flexible database system. These are the following MongoDB’s architecture:
- Drivers & Storage Engine
- Security
- MongoDB Server
- MongoDB Shell
- Data Storage in MongoDB
- Replication
- Sharding
- 
### What are replica sets?
A replica set is a group of servers that maintain identical copies of the same data. Replication provides high availability, durability, and data redundancy.

### What is sharding?
A shard is a horizontal partition of data that is spread across multiple servers.

### Advantages of MongoDB?
- MongoDB doesn’t demand predefined schemas, but schema migration might be necessary for evolving data structures.
- MongoDB’s document-oriented approach aligns with dynamic queries. It allows flexible and varied query operations based on the nature of the documents, unlike static table-based queries of RDBMS.
- MongoDB uses internal memory for data storage. So, it accesses the data very fast and enhances the overall performance.
- Using MongoDB, we can horizontally expand our database by distributing data across multiple servers.

### Disadvantages of MongoDB?
- In MongoDB, transactions work within each piece of data (called a document), but they don’t fully cover situations where you need to do multiple things at once across lots of data. This might be tricky for applications that really need everything to happen perfectly together.
- While MongoDB offers Atomicity, Consistency, Isolation, and Durability (ACID) at the document level, it doesn’t provide full ACID compliance across multiple documents or collections. This limitation can be challenging for applications requiring strict and complex transactional guarantees.
- Unlike traditional relational databases, MongoDB doesn’t support joins in the same way. While it’s possible to manually perform join-like operations using code, it can slow down execution and affect performance.
- MongoDB stores key names with each value pair, causing some data redundancy due to the limitations of joins. This redundancy might lead to increased memory usage compared to what’s strictly necessary.

### What scenarios is MongoDB good for?
MongoDB is a general-purpose database used in various ways to support applications in many different industries (e.g., telecommunications, gaming, finances, healthcare, and retail).
- Integrating large amounts of diverse data
- Describing complex data structures that evolve
- Supporting agile development and collaboration

### What scenarios is it not good for?
MongoDB should not be used if a rigid schema with strong data integrity constraints is required. In this case, a relational database would be more suitable.