import pyautogui
import pyperclip
import time

#creacion de usuario

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,9): #tab hasta llegar a login
	pyautogui.press('tab')

pyautogui.press('enter')


time.sleep(7)

for i in range(0,4):
	pyautogui.press('tab') #tab hasta llegar crear usuario

pyautogui.press('enter')

time.sleep(5)

#ingreso de datos para la cuenta
pyperclip.copy("bastian")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyperclip.copy("alejandro")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyperclip.copy("bastian.lopez@mail.udp.cl")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

for i in range(0,3):
	pyautogui.press('tab')

pyperclip.copy("userblopez")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyperclip.copy("passblopez")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyperclip.copy("passblopez")
pyautogui.hotkey("command", "v")
pyautogui.press('tab')

pyautogui.press('enter') #crear usuario
