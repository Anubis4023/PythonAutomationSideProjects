from pywinauto.application import Application
import mouse
import time

#Open the mouse settings application and connect to the window that opens
openVal = Application(backend="uia").start('C:\Program Files (x86)\Glorious Model O Software\OemDrv.exe').connect(title='Glorious Model O Software', timeout=3)
#openVal.GloriousModelOSoftware.print_control_identifiers()

#Move mouse to profiles button
mouse.move(582, 737, True, 0)
mouse.click(button='left')
#Select my profile
mouse.move(582, 767, True, 0)
mouse.click(button='left')
#Apply changes
mouse.move(1380, 822, True, 0)
mouse.click(button='left')
#Close the window
mouse.move(1426, 227, True, 0)
time.sleep(1)
mouse.click(button='left')


#Open discord 
