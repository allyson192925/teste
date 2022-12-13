# -----------------------------------------------------------#
import sys
from pyautogui import locateOnScreen, hotkey, write, moveTo
from time import sleep
# -----------------------------------------------------------#

# -----------------------------------------------------------#

sleep(2)
hotkey('enter')
sleep(1)
import pyperclip
pyperclip.copy(fr'$_Py_Path_Pai_Print$\$_Nome_Arquivo_PDF$.pdf')
sleep(.3)
pyperclip.copy(fr'$_Py_Path_Pai_Print$\$_Nome_Arquivo_PDF$.pdf')
sleep(.3)
hotkey("ctrl", "v")
sleep(.3)
hotkey('enter')
moveTo(1, 1)
