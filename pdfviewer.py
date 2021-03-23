from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtWidgets
import pymysql
from sys import exit, argv
import subprocess
import socket
import threading

app = QtWidgets.QApplication(argv)
PDFJS = 'file:///C:/itoDB/webEngine/web/viewer.html'
# PDFJS = 'file:///usr/share/pdf.js/web/viewer.html'

class Window(QtWebEngineWidgets.QWebEngineView):

    def tcpserver(self):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 65101  # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(str(data))
                    conn.sendall(data)
                    data = str(data.decode())
        return data


    def __init__(self):
        super().__init__()
        self.runUi()

    def runUi(self):
        print('111')
        # specName = self.tcpserver()
        PDF = 'file:///C:/itoDB/specsource/' + '031 Ташкентская' + '.pdf'
        self.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF)))



    def getObjSpec(self):
        SqlDBName = 'itodb'
        passlog = open('C:\itoDB\sqlpasslog.txt', "r")
        l = [line.strip() for line in passlog]
        # print(l)
        data = str(l[0])
        return data


    def closeEvent(self, event):
            event.accept()


if __name__ == "__main__":
    window = Window()
    window.setGeometry(600, 50, 800, 600)
    window.show()
    exit(app.exec_())
