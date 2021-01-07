import webbrowser
import pyautogui as gui # pip install pyautogui
import time
import random

random.seed()


#Change to your gmail acct url
url = 'https://mail.google.com/mail/u/2/#inbox'

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'


print("Opening chrome")
webbrowser.get(chrome_path).open(url)
print("waiting 10 seconds for chrome to load")
time.sleep(1 * 10)

def moveMouse():
    sleepyTime = 1
    print("Mouse move 1")
    gui.moveTo(100, 200, 0.25)
    print("waiting for " + str(sleepyTime) + " seconds" )
    time.sleep(sleepyTime)
    gui.moveTo(200, 100, 0.25)
    print("Mouse move 2")

print("init mouse move loop")
while True:
    sleepyTime = 1 * 60 * random.randint(0,27)
    print("Mouse move call")
    moveMouse()
   
    print("waiting for " + str(sleepyTime) + " seconds" )
    time.sleep(sleepyTime)