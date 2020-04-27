import sys
import os
import psycopg2

from PyQt5 import QtWidgets, QtCore, QtGui
import interface
import warning
import Barter
from PyQt5.QtWidgets import QHeaderView
import PSQL
from auth import *


# подключаем бд
conn = psycopg2.connect(dbname=dbnameSql, user=loginSql,
                        password=passSql, host='localhost', port="5432")
cursor = conn.cursor()

globalName = ""

class Interface(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setNameIntoNameBox()
        self.setGoodsNameIntoGoodsNameBox()
        self.setOperIntoOperTypeBox()

        self.warningTxt.setText("ok")

        self.initLoadDataFromName()

        self.NameBox.currentIndexChanged.connect(self.initLoadDataFromName)

        self.amountSpinBox.valueChanged.connect(self.changeManyCash)
        self.amountSpinBox.valueChanged.connect(self.warningStoreCount)

        self.GoodsNameBox.currentIndexChanged.connect(self.changeOneCash)
        self.GoodsNameBox.currentIndexChanged.connect(self.changeManyCash)
        self.GoodsNameBox.currentIndexChanged.connect(self.warningStoreCount)
        self.OperTypeBox.currentIndexChanged.connect(self.changeManyCash)
        self.OperTypeBox.currentIndexChanged.connect(self.barterWindow)

        self.nextBtn.clicked.connect(self.nextBtnPressed)
        self.nextBtn.clicked.connect(self.initLoadDataFromName)
        self.nextBtn.clicked.connect(self.changeManyCash)
        self.nextBtn.clicked.connect(self.warningStoreCount)
        self.delBtn.clicked.connect(self.delete_all)
        self.delBtn.clicked.connect(self.initLoadDataFromName)

        self.tableWidget.horizontalHeader().setMinimumSectionSize(75)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.allOrdersTable.horizontalHeader().setMinimumSectionSize(75)
        self.allOrdersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.barterWindow()


    def warning(self, code):

        window2 = Warning()
        window2.setModal(True)
        # window2.show()
        window2.exec_()

    def delete_all(self):
        cursor.execute(
            f"""DROP TABLE Заказы, Клиенты, Товары;"""
        )
        conn.commit()
        PSQL.main()

    def barterWindow(self):
        if self.OperTypeBox.currentText() == "Бартер":
            global globalName
            globalName = self.NameBox.currentText()
            window = Barter()
            window.setModal(True)
            window.exec_()
            self.changeManyCash()
            self.OperTypeBox.setCurrentIndex(1)
            self.loadDataForOrders()


    def nextBtnPressed(self):
        warnControl = self.warningTxt.text()
        if warnControl != "ok":
            print("go out")
            self.warning(1)
            return


        NameKlient = str(self.NameBox.currentText())
        NameGoods = str(self.GoodsNameBox.currentText())
        countOrder = self.amountSpinBox.value()
        allCash = int(self.manyCashTxt.text())
        OperType = str(self.OperTypeBox.currentText())


        cursor.execute(
            f'''SELECT Долг, Потолок_кредита, Общий_счет_клиента FROM Клиенты WHERE Имя = '{NameKlient}';'''
        )
        dolgAndMax = cursor.fetchall()





        if OperType == "Кредит":
            if (dolgAndMax[0][0] + allCash) > dolgAndMax[0][1]:
                self.warning(1)
                print("warning")
                return
            cursor.execute(
                f'''UPDATE Клиенты SET Долг = Долг + {allCash}, Остаток_кредита = Остаток_кредита - {allCash} WHERE Имя='{NameKlient}';'''
            )
            print("долг")
            conn.commit()

        if OperType == "Безналичный расчет":
            if (dolgAndMax[0][2] < allCash):
                self.warning(1)
                return
            cursor.execute(
                f"""UPDATE Клиенты SET Общий_счет_клиента = Общий_счет_клиента - {allCash} WHERE Имя = '{NameKlient}';"""
            )
            conn.commit()

        if OperType == "Взаимозачет":
            countOrder = - countOrder
            cursor.execute(
                f'''UPDATE Клиенты SET Долг = Долг - {allCash}, Остаток_кредита = Остаток_кредита + {allCash} WHERE Имя='{NameKlient}';'''
            )
            conn.commit()

            allCash = 0

        cursor.execute(
            f"""UPDATE Клиенты SET Общий_счет_покупок = Общий_счет_покупок + {allCash} WHERE Имя = '{NameKlient}';"""
        )
        conn.commit()

        cursor.execute(
            f"""UPDATE Товары SET Количество = Количество - {countOrder} WHERE Название = '{NameGoods}';"""
        )
        conn.commit()

        cursor.execute(
            f"""INSERT INTO Заказы (id_клиента, id_товара, Количество_купленного, Общая_цена) VALUES ((
            SELECT id FROM Клиенты WHERE Имя='{NameKlient}'), (SELECT id FROM Товары WHERE Название='{NameGoods}'), 
            {countOrder}, {allCash}); """
        )
        conn.commit()




        self.loadDataForOrders()

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
        if self.OperTypeBox.currentText() == "Взаимозачет":
            self.amountOnStoreTxt.setText(str(rows[0][1] + many))

    def warningStoreCount(self):
        count = str(self.amountOnStoreTxt.text())
        if int(count) < 0:
            self.warningTxt.setText("Вы заказываете больше, \nтоваров чем есть на складе \nзаказ выведет ошибку!!!")
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
        self.manyCashTxt.setText(str(rows[0][0]))

    def initLoadDataFromName(self):
        name = self.NameBox.currentText()
        sName = str(name)
        cursor.execute(
            f'''SELECT Имя, Комментарий, Долг, Потолок_кредита,
            Остаток_кредита, Общий_счет_покупок, Общий_счет_клиента FROM Клиенты WHERE Имя = '{sName}';'''
        )
        all_data = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(all_data[0]))


        # Названия для столбцов
        column_names = ['Имя', 'Комментарий', 'Долг', 'Потолок_кредита',  'Остаток_кредита', 'Общий_счет_покупок', 'Общий_счет_клиента']
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
        self.NameGoodsLoad()
        self.changeAnyBox()
        self.count()
        self.okBtn.clicked.connect(self.update)
        self.cancelBtn.clicked.connect(self.close)

    def changeAnyBox(self):
        self.ClientCountSpinBox.valueChanged.connect(self.price)
        self.StoreCountSpinBox.valueChanged.connect(self.price)
        self.ClientGoodsNameBox.currentIndexChanged.connect(self.price)
        self.StoreGoodsNameBox.currentIndexChanged.connect(self.price)
        self.StoreGoodsNameBox.currentIndexChanged.connect(self.count)

    def NameGoodsLoad(self):
        for row in self.selectGoods():
            self.StoreGoodsNameBox.addItem(row[0])
            self.ClientGoodsNameBox.addItem(row[0])
        self.price()
    def price(self):
        for row in self.selectGoods(self.StoreGoodsNameBox.currentText()):
            self.StorePrice.setText(str(row[1]*self.StoreCountSpinBox.value()))
        for row in self.selectGoods(self.ClientGoodsNameBox.currentText()):
            self.ClientPrice.setText(str(row[1]*self.ClientCountSpinBox.value()))
    def count(self):
        for row in self.selectGoods(self.StoreGoodsNameBox.currentText()):
            self.countOnStore.setText(str(row[2]))
    def selectGoods(self, name=None):
        if isinstance(name, str):
            cursor.execute(
                f"""SELECT Название, Цена, Количество From Товары WHERE Название='{name}';"""
            )
            return cursor.fetchall()
        else:
            cursor.execute(
                f"""SELECT Название, Цена, Количество From Товары;"""
            )
            return cursor.fetchall()
    def update(self):
        global globalName
        if self.ClientPrice.text() != self.StorePrice.text():
            self.warning(1)
            return
        if self.StoreCountSpinBox.value() > int(self.countOnStore.text()):
            self.warning(1)
            return
        if self.StoreGoodsNameBox.currentText() == self.ClientGoodsNameBox.currentText():
            self.warning(1)
            return
        cursor.execute(
            f"""UPDATE Товары SET Количество = Количество + {self.ClientCountSpinBox.value()} 
            WHERE Название = '{self.ClientGoodsNameBox.currentText()}';"""
        )
        conn.commit()
        cursor.execute(
            f"""INSERT INTO Заказы (id_клиента, id_товара, Количество_купленного) VALUES ((
                    SELECT id FROM Клиенты WHERE Имя='{globalName}'), (SELECT id FROM Товары 
                    WHERE Название='{self.StoreGoodsNameBox.currentText()}'), 
                    {self.StoreCountSpinBox.value()}); """
        )
        conn.commit()
        self.close()

    def warning(self, code):
        window2 = Warning(1)
        window2.setModal(True)
        # window2.show()
        window2.exec_()

class Warning(QtWidgets.QDialog, warning.Ui_Dialog):
    def __init__(self, code=None):
        super().__init__()
        self.setupUi(self)
        self.warnOkBtn.clicked.connect(self.exit_warn)


    def exit_warn(self):
        self.close()

def printTest(*scores):
    for score in scores:
        print(score)
def main():
    print("Let's start")
    printTest(1,2,3,4)
    # PSQL.main()

    a = [1, 5, 9, 2]
    for i, x in enumerate(a):
        print("test", i, x)

    b = [*a, 9, 10, 11]
    print(b)

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