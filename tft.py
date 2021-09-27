import pyautogui
import time


temp = True
while temp:
    currentMouseX, currentMouseY = pyautogui.position()
    time.sleep(1)
    print(currentMouseX)
    print(currentMouseY)

    time.sleep(3)
    pyautogui.write("/ff", .25)
    pyautogui.press('enter')

    temp = False

    #code words, praise baal