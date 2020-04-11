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
    a = pyautogui.locateAllOnScreen('schaluppe_3.png', grayscale=True, limit = 1, region=(337,145,761,580))
    ships = []
    for i in a:
        ships.append(i)
        print(i)
    if ships != []:
        x = ships[0][0] # 2 to 3 change per sec
        y = ships[0][1] # 4 change per sec
        print(x,y)
        pyautogui.click(x + 45,y - 12)

        #b = pyautogui.locateAllOnScreen('shaluppe.png', grayscale=True, limit = 1, region=(ships[0][0]-30,ships[0][1]-30,200,70))
        #for i in b:
            #print("found it",i)
    sleep(3)
