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
	headerSize = 50
	sleepyTime = 1 * random.randint(0,10) # seconds
	print("Mouse move  - initial position")
	gui.moveTo(1, 1, random.randint(0, 3))
	print("waiting for " + str(sleepyTime) + " seconds" )
	time.sleep(sleepyTime)
	print("Mouse move - green dot area")
	for x in range(12):
		gui.moveTo(random.randint(35, 50), random.randint(390, 425) + headerSize, random.randint(0, 2))
		time.sleep(random.randint(0, 2))
	print("Mouse move  - random position")
	gui.moveTo(random.randint(0, 300), random.randint(0, 300), random.randint(0, 3))

print("init mouse move loop")
while True:
    sleepyTime = 1 * 60 * random.randint(0,19) # minutes
    print("Mouse move call")
    moveMouse()
   
    print("waiting for " + str(sleepyTime) + " seconds" )
    time.sleep(sleepyTime)