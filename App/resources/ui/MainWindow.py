# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(420, 540))
        MainWindow.setMaximumSize(QtCore.QSize(490, 775))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(150, 141, 181);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(413, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setPixmap(QtGui.QPixmap("../default.png"))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.author_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.author_label.setFont(font)
        self.author_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.author_label.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label.setObjectName("author_label")
        self.verticalLayout.addWidget(self.author_label)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.current_time_label = QtWidgets.QLabel(self.centralwidget)
        self.current_time_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.current_time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.current_time_label.setObjectName("current_time_label")
        self.horizontalLayout_2.addWidget(self.current_time_label)
        self.song_slider = QtWidgets.QSlider(self.centralwidget)
        self.song_slider.setOrientation(QtCore.Qt.Horizontal)
        self.song_slider.setObjectName("song_slider")
        self.horizontalLayout_2.addWidget(self.song_slider)
        self.end_time_label = QtWidgets.QLabel(self.centralwidget)
        self.end_time_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.end_time_label.setObjectName("end_time_label")
        self.horizontalLayout_2.addWidget(self.end_time_label)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem4)
        self.dislike_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dislike_button.sizePolicy().hasHeightForWidth())
        self.dislike_button.setSizePolicy(sizePolicy)
        self.dislike_button.setMinimumSize(QtCore.QSize(0, 70))
        self.dislike_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/dislike.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dislike_button.setIcon(icon1)
        self.dislike_button.setIconSize(QtCore.QSize(50, 50))
        self.dislike_button.setFlat(True)
        self.dislike_button.setObjectName("dislike_button")
        self.buttons_layout.addWidget(self.dislike_button)
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_button.sizePolicy().hasHeightForWidth())
        self.prev_button.setSizePolicy(sizePolicy)
        self.prev_button.setMinimumSize(QtCore.QSize(0, 70))
        self.prev_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/prev.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev_button.setIcon(icon2)
        self.prev_button.setIconSize(QtCore.QSize(50, 50))
        self.prev_button.setFlat(True)
        self.prev_button.setObjectName("prev_button")
        self.buttons_layout.addWidget(self.prev_button)
        self.main_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button.sizePolicy().hasHeightForWidth())
        self.main_button.setSizePolicy(sizePolicy)
        self.main_button.setMinimumSize(QtCore.QSize(0, 70))
        self.main_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button.setIcon(icon3)
        self.main_button.setIconSize(QtCore.QSize(70, 70))
        self.main_button.setFlat(True)
        self.main_button.setObjectName("main_button")
        self.buttons_layout.addWidget(self.main_button)
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setMinimumSize(QtCore.QSize(0, 70))
        self.next_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon4)
        self.next_button.setIconSize(QtCore.QSize(50, 50))
        self.next_button.setFlat(True)
        self.next_button.setObjectName("next_button")
        self.buttons_layout.addWidget(self.next_button)
        self.like_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.like_button.sizePolicy().hasHeightForWidth())
        self.like_button.setSizePolicy(sizePolicy)
        self.like_button.setMinimumSize(QtCore.QSize(0, 70))
        self.like_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.like_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/like.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.like_button.setIcon(icon5)
        self.like_button.setIconSize(QtCore.QSize(50, 50))
        self.like_button.setFlat(True)
        self.like_button.setObjectName("like_button")
        self.buttons_layout.addWidget(self.like_button)
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.buttons_layout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.effects_button = QtWidgets.QPushButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../icons/effects.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.effects_button.setIcon(icon6)
        self.effects_button.setFlat(True)
        self.effects_button.setObjectName("effects_button")
        self.horizontalLayout.addWidget(self.effects_button)
        self.volume_button = QtWidgets.QPushButton(self.centralwidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../icons/volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volume_button.setIcon(icon7)
        self.volume_button.setFlat(True)
        self.volume_button.setObjectName("volume_button")
        self.horizontalLayout.addWidget(self.volume_button)
        self.playlist_button = QtWidgets.QPushButton(self.centralwidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../icons/playlist.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playlist_button.setIcon(icon8)
        self.playlist_button.setFlat(True)
        self.playlist_button.setObjectName("playlist_button")
        self.horizontalLayout.addWidget(self.playlist_button)
        spacerItem8 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: rgb(225, 225, 225);")
        self.error_label.setScaledContents(True)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 26))
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menuTrack = QtWidgets.QMenu(self.menubar)
        self.menuTrack.setObjectName("menuTrack")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setShortcutVisibleInContextMenu(True)
        self.action.setObjectName("action")
        self.open_file_action = QtWidgets.QAction(MainWindow)
        self.open_file_action.setObjectName("open_file_action")
        self.open_folder_action = QtWidgets.QAction(MainWindow)
        self.open_folder_action.setObjectName("open_folder_action")
        self.properties_action = QtWidgets.QAction(MainWindow)
        self.properties_action.setObjectName("properties_action")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.menuOpen.addAction(self.open_file_action)
        self.menuOpen.addAction(self.open_folder_action)
        self.menuTrack.addAction(self.properties_action)
        self.menuHelp.addAction(self.about_action)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuTrack.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shuffle"))
        self.title_label.setText(_translate("MainWindow", "TextLabel"))
        self.author_label.setText(_translate("MainWindow", "TextLabel"))
        self.current_time_label.setText(_translate("MainWindow", "0:00"))
        self.end_time_label.setText(_translate("MainWindow", "0:00"))
        self.error_label.setText(_translate("MainWindow", "Ошибка: не выбран файл!"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuTrack.setTitle(_translate("MainWindow", "Track"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.action.setText(_translate("MainWindow", "Open folder"))
        self.open_file_action.setText(_translate("MainWindow", "Open File"))
        self.open_folder_action.setText(_translate("MainWindow", "Open Folder"))
        self.open_folder_action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.properties_action.setText(_translate("MainWindow", "Properties"))
        self.properties_action.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.about_action.setText(_translate("MainWindow", "About"))
