# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PanelGlobalStat_v23.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
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
        self.tbl_StatTbl.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
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
        self.btn_Sett.setGeometry(QtCore.QRect(12, 24, 26, 26))
        self.btn_Sett.setObjectName("btn_Sett")
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
        self.tbl_ConnTbl.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "????????????????????"))
        self.tbl_StatTbl.setSortingEnabled(False)
        item = self.tbl_StatTbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "????????????????????????"))
        item = self.tbl_StatTbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "????????????"))
        item = self.tbl_StatTbl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "??????????, ????."))
        item = self.tbl_StatTbl.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "????????, ????."))
        item = self.tbl_StatTbl.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "??????????????????????"))
        self.btn_Sett.setText(_translate("Dialog", "#"))
        self.label.setText(_translate("Dialog", "?????????????? ??????????????????????????"))
        self.label_2.setText(_translate("Dialog", "?????????????????? ??????????????????"))
        self.tbl_ConnTbl.setSortingEnabled(False)
        item = self.tbl_ConnTbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "????????????????????????"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "????????????"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "???????????????? ??????????"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "?????????????? ????????????"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "?????????????????????? ????????????"))
        item = self.tbl_ConnTbl.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "?????????????? ??????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
