from abc import ABC, abstractmethod
import inspect
import collections
from ComputerVision import find_all_matches, find_object
import pydirectinput as pyd
import time


# class AbstractMode(ABC):
#
#     def __init__(self):
#         logging.debug("created")
#
#     @abstractmethod
#     def initial(self):
#         pass
#
#     @abstractmethod
#     def use_keyboard_input(self, kb: dict):
#         pass
#
#     @abstractmethod
#     def screen(self):
#         pass


class Fishing:

    def __int__(self):
        print("created a fisherman")

    def start_fishing(self):
        while True:
            fishing = True
            catching = False
            while fishing:
                if find_object(300, 300, 800, 300, image="assets/space.png") is True:
                    pyd.press("space")
                    catching = True
                    fishing = False
            while catching:
                if find_object(300, 300, 800, 300, image="assets/fish_on.png") is True:
                    pyd.keyDown("space")
                    time.sleep(.01)
                    pyd.keyUp("space")
                    catching = False
                    time.sleep(1)
                    pyd.keyDown("space")
                    time.sleep(.01)
                    pyd.keyUp("space")
            if fishing is False and catching is False:
                break

    def play_minigame(self):
        while True:
            values = {}
            w_y, w_x = find_all_matches(600, 300, 700, 300, "assets/W.png")
            a_y, a_x = find_all_matches(600, 300, 700, 300, "assets/A.png")
            s_y, s_x = find_all_matches(600, 300, 700, 300, "assets/S.png")
            d_y, d_x = find_all_matches(600, 300, 700, 300, "assets/D.png")
            if len(w_x) != 0:
                w = set(w_x)
                for i in w:
                    values[i] = "w"
            if len(a_x) != 0:
                a = set(a_x)
                for i in a:
                    values[i] = "a"
            if len(s_x) != 0:
                s = set(s_x)
                for i in s:
                    values[i] = "s"
            if len(d_x) != 0:
                d = set(d_x)
                for i in d:
                    values[i] = "d"

            sorted_values = sorted(values.items())
            sequence = []
            for i in sorted_values:
                sequence.append(i[1])
            if len(sequence) != 0:

                for i in sequence:
                    pyd.press(i)
                break

