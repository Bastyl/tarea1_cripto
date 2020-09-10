import pyautogui
import pyperclip
import time

#cambiar pass

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,33): #tab hasta llegar a "cambio de contrasena"
	pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(5)	#espera para que cargue la pagina

for i in range(0,32): #tab hasta llegar a pass vieja
	pyautogui.press('tab')

pyperclip.copy("passblopez")
pyautogui.hotkey("command", "v")

pyautogui.press('tab')

pyperclip.copy("password2")
pyautogui.hotkey("command", "v")

pyautogui.press('tab')

pyperclip.copy("password2")
pyautogui.hotkey("command", "v")

pyautogui.press('tab')

pyautogui.press('enter') #cambiar pass