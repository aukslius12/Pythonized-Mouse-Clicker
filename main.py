import os
import pyautogui
import time
import pywinauto

def get_settings():
    settings_txt = open(os.getcwd() + "\\settings.txt", "r")
    temp = settings_txt.read()
    settings_txt.close()
    temp = temp.split(sep=",")
    return (temp)

def open_website(path, webpage = "www.google.com"):
        os.system(path + " %s %s" % ("-incognito", webpage))

def click_button(scroll_amount, x_pos, y_pos, close = "True"):
    time.sleep(5)
    pyautogui.moveTo(1904, 169)
    pyautogui.scroll(scroll_amount)
    time.sleep(1)
    pyautogui.click(x_pos, y_pos)
    time.sleep(1)
    if close == "True":
        pywinauto.keyboard.SendKeys('%{F4}')


settings_txt = get_settings()
open_website(path=settings_txt[0], webpage=settings_txt[1])
click_button(scroll_amount=int(settings_txt[2]), x_pos=int(settings_txt[3]), y_pos=int(settings_txt[4]), close=settings_txt[5])
