import cv2
import numpy as np
import pyautogui
import time

import win32gui, win32ui, win32con


def window_capture(width, height, top=0, left=0):
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


def find_object():
    screenshot = window_capture(300, 300, 800, 300)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    space = cv2.imread("assets/space.png", 0)

    result = cv2.matchTemplate(screenshot, space, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= .80:
        print("Found space")


# while True:
#     start_time = time.time()
#     img_capture = window_capture(500, 500)
#     cv2.imshow("Computer Vision", img_capture)
#     end_time = time.time()
#     print(f"FPS is {1 / (end_time - start_time)}")
#     if cv2.waitKey(1) == ord("q"):
#         cv2.destroyAllWindows()
#         break

