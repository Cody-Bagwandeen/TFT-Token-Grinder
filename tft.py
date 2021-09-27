import pyautogui
import time

def surrender():
    pyautogui.press('enter')
    pyautogui.write("/ff", .25)
    pyautogui.press('enter')

def startQueue():
    QueueX, QueueY = pyautogui.locateCenterOnScreen('find_match.png')
    pyautogui.moveTo(QueueX,QueueY)
    pyautogui.click()


temp = True
while temp:
    time.sleep(5)
    startQueue()
    

    temp = False

    #code words, praise baal

