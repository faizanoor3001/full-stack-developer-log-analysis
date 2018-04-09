--- View Scripts File for all the three Questions 

--- for Question 1 : 

create view topThreePathViews AS select path , count(*) as num from log 
group by path order by num desc LIMIT 3 OFFSET 1;


--- for Question 2 : 


create view view1 AS select path , count(*) as num from log group by path order by num desc;


create view view2new as select articles.title ,articles.author, view1.num as views from articles ,
view1 where '/article/'||articles.slug = view1.path order by num desc;

 
create view view3 as select sum(views) as mostViewed, view2new.author from view2new group by author order
by author ; 


---for Question 3 :

create view viewStatusAll as select time::date ,  count(*) as status from log group by time::date order by time::date;


create view viewStatusNotFound as select time::date ,  count(*) as status from log 
where status='404 NOT FOUND' group by time::date order by time::date;


create view errorPercent as select viewStatusAll.time , (100.0 * viewStatusNotFound.status/viewStatusAll.status) as percentage from 
viewStatusAll , viewStatusNotFound where viewStatusAll.time = viewStatusNotFound.time order by viewStatusAll.time;