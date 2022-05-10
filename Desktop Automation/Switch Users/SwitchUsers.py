from pywinauto.application import Application
import mouse
import time
""""
#Open the mouse settings application and connect to the window that opens
openMouse = Application(backend="uia").start('C:\Program Files (x86)\Glorious Model O Software\OemDrv.exe')#.connect(title='Glorious Model O Software', timeout=3)
#openMouse.GloriousModelOSoftware.print_control_identifiers()

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
"""

#Open discord and connect to the window that opens
discord = Application(backend="uia").start(r"C:\Users\pacow\AppData\Local\DiscordPTB\app-1.0.1013\DiscordPTB.exe")#.connect(title = 'Discord', timeout=10)
#discord.window(best_match='Discord').print_control_identifiers()

#Move mouse to switch profiles
mouse.move(109, 1007, True, 0)
mouse.click(button='left')
mouse.move(175, 947, True, 0)
mouse.click(button='left')
mouse.move(1068, 503, True, 0)
time.sleep(1)
mouse.click(button='left')

#Move and click on the close window button
mouse.move(1904, 12, True, 0)
mouse.click(button='left')
