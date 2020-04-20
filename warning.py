# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './warning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.wrnTxt = QtWidgets.QLabel(Dialog)
        self.wrnTxt.setGeometry(QtCore.QRect(130, 80, 161, 81))
        self.wrnTxt.setObjectName("wrnTxt")
        self.warnOkBtn = QtWidgets.QPushButton(Dialog)
        self.warnOkBtn.setGeometry(QtCore.QRect(140, 190, 117, 31))
        self.warnOkBtn.setObjectName("warnOkBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.wrnTxt.setText(_translate("Dialog", "Вы ввели \n"
"не корректное \n"
"значения"))
        self.warnOkBtn.setText(_translate("Dialog", "Вернуться"))

