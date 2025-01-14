# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FavoriteWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FavoriteWidget(object):
    def setupUi(self, FavoriteWidget):
        FavoriteWidget.setObjectName("FavoriteWidget")
        FavoriteWidget.resize(634, 586)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("App/resources/icons/like_black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FavoriteWidget.setWindowIcon(icon)
        FavoriteWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(FavoriteWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_button = QtWidgets.QPushButton(FavoriteWidget)
        self.play_button.setStyleSheet("QPushButton {\n"
"    height: 30px;\n"
"    color: #FFF;\n"
"    background-color: #6240C2;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4422A4;\n"
"}")
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        self.reload_button = QtWidgets.QPushButton(FavoriteWidget)
        self.reload_button.setStyleSheet("QPushButton {\n"
"    height: 30px;\n"
"    color: #FFF;\n"
"    background-color: #6240C2;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4422A4;\n"
"}")
        self.reload_button.setObjectName("reload_button")
        self.horizontalLayout.addWidget(self.reload_button)
        self.delete_button = QtWidgets.QPushButton(FavoriteWidget)
        self.delete_button.setStyleSheet("QPushButton {\n"
"    height: 30px;\n"
"    color: #FFF;\n"
"    background-color: #C04141;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #AC2D2D;\n"
"}")
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableWidget(FavoriteWidget)
        self.table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(98, 64, 194);")
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setColumnCount(2)
        self.table.setObjectName("table")
        self.table.setRowCount(0)
        self.table.horizontalHeader().setDefaultSectionSize(300)
        self.verticalLayout.addWidget(self.table)

        self.retranslateUi(FavoriteWidget)
        QtCore.QMetaObject.connectSlotsByName(FavoriteWidget)

        #
        FavoriteWidget.setFixedSize(634, 586)
        #

    def retranslateUi(self, FavoriteWidget):
        _translate = QtCore.QCoreApplication.translate
        FavoriteWidget.setWindowTitle(_translate("FavoriteWidget", "Favorite music"))
        self.play_button.setText(_translate("FavoriteWidget", "Play"))
        self.reload_button.setText(_translate("FavoriteWidget", "Update"))
        self.delete_button.setText(_translate("FavoriteWidget", "Delete all"))
