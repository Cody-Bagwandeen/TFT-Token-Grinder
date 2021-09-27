import pyautogui
import time

def surrender():
    pyautogui.press('enter')
    pyautogui.write("/ff", .25)
    pyautogui.press('enter')

def startQueue():
    QueueX, QueueY = pyautogui.locateCenterOnScreen('')
    pyautogui.moveTo(QueueX,QueueY)
    pyautogui.click()


temp = True
while temp:
    currentMouseX, currentMouseY = pyautogui.position()
    print(pyautogui.size())
    time.sleep(1)
    print(currentMouseX)
    print(currentMouseY)

    time.sleep(3)
    surrender()
    

    temp = False

    #code words, praise baal

