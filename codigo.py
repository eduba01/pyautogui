
# pip install PyAutoGUI
# pip install pandas numpy openpyxl

import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)

pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=437, y=385)

pyautogui.write("e-mail.com")

pyautogui.press("tab")

pyautogui.write("123456")

pyautogui.press("tab")

pyautogui.click




