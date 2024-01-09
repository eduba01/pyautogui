
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

time.sleep(3)

pyautogui.click(x=437, y=381)

pyautogui.write("e-mail.com")

pyautogui.press("tab")

pyautogui.write("123456")

pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(2)

tabela = pandas.read_csv("./dados/produtos.csv")

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=536, y=250)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")






