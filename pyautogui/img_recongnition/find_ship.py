import pyautogui
from time import sleep
import screenshotUtil as pag

import time
from PIL import Image

#print(help(pyautogui))


"""
while(True):
    # 5 to 7 seconds
    start = time.time()
    a = pyautogui.locateCenterOnScreen('ship_1_2px_down_right.png')
    b = pyautogui.locateCenterOnScreen('ship_1_2px_down_left.png')
    c = pyautogui.locateCenterOnScreen('ship_1_2px_up_right.png')
    d = pyautogui.locateCenterOnScreen('ship_1_2px_up_left.png')
    end = time.time()
    print(a,b,c,d, end - start)
"""
"""
while(True):
    # 4 to 6 seconds
    start = time.time()
    a = pyautogui.locateCenterOnScreen('ship_1_8px_down_right.png', grayscale=True)
    b = pyautogui.locateCenterOnScreen('ship_1_8px_down_left.png', grayscale=True)
    c = pyautogui.locateCenterOnScreen('ship_1_8px_up_right.png', grayscale=True)
    d = pyautogui.locateCenterOnScreen('ship_1_8px_up_left.png', grayscale=True)
    end = time.time()
    print(a,b,c,d, end - start)
"""
"""
while(True):
    #  4 to 6
    start = time.time()
    a = pyautogui.locateCenterOnScreen('ship_1_4px_down_right.png', grayscale=True)
    b = pyautogui.locateCenterOnScreen('ship_1_4px_down_left.png', grayscale=True)
    c = pyautogui.locateCenterOnScreen('ship_1_4px_up_right.png', grayscale=True)
    d = pyautogui.locateCenterOnScreen('ship_1_4px_up_left.png', grayscale=True)
    end = time.time()
    print(a,b,c,d, end - start)
"""
"""
im_0 = pyautogui.screenshot()
im_1 = Image.open(open('ship_1_1px_down_right.png', 'rb'))
im_2 = Image.open(open('ship_1_1px_down_left.png', 'rb'))
im_3 = Image.open(open('ship_1_1px_up_right.png', 'rb'))
im_4 = Image.open(open('ship_1_1px_up_left.png', 'rb'))
while(True):
    # 6
    start = time.time()
    a = pyautogui.locateCenterOnScreen(im_1)
    b = pyautogui.locateCenterOnScreen(im_2)
    c = pyautogui.locateCenterOnScreen(im_3)
    d = pyautogui.locateCenterOnScreen(im_4)
    end = time.time()
    print(a,b,c,d, end - start)
"""

im_0 = pyautogui.screenshot()
im_1 = Image.open(open('ship_1_4px_down_right.png', 'rb'))
im_2 = Image.open(open('ship_1_4px_down_left.png', 'rb'))
im_3 = Image.open(open('ship_1_4px_up_right.png', 'rb'))
im_4 = Image.open(open('ship_1_4px_up_left.png', 'rb'))
while(True):
    #
    start = time.time()
    a = pyautogui.locateCenterOnScreen(im_1, grayscale=True)
    b = pyautogui.locateCenterOnScreen(im_2, grayscale=True)
    c = pyautogui.locateCenterOnScreen(im_3, grayscale=True)
    d = pyautogui.locateCenterOnScreen(im_4, grayscale=True)
    end = time.time()
    print(a,b,c,d, end - start)


#pyautogui.press(btn_attack)
