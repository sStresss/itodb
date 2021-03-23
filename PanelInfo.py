# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PanelJournal_v15.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import pymysql
import threading
import time
import sys
import GlobalValues

app = QtWidgets.QApplication(sys.argv)

class Ui_Info(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(640, 449)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 651, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(5, 4, 631, 441))
        self.textEdit.setObjectName("textEdit")


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.firstSets()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))

    def firstSets(self):
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                                  port=GlobalValues.SqlPort,
                                  user=GlobalValues.SqlUserName,
                                  passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            print('tree parname by r click:', str(GlobalValues.treeParentNameByRightClick))
            cur.execute("SELECT Info FROM treeobjtbl WHERE ParentObjName Like '" + str(GlobalValues.treeParentNameByRightClick) + "'")
            rows = cur.fetchall()

            for row in rows:
                self.textEdit.setPlainText(str(row[0]))

    def closeEvent(self, event):
        self.saveDataToBD()
        time.sleep(0.05)
        event.accept()

    def saveDataToBD(self):
        newInfo = self.textEdit.toPlainText()
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            query = ("UPDATE treeobjtbl SET Info = (%s) WHERE ParentObjName = (%s)")
            cur.execute(query, (newInfo, GlobalValues.treeParentNameByRightClick))








if __name__ == "__main__":
    uiInfo = Ui_Info()
    uiInfo.show()
    sys.exit(app.exec_())
