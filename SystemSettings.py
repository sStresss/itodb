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
import pymysql
import sys
import GlobalValues
from PanelMesBox import Ui_MesBox

app = QtWidgets.QApplication(sys.argv)

class Ui_SysSettings(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("Dialog")
        self.resize(370, 326)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 369, 326))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 371, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.MySQL = QtWidgets.QWidget()
        self.MySQL.setObjectName("MySQL")
        self.btn_DBCheckConn = QtWidgets.QPushButton(self.MySQL)
        self.btn_DBCheckConn.setGeometry(QtCore.QRect(110, 245, 161, 28))
        self.btn_DBCheckConn.setObjectName("btn_DBCheckConn")
        self.label_7 = QtWidgets.QLabel(self.MySQL)
        self.label_7.setGeometry(QtCore.QRect(50, 87, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.MySQL)
        self.label_8.setGeometry(QtCore.QRect(50, 137, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.MySQL)
        self.label_9.setGeometry(QtCore.QRect(50, 187, 111, 16))
        self.label_9.setObjectName("label_9")
        self.le_DBIP = QtWidgets.QLineEdit(self.MySQL)
        self.le_DBIP.setGeometry(QtCore.QRect(50, 57, 271, 22))
        self.le_DBIP.setObjectName("le_DBIP")
        self.label_6 = QtWidgets.QLabel(self.MySQL)
        self.label_6.setGeometry(QtCore.QRect(50, 37, 111, 16))
        self.label_6.setObjectName("label_6")
        self.le_DBPort = QtWidgets.QLineEdit(self.MySQL)
        self.le_DBPort.setGeometry(QtCore.QRect(50, 107, 271, 22))
        self.le_DBPort.setObjectName("le_DBPort")
        self.le_DBPass = QtWidgets.QLineEdit(self.MySQL)
        self.le_DBPass.setGeometry(QtCore.QRect(50, 207, 271, 22))
        self.le_DBPass.setObjectName("le_DBPass")
        self.le_DBLogin = QtWidgets.QLineEdit(self.MySQL)
        self.le_DBLogin.setGeometry(QtCore.QRect(50, 157, 271, 22))
        self.le_DBLogin.setObjectName("le_DBLogin")
        self.tabWidget.addTab(self.MySQL, "")
        self.OSTUFF = QtWidgets.QWidget()
        self.OSTUFF.setObjectName("OSTUFF")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.OSTUFF)
        self.tabWidget_2.setGeometry(QtCore.QRect(-2, -3, 371, 311))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.OType = QtWidgets.QWidget()
        self.OType.setObjectName("OType")
        self.label_3 = QtWidgets.QLabel(self.OType)
        self.label_3.setGeometry(QtCore.QRect(5, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.OType)
        self.label_4.setGeometry(QtCore.QRect(5, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.OType)
        self.line_2.setGeometry(QtCore.QRect(-2, 132, 370, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_21 = QtWidgets.QLabel(self.OType)
        self.label_21.setGeometry(QtCore.QRect(70, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.le_NewOType = QtWidgets.QLineEdit(self.OType)
        self.le_NewOType.setGeometry(QtCore.QRect(70, 60, 231, 20))
        self.le_NewOType.setObjectName("le_NewOType")
        self.btn_AddNewOType = QtWidgets.QPushButton(self.OType)
        self.btn_AddNewOType.setGeometry(QtCore.QRect(130, 90, 111, 23))
        self.btn_AddNewOType.setObjectName("btn_AddNewOType")
        self.btn_DelOType = QtWidgets.QPushButton(self.OType)
        self.btn_DelOType.setGeometry(QtCore.QRect(130, 230, 111, 23))
        self.btn_DelOType.setObjectName("btn_DelOType")
        self.label_30 = QtWidgets.QLabel(self.OType)
        self.label_30.setGeometry(QtCore.QRect(70, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.cb_OType = QtWidgets.QComboBox(self.OType)
        self.cb_OType.setGeometry(QtCore.QRect(70, 200, 231, 22))
        self.cb_OType.setObjectName("cb_OType")
        self.tabWidget_2.addTab(self.OType, "")
        self.OModel = QtWidgets.QWidget()
        self.OModel.setObjectName("OModel")
        self.label_5 = QtWidgets.QLabel(self.OModel)
        self.label_5.setGeometry(QtCore.QRect(5, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.OModel)
        self.label_10.setGeometry(QtCore.QRect(5, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line_3 = QtWidgets.QFrame(self.OModel)
        self.line_3.setGeometry(QtCore.QRect(-2, 132, 370, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.btn_AddNewOModel = QtWidgets.QPushButton(self.OModel)
        self.btn_AddNewOModel.setGeometry(QtCore.QRect(130, 90, 111, 23))
        self.btn_AddNewOModel.setObjectName("btn_AddNewOModel")
        self.label_23 = QtWidgets.QLabel(self.OModel)
        self.label_23.setGeometry(QtCore.QRect(70, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.le_NewOModel = QtWidgets.QLineEdit(self.OModel)
        self.le_NewOModel.setGeometry(QtCore.QRect(70, 60, 231, 20))
        self.le_NewOModel.setObjectName("le_NewOModel")
        self.btn_DelOModel = QtWidgets.QPushButton(self.OModel)
        self.btn_DelOModel.setGeometry(QtCore.QRect(130, 230, 111, 23))
        self.btn_DelOModel.setObjectName("btn_DelOModel")
        self.label_31 = QtWidgets.QLabel(self.OModel)
        self.label_31.setGeometry(QtCore.QRect(70, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.cb_OModel = QtWidgets.QComboBox(self.OModel)
        self.cb_OModel.setGeometry(QtCore.QRect(70, 200, 231, 22))
        self.cb_OModel.setObjectName("cb_OModel")
        self.tabWidget_2.addTab(self.OModel, "")
        self.OMaker = QtWidgets.QWidget()
        self.OMaker.setObjectName("OMaker")
        self.label = QtWidgets.QLabel(self.OMaker)
        self.label.setGeometry(QtCore.QRect(5, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.OMaker)
        self.line.setGeometry(QtCore.QRect(-2, 132, 370, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.OMaker)
        self.label_2.setGeometry(QtCore.QRect(5, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_AddNewOMaker = QtWidgets.QPushButton(self.OMaker)
        self.btn_AddNewOMaker.setGeometry(QtCore.QRect(130, 90, 111, 23))
        self.btn_AddNewOMaker.setObjectName("btn_AddNewOMaker")
        self.label_24 = QtWidgets.QLabel(self.OMaker)
        self.label_24.setGeometry(QtCore.QRect(70, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.le_NewOMaker = QtWidgets.QLineEdit(self.OMaker)
        self.le_NewOMaker.setGeometry(QtCore.QRect(70, 60, 231, 20))
        self.le_NewOMaker.setObjectName("le_NewOMaker")
        self.cb_OMaker = QtWidgets.QComboBox(self.OMaker)
        self.cb_OMaker.setGeometry(QtCore.QRect(70, 200, 231, 22))
        self.cb_OMaker.setObjectName("cb_OMaker")
        self.label_32 = QtWidgets.QLabel(self.OMaker)
        self.label_32.setGeometry(QtCore.QRect(70, 180, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.btn_DelOMaker = QtWidgets.QPushButton(self.OMaker)
        self.btn_DelOMaker.setGeometry(QtCore.QRect(130, 230, 111, 23))
        self.btn_DelOMaker.setObjectName("btn_DelOMaker")
        self.tabWidget_2.addTab(self.OMaker, "")
        self.ODistributor = QtWidgets.QWidget()
        self.ODistributor.setObjectName("ODistributor")
        self.label_11 = QtWidgets.QLabel(self.ODistributor)
        self.label_11.setGeometry(QtCore.QRect(5, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.ODistributor)
        self.label_12.setGeometry(QtCore.QRect(5, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.line_4 = QtWidgets.QFrame(self.ODistributor)
        self.line_4.setGeometry(QtCore.QRect(-2, 132, 370, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.btn_AddNewODistributor = QtWidgets.QPushButton(self.ODistributor)
        self.btn_AddNewODistributor.setGeometry(QtCore.QRect(130, 90, 111, 23))
        self.btn_AddNewODistributor.setObjectName("btn_AddNewODistributor")
        self.label_25 = QtWidgets.QLabel(self.ODistributor)
        self.label_25.setGeometry(QtCore.QRect(70, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.le_NewODistributor = QtWidgets.QLineEdit(self.ODistributor)
        self.le_NewODistributor.setGeometry(QtCore.QRect(70, 60, 231, 20))
        self.le_NewODistributor.setObjectName("le_NewODistributor")
        self.cb_ODistributor = QtWidgets.QComboBox(self.ODistributor)
        self.cb_ODistributor.setGeometry(QtCore.QRect(70, 200, 231, 22))
        self.cb_ODistributor.setObjectName("cb_ODistributor")
        self.label_29 = QtWidgets.QLabel(self.ODistributor)
        self.label_29.setGeometry(QtCore.QRect(70, 180, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.btn_DelODistributor = QtWidgets.QPushButton(self.ODistributor)
        self.btn_DelODistributor.setGeometry(QtCore.QRect(130, 230, 111, 23))
        self.btn_DelODistributor.setObjectName("btn_DelODistributor")
        self.tabWidget_2.addTab(self.ODistributor, "")
        self.tabWidget.addTab(self.OSTUFF, "")
        self.KSTUFF = QtWidgets.QWidget()
        self.KSTUFF.setObjectName("KSTUFF")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.KSTUFF)
        self.tabWidget_3.setGeometry(QtCore.QRect(-2, -3, 371, 311))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.KType = QtWidgets.QWidget()
        self.KType.setObjectName("KType")
        self.label_13 = QtWidgets.QLabel(self.KType)
        self.label_13.setGeometry(QtCore.QRect(5, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.KType)
        self.label_14.setGeometry(QtCore.QRect(5, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.line_5 = QtWidgets.QFrame(self.KType)
        self.line_5.setGeometry(QtCore.QRect(-2, 132, 370, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_22 = QtWidgets.QLabel(self.KType)
        self.label_22.setGeometry(QtCore.QRect(70, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.le_NewKType = QtWidgets.QLineEdit(self.KType)
        self.le_NewKType.setGeometry(QtCore.QRect(70, 60, 231, 20))
        self.le_NewKType.setObjectName("le_NewKType")
        self.btn_AddNewKType = QtWidgets.QPushButton(self.KType)
        self.btn_AddNewKType.setGeometry(QtCore.QRect(130, 90, 111, 23))
        self.btn_AddNewKType.setObjectName("btn_AddNewKType")
        self.cb_KType = QtWidgets.QComboBox(self.KType)
        self.cb_KType.setGeometry(QtCore.QRect(70, 200, 231, 22))
        self.cb_KType.setObjectName("cb_KType")
        self.label_33 = QtWidgets.QLabel(self.KType)
        self.label_33.setGeometry(QtCore.QRect(70, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.btn_DelKType = QtWidgets.QPushButton(self.KType)
        self.btn_DelKType.setGeometry(QtCore.QRect(130, 230, 111, 23))
        self.btn_DelKType.setObjectName("btn_DelKType")
        self.tabWidget_3.addTab(self.KType, "")
        self.KModel = QtWidgets.QWidget()
        self.KModel.setObjectName("KModel")
        self.label_15 = QtWidgets.QLabel(self.KModel)
        self.label_15.setGeometry(QtCore.QRect(5, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.KModel)
        self.label_16.setGeometry(QtCore.QRect(5, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.line_6 = QtWidgets.QFrame(self.KModel)
        self.line_6.setGeometry(QtCore.QRect(-2, 132, 370, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.btn_AddNewKModel = QtWidgets.QPushButton(self.KModel)
        self.btn_AddNewKModel.setGeometry(QtCore.QRect(130, 90, 111, 23))
        self.btn_AddNewKModel.setObjectName("btn_AddNewKModel")
        self.label_26 = QtWidgets.QLabel(self.KModel)
        self.label_26.setGeometry(QtCore.QRect(70, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.le_NewKModel = QtWidgets.QLineEdit(self.KModel)
        self.le_NewKModel.setGeometry(QtCore.QRect(70, 60, 231, 20))
        self.le_NewKModel.setObjectName("le_NewKModel")
        self.cb_KModel = QtWidgets.QComboBox(self.KModel)
        self.cb_KModel.setGeometry(QtCore.QRect(70, 200, 231, 22))
        self.cb_KModel.setObjectName("cb_KModel")
        self.label_34 = QtWidgets.QLabel(self.KModel)
        self.label_34.setGeometry(QtCore.QRect(70, 180, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.btn_DelKModel = QtWidgets.QPushButton(self.KModel)
        self.btn_DelKModel.setGeometry(QtCore.QRect(130, 230, 111, 23))
        self.btn_DelKModel.setObjectName("btn_DelKModel")
        self.tabWidget_3.addTab(self.KModel, "")
        self.KMaker = QtWidgets.QWidget()
        self.KMaker.setObjectName("KMaker")
        self.label_17 = QtWidgets.QLabel(self.KMaker)
        self.label_17.setGeometry(QtCore.QRect(5, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.KMaker)
        self.label_18.setGeometry(QtCore.QRect(5, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.line_7 = QtWidgets.QFrame(self.KMaker)
        self.line_7.setGeometry(QtCore.QRect(-2, 132, 370, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.btn_AddNewKMaker = QtWidgets.QPushButton(self.KMaker)
        self.btn_AddNewKMaker.setGeometry(QtCore.QRect(130, 90, 111, 23))
        self.btn_AddNewKMaker.setObjectName("btn_AddNewKMaker")
        self.label_27 = QtWidgets.QLabel(self.KMaker)
        self.label_27.setGeometry(QtCore.QRect(70, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.le_NewKMaker = QtWidgets.QLineEdit(self.KMaker)
        self.le_NewKMaker.setGeometry(QtCore.QRect(70, 60, 231, 20))
        self.le_NewKMaker.setObjectName("le_NewKMaker")
        self.cb_KMaker = QtWidgets.QComboBox(self.KMaker)
        self.cb_KMaker.setGeometry(QtCore.QRect(70, 200, 231, 22))
        self.cb_KMaker.setObjectName("cb_KMaker")
        self.label_35 = QtWidgets.QLabel(self.KMaker)
        self.label_35.setGeometry(QtCore.QRect(70, 180, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.btn_DelKMaker = QtWidgets.QPushButton(self.KMaker)
        self.btn_DelKMaker.setGeometry(QtCore.QRect(130, 230, 111, 23))
        self.btn_DelKMaker.setObjectName("btn_DelKMaker")
        self.tabWidget_3.addTab(self.KMaker, "")
        self.KDistributor = QtWidgets.QWidget()
        self.KDistributor.setObjectName("KDistributor")
        self.label_19 = QtWidgets.QLabel(self.KDistributor)
        self.label_19.setGeometry(QtCore.QRect(5, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.KDistributor)
        self.label_20.setGeometry(QtCore.QRect(5, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.line_8 = QtWidgets.QFrame(self.KDistributor)
        self.line_8.setGeometry(QtCore.QRect(-2, 132, 370, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.btn_AddNewKDistributor = QtWidgets.QPushButton(self.KDistributor)
        self.btn_AddNewKDistributor.setGeometry(QtCore.QRect(130, 90, 111, 23))
        self.btn_AddNewKDistributor.setObjectName("btn_AddNewKDistributor")
        self.label_28 = QtWidgets.QLabel(self.KDistributor)
        self.label_28.setGeometry(QtCore.QRect(70, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.le_NewKDistributor = QtWidgets.QLineEdit(self.KDistributor)
        self.le_NewKDistributor.setGeometry(QtCore.QRect(70, 60, 231, 20))
        self.le_NewKDistributor.setObjectName("le_NewKDistributor")
        self.cb_KDistributor = QtWidgets.QComboBox(self.KDistributor)
        self.cb_KDistributor.setGeometry(QtCore.QRect(70, 200, 231, 22))
        self.cb_KDistributor.setObjectName("cb_KDistributor")
        self.label_36 = QtWidgets.QLabel(self.KDistributor)
        self.label_36.setGeometry(QtCore.QRect(70, 180, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.btn_DelKDistributor = QtWidgets.QPushButton(self.KDistributor)
        self.btn_DelKDistributor.setGeometry(QtCore.QRect(130, 230, 111, 23))
        self.btn_DelKDistributor.setObjectName("btn_DelKDistributor")
        self.tabWidget_3.addTab(self.KDistributor, "")
        self.tabWidget.addTab(self.KSTUFF, "")
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(3)


        self.FirstSets()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Настройки системы"))
        self.btn_DBCheckConn.setText(_translate("Dialog", "Проверка соединения"))
        self.label_7.setText(_translate("Dialog", "Порт"))
        self.label_8.setText(_translate("Dialog", "Логин:"))
        self.label_9.setText(_translate("Dialog", "Пароль:"))
        self.label_6.setText(_translate("Dialog", "IP адрес БД"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MySQL), _translate("Dialog", "My SQL"))
        self.label_3.setText(_translate("Dialog", "Добавление"))
        self.label_4.setText(_translate("Dialog", "Удаление"))
        self.label_21.setText(_translate("Dialog", "Новый тип:"))
        self.btn_AddNewOType.setText(_translate("Dialog", "Добавить"))
        self.btn_DelOType.setText(_translate("Dialog", "Удалить"))
        self.label_30.setText(_translate("Dialog", "Список существующих типов:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.OType), _translate("Dialog", "Тип"))
        self.label_5.setText(_translate("Dialog", "Добавление"))
        self.label_10.setText(_translate("Dialog", "Удаление"))
        self.btn_AddNewOModel.setText(_translate("Dialog", "Добавить"))
        self.label_23.setText(_translate("Dialog", "Новая модель:"))
        self.btn_DelOModel.setText(_translate("Dialog", "Удалить"))
        self.label_31.setText(_translate("Dialog", "Список существующих моделей:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.OModel), _translate("Dialog", "Модель"))
        self.label.setText(_translate("Dialog", "Добавление"))
        self.label_2.setText(_translate("Dialog", "Удаление"))
        self.btn_AddNewOMaker.setText(_translate("Dialog", "Добавить"))
        self.label_24.setText(_translate("Dialog", "Новый производитель:"))
        self.label_32.setText(_translate("Dialog", "Список существующих производителей:"))
        self.btn_DelOMaker.setText(_translate("Dialog", "Удалить"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.OMaker), _translate("Dialog", "Производитель"))
        self.label_11.setText(_translate("Dialog", "Добавление"))
        self.label_12.setText(_translate("Dialog", "Удаление"))
        self.btn_AddNewODistributor.setText(_translate("Dialog", "Добавить"))
        self.label_25.setText(_translate("Dialog", "Новый поставщик:"))
        self.label_29.setText(_translate("Dialog", "Список существующих поставщиков:"))
        self.btn_DelODistributor.setText(_translate("Dialog", "Удалить"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.ODistributor), _translate("Dialog", "Поставщик"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OSTUFF), _translate("Dialog", "Оборудование"))
        self.label_13.setText(_translate("Dialog", "Добавление"))
        self.label_14.setText(_translate("Dialog", "Удаление"))
        self.label_22.setText(_translate("Dialog", "Новый тип:"))
        self.btn_AddNewKType.setText(_translate("Dialog", "Добавить"))
        self.label_33.setText(_translate("Dialog", "Список существующих типов:"))
        self.btn_DelKType.setText(_translate("Dialog", "Удалить"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.KType), _translate("Dialog", "Тип"))
        self.label_15.setText(_translate("Dialog", "Добавление"))
        self.label_16.setText(_translate("Dialog", "Удаление"))
        self.btn_AddNewKModel.setText(_translate("Dialog", "Добавить"))
        self.label_26.setText(_translate("Dialog", "Новая модель:"))
        self.label_34.setText(_translate("Dialog", "Список существующих моделей:"))
        self.btn_DelKModel.setText(_translate("Dialog", "Удалить"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.KModel), _translate("Dialog", "Модель"))
        self.label_17.setText(_translate("Dialog", "Добавление"))
        self.label_18.setText(_translate("Dialog", "Удаление"))
        self.btn_AddNewKMaker.setText(_translate("Dialog", "Добавить"))
        self.label_27.setText(_translate("Dialog", "Новый производитель:"))
        self.label_35.setText(_translate("Dialog", "Список существующих производителей:"))
        self.btn_DelKMaker.setText(_translate("Dialog", "Удалить"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.KMaker), _translate("Dialog", "Производитель"))
        self.label_19.setText(_translate("Dialog", "Добавление"))
        self.label_20.setText(_translate("Dialog", "Удаление"))
        self.btn_AddNewKDistributor.setText(_translate("Dialog", "Добавить"))
        self.label_28.setText(_translate("Dialog", "Новый поставщик:"))
        self.label_36.setText(_translate("Dialog", "Список существующих поставщиков:"))
        self.btn_DelKDistributor.setText(_translate("Dialog", "Удалить"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.KDistributor), _translate("Dialog", "Поставщик"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.KSTUFF), _translate("Dialog", "Комплектующие"))

    def FirstSets(self):
        #автоподхват паслогина
        self.le_DBPass.setEchoMode(QLineEdit.Password)
        self.le_DBIP.setText(str(GlobalValues.SqlHostname))
        self.le_DBPort.setText(str(GlobalValues.SqlPort))
        self.le_DBLogin.setText(str(GlobalValues.SqlUserName))
        self.le_DBPass.setText(str(GlobalValues.SqlPwd))

        self.btn_DBCheckConn.clicked.connect(self.sqlConnectCheck)
        self.btn_AddNewOType.clicked.connect(self.AddNewOType)
        self.btn_DelOType.clicked.connect(self.DelOType)
        self.btn_AddNewKType.clicked.connect(self.AddNewKType)
        self.btn_DelKType.clicked.connect(self.DelKType)
        self.btn_AddNewOModel.clicked.connect(self.AddNewOModel)
        self.btn_DelOModel.clicked.connect(self.DelOModel)
        self.btn_AddNewKModel.clicked.connect(self.AddNewKModel)
        self.btn_DelKModel.clicked.connect(self.DelKModel)
        self.btn_AddNewOMaker.clicked.connect(self.AddNewOMaker)
        self.btn_DelOMaker.clicked.connect(self.DelOMaker)
        self.btn_AddNewKMaker.clicked.connect(self.AddNewKMaker)
        self.btn_DelKMaker.clicked.connect(self.DelKMaker)
        self.btn_AddNewODistributor.clicked.connect(self.AddNewODistributor)
        self.btn_DelODistributor.clicked.connect(self.DelODistributor)
        self.btn_AddNewKDistributor.clicked.connect(self.AddNewKDistributor)
        self.btn_DelKDistributor.clicked.connect(self.DelKDistributor)
        if GlobalValues.checkFirstConn == True:
            self.MakeOTypeList()
            self.MakeKTypeList()
            self.MakeOModelList()
            self.MakeKModelList()
            self.MakeOMakerList()
            self.MakeKMakerList()
            self.MakeODistributorList()
            self.MakeKDistributorList()

    def sqlConnectCheck(self):
        try:
            locHostName = str(self.le_DBIP.text())
            locPort = int(self.le_DBPort.text())
            locUserName = str(self.le_DBLogin.text())
            locPwd = str(self.le_DBPass.text())
            locDBName = str(GlobalValues.SqlDBName)

            #зпись паслогов в файл для подхвата при первом запуске
            passlog = open("C:\itoDB\sqlpasslog.txt", "w")
            passlog.write(str(locHostName) + "\n")
            passlog.write(str(locPort) + "\n")
            passlog.write(str(locUserName) + "\n")
            passlog.write(str(locPwd) + "\n")
            passlog.close()

            GlobalValues.SqlHostname = locHostName
            GlobalValues.SqlPort = locPort
            GlobalValues.SqlUserName = locUserName
            GlobalValues.SqlPwd = locPwd

            con = pymysql.connect(host=locHostName,
                                  port=locPort,
                                  user=locUserName,
                                  passwd=locPwd,
                                  db=locDBName)
            with con:
                cur = con.cursor()
                cur.execute("SELECT VERSION()")

                version = cur.fetchone()

                if str(format(version[0])) != '':
                    GlobalValues.MesText = 'Соединение установлено!'
                    GlobalValues.SqlConCheck = True
                    GlobalValues.SqlFirstConnectUpdate = True
                    GlobalValues.treeUpdate = True





                print("Database version: {}".format(version[0]))
            # con.close()
        except:
            GlobalValues.MesText = 'Соединение не установлено'
            GlobalValues.SqlConCheck = False

        self.openPanelMexBox()

    def openPanelMexBox(self):
        self.uiMesBox = Ui_MesBox()
        self.uiMesBox.exec_()

    def MakeOTypeList(self):
        try:
            self.cb_OType.clear()
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                cur.execute("SELECT ID, OTypeName FROM otypetbl")
                OType_rows = cur.fetchall()
                for row in OType_rows:
                    self.cb_OType.addItem(str(row[1]))
        except:
            print("Err OTypes")
    def MakeKTypeList(self):
        try:
            self.cb_KType.clear()
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
                    self.cb_KType.addItem(str(row[1]))
        except:
            print("Err KType")

    def MakeOModelList(self):
        try:
            self.cb_OModel.clear()
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                cur.execute("SELECT ID, OModelName FROM omodeltbl")
                OModel_rows = cur.fetchall()
                for row in OModel_rows:
                    self.cb_OModel.addItem(str(row[1]))
        except:
            print("Err OMode")

    def MakeKModelList(self):
        try:
            self.cb_KModel.clear()
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
                    self.cb_KModel.addItem(str(row[1]))
        except:
            print("Err KMode")

    def MakeOMakerList(self):
        try:
            self.cb_OMaker.clear()
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                cur.execute("SELECT ID, OMakerName FROM omakertbl")
                OMaker_rows = cur.fetchall()
                for row in OMaker_rows:
                    self.cb_OMaker.addItem(str(row[1]))
        except:
            print("Err OMaker")

    def MakeKMakerList(self):
        try:
            self.cb_KMaker.clear()
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
                    self.cb_KMaker.addItem(str(row[1]))
        except:
            print("Err KMaker")

    def MakeODistributorList(self):
        try:
            self.cb_ODistributor.clear()
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                cur.execute("SELECT ID, ODistributorName FROM odistributortbl")
                ODistributor_rows = cur.fetchall()
                for row in ODistributor_rows:
                    self.cb_ODistributor.addItem(str(row[1]))
        except:
            print("Err ODist")

    def MakeKDistributorList(self):
        try:
            self.cb_KDistributor.clear()
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
                    self.cb_KDistributor.addItem(str(row[1]))
        except:
            print("Err LDist")

    def AddNewOType(self):
        checkName = False
        OTypeName = self.le_NewOType.text()
        GlobalValues.MesText = "Вы уверены?"
        self.openPanelMexBox()

        if GlobalValues.MesResult == True:

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ID, OTypeName FROM otypetbl")
                OTypeList_rows = cur.fetchall()

                for row in OTypeList_rows:
                    if str(OTypeName) == str(row[1]):
                        checkName = True

                OID = 1
                if (len(OTypeList_rows) != 0):
                    for row in reversed(OTypeList_rows):
                        try:
                            OID = str(int(row[0]) + 1)
                        except:
                            print("OID Error!!!")
                        break
                if str(OTypeName) != "":
                    if checkName == False:
                        query = ("INSERT INTO otypetbl (ID, OTypeName) VALUES ( %s, %s)")
                        cur.execute(query, (OID, OTypeName))
                        con.commit()
                    else:
                        GlobalValues.MesText = "Ошибка! Введенное имя уже существует!"
                        self.openPanelMexBox()
                else:
                    GlobalValues.MesText = "Ошибка! Заполните текстовое поле!"
                    self.openPanelMexBox()
                self.MakeOTypeList()


            cur.close()

    def DelOType(self):
        GlobalValues.MesResult = "Вы уверены?"
        self.openPanelMexBox()
        if GlobalValues.MesResult == True:
            OTypeName = str(self.cb_OType.currentText())
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                query = ("DELETE FROM otypetbl where OTypeName = (%s)")
                cur.execute(query, (OTypeName))

                con.commit()
                self.MakeOTypeList()
            # con.close()

    def AddNewKType(self):
        checkName = False
        KTypeName = self.le_NewKType.text()
        GlobalValues.MesText = "Вы уверены?"
        self.openPanelMexBox()

        if GlobalValues.MesResult == True:

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ID, KTypeName FROM ktypetbl")
                KTypeList_rows = cur.fetchall()

                for row in KTypeList_rows:
                    if str(KTypeName) == str(row[1]):
                        checkName = True

                KID = 1
                if (len(KTypeList_rows) != 0):
                    for row in reversed(KTypeList_rows):
                        try:
                            KID = str(int(row[0]) + 1)
                        except:
                            print("OID Error!!!")
                        break
                if str(KTypeName) != "":
                    if checkName == False:
                        query = ("INSERT INTO ktypetbl (ID, KTypeName) VALUES ( %s, %s)")
                        cur.execute(query, (KID, KTypeName))
                        con.commit()
                    else:
                        GlobalValues.MesText = "Ошибка! Введенное имя уже существует!"
                        self.openPanelMexBox()
                else:
                    GlobalValues.MesText = "Ошибка! Заполните текстовое поле!"
                    self.openPanelMexBox()
                self.MakeKTypeList()


            cur.close()

    def DelKType(self):
        GlobalValues.MesResult = "Вы уверены?"
        self.openPanelMexBox()
        if GlobalValues.MesResult == True:
            KTypeName = str(self.cb_KType.currentText())
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                query = ("DELETE FROM ktypetbl where KTypeName = (%s)")
                cur.execute(query, (KTypeName))

                con.commit()
                self.MakeKTypeList()
            # con.close()

    def AddNewOModel(self):
        checkName = False
        OModelName = self.le_NewOModel.text()
        GlobalValues.MesText = "Вы уверены?"
        self.openPanelMexBox()

        if GlobalValues.MesResult == True:

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ID, OModelName FROM omodeltbl")
                OModelList_rows = cur.fetchall()

                for row in OModelList_rows:
                    if str(OModelName) == str(row[1]):
                        checkName = True

                OID = 1
                if (len(OModelList_rows) != 0):
                    for row in reversed(OModelList_rows):
                        try:
                            OID = str(int(row[0]) + 1)
                        except:
                            print("OID Error!!!")
                        break
                if str(OModelName) != "":
                    if checkName == False:
                        query = ("INSERT INTO omodeltbl (ID, OModelName) VALUES ( %s, %s)")
                        cur.execute(query, (OID, OModelName))
                        con.commit()
                    else:
                        GlobalValues.MesText = "Ошибка! Введенное имя уже существует!"
                        self.openPanelMexBox()
                else:
                    GlobalValues.MesText = "Ошибка! Заполните текстовое поле!"
                    self.openPanelMexBox()
                self.MakeOModelList()


            cur.close()

    def DelOModel(self):
        GlobalValues.MesResult = "Вы уверены?"
        self.openPanelMexBox()
        if GlobalValues.MesResult == True:
            OModelName = str(self.cb_OModel.currentText())
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                query = ("DELETE FROM omodeltbl where OModelName = (%s)")
                cur.execute(query, (OModelName))

                con.commit()
                self.MakeOModelList()
            # con.close()

    def AddNewKModel(self):
        checkName = False
        KModelName = self.le_NewKModel.text()
        GlobalValues.MesText = "Вы уверены?"
        self.openPanelMexBox()

        if GlobalValues.MesResult == True:

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ID, KModelName FROM kmodeltbl")
                KModelList_rows = cur.fetchall()

                for row in KModelList_rows:
                    if str(KModelName) == str(row[1]):
                        checkName = True

                KID = 1
                if (len(KModelList_rows) != 0):
                    for row in reversed(KModelList_rows):
                        try:
                            KID = str(int(row[0]) + 1)
                        except:
                            print("OID Error!!!")
                        break
                if str(KModelName) != "":
                    if checkName == False:
                        query = ("INSERT INTO kmodeltbl (ID, KModelName) VALUES ( %s, %s)")
                        cur.execute(query, (KID, KModelName))
                        con.commit()
                    else:
                        GlobalValues.MesText = "Ошибка! Введенное имя уже существует!"
                        self.openPanelMexBox()
                else:
                    GlobalValues.MesText = "Ошибка! Заполните текстовое поле!"
                    self.openPanelMexBox()
                self.MakeKModelList()


            cur.close()

    def DelKModel(self):
        GlobalValues.MesResult = "Вы уверены?"
        self.openPanelMexBox()
        if GlobalValues.MesResult == True:
            KModelName = str(self.cb_KModel.currentText())
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                query = ("DELETE FROM kmodeltbl where KModelName = (%s)")
                cur.execute(query, (KModelName))

                con.commit()
                self.MakeKModelList()
            # con.close()

    def AddNewOMaker(self):
        checkName = False
        OMakerName = self.le_NewOMaker.text()
        GlobalValues.MesText = "Вы уверены?"
        self.openPanelMexBox()

        if GlobalValues.MesResult == True:

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ID, OMakerName FROM omakertbl")
                OMakerList_rows = cur.fetchall()

                for row in OMakerList_rows:
                    if str(OMakerName) == str(row[1]):
                        checkName = True

                OID = 1
                if (len(OMakerList_rows) != 0):
                    for row in reversed(OMakerList_rows):
                        try:
                            OID = str(int(row[0]) + 1)
                        except:
                            print("OID Error!!!")
                        break
                if str(OMakerName) != "":
                    if checkName == False:
                        query = ("INSERT INTO omakertbl (ID, OMakerName) VALUES ( %s, %s)")
                        cur.execute(query, (OID, OMakerName))
                        con.commit()
                    else:
                        GlobalValues.MesText = "Ошибка! Введенное имя уже существует!"
                        self.openPanelMexBox()
                else:
                    GlobalValues.MesText = "Ошибка! Заполните текстовое поле!"
                    self.openPanelMexBox()
                self.MakeOMakerList()


            cur.close()

    def DelOMaker(self):
        GlobalValues.MesResult = "Вы уверены?"
        self.openPanelMexBox()
        if GlobalValues.MesResult == True:
            OMakerName = str(self.cb_OMaker.currentText())
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                query = ("DELETE FROM omakertbl where OMakerName = (%s)")
                cur.execute(query, (OMakerName))

                con.commit()
                self.MakeOMakerList()
            # con.close()

    def AddNewKMaker(self):
        checkName = False
        KMakerName = self.le_NewKMaker.text()
        GlobalValues.MesText = "Вы уверены?"
        self.openPanelMexBox()

        if GlobalValues.MesResult == True:

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ID, KMakerName FROM kmakertbl")
                KMakerList_rows = cur.fetchall()

                for row in KMakerList_rows:
                    if str(KMakerName) == str(row[1]):
                        checkName = True

                KID = 1
                if (len(KMakerList_rows) != 0):
                    for row in reversed(KMakerList_rows):
                        try:
                            KID = str(int(row[0]) + 1)
                        except:
                            print("OID Error!!!")
                        break
                if str(KMakerName) != "":
                    if checkName == False:
                        query = ("INSERT INTO kmakertbl (ID, KMakerName) VALUES ( %s, %s)")
                        cur.execute(query, (KID, KMakerName))
                        con.commit()
                    else:
                        GlobalValues.MesText = "Ошибка! Введенное имя уже существует!"
                        self.openPanelMexBox()
                else:
                    GlobalValues.MesText = "Ошибка! Заполните текстовое поле!"
                    self.openPanelMexBox()
                self.MakeKMakerList()


            cur.close()

    def DelKMaker(self):
        GlobalValues.MesResult = "Вы уверены?"
        self.openPanelMexBox()
        if GlobalValues.MesResult == True:
            KMakerName = str(self.cb_KMaker.currentText())
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                query = ("DELETE FROM kmakertbl where KMakerName = (%s)")
                cur.execute(query, (KMakerName))

                con.commit()
                self.MakeKMakerList()
            # con.close()

    def AddNewODistributor(self):
        checkName = False
        ODistributorName = self.le_NewODistributor.text()
        GlobalValues.MesText = "Вы уверены?"
        self.openPanelMexBox()

        if GlobalValues.MesResult == True:

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ID, ODistributorName FROM odistributortbl")
                ODistributorList_rows = cur.fetchall()

                for row in ODistributorList_rows:
                    if str(ODistributorName) == str(row[1]):
                        checkName = True

                OID = 1
                if (len(ODistributorList_rows) != 0):
                    for row in reversed(ODistributorList_rows):
                        try:
                            OID = str(int(row[0]) + 1)
                        except:
                            print("OID Error!!!")
                        break
                if str(ODistributorName) != "":
                    if checkName == False:
                        query = ("INSERT INTO odistributortbl (ID, ODistributorName) VALUES ( %s, %s)")
                        cur.execute(query, (OID, ODistributorName))
                        con.commit()
                    else:
                        GlobalValues.MesText = "Ошибка! Введенное имя уже существует!"
                        self.openPanelMexBox()
                else:
                    GlobalValues.MesText = "Ошибка! Заполните текстовое поле!"
                    self.openPanelMexBox()
                self.MakeODistributorList()


            cur.close()

    def DelODistributor(self):
        GlobalValues.MesResult = "Вы уверены?"
        self.openPanelMexBox()
        if GlobalValues.MesResult == True:
            ODistributorName = str(self.cb_ODistributor.currentText())
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                query = ("DELETE FROM odistributortbl where ODistributorName = (%s)")
                cur.execute(query, (ODistributorName))

                con.commit()
                self.MakeODistributorList()
            # con.close()

    def AddNewKDistributor(self):
        checkName = False
        KDistributorName = self.le_NewKDistributor.text()
        GlobalValues.MesText = "Вы уверены?"
        self.openPanelMexBox()

        if GlobalValues.MesResult == True:

            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()

                cur.execute("SELECT ID, KDistributorName FROM kdistributortbl")
                KDistributorList_rows = cur.fetchall()

                for row in KDistributorList_rows:
                    if str(KDistributorName) == str(row[1]):
                        checkName = True

                KID = 1
                if (len(KDistributorList_rows) != 0):
                    for row in reversed(KDistributorList_rows):
                        try:
                            KID = str(int(row[0]) + 1)
                        except:
                            print("OID Error!!!")
                        break
                if str(KDistributorName) != "":
                    if checkName == False:
                        query = ("INSERT INTO kdistributortbl (ID, KDistributorName) VALUES ( %s, %s)")
                        cur.execute(query, (KID, KDistributorName))
                        con.commit()
                    else:
                        GlobalValues.MesText = "Ошибка! Введенное имя уже существует!"
                        self.openPanelMexBox()
                else:
                    GlobalValues.MesText = "Ошибка! Заполните текстовое поле!"
                    self.openPanelMexBox()
                self.MakeKDistributorList()


            cur.close()

    def DelKDistributor(self):
        GlobalValues.MesResult = "Вы уверены?"
        self.openPanelMexBox()
        if GlobalValues.MesResult == True:
            KDistributorName = str(self.cb_KDistributor.currentText())
            con = pymysql.connect(host=str(GlobalValues.SqlHostname),
                                  port=int(GlobalValues.SqlPort),
                                  user=str(GlobalValues.SqlUserName),
                                  passwd=str(GlobalValues.SqlPwd),
                                  db=str(GlobalValues.SqlDBName))
            with con:
                cur = con.cursor()
                query = ("DELETE FROM kdistributortbl where KDistributorName = (%s)")
                cur.execute(query, (KDistributorName))

                con.commit()
                self.MakeKDistributorList()
            # con.close()




if __name__ == "__main__":
    uiAddKStuff = Ui_SysSettings()
    uiAddKStuff.show()
    sys.exit(app.exec_())
