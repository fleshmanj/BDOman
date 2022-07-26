import time

import cv2
import numpy as np
import pydirectinput
import pyautogui
import win32con
import win32gui
import win32ui
from PIL import Image
import utils


def calibrate_window():
    hwnd = win32gui.FindWindow(None, "BLACK DESERT - 421041")
    rect = win32gui.GetWindowRect(hwnd)
    return rect


def calibrate_mouse_pos(x, y):
    rect = calibrate_window()
    y = rect[1] + y
    x = rect[0] + x
    return x, y


def window_capture(width, height, top=0, left=0):
    """

    :param width: window width
    :param height: window height
    :param top: Top left corner x coordinate
    :param left: Top left corner y coordinate
    :return: image
    """
    # rect = calibrate_window()
    # top = rect[1] + top
    # left = rect[0] + left

    w = width  # set this
    h = height  # set this
    bmpfilenamename = "debug.bmp"  # set this

    hwnd = win32gui.FindWindow(None, "BLACK DESERT - 421041")
    # hwnd = None
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (top, left), win32con.SRCCOPY)
    # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    img = np.ascontiguousarray(img)

    # filter red and blue channel
    # red = img[:, :, 2] > 0
    # img[red, 2] = 0
    # blue = img[:, :,  0] > 0
    # img[blue, 0] = 0

    return img


def find_object(w, h, top, left, image):
    rect = calibrate_window()
    # top = rect[1] - top
    # left = rect[0] - left
    screenshot = window_capture(w, h, top, left)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(image, 0)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= .80:
        return True


def find_and_click(w, h, top, left, image):
    rect = calibrate_window()
    top = rect[1] + top
    left = rect[0] + left
    utils.take_screenshot(w, h, top, left)
    screenshot = window_capture(w, h, top, left)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(image, 0)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    if max_val >= .80:
        max_x = max_loc[0]
        max_x = max_x + top + 5
        max_y = max_loc[1]
        max_y = max_y + left + 5
        pydirectinput.mouseDown(max_x, max_y, button="left", duration=0.1)
        pydirectinput.mouseUp(max_x, max_y, button="left", duration=0.1)


def find_all_matches(w, h, top, left, image):
    # rect = calibrate_window()
    # top = rect[1] + top
    # left = rect[0] + left

    args = {"threshold": 0.75
            }

    screenshot = window_capture(w, h, top, left)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(image)

    # filter red and blue channel
    # r = template[:, :, 2] > 0
    # template[r, 2] = 0
    # b = template[:, :, 0] > 0
    # template[b, 0] = 0

    image_w = template.shape[1]
    image_h = template.shape[0]
    template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    (yCoords, xCoords) = np.where(result >= args["threshold"])

    rectangles = []
    for (x, y) in zip(xCoords, yCoords):
        rectangles.append([int(x), int(y), int(image_w), int(image_h)])
        rectangles.append([int(x), int(y), int(image_w), int(image_h)])
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    print(len(rectangles))
    xcords = []
    for rectangle in rectangles:
        xcords.append(rectangle[0])
    return xcords


def get_pixel_color(w, h, top, left):
    x = 1
    y = 1
    pixel = (x, y)
    screenshot = window_capture(w, h, top, left)
    screenshot = Image.fromarray(screenshot)
    rgb_image = screenshot.convert("RGB")
    r, g, b = rgb_image.getpixel(pixel)
    # print(r,g,b)
    return r, g, b


def point_and_click(x, y):
    x, y = calibrate_mouse_pos(x, y)
    # pydirectinput.moveTo(x,y)
    pydirectinput.mouseDown(x, y, button="left", duration=0.5)
    pydirectinput.mouseUp(x, y, button="left", duration=0.5)