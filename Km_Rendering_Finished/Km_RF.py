import nuke
import os
import sys
import platform
import subprocess
import datetime

operatingSystem = platform.system()


def Open_Render_Directory():
        path =  os.path.dirname(nuke.thisNode().knob('file').value())
        if os.path.exists(path):
    
            if operatingSystem == "Windows":
                os.startfile(path)
            elif operatingSystem == "Darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])

def Open_Render_File():
        r_file =  nuke.thisNode().knob('file').value()
        os.startfile(r_file)

def Copy_To_ClipBoard(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


def Set_Render_Start_Time():
    if not nuke.root().knob("Km_Render_Start_Time"):
        nuke.root().addKnob(nuke.EvalString_Knob("Km_Render_Start_Time"))
        nuke.root().knob("Km_Render_Start_Time").setVisible(False)

    Current_time_str = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    nuke.root().knob("Km_Render_Start_Time").setValue(Current_time_str)
    

def Get_Time_Duration():
    time1_str = nuke.root().knob("Km_Render_Start_Time").getValue()
    time1 = datetime.datetime.strptime(time1_str, '%Y-%m-%d %H:%M:%S') # time1_str sample : '2021-11-20 12:33:00'
    time2 = datetime.datetime.now()
    duration  = time2 - time1
    duration_in_s = duration.total_seconds()
    days    = divmod(duration_in_s, 86400)        # Get days (without [0]!)
    hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
    minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
    seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
    print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))

def Get_Script_Name():
    return os.path.basename(nuke.root().name())



nuke.addBeforeRender(Set_Render_Start_Time)
nuke.addAfterRender(Get_Time_Duration)







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



class Notif_Panel(QWidget):
    """docstring for Panel"""
    def __init__(self):
        super(Notif_Panel, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

app = QApplication(sys.argv)
window = Notif_Panel()
sys.exit(app.exec_())