# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1163, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(186, 247, 247);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color: rgb(36, 88, 122);")
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.amountSpinBox = QtWidgets.QSpinBox(self.tab)
        self.amountSpinBox.setStyleSheet("\n"
"background-color: #FFA200;")
        self.amountSpinBox.setMinimum(1)
        self.amountSpinBox.setObjectName("amountSpinBox")
        self.gridLayout.addWidget(self.amountSpinBox, 4, 0, 1, 1)
        self.OperTypeBox = QtWidgets.QComboBox(self.tab)
        self.OperTypeBox.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.OperTypeBox.setObjectName("OperTypeBox")
        self.gridLayout.addWidget(self.OperTypeBox, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.NameBox = QtWidgets.QComboBox(self.tab)
        self.NameBox.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.NameBox.setObjectName("NameBox")
        self.gridLayout.addWidget(self.NameBox, 0, 1, 1, 1)
        self.amountOnStoreTxt = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amountOnStoreTxt.sizePolicy().hasHeightForWidth())
        self.amountOnStoreTxt.setSizePolicy(sizePolicy)
        self.amountOnStoreTxt.setMinimumSize(QtCore.QSize(100, 0))
        self.amountOnStoreTxt.setStyleSheet("\n"
"background-color: #FFA200;")
        self.amountOnStoreTxt.setObjectName("amountOnStoreTxt")
        self.gridLayout.addWidget(self.amountOnStoreTxt, 3, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.tableWidget.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 5)
        self.oneCashTxt = QtWidgets.QLabel(self.tab)
        self.oneCashTxt.setStyleSheet("\n"
"background-color: #FFA200;")
        self.oneCashTxt.setObjectName("oneCashTxt")
        self.gridLayout.addWidget(self.oneCashTxt, 4, 2, 1, 1)
        self.nextBtn = QtWidgets.QPushButton(self.tab)
        self.nextBtn.setStyleSheet("\n"
"background-color: #FFA200;")
        self.nextBtn.setObjectName("nextBtn")
        self.gridLayout.addWidget(self.nextBtn, 6, 0, 1, 1)
        self.GoodsNameBox = QtWidgets.QComboBox(self.tab)
        self.GoodsNameBox.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.GoodsNameBox.setObjectName("GoodsNameBox")
        self.gridLayout.addWidget(self.GoodsNameBox, 3, 1, 1, 1)
        self.loadBtn = QtWidgets.QPushButton(self.tab)
        self.loadBtn.setObjectName("loadBtn")
        self.gridLayout.addWidget(self.loadBtn, 6, 3, 1, 1)
        self.delBtn = QtWidgets.QPushButton(self.tab)
        self.delBtn.setObjectName("delBtn")
        self.gridLayout.addWidget(self.delBtn, 6, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setStyleSheet("\n"
"background-color: rgb(101, 166, 209);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)
        self.manyCashTxt = QtWidgets.QLabel(self.tab)
        self.manyCashTxt.setStyleSheet("\n"
"background-color: #FFA200;")
        self.manyCashTxt.setObjectName("manyCashTxt")
        self.gridLayout.addWidget(self.manyCashTxt, 4, 4, 1, 1)
        self.warningTxt = QtWidgets.QLabel(self.tab)
        self.warningTxt.setStyleSheet("color: rgb(204, 0, 0);\n"
"\n"
"background-color: rgb(101, 166, 209);")
        self.warningTxt.setObjectName("warningTxt")
        self.gridLayout.addWidget(self.warningTxt, 5, 1, 2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.allOrdersTable = QtWidgets.QTableWidget(self.tab_2)
        self.allOrdersTable.setObjectName("allOrdersTable")
        self.allOrdersTable.setColumnCount(0)
        self.allOrdersTable.setRowCount(0)
        self.gridLayout_2.addWidget(self.allOrdersTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.allPrice = QtWidgets.QLabel(self.centralwidget)
        self.allPrice.setText("")
        self.allPrice.setObjectName("allPrice")
        self.verticalLayout.addWidget(self.allPrice)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Цена за одну штуку"))
        self.label_2.setText(_translate("MainWindow", "Введите Имя"))
        self.amountOnStoreTxt.setText(_translate("MainWindow", "0"))
        self.oneCashTxt.setText(_translate("MainWindow", "0"))
        self.nextBtn.setText(_translate("MainWindow", "Продолжить"))
        self.loadBtn.setText(_translate("MainWindow", "Load"))
        self.delBtn.setText(_translate("MainWindow", "Удалить данные"))
        self.label.setText(_translate("MainWindow", "Название товара:"))
        self.label_3.setText(_translate("MainWindow", "Количество на складе:"))
        self.label_5.setText(_translate("MainWindow", "Цена за все:"))
        self.manyCashTxt.setText(_translate("MainWindow", "0"))
        self.warningTxt.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#cc0000;\"><br/></span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Оформление заказа"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Все заказы"))
        self.label_6.setText(_translate("MainWindow", "Общая цена всех заказов:"))

