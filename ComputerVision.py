import cv2
import numpy as np
import pydirectinput
import win32con
import win32gui
import win32ui


def window_capture(width, height, top=0, left=0):
    """

    :param width: window width
    :param height: window height
    :param top: Top left corner x coordinate
    :param left: Top left corner y coordinate
    :return: image
    """
    w = width  # set this
    h = height  # set this
    bmpfilenamename = "debug.bmp"  # set this

    # hwnd = win32gui.FindWindow(None, windowname)
    hwnd = None
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

    return img


def find_object(w, h, top, left, image):
    screenshot = window_capture(w, h, top, left)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    space = cv2.imread(image, 0)

    result = cv2.matchTemplate(screenshot, space, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= .80:
        return True


def find_all_matches(w, h, top, left, image):
    args = {"threshold": 0.90
            }
    screenshot = window_capture(w, h, top, left)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(image)
    template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    (yCoords, xCoords) = np.where(result >= args["threshold"])
    return yCoords, xCoords


