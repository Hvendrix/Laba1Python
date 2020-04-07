import sys
import os
import psycopg2
from PyQt5 import QtWidgets

import Form2
import Form3

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


def main():

    # conn = psycopg2.connect(dbname='hvendrix', user='hvendrix',
    #                         password="", host='127.0.0.1', port="5432")
    # cursor = conn.cursor()
    # print(cursor.execute("SELECT * FROM playground"))


    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp3()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()