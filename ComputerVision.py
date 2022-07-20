import cv2
import numpy as np
import pyautogui


while True:
    img_capture = np.array()
    img_capture = img_capture[:, :, ::-1].copy()
    cv2.imshow("Computer Vision", img_capture)
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break
print("done")