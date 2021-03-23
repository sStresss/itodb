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
import pymysql
import GlobalValues

app = QtWidgets.QApplication(sys.argv)

class Ui_GlobStatSett(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(372, 214)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 371, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cb_TypeStuff = QtWidgets.QComboBox(self.frame)
        self.cb_TypeStuff.setGeometry(QtCore.QRect(150, 60, 201, 22))
        self.cb_TypeStuff.setObjectName("cb_TypeOStuff")
        self.cb_ModelStuff = QtWidgets.QComboBox(self.frame)
        self.cb_ModelStuff.setGeometry(QtCore.QRect(150, 90, 201, 22))
        self.cb_ModelStuff.setObjectName("cb_ModelOStuff")
        self.btn_AddStuff = QtWidgets.QPushButton(self.frame)
        self.btn_AddStuff.setGeometry(QtCore.QRect(280, 180, 75, 23))
        self.btn_AddStuff.setObjectName("btn_AddOStuff")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.label_4.setObjectName("label_4")
        self.cb_Num = QtWidgets.QComboBox(self.frame)
        self.cb_Num.setGeometry(QtCore.QRect(150, 120, 61, 22))
        self.cb_Num.setObjectName("cb_ModelOStuff_2")


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.firstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_AddStuff.setText(_translate("Dialog", "Добавить"))
        self.label_3.setText(_translate("Dialog", "Модель"))
        self.label_2.setText(_translate("Dialog", "Тип"))
        self.label.setText(_translate("Dialog", "Оборудование"))
        self.label_4.setText(_translate("Dialog", "Количество"))

    def firstSets(self):
        self.makeTypeList()
        self.makeModelList()
        self.makeNumList()

        self.btn_AddStuff.clicked.connect(self.addRecord)

    def makeTypeList(self):

        self.cb_TypeStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))

        cur = con.cursor()
        cur.execute("SELECT ID, OTypeName FROM otypetbl")
        OType_rows = cur.fetchall()
        for row in OType_rows:
            self.cb_TypeStuff.addItem(str(row[1]))

        cur.execute("SELECT ID, KTypeName FROM ktypetbl")
        KType_rows = cur.fetchall()
        for row in KType_rows:
            self.cb_TypeStuff.addItem(str(row[1]))

    def makeModelList(self):
        self.cb_ModelStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))

        cur = con.cursor()
        cur.execute("SELECT ID, OModelName FROM omodeltbl")
        OModel_rows = cur.fetchall()
        for row in OModel_rows:
            self.cb_ModelStuff.addItem(str(row[1]))

        cur.execute("SELECT ID, KModelName FROM kmodeltbl")
        KModel_rows = cur.fetchall()
        for row in KModel_rows:
            self.cb_ModelStuff.addItem(str(row[1]))

    def makeNumList(self):
        i = 0
        for i in range(120):
            i+=1
            self.cb_Num.addItem(str(i))

    def addRecord(self):
        model = self.cb_ModelStuff.currentText()
        type = self.cb_TypeStuff.currentText()
        num = self.cb_Num.currentText()
        objName = GlobalValues.pTreeParentName
        print(GlobalValues.TreeParentName)

        locHostName = str(GlobalValues.SqlHostname)
        locPort = int(GlobalValues.SqlPort)
        locUserName = str(GlobalValues.SqlUserName)
        locPwd = str(GlobalValues.SqlPwd)
        locDBName = str(GlobalValues.SqlDBName)
        con = pymysql.connect(host=locHostName,
                              port=locPort,
                              user=locUserName,
                              passwd=locPwd,
                              db=locDBName)

        cur = con.cursor()
        cur.execute(
            "SELECT ParentObjName, ConnectionID FROM treeobjtbl WHERE ParentObjName Like '" + str(objName) + "'")
        rows = cur.fetchall()
        for row in rows:
            conID = row[1]

        cur.execute("SELECT ID FROM globstattbl")
        rows = cur.fetchall()
        #
        OID = 1
        print(len(rows))
        if (len(rows) != 0):
            for row in reversed(rows):
                try:
                    OID = str(int(row[0]) + 1)
                except:
                    print("OID Error!!!")
                break

        query = (
            "INSERT INTO globstattbl (ID, ModelObj, TypeObj, Num, ConID) VALUES ( %s, %s, %s, %s, %s )")
        cur.execute(query, (
        OID, model, type, num, conID ))
        con.commit()
        GlobalValues.checkGlobStatTblUpdateEvent = True
        GlobalValues.checkTreeStatesUpdate = True





if __name__ == "__main__":
    uiGlobStatSett = Ui_GlobStatSett()
    uiGlobStatSett.show()
    sys.exit(app.exec_())
