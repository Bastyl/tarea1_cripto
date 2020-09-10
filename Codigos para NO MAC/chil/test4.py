import pyautogui
import pyperclip
import time

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,15): #tab hasta llegar a pass olvidada
	pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(5)

for i in range(0,24): #tab hasta llegar al input para el mail
	pyautogui.press('tab')

pyperclip.copy("bastian.lopez@mail.udp.cl")
pyautogui.hotkey("ctrl", "v")

pyautogui.press('tab')
pyautogui.press('enter')