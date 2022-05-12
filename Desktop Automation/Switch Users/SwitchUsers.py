from pywinauto.application import Application
import mouse
import time


#Open the mouse settings application and connect to the window that opens
openMouse = Application(backend="uia").start('C:\Program Files (x86)\Glorious Model O Software\OemDrv.exe')#.connect(title='Glorious Model O Software', timeout=3)
#openMouse.GloriousModelOSoftware.print_control_identifiers()

#GLORIOUS O MODEL
#Move mouse to profiles button
mouse.move(582, 737, True, 0)
time.sleep(1)
mouse.click(button='left')
#Select my profile
mouse.move(582, 767, True, 0)
mouse.click(button='left')
#Apply changes
mouse.move(1380, 822, True, 0)
time.sleep(1)
mouse.click(button='left')
#Wait for changes to be applied
time.sleep(2)
#Close the window
mouse.move(1435, 227, True, 0)
#time.sleep(1)
mouse.click(button='left')

#Open discord
app = Application(backend="uia").start(r"C:\Users\pacow\AppData\Local\DiscordPTB\app-1.0.1013\DiscordPTB.exe")#.connect(title = 'Discord', timeout=10)
#discord.window(best_match='Discord').print_control_identifiers()

#wait for Discord to finish loading page
time.sleep(5)

#DISCORD
#Open profiles list
mouse.move(109, 1007, True, 0)
mouse.click(button='left')
#Click on 'Switch Accounts'
mouse.move(175, 947, True, 0)
mouse.click(button='left')
#Let list of profiles load
time.sleep(1)
#Switch account to my profile
mouse.move(1068, 503, True, 0)
mouse.click(button='left')
#Let my profile load for discord
time.sleep(2)

#Move mouse to switch mic settings
#Click on settings
mouse.move(314, 1012, True, 0)
mouse.click()
#Let settings load
time.sleep(1)
#Click on 'Voice & Video'
mouse.move(477, 681, True, 0)
mouse.click()
#Open list of input devices
mouse.move(966, 184, True, 0)
mouse.click()
#Select XIBERIA
mouse.move(857, 368, True, 0)
mouse.click()
#Close settings window
mouse.move(1471, 109, True, 0)
mouse.click()
#Close the Discord window
mouse.move(1904, 12, True, 0)
mouse.click()

#Close Discord background process
app2 = Application(backend="uia").connect(path="explorer.exe")
sys_tray = app2.window(class_name="Shell_TrayWnd")
hidden_tray_button = sys_tray.child_window(title="Notification Chevron").wrapper_object()
hidden_tray_button.click()

notifyWindow = Application().connect(best_match="NotificationOverflow")

list_box = Application(backend="uia").connect(class_name="NotifyIconOverflowWindow")
list_box_win = list_box.window(class_name="NotifyIconOverflowWindow")

Discord = list_box_win.child_window(title="DiscordPtb")
if Discord.exists():
    Discord.wrapper_object().right_click_input()
    time.sleep(1)
    mouse.move(50, -15, False, 0)
    mouse.click()

#Format to add more background processes to close
# time.sleep(1)
# hidden_tray_button.click()

# Name = list_box_win.child_window(title="NAME")
# if Name.exists():
#     Name.wrapper_object().right_click_input() #Open submenu
#     time.sleep(1)
#     mouse.move(50, -15, False, 0) #Move to exit/close button
#     mouse.click() #Click on exit/close button


#TODO: #5 Open Chrome window and select my user profile
