import pyautogui
from time import sleep

# get screen size
#screenWidth, screenHeight = pyautogui.size()
#print("screen infos: ",screenWidth, screenHeight)

#pyautogui.moveTo(pyautogui.locateCenterOnScreen('old/screenshot_2.png'))
sleep(2)
# buttons to recognize :
# repair active
# repair inactive
# select cheap harpoons
# fire harppons

"""
for i in range(0, 10):
    pyautogui.moveTo(screenWidth/2, screenHeight/2)


    btn = 'left'
    pyautogui.keyDown(btn)
    sleep(1.3)
    pyautogui.keyUp(btn)


    pyautogui.click()
    sleep(2) # wait for boat to move
    try:
        a = 0
        b = 0
        a, b = pyautogui.locateCenterOnScreen('screenshot_2.png')
        print(a, b)
        #pyautogui.moveTo()
    except:
        sleep(0.1)
"""

class SeafightGameBot():
    def __init__(self):
        self.number = 1

    def shoot(self):
        btn = 'q'
        pyautogui.keyDown(btn)


#bot = SeafightGameBot()
#bot.shoot()

btn_attack = 'q'
btn_cancel_attack = 'w'
btn_toggle_opponents = 'r'
btn_set_corse = 't'
btn_to_the_ship = 'z'
btn_repair = 'u'

while(True):
    print(pyautogui.locateCenterOnScreen('ship_1_down_right.png'))
    print(pyautogui.locateCenterOnScreen('ship_1_down_left.png'))
    print(pyautogui.locateCenterOnScreen('ship_1_up_right.png'))
    print(pyautogui.locateCenterOnScreen('ship_1_up_left.png'))
    sleep(0.1)
    print(pyautogui.locateCenterOnScreen('ship_2_down_right.png'))
    print(pyautogui.locateCenterOnScreen('ship_2_down_left.png'))
    print(pyautogui.locateCenterOnScreen('ship_2_up_right.png'))
    print(pyautogui.locateCenterOnScreen('ship_2_up_left.png'))
    sleep(0.1)
    print(pyautogui.locateCenterOnScreen('ship_3_down_right.png'))
    print(pyautogui.locateCenterOnScreen('ship_3_down_left.png'))
    print(pyautogui.locateCenterOnScreen('ship_3_up_right.png'))
    print(pyautogui.locateCenterOnScreen('ship_3_up_left.png'))
    sleep(0.1)
#pyautogui.press(btn_attack)
