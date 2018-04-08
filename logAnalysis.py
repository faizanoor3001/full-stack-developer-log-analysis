#python --version 3.6.4

import psycopg2

DBNAME = "news"

def logAnalysis():

    conn = psycopg2.connect("dbname=DBNAME")
    cursor1 = conn.cursor()
    cursor1.execute()
    results = cursor1.fetchall()
    print(results)

    cursor2 = conn.cursor()
    cursor2.execute()
    results = cursor2.fetchall()
    print(results)

    cursor3 = conn.cursor()
    cursor3.execute()
    results = cursor3.fetchall()
    print(results)


    
    conn.close();
    
