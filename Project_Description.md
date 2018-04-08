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

## Explore the data
Once you have the data loaded into your database, connect to your database using ``` psql -d news ``` and explore the tables using the ``` \dt ``` and ``` \d table ``` commands and select statements.

* ``` \dt ``` — display tables — lists the tables that are available in the database.
* ``` \d table ```— (replace table with the name of a table) — shows the database schema for that particular table.

Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.

As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

### Connecting from your code
The database that you're working with in this project is running PostgreSQL, like the forum database that you worked with in the course. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

```
db = psycopg2.connect("dbname=news")
```


## Your assignment: Build it!
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the `psycopg2` module to connect to the database.

### So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

** 1. What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

**Example**:

* "Princess Shellfish Marries Prince Handsome" — 1201 views
* "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
* "Political Scandal Ends In Political Scandal" — 553 views

**2. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**Example:**

* Ursula La Multa — 2304 views
* Rudolf von Treppenwitz — 1985 views
* Markoff Chaney — 1723 views
* Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)

**Example:**

* July 29, 2016 — 2.5% errors

### Good coding practices
#### SQL style
Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the `where` clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

In building this tool, you may find it useful to add views to the database. You are allowed and encouraged to do this! However, if you create views, make sure to put the **create view** commands you used into your lab's README file so your reviewer will know how to recreate them.

#### Python code quality
Your code should be written with good Python style. The [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/) is an excellent standard to follow. You can do a quick check using the `pep8` command-line tool.


## Frequently asked questions

### Q: I modified my database. Can I undo it?
If you'd like to revert the `news` database to its original form, you can do that by dropping each of the tables, then re-importing the data from the `newsdata.sql` file.

In `psql`:

```sql
drop table log;
drop table articles;
drop table authors;
```

Then in the shell, re-import the data:

```bash
psql -d news -f newsdata.sql
```

### Q: These queries are complicated. Where do I start?
One of the best ways to build complex queries is by starting with smaller pieces, and testing each of them in small steps. Here's a worked example —

Suppose we wanted to print out each article's title and author name.

Looking at the schema for `articles` (with `\d articles`) we can see there's an author and title column. But the author column doesn't have names in it — just numbers. To see this in your database, run:

```sql
select author from articles;
```

But the `authors` table has a `name` column, and a numeric `id` column. To see this, run:

```sql
select * from authors;
```

Those numeric id values match up with the `articles.author` column. And that means we can connect the two tables with a join:

```sql
select title, name
from articles join authors
on article.author = authors.id;
```

or:

```sql
select title, name
from articles, authors
where articles.author = authors.id;
```
Try these queries on your `news` database! Look for other relationships that can work with `join`.

