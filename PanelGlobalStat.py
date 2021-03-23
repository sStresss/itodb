# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PanelJournal_v15.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt

from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import threading
import time
import sys
import GlobalValues
import MainPanel
from PanelMesBox import Ui_MesBox
import pymysql
from PanelGlobStatSett import Ui_GlobStatSett
from PanelGlobStatEdit import Ui_GlobStatEdit
app = QtWidgets.QApplication(sys.argv)

def getObjStat():
    Ui_GlobalStat.getObjStat()

class Ui_GlobalStat(QDialog):

    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(1257, 790)
        self.setStyleSheet("")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 1251, 791))
        self.lblBack.setStyleSheet("background-color: rgb(242,242,242);")
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.tbl_StatTbl = QtWidgets.QTableWidget(self)
        self.tbl_StatTbl.setGeometry(QtCore.QRect(13, 25, 1221, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_StatTbl.sizePolicy().hasHeightForWidth())
        self.tbl_StatTbl.setSizePolicy(sizePolicy)
        self.tbl_StatTbl.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tbl_StatTbl.setStyleSheet("QTableWidget {background-color: rgb(255,255,255);\n"
                                       "border: 1px solid rgb(150,150,150);\n"
                                       "gridline-color: rgb(42,42,42);\n"
                                       "border-radius:0px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "color:black;}\n"
                                       "\n"
                                       "QLineEdit {background-color: white;}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "gridline-color: rgb(89,89,89);\n"
                                       "background-color: rgb(142,187,208);\n"
                                       "color: black;};")
        self.tbl_StatTbl.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_StatTbl.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_StatTbl.setAutoScrollMargin(5)
        self.tbl_StatTbl.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.tbl_StatTbl.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_StatTbl.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_StatTbl.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tbl_StatTbl.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl_StatTbl.setObjectName("tbl_StatTbl")
        self.tbl_StatTbl.setColumnCount(5)
        self.tbl_StatTbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_StatTbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_StatTbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_StatTbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_StatTbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_StatTbl.setHorizontalHeaderItem(4, item)
        self.tbl_StatTbl.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_StatTbl.horizontalHeader().setDefaultSectionSize(157)
        self.tbl_StatTbl.horizontalHeader().setHighlightSections(True)
        self.tbl_StatTbl.verticalHeader().setVisible(False)
        self.vScrl_TblStat = QtWidgets.QScrollBar(self)
        self.vScrl_TblStat.setGeometry(QtCore.QRect(1233, 48, 11, 338))
        self.vScrl_TblStat.setStyleSheet("QScrollBar:vertical {\n"
                                         "border: 1px solid rgb(89,89,89);\n"
                                         " background: rgb(255,255,255);\n"
                                         "width:10px;\n"
                                         "margin: 0px 0px 0px 0px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical {\n"
                                         "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0 rgb(142,187,208), stop: 0.5 rgb(142,187,208), stop:1 rgb(142,187,208));\n"
                                         "min-height: 5px;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical {\n"
                                         " background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(142,187,208), stop: 0.5 rgb(142,187,208),  stop:1 rgb(142,187,208));\n"
                                         "height: 0px;\n"
                                         "subcontrol-position: bottom;\n"
                                         "subcontrol-origin: margin;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical {\n"
                                         "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0  rgb(142,187,208), stop: 0.5 rgb(142,187,208),  stop:1 rgb(142,187,208));\n"
                                         "height: 0 px;\n"
                                         "subcontrol-position: top;\n"
                                         "subcontrol-origin: margin;\n"
                                         "}")
        self.vScrl_TblStat.setMaximum(101)
        self.vScrl_TblStat.setOrientation(QtCore.Qt.Vertical)
        self.vScrl_TblStat.setObjectName("vScrl_TblStat")
        self.btn_Sett = QtWidgets.QPushButton(self)
        self.btn_Sett.setGeometry(QtCore.QRect(12, 24, 26, 25))
        self.btn_Sett.setObjectName("btn_Sett")
        self.btn_Spec = QtWidgets.QPushButton(self)
        self.btn_Spec.setGeometry(QtCore.QRect(1209, 24, 26, 25))
        self.btn_Spec.setObjectName("btn_Spec")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(12, 5, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(12, 395, 371, 16))
        self.label_2.setObjectName("label_2")
        self.vScrl_TblConn = QtWidgets.QScrollBar(self)
        self.vScrl_TblConn.setGeometry(QtCore.QRect(1233, 438, 11, 338))
        self.vScrl_TblConn.setStyleSheet("QScrollBar:vertical {\n"
                                         "border: 1px solid rgb(89,89,89);\n"
                                         " background: rgb(255,255,255);\n"
                                         "width:10px;\n"
                                         "margin: 0px 0px 0px 0px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical {\n"
                                         "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0 rgb(142,187,208), stop: 0.5 rgb(142,187,208), stop:1 rgb(142,187,208));\n"
                                         "min-height: 5px;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical {\n"
                                         " background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(142,187,208), stop: 0.5 rgb(142,187,208),  stop:1 rgb(142,187,208));\n"
                                         "height: 0px;\n"
                                         "subcontrol-position: bottom;\n"
                                         "subcontrol-origin: margin;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical {\n"
                                         "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0  rgb(142,187,208), stop: 0.5 rgb(142,187,208),  stop:1 rgb(142,187,208));\n"
                                         "height: 0 px;\n"
                                         "subcontrol-position: top;\n"
                                         "subcontrol-origin: margin;\n"
                                         "}")
        self.vScrl_TblConn.setMaximum(101)
        self.vScrl_TblConn.setOrientation(QtCore.Qt.Vertical)
        self.vScrl_TblConn.setObjectName("vScrl_TblConn")
        self.tbl_ConnTbl = QtWidgets.QTableWidget(self)
        self.tbl_ConnTbl.setGeometry(QtCore.QRect(13, 415, 1221, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_ConnTbl.sizePolicy().hasHeightForWidth())
        self.tbl_ConnTbl.setSizePolicy(sizePolicy)
        self.tbl_ConnTbl.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tbl_ConnTbl.setStyleSheet("QTableWidget {background-color: rgb(255,255,255);\n"
                                       "border: 1px solid rgb(150,150,150);\n"
                                       "gridline-color: rgb(42,42,42);\n"
                                       "border-radius:0px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "color:black;}\n"
                                       "\n"
                                       "QLineEdit {background-color: white;}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "gridline-color: rgb(89,89,89);\n"
                                       "background-color: rgb(142,187,208);\n"
                                       "color: black;};")
        self.tbl_ConnTbl.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_ConnTbl.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_ConnTbl.setAutoScrollMargin(5)
        self.tbl_ConnTbl.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.tbl_ConnTbl.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_ConnTbl.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_ConnTbl.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tbl_ConnTbl.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tbl_ConnTbl.setObjectName("tbl_ConnTbl")
        self.tbl_ConnTbl.setColumnCount(6)
        self.tbl_ConnTbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ConnTbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ConnTbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ConnTbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ConnTbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ConnTbl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_ConnTbl.setHorizontalHeaderItem(5, item)
        self.tbl_ConnTbl.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_ConnTbl.horizontalHeader().setDefaultSectionSize(157)
        self.tbl_ConnTbl.horizontalHeader().setHighlightSections(True)
        self.tbl_ConnTbl.verticalHeader().setVisible(False)

        #===============================================================================================================
        self.tbl_StatTbl.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tbl_StatTbl.customContextMenuRequested.connect(self.generateMenu)
        self.tbl_StatTbl.viewport().installEventFilter(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tbl_StatTbl)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.firstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Статистика"))
        self.tbl_StatTbl.setSortingEnabled(False)
        item = self.tbl_StatTbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Оборудование"))
        item = self.tbl_StatTbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Модель"))
        item = self.tbl_StatTbl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Спека, шт."))
        item = self.tbl_StatTbl.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Факт, шт."))
        item = self.tbl_StatTbl.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Расшифровка"))
        self.btn_Sett.setText(_translate("Dialog", "#"))
        self.btn_Spec.setText(_translate("Dialog", "C"))
        self.label.setText(_translate("Dialog", "Текущая комплектность"))
        self.label_2.setText(_translate("Dialog", "Возможные связности"))
        self.tbl_ConnTbl.setSortingEnabled(False)
        item = self.tbl_ConnTbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Оборудование"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Модель"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Серийный номер"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Целевой объект"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Фактический объект"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Причина связности"))

    def firstSets(self):
        self.objParentName = GlobalValues.TreeParentName
        GlobalValues.pTreeParentName = self.objParentName
        # print("ENTER in FUNC firstSets")

        self.btn_Spec.clicked.connect(self.openSpec)
        self.btn_Sett.clicked.connect(self.openGlobStatSett)

        self.tbl_StatTbl.setColumnWidth(0,180)
        self.tbl_StatTbl.setColumnWidth(1,180)
        self.tbl_StatTbl.setColumnWidth(2,80)
        self.tbl_StatTbl.setColumnWidth(3,80)
        self.tbl_StatTbl.setColumnWidth(4,700)
        self.tbl_StatTbl.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tbl_StatTbl.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tbl_StatTbl.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tbl_StatTbl.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tbl_StatTbl.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)

        self.tbl_ConnTbl.setColumnWidth(0,180)
        self.tbl_ConnTbl.setColumnWidth(1,180)
        self.tbl_ConnTbl.setColumnWidth(2,180)
        self.tbl_ConnTbl.setColumnWidth(3,150)
        self.tbl_ConnTbl.setColumnWidth(4,150)
        self.tbl_ConnTbl.setColumnWidth(5,380)
        self.tbl_ConnTbl.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tbl_ConnTbl.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tbl_ConnTbl.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tbl_ConnTbl.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tbl_ConnTbl.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tbl_ConnTbl.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)

        self.thStatTblUpdate()
        check = self.getObjStat()
        print('OBJ CHECKING: ', str(check))
        GlobalValues.checkGlobStatTblUpdateEvent = True

    def openSpec(self):
        GlobalValues.checkOpenSpecFromGlobalStat = True

    def openGlobStatSett(self):
        self.uiGlobStatSett = Ui_GlobStatSett()
        self.uiGlobStatSett.exec_()

    def thStatTblUpdate(self):
        # print("ENTER in FUNC thStatTblUpdate")
        th = threading.Thread(target=self.TblUpdateThread)
        th.start()

    def TblUpdateThread(self):
        # print("ENTER in FUNC TblUpdateThread")

        while True:
            if (GlobalValues.checkGlobStatTblUpdateEvent == True):
                GlobalValues.checkGlobStatTblUpdateEvent = False
                print('STAT TBL UPD COLLING')
                self.statTblUpdate()
            if GlobalValues.checkStopGlobStatThread == True:
                GlobalValues.checkStopGlobStatThread = False
                break
            time.sleep(0.5)

    def statTblUpdate(self):
        print('stat tbl update start')
        # print("ENTER in FUNC statTblUpdate")
        self.tbl_StatTbl.setRowCount(0)
        # print("statTblUpdate start!")
        objName = self.objParentName

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

        cur.execute(
            "SELECT TypeObj, ModelObj, Num, ConID  FROM globstattbl WHERE ConID Like '" + str(conID) + "'")
        rows = cur.fetchall()

        valWdg = 0

        countRow = len(rows)

        for row in reversed(rows):
            countRow -= 1
            self.tbl_StatTbl.insertRow(valWdg)

            item = QtWidgets.QTableWidgetItem(str(row[0]))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tbl_StatTbl.setItem(valWdg, 0, item)

            item = QtWidgets.QTableWidgetItem(str(row[1]))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tbl_StatTbl.setItem(valWdg, 1, item)

            item = QtWidgets.QTableWidgetItem(str(row[2]))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tbl_StatTbl.setItem(valWdg, 2, item)

            GlobalValues.STblCurrTypeObj = str(row[0])
            GlobalValues.STblCurrModelObj = str(row[1])
            GlobalValues.STblCurrNumBySpec = str(row[2])
            factNum, comment = self.getElemStat(con)

            item = QtWidgets.QTableWidgetItem(str(factNum))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tbl_StatTbl.setItem(valWdg, 3, item)

            item = QtWidgets.QTableWidgetItem(str(comment))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tbl_StatTbl.setItem(valWdg, 4, item)

        self.tbl_StatTbl.update()
        print('stat tbl update end')


    def generateMenu(self, pos):
        # print("pos======", pos)
        self.menu.exec(self.tbl_StatTbl.mapToGlobal(pos))

    def closeEvent(self, event):
        GlobalValues.checkStopGlobStatThread = True
        event.accept()


    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonPress and
                event.buttons() == QtCore.Qt.RightButton and
                source is self.tbl_StatTbl.viewport()):
            item = self.tbl_StatTbl.itemAt(event.pos())
            if item is not None:
                #определение параметров ячеек нажатой строки
                GlobalValues.STblCurrTypeObj = self.tbl_StatTbl.item(item.row(), 0).text()
                GlobalValues.STblCurrModelObj = self.tbl_StatTbl.item(item.row(), 1).text()
                GlobalValues.STblCurrNumBySpec = self.tbl_StatTbl.item(item.row(), 2).text()


                # создание контекста
                self.menu = QMenu(self)
                self.menu.setStyleSheet("""
                     QMenu {border: 1px inset grey; background-color: #fff; color: #000; padding: -1; padding-left: -6;}
                     QMenu:selected {background-color: #ddf; color: #000;}
                 """)
                self.menu.setFixedWidth(105)

                self.menu_actionBtn1 = QAction('Редактировать', self)
                self.menu_actionBtn1.setData('option1')
                self.menu_actionBtn1.triggered.connect(self.openRecEdit)
                self.menu.addAction(self.menu_actionBtn1)


                self.menu_actionBtn2 = QAction('Удалить', self)
                self.menu_actionBtn2.setData('option2')
                self.menu_actionBtn2.triggered.connect(self.openRecDel)
                self.menu.addAction(self.menu_actionBtn2)

        return super(Ui_GlobalStat, self).eventFilter(source, event)

    def openRecEdit(self):
        self.openPanelGlobStatEdit()


    def openRecDel(self):
        GlobalValues.MesText = 'Удалить объект?'
        self.openMesBox()
        if GlobalValues.MesResult == True:
            curID = self.getCurrID()

            print('DEL CurID: ', str(curID))
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))

            cur = con.cursor()

            del_query = ("DELETE FROM globstattbl where ID = (%s)")
            cur.execute(del_query, curID)
            con.commit()

            GlobalValues.checkGlobStatTblUpdateEvent = True
            GlobalValues.checkTreeStatesUpdate = True

    def getElemStat(self, db_con):
        checkObj = False
        pType = GlobalValues.STblCurrTypeObj
        pModel = GlobalValues.STblCurrModelObj
        pNumBySpec = GlobalValues.STblCurrNumBySpec
        pTargetObj = self.objParentName

        con = db_con

        cur = con.cursor()
        cur.execute(
            "SELECT OTypeName FROM otypetbl WHERE OTypeName Like '" + str(pType) + "'")
        orows = cur.fetchall()

        if str(len(orows)) == '1':
            checkObj = False
        else:
            checkObj = True
        # print(checkObj)

        if checkObj == False:
            cur.execute(
                "SELECT OType, OModel, OTargetObj, OFactObj FROM ostuff")
            StuffRows = cur.fetchall()

        else:
            cur.execute(
                "SELECT KType, KModel, KTargetObj, KFactObj FROM kstuff")
            StuffRows = cur.fetchall()

        # print('StuffRows: ', str(StuffRows))
        pFactNum = 0

        for row in StuffRows:
            if (str(row[2]) == pTargetObj) or (str(row[3]) == pTargetObj):
                if str(row[0]) == pType:
                    if str(row[1]) == pModel:
                        if (str(row[3]) == 'Склад Офис') or (str(row[3]) == pTargetObj):
                            pFactNum +=1

        # pFactNum = 'неопределено'
        pComment = 'неопределено'
        pFactNum = str(pFactNum)
        return pFactNum, pComment

    def getObjStat(self):
        pArr = []
        curConID = 0
        checkObj = True
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
            "SELECT ConnectionID FROM treeobjtbl WHERE ParentObjName Like '" + str(GlobalValues.TreeParentName) + "'")
        rows = cur.fetchall()


        for row in rows:
            curConID = row[0]
        print('COnnectID: ', str(curConID))

        cur.execute(
            "SELECT TypeObj, ModelObj, Num, ConID FROM globstattbl WHERE ConID Like '" + str(curConID) + "'")
        statCellRows = cur.fetchall()
        print(statCellRows)

        for row in statCellRows:
            GlobalValues.STblCurrTypeObj = row[0]
            GlobalValues.STblCurrModelObj = row[1]
            GlobalValues.STblCurrNumBySpec = row[2]

            factNum, comment = self.getElemStat(con)
            print('specNum: ', str(row[2]))
            print('factNUM: ', str(factNum))
            if str(row[2]) != str(factNum):
                checkObj = False

        return checkObj

    def getCurrID(self):
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
            if row[1] == GlobalValues.STblCurrModelObj:
                if row[2] == GlobalValues.STblCurrTypeObj:
                    if row[3] == GlobalValues.STblCurrNumBySpec:
                        pID = row[0]
        return pID

    def openPanelGlobStatEdit(self):
        self.uiGlobStatEdit = Ui_GlobStatEdit()
        self.uiGlobStatEdit.exec_()

    def openMesBox(self):
        self.uiMesBox = Ui_MesBox()
        self.uiMesBox.exec_()


if __name__ == "__main__":
    uiGlobalStat = Ui_GlobalStat()
    uiGlobalStat.show()
    sys.exit(app.exec_())
