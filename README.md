# full-stack-developer-log-analysis
LogAnalysis


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

