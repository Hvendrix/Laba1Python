import sys
import os
import psycopg2

from PyQt5 import QtWidgets, QtCore, QtGui
import interface
import Barter

import PSQL
from auth import *


# подключаем бд
conn = psycopg2.connect(dbname=dbnameSql, user=loginSql,
                        password=passSql, host='localhost', port="5432")
cursor = conn.cursor()



class Interface(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setNameIntoNameBox()
        self.setGoodsNameIntoGoodsNameBox()
        self.setOperIntoOperTypeBox()

        self.loadDataFromName()

        self.NameBox.currentIndexChanged.connect(self.loadDataFromName)

        self.amountSpinBox.valueChanged.connect(self.changeManyCash)
        self.amountSpinBox.valueChanged.connect(self.warningStoreCount)

        self.GoodsNameBox.currentIndexChanged.connect(self.changeOneCash)
        self.GoodsNameBox.currentIndexChanged.connect(self.changeManyCash)
        self.GoodsNameBox.currentIndexChanged.connect(self.warningStoreCount)

        self.nextBtn.clicked.connect(self.nextBtnPressed)





    def nextBtnPressed(self):
        x = 3
        if x == 3:
            print("go out")
            return
        NameKlient = str(self.NameBox.currentText())
        NameGoods = str(self.GoodsNameBox.currentText())
        countOrder = self.amountSpinBox.value()
        allCash = int(self.manyCashTxt.text())

        cursor.execute(
            f"""INSERT INTO Заказы (id_клиента, id_товара, Количество_купленного, Общая_цена) VALUES ((
            SELECT id FROM Клиенты WHERE Имя='{NameKlient}'), (SELECT id FROM Товары WHERE Название='{NameGoods}'), 
            {countOrder}, {allCash}); """
        )
        conn.commit()

        self.loadDataForOrders()

        # window2 = Barter()
        # window2.setModal(True)
        # # window2.show()
        # window2.exec_()




    def changeOneCash(self):
        oneName = str(self.GoodsNameBox.currentText())
        cursor.execute(f"""SELECT Цена, Количество FROM Товары WHERE Название = '{oneName}';""")
        rows = cursor.fetchall()
        self.oneCashTxt.setText(str(rows[0][0]))
        self.amountOnStoreTxt.setText(str(rows[0][1]))

    def changeManyCash(self):
        print(self.amountSpinBox.value())
        many = self.amountSpinBox.value()
        oneName = self.GoodsNameBox.currentText()

        cursor.execute(f"""SELECT Цена, Количество FROM Товары where Название = '{oneName}' """)
        rows = cursor.fetchall()
        one = rows[0][0]
        self.manyCashTxt.setText(str(one * many))
        self.amountOnStoreTxt.setText(str(rows[0][1]-many))

    def warningStoreCount(self):
        count = str(self.amountOnStoreTxt.text())
        if int(count) < 0:
            self.warningTxt.setText("Внимание!!! \n Вы заказываете больше товаров, \n чем есть на складе \n заказ выведет ошибку")
        else:
            self.warningTxt.setText("ok")




    def setOperIntoOperTypeBox(self):
        self.OperTypeBox.addItem("Наличный расчет")
        self.OperTypeBox.addItem("Безналичный расчет")
        self.OperTypeBox.addItem("Кредит")
        self.OperTypeBox.addItem("Бартер")
        self.OperTypeBox.addItem("Взаимозачет")

    def setNameIntoNameBox(self):
        cursor.execute("SELECT Имя FROM Клиенты;")
        rows = cursor.fetchall()
        for row in rows:
            self.NameBox.addItem(row[0])

    def setGoodsNameIntoGoodsNameBox(self):
        cursor.execute("SELECT Название FROM Товары;")
        rows = cursor.fetchall()
        for row in rows:
            self.GoodsNameBox.addItem(row[0])

        cursor.execute("SELECT Цена, Количество FROM Товары WHERE id = 1;")
        rows = cursor.fetchall()
        self.oneCashTxt.setText(str(rows[0][0]))
        self.amountOnStoreTxt.setText(str(rows[0][1]))

    # def setUpText1(self):
    #     indexB = self.NameBox.currentText()
    #     self.KommentTxt.setText(indexB)


    def loadDataFromName(self):
        name = self.NameBox.currentText()
        sName = str(name)
        cursor.execute(f'''SELECT Имя, Комментарий, Долг, Max_Кредит FROM Клиенты WHERE Имя = '{sName}';''')
        all_data = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(all_data[0]))


        # Названия для столбцов
        column_names = ['Имя', 'Комментарий', 'Долг', 'Макс. кредит']
        def to_table_item(item):
            return QtWidgets.QTableWidgetItem(str(item))
        for i, el in enumerate(column_names):
            #self.tableWidget.insertColumn(i)
            self.tableWidget.setHorizontalHeaderItem(i, to_table_item(el))

        # Заполнение таблицы значениями
        for row_number, row_data in enumerate(all_data):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def loadDataForOrders(self):
        cursor.execute(
            f'''SELECT O.id, K.Имя, G.Название, O.Количество_купленного, O.Общая_цена
            FROM Заказы AS O, Товары AS G, Клиенты AS K WHERE O.id_клиента=K.id AND 
            O.id_товара=G.id;''')
        all_data = cursor.fetchall()
        self.allOrdersTable.setRowCount(0)
        self.allOrdersTable.setColumnCount(len(all_data[0]))


        # Названия для столбцов
        column_names = ['id', 'Заказчик', 'Товар', 'Количество', 'Общая_цена']
        def to_table_item(item):
            return QtWidgets.QTableWidgetItem(str(item))
        for i, el in enumerate(column_names):
            #self.tableWidget.insertColumn(i)
            self.allOrdersTable.setHorizontalHeaderItem(i, to_table_item(el))

        # Заполнение таблицы значениями
        for row_number, row_data in enumerate(all_data):
            self.allOrdersTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.allOrdersTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



class Barter(QtWidgets.QDialog, Barter.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)






def main():
    print("Let's start")
    PSQL.main()

    a = [1, 5, 9, 2]
    for i, x in enumerate(a):
        print("test", i, x)


    cursor.execute(f'''SELECT Название, Количество FROM Товары''')

    row = cursor.fetchall()
    print(row)



    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    app.exec_()

    cursor.close()


if __name__ == '__main__':
    main()



# def trash():
#     self.loadBtn.clicked.connect(self.loadData)
#     def loadData(self):
#         cursor.execute('SELECT * FROM Товары;')
#         all_data = cursor.fetchall()
#         self.tableWidget.setRowCount(0)
#         self.tableWidget.setColumnCount(len(all_data[0]))
#         for row_number, row_data in enumerate(all_data):
#             self.tableWidget.insertRow(row_number)
#             for column_number, data in enumerate(row_data):
#                 self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))