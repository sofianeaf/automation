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

def loot():
    j = 0
    while(1):
        j = j + 1
        # waiting for a target
        i = 0
        while(1):
            i = i + 1
            pyautogui.typewrite([btn_toggle_opponents, btn_attack], interval=1)
            a = pyautogui.locateOnScreen('full_img/asus/stop_active.png', grayscale=True)
            if a != None:
                #stop_ship()
                break
            print(i,j)
            if i == 4:
                #sale_ship(j % 2)
                j = j + 1
            sleep(1)
        print("found target")

        # kill target
        while(1):
            a = pyautogui.locateOnScreen('full_img/asus/stop_active.png', grayscale=True)
            if a == None:
                break
            sleep(5)
        print("kill done")

        # repair if needed
        sleep(1)
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

#loot()qr
loot()
