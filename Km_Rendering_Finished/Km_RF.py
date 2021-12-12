#
# Km Rendering Finished v1.0.2
#
# Developed By Hossein Karamian
# 
# www.hkaramian.com
#
#    _  __  __  __ 
#   | |/ / |  \/  |
#   | ' /  | \  / |
#   |  <   | |\/| |
#   |_|\_\ |_|  |_|
#

"""
Changes Log :
v1.0 | First version | November 24 , 2021 
v1.0.1 | Bug Fix , in some cases notification window disappears just after it's popping up | November 25 , 2021 
v1.0.2 | Bug Fix | November 27 , 2021 
v2.0 | Linux compatible , Bug Fix , Add Create Read Node Button, Open Render File button now also working for sequence renders | December 10 , 2021
"""


import nuke
import nukescripts
import os
import sys
import platform
import subprocess
import datetime
import glob 
import re


################################################################################
## ui_notif_panel.py changes needed for new version from qt designer : 
## add import os 
## Replace  : 
## u"../Km_Rendering_Finished/icons
## os.path.dirname(__file__)+"/icons
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_notif_panel import Ui_MainWindow

class Km_Notification_Panel(QMainWindow):
    def __init__(self,WR):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Write_node = WR

        #self.setStyle(QStyleFactory.create('Plastique'))
        ## REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # opacity
        self.op_effect=QGraphicsOpacityEffect(self)
        self.opacity_value = 0.92
        self.op_effect.setOpacity(self.opacity_value)
        self.setGraphicsEffect(self.op_effect)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.frame.setGraphicsEffect(self.shadow)

        # remove text shadows
        self.RemoveDefaultTextShadow()

        # set center , for linux 
        centerX = int(QDesktopWidget().screenGeometry(-1).width()/2.0 - self.width()/2.0)
        centerY = int(QDesktopWidget().screenGeometry(-1).height()/2.0 - self.height()/2.0)
        self.move(centerX,centerY)

        
        # Set Signals
        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.Open_Render_Directory)
        self.ui.pushButton_3.clicked.connect(self.Open_Render_File)
        self.ui.pushButton_clipboard_directory.clicked.connect(self.Copy_To_ClipBoard_Directory)
        self.ui.pushButton_clipboard_file.clicked.connect(self.Copy_To_ClipBoard_File)
        self.ui.pushButton_CreateRead.clicked.connect(self.CreateReadNode)

        # render time
        #self.ui.label_render_time.setText(" Render Time (H:M:S) :  "+self.Get_Time_Duration())
        self.ui.pushButton_render_icon.setText(self.Get_Time_Duration())

        # credit
        self.ui.label__Hossein.setText('''<a href='http://www.hkaramian.com' style='color: rgb(166, 166, 166);text-decoration: none;'>By Hossein Karamian</a>''')
        self.ui.label__Hossein.setOpenExternalLinks(True)


        # set project name lable
        self.ui.label_project_name.setText(os.path.basename(nuke.root().name()))




        
    def RemoveDefaultTextShadow(self):
        """Get Rid of nuke pyside default style that apply shadow for texts"""   
        #self.setStyle(QStyleFactory.create('Windows'))
        self.ui.pushButton_CreateRead.setStyle(QStyleFactory.create('Windows'))
        self.ui.pushButton_render_icon.setStyle(QStyleFactory.create('Windows'))
        self.ui.label_version.setStyle(QStyleFactory.create('Windows'))
        self.ui.label_project_name.setStyle(QStyleFactory.create('Windows'))


    # def enterEvent(self, event): 
    #     self.op_effect.setOpacity(1)

    # def leaveEvent(self, event):  
    #     self.op_effect.setOpacity(self.opacity_value)


    def Open_Render_Directory(self):
            path =  os.path.dirname(self.Write_node.knob('file').value())
            self.OpenFileOrFolder(path)

    def Copy_To_ClipBoard_Directory(self):
        txt = os.path.dirname(self.Write_node.knob('file').value())
        self.Copy_To_ClipBoard(txt)

    def Copy_To_ClipBoard_File(self):
        txt = self.Write_node.knob('file').getEvaluatedValue()
        self.Copy_To_ClipBoard(txt)

    def Open_Render_File(self):
        filePath = self.Write_node.knob('file').getEvaluatedValue()
        self.OpenFileOrFolder(filePath)

    def OpenFileOrFolder(self,path):
        operatingSystem = platform.system()
        if os.path.exists(path):
            if operatingSystem == "Windows":
                os.startfile(path)
            elif operatingSystem == "Darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])

    def Copy_To_ClipBoard(self,txt) :
        # copy text to clipboard using pyside library , works for both windows & linux
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard )
        cb.setText(txt, mode=cb.Clipboard)

    def CreateReadNode(self):
        filePath = self.Write_node.knob('file').value()

        if filePath == self.Write_node.knob('file').getEvaluatedValue() : # check if it's sequence
            isSequence = False
        else:
            isSequence = True

        readNode = nuke.createNode("Read")
        if isSequence : # using v!ctor tools code(by Victor Perez ) for creating read node for sequence . https://www.nukepedia.com/gizmos/image/vctor-tools
            i = self.Write_node
            fileName = i.knob('file').value()
            readNode.knob('file').setValue(fileName)
            cleanPath = nukescripts.replaceHashes(fileName) 
            padRE = re.compile('%0(\d+)d') 
            padMatch = padRE.search(cleanPath)         
            if padMatch: 
                padSize = int(padMatch.group(1)) 
                frameList = sorted(glob.iglob(padRE.sub('[0-9]' * padSize, cleanPath))) 
                first = os.path.splitext(frameList[0])[0][-padSize:] 
                last = os.path.splitext(frameList[-1])[0][-padSize:] 
                if platform.system() == "Windows":
                    readNode['file'].fromUserText('%s %s-%s' % (cleanPath, first, last))
                else : # for linux
                    readNode['file'].fromUserText(cleanPath)
                    readNode['first'].setValue(int(nuke.root()["first_frame"].getValue())) # code above doesn't work properly for linux so we set first & last from project
                    readNode['last'].setValue(int(nuke.root()["last_frame"].getValue()))
                    readNode['origfirst'].setValue(int(nuke.root()["first_frame"].getValue()))
                    readNode['origlast'].setValue(int(nuke.root()["last_frame"].getValue()))
        else : # if it's not seq 
            readNode.knob('file').fromUserText(filePath)
            projectStartFrame = nuke.root()["first_frame"].getValue()
            readNode.knob('frame').setValue(str(projectStartFrame))
            readNode.knob('frame_mode').setValue("start at")
        # set position
        readNode.setXpos(self.Write_node.xpos())
        readNode.setYpos(self.Write_node.ypos() + self.Write_node.screenHeight() + 50)
        notif_panel.activateWindow() # just to be sure it's on top 
        notif_panel.raise_() # just to be sure it's on top 

        
    @staticmethod
    def Set_Render_Start_Time():
        if not nuke.root().knob("Km_Render_Start_Time"):
            nuke.root().addKnob(nuke.EvalString_Knob("Km_Render_Start_Time"))
            nuke.root().knob("Km_Render_Start_Time").setVisible(False)

        Current_time_str = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        nuke.root().knob("Km_Render_Start_Time").setValue(Current_time_str)
        
    def Get_Time_Duration(self):
        time1_str = nuke.root().knob("Km_Render_Start_Time").getValue()
        time1 = datetime.datetime.strptime(time1_str, '%Y-%m-%d %H:%M:%S') # time1_str sample : '2021-11-20 12:33:00'
        time2 = datetime.datetime.now()
        duration  = time2 - time1
        duration_in_s = duration.total_seconds()
        days    = divmod(duration_in_s, 86400)        # Get days (without [0]!)
        hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
        minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
        seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
        #print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0])) # Sample Result: Time between dates: 1 days, 8 hours, 34 minutes and 7 seconds
        h,m,s = "","",""
        if (hours[0] < 10) : 
            h = "0"+str(int(hours[0]))
        else:
            h = str(int(hours[0]))
        if (minutes[0] < 10) : 
            m = "0"+str(int(minutes[0])) 
        else:
            m = str(int(minutes[0])) 
        if (seconds[0] < 10) : 
            s = "0"+str(int(seconds[0])) 
        else:
            s = str(int(seconds[0])) 

        render_time = h+":"+m+":"+s
       
        #self.ui.label_render_time.setToolTip("Started at : "+time1_str+", Finished at :"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        return render_time

    def Get_Script_Name(self):
        return os.path.basename(nuke.root().name())


def Create_Show_Notif_Panel():
    global notif_panel
    notif_panel = Km_Notification_Panel(nuke.thisNode())
    notif_panel.show()
    notif_panel.activateWindow() # just to be sure it's on top 
    notif_panel.raise_() # just to be sure it's on top 


# add nuke callbacks
nuke.addBeforeRender(Km_Notification_Panel.Set_Render_Start_Time)
nuke.addAfterRender(Create_Show_Notif_Panel)






