import pyautogui
import pyperclip


#creacion de usuario

pyautogui.click()  #click para poner como ventana principal a la web (estaba en terminal)

for i in range(0,24): #tab hasta llegar a login
	pyautogui.press('tab')

pyperclip.copy("userblopez")  #input usuario
pyautogui.hotkey("command", "v")

pyautogui.press('tab') #tab para pasar a siguiente input

pyperclip.copy("passblopez")
pyautogui.hotkey("command", "v")

pyautogui.press('tab')

pyperclip.copy("passblopez")
pyautogui.hotkey("command", "v")

pyautogui.press('tab')

pyperclip.copy("bastian.lopez@mail.udp.cl")
pyautogui.hotkey("command", "v")

pyautogui.press('tab')
pyautogui.press('tab')

pyautogui.press('enter') #click boton


