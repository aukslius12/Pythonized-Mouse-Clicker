import os
from os.path import join
import pyautogui
import time
import tkinter
from tkinter import simpledialog
from tkinter import messagebox
import win32gui

def find_chrome_path():
    lookfor = "chrome.exe"
    for root, dirs, files in os.walk('C:\\'):
        if lookfor in files:
            chrome_path = join(root, lookfor)
            break
    return(chrome_path)

def open_website(chrome_path, webpage="www.google.com"):
    os.system(chrome_path + " %s %s" % ("-incognito", webpage))
    time.sleep(5)
    pyautogui.click(1904, 169)
    pyautogui.scroll(-1000)

def get_settings():
    root = tkinter.Tk()
    root.withdraw()
    website = simpledialog.askstring(title="Website", prompt="Enter your website adress:")
    chrome_path = find_chrome_path()
    return(chrome_path, website)

def save_calibration_data(chrome_path, webpage, scroll_amount, x_pos, y_pos, if_close):
    settings_txt = open(os.getcwd() + "\\settings.txt", "w")
    settings_txt.write(chrome_path + "," + webpage + "," + scroll_amount.__str__() + "," + x_pos.__str__() + ","+ y_pos.__str__() + "," + if_close)
    settings_txt.close()

def calibrate():
    sett = get_settings()
    open_website(chrome_path = sett[0], webpage = sett[1])
    scroll_amount = -1000
    visibility = messagebox.askyesno("",  "Do you see your button on the website?")
    if visibility == False:
        while (visibility == False):
            pyautogui.moveTo(1904, 169)
            pyautogui.scroll(-1000)
            scroll_amount = scroll_amount - 1000
            visibility = messagebox.askyesno("", "How about now?")
    messagebox.askokcancel("", "Hover your mouse over your button and press Enter to continue.")
    mouse_coords = win32gui.GetCursorInfo()[2]
    if_close = str(messagebox.askyesno(title="", message="Would you like to close the website after voting?"))
    messagebox.askokcancel("", "Calibration successful!")
    save_calibration_data(sett[0], sett[1], scroll_amount, mouse_coords[0], mouse_coords[1], if_close)

calibrate()
