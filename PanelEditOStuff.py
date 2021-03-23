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

class Ui_EditOStuff(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(372, 471)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 371, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.de_ComeTimeOStuff = QtWidgets.QDateEdit(self.frame)
        self.de_ComeTimeOStuff.setGeometry(QtCore.QRect(150, 230, 201, 22))
        self.de_ComeTimeOStuff.setObjectName("de_ComeTimeOStuff")
        self.cb_MakerOStuff = QtWidgets.QComboBox(self.frame)
        self.cb_MakerOStuff.setGeometry(QtCore.QRect(150, 170, 201, 22))
        self.cb_MakerOStuff.setObjectName("cb_MakerOStuff")
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
        self.cb_TargetObjStuff.setGeometry(QtCore.QRect(150, 260, 201, 22))
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 230, 111, 16))
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 170, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 263, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 290, 111, 16))
        self.label_13.setObjectName("label_13")
        self.de_TransferDate = QtWidgets.QDateEdit(self.frame)
        self.de_TransferDate.setGeometry(QtCore.QRect(150, 290, 201, 22))
        self.de_TransferDate.setObjectName("de_TransferDate")
        self.tE_OComment = QtWidgets.QTextEdit(self.frame)
        self.tE_OComment.setGeometry(QtCore.QRect(150, 320, 201, 91))
        self.tE_OComment.setObjectName("tE_OComment")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 101, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.FirstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель редактирования"))
        self.btn_AddOStuff.setText(_translate("Dialog", "Сохранить"))
        self.label_3.setText(_translate("Dialog", "Модель"))
        self.label_8.setText(_translate("Dialog", "Поставщик"))
        self.label_4.setText(_translate("Dialog", "S/n"))
        self.label_2.setText(_translate("Dialog", "Тип"))
        self.label_12.setText(_translate("Dialog", "Дата поступления"))
        self.label.setText(_translate("Dialog", "Оборудование | Редактирование"))
        self.label_7.setText(_translate("Dialog", "Производитель"))
        self.label_10.setText(_translate("Dialog", "Целевой объект"))
        self.label_13.setText(_translate("Dialog", "Дата перемещения"))
        self.label_6.setText(_translate("Dialog", "Комментарий:"))

    checkTransferDateNone = False

    def FirstSets(self):
        GlobalValues.checkOTblWasClicked = False
        self.btn_AddOStuff.clicked.connect(self.MakeUpdate)
        self.MakeCurrTypeList()
        self.MakeCurrModelList()
        self.MakeCurrSerialNum()
        self.MakeCurrMakerList()
        self.MakeDistributorList()
        self.MakeInputDate()
        self.MakeTargetObjList()
        self.MakeTransferDate()
        self.MakeComment()

    def MakeCurrTypeList(self):
        self.cb_TypeOStuff.addItem(str(GlobalValues.OTblCurrTypeObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                                  port=GlobalValues.SqlPort,
                                  user=GlobalValues.SqlUserName,
                                  passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ID, OTypeName FROM otypetbl")

            rows = cur.fetchall()

            for row in rows:
                if str(row[1]) != str(GlobalValues.OTblCurrTypeObj):
                    self.cb_TypeOStuff.addItem(str(row[1]))
            cur.close()
        # con.close()

    def MakeCurrModelList(self):
        self.cb_ModelOStuff.addItem(str(GlobalValues.OTblCurrModelObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ID, OModelName FROM omodeltbl")

            rows = cur.fetchall()

            for row in rows:
                if str(row[1]) != str(GlobalValues.OTblCurrModelObj):
                    self.cb_ModelOStuff.addItem(str(row[1]))
            cur.close()
        # con.close()

    def MakeCurrSerialNum(self):
        self.le_SNOStuff.setText(str(GlobalValues.OTblCurrSerialNumObj))

    def MakeCurrMakerList(self):
        self.cb_MakerOStuff.addItem(str(GlobalValues.OTblCurrMakerObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ID, OMakerName FROM omakertbl")

            rows = cur.fetchall()

            for row in rows:
                if str(row[1]) != str(GlobalValues.OTblCurrMakerObj):
                    self.cb_MakerOStuff.addItem(str(row[1]))
            cur.close()
        # con.close()

    def MakeDistributorList(self):
        self.cb_DistribOStuff.addItem(str(GlobalValues.OTblCurrDistributorObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ID, ODistributorName FROM odistributortbl")

            rows = cur.fetchall()

            for row in rows:
                if str(row[1]) != str(GlobalValues.OTblCurrDistributorObj):
                    self.cb_DistribOStuff.addItem(str(row[1]))
            cur.close()
        # con.close()

    def MakeInputDate(self):
        day = int(GlobalValues.OTblCurrInputDateObj[0] + GlobalValues.OTblCurrInputDateObj[1])
        month = int(GlobalValues.OTblCurrInputDateObj[3] + GlobalValues.OTblCurrInputDateObj[4])
        year = int(GlobalValues.OTblCurrInputDateObj[6] + GlobalValues.OTblCurrInputDateObj[7] + GlobalValues.OTblCurrInputDateObj[8] + GlobalValues.OTblCurrInputDateObj[9])
        self.de_ComeTimeOStuff.setDate(QtCore.QDate(year,month,day))

    def MakeTargetObjList(self):
        self.cb_TargetObjStuff.addItem(str(GlobalValues.OTblCurrTargetObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ObjID, ParentObjName FROM treeobjtbl")

            rows = cur.fetchall()
            count = 0
            for row in rows:
                if count > 0:
                    if str(row[1]) != str(GlobalValues.OTblCurrTargetObj):
                        self.cb_TargetObjStuff.addItem(str(row[1]))
                count+=1
            cur.close()
        # con.close()

    def MakeTransferDate(self):
        if GlobalValues.OTblCurrTransferDateObj == "None":
            self.de_TransferDate.setEnabled(False)
            self.checkTransferDateNone = True
        else:
            self.checkTransferDateNone = False
            day = int(GlobalValues.OTblCurrTransferDateObj[0] + GlobalValues.OTblCurrTransferDateObj[1])
            month = int(GlobalValues.OTblCurrTransferDateObj[3] + GlobalValues.OTblCurrTransferDateObj[4])
            year = int(GlobalValues.OTblCurrTransferDateObj[6] + GlobalValues.OTblCurrTransferDateObj[7] + GlobalValues.OTblCurrTransferDateObj[8] + GlobalValues.OTblCurrTransferDateObj[9])
            self.de_TransferDate.setDate(QtCore.QDate(year,month,day))

    def MakeComment(self):
        self.tE_OComment.setPlainText(GlobalValues.OTblCurrComment)

    def openMesBox(self):
        self.uiMesBox = Ui_MesBox()
        self.uiMesBox.exec_()

    def MakeUpdate(self):
        self.checkTypeWasChanged = False
        self.checkModelWasChanged = False
        self.checkSerialWasChanged = False
        self.checkMakerWasChanged = False
        self.checkDistributorWasChanged = False
        self.checkInputDateWasChanged = False
        self.checkTargetObjWasChanged = False
        self.checkTransferDateWasChanged = False
        self.checkCommentWasChanged = False

        checkMakeUpdate = False
        checkDataWasChanged = False
        GlobalValues.MesText = "Вы уверены?"
        self.openMesBox()
        if GlobalValues.MesResult:
            pID = str(GlobalValues.OTblCurrID)
            pType = str(self.cb_TypeOStuff.currentText())
            pModel = str(self.cb_ModelOStuff.currentText())
            pSerialNum = str(self.le_SNOStuff.text())
            pMaker = str(self.cb_MakerOStuff.currentText())
            pDistributor = str(self.cb_DistribOStuff.currentText())
            pInputDate = str(self.de_ComeTimeOStuff.text())
            pTargerObj = str(self.cb_TargetObjStuff.currentText())
            if str(self.de_TransferDate.text()) == "01.01.2000":
                pTransferDate = "None"
            else:
                pTransferDate = str(self.de_TransferDate.text())
            pComment = str(self.tE_OComment.toPlainText())
            changeType = ""
            if GlobalValues.OTblCurrTypeObj != pType:
                changeType = "Тип объекта"
                oldstate = GlobalValues.OTblCurrTypeObj
                newstate = pType
                GlobalValues.Hystory(GlobalValues.UserName, newstate, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkTypeWasChanged = True
                checkDataWasChanged = True

            if GlobalValues.OTblCurrModelObj != pModel:
                changeType = "Модель объекта"
                oldstate = GlobalValues.OTblCurrModelObj
                newstate = pModel
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.OTblCurrTypeObj, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkModelWasChanged = True
                checkDataWasChanged = True

            if GlobalValues.OTblCurrSerialNumObj != pSerialNum:
                changeType = "Серийный номер"
                oldstate = GlobalValues.OTblCurrSerialNumObj
                newstate = pSerialNum
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.OTblCurrTypeObj, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkSerialWasChanged = True
                checkDataWasChanged = True

            if GlobalValues.OTblCurrMakerObj != pMaker:
                changeType = "Производитель"
                oldstate = GlobalValues.OTblCurrMakerObj
                newstate = pMaker
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.OTblCurrTypeObj, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkMakerWasChanged = True
                checkDataWasChanged = True

            if GlobalValues.OTblCurrDistributorObj != pDistributor:
                changeType = "Поставщик"
                oldstate = GlobalValues.OTblCurrDistributorObj
                newstate = pDistributor
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.OTblCurrTypeObj, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkDistributorWasChanged = True
                checkDataWasChanged = True

            if GlobalValues.OTblCurrInputDateObj != pInputDate:
                changeType = "Дата поступления"
                oldstate = GlobalValues.OTblCurrInputDateObj
                newstate = pInputDate
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.OTblCurrTypeObj, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkInputDateWasChanged = True
                checkDataWasChanged = True

            if GlobalValues.OTblCurrTargetObj != pTargerObj:
                changeType = "Целевой объект"
                oldstate = GlobalValues.OTblCurrTargetObj
                newstate = pTargerObj
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.OTblCurrTypeObj, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkTargetObjWasChanged = True
                checkDataWasChanged = True

            if GlobalValues.OTblCurrTransferDateObj != pTransferDate:
                changeType = "Дата перемещения"
                oldstate = GlobalValues.OTblCurrTransferDateObj
                newstate = pTransferDate
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.OTblCurrTypeObj, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkTransferDateWasChanged = True
                checkDataWasChanged = True

            if GlobalValues.OTblCurrComment != pComment:
                changeType = "Комментарий"
                oldstate = GlobalValues.OTblCurrComment
                newstate = pComment
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.OTblCurrTypeObj, GlobalValues.OTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                self.checkCommentWasChanged = True
                checkDataWasChanged = True


            if pSerialNum == "":
                GlobalValues.MesText = "Ошибка! Введите серийный номер!"
                self.openMesBox()
            else:
                if checkDataWasChanged == False:
                    GlobalValues.MesText = "Изменений не найдено!"
                    self.openMesBox()
                else:
                    checkDataWasChanged = False
                    con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                          port=int(GlobalValues.SqlPort),
                                          user=str(GlobalValues.SqlUserName),
                                          passwd=str(GlobalValues.SqlPwd),
                                          db=str(GlobalValues.SqlDBName))
                    with con:

                        cur = con.cursor()
                        cur.execute(
                            "SELECT ID, OSerialNum FROM ostuff WHERE OSerialNum Like '%" + self.le_SNOStuff.text() + "%'")
                        rows = cur.fetchall()
                        time.sleep(0.2)
                        tempID = pID
                        if (len(rows) != 0):
                            for row in rows:
                                tempID = row[0]
                        if (pID != str(tempID)):
                            GlobalValues.MesText = "Ошибка! Серийный номер уже существует!"
                            self.openMesBox()
                        else:
                            if self.checkTypeWasChanged == True:
                                cur = con.cursor()
                                query = ("UPDATE ostuff SET OType = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pType, pID))
                                time.sleep(0.05)

                            if self.checkModelWasChanged == True:
                                cur = con.cursor()
                                query = ("UPDATE ostuff SET OModel = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pModel, pID))
                                time.sleep(0.05)

                            if self.checkSerialWasChanged == True:
                                cur = con.cursor()
                                query = ("UPDATE ostuff SET OSerialNum = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pSerialNum, pID))
                                time.sleep(0.05)

                            if self.checkDistributorWasChanged == True:
                                cur = con.cursor()
                                query = ("UPDATE ostuff SET ODistributor = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pDistributor, pID))
                                time.sleep(0.05)

                            if self.checkMakerWasChanged == True:
                                cur = con.cursor()
                                query = ("UPDATE ostuff SET OMaker = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pMaker, pID))
                                time.sleep(0.05)

                            if self.checkInputDateWasChanged == True:
                                cur = con.cursor()
                                query = ("UPDATE ostuff SET OComeTime = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pInputDate, pID))
                                time.sleep(0.05)

                            if self.checkTargetObjWasChanged == True:
                                cur = con.cursor()
                                query = ("UPDATE ostuff SET OTargetObj = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pTargerObj, pID))
                                time.sleep(0.05)

                            if self.checkCommentWasChanged == True:
                                cur = con.cursor()
                                query = ("UPDATE ostuff SET OComment = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pComment, pID))
                                time.sleep(0.05)

                            if self.checkTransferDateWasChanged == True:
                                if self.checkTransferDateNone == False:
                                    query = ("UPDATE ostuff SET OGoneToObjTime = (%s) WHERE ID = (%s)")
                                    cur.execute(query, (pTransferDate, pID))
                                    time.sleep(0.05)
                            checkMakeUpdate = True

                        cur.close()
                    # con.close()

                if GlobalValues.checkGlobalviewMode == True:
                    GlobalValues.checkOTblUpdateEvent = True
                else:
                    GlobalValues.checkTreeUpdateEvent = True
                time.sleep(0.2)

                GlobalValues.checkTreeStatesUpdate = True


                if checkMakeUpdate == True:
                    self.close()



if __name__ == "__main__":
    uiEditOStuff = Ui_EditOStuff()
    uiEditOStuff.show()
    sys.exit(app.exec_())
