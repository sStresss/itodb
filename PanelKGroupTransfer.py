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
import datetime
import sys
import GlobalValues
import pymysql
from PanelMesBox import Ui_MesBox

app = QtWidgets.QApplication(sys.argv)

class Ui_KGroupTransfer(QDialog):


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
        self.de_TransferDate = QtWidgets.QDateEdit(self.frame)
        self.de_TransferDate.setGeometry(QtCore.QRect(150, 110, 201, 22))
        self.de_TransferDate.setObjectName("de_TransferDate")
        self.cb_ParenKbjName = QtWidgets.QComboBox(self.frame)
        self.cb_ParenKbjName.setGeometry(QtCore.QRect(150, 50, 201, 22))
        self.cb_ParenKbjName.setObjectName("cb_ParenKbjName")
        self.cb_ChildKbjName = QtWidgets.QComboBox(self.frame)
        self.cb_ChildKbjName.setGeometry(QtCore.QRect(150, 80, 201, 22))
        self.cb_ChildKbjName.setObjectName("cb_ChildKbjName")
        self.btn_Transfer = QtWidgets.QPushButton(self.frame)
        self.btn_Transfer.setGeometry(QtCore.QRect(264, 150, 91, 23))
        self.btn_Transfer.setObjectName("btn_Transfer")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 83, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 106, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 53, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.FirstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_Transfer.setText(_translate("Dialog", "Переместить"))
        self.label_3.setText(_translate("Dialog", "Имя подобъекта:"))
        self.label_4.setText(_translate("Dialog", "Дата перемещения:"))
        self.label_2.setText(_translate("Dialog", "Куда переместить:"))
        self.label.setText(_translate("Dialog", "Перемещение комплектующих"))

    def FirstSets(self):
        self.MakeParentList()
        self.cb_ParenKbjName.currentIndexChanged.connect(self.MakeCurrChildList)
        self.btn_Transfer.clicked.connect(self.MakeKTransfer)
        data = time.localtime()
        year = data[0]
        month = data[1]
        day = data[2]
        self.de_TransferDate.setDate(QtCore.QDate(year, month, day))

        self.MakeParentList()
        self.cb_ParenKbjName.setCurrentIndex(0)
        self.MakeCurrChildList()

    def MakeParentList(self):
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
            cur.execute("SELECT ParentObjName, ConnectionID FROM treeobjtbl")
            curr_PObj_list_rows = cur.fetchall()
            cur.execute("SELECT ChildNameObj, ConnectionID FROM treechildobjtbl")
            curr_CObj_list_rows = cur.fetchall()


            indexlist = 0
            temp__p_index = 0
            temp_c_index = 0
            for row in curr_PObj_list_rows:
                if str(row[0]) != "Резерв":
                    if str(GlobalValues.KTblCurrFactObj) != str(row[0]):
                        self.cb_ParenKbjName.addItem(str(row[0]))
                        temp__p_index+=1
                    else:
                        for row1 in curr_CObj_list_rows:
                            if str(row1[1]) == str(row[1]):
                                temp_c_index+=1
                        if temp_c_index != 0:
                            self.cb_ParenKbjName.addItem(str(row[0]))
                    indexlist+=1

    def MakeCurrChildList(self):
        self.cb_ChildKbjName.clear()
        self.cb_ChildKbjName.update()
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
            cur.execute("SELECT ParentObjName, ConnectionID FROM treeobjtbl")
            temp_PObj_list_rows = cur.fetchall()
            cur.execute("SELECT ChildID, ChildNameObj, ConnectionID FROM treechildobjtbl")
            temp_CObj_list_rows = cur.fetchall()
            cur.execute("SELECT ID, ParentID, ChildID FROM kstuff")
            temp_data_list_rows = cur.fetchall()

            curr_ParentName = str(self.cb_ParenKbjName.currentText())
            curr_ParentID = ""

            for temp_data_row in temp_data_list_rows:
                if str(temp_data_row[0]) == str(GlobalValues.KTblCurrID):
                    currChildID = str(temp_data_row[2])
                    print(str(currChildID))

            for temp_P_row in temp_PObj_list_rows:
                if str(temp_P_row[0]) == str(curr_ParentName):
                    curr_ParentID = str(temp_P_row[1])
            newtemp_c_index = 0
            for temp_C_row in temp_CObj_list_rows:
                if str(curr_ParentID) == str(temp_C_row[2]) and str(currChildID) != str(temp_C_row[0]):
                    self.cb_ChildKbjName.addItem(str(temp_C_row[1]))
                newtemp_c_index+=1
        # con.close()

    def MakeKTransfer(self):
        GlobalValues.MesText = "Переместить. Вы уверены?"
        self.openMexBox()
        currDate = self.de_TransferDate.text()
        if GlobalValues.MesResult == True:
            clear = None
            checkChildTransfer = False
            targetParentObj = self.cb_ParenKbjName.currentText()
            if self.cb_ChildKbjName.currentText() != "" :
                targetChildObj = self.cb_ChildKbjName.currentText()
                checkChildTransfer = True
            else:
                targetChildObj = None

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ObjID, ParentObjName FROM treeobjtbl")
                rows = cur.fetchall()
                for row in rows:
                    if str(row[1]) == str(targetParentObj):
                        targetCurrParentID = str(row[0])

                for elem in GlobalValues.ktbl_selected_lst:
                    query = ("UPDATE kstuff SET ParentID = (%s) WHERE ID = (%s)")
                    cur.execute(query, (targetCurrParentID, elem[0]))
                    query = ("UPDATE kstuff SET KFactObj = (%s) WHERE ID = (%s)")
                    cur.execute(query, (str(targetParentObj), elem[0]))
                    query = ("UPDATE kstuff SET KGoneTOObjTime = (%s) WHERE ID = (%s)")
                    cur.execute(query, (str(currDate), elem[0]))
                    query = ("UPDATE kstuff SET ChildID = (%s) WHERE ID = (%s)")
                    cur.execute(query, (clear, elem[0]))
                    if checkChildTransfer == True:
                        cur.execute("SELECT ChildID, ChildNameObj, ConnectionID FROM treechildobjtbl")
                        rows = cur.fetchall()
                        cur.execute("SELECT ObjID, ParentObjName, ConnectionID FROM treeobjtbl")
                        rows1 = cur.fetchall()
                        CurrParentName = str(self.cb_ParenKbjName.currentText())
                        for row1 in rows1:
                            if str(CurrParentName) == str(row1[1]):
                                CurrParentConID = str(row1[2])

                        for row in rows:
                            if str(row[1]) == str(targetChildObj) and str(row[2]) == str(CurrParentConID):
                                targetCurrChildID = row[0]
                        query = ("UPDATE kstuff SET ChildID = (%s) WHERE ID = (%s)")
                        cur.execute(query, (targetCurrChildID, elem[0]))

                    GlobalValues.Hystory(GlobalValues.UserName, elem[1],
                                         elem[2],
                                         "Перемещение с " + str(elem[3]) + " на " + str(
                                             targetParentObj))
                    time.sleep(0.05)
                con.commit()
                time.sleep(0.05)


        if GlobalValues.checkGlobalviewMode == False:
            GlobalValues.checkTreeUpdateEvent = True
        else:
            GlobalValues.checkKTblUpdateEvent = True
        GlobalValues.checkTreeStatesUpdate = True
        self.close()
        time.sleep(0.2)

    def openMexBox(self):
        self.uiMesBox = Ui_MesBox()
        self.uiMesBox.exec_()






if __name__ == "__main__":
    uiKGroupTransfer = Ui_KGroupTransfer()
    uiKGroupTransfer.show()
    sys.exit(app.exec_())
