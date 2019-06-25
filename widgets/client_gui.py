# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 370)
        MainWindow.setStyleSheet("#messageEdit{background:#fff;border: 1px solid #ddd;border-radius: 35px;}\n"
            "#sendBtn{\n"
            "color: #fff;\n"
            "background-color: #34ace0;\n"
            "font-size: 15px;\n"
            "border-radius: 25px;\n"
            "-webkit-transition-duration: 0.4; /* Safari*/\n"
            "transition-duration: 0.4s;\n"
            "cursor: pointer;\n"
            "}\n"
            "#sendBtn:hover{\n"
            "background-color: #0984e3;\n"
            "border-radius:25px;\n"
            "font-size:15px;\n"
            "-webkit-transition-duration: 0.4; /* Safari*/\n"
            "transition-duration: 0.4s;\n"
            "cursor: pointer;\n"
            "color: black; \n"
            "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.messageEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.messageEdit.setGeometry(QtCore.QRect(15, 210, 400, 74))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.messageEdit.setFont(font)
        self.messageEdit.setObjectName("messageEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 180, 350, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.receivedMessages = QtWidgets.QTextBrowser(self.centralwidget)
        self.receivedMessages.setGeometry(QtCore.QRect(1, 2, 421, 200))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.receivedMessages.setFont(font)
        self.receivedMessages.setObjectName("receivedMessages")
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(135, 295, 171, 51))
        self.sendBtn.setObjectName("sendBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.nickname = ""
        self.port = 8080
        self.hostname = "127.0.0.1"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E-Chat"))
        self.sendBtn.setText(_translate("MainWindow", "Send"))