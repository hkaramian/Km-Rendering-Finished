# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_v2fPtqWR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(425, 288)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 385, 227))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.label_version = QLabel(self.frame)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(6, 205, 191, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_version.setFont(font1)
        self.label_version.setStyleSheet(u"color: rgb(166, 166, 166);\n"
"\n"
"")
        self.label_version.setTextFormat(Qt.AutoText)
        self.label_version.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 45, 381, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(15)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(0, 170, 127);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 115, 166, 30))
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(9)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon = QIcon()
        icon.addFile(os.path.dirname(__file__)+"/icons/pack/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.label_project_name = QLabel(self.frame)
        self.label_project_name.setObjectName(u"label_project_name")
        self.label_project_name.setGeometry(QRect(0, 75, 381, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(10)
        self.label_project_name.setFont(font4)
        self.label_project_name.setStyleSheet(u"color: rgb(66, 66, 66);")
        self.label_project_name.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(196, 115, 167, 30))
        self.pushButton_3.setMinimumSize(QSize(150, 30))
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(os.path.dirname(__file__)+"/icons/pack/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.label__Hossein = QLabel(self.frame)
        self.label__Hossein.setObjectName(u"label__Hossein")
        self.label__Hossein.setGeometry(QRect(207, 205, 171, 20))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setWeight(50)
        font5.setStrikeOut(False)
        self.label__Hossein.setFont(font5)
        self.label__Hossein.setStyleSheet(u"color: rgb(166, 166, 166);")
        self.label__Hossein.setTextFormat(Qt.AutoText)
        self.label__Hossein.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_close = QPushButton(self.frame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(361, 4, 20, 20))
        self.pushButton_close.setMinimumSize(QSize(18, 18))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(9)
        self.pushButton_close.setFont(font6)
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(128, 146, 177);\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(128, 146, 177);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(97, 110, 134);\n"
"	border: 2px solid rgb(97, 110, 134);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(os.path.dirname(__file__)+"/icons/pack/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_clipboard_directory = QPushButton(self.frame)
        self.pushButton_clipboard_directory.setObjectName(u"pushButton_clipboard_directory")
        self.pushButton_clipboard_directory.setGeometry(QRect(20, 155, 41, 30))
        self.pushButton_clipboard_directory.setMinimumSize(QSize(20, 20))
        self.pushButton_clipboard_directory.setFont(font6)
        self.pushButton_clipboard_directory.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid  rgb(133, 201, 84);\n"
"	border-radius: 5px;	\n"
"	background-color:  rgb(133, 201, 84);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(145, 210, 90);\n"
"	border: 2px solidrgb(145, 210, 90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(133, 201, 84);\n"
"	border: 2px solid rgb(133, 201, 84);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(os.path.dirname(__file__)+"/icons/pack/cil-copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clipboard_directory.setIcon(icon3)
        self.pushButton_clipboard_file = QPushButton(self.frame)
        self.pushButton_clipboard_file.setObjectName(u"pushButton_clipboard_file")
        self.pushButton_clipboard_file.setGeometry(QRect(322, 155, 41, 30))
        self.pushButton_clipboard_file.setMinimumSize(QSize(20, 20))
        self.pushButton_clipboard_file.setFont(font6)
        self.pushButton_clipboard_file.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid  rgb(133, 201, 84);\n"
"	border-radius: 5px;	\n"
"	background-color:  rgb(133, 201, 84);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(145, 210, 90);\n"
"	border: 2px solidrgb(145, 210, 90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(133, 201, 84);\n"
"	border: 2px solid rgb(133, 201, 84);\n"
"}")
        self.pushButton_clipboard_file.setIcon(icon3)
        self.pushButton_render_icon = QPushButton(self.frame)
        self.pushButton_render_icon.setObjectName(u"pushButton_render_icon")
        self.pushButton_render_icon.setEnabled(True)
        self.pushButton_render_icon.setGeometry(QRect(73, 155, 113, 30))
        self.pushButton_render_icon.setMinimumSize(QSize(20, 20))
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semibold")
        font7.setPointSize(11)
        font7.setBold(False)
        font7.setWeight(50)
        self.pushButton_render_icon.setFont(font7)
        self.pushButton_render_icon.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid  rgb(77, 190, 217);\n"
"	border-radius: 5px;	\n"
"	background-color:  rgb(77, 190, 217);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(98, 193, 217);\n"
"	border: 2px solidrgb(98, 193, 217);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(77, 190, 217);\n"
"	border: 2px solid rgb(77, 190, 217);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(os.path.dirname(__file__)+"/icons/pack/cil-speedometer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_render_icon.setIcon(icon4)
        self.pushButton_render_icon.setIconSize(QSize(30, 30))
        self.pushButton_CreateRead = QPushButton(self.frame)
        self.pushButton_CreateRead.setObjectName(u"pushButton_CreateRead")
        self.pushButton_CreateRead.setGeometry(QRect(196, 155, 113, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI Semibold")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.pushButton_CreateRead.setFont(font8)
        self.pushButton_CreateRead.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid  rgb(77, 190, 217);\n"
"	border-radius: 5px;	\n"
"	background-color:  rgb(77, 190, 217);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(98, 193, 217);\n"
"	border: 2px solidrgb(98, 193, 217);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(77, 190, 217);\n"
"	border: 2px solid rgb(77, 190, 217);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(os.path.dirname(__file__)+"/icons/pack/cil-movie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_CreateRead.setIcon(icon5)
        self.label_icon_success = QLabel(self.centralwidget)
        self.label_icon_success.setObjectName(u"label_icon_success")
        self.label_icon_success.setGeometry(QRect(170, 10, 80, 80))
        self.label_icon_success.setStyleSheet(u"")
        self.label_icon_success.setFrameShape(QFrame.NoFrame)
        self.label_icon_success.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/success.png"))
        self.label_icon_success.setScaledContents(True)
        self.label_icon_success.setAlignment(Qt.AlignCenter)
        self.label_icon_success.setWordWrap(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notification Panel", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Km Rendering Finished v2.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<strong>Rendering Finished !</strong>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Open Render Directory", None))
        self.label_project_name.setText(QCoreApplication.translate("MainWindow", u"FS_132-080_comp_v007.nk", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Open Render File", None))
        self.label__Hossein.setText(QCoreApplication.translate("MainWindow", u"By Hossein Karamian", None))
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_clipboard_directory.setToolTip(QCoreApplication.translate("MainWindow", u"Copy Render Directory Address to ClipBoard", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clipboard_directory.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_clipboard_file.setToolTip(QCoreApplication.translate("MainWindow", u"Copy Render File Address to ClipBoard", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clipboard_file.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_render_icon.setToolTip(QCoreApplication.translate("MainWindow", u"Render Time (H:M:S)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_render_icon.setText(QCoreApplication.translate("MainWindow", u"00:05:23", None))
#if QT_CONFIG(tooltip)
        self.pushButton_CreateRead.setToolTip(QCoreApplication.translate("MainWindow", u"Create Read Node From Rendered File", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_CreateRead.setText(QCoreApplication.translate("MainWindow", u"Create Read", None))
#if QT_CONFIG(tooltip)
        self.label_icon_success.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_icon_success.setText("")
    # retranslateUi

