# full-stack-developer-log-analysis
LogAnalysis


Views Description : 

For the first question , create the below view : 

create view topThreePathViews AS select path , count(*) as num from log group by path order by num desc LIMIT 3 OFFSET 1;

query : 
select articles.title , topThreePathViews.num as views from articles , topThreePathViews where '/article/'||articles.slug = topThreePathViews.path order by num desc;

