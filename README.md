# Project - Log Analysis


## [Project_Description](Project_Description.md)


## Questions
1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Requirements
* Python 3.5.3
* psycopg2
* Postgresql 9.6

## How to run

* load the data onto the database
```sql
psql -d news -f newsdata.sql
```
* connect to the database
```sql
psql -d news
```
* create views from the ViewScripts.sq; file or you can copy the scripts from below in the README.md file.
* python3 LogsAnalysis.py

## Views Description : 

#### For the first question , create the below view : 

```sql
create view topThreePathViews AS select path , count(*) as num from log group by path order by num desc LIMIT 3 OFFSET 1;
```


#### For the Second question create below views : 

```sql
create view view1 AS select path , count(*) as num from log group by path order by num desc;
```

```sql
 create view view2new as select articles.title ,articles.author, view1.num as views from articles , view1 where '/article/'||articles.slug = view1.path order by num desc;
```

```sql
create view view3 as select sum(views) as mostViewed, view2new.author from view2new group by author order
by author ;
```

#### For the third question , create below views : 

All positive and negative status logs: 

```sql
create view viewStatusAll as select time::date ,  count(*) as status from log group by time::date order by time::date;
```
All failed status logs: 

```sql
create view viewStatusNotFound as select time::date ,  count(*) as status from log where status='404 NOT FOUND' group by time::date order by time::date;
```

Error Percentage status :

```sql
create view errorPercent as select viewStatusAll.time , (100.0 * viewStatusNotFound.status/viewStatusAll.status) as percentage from viewStatusAll , viewStatusNotFound where viewStatusAll.time = viewStatusNotFound.time order
by viewStatusAll.time;
```


NOTE: The project description part has been taken up from the Udacity's Site , where we have defined what needs to be done in this project. 
