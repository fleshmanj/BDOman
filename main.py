import time
import sys

import utils
from modes import Fishing
from PIL import Image
from ComputerVision import window_capture
import cv2
from Camera import Camera

"""
Write only one statement per line.
Write what you mean, not how to program it
Give proper indentation to show hierarchy and make code understandable.
Make the program as simple as possible.
Conditions and loops must be specified well ie. begun and ended explicity as in given pseudocode examples :
"""

def testing():
    while True:
        utils.show_mouse_position()

def fish():
    print("starting program")
    time.sleep(2)
    fisherman = Fishing()
    print("starting fishing")
    while True:
        print("starting loop")
        fisherman.start_fishing()
        fisherman.play_minigame()

def image_test():
    image = window_capture(300, 300)
    r = image[:, :, 2] > 0
    image[r, 2] = 0
    print(image)
    cv2.imshow("test",image)
    cv2.waitKey()
    cv2.destroyAllWindows()

def test():
    time.sleep(1)
    cam = Camera()
    for i in range(20):
        cam.turn_around()

if __name__ == "__main__":
    # testing()
    # fish()
    # image_test()
    test()



