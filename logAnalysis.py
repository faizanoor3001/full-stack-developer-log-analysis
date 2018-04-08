#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

sql_fetch_most_popular_articles = """ select articles.title , topThreePathViews.num as views
                                        from articles ,topThreePathViews
                                        where '/article/'||articles.slug =
                                        topThreePathViews.path
                                        order by num desc;
                                  """

sql_fetch_most_popular_author = """select authors.name as author, view3.mostViewed
                                   from authors, view3
                                   where authors.id = view3.author;
                                """

sql_fetch_days_with_more_errors = """ select time as day , CONCAT(round(percentage,2),'% errors')
                                      from errorPercent
                                      where percentage > 1
                                      order by time desc;
                                  """


def main():
    '''Create the views given in the readme.md for the below questions
        1. What are the most popular three articles of all time?
        2. Who are the most popular article authors of all time?
        3. On which days did more than 1% of requests lead to errors?
    '''

    '''To establish a connection to a postgresql database'''
    conn = psycopg2.connect(database=DBNAME)
    '''Get a cursor from the database to execute the queries'''
    cursor = conn.cursor()
    cursor.execute(sql_fetch_most_popular_articles)
    results = cursor.fetchall()
    print("1. What are the most popular three articles of all time?\n")
    for (title, views) in results:
        print("    {} - {} views".format(title, views))
        print("-" * 80)

    cursor.execute(sql_fetch_most_popular_author)
    results = cursor.fetchall()
    print("\n2. Who are the most popular article authors of all time?\n")
    for(author, mostViewed) in results:
        print(" {}  - {} views".format(author, mostViewed))
        print("-" * 80)

    cursor.execute(sql_fetch_days_with_more_errors)
    results = cursor.fetchall()
    print("\n3. On which days did more than 1% of requests lead to errors?\n")
    for(day, percentage) in results:
        print(" {}  - {} views".format(day, percentage))
        print("-" * 80)

    conn.close()


if __name__ == "__main__":
    main()
