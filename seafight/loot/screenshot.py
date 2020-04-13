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

# state bar
b_x1 = 781
b_y1 = 929
b_x2 = 1201
b_y2 = 972

def sale_ship(direction):
    if direction == 0:
        x = 972
        y = 258
    elif direction == 1:
        x = 1049
        y = 258
    pyautogui.click(x, y,interval=0.5)
    pyautogui.typewrite([btn_set_course, btn_to_the_ship], interval=0.5)

def stop_ship():
    pyautogui.typewrite([btn_to_the_ship, 'up', btn_set_course], interval=0.1)

alert_cnt = 0
alert_flag = False

while(1):

    # FIND A TARGET
    while(alert_flag == False):
        alert_cnt = alert_cnt + 1
        print("looking for target state",alert_cnt)
        # already shooting at start time
        a = pyautogui.locateOnScreen('full_img/stop_active.png', grayscale=True, region=(752,832,470,60)) #
        if a != None:
            alert_cnt = 0
            break
        # hit something
        pyautogui.typewrite([btn_toggle_opponents, btn_attack], interval=1)
        a = pyautogui.locateOnScreen('full_img/stop_active.png', grayscale=True, region=(752,832,470,60)) #, region=(476,677,455,59)
        # EXIT CONDITION
        if a != None:
            print("found target")
            alert_cnt = 0
            break
        # EXIT ALERT
        if alert_cnt == 100:
            alert_cnt = 0
            alert_flag = True
            # move around to prevent log out
            # move around to prevent log out
            # move around to prevent log out
            break
        sleep(1)

    # TRAVEL TO TARGET
    for i in range(0,4):
        a = pyautogui.locateCenterOnScreen('full_img/yellow_dot.png', grayscale=False, region=(611,296,769,590)) #, region=(337,145,761,580)
        if a != None:
            sleep(1)
            pyautogui.click(a)
        sleep(1)

    # SINK A TARGET
    while(alert_flag == False):
        alert_cnt = alert_cnt + 1
        print("hit target state",alert_cnt)
        a = pyautogui.locateOnScreen('full_img/stop_active.png', grayscale=True, region=(752,832,470,60)) #, region=(476,677,455,59)
        # EXIT CONDITION
        if a == None:
            print("kill done")
            alert_cnt = 0
            break
        # EXIT ALERT
        if alert_cnt == 80:
            alert_cnt = 0
            alert_flag = True
            break
        sleep(5)

    # REVIVE
    while(alert_flag == True):
        alert_cnt = alert_cnt + 1
        print("revive state",alert_cnt)
        a = pyautogui.locateCenterOnScreen('full_img/revive.png', grayscale=True, region=(611,296,769,590)) #, region=(337,145,761,580)
        if a != None:
            print(a)
            pyautogui.click(a)
            alert_flag = False
            alert_cnt = 0
            break
        if alert_cnt == 3:
            alert_flag = False
            alert_cnt = 0
            break
        sleep(4)

    # REPAIR
    while(alert_flag == False):
        alert_cnt = alert_cnt + 1
        print("repair state",alert_cnt)
        a = pyautogui.locateOnScreen('full_img/repair_inactive.png', grayscale=True, region=(752,832,470,60)) #, region=(476,677,455,59)
        # EXIT CONDITION
        if a != None:
            print("repear done")
            alert_cnt = 0
            break
        sleep(1)
        a = pyautogui.locateOnScreen('full_img/repair_ongoing_mini.png', grayscale=True, region=(752,832,470,60)) #, region=(476,677,455,59)
        if a == None:
            sleep(2)
            pyautogui.typewrite([btn_repair], interval=1)
            print("press repair")
        # EXIT ALERT
        if alert_cnt == 20:
            alert_cnt = 0
            alert_flag = True
            break
        sleep(5)
