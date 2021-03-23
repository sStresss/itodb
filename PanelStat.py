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

app = QtWidgets.QApplication(sys.argv)

class Ui_Stat(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(451, 581)
        self.setStyleSheet("")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 451, 581))
        self.lblBack.setStyleSheet("background-color: rgb(242,242,242);")
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.tbl_StatTbl = QtWidgets.QTableWidget(self)
        self.tbl_StatTbl.setGeometry(QtCore.QRect(10, 10, 421, 561))
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
        self.tbl_StatTbl.setColumnCount(3)
        self.tbl_StatTbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_StatTbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_StatTbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_StatTbl.setHorizontalHeaderItem(2, item)
        self.tbl_StatTbl.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_StatTbl.horizontalHeader().setDefaultSectionSize(157)
        self.tbl_StatTbl.horizontalHeader().setHighlightSections(True)
        self.tbl_StatTbl.verticalHeader().setVisible(False)
        self.vScrl_TblStat = QtWidgets.QScrollBar(self)
        self.vScrl_TblStat.setGeometry(QtCore.QRect(430, 33, 11, 538))
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


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.FirstSets()



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Статистика"))
        self.tbl_StatTbl.setSortingEnabled(False)
        item = self.tbl_StatTbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Тип объекта"))
        item = self.tbl_StatTbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Модель"))
        item = self.tbl_StatTbl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Количество, шт."))

    def FirstSets(self):
        self.tbl_StatTbl.setColumnWidth(0,160)
        self.tbl_StatTbl.setColumnWidth(1,160)
        self.tbl_StatTbl.setColumnWidth(2,100)
        self.tbl_StatTbl.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)
        self.tbl_StatTbl.horizontalHeader().setSectionResizeMode(1,QHeaderView.Fixed)
        self.tbl_StatTbl.horizontalHeader().setSectionResizeMode(2,QHeaderView.Fixed)

        self.MakeStat()

    def MakeStat(self):
        arr = GlobalValues.CurrStatArray
        unique_arr = []
        checkUnique = True
        res_arr = []
        for elem in arr:
            p_arr = []
            for p_elem in unique_arr:
                if str(elem[1]) == str(p_elem[1]):
                    checkUnique = False
            if checkUnique == True:
                p_arr.append(elem[0])
                p_arr.append(elem[1])
                unique_arr.append(p_arr)
                p_arr = []
            checkUnique = True
        # print(arr)
        # print(unique_arr)
        for p_elem in unique_arr:
            p_arr = []
            elem_count = 0
            for elem in arr:
                if str(p_elem[1]) == str(elem[1]):
                   elem_count+=1
            # print(str(p_elem), " : ", str(elem_count))
            p_arr.append(p_elem[0])
            p_arr.append(p_elem[1])
            p_arr.append(elem_count)
            res_arr.append(p_arr)
        print(res_arr)

        valWdg = 0
        self.tbl_StatTbl.setRowCount(0)
        for row in res_arr:
            self.tbl_StatTbl.insertRow(valWdg)

            item = QtWidgets.QTableWidgetItem(str(row[0]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tbl_StatTbl.setItem(valWdg, 0, item)

            item = QtWidgets.QTableWidgetItem(str(row[1]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tbl_StatTbl.setItem(valWdg, 1, item)

            item = QtWidgets.QTableWidgetItem(str(row[2]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.tbl_StatTbl.setItem(valWdg, 2, item)

            valWdg += 1





if __name__ == "__main__":
    uiStat = Ui_Stat()
    uiStat.show()
    sys.exit(app.exec_())
