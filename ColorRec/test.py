import pyautogui 
import time

print(pyautogui.displayMousePosition())
time.sleep(0.2)

screen_width, screen_height = pyautogui.size() #1920 1080
print(screen_width, screen_height)