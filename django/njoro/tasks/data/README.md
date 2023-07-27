# SQLITE
## -------------------------------------------------------------------
### creating table
```sql
CREATE TABLE flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
```
### inserting data
```sql
INSERT INTO flights
    (origin, destination, duration)
    VALUES ("Nairobi", "Kenya", 415);
```
### querying data || retrieving data
```sql
SELECT * FROM flights;
```
### querying specific rows || retrieving specific data
```sql
SELECT * FROM flights WHERE origin = "Nairobi";
```
### querying specific columns || retrieving specific data
```sql
SELECT origin, destination FROM flights;
```

## -------------------------------------------------------------------
## CREATING A SQLITE DATABASE
sqlite database is a lighter version of the sql database, it stores data in a file.
To create a sqlite datbase, just create a file, and if you have the sqlite3 installed, you can run the following command to create a database and access its shell.
```bash
touch flights.sql
sqlite3 flights.sql
```
On the shell, you can run all sqlite commands, to see all the tables you have created, run the following command in the shell.
```sql
.tables
```
To output the data in a friendly format, run the following sqlite commands before running the query.
```sql
.mode columns
.headers yes
```
To exit the sqlite shell, run the following command.
```sql
.exit
```
### updating data
the data that will be affected by the update is determined by the where clause.
```sql
UPDATE flights
    SET duration = 430
    WHERE origin = "Nairobi"
    AND destination = "Kenya";
```
### deleting data
the data that will be affected by the delete is determined by the where clause.
```sql
DELETE FROM flights
    WHERE origin = "Nairobi"
    AND destination = "Kenya";
```
## -------------------------------------------------------------------
# RELATIONASHIPS

## foreign keys
foreign keys are used to reference data in another table, they are used to create relationships between tables.
Normalizing data is the process of organizing data in a database, this is done by creating tables that are related to each other.

```sql
CREATE TABLE passengers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    flight_id INTEGER REFERENCES flights
);
```

Having multiple tables that carry a relation is great but it messy when it comes to viewing the data of one item, which is where JOIN commands comes in.
```sql
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
```
### description
- ON passengers.flight_id = flights.id - this is the condition that will be used to join the two tables. the flight id will be what shows the relationship between the two tables.

There are other JOINS that can be used to join tables.

## -------------------------------------------------------------------
# creating an INDEX
An index is a data structure that organizes the values of a column or columns in a table, which makes it faster to retrieve data from the table.
```sql
CREATE INDEX flights_origin ON flights(origin);
```
we are creating an index on the column origin in the flights table, to decide on what values to index, you have to ask the question, what data will be queried the most.
** what will i query from this table the most, and in our case, we will oftelnly query data using the origin column. **

## -------------------------------------------------------------------
# VULNERABILITIES
### SQL INJECTION
SQL injection is a code injection technique that might destroy your database.
SQL injection is one of the most common web hacking techniques.
SQL injection is the placement of malicious code in SQL statements, via web page input.
SQL injection usually occurs when you ask a user for input, like their username/userid, and instead of a name/id, the user gives you an SQL statement that you will unknowingly run on your database.

## SOLUTION
ABSTRACTING AWAY SQL QUERIES
```python
def execute(self, operation, values=None):
    with sqlite3.connect(self.db) as conn:
        cursor = conn.cursor()
        cursor.execute(operation, values or [])
        conn.commit()
        return cursor
```

## -------------------------------------------------------------------
# race conditions
where the users do a similar action at the same time, i.e they like a post at the same time, and the system is not able to handle the requests at the same time, so it ends up liking the post twice.

## SOLUTION
locking the database when a user is performing an action, and unlocking it when the action is complete.

