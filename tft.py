from os import putenv
import pyautogui
import time


def surrender():
    print('about to type /ff')
    pyautogui.press('enter')
    pyautogui.press('/')
    pyautogui.press('f')
    pyautogui.press('f')
    pyautogui.press('enter')
    print('typed /ff')

    print('about to press q 6 times')
    for index in range(6):
        pyautogui.press('q')
        time.sleep(0.25)
    print('finished pressing')


def startQueue():
    time.sleep(3)
    QueueX, QueueY = pyautogui.locateCenterOnScreen('find_match.png')
    pyautogui.moveTo(QueueX, QueueY)
    pyautogui.click()


def acceptQueue():
    inQueue = True
    pyautogui.moveTo(984, 776)
    while inQueue:
        time.sleep(4)
        pyautogui.click()
        print('just clicked')
        if(pyautogui.locateCenterOnScreen('in_game_checker.png') != None):
            print('now in game')
            inQueue = False    
        

def InGame():
    print('meow')


def reQueue():
    reQueueX, reQueueY = pyautogui.locateCenterOnScreen('play_again.png')
    pyautogui.moveTo(reQueueX,reQueueY)
    pyautogui.click()
    time.sleep(5)
    




temp = True
while temp:
    time.sleep(2)

    startQueue()
    acceptQueue()
    #reQueue()
    #startQueue()
    

    

    temp = False

    # code words, praise baal

