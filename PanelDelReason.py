# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PanelJournal_v15.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PanelMesBox import Ui_MesBox
import GlobalValues
import time

app = QtWidgets.QApplication(sys.argv)

class Ui_DelReason(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(347, 181)
        self.setStyleSheet("")
        self.btnOK = QtWidgets.QPushButton(self)
        self.btnOK.setGeometry(QtCore.QRect(135, 140, 90, 25))
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
        self.btnCnsl.setGeometry(QtCore.QRect(236, 140, 90, 25))
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
        self.labeltxt.setGeometry(QtCore.QRect(40, 10, 261, 21))
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
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 347, 181))
        self.lblBack.setStyleSheet("background-color: rgb(242,242,242);")
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.tE_DelReason = QtWidgets.QTextEdit(self)
        self.tE_DelReason.setGeometry(QtCore.QRect(10, 40, 331, 91))
        self.tE_DelReason.setObjectName("tE_DelReason")
        self.lblBack.raise_()
        self.btnOK.raise_()
        self.btnCnsl.raise_()
        self.labeltxt.raise_()
        self.label_iconques.raise_()
        self.tE_DelReason.raise_()

        self.btnOK.clicked.connect(self.ClickOk)
        self.btnCnsl.clicked.connect(self.ClickCancel)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.FirstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Удаление"))
        self.btnOK.setText(_translate("Dialog", "Принять"))
        self.btnCnsl.setText(_translate("Dialog", "Отменить"))
        self.labeltxt.setText(_translate("Dialog", "Укажите причину удаления!"))

    # def FirstSets(self):
    #     self.btnOK.clicked.connect(self.ClickOk)
    #     self.btnCnsl.clicked.connect(self.ClickCancel)

    def ClickOk(self):
        checkdata = False
        if str(self.tE_DelReason.toPlainText()) == "":
            checkdata = False
            GlobalValues.MesText = "Комментарий пуст!"
            self.openMesBox()
        else:
            checkdata = True


        if checkdata == True:
            GlobalValues.checkDelComment = True
            GlobalValues.DelReasonComment = self.tE_DelReason.toPlainText()
            GlobalValues.MesText = 'Вы уверены?'
            self.openMesBox()
            if GlobalValues.MesResult == True:
                self.ClickCancel()

    def ClickCancel(self):
        self.close()
        time.sleep(0.2)



    def openMesBox(self):
        uiMesBox = Ui_MesBox()
        uiMesBox.exec_()

if __name__ == "__main__":
    uiDelReason = Ui_DelReason()
    uiDelReason.show()
    sys.exit(app.exec_())
