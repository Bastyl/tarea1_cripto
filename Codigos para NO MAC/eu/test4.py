import pyautogui
import pyperclip
import time

#recuperar pass

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,9): #tab hasta llegar a forgoten pass
	pyautogui.press('tab')

pyautogui.press('enter')


time.sleep(7)


for i in range(0,3):
	pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(10)

pyperclip.copy("bastian.lopez@mail.udp.cl") #ingresa mail
pyautogui.hotkey("ctrl", "v")

pyautogui.press('tab')

pyautogui.press('enter')


time.sleep(10)

""" Automatizacion reestablecer 10 veces la pass
for i in range(0,10):
	pyperclip.copy("bastian.lopez@mail.udp.cl")
	pyautogui.hotkey("ctrl", "v")

	pyautogui.press('tab')

	pyautogui.press('enter')

	time.sleep(10)
"""

