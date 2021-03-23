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
from PanelMesBox import Ui_MesBox

app = QtWidgets.QApplication(sys.argv)

class Ui_DialogBox(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(347, 126)
        self.setStyleSheet("")
        self.btnOK = QtWidgets.QPushButton(self)
        self.btnOK.setGeometry(QtCore.QRect(135, 80, 90, 25))
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
        self.btnCnsl.setGeometry(QtCore.QRect(236, 80, 90, 25))
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
        self.lbl_Text = QtWidgets.QLabel(self)
        self.lbl_Text.setGeometry(QtCore.QRect(10, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_Text.setFont(font)
        self.lbl_Text.setStyleSheet("background-color: rgb(242,242,242);\n"
                                    "color: rgb(0,0,0);")
        self.lbl_Text.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Text.setObjectName("lbl_Text")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 347, 121))
        self.lblBack.setStyleSheet("background-color: rgb(242,242,242);")
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.tE_Text = QtWidgets.QTextEdit(self)
        self.tE_Text.setGeometry(QtCore.QRect(140, 30, 191, 21))
        self.tE_Text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tE_Text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tE_Text.setObjectName("tE_Text")
        self.lblBack.raise_()
        self.btnOK.raise_()
        self.btnCnsl.raise_()
        self.lbl_Text.raise_()
        self.tE_Text.raise_()


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.firstSets()



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnOK.setText(_translate("Dialog", "Принять"))
        self.btnCnsl.setText(_translate("Dialog", "Отменить"))
        self.lbl_Text.setText(_translate("Dialog", "Имя нового объекта"))

    def firstSets(self):
        self.tE_Text.setPlainText(str(GlobalValues.DialogText))
        self.lbl_Text.setText(str(GlobalValues.DialogHeadText))
        self.btnOK.clicked.connect(self.ClickOk)
        self.btnCnsl.clicked.connect(self.ClickCancel)

    def openMexBox(self):
        self.uiMesBox = Ui_MesBox()
        self.uiMesBox.exec_()


    def ClickOk(self):
        if self.tE_Text.toPlainText() == "":
            GlobalValues.MesText = "Введите имя!"
            self.openMexBox()
        else:
            GlobalValues.DialogText = self.tE_Text.toPlainText()
            GlobalValues.DialogRes = True
            self.close()

    def ClickCancel(self):
        GlobalValues.DialogRes = False
        self.close()




if __name__ == "__main__":
    uiDialogBox = Ui_DialogBox()
    uiDialogBox.show()
    sys.exit(app.exec_())
