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
from PanelMesBox import Ui_MesBox

app = QtWidgets.QApplication(sys.argv)

class Ui_AddNewKStuff(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(371, 471)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 371, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cb_MakerKStuff = QtWidgets.QComboBox(self.frame)
        self.cb_MakerKStuff.setGeometry(QtCore.QRect(150, 170, 201, 22))
        self.cb_MakerKStuff.setObjectName("cb_MakerKStuff")
        self.cb_MakerKStuff.addItem("")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 170, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 293, 111, 16))
        self.label_7.setObjectName("label_7")
        self.cb_DistribKStuff = QtWidgets.QComboBox(self.frame)
        self.cb_DistribKStuff.setGeometry(QtCore.QRect(150, 200, 201, 22))
        self.cb_DistribKStuff.setObjectName("cb_DistribKStuff")
        self.cb_DistribKStuff.addItem("")
        self.cb_DistribKStuff.addItem("")
        self.cb_DistribKStuff.addItem("")
        self.cb_DistribKStuff.addItem("")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 263, 111, 16))
        self.label_12.setObjectName("label_12")
        self.cb_TypeKStuff = QtWidgets.QComboBox(self.frame)
        self.cb_TypeKStuff.setGeometry(QtCore.QRect(150, 80, 201, 22))
        self.cb_TypeKStuff.setObjectName("cb_TypeKStuff")
        self.cb_TypeKStuff.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 55, 16))
        self.label_4.setObjectName("label_4")
        self.cb_ModelKStuff = QtWidgets.QComboBox(self.frame)
        self.cb_ModelKStuff.setGeometry(QtCore.QRect(150, 110, 201, 22))
        self.cb_ModelKStuff.setObjectName("cb_ModelKStuff")
        self.cb_ModelKStuff.addItem("")
        self.cb_ModelKStuff.addItem("")
        self.cb_ModelKStuff.addItem("")
        self.de_ComeTimeKStuff = QtWidgets.QDateEdit(self.frame)
        self.de_ComeTimeKStuff.setGeometry(QtCore.QRect(150, 260, 201, 22))
        self.de_ComeTimeKStuff.setObjectName("de_ComeTimeKStuff")
        self.btn_AddKStuff = QtWidgets.QPushButton(self.frame)
        self.btn_AddKStuff.setGeometry(QtCore.QRect(280, 430, 75, 23))
        self.btn_AddKStuff.setObjectName("btn_AddKStuff")
        self.cb_TargetKbjStuff = QtWidgets.QComboBox(self.frame)
        self.cb_TargetKbjStuff.setGeometry(QtCore.QRect(150, 230, 201, 22))
        self.cb_TargetKbjStuff.setObjectName("cb_TargetKbjStuff")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 234, 101, 16))
        self.label_10.setObjectName("label_10")
        self.cb_SavePlaceKstuff = QtWidgets.QComboBox(self.frame)
        self.cb_SavePlaceKstuff.setGeometry(QtCore.QRect(150, 290, 201, 22))
        self.cb_SavePlaceKstuff.setObjectName("cb_SavePlaceKstuff")
        self.cb_SavePlaceKstuff.addItem("")
        self.cb_SavePlaceKstuff.addItem("")
        self.le_SNKStuff = QtWidgets.QLineEdit(self.frame)
        self.le_SNKStuff.setGeometry(QtCore.QRect(150, 140, 201, 22))
        self.le_SNKStuff.setObjectName("le_SNKStuff")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 203, 91, 16))
        self.label_8.setObjectName("label_8")
        self.tE_KComment = QtWidgets.QTextEdit(self.frame)
        self.tE_KComment.setGeometry(QtCore.QRect(150, 320, 201, 91))
        self.tE_KComment.setObjectName("tE_KComment")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 101, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.FirstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cb_MakerKStuff.setItemText(0, _translate("Dialog", "Cisco"))
        self.label_9.setText(_translate("Dialog", "Производитель"))
        self.label_3.setText(_translate("Dialog", "Модель"))
        self.label_7.setText(_translate("Dialog", "Поступил на:"))
        self.cb_DistribKStuff.setItemText(0, _translate("Dialog", "Неизвестно"))
        self.cb_DistribKStuff.setItemText(1, _translate("Dialog", "Войслинк"))
        self.cb_DistribKStuff.setItemText(2, _translate("Dialog", "СИП"))
        self.cb_DistribKStuff.setItemText(3, _translate("Dialog", "Серфконсалтинг"))
        self.label_12.setText(_translate("Dialog", "Дата поступления"))
        self.cb_TypeKStuff.setItemText(0, _translate("Dialog", "Трансивер"))
        self.label_2.setText(_translate("Dialog", "Тип"))
        self.label.setText(_translate("Dialog", "Комплектующие"))
        self.label_4.setText(_translate("Dialog", "S/n"))
        self.cb_ModelKStuff.setItemText(0, _translate("Dialog", "GLC-LH-SMD"))
        self.cb_ModelKStuff.setItemText(1, _translate("Dialog", "GLC-FE-100LX-RGD"))
        self.cb_ModelKStuff.setItemText(2, _translate("Dialog", "GLC-ZX-SM-RGD"))
        self.btn_AddKStuff.setText(_translate("Dialog", "Добавить"))
        self.label_10.setText(_translate("Dialog", "Целевой объект"))
        self.cb_SavePlaceKstuff.setItemText(0, _translate("Dialog", "Склад Офис"))
        self.cb_SavePlaceKstuff.setItemText(1, _translate("Dialog", "Склад СБВ"))
        self.label_8.setText(_translate("Dialog", "Поставщик"))
        self.label_6.setText(_translate("Dialog", "Комментарий:"))

    def FirstSets(self):
        self.MakeTargetObjList()
        self.MakeKTypeList()
        self.MakeKModelList()
        self.MakeKMakerList()
        self.MakeKDistributorList()
        self.MakeInputPlaceList()

        self.btn_AddKStuff.clicked.connect(self.AddNewRcord)

    def AddNewRcord(self):
        GlobalValues.MesText = "Вы уверены?"
        self.openMesBox()
        if (GlobalValues.MesResult != False) and (str(self.cb_TargetKbjStuff.currentText()) != ""):

            if (self.le_SNKStuff.text() != ""):
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
                    "SELECT KSerialNum FROM kstuff WHERE KSerialNum Like '%" + self.le_SNKStuff.text() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    GlobalValues.MesText = "Ошибка! Серийный номер уже сущесвует!"
                    self.openMesBox()
                else:

                    KType = self.cb_TypeKStuff.currentText()
                    KModel = self.cb_ModelKStuff.currentText()
                    KSerialNum = self.le_SNKStuff.text()
                    KMaker = self.cb_MakerKStuff.currentText()
                    KDistributor = self.cb_DistribKStuff.currentText()
                    KComeTime = self.de_ComeTimeKStuff.text()
                    KTargetObj = self.cb_TargetKbjStuff.currentText()
                    KFactObj = self.cb_SavePlaceKstuff.currentText()
                    KInputObj = self.cb_SavePlaceKstuff.currentText()
                    KComment = self.tE_KComment.toPlainText()
                    # print(str(OType))

                    cur.execute("SELECT ID FROM kstuff")
                    rows = cur.fetchall()
                    #
                    KID = 1
                    print(len(rows))
                    if (len(rows) != 0):
                        for row in reversed(rows):
                            try:
                                KID = str(int(row[0]) + 1)
                            except:
                                print("OID Error!!!")
                            break

                    query = ("INSERT INTO kstuff (ID, KType, KModel, KSerialNum, KMaker, KDistributor, KComeTime, KTargetObj, KFactObj, KInputObj, KComment) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    cur.execute(query, (KID, KType, KModel, KSerialNum, KMaker, KDistributor, KComeTime, KTargetObj, KFactObj, KInputObj, KComment))
                    con.commit()


                    cur.close()
                    # con.close()
                    GlobalValues.Hystory(GlobalValues.UserName, KType, KSerialNum, "Добавление в базу")
                    GlobalValues.MesResult = False

                    if GlobalValues.checkTreeFocusInTransfer == True:
                        GlobalValues.checkTreeUpdateEvent = True
                        GlobalValues.checkTreeFocusInTransfer = False
                    else:
                        GlobalValues.checkKTblUpdateEvent = True
                    GlobalValues.checkTreeStatesUpdate = True


            else:
                GlobalValues.MesResult = False
                GlobalValues.MesText = "Введены не все данные!!!"
                self.uiMesBox.btnOK.hide()
                self.uiMesBox.btnCnsl.hide()
                self.openMesBox()

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
        with con:

            cur = con.cursor()
            cur.execute("SELECT ObjID, PArentObjName FROM treeobjtbl")
            curr_TObj_list_rows = cur.fetchall()
            indexlist = 0
            for row in curr_TObj_list_rows:
                if indexlist > 0:
                    self.cb_TargetKbjStuff.addItem(str(row[1]))
                indexlist += 1
        # con.close()

    def openMesBox(self):
        self.uiMesBox = Ui_MesBox()
        self.uiMesBox.exec_()

    def MakeKTypeList(self):
        self.cb_TypeKStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))
        with con:
            cur = con.cursor()
            cur.execute("SELECT ID, KTypeName FROM ktypetbl")
            KType_rows = cur.fetchall()
            for row in KType_rows:
                self.cb_TypeKStuff.addItem(str(row[1]))

    def MakeKModelList(self):
        self.cb_ModelKStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))
        with con:
            cur = con.cursor()
            cur.execute("SELECT ID, KModelName FROM kmodeltbl")
            KModel_rows = cur.fetchall()
            for row in KModel_rows:
                self.cb_ModelKStuff.addItem(str(row[1]))

    def MakeKMakerList(self):
        self.cb_MakerKStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))
        with con:
            cur = con.cursor()
            cur.execute("SELECT ID, KMakerName FROM kmakertbl")
            KMaker_rows = cur.fetchall()
            for row in KMaker_rows:
                self.cb_MakerKStuff.addItem(str(row[1]))

    def MakeKDistributorList(self):
        self.cb_DistribKStuff.clear()
        con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                              port=int(GlobalValues.SqlPort),
                              user=str(GlobalValues.SqlUserName),
                              passwd=str(GlobalValues.SqlPwd),
                              db=str(GlobalValues.SqlDBName))
        with con:
            cur = con.cursor()
            cur.execute("SELECT ID, KDistributorName FROM kdistributortbl")
            KDistributor_rows = cur.fetchall()
            for row in KDistributor_rows:
                self.cb_DistribKStuff.addItem(str(row[1]))

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
        with con:
            cur = con.cursor()
            cur.execute("SELECT ObjID, ParentObjName FROM treeobjtbl")
            TreeParentNames_rows = cur.fetchall()

            for row in TreeParentNames_rows:
                self.cb_SavePlaceKstuff.addItem(str(row[1]))




if __name__ == "__main__":
    uiAddKStuff = Ui_AddNewKStuff()
    uiAddKStuff.show()
    sys.exit(app.exec_())
