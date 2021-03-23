# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PanelJournal_v15.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import threading
import time
import sys
import GlobalValues
import pymysql

app = QtWidgets.QApplication(sys.argv)

class Ui_Journal(QDialog):

    StopAll = False


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(1062, 1004)
        self.setStyleSheet("")
        self.labelnameForm = QtWidgets.QLabel(self)
        self.labelnameForm.setGeometry(QtCore.QRect(440, -5, 171, 47))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelnameForm.setFont(font)
        self.labelnameForm.setStyleSheet("gridline-color: rgb(20, 18, 57);")
        self.labelnameForm.setObjectName("labelnameForm")
        self.lblIconJournal = QtWidgets.QLabel(self)
        self.lblIconJournal.setGeometry(QtCore.QRect(410, 8, 23, 23))
        self.lblIconJournal.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 0), stop:1 rgba(62, 62, 62, 0));\n"
            "image: url(C:/img/iconworkpanel1.png);")
        self.lblIconJournal.setText("")
        self.lblIconJournal.setObjectName("lblIconJournal")
        self.line1 = QtWidgets.QFrame(self)
        self.line1.setGeometry(QtCore.QRect(440, 26, 165, 16))
        self.line1.setStyleSheet("gridline-color: rgb(20, 18, 57);")
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.tblJournal = QtWidgets.QTableWidget(self)
        self.tblJournal.setGeometry(QtCore.QRect(11, 92, 1031, 901))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblJournal.sizePolicy().hasHeightForWidth())
        self.tblJournal.setSizePolicy(sizePolicy)
        self.tblJournal.setStyleSheet("QTableWidget {background-color: rgb(255,255,255);\n"
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
        self.tblJournal.setInputMethodHints(QtCore.Qt.ImhDate)
        self.tblJournal.setObjectName("tblJournal")
        self.tblJournal.setColumnCount(5)
        self.tblJournal.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tblJournal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblJournal.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblJournal.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblJournal.setHorizontalHeaderItem(4, item)
        self.tblJournal.horizontalHeader().setCascadingSectionResizes(False)
        self.tblJournal.horizontalHeader().setDefaultSectionSize(257)
        self.tblJournal.horizontalHeader().setMinimumSectionSize(31)
        self.tblJournal.horizontalHeader().setStretchLastSection(False)
        self.btnAccept = QtWidgets.QPushButton(self)
        self.btnAccept.setGeometry(QtCore.QRect(450, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAccept.setFont(font)
        self.btnAccept.setStyleSheet("QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                     "color: rgb(0,0,0);\n"
                                     "border-radius:3px;\n"
                                     "border:1px solid rgb(135,135,135);\n"
                                     "image: url(C:/img/iconsearch12grey.png);}\n"
                                     "\n"
                                     "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius:3px;\n"
                                     "border:1px solid rgb(63,63,63);\n"
                                     "image: url(C:/img/iconsearch12.png);}\n"
                                     "\n"
                                     "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius:3px;\n"
                                     "border:1px solid rgb(63,63,63);\n"
                                     "image: url(C:/img/iconsearch12.png);};")
        self.btnAccept.setIconSize(QtCore.QSize(25, 25))
        self.btnAccept.setObjectName("btnAccept")
        self.frmDateRng = QtWidgets.QFrame(self)
        self.frmDateRng.setGeometry(QtCore.QRect(10, 50, 431, 31))
        self.frmDateRng.setStyleSheet("color: rgb(0,0,0);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";")
        self.frmDateRng.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDateRng.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDateRng.setObjectName("frmDateRng")
        self.label_DateRng = QtWidgets.QLabel(self.frmDateRng)
        self.label_DateRng.setGeometry(QtCore.QRect(10, 5, 71, 21))
        self.label_DateRng.setStyleSheet("color: rgb(0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";")
        self.label_DateRng.setObjectName("label_DateRng")
        self.label_dateAt = QtWidgets.QLabel(self.frmDateRng)
        self.label_dateAt.setGeometry(QtCore.QRect(73, 5, 24, 21))
        self.label_dateAt.setStyleSheet("color: rgb(0,0,0);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.label_dateAt.setObjectName("label_dateAt")
        self.DTEditRngAt = QtWidgets.QDateTimeEdit(self.frmDateRng)
        self.DTEditRngAt.setGeometry(QtCore.QRect(100, 0, 141, 31))
        self.DTEditRngAt.setStyleSheet("background-color: rgb(227,227,227);\n"
                                       "color: black;\n"
                                       "border-radius: 3px;\n"
                                       "border: 1px solid rgb(135,135,135);\n"
                                       "font: 11pt \"MS Shell Dlg 2\";")
        self.DTEditRngAt.setObjectName("DTEditRngAt")
        self.DTEditRngTo = QtWidgets.QDateTimeEdit(self.frmDateRng)
        self.DTEditRngTo.setGeometry(QtCore.QRect(290, 0, 141, 31))
        self.DTEditRngTo.setStyleSheet("background-color: rgb(227,227,227);\n"
                                       "color: black;\n"
                                       "border-radius: 3px;\n"
                                       "border: 1px solid rgb(135,135,135);\n"
                                       "font: 11pt \"MS Shell Dlg 2\";")
        self.DTEditRngTo.setObjectName("DTEditRngTo")
        self.label_DateTo = QtWidgets.QLabel(self.frmDateRng)
        self.label_DateTo.setGeometry(QtCore.QRect(260, 5, 24, 21))
        self.label_DateTo.setStyleSheet("color: rgb(0,0,0);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.label_DateTo.setObjectName("label_DateTo")
        self.btnRefresh = QtWidgets.QPushButton(self)
        self.btnRefresh.setGeometry(QtCore.QRect(580, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setStyleSheet("QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                      "color: rgb(0,0,0);\n"
                                      "border-radius:3px;\n"
                                      "border:1px solid rgb(135,135,135);\n"
                                      "image: url(C:/img/iconrefreshgrey.png);}\n"
                                      "\n"
                                      "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius:3px;\n"
                                      "border:1px solid rgb(63,63,63);\n"
                                      "image: url(C:/img/iconrefresh.png);}\n"
                                      "\n"
                                      "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius:3px;\n"
                                      "border:1px solid rgb(63,63,63);\n"
                                      "image: url(C:/img/iconrefresh.png);};r")
        self.btnRefresh.setText("")
        self.btnRefresh.setIconSize(QtCore.QSize(25, 25))
        self.btnRefresh.setObjectName("btnRefresh")
        self.lblBack = QtWidgets.QLabel(self)
        self.lblBack.setGeometry(QtCore.QRect(0, 0, 1091, 1004))
        self.lblBack.setStyleSheet("")
        self.lblBack.setText("")
        self.lblBack.setObjectName("lblBack")
        self.verticalScrollBar = QtWidgets.QScrollBar(self)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1040, 115, 10, 878))
        self.verticalScrollBar.setStyleSheet("QScrollBar:vertical {\n"
                                      "border: 1px solid rgb(89,89,89);\n"
                                      " background: rgb(255,255,255);\n"
                                      "width:10px;\n"
                                      "margin: 0px 0px 0px 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0 rgb(142,187,208), stop: 0.5 rgb(142,187,208), stop:1 rgb(142,187,208));\n"
                                      "min-height: 10px;\n"
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
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.lblBack.raise_()
        self.labelnameForm.raise_()
        self.lblIconJournal.raise_()
        self.line1.raise_()
        self.tblJournal.raise_()
        self.btnAccept.raise_()
        self.btnRefresh.raise_()
        self.frmDateRng.raise_()
        self.verticalScrollBar.raise_()


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.tblJournal.viewport().installEventFilter(self)



        self.FirstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelnameForm.setText(_translate("Dialog", "Журнал событий"))
        self.tblJournal.setSortingEnabled(True)
        item = self.tblJournal.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Дата"))
        item = self.tblJournal.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Пользователь"))
        item = self.tblJournal.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Объект"))
        item = self.tblJournal.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Серийный номер"))
        item = self.tblJournal.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Событие"))
        self.btnAccept.setText(_translate("Dialog", "  Применить"))
        self.label_DateRng.setText(_translate("Dialog", "Период:"))
        self.label_dateAt.setText(_translate("Dialog", "От"))
        self.label_DateTo.setText(_translate("Dialog", "До"))

    def FirstSets(self):
        self.tblJournal.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblJournal.setColumnWidth(0,130)
        self.tblJournal.setColumnWidth(1,100)
        self.tblJournal.setColumnWidth(2,150)
        self.tblJournal.setColumnWidth(3,160)
        self.tblJournal.setColumnWidth(4,489)
        self.tblJournal.verticalHeader().hide()
        self.tblJournal.verticalScrollBar().hide()
        self.tblJournal.horizontalScrollBar().hide()
        self.tblJournal.verticalHeader().setDefaultSectionSize(5)
        self.tblJournal.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblJournal.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblJournal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblJournal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tblJournal.setAutoScrollMargin(5)
        self.tblJournal.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.verticalScrollBar.valueChanged.connect(self.vScrollSync)
        self.checkEventUpdate = True
        self.thScroll()

        self.UpdateHTable()
    def vScrollSync(self):
        self.tblJournal.verticalScrollBar().setValue(self.verticalScrollBar.value())

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.Wheel and source is self.tblJournal.viewport()):
            print("OSCROLL")
            self.verticalScrollBar.setValue(self.tblJournal.verticalScrollBar().value())
        return super(Ui_Journal, self).eventFilter(source, event)

    def UpdateHTable(self):
        sql_con = pymysql.connect(host=GlobalValues.SqlHostname,
                                  port=GlobalValues.SqlPort,
                                  user=GlobalValues.SqlUserName,
                                  passwd=GlobalValues.SqlPwd, db=GlobalValues.SqlDBName)
        with sql_con:
            cur = sql_con.cursor()
            if GlobalValues.checkTargetHystory == False:
                cur.execute(
                    "SELECT DateEvent, userName, TypeObj, SerialNum, EventObj FROM hystory")
            else:
                if GlobalValues.checkWichTblWasClicked == False:
                    print("111", str(GlobalValues.OTblCurrSerialNumObj))
                    cur.execute(
                        "SELECT DateEvent, userName, TypeObj, SerialNum, EventObj FROM hystory WHERE SerialNum Like '" + str(GlobalValues.OTblCurrSerialNumObj) + "'")
                else:
                    print("222", str(GlobalValues.KTblCurrSerialNumObj))
                    cur.execute(
                        "SELECT DateEvent, userName, TypeObj, SerialNum, EventObj FROM hystory WHERE SerialNum Like '" + str(
                            GlobalValues.KTblCurrSerialNumObj) + "'")
                GlobalValues.checkTargetHystory = False

            rows = cur.fetchall()
            # print(str(row))

            self.tblJournal.setRowCount(0)

            valWdg = 0

            countRow = 0
            for row in rows:
                countRow += 1

            for row in reversed(rows):
                countRow -= 1
                self.tblJournal.insertRow(valWdg)

                item = QtWidgets.QTableWidgetItem(str(row[0]))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tblJournal.setItem(valWdg, 0, item)

                if row[1] == None:
                    user = ''
                else:
                    user = row[1]

                item = QtWidgets.QTableWidgetItem(str(user))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tblJournal.setItem(valWdg, 1, item)

                item = QtWidgets.QTableWidgetItem(str(row[2]))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tblJournal.setItem(valWdg, 2, item)

                item = QtWidgets.QTableWidgetItem(str(row[3]))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tblJournal.setItem(valWdg, 3, item)

                item = QtWidgets.QTableWidgetItem(str(row[4]))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item.setToolTip("<font color=black>%s</font>" % str(row[4]).replace("\n", "<br/>"))
                self.tblJournal.setItem(valWdg, 4, item)



                valWdg += 1

    def closeEvent(self, event):
            self.StopAll = True
            event.accept()

    def thScroll(self):
        th =threading.Thread(target = self.thEvent)
        th.start()

    def thEvent(self):
        while True:
            if self.StopAll == True:
                print("ScrlThreadStop")
                break
            else:
                if self.checkEventUpdate == True:
                    th_scroll = threading.Thread(target=self.ChangeScroll)
                    th_scroll.start()
                time.sleep(0.2)

    def ChangeScroll(self):
        try:

            num_delta =2000

            start_time = round(time.time() * 100)
            while True:
                numRows = self.tblJournal.verticalScrollBar().maximum()
                delta = round(abs(time.time() * 100) - start_time)
                if numRows != 0:
                    time.sleep(0.2)
                    self.verticalScrollBar.setMaximum(self.tblJournal.verticalScrollBar().maximum())
                    break

                if delta > num_delta:
                    self.verticalScrollBar.setMaximum(self.tblJournal.verticalScrollBar().maximum())
                    break

                time.sleep(0.1)

        except:
            GlobalValues.checkVScrollOTblError = True




if __name__ == "__main__":
    uiJournal = Ui_Journal()
    uiJournal.show()
    sys.exit(app.exec_())
