# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PanelJournal_v15.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import threading
import time
import sys
import GlobalValues

app = QtWidgets.QApplication(sys.argv)

class Ui_MesBox(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(347, 117)
        self.setStyleSheet("")
        self.btnOK = QtWidgets.QPushButton(self)
        self.btnOK.setGeometry(QtCore.QRect(135, 77, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnOK.setFont(font)
        self.btnOK.setStyleSheet("QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                 "color: rgb(0,0,0);\n"
                                 "border-radius:3px;\n"
                                 "border:1px solid rgb(135,135,135);}\n"
                                 "\n"
                                 "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "border-radius:3px;\n"
                                 "border:1px solid rgb(63,63,63);}\n"
                                 "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "border-radius:3px;\n"
                                 "border:1px solid rgb(63,63,63);};")
        self.btnOK.setObjectName("btnOK")
        self.btnCnsl = QtWidgets.QPushButton(self)
        self.btnCnsl.setGeometry(QtCore.QRect(236, 77, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCnsl.setFont(font)
        self.btnCnsl.setStyleSheet("QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                   "color: rgb(0,0,0);\n"
                                   "border-radius:3px;\n"
                                   "border:1px solid rgb(135,135,135);}\n"
                                   "\n"
                                   "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-radius:3px;\n"
                                   "border:1px solid rgb(63,63,63);}\n"
                                   "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-radius:3px;\n"
                                   "border:1px solid rgb(63,63,63);};")
        self.btnCnsl.setObjectName("btnCnsl")
        self.labeltxt = QtWidgets.QLabel(self)
        self.labeltxt.setGeometry(QtCore.QRect(40, 30, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labeltxt.setFont(font)
        self.labeltxt.setStyleSheet("background-color: rgb(242,242,242);\n"
                                    "color: rgb(0,0,0);")
        self.labeltxt.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltxt.setObjectName("labeltxt")
        self.label_iconques = QtWidgets.QLabel(self)
        self.label_iconques.setGeometry(QtCore.QRect(10, 11, 25, 25))
        self.label_iconques.setStyleSheet("background-color: rgb(242,242,242);\n"
                                          "image: url(C:/img/iconqstn.png);")
        self.label_iconques.setText("")
        self.label_iconques.setObjectName("label_iconques")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 347, 117))
        self.lblBack.setStyleSheet("background-color: rgb(242,242,242);")
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.lblBack.raise_()
        self.btnOK.raise_()
        self.btnCnsl.raise_()
        self.labeltxt.raise_()
        self.label_iconques.raise_()
        self.labeltxt.setText(GlobalValues.MesText)
        self.btnOK.clicked.connect(self.ClickOk)
        self.btnCnsl.clicked.connect(self.ClickCancel)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "!!!"))
        self.btnOK.setText(_translate("Dialog", "Принять"))
        self.btnCnsl.setText(_translate("Dialog", "Отменить"))
        self.labeltxt.setText(_translate("Dialog", str(GlobalValues.MesText)))


    def ClickOk(self):
        GlobalValues.MesResult = True
        self.close()

    def ClickCancel(self):
        GlobalValues.MesResult = False
        self.close()




if __name__ == "__main__":
    uiMesBox = Ui_MesBox()
    uiMesBox.show()
    sys.exit(app.exec_())
