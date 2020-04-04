import pyautogui
from time import sleep

[width,height] = pyautogui.size()
print(width,height)

# import pyautogui
# pyautogui.displayMousePosition()

btn_attack = 'q'
btn_cancel_attack = 'w'
btn_toggle_opponents = 'r'
btn_set_course = 't'
btn_to_the_ship = 'z'
btn_repair = 'u'

# game screen
s_x1 = 781
s_y1 = 929
s_x2 = 1201
s_y2 = 972

# state bar
b_x1 = 781
b_y1 = 929
b_x2 = 1201
b_y2 = 972

while(1):
    while(1):
        b = pyautogui.locateOnScreen('full_img/asus/stop_active.png', grayscale=True)
        if b != None:
            break
        a = pyautogui.locateAllOnScreen('full_img/asus/sunburst.png', grayscale=True, limit = 1, region=(337,145,761,580))
        ships = []
        for i in a:
            ships.append(i)
        if ships != []:
            x = ships[0][0] # 2 to 3 change per sec
            y = ships[0][1] # 4 change per sec
            print(x,y)
            pyautogui.click(x, y)
            sleep(0.2)
            y = y - 20 #target ship
            pyautogui.click(x,y)
            sleep(0.2)
            pyautogui.click(x,y)
            # flag for repetition + prediction of trajectoryu
            sleep(4.5) # yqit until chip arrives?
            pyautogui.typewrite(btn_attack, interval=1)
            b = pyautogui.locateOnScreen('full_img/asus/stop_active.png', grayscale=True)
            if b != None:
                break
        sleep(1)
    print("found target")
    while(1):
        a = pyautogui.locateOnScreen('full_img/asus/stop_active.png', grayscale=True)
        if a == None:
            break
        sleep(5)
    print("kill done")

    # repair if needed
    #sleep(1)
    a = pyautogui.locateOnScreen('full_img/asus/repair_inactive.png', grayscale=True)
    if a == None:
        pyautogui.typewrite([btn_repair], interval=1)
        print("repair")

    # wait till repear is done
    while(1):
        sleep(10)
        a = pyautogui.locateOnScreen('full_img/asus/repair_inactive.png', grayscale=True)
        if a != None:
            print("repear done")
            break
