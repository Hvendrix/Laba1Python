import sys
import os
import psycopg2


def main():

    conn = psycopg2.connect(dbname='hvendrix', user='hvendrix',
                            password="200915", host='localhost', port="5432")
    cursor = conn.cursor()

    cursor.execute(
        '''INSERT INTO clients2 (Имя, Фамилия, Комментарий, Долг, Max_Кредит) VALUES ('Иван', 'Иванов', 'надежен', 2000, 3000)'''
    )
    conn.commit()

    print(cursor.execute('''SELECT * FROM clients2'''))



    cursor.close()
    conn.close()