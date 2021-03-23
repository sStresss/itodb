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
import pymysql
from PanelMesBox import Ui_MesBox

app = QtWidgets.QApplication(sys.argv)

class Ui_KGroupEdit(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(372, 189)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 371, 189))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_Save = QtWidgets.QPushButton(self.frame)
        self.btn_Save.setGeometry(QtCore.QRect(270, 150, 91, 23))
        self.btn_Save.setObjectName("btn_Save")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tE_Comm = QtWidgets.QTextEdit(self.frame)
        self.tE_Comm.setGeometry(QtCore.QRect(10, 40, 381, 101))
        self.tE_Comm.setObjectName("tE_Comm")


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.firstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_Save.setText(_translate("Dialog", "Сохранить"))
        self.label.setText(_translate("Dialog", "Редактор группы | комментарий"))

    def firstSets(self):
        self.tE_Comm.setFocus()
        self.btn_Save.clicked.connect(self.PushGroupComment)


    def PushGroupComment(self):
        GlobalValues.MesText = 'Сохранить комментарий группы устройств?'
        self.openMexBox()
        comm = self.tE_Comm.toPlainText()
        if GlobalValues.MesResult == True:
            sql_con = pymysql.connect(host=GlobalValues.SqlHostname,
                                      port=GlobalValues.SqlPort,
                                      user=GlobalValues.SqlUserName,
                                      passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)
            with sql_con:
                cur = sql_con.cursor()
                for elem in GlobalValues.ktbl_selected_lst:
                    query = ("UPDATE kstuff SET KComment = (%s) WHERE ID = (%s)")
                    cur.execute(query, (comm, elem[0]))
                    time.sleep(0.05)
                    GlobalValues.Hystory(GlobalValues.UserName, elem[1],
                                         elem[2],
                                         "Редактор группы | комментарий | БЫЛ: " + str(elem[3]) + " || СТАЛ: " + str(comm))
                sql_con.commit()
                time.sleep(0.05)

            if GlobalValues.checkGlobalviewMode == False:
                GlobalValues.checkTreeUpdateEvent = True
            else:
                GlobalValues.checkKTblUpdateEvent = True
            self.close()
            time.sleep(0.2)

    def openMexBox(self):
        self.uiMexBox = Ui_MesBox()
        self.uiMexBox.exec_()


if __name__ == "__main__":
    uiKGroupEdit = Ui_KGroupEdit()
    uiKGroupEdit.show()
    sys.exit(app.exec_())
