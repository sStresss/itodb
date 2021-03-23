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

app = QtWidgets.QApplication(sys.argv)

class Ui_GlobStatEdit(QDialog):


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
        self.cb_TypeStuff.setObjectName("cb_TypeStuff")
        self.cb_ModelStuff = QtWidgets.QComboBox(self.frame)
        self.cb_ModelStuff.setGeometry(QtCore.QRect(150, 90, 201, 22))
        self.cb_ModelStuff.setObjectName("cb_ModelStuff")
        self.btn_EditStuff = QtWidgets.QPushButton(self.frame)
        self.btn_EditStuff.setGeometry(QtCore.QRect(280, 180, 75, 23))
        self.btn_EditStuff.setObjectName("btn_AddStuff")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.label_4.setObjectName("label_4")
        self.cb_Num = QtWidgets.QComboBox(self.frame)
        self.cb_Num.setGeometry(QtCore.QRect(150, 120, 61, 22))
        self.cb_Num.setObjectName("cb_Num")


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.firstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_EditStuff.setText(_translate("Dialog", "Сохранить"))
        self.label_3.setText(_translate("Dialog", "Модель"))
        self.label_2.setText(_translate("Dialog", "Тип"))
        self.label.setText(_translate("Dialog", "Оборудование | Редактирование"))
        self.label_4.setText(_translate("Dialog", "Количество"))

    def firstSets(self):
        self.makeCurrTypeList()
        self.makeCurrNum()
        self.makeCurrModelList()

        self.btn_EditStuff.clicked.connect(self.editRecord)


    def makeCurrNum(self):
        i = 0
        for i in range(120):
            i+=1
            self.cb_Num.addItem(str(i))

        self.cb_Num.setCurrentIndex(int(GlobalValues.STblCurrNumBySpec) - 1)
        self.oldNum = self.cb_Num.currentText()

    def makeCurrTypeList(self):
        self.cb_TypeStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))

        cur = con.cursor()
        cur.execute("SELECT ID, OTypeName FROM otypetbl")
        OType_rows = cur.fetchall()
        count = 0
        for row in OType_rows:
            self.cb_TypeStuff.addItem(str(row[1]))
            count+=1

        cur.execute("SELECT ID, KTypeName FROM ktypetbl")
        KType_rows = cur.fetchall()
        for row in KType_rows:
            self.cb_TypeStuff.addItem(str(row[1]))
            count+=1

        i = 0
        currInd = 0
        for i in range(count):
            if self.cb_TypeStuff.itemText(i) == GlobalValues.STblCurrTypeObj:
                currInd = i
        self.cb_TypeStuff.setCurrentIndex(currInd)
        # self.oldType = self.cb_TypeStuff.currentText()

    def makeCurrModelList(self):
        self.cb_ModelStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))

        cur = con.cursor()
        cur.execute("SELECT ID, OModelName FROM omodeltbl")
        OModel_rows = cur.fetchall()
        count = 0
        for row in OModel_rows:
            self.cb_ModelStuff.addItem(str(row[1]))
            count+=1

        cur.execute("SELECT ID, KModelName FROM kmodeltbl")
        KModel_rows = cur.fetchall()
        for row in KModel_rows:
            self.cb_ModelStuff.addItem(str(row[1]))
            count+=1

        i = 0
        currInd = 0
        for i in range(count):
            if self.cb_ModelStuff.itemText(i) == GlobalValues.STblCurrModelObj:
                currInd = i
        self.cb_ModelStuff.setCurrentIndex(currInd)
        # self.oldModel = self.cb_ModelStuff.currentText()

    def editRecord(self):
        newType = self.cb_TypeStuff.currentText()
        newModel = self.cb_ModelStuff.currentText()
        newNum = self.cb_Num.currentText()

        oldType = GlobalValues.STblCurrTypeObj
        oldModel = GlobalValues.STblCurrModelObj
        oldNum = GlobalValues.STblCurrNumBySpec

        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))

        cur = con.cursor()
        cur.execute(
        "SELECT ParentObjName, ConnectionID FROM treeobjtbl WHERE ParentObjName Like '%" + GlobalValues.pTreeParentName + "%'")
        objNamesRows = cur.fetchall()

        for row in objNamesRows:
            curConID = row[1]

        cur.execute(
        "SELECT ID, ModelObj, TypeObj, Num, ConID FROM globstattbl WHERE ConID Like '%" + str(curConID) + "%'")
        rows = cur.fetchall()
        time.sleep(0.2)

        for row in rows:
            if row[1] == oldModel:
                if row[2] == oldType:
                    if row[3] == oldNum:
                        pID = row[0]

        # pID = int(pID)
        cur = con.cursor()
        query = ("UPDATE globstattbl SET ModelObj = (%s) WHERE ID = (%s)")
        cur.execute(query, (newModel, pID))

        query = ("UPDATE globstattbl SET TypeObj = (%s) WHERE ID = (%s)")
        cur.execute(query, (newType, pID))

        query = ("UPDATE globstattbl SET Num = (%s) WHERE ID = (%s)")
        cur.execute(query, (newNum, pID))

        con.commit()
        GlobalValues.checkGlobStatTblUpdateEvent = True
        GlobalValues.checkTreeStatesUpdate = True
        self.close()



if __name__ == "__main__":
    uiGlobStatEdit = Ui_GlobStatEdit()
    uiGlobStatEdit.show()
    sys.exit(app.exec_())
