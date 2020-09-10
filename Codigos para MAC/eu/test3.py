import pyautogui
import pyperclip
import time

#cambiar pass

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,24): #tab hasta llegar a detalles de cuenta
	pyautogui.press('tab') 

pyautogui.press('enter')


time.sleep(7)

for i in range(0,30): #tab hasta llegar a input para cambiar pass
	pyautogui.press('tab')

pyperclip.copy("passblopez")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyperclip.copy("passblopez2")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyperclip.copy("passblopez2")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyautogui.press('enter') #cambiar pass