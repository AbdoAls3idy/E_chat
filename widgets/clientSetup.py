# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientSetup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 370)
        Form.setMinimumSize(QtCore.QSize(420, 370))
        Form.setMaximumSize(QtCore.QSize(420, 550))
        Form.setSizeIncrement(QtCore.QSize(420, 370))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../widgets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#nicknameField,#portNoField,#hostnameField{background:#fff;border-radius: 30px;color:#666;}\n"
"#BG_input,#BG_input_2,#BG_input_3{background:#fff;border: 1px solid #ddd;border-radius: 30px;}\n"
"#Icon_BG{background:transparent}\n"
"#connectButton,#close_btn{\n"
"color: #fff;\n"
"background-color: #34ace0;\n"
"font-size: 15px;\n"
"border-radius: 25px;\n"
"-webkit-transition-duration: 0.4; /* Safari*/\n"
"transition-duration: 0.4s;\n"
"cursor: pointer;\n"
"}\n"
"#connectButton:hover,#close_btn:hover{\n"
"background-color: #0984e3;\n"
"border-radius:25px;\n"
"font-size:15px;\n"
"-webkit-transition-duration: 0.4; /* Safari*/\n"
"transition-duration: 0.4s;\n"
"cursor: pointer;\n"
"color: black; \n"
"}")
        self.connectButton = QtWidgets.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(210, 290, 171, 51))
        self.connectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connectButton.setObjectName("connectButton")
        self.lblNickname = QtWidgets.QLabel(Form)
        self.lblNickname.setGeometry(QtCore.QRect(20, 60, 125, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblNickname.setFont(font)
        self.lblNickname.setObjectName("lblNickname")
        self.lblPortNo = QtWidgets.QLabel(Form)
        self.lblPortNo.setGeometry(QtCore.QRect(20, 129, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblPortNo.setFont(font)
        self.lblPortNo.setObjectName("lblPortNo")
        self.nicknameField = QtWidgets.QLineEdit(Form)
        self.nicknameField.setGeometry(QtCore.QRect(170, 49, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nicknameField.setFont(font)
        self.nicknameField.setAccessibleDescription("")
        self.nicknameField.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nicknameField.setAutoFillBackground(False)
        self.nicknameField.setStyleSheet("text-align: left;")
        self.nicknameField.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.nicknameField.setObjectName("nicknameField")
        self.portNoField = QtWidgets.QLineEdit(Form)
        self.portNoField.setGeometry(QtCore.QRect(170, 120, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portNoField.setFont(font)
        self.portNoField.setStyleSheet("text-align: left;")
        self.portNoField.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.portNoField.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.portNoField.setObjectName("portNoField")
        self.hostnameField = QtWidgets.QLineEdit(Form)
        self.hostnameField.setGeometry(QtCore.QRect(167, 190, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hostnameField.setFont(font)
        self.hostnameField.setStyleSheet("text-align: left;")
        self.hostnameField.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.hostnameField.setInputMethodHints(QtCore.Qt.ImhNone)
        self.hostnameField.setText("")
        self.hostnameField.setObjectName("hostnameField")
        self.lblHostname = QtWidgets.QLabel(Form)
        self.lblHostname.setGeometry(QtCore.QRect(20, 202, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblHostname.setFont(font)
        self.lblHostname.setObjectName("lblHostname")
        self.close_btn = QtWidgets.QPushButton(Form)
        self.close_btn.setGeometry(QtCore.QRect(30, 290, 171, 51))
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setObjectName("close_btn")
        self.BG_input = QtWidgets.QLineEdit(Form)
        self.BG_input.setGeometry(QtCore.QRect(150, 45, 241, 61))
        self.BG_input.setFocusPolicy(QtCore.Qt.NoFocus)
        self.BG_input.setObjectName("BG_input")
        self.BG_input_2 = QtWidgets.QLineEdit(Form)
        self.BG_input_2.setGeometry(QtCore.QRect(150, 116, 241, 60))
        self.BG_input_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.BG_input_2.setObjectName("BG_input_2")
        self.BG_input_3 = QtWidgets.QLineEdit(Form)
        self.BG_input_3.setGeometry(QtCore.QRect(150, 186, 241, 60))
        self.BG_input_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.BG_input_3.setObjectName("BG_input_3")
        self.BG_input_3.raise_()
        self.BG_input_2.raise_()
        self.BG_input.raise_()
        self.lblHostname.raise_()
        self.connectButton.raise_()
        self.lblNickname.raise_()
        self.lblPortNo.raise_()
        self.nicknameField.raise_()
        self.portNoField.raise_()
        self.hostnameField.raise_()
        self.close_btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "E-Chat"))
        self.connectButton.setText(_translate("Form", "Connect"))
        self.lblNickname.setText(_translate("Form", "User Name"))
        self.lblPortNo.setText(_translate("Form", "Port number"))
        self.nicknameField.setPlaceholderText(_translate("Form", "Enter User Name"))
        self.portNoField.setPlaceholderText(_translate("Form", "               Enter Port"))
        self.hostnameField.setPlaceholderText(_translate("Form", "                 Enter IP"))
        self.lblHostname.setText(_translate("Form", "Hostname"))
        self.close_btn.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

