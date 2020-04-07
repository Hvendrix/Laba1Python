import sys
import os
import psycopg2


def main():
    conn = psycopg2.connect(dbname='hvendrix', user='hvendrix',
                            password="200915", host='localhost', port="5432")
    cursor = conn.cursor()



    def createTable():
        cursor.execute('''CREATE TABLE clients2 (id serial PRIMARY KEY, Имя varchar(50), Фамилия varchar(50), Комментарий varchar (25), Долг int, Max_Кредит int);''')
        conn.commit()


    def insertIntoTable():

        cursor.execute(
            '''INSERT INTO clients2 (Имя, Фамилия, Комментарий, Долг, Max_Кредит) VALUES ('Иван', 'Иванов', 'надежен', 2000, 3000)'''
        )
        conn.commit()





    def selectFromTable():
        cursor.execute("SELECT id, Имя from clients2")

        rows = cursor.fetchall()
        for row in rows:
            print("id =", row[0])
            print("ИМЯ =", row[1], "\n")

        print("Operation done successfully")



    selectFromTable()


    cursor.close()
    conn.close()