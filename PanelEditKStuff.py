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

class Ui_EditKStuff(QDialog):

    checkTransferDateNone = False

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
        self.cb_MakerKStuff = QtWidgets.QComboBox(self.frame)
        self.cb_MakerKStuff.setGeometry(QtCore.QRect(150, 170, 201, 22))
        self.cb_MakerKStuff.setObjectName("cb_MakerKStuff")
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
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 233, 111, 16))
        self.label_12.setObjectName("label_12")
        self.cb_TypeKStuff = QtWidgets.QComboBox(self.frame)
        self.cb_TypeKStuff.setGeometry(QtCore.QRect(150, 80, 201, 22))
        self.cb_TypeKStuff.setObjectName("cb_TypeKStuff")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 30, 311, 31))
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
        self.de_ComeTimeKStuff = QtWidgets.QDateEdit(self.frame)
        self.de_ComeTimeKStuff.setGeometry(QtCore.QRect(150, 230, 201, 22))
        self.de_ComeTimeKStuff.setObjectName("de_ComeTimeKStuff")
        self.btn_AddKStuff = QtWidgets.QPushButton(self.frame)
        self.btn_AddKStuff.setGeometry(QtCore.QRect(280, 430, 75, 23))
        self.btn_AddKStuff.setObjectName("btn_AddKStuff")
        self.cb_TargetKbjStuff = QtWidgets.QComboBox(self.frame)
        self.cb_TargetKbjStuff.setGeometry(QtCore.QRect(150, 260, 201, 22))
        self.cb_TargetKbjStuff.setObjectName("cb_TargetKbjStuff")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 264, 101, 16))
        self.label_10.setObjectName("label_10")
        self.le_SNKStuff = QtWidgets.QLineEdit(self.frame)
        self.le_SNKStuff.setGeometry(QtCore.QRect(150, 140, 201, 22))
        self.le_SNKStuff.setObjectName("le_SNKStuff")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 203, 91, 16))
        self.label_8.setObjectName("label_8")
        self.de_TransferDate = QtWidgets.QDateEdit(self.frame)
        self.de_TransferDate.setGeometry(QtCore.QRect(150, 290, 201, 22))
        self.de_TransferDate.setObjectName("de_TransferDate")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 101, 16))
        self.label_6.setObjectName("label_6")
        self.tE_KComment = QtWidgets.QTextEdit(self.frame)
        self.tE_KComment.setGeometry(QtCore.QRect(150, 320, 201, 91))
        self.tE_KComment.setObjectName("tE_KComment")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.FirstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Панель редактирования"))
        self.label_9.setText(_translate("Dialog", "Производитель"))
        self.label_3.setText(_translate("Dialog", "Модель"))
        self.label_7.setText(_translate("Dialog", "Дата перемещения"))
        self.label_12.setText(_translate("Dialog", "Дата поступления"))
        self.label_2.setText(_translate("Dialog", "Тип"))
        self.label.setText(_translate("Dialog", "Комплектующие | Редактирование"))
        self.label_4.setText(_translate("Dialog", "S/n"))
        self.btn_AddKStuff.setText(_translate("Dialog", "Сохранить"))
        self.label_10.setText(_translate("Dialog", "Целевой объект"))
        self.label_8.setText(_translate("Dialog", "Поставщик"))
        self.label_6.setText(_translate("Dialog", "Комментарий:"))

    def FirstSets(self):
        GlobalValues.checkKTblWasClicked = False
        self.btn_AddKStuff.clicked.connect(self.MakeUpdate)
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
        self.cb_TypeKStuff.addItem(str(GlobalValues.KTblCurrTypeObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ID, KTypeName FROM ktypetbl")

            rows = cur.fetchall()

            for row in rows:
                if str(row[1]) != str(GlobalValues.KTblCurrTypeObj):
                    self.cb_TypeKStuff.addItem(str(row[1]))
            cur.close()
        # con.close()

    def MakeCurrModelList(self):
        self.cb_ModelKStuff.addItem(str(GlobalValues.KTblCurrModelObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ID, KModelName FROM kmodeltbl")

            rows = cur.fetchall()

            for row in rows:
                if str(row[1]) != str(GlobalValues.KTblCurrModelObj):
                    self.cb_ModelKStuff.addItem(str(row[1]))
            cur.close()
        # con.close()

    def MakeCurrSerialNum(self):
        self.le_SNKStuff.setText(str(GlobalValues.KTblCurrSerialNumObj))

    def MakeCurrMakerList(self):
        self.cb_MakerKStuff.addItem(str(GlobalValues.KTblCurrMakerObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ID, KMakerName FROM kmakertbl")

            rows = cur.fetchall()

            for row in rows:
                if str(row[1]) != str(GlobalValues.KTblCurrMakerObj):
                    self.cb_MakerKStuff.addItem(str(row[1]))
            cur.close()
        # con.close()

    def MakeDistributorList(self):
        self.cb_DistribKStuff.addItem(str(GlobalValues.KTblCurrDistributorObj))
        con = pymysql.connect(host=GlobalValues.SqlHostname,
                              port=GlobalValues.SqlPort,
                              user=GlobalValues.SqlUserName,
                              passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)

        with con:
            cur = con.cursor()
            cur.execute(
                "SELECT ID, KDistributorName FROM kdistributortbl")

            rows = cur.fetchall()

            for row in rows:
                if str(row[1]) != str(GlobalValues.KTblCurrDistributorObj):
                    self.cb_DistribKStuff.addItem(str(row[1]))
            cur.close()
        # con.close()

    def MakeInputDate(self):
        day = int(GlobalValues.KTblCurrInputDateObj[0] + GlobalValues.KTblCurrInputDateObj[1])
        month = int(GlobalValues.KTblCurrInputDateObj[3] + GlobalValues.KTblCurrInputDateObj[4])
        year = int(GlobalValues.KTblCurrInputDateObj[6] + GlobalValues.KTblCurrInputDateObj[7] +
                   GlobalValues.KTblCurrInputDateObj[8] + GlobalValues.KTblCurrInputDateObj[9])
        self.de_ComeTimeKStuff.setDate(QtCore.QDate(year, month, day))

    def MakeComment(self):
        self.tE_KComment.setPlainText(GlobalValues.KTblCurrComment)

    def MakeTargetObjList(self):
        self.cb_TargetKbjStuff.addItem(str(GlobalValues.KTblCurrTargetObj))
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
                    if str(row[1]) != str(GlobalValues.KTblCurrTargetObj):
                        self.cb_TargetKbjStuff.addItem(str(row[1]))
                count += 1
            cur.close()
        # con.close()

    def MakeTransferDate(self):
        if GlobalValues.KTblCurrTransferDateObj == "None":
            self.de_TransferDate.setEnabled(False)
            self.checkTransferDateNone = True
        else:
            self.checkTransferDateNone = False
            day = int(GlobalValues.KTblCurrTransferDateObj[0] + GlobalValues.KTblCurrTransferDateObj[1])
            month = int(GlobalValues.KTblCurrTransferDateObj[3] + GlobalValues.KTblCurrTransferDateObj[4])
            year = int(GlobalValues.KTblCurrTransferDateObj[6] + GlobalValues.KTblCurrTransferDateObj[7] +
                       GlobalValues.KTblCurrTransferDateObj[8] + GlobalValues.KTblCurrTransferDateObj[9])
            self.de_TransferDate.setDate(QtCore.QDate(year, month, day))

    def openMesBox(self):
        self.uiMesBox = Ui_MesBox()
        self.uiMesBox.exec_()

    def MakeUpdate(self):
        checkMakeUpdate = False
        checkDataWasChanged = False
        GlobalValues.MesText = "Вы уверены?"
        self.openMesBox()
        if GlobalValues.MesResult:
            pID = str(GlobalValues.KTblCurrID)
            pType = str(self.cb_TypeKStuff.currentText())
            pModel = str(self.cb_ModelKStuff.currentText())
            pSerialNum = str(self.le_SNKStuff.text())
            pMaker = str(self.cb_MakerKStuff.currentText())
            pDistributor = str(self.cb_DistribKStuff.currentText())
            pInputDate = str(self.de_ComeTimeKStuff.text())
            pTargerObj = str(self.cb_TargetKbjStuff.currentText())
            if str(self.de_TransferDate.text()) == "01.01.2000":
                pTransferDate = "None"
            else:
                pTransferDate = str(self.de_TransferDate.text())
            pComment = str(self.tE_KComment.toPlainText())
            changeType = ""
            print("DTran", pTransferDate)
            if GlobalValues.KTblCurrTypeObj != pType:
                changeType = "Тип объекта"
                oldstate = GlobalValues.KTblCurrTypeObj
                newstate = pType
                GlobalValues.Hystory(GlobalValues.UserName, newstate, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                checkDataWasChanged = True
            if GlobalValues.KTblCurrModelObj != pModel:
                changeType = "Модель объекта"
                oldstate = GlobalValues.KTblCurrModelObj
                newstate = pModel
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.KTblCurrTypeObj, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                checkDataWasChanged = True
            if GlobalValues.KTblCurrSerialNumObj != pSerialNum:
                changeType = "Серийный номер"
                oldstate = GlobalValues.KTblCurrSerialNumObj
                newstate = pSerialNum
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.KTblCurrTypeObj, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                checkDataWasChanged = True
            if GlobalValues.KTblCurrMakerObj != pMaker:
                changeType = "Производитель"
                oldstate = GlobalValues.KTblCurrMakerObj
                newstate = pMaker
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.KTblCurrTypeObj, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                checkDataWasChanged = True
            if GlobalValues.KTblCurrDistributorObj != pDistributor:
                changeType = "Поставщик"
                oldstate = GlobalValues.KTblCurrDistributorObj
                newstate = pDistributor
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.KTblCurrTypeObj, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                checkDataWasChanged = True
            if GlobalValues.KTblCurrInputDateObj != pInputDate:
                changeType = "Дата поступления"
                oldstate = GlobalValues.KTblCurrInputDateObj
                newstate = pInputDate
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.KTblCurrTypeObj, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                checkDataWasChanged = True
            if GlobalValues.KTblCurrTargetObj != pTargerObj:
                changeType = "Целевой объект"
                oldstate = GlobalValues.KTblCurrTargetObj
                newstate = pTargerObj
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.KTblCurrTypeObj, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                checkDataWasChanged = True
            if GlobalValues.KTblCurrTransferDateObj != pTransferDate:
                changeType = "Дата перемещения"
                oldstate = GlobalValues.KTblCurrTransferDateObj
                newstate = pTransferDate
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.KTblCurrTypeObj, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
                checkDataWasChanged = True
            if GlobalValues.KTblCurrComment != pComment:
                changeType = "Комментарий"
                oldstate = GlobalValues.KTblCurrComment
                newstate = pComment
                GlobalValues.Hystory(GlobalValues.UserName, GlobalValues.KTblCurrTypeObj, GlobalValues.KTblCurrSerialNumObj,
                                     "Редактирование. Параметр : " + changeType + " | " + oldstate + " был изменен на " + newstate)
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
                            "SELECT ID, KSerialNum FROM kstuff WHERE KSerialNum Like '%" + self.le_SNKStuff.text() + "%'")
                        rows = cur.fetchall()
                        print("row: ", rows)
                        tempID = pID
                        if (len(rows) != 0):
                            for row in rows:
                                tempID = row[0]
                        if (pID != str(tempID)):
                            print("pID: ", str(pID))
                            print("tempID: ", str(tempID))
                            GlobalValues.MesText = "Ошибка! Серийный номер уже существует!"
                            self.openMesBox()
                        else:

                            cur = con.cursor()
                            query = ("UPDATE kstuff SET KType = (%s) WHERE ID = (%s)")
                            cur.execute(query, (pType, pID))
                            time.sleep(0.05)

                            query = ("UPDATE kstuff SET KModel = (%s) WHERE ID = (%s)")
                            cur.execute(query, (pModel, pID))
                            time.sleep(0.05)

                            query = ("UPDATE kstuff SET KSerialNum = (%s) WHERE ID = (%s)")
                            cur.execute(query, (pSerialNum, pID))
                            time.sleep(0.05)

                            query = ("UPDATE kstuff SET KDistributor = (%s) WHERE ID = (%s)")
                            cur.execute(query, (pDistributor, pID))
                            time.sleep(0.05)

                            query = ("UPDATE kstuff SET KMaker = (%s) WHERE ID = (%s)")
                            cur.execute(query, (pMaker, pID))
                            time.sleep(0.05)

                            query = ("UPDATE kstuff SET KComeTime = (%s) WHERE ID = (%s)")
                            cur.execute(query, (pInputDate, pID))
                            time.sleep(0.05)

                            query = ("UPDATE kstuff SET KTargetObj = (%s) WHERE ID = (%s)")
                            cur.execute(query, (pTargerObj, pID))
                            time.sleep(0.05)

                            query = ("UPDATE kstuff SET KComment = (%s) WHERE ID = (%s)")
                            cur.execute(query, (pComment, pID))
                            time.sleep(0.05)

                            if self.checkTransferDateNone == False:
                                query = ("UPDATE kstuff SET KGoneToObjTime = (%s) WHERE ID = (%s)")
                                cur.execute(query, (pTransferDate, pID))
                            time.sleep(0.05)
                            checkMakeUpdate = True

                        cur.close()
                    # con.close()


                if GlobalValues.checkGlobalviewMode == True:
                    GlobalValues.checkKTblUpdateEvent = True
                else:
                    GlobalValues.checkTreeUpdateEvent = True

                GlobalValues.checkTreeStatesUpdate = True


                if GlobalValues.checkTreeStatesUpdate == True:
                    self.close()


if __name__ == "__main__":
    uiEditKStuff = Ui_EditKStuff()
    uiEditKStuff.show()
    sys.exit(app.exec_())
