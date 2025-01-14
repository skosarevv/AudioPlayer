# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(443, 189)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("App/resources/icons/logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginDialog.setWindowIcon(icon)
        LoginDialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_label = QtWidgets.QLabel(LoginDialog)
        self.login_label.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.horizontalLayout.addWidget(self.login_label)
        self.login_input = QtWidgets.QLineEdit(LoginDialog)
        self.login_input.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_input.setFont(font)
        self.login_input.setStyleSheet("border-radius: 5px;\n"
"border-color: #787878;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"height: 24px;")
        self.login_input.setObjectName("login_input")
        self.horizontalLayout.addWidget(self.login_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pass_label = QtWidgets.QLabel(LoginDialog)
        self.pass_label.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.horizontalLayout_2.addWidget(self.pass_label)
        self.pass_input = QtWidgets.QLineEdit(LoginDialog)
        self.pass_input.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pass_input.setFont(font)
        self.pass_input.setStyleSheet("border-radius: 5px;\n"
"border-color: #787878;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"height: 24px;")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        self.horizontalLayout_2.addWidget(self.pass_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.reg_button = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reg_button.sizePolicy().hasHeightForWidth())
        self.reg_button.setSizePolicy(sizePolicy)
        self.reg_button.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reg_button.setFont(font)
        self.reg_button.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #282828;\n"
"    height: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"}\n"
"QPushButton:onclick {\n"
"    background-color: rgb(56, 70, 77);\n"
"}")
        self.reg_button.setAutoDefault(False)
        self.reg_button.setObjectName("reg_button")
        self.horizontalLayout_3.addWidget(self.reg_button)
        self.log_in_button = QtWidgets.QPushButton(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_in_button.sizePolicy().hasHeightForWidth())
        self.log_in_button.setSizePolicy(sizePolicy)
        self.log_in_button.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_in_button.setFont(font)
        self.log_in_button.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color:#6240C2;\n"
"    color: rgb(255, 255, 255);\n"
"    height: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4422A4;\n"
"}")
        self.log_in_button.setAutoDefault(False)
        self.log_in_button.setDefault(True)
        self.log_in_button.setObjectName("log_in_button")
        self.horizontalLayout_3.addWidget(self.log_in_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.error_label = QtWidgets.QLabel(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)

        #
        self.error_label.hide()
        #

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Auth"))
        self.login_label.setText(_translate("LoginDialog", "Login"))
        self.pass_label.setText(_translate("LoginDialog", "Password"))
        self.reg_button.setText(_translate("LoginDialog", "Register"))
        self.log_in_button.setText(_translate("LoginDialog", "Log in"))
        self.error_label.setText(_translate("LoginDialog", "Error: Invalid username or password"))
