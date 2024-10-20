from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from PIL import Image
from pywinauto.application import Application
import time

chosen_block = 'ice'
chosen_head_left = 'face_left'
chosen_head_right = 'face_right'
x_min = 250
x_max = 1920
y_min = 350
y_max = 750

class block:
    def __init__(self, image): 
        self.image = image

    def identify_block(self):
     search_region = (x_min, y_min, x_max - x_min, y_max - y_min)

     try:
          location = pyautogui.locateOnScreen(f'{self.image}.png', region=search_region, confidence=0.8)


          if location is not None:
            time.sleep(0.5)
            return True
        
        
          time.sleep(0.5)
          return False
        
     except Exception as e:
        print(f"Block not found: {e}")
        return False
     
    def locate_block(self):
     try:
        search_region = (x_min, y_min, x_max - x_min, y_max - y_min)
        location = pyautogui.locateOnScreen(f'{self.image}.png', region=search_region, confidence=0.9)

        if location is not None:
            left, top, width, height = location
            #print(f"Located {self.image} at {left}, {top}, {width}, {height}")
            return left, top, width, height
        else:
            print(f"{self.image} not found in the region.")
            return 0, 0, 0, 0

     except Exception as e:
        #print(f"Error locating {self.image}: {e}")
        return 0, 0, 0, 0


    def cursor_on_block(self, offset_x, offset_y):
       location = self.locate_block()
       left, top, width, height = location
       located_x = int(int(left) + int(width)/2)
       located_y = int(int(top)  + int(height)/2)
       win32api.SetCursorPos((located_x + offset_x, located_y + offset_y)) 

    def click_on(self, offset_x, offset_y, times):
       mouse = self.cursor_on_block(offset_x, offset_y)
       win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
       time.sleep(times)  # Small delay to simulate a click
       win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)







def click(x, y, times): # 1675 870 punch 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(times)  # Small delay to simulate a click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
def rand():
   randomize = random.randint(1, 10) * 0.000001
   return round(randomize, 4)
   return randomize

def switch_to_app(window_title):
    try:
        app = Application().connect(title_re=window_title)
        app.window(title_re=window_title).set_focus()
        print(f"Switched to {window_title}")
    except Exception as e:
        print(f"Failed to switch to {window_title}: {e}")
    
def left(times):
    keyboard.press('left')
    time.sleep(times) 
    keyboard.release('left')

def right(times):
    keyboard.press('right')
    time.sleep(times)  
    keyboard.release('right')


switch_to_app("BlueStacks App Player")
time.sleep(0.1)

""" 
2 Punches: Takes about 0.4 - 0.6 seconds.
3 Punches: Takes about 1.1       seconds.
4 Punches: Takes about 0.8 - 1.2 seconds.
5 Punches: Takes about 1.0 - 1.5 seconds.
 """

breaker = 0
blockStrength = 1.1
offset = 0
while keyboard.is_pressed('q') == False:
  blockBust = block(chosen_block)
  headBust_left = block(chosen_head_left)
  headBust_right = block(chosen_head_right)

  #1087 1156 suppose to be 99 between block and face
  xPosBlock = int(blockBust.locate_block()[0]) + offset
  yPosBlock = int(blockBust.locate_block()[1])

  xPosHead_right = headBust_right.locate_block()[0]
  yPosHead_right = headBust_right.locate_block()[1]

  xPosHead_left = headBust_left.locate_block()[0]
  yPosHead_left = headBust_left.locate_block()[1]

  print(xPosHead_left, xPosHead_right, xPosBlock)
#_________________________________________________________
#stop if nothing is visable
  if xPosHead_right == 0 and xPosHead_left == 0 and xPosBlock == 0: 
       print(xPosHead_left, xPosHead_right, xPosBlock)
       print("Can't locate image on screen")
       time.sleep(3)


#_________________________________________________________
    #base case if hit x-wall x_max
  elif xPosHead_right >= 1760:
     breaker == 0 
     print('Xx')
     left(0.244 + rand())
     time.sleep(0.5)
     headBust_left.cursor_on_block(0,0)
     time.sleep(0.001 + rand())

     x,y = pyautogui.position()
     click(x+50, y, 0.3+rand())
     time.sleep(0.001+ rand())
     click(x+100, y, 0.3+rand())

     time.sleep(2.5 + rand())  


#_________________________________________________________
  #destroy blocks 
  # -1091 + 1274 = 1
  elif breaker >= 1: 
      if 0 > xPosBlock - xPosHead_left or 0 > xPosBlock - xPosHead_right :
         left(0.25+ rand())
         time.sleep(0.001 + rand())
      
      elif 0 < xPosBlock - xPosHead_left  <= 170 or 0 < xPosBlock - xPosHead_right <= 170:
         right(0.03 + rand())
         time.sleep(0.001 + rand())
         click(1675, 870, blockStrength*2.2 + rand())
         time.sleep(0.001 + rand())
      else:
        right(0.25 + rand())
        time.sleep(0.001 + rand())

  # initiate a break / breaker   
  elif 10 <= xPosHead_right <= 360 or 10 <=  xPosHead_left <= 360: 
     breaker +=1 
    

#_________________________________________________________
   #place blocks
   #distans between right_head and block == 1717 - 1574
  else:   
    print(xPosBlock, xPosHead_right, xPosHead_left)
    xPosition = 0
    yPosition = 0
    if xPosBlock - xPosHead_right <= 150 or xPosBlock - xPosHead_left <= 150 or xPosBlock == 0:
       left(0.12 + rand())
       time.sleep(0.001 + rand())

    else:
     if  xPosHead_right != 0:
         xPosition = xPosHead_right
         yPosition = yPosHead_right
     else: 
        xPosition = xPosHead_left
        yPosition = yPosHead_left
     time.sleep(0.5 + rand())
     click(xPosition + 100, yPosition, 0.3 + rand())
     time.sleep(0.001 + rand())
     click(xPosition + 150, yPosition, 0.3 + rand())
     time.sleep(0.001 + rand()) 
     
    
     




   
    
   
 

    


