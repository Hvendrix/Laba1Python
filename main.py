import sys
import os
import psycopg2
from auth import *


from PyQt5 import QtWidgets, QtCore, QtGui

import Form2
import Form3
import interface

import PSQL

class ExampleApp(QtWidgets.QMainWindow, Form2.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Form2.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btnBrowse.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.listWidget.addItem(file_name)  # добавить файл в listWidget

class ExampleApp3(QtWidgets.QMainWindow, Form3.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.txtBtn.clicked.connect(self.setUpText1)
        self.label.setText("Hello")
        self.label.setStyleSheet("color: rgb(28, 43, 255);")
        self.comboBox.addItem("asdasd")
        self.comboBox.addItem("qweqweqwe")

    def setUpText1(self):
        self.label.setText("qwertasd")

# подключаем бд
conn = psycopg2.connect(dbname=dbnameSql, user=loginSql,
                        password=passSql, host='localhost', port="5432")
cursor = conn.cursor()



class Interface(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setNameIntoNameBox()

        self.NameBox.currentIndexChanged.connect(self.loadDataFromName)








    def setNameIntoNameBox(self):
        cursor.execute("SELECT id, Имя from Клиенты")
        rows = cursor.fetchall()
        for row in rows:
            self.NameBox.addItem(row[1])



    def setUpText1(self):
        indexB = self.NameBox.currentText()
        self.KommentTxt.setText(indexB)


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






def main():
    print("Let's start")

    PSQL.main()



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