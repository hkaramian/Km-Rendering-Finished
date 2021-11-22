import nuke
import os
import sys
import platform
import subprocess
import datetime


################################################################################
## ui_notif_panel.py changes needed for new version from qt designer : 
## remove import files_rc
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
        
        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
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

        
        # Set Signals
        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.label_icon_success.mousePressEvent = self.close_notif_panel
        self.ui.pushButton_2.clicked.connect(self.Open_Render_Directory)
        self.ui.pushButton_3.clicked.connect(self.Open_Render_File)
        self.ui.pushButton_clipboard_directory.clicked.connect(self.Copy_To_ClipBoard_Directory)
        self.ui.pushButton_clipboard_file.clicked.connect(self.Copy_To_ClipBoard_File)

        # render time
        #self.ui.label_render_time.setText(" Render Time (H:M:S) :  "+self.Get_Time_Duration())
        self.ui.label_render_time.setText("<strong>Render Time (H:M:S) :  "+self.Get_Time_Duration()+"</strong>")

        # credit
        self.ui.label__Hossein.setText('''<a href='http://www.kmworks.ir' style='color: rgb(166, 166, 166);text-decoration: none;'><strong>By Hossein Karamian</strong></a>''')
        self.ui.label__Hossein.setOpenExternalLinks(True)


        # set project name lable
        self.ui.label_project_name.setText("<strong>"+os.path.basename(nuke.root().name())+"</strong>")
        
        self.show()

    # def enterEvent(self, event): 
    #     self.op_effect.setOpacity(1)

    # def leaveEvent(self, event):  
    #     self.op_effect.setOpacity(self.opacity_value)

    def close_notif_panel(self,aaa):
        #self.close()
        return

    def Open_Render_Directory(self):
            path =  os.path.dirname(self.Write_node.knob('file').value())
            operatingSystem = platform.system()
            if os.path.exists(path):
        
                if operatingSystem == "Windows":
                    os.startfile(path)
                elif operatingSystem == "Darwin":
                    subprocess.Popen(["open", path])
                else:
                    subprocess.Popen(["xdg-open", path])

    def Open_Render_File(self):
            r_file =  self.Write_node.knob('file').value()
            os.startfile(r_file)

    def Copy_To_ClipBoard_Directory(self):
        txt = os.path.dirname(self.Write_node.knob('file').value())
        cmd='echo '+txt.strip()+'|clip'
        return subprocess.check_call(cmd, shell=True)

    def Copy_To_ClipBoard_File(self):
        txt = self.Write_node.knob('file').value()
        cmd='echo '+txt.strip()+'|clip'
        return subprocess.check_call(cmd, shell=True)

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
       
        self.ui.label_render_time.setToolTip("Started at : "+time1_str+", Finished at :"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        return render_time

    def Get_Script_Name(self):
        return os.path.basename(nuke.root().name())


def Create_Show_Notif_Panel():
    notif_panel = Km_Notification_Panel(nuke.thisNode())
    notif_panel.show()


# add nuke callbacks
nuke.addBeforeRender(Km_Notification_Panel.Set_Render_Start_Time)
nuke.addAfterRender(Create_Show_Notif_Panel)






