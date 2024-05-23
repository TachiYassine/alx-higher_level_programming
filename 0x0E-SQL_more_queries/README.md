# MySQL Quick Reference

## General

### How to create a new MySQL user
Use `CREATE USER 'username'@'host' IDENTIFIED BY 'password';`.

### How to manage privileges for a user to a database or table
Use `GRANT privileges ON database.table TO 'username'@'host';`.

### What’s a PRIMARY KEY
A unique identifier for each record in a table.

### What’s a FOREIGN KEY
A field in one table that links to the PRIMARY KEY of another table.

### How to use NOT NULL and UNIQUE constraints
Use `NOT NULL` to ensure a column cannot have a NULL value, and `UNIQUE` to ensure all values in a column are distinct.

### How to retrieve data from multiple tables in one request
Use `JOIN` clauses in your SQL query.

### What are subqueries
Queries nested inside another query.

### What are JOIN and UNION
`JOIN` combines rows from multiple tables based on related columns, and `UNION` combines results from multiple SELECT queries.
