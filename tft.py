import pyautogui
import time



while True:
    currentMouseX, currentMouseY = pyautogui.position()
    time.sleep(1)
    print(currentMouseX)
    print(currentMouseY)

    #code words, praise baal