import pyscreenshot as ImageGrab
import pyautogui

[width,height] = pyautogui.size()
print(width,height)

# pyautogui.displayMousePosition()
# map
m_x1 = 1241
m_y1 = 331
m_x2 = 1334
m_y2 = 423
# screen (tbd)
s_x1 = 0
s_y1 = 0
s_x2 = 0
s_y2 = 0

img = ImageGrab.grab(bbox=(x1,y1,x2,y2))

print(img)



