import os
import sys
import platform
import subprocess
import datetime





# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proto_v02OKwJfZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_notif_panel import Ui_MainWindow

class MainWindow2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        


        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        ## opacity
        # self.op_effect=QGraphicsOpacityEffect(self)
        # self.opacity_value = 0.88
        # self.op_effect.setOpacity(self.opacity_value)
        # self.setGraphicsEffect(self.op_effect)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.frame.setGraphicsEffect(self.shadow)


        self.ui.pushButton_close.clicked.connect(self.close)

        self.show()

    # def enterEvent(self, event): 
    #     self.op_effect.setOpacity(1)

    # def leaveEvent(self, event):  
    #     self.op_effect.setOpacity(self.opacity_value)
        

        

app = QApplication(sys.argv)
window = MainWindow2()
sys.exit(app.exec_())