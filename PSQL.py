import sys
import os
import psycopg2
from auth import *


def main():
    conn = psycopg2.connect(dbname=dbnameSql, user=loginSql,
                            password=passSql, host='localhost', port="5432")
    cursor = conn.cursor()

    """
    • общий счет покупок клиента (сумма всех покупок)
    • текущий счет клиента (деньги на счету фирмы для покупок);
    • потолок кредита (кредитный лимит, который не изменяется);
    • текущий долг клиента;
    • остаток кредита (разница между потолком кредита и текущим долгом);
    • комментарий (о причине долга клиента, его надежности и т.п.).
    """

    def createClients():
        cursor.execute(
            '''CREATE TABLE Клиенты (id serial PRIMARY KEY, Имя varchar(50), Фамилия varchar(50), 
            Комментарий varchar (25), Долг int, Потолок_кредита int, Остаток_кредита int, Общий_счет_покупок int,
            Общий_счет_клиента int);'''
        )
        conn.commit()

    def createGoods():
        cursor.execute(
            '''CREATE TABLE Товары (id serial PRIMARY KEY, Название varchar(50), Цена int, Количество int);'''
        )
        conn.commit()

    def createOrders():
        cursor.execute(
            '''CREATE TABLE Заказы (id serial PRIMARY KEY, id_клиента INT REFERENCES Клиенты (id) ON DELETE CASCADE, 
            id_товара INT REFERENCES Товары (id) ON DELETE CASCADE, Количество_купленного INT, Общая_цена INT); '''
        )
        conn.commit()


    def insertIntoClients(Name, LName, Komment, Dolg, Potolok, Ostatok, Cash, Schet):

        cursor.execute(
            f'''INSERT INTO Клиенты (Имя, Фамилия, Комментарий, Долг, Потолок_кредита,
            Остаток_кредита, Общий_счет_покупок, Общий_счет_клиента) 
            VALUES ('{Name}', '{LName}', '{Komment}', {Dolg}, {Potolok}, {Ostatok}, {Cash}, {Schet})'''
        )


    def insertIntoGoods():

        cursor.execute(
            '''INSERT INTO Товары (Название, Цена, Количество) VALUES ('Ноутбук', 200, 40)'''
        )
        cursor.execute(
            '''INSERT INTO Товары (Название, Цена, Количество) VALUES ('Пк', 600, 22)'''
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


    def delete_all():
        cursor.execute("DROP TABLE Заказы, Клиенты, Товары;")
        conn.commit()

    # delete_all()

    createGoods()
    insertIntoGoods()
    createClients()
    insertIntoClients('Иван', 'Иванов', 'надежен', 2000, 30000, 28000, 0, 20000)
    insertIntoClients('Денис', 'Сидоров', 'надежен', 0, 9000, 9000, 0, 6000)
    createOrders()



    # selectFromGoods()




    cursor.close()
    conn.close()


