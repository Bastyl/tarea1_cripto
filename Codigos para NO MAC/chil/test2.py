import pyautogui
import pyperclip

#INICIAR SESION

pyautogui.click() #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,12):  #tab hasta llegar a login
	pyautogui.press('tab')

pyperclip.copy("userblopez")
pyautogui.hotkey("ctrl", "v")

pyautogui.press('tab')

pyperclip.copy("passblopez")
pyautogui.hotkey("ctrl", "v")

pyautogui.press('tab')

pyautogui.press('enter') #logear

