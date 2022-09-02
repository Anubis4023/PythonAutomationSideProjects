from pywinauto.application import Application
import time
import os


#Open Valorant by clicking on the shortcut in the taskbar
openVal = Application(backend="uia").connect(path="explorer.exe")
sys_tray = openVal.window(class_name="Shell_TrayWnd")
sys_tray.child_window(title="VALORANT").click()

#Connect to the Valorant page opened
Valorant = Application(backend="uia").connect(title='Riot Client Main',timeout=20)
#Valorant.RiotClientMain.print_control_identifiers()

#Login information
username = Valorant.RiotClientMain.child_window(title="USERNAME", auto_id="username", control_type="Edit").wrapper_object()
username.set_edit_text(os.environ.get("Valorant Username"))
password = Valorant.RiotClientMain.child_window(title="PASSWORD", auto_id="password", control_type="Edit").wrapper_object()
password.set_edit_text(os.environ.get("Valorant Password"))

#Click the sign in button
SignIn = Valorant.RiotClientMain.child_window(title="Sign in", control_type="Button").wrapper_object()
SignIn.click()

#Wait until "Play" button appears and click on it (Valorant may need updating, so "Play" button won't always appear at the start)
Valorant.RiotClientMain.child_window(title="Play", control_type="Button").wait('visible')
Play = Valorant.RiotClientMain.child_window(title="Play", control_type="Button").wrapper_object()
Play.click()
