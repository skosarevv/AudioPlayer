# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PropertiesWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PropertiesWidget(object):
    def setupUi(self, PropertiesWidget):
        PropertiesWidget.setObjectName("PropertiesWidget")
        PropertiesWidget.resize(505, 525)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PropertiesWidget.sizePolicy().hasHeightForWidth())
        PropertiesWidget.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("App/resources/icons/info_black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PropertiesWidget.setWindowIcon(icon)
        PropertiesWidget.setStyleSheet("QLabel {\n"
                                       "    color: rgb(120, 120, 120);\n"
                                       "}\n"
                                       "QWidget#PropertiesWidget {\n"
                                       "    background-color: rgb(98, 64, 194);\n"
                                       "}")
        self.gridLayout = QtWidgets.QGridLayout(PropertiesWidget)
        self.gridLayout.setContentsMargins(65, 65, 65, 65)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.title_label = QtWidgets.QLabel(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)
        self.file_label = QtWidgets.QLabel(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.file_label.setFont(font)
        self.file_label.setObjectName("file_label")
        self.gridLayout.addWidget(self.file_label, 6, 0, 1, 1)
        self.file_text = QtWidgets.QLineEdit(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.file_text.setFont(font)
        self.file_text.setText("")
        self.file_text.setFrame(False)
        self.file_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.file_text.setReadOnly(True)
        self.file_text.setObjectName("file_text")
        self.gridLayout.addWidget(self.file_text, 6, 1, 1, 1)
        self.album_text = QtWidgets.QLineEdit(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.album_text.setFont(font)
        self.album_text.setFrame(False)
        self.album_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.album_text.setReadOnly(True)
        self.album_text.setObjectName("album_text")
        self.gridLayout.addWidget(self.album_text, 2, 1, 1, 1)
        self.genre_label = QtWidgets.QLabel(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.genre_label.setFont(font)
        self.genre_label.setObjectName("genre_label")
        self.gridLayout.addWidget(self.genre_label, 3, 0, 1, 1)
        self.album_label = QtWidgets.QLabel(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.album_label.setFont(font)
        self.album_label.setObjectName("album_label")
        self.gridLayout.addWidget(self.album_label, 2, 0, 1, 1)
        self.year_text = QtWidgets.QLineEdit(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.year_text.setFont(font)
        self.year_text.setFrame(False)
        self.year_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.year_text.setReadOnly(True)
        self.year_text.setObjectName("year_text")
        self.gridLayout.addWidget(self.year_text, 4, 1, 1, 1)
        self.length_text = QtWidgets.QLineEdit(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.length_text.setFont(font)
        self.length_text.setText("")
        self.length_text.setFrame(False)
        self.length_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.length_text.setReadOnly(True)
        self.length_text.setObjectName("length_text")
        self.gridLayout.addWidget(self.length_text, 5, 1, 1, 1)
        self.length_label = QtWidgets.QLabel(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.length_label.setFont(font)
        self.length_label.setObjectName("length_label")
        self.gridLayout.addWidget(self.length_label, 5, 0, 1, 1)
        self.author_label = QtWidgets.QLabel(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.author_label.setFont(font)
        self.author_label.setObjectName("author_label")
        self.gridLayout.addWidget(self.author_label, 1, 0, 1, 1)
        self.title_text = QtWidgets.QLineEdit(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title_text.setFont(font)
        self.title_text.setFrame(False)
        self.title_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.title_text.setReadOnly(True)
        self.title_text.setObjectName("title_text")
        self.gridLayout.addWidget(self.title_text, 0, 1, 1, 1)
        self.author_text = QtWidgets.QLineEdit(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.author_text.setFont(font)
        self.author_text.setFrame(False)
        self.author_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.author_text.setReadOnly(True)
        self.author_text.setObjectName("author_text")
        self.gridLayout.addWidget(self.author_text, 1, 1, 1, 1)
        self.genre_text = QtWidgets.QLineEdit(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.genre_text.setFont(font)
        self.genre_text.setFrame(False)
        self.genre_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.genre_text.setReadOnly(True)
        self.genre_text.setObjectName("genre_text")
        self.gridLayout.addWidget(self.genre_text, 3, 1, 1, 1)
        self.year_label = QtWidgets.QLabel(PropertiesWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.year_label.setFont(font)
        self.year_label.setObjectName("year_label")
        self.gridLayout.addWidget(self.year_label, 4, 0, 1, 1)

        self.retranslateUi(PropertiesWidget)
        QtCore.QMetaObject.connectSlotsByName(PropertiesWidget)

        #
        PropertiesWidget.setFixedSize(505, 645)
        #

    def retranslateUi(self, PropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        PropertiesWidget.setWindowTitle(_translate("PropertiesWidget", "Properties"))
        self.title_label.setText(_translate("PropertiesWidget", "Title"))
        self.file_label.setText(_translate("PropertiesWidget", "Location"))
        self.genre_label.setText(_translate("PropertiesWidget", "Genre"))
        self.album_label.setText(_translate("PropertiesWidget", "Album"))
        self.length_label.setText(_translate("PropertiesWidget", "Length"))
        self.author_label.setText(_translate("PropertiesWidget", "Author"))
        self.year_label.setText(_translate("PropertiesWidget", "Year"))
