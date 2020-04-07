import sys
import os
import psycopg2


def main():

    conn = psycopg2.connect(dbname='hvendrix', user='hvendrix',
                            password="200915", host='localhost', port="5432")
    cursor = conn.cursor()

    cursor.execute("SELECT id, Имя from clients2")

    rows = cursor.fetchall()
    for row in rows:
        print("id =", row[0])
        print("ИМЯ =", row[1], "\n")

    print("Operation done successfully")


    cursor.close()
    conn.close()