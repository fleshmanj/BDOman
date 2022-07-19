from PIL import ImageGrab
import time
import pyautogui
import pydirectinput as pyd
from Camera import Camera


"""
Write only one statement per line.
Write what you mean, not how to program it
Give proper indentation to show hierarchy and make code understandable.
Make the program as simple as possible.
Conditions and loops must be specified well ie. begun and ended explicity as in given pseudocode examples :
"""

time.sleep(2)

camera = Camera()

for x in range(100):
    pyd.press("ctrl")
    camera.turn_around()
    pyd.keyDown("w")
    time.sleep(1)
    pyd.keyUp("w")



# while True:
#     if pyd.MOUSEEVENTF_LEFTCLICK:
#         print(pyd.position())
#     else:
#         print("0")
