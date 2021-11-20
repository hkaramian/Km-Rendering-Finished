# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proto_v02CgLFrM.ui'
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



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(425, 297)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 385, 227))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(250, 246, 255);\n"
"	border-radius : 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 203, 161, 20))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(155, 137, 200);")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 40, 381, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(0, 170, 127);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 110, 161, 30))
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.pushButton_2.setFont(font2)
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
        icon.addFile(u"F:\KmWorks\KmTools\Km_Rendering_Finished\Github\Km-Rendering-Finished\Km_Rendering_Finished\icons/pack/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 70, 381, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Emoji")
        font3.setPointSize(12)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(57, 57, 57);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(200, 110, 161, 30))
        self.pushButton_3.setMinimumSize(QSize(150, 30))
        self.pushButton_3.setFont(font2)
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
        self.pushButton_3.setIcon(icon)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(265, 203, 121, 20))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(155, 137, 200);")
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 160, 381, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(255, 170, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.pushButton_close = QPushButton(self.frame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(178, 200, 20, 20))
        self.pushButton_close.setMinimumSize(QSize(20, 20))
        self.pushButton_close.setFont(font2)
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(68, 77, 94);\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(68, 77, 94);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}")
        self.label_icon_success = QLabel(self.centralwidget)
        self.label_icon_success.setObjectName(u"label_icon_success")
        self.label_icon_success.setGeometry(QRect(170, 10, 80, 80))
        self.label_icon_success.setStyleSheet(u"")
        self.label_icon_success.setFrameShape(QFrame.NoFrame)
        self.label_icon_success.setPixmap(QPixmap(u"F:\KmWorks\KmTools\Km_Rendering_Finished\Github\Km-Rendering-Finished\Km_Rendering_Finished\icons/success.png"))
        self.label_icon_success.setScaledContents(True)
        self.label_icon_success.setAlignment(Qt.AlignCenter)
        self.label_icon_success.setWordWrap(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Km Rendering Finished v1.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<strong>Rendering Finished !</strong>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Open Render Directory", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FS_132-080_comp_v007.nk", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Open Render File", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"By Hossein Karamian", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<strong>Render Time (H:M:S) : 0:14:07</strong>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_icon_success.setText("")
    # retranslateUi

