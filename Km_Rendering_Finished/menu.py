import nuke


if int(nuke.env ["NukeVersionMajor"]) >= 11:
    import Km_RF
    menu = nuke.menu("Nuke")
    Km_Tools_menu = menu.addMenu("KmTools")
    Km_Tools_menu.addCommand("Km Rendering Finished","nuke.message('This tool pop up a Notification with some tools after a render finished \\n Km Rendering Finished v1.0.1')","")
