import pyautogui
import pyperclip
import time

#Inicio de sesion

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,9): #tab hasta llegar a iniciar sesion
	pyautogui.press('tab')

pyautogui.press('enter')


time.sleep(7)

pyperclip.copy("userblopez") #ingreso de datos de la cuenta
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyperclip.copy("passblopez")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyautogui.press('enter') #entrar