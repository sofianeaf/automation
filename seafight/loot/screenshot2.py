import pyautogui
from time import sleep

import system_spec

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

alert_cnt = 0
alert_flag = False

re_enter_flag = False

while(1):

    # FIND A TARGET
    while(alert_flag == False):
    #while(0):
        alert_cnt = alert_cnt + 1
        print("looking for target state",alert_cnt)
        b = pyautogui.locateOnScreen('full_img/stop_active.png', grayscale=True, region=system_spec.main_bar)
        if b != None:
            break
        a = pyautogui.locateAllOnScreen('full_img/sunburst.png', grayscale=True, limit = 1, region=system_spec.game_screen)
        ships = []
        for i in a:
            ships.append(i)
        if ships != []:
            x = ships[0][0] # 2 to 3 change per sec
            y = ships[0][1] # 4 change per sec
            print(x,y)
            pyautogui.click(x,y - 20)
            sleep(0.2)
            pyautogui.click(x,y - 20)
            sleep(0.2)
            pyautogui.click(x,y)
            # flag for repetition + prediction of trajectoryu
            sleep(4.5) # yqit until chip arrives?
            pyautogui.typewrite(btn_attack, interval=1)
            b = pyautogui.locateOnScreen('full_img/stop_active.png', grayscale=True, region=system_spec.main_bar)
            # EXIT CONDITION
            if b != None:
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

    # SINK A TARGET
    while(alert_flag == False):
        alert_cnt = alert_cnt + 1
        print("hit target state",alert_cnt)
        a = pyautogui.locateOnScreen('full_img/stop_active.png', grayscale=True, region=system_spec.main_bar)
        # EXIT CONDITION
        if a == None:
            print("kill done")
            alert_cnt = 0
            break
        # EXIT ALERT
        if alert_cnt == 50:#50
            alert_cnt = 0
            alert_flag = True
            break
        sleep(5)

    # REVIVE
    while(alert_flag == True):
        alert_cnt = alert_cnt + 1
        print("revive state",alert_cnt)
        a = pyautogui.locateCenterOnScreen('full_img/revive.png', grayscale=True, region=system_spec.game_screen)
        if a != None:
            print(a)
            pyautogui.click(a)
            alert_flag = False
            alert_cnt = 0
            re_enter_flag = True
            break
        if alert_cnt == 3:
            alert_flag = False
            alert_cnt = 0
            break
        sleep(4)

    # RE ENTER
    while(re_enter_flag == True):
        # REPAIR
        while(1):
            a = pyautogui.locateOnScreen('full_img/repair_inactive.png', grayscale=True, region=system_spec.main_bar)
            # EXIT CONDITION
            if a != None:
                print("repair done")
                break
            sleep(1)
            a = pyautogui.locateOnScreen('full_img/repair_ongoing.png', grayscale=True, region=system_spec.main_bar)
            if a == None:
                sleep(2)
                pyautogui.typewrite([btn_repair], interval=1)
                print("press repair")
            sleep(5)
        # ENTER MAP
        a = pyautogui.locateCenterOnScreen('full_img/enter_raid_map.png', grayscale=True)# add region
        if a != None:
            print(a)
            pyautogui.click(a)
            re_enter_flag = False

    # REPAIR
    while(alert_flag == False):
        alert_cnt = alert_cnt + 1
        print("repair state",alert_cnt)
        a = pyautogui.locateOnScreen('full_img/repair_inactive.png', grayscale=True, region=system_spec.main_bar)
        # EXIT CONDITION
        if a != None:
            print("repear done")
            alert_cnt = 0
            break
        sleep(1)
        a = pyautogui.locateOnScreen('full_img/repair_ongoing.png', grayscale=True, region=system_spec.main_bar)
        if a == None:
            sleep(2)
            pyautogui.typewrite([btn_repair], interval=1)
            print("press repair")
        # EXIT ALERT
        if alert_cnt == 20:#20
            alert_cnt = 0
            alert_flag = True
            break
        sleep(5)
