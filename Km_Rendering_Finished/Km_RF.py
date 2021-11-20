#print(nuke.selectedNode()["file"].getValue())

import nuke
import os
import platform
import subprocess

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
    
nuke.addAfterRender(Open_Render_File)