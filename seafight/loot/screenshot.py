import pyscreenshot as ImageGrab
import pyautogui
from time import sleep

[width,height] = pyautogui.size()
print(width,height)

# import pyautogui
# pyautogui.displayMousePosition()

btn_attack = 'q'
btn_cancel_attack = 'w'
btn_toggle_opponents = 'r'
btn_set_corse = 't'
btn_to_the_ship = 'z'
btn_repair = 'u'

# state bar
b_x1 = 781
b_y1 = 929
b_x2 = 1201
b_y2 = 972

while(1):
    # waiting for a target
    while(1):
        pyautogui.typewrite([btn_toggle_opponents, btn_attack], interval=1)
        a = pyautogui.locateOnScreen('full_img/stop_active.png', grayscale=True)
        if a != None:
            break
        sleep(1.5)
    print("found target")

    # kill target
    while(1):
        a = pyautogui.locateOnScreen('full_img/stop_active.png', grayscale=True)
        if a == None:
            break
        sleep(10)
    print("kill done")

    # repair if needed
    sleep(20)
    a = pyautogui.locateOnScreen('full_img/repair_inactive.png', grayscale=True)
    if a == None:
        pyautogui.typewrite([btn_repair], interval=1)
        print("repair")

    # wait till repear is done
    while(1):
        sleep(10)
        a = pyautogui.locateOnScreen('full_img/repair_inactive.png', grayscale=True)
        if a != None:
            print("repear done")
            break

#img = ImageGrab.grab(bbox=(b_x1,b_y1,b_x2,b_y2))
#img.show()
