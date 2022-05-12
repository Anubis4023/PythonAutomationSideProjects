
from pywinauto import Desktop
from pywinauto.application import Application
import time
import mouse

openVal = Application(backend="uia").connect(path="explorer.exe")
sys_tray = openVal.window(class_name="Shell_TrayWnd")
hidden_tray_button = sys_tray.child_window(title="Notification Chevron").wrapper_object()
hidden_tray_button.click_input()

app = Application().connect(best_match="NotificationOverflow")

list_box = Application(backend="uia").connect(class_name="NotifyIconOverflowWindow")
list_box_win = list_box.window(class_name="NotifyIconOverflowWindow")

Steam = list_box_win.child_window(title="Steam")
if Steam.exists():
    Steam.wrapper_object().click_input()
    time.sleep(1)
    mouse.move(-220, -20, False, 0)
    mouse.click()

time.sleep(1)
hidden_tray_button.click()

Discord = list_box_win.child_window(title="DiscordPtb")
if Discord.exists():
    Discord.wrapper_object().right_click_input()
    time.sleep(1)
    mouse.move(50, -15, False, 0)
    mouse.click()

#TODO: #2 Add more code that closes the other background running processes
