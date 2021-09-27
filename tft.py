from os import putenv
import pyautogui
import time

def findMouse():
    while True:
        CurrentX, CurrentY = pyautogui.position()
        print(CurrentX,CurrentY)


def surrender():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('f')
    pyautogui.keyUp('ctrlleft')
    time.sleep(1)

    pyautogui.click(835,487)
    time.sleep(10)


def startQueue():
    time.sleep(3)
    QueueX, QueueY = pyautogui.locateCenterOnScreen('find_match.png')
    pyautogui.moveTo(QueueX, QueueY)
    pyautogui.click()


def acceptQueue():
    inQueue = True
    pyautogui.moveTo(984, 776)
    while inQueue:
        time.sleep(9)
        pyautogui.click()
        print('just clicked')
        if(pyautogui.locateCenterOnScreen('in_game_checker.png') != None):
            print('now in game')
            inQueue = False    
        
def levelUp():
    pyautogui.click()

def buy():
    pyautogui.click()

def inGame():
    time.sleep(10 * 60)
    surrender()

def inGame2():
    playing = True
    while playing:
        levelUp()
        buy()


def reQueue():
    reQueueX, reQueueY = pyautogui.locateCenterOnScreen('play_again.png')
    pyautogui.moveTo(reQueueX,reQueueY)
    pyautogui.click()
    time.sleep(5)
    
print('Enter how many games you want to grind ')
games = int(input())

for x in range(games) :
    startQueue()
    acceptQueue()
    inGame()
    reQueue() 
    # praying to baal

