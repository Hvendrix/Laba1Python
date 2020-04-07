import sys
import os
import psycopg2


def main():

    conn = psycopg2.connect(dbname='hvendrix', user='hvendrix',
                            password="200915", host='localhost', port="5432")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE clients2 (id serial PRIMARY KEY, Имя varchar(50), Фамилия varchar(50), Комментарий varchar (25), Долг int, Max_Кредит int);''')
    conn.commit()

    print(cursor.execute("SELECT * FROM clients"))

    cursor.close()
    conn.close()