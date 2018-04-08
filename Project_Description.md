# Project Description

### Overview

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

### The PostgreSQL documentation
In this project, you'll be using a PostgreSQL database. If you'd like to know a lot more about the kinds of queries that you can use in this dialect of SQL, check out the PostgreSQL documentation. It's a lot of detail, but it spells out all the many things the database can do.

Here are some parts that may be particularly useful to refer to:


* [The select statement](https://www.postgresql.org/docs/9.5/static/sql-select.html)
* [SQL string functions](https://www.postgresql.org/docs/9.5/static/functions-string.html)
* [Aggregate functions](https://www.postgresql.org/docs/9.5/static/functions-aggregate.html)

To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

### Download the data
Next, download the data here. 
You will need to unzip [newsdata.sql file](newsdata.sql) file after downloading it. 
The file inside is called ```newsdata.sql. ```

To build the reporting tool, you'll need to load the site's data into your local database. 

To load the data, cd into directory having psql setup and use the command 
```
psql -d news -f newsdata.sql
```
Here's what this command does:

* ``` psql ``` — the PostgreSQL command line program
* ``` -d news ``` connect to the database named news which has been set up for you
* ``` -f newsdata.sql ``` run the SQL statements in the file ``` newsdata.sql ```

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

Getting an error?

If this command gives an error message, such as —

```
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
```

this means the database server is not running or is not set up correctly. 
