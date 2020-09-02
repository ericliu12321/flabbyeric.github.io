import pyautogui, threading, time

def x():
    pyautogui.moveRel(1,1)

while 1:
    timer = threading.Timer(600, x)
    timer.start()
    time.sleep(600)
