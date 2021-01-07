import webbrowser
import pyautogui as gui # pip install pyautogui
import time
import random

gui.FAILSAFE = False
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
	headerSize = 75
	sleepyTime = 1 * random.randint(0,10) # seconds
	print("Mouse move  - initial position")
	gui.moveTo(1, 1, 0.45)
	print("waiting for " + str(sleepyTime) + " seconds" )
	time.sleep(sleepyTime)
	print("Mouse move - green dot area")
	gui.moveTo(40, 400 + headerSize, 0.5)
	gui.moveTo(41, 403 + headerSize, 0.1)
	gui.moveTo(38, 399 + headerSize, 0.3)
	gui.moveTo(42, 402 + headerSize, 0.25)
	print("Mouse move  - initial position")
	gui.moveTo(1, 1, 1)

print("init mouse move loop")
while True:
    sleepyTime = 1 * 60 * random.randint(0,19) # minutes
    print("Mouse move call")
    moveMouse()
   
    print("waiting for " + str(sleepyTime) + " seconds" )
    time.sleep(sleepyTime)