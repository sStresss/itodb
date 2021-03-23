from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import GlobalValues
import sys
import pyautogui
from MainPanel import Ui_MainDB
import pymysql
import win32api
import time




app = QtWidgets.QApplication(sys.argv)

class Ui_Login(QDialog):


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        self.setObjectName("panel_autologin")
        self.resize(1920, 1080)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(0,0,0);")
        self.leLogin = QtWidgets.QLineEdit(self)
        self.leLogin.setGeometry(QtCore.QRect(825, 510, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leLogin.setFont(font)
        self.leLogin.setStyleSheet("background-color: rgb(255,255,255);\n"
                                   "color: rgb(0,0,0);\n"
                                   "border-radius:3px;\n"
                                   "border: 1px solid rgb(150,150,150);")
        self.leLogin.setText("")
        self.leLogin.setObjectName("leLogin")
        self.lePassword = QtWidgets.QLineEdit(self)
        self.lePassword.setGeometry(QtCore.QRect(825, 546, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lePassword.setFont(font)
        self.lePassword.setStyleSheet("background-color: rgb(255,255,255);\n"
                                      "color: rgb(0,0,0);\n"
                                      "border-radius:3px;\n"
                                      "border: 1px solid rgb(150,150,150);")
        self.lePassword.setText("")
        self.lePassword.setObjectName("lePassword")
        self.lbl = QtWidgets.QLabel(self)
        self.lbl.setGeometry(QtCore.QRect(895, 475, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet("background-color: rgb(242,242,242);\n"
                               "color: black;")
        self.lbl.setObjectName("lbl")
        self.butInput = QtWidgets.QPushButton(self)
        self.butInput.setGeometry(QtCore.QRect(910, 601, 101, 26))
        self.butInput.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.butInput.setFont(font)
        self.butInput.setStyleSheet("QPushButton:!hover {background-color: rgb(227,227,227);\n"
                                    "color: rgb(0,0,0);\n"
                                    "border-radius:3px;\n"
                                    "border:1px solid rgb(135,135,135);}\n"
                                    "\n"
                                    "QPushButton:hover {background-color: rgb(84,122,181);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius:3px;\n"
                                    "border:1px solid rgb(63,63,63);}\n"
                                    "QPushButton:hover:pressed {background-color: rgb(50,75,115);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius:3px;\n"
                                    "border:1px solid rgb(63,63,63);};")
        self.butInput.setObjectName("butInput")
        self.label_33 = QtWidgets.QLabel(self)
        self.label_33.setGeometry(QtCore.QRect(758, 448, 404, 22))
        self.label_33.setStyleSheet("background-color: rgb(255,255,255);\n"
                                    "border: 1px solid rgb(255,255,255);\n"
                                    "border-bottom-color: rgb(205,205,205);\n"
                                    "border-top-color: rgb(150,150,150);\n"
                                    "border-left-color: rgb(150,150,150);\n"
                                    "border-right-color: rgb(150,150,150);")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self)
        self.label_34.setGeometry(QtCore.QRect(760, 449, 20, 20))
        self.label_34.setStyleSheet("background-color: rgb(255,255,255);")
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap(":/img/img/sinaps1818.png"))
        self.label_34.setObjectName("label_34")
        self.btnCloseMainForm = QtWidgets.QPushButton(self)
        self.btnCloseMainForm.setGeometry(QtCore.QRect(1141, 449, 20, 20))
        self.btnCloseMainForm.setStyleSheet("QPushButton:!hover{ background-color: rgb(255,255,255);\n"
                                            "border: 0px solid rgb(255,255,255);\n"
                                            "border-radius: 0px;\n"
                                            "image: url(C:/img/iconextbl1313.png);}\n"
                                            "\n"
                                            "QPushButton:hover { background-color: rgb(84,122,181);\n"
                                            "border: 0px solid rgb(0,0,0);\n"
                                            "border-radius: 0px;\n"
                                            "image: url(C:/img/iconext1313.png);}\n"
                                            "\n"
                                            "\n"
                                            "QPushButton:hover:pressed { background-color: rgb(50,75,115);\n"
                                            "border: 0px solid rgb(0,0,0);\n"
                                            "border-radius:02px;\n"
                                            "image: url(C:/img/iconext1313.png);};\n"
                                            "")
        self.btnCloseMainForm.setText("")
        self.btnCloseMainForm.setObjectName("btnCloseMainForm")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(758, 469, 404, 171))
        self.label.setStyleSheet("background-color: rgb(242,242,242);\n"
                                 "border: 1px solid rgb(242,242,242);\n"
                                 "border-bottom-color: rgb(150,150,150);\n"
                                 "border-left-color: rgb(150,150,150);\n"
                                 "border-right-color: rgb(150,150,150);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_setscreen = QtWidgets.QLabel(self)
        self.label_setscreen.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label_setscreen.setStyleSheet("image: url(C:/img/screen1.png);")
        self.label_setscreen.setObjectName("label_setscreen")
        self.label_gradient = QtWidgets.QLabel(self)
        self.label_gradient.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label_gradient.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0,0,0, 110), stop:1 rgba(0,0,0, 110));")
        self.label_gradient.setObjectName("label_gradient")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(1150, 458, 31, 172))
        self.label_5.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(739, 458, 31, 172))
        self.label_6.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0.511, x2:0, y2:0.5, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(769, 427, 381, 31))
        self.label_7.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(1150, 397, 61, 61))
        self.label_8.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0, cy:1, radius:0.5, fx:0, fy:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(1150, 630, 61, 61))
        self.label_10.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0, cy:0, radius:0.5, fx:0, fy:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0,0,0, 0))")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(708, 397, 61, 61))
        self.label_11.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:1, cy:1, radius:0.5, fx:1, fy:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(770, 630, 380, 31))
        self.label_12.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(708, 630, 62, 61))
        self.label_13.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:1, cy:0, radius:0.5, fx:1, fy:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_textMes = QtWidgets.QLabel(self)
        self.label_textMes.setGeometry(QtCore.QRect(826, 577, 271, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_textMes.setFont(font)
        self.label_textMes.setStyleSheet("background-color: rgb(242,242,242);\n"
                                         "color: black;")
        self.label_textMes.setText("")
        self.label_textMes.setObjectName("label_textMes")
        self.label_setscreen.raise_()
        self.label_gradient.raise_()


        self.label_13.raise_()
        self.label_11.raise_()
        self.label_6.raise_()
        self.label_12.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.label_33.raise_()
        self.btnCloseMainForm.raise_()
        self.label_34.raise_()
        self.lePassword.raise_()
        self.lbl.raise_()
        self.leLogin.raise_()
        self.butInput.raise_()
        self.label_textMes.raise_()




        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.firstSets()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("panel_autologin", "Dialog"))
        self.lbl.setText(_translate("panel_autologin", "Авторизация"))
        self.butInput.setText(_translate("panel_autologin", "ВХОД"))
        self.label_33.setText(_translate("panel_autologin", "         Вход в систему"))

    def firstSets(self):
        win32api.LoadKeyboardLayout('00000409', 1)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.label_34.setStyleSheet("background-color: rgb(255,255,255);\n"
                                    "image: url(C:/itoDB/iconMainWindow.ico);")

        pyautogui.screenshot('C:\\itoDB\\s_login.png')
        self.label_setscreen.setStyleSheet("image: url(C:/itoDB/s_login.png);")
        self.butInput.clicked.connect(self.checkPassLog)
        self.btnCloseMainForm.clicked.connect(self.exitLogin)

        #aurologin
        # self.leLogin.setText("ksv")
        # self.lePassword.setText("281082")
        # self.butInput.setFocus()

    def checkPassLog(self):

        print('startCheck')

        self.label_textMes.setText('')
        checkLogin = False
        checkPassLog = False
        login = self.leLogin.text()
        pwd = self.lePassword.text()

        passlog = open('C:\itoDB\sqlpasslog.txt', "r")
        l = [line.strip() for line in passlog]
        # print(l)
        SqlHostname = str(l[0])
        SqlPort = int(l[1])
        SqlUserName = str(l[2])
        SqlPwd = str(l[3])
        SqlDBName = 'itodb'

        con = pymysql.connect(host=str(SqlHostname),
                              port=int(SqlPort),
                              user=str(SqlUserName),
                              passwd=str(SqlPwd),
                              db=str(SqlDBName))


        print('checkBD: ', con.open)

        with con:
            cur = con.cursor()
            cur.execute("SELECT login, password, accessgroup FROM passlog")
            rows = cur.fetchall()

            for row in rows:
                if str(row[0]) == str(login):
                    checkLogin = True
                    if str(row[1]) == str(pwd):
                        checkPassLog = True
                        GlobalValues.AccesGroup = str(row[2])
            if (login == '') or (pwd == ''):
                self.label_textMes.setText('Ошибка. Введите данные для авторизации.')
            else:
                if checkPassLog == True:
                    GlobalValues.UserName = login
                    self.openMainPanel()
                else:
                    if checkLogin == True:
                        self.label_textMes.setText('Ошибка. Не верный пароль.')
                        self.lePassword.setText('')
                    else:
                        self.label_textMes.setText('Ошибка. Не верный логин')
            cur.close()
        con.close()

    def openMainPanel(self):
        print('start')
        self.uiMainPanel = Ui_MainDB()
        self.uiMainPanel.show()
        print('finish!')
        uiLogin.close()

    def exitLogin(self):
        Ui_Login.close()




if __name__ == "__main__":
    uiLogin = Ui_Login()
    uiLogin.show()
    sys.exit(app.exec_())
