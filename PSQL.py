import sys
import os
import psycopg2
from auth import *


def main():
    conn = psycopg2.connect(dbname=dbnameSql, user=loginSql,
                            password=passSql, host='localhost', port="5432")
    cursor = conn.cursor()



    def createClients():
        cursor.execute(
            '''CREATE TABLE Клиенты (id serial PRIMARY KEY, Имя varchar(50), Фамилия varchar(50), 
            Комментарий varchar (25), Долг int, Max_Кредит int);'''
        )
        conn.commit()

    def createGoods():
        cursor.execute(
            '''CREATE TABLE Товары (id serial PRIMARY KEY, Название varchar(50), Цена int, Количество int);'''
        )
        conn.commit()


    def insertIntoClients():

        cursor.execute(
            '''INSERT INTO Клиенты (Имя, Фамилия, Комментарий, Долг, Max_Кредит) VALUES ('Иван', 'Иванов', 'надежен', 2000, 3000)'''
        )

        cursor.execute(
            '''INSERT INTO Клиенты (Имя, Фамилия, Комментарий, Долг, Max_Кредит) VALUES ('Денис', 'Сидоров', 'надежен', 4000, 9000)'''
        )
        conn.commit()

    def insertIntoGoods():

        cursor.execute(
            '''INSERT INTO Товары (Название, Цена, Количество) VALUES ('Приора', 20000, 4)'''
        )
        cursor.execute(
            '''INSERT INTO Товары (Название, Цена, Количество) VALUES ('Lada', 60000, 2)'''
        )
        conn.commit()


    def selectFromClients():
        cursor.execute("SELECT id, Имя from Клиенты")

        rows = cursor.fetchall()
        for row in rows:
            print("id =", row[0])
            print("ИМЯ =", row[1], "\n")

        print("Operation done successfully")

    def selectFromGoods():
        cursor.execute("SELECT id, Название from Товары")

        rows = cursor.fetchall()
        for row in rows:
            print("id =", row[0])
            print("ИМЯ =", row[1], "\n")

        print("Operation done successfully")



    # createGoods()
    # insertIntoGoods()
    # #selectFromGoods()
    #
    #
    #
    # createClients()
    # insertIntoClients()

    cursor.close()
    conn.close()