import time
import pyautogui

def take_screenshot():

#when we run the screenshot the image ovewrites the former one so to 
#correct this we 

    name = int(round(time.time() * 1000))  # Use current timestamp as filename 
    name = 'C:/Users/Dev Marsh/Desktop/python/screenshots/{}.png'.format(name)   
    time.sleep(5)  # Wait for 5 seconds before taking the screenshot
    screenshot = pyautogui.screenshot(name)
    screenshot.show()

take_screenshot()