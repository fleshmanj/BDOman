import pydirectinput as pyd
from ComputerVision import window_capture
from PIL import Image


def show_mouse_position():
    currentpos = pyd.position()
    if currentpos != pyd.position():
        print(pyd.position())


def take_screenshot(w=1280, h=720, top=0, left=0):
    image = window_capture(w, h, top, left)
    image_from_array = Image.fromarray(image)
    image_from_array.save(fp="matches_template.png")

