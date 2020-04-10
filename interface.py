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
        MainWindow.resize(882, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.OperTypeBox = QtWidgets.QComboBox(self.tab)
        self.OperTypeBox.setObjectName("OperTypeBox")
        self.gridLayout.addWidget(self.OperTypeBox, 2, 0, 1, 1)
        self.GoodsNameBox = QtWidgets.QComboBox(self.tab)
        self.GoodsNameBox.setObjectName("GoodsNameBox")
        self.gridLayout.addWidget(self.GoodsNameBox, 3, 0, 1, 1)
        self.loadBtn = QtWidgets.QPushButton(self.tab)
        self.loadBtn.setObjectName("loadBtn")
        self.gridLayout.addWidget(self.loadBtn, 5, 0, 1, 1)
        self.NameBox = QtWidgets.QComboBox(self.tab)
        self.NameBox.setObjectName("NameBox")
        self.gridLayout.addWidget(self.NameBox, 0, 0, 1, 1)
        self.KommentTxt = QtWidgets.QLabel(self.tab)
        self.KommentTxt.setObjectName("KommentTxt")
        self.gridLayout.addWidget(self.KommentTxt, 0, 2, 1, 1)
        self.oneCashTxt = QtWidgets.QLabel(self.tab)
        self.oneCashTxt.setObjectName("oneCashTxt")
        self.gridLayout.addWidget(self.oneCashTxt, 4, 1, 1, 1)
        self.manyCashTxt = QtWidgets.QLabel(self.tab)
        self.manyCashTxt.setObjectName("manyCashTxt")
        self.gridLayout.addWidget(self.manyCashTxt, 4, 2, 1, 1)
        self.amountSpinBox = QtWidgets.QSpinBox(self.tab)
        self.amountSpinBox.setObjectName("amountSpinBox")
        self.gridLayout.addWidget(self.amountSpinBox, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadBtn.setText(_translate("MainWindow", "Load"))
        self.KommentTxt.setText(_translate("MainWindow", "TextLabel"))
        self.oneCashTxt.setText(_translate("MainWindow", "TextLabel"))
        self.manyCashTxt.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

