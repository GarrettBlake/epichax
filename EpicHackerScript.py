import pyautogui
import time

pyautogui.press("win")
pyautogui.typewrite("notepad")
pyautogui.press("enter")
time.sleep(.5)

pyautogui.typewrite("Hello")
time.sleep(1)
pyautogui.typewrite(".")
time.sleep(.1)
pyautogui.typewrite(".")
time.sleep(.1)
pyautogui.typewrite(".")
time.sleep(.1)
pyautogui.press("enter")
time.sleep(.5)

pyautogui.typewrite("I seeee you...")
pyautogui.press("enter")

time.sleep(1)
pyautogui.typewrite("You've been hacked.")
pyautogui.press("enter")


i = 0 
while i <10:
	i+=1
	pyautogui.typewrite("#EXPOSED")
	pyautogui.press("enter")


pyautogui.press("win")
pyautogui.typewrite("cmd")
pyautogui.press("enter")
time.sleep(.5)

pyautogui.typewrite("start firefox")
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite("https://hackertyper.net/")
pyautogui.press("enter")
pyautogui.hotkey('f11')
time.sleep(2)

y = 0
while y <100:
	y+=1
	pyautogui.press("enter")




