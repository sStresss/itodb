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
from datetime import datetime
import GlobalValues
from PanelMesBox import Ui_MesBox

app = QtWidgets.QApplication(sys.argv)

class Ui_AddNewOStuff(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(372, 469)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 371, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.de_ComeTimeOStuff = QtWidgets.QDateEdit(self.frame)
        self.de_ComeTimeOStuff.setGeometry(QtCore.QRect(150, 260, 201, 22))
        self.de_ComeTimeOStuff.setObjectName("de_ComeTimeOStuff")
        self.cb_MakerOStuff = QtWidgets.QComboBox(self.frame)
        self.cb_MakerOStuff.setGeometry(QtCore.QRect(150, 170, 201, 22))
        self.cb_MakerOStuff.setObjectName("cb_MakerOStuff")
        self.cb_SavePlaceOstuff = QtWidgets.QComboBox(self.frame)
        self.cb_SavePlaceOstuff.setGeometry(QtCore.QRect(150, 290, 201, 22))
        self.cb_SavePlaceOstuff.setObjectName("cb_SavePlaceOstuff")
        self.cb_TypeOStuff = QtWidgets.QComboBox(self.frame)
        self.cb_TypeOStuff.setGeometry(QtCore.QRect(150, 80, 201, 22))
        self.cb_TypeOStuff.setObjectName("cb_TypeOStuff")
        self.cb_ModelOStuff = QtWidgets.QComboBox(self.frame)
        self.cb_ModelOStuff.setGeometry(QtCore.QRect(150, 110, 201, 22))
        self.cb_ModelOStuff.setObjectName("cb_ModelOStuff")
        self.btn_AddOStuff = QtWidgets.QPushButton(self.frame)
        self.btn_AddOStuff.setGeometry(QtCore.QRect(280, 430, 75, 23))
        self.btn_AddOStuff.setObjectName("btn_AddOStuff")
        self.cb_DistribOStuff = QtWidgets.QComboBox(self.frame)
        self.cb_DistribOStuff.setGeometry(QtCore.QRect(150, 200, 201, 22))
        self.cb_DistribOStuff.setObjectName("cb_DistribOStuff")
        self.cb_TargetObjStuff = QtWidgets.QComboBox(self.frame)
        self.cb_TargetObjStuff.setGeometry(QtCore.QRect(150, 230, 201, 22))
        self.cb_TargetObjStuff.setObjectName("cb_TargetObjStuff")
        self.le_SNOStuff = QtWidgets.QLineEdit(self.frame)
        self.le_SNOStuff.setGeometry(QtCore.QRect(150, 140, 201, 22))
        self.le_SNOStuff.setObjectName("le_SNOStuff")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 200, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 290, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 260, 111, 16))
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 170, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 230, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 101, 16))
        self.label_6.setObjectName("label_6")
        self.tE_OComment = QtWidgets.QTextEdit(self.frame)
        self.tE_OComment.setGeometry(QtCore.QRect(150, 320, 201, 91))
        self.tE_OComment.setObjectName("tE_OComment")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.FirstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_AddOStuff.setText(_translate("Dialog", "Добавить"))
        self.label_3.setText(_translate("Dialog", "Модель"))
        self.label_8.setText(_translate("Dialog", "Поставщик"))
        self.label_4.setText(_translate("Dialog", "S/n"))
        self.label_5.setText(_translate("Dialog", "Поступил на:"))
        self.label_2.setText(_translate("Dialog", "Тип"))
        self.label_12.setText(_translate("Dialog", "Дата поступления"))
        self.label.setText(_translate("Dialog", "Оборудование"))
        self.label_7.setText(_translate("Dialog", "Производитель"))
        self.label_10.setText(_translate("Dialog", "Целевой объект"))
        self.label_6.setText(_translate("Dialog", "Комментарий:"))

    def FirstSets(self):
        self.MakeTargetObjList()
        self.MakeOTypeList()
        self.MakeOModelList()
        self.MakeOMakerList()
        self.MakeODistributorList()
        self.MakeInputPlaceList()
        self.btn_AddOStuff.clicked.connect(self.AddNewRcord)

    def AddNewRcord(self):
        GlobalValues.MesText = "Вы уверены?"
        self.openMesBox()
        if (GlobalValues.MesResult != False) and (str(self.cb_TargetObjStuff.currentText()) != ""):
            GlobalValues.MesResult = False
            if str(self.le_SNOStuff.text()) == "":
                GlobalValues.MesText = "Ошибка! Введите серийный номер!"
                self.openMesBox()
            else:

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
                    "SELECT OSerialNum FROM ostuff WHERE OSerialNum Like '%" + self.le_SNOStuff.text() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    GlobalValues.MesText = "Ошибка! Серийный номер уже сущесвует!"
                    self.openMesBox()
                else:
                    OType = self.cb_TypeOStuff.currentText()
                    OModel = self.cb_ModelOStuff.currentText()
                    OSerialNum = self.le_SNOStuff.text()
                    OMaker = self.cb_MakerOStuff.currentText()
                    ODistributor = self.cb_DistribOStuff.currentText()
                    OComeTime = self.de_ComeTimeOStuff.text()
                    OTargetObj = self.cb_TargetObjStuff.currentText()
                    OFactObj = self.cb_SavePlaceOstuff.currentText()
                    OInputObj = self.cb_SavePlaceOstuff.currentText()
                    OComment = self.tE_OComment.toPlainText()
                    # print(str(OType))


                    cur.execute("SELECT ID FROM ostuff")
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


                    query = ("INSERT INTO ostuff (ID, OType, OModel, OSerialNum, OMaker, ODistributor, OComeTime, OTargetObj, OFactObj, OInputObj, OComment) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    cur.execute(query, (OID, OType, OModel, OSerialNum, OMaker, ODistributor, OComeTime, OTargetObj, OFactObj, OInputObj, OComment))
                    con.commit()
                    cur.close()
                    # con.close()

                    GlobalValues.Hystory(GlobalValues.UserName, OType, OSerialNum, "Добавление в базу")
                    GlobalValues.MesResult = False

                    if GlobalValues.checkTreeFocusInTransfer == True:
                        GlobalValues.checkTreeUpdateEvent = True
                        GlobalValues.checkTreeFocusInTransfer = False
                    else:
                        GlobalValues.checkOTblUpdateEvent = True
                    GlobalValues.checkTreeStatesUpdate = True

    def MakeTargetObjList(self):
        _translate = QtCore.QCoreApplication.translate
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
        cur.execute("SELECT ObjID, ParentObjName FROM treeobjtbl")
        curr_TObj_list_rows = cur.fetchall()
        indexlist = 0
        for row in curr_TObj_list_rows:
            if indexlist > 0:
                self.cb_TargetObjStuff.addItem(str(row[1]))
            indexlist += 1
        # con.close()

    def openMesBox(self):
        self.uiMesBox = Ui_MesBox()
        self.uiMesBox.exec_()

    def MakeOTypeList(self):
        self.cb_TypeOStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))

        cur = con.cursor()
        cur.execute("SELECT ID, OTypeName FROM otypetbl")
        OType_rows = cur.fetchall()
        for row in OType_rows:
            self.cb_TypeOStuff.addItem(str(row[1]))

    def MakeOModelList(self):
        self.cb_ModelOStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))
        cur = con.cursor()
        cur.execute("SELECT ID, OModelName FROM omodeltbl")
        OModel_rows = cur.fetchall()
        for row in OModel_rows:
            self.cb_ModelOStuff.addItem(str(row[1]))

    def MakeOMakerList(self):
        self.cb_MakerOStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))
        cur = con.cursor()
        cur.execute("SELECT ID, OMakerName FROM omakertbl")
        OMaker_rows = cur.fetchall()
        for row in OMaker_rows:
            self.cb_MakerOStuff.addItem(str(row[1]))

    def MakeODistributorList(self):
        self.cb_DistribOStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))
        cur = con.cursor()
        cur.execute("SELECT ID, ODistributorName FROM odistributortbl")
        ODistributor_rows = cur.fetchall()
        for row in ODistributor_rows:
            self.cb_DistribOStuff.addItem(str(row[1]))

    def MakeInputPlaceList(self):

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
        cur.execute("SELECT ObjID, ParentObjName FROM treeobjtbl")
        TreeParentNames_rows = cur.fetchall()

        for row in TreeParentNames_rows:
            self.cb_SavePlaceOstuff.addItem(str(row[1]))



if __name__ == "__main__":
    uiAddOStuff = Ui_AddNewOStuff()
    uiAddOStuff.show()
    sys.exit(app.exec_())
