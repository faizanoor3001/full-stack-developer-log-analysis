# Project - Log Analysis


## [Project Description]

Views Description : 

For the first question , create the below view : 

create view topThreePathViews AS select path , count(*) as num from log group by path order by num desc LIMIT 3 OFFSET 1;

query : 
select articles.title , topThreePathViews.num as views from articles , topThreePathViews where '/article/'||articles.slug = topThreePathViews.path order by num desc;

For the Second question create below views : 



View 1:
create view view1 AS select path , count(*) as num from log group by path order by num desc;


View 2:
 create view view2new as select articles.title ,articles.author, view1.num as views from articles , view1 wher
e '/article/'||articles.slug = view1.path order by num desc;


View 3:

create view view3 as select sum(views) as mostViewed, view2new.author from view2new group by author order
by author ;

#need to remove the query from readme.md

final query :
    
select authors.name , view3.mostViewed from authors,
view3 where authors.id = view3.author;


Question 3: 

All positive and negative status logs: 

create view viewStatusAll as select time::date ,  count(*) as status from log group by time::date order by time::date;

All failed status logs: 

 create view viewStatusNotFound as select time::date ,  count(*) as status from log where status='404 NOT FOUND' group by time::date order by time::date;

Error Percentage status :

create view errorPercent as select viewStatusAll.time , (100.0 * viewStatusNotFound.status/viewStatusAll.stat
us ) as percentage from viewStatusAll , viewStatusNotFound where viewStatusAll.time = viewStatusNotFound.time order
by viewStatusAll.time;

Query :

select time from errorPercent where percentage > 1 order by time desc;


