from abc import ABC, abstractmethod
import inspect
import logging
import collections

import utils
from ComputerVision import find_all_matches, find_object, find_and_click, get_pixel_color, point_and_click
import pydirectinput as pyd
import time


class AbstractMode(ABC):

    def __init__(self):
        logging.debug("created")

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def repair(self):
        find_and_click(350, 50, 1030, 20, image="assets/search_icon.png")
        find_and_click(350, 50, 900, 140, image="assets/search_icon.png")


class Fishing:

    def __int__(self):
        print("created a fisherman")


    def repair(self):
        point_and_click(1055, 40)
        find_and_click(100, 100, 900, 140, image="assets/small_repair.png")
        pyd.keyDown("esc")
        time.sleep(.2)
        pyd.keyUp("esc")
        pyd.keyDown("t")
        time.sleep(.2)
        pyd.keyUp("t")



        # time.sleep(.1)
        # point_and_click(800, 560)
        # time.sleep(.1)
        # pyd.typewrite("Gabril")
        # point_and_click(1000, 560)
        # point_and_click(1000, 560)
        # point_and_click(850, 450)
        # pyd.keyDown("t")
        # time.sleep(.2)
        # pyd.keyUp("t")


    def start_fishing(self):
        fishing = True
        catching = False
        reeling = False
        while True:
            while fishing:
                if find_object(150, 100, 580, 240, image="assets/small_space.png"):
                    print("Found space")
                    pyd.keyDown("space")
                    time.sleep(.1)
                    pyd.keyUp("space")
                    catching = True
                    fishing = False
            while catching:
                if find_object(100, 100, 580, 300, image="assets/fish_biting.png"):
                    print("Found fish on")
                    time.sleep(2)
                    pyd.keyDown("space")
                    time.sleep(.1)
                    pyd.keyUp("space")
                    reeling = True
                    while reeling:
                        r, g, b = get_pixel_color(5, 5, 720, 285)
                        if r == 217 and g == 169 and b == 83:
                            print("catching fish")
                            catching = False
                            time.sleep(.1)
                            pyd.keyDown("space")
                            time.sleep(.1)
                            pyd.keyUp("space")
                            reeling = False
            time.sleep(3.5)
            if not find_object(300, 300, 800, 300, image="assets/small_space.png"):
                if fishing is False and catching is False and reeling is False:
                    print("ending fishing")
                    break
            else:
                pyd.leftClick(1482, 648, duration=0.5)
                pyd.leftClick(1482, 648, duration=0.5)
                fishing = True
                print("still fishing")

    def play_minigame(self):
        playing = True
        utils.take_screenshot(300, 100, 450, 250)
        while playing:
            values = {}
            w_x = find_all_matches(300, 100, 450, 250, "assets/small_w.png")
            a_x = find_all_matches(300, 100, 450, 250, "assets/small_a.png")
            s_x = find_all_matches(300, 100, 450, 250, "assets/small_s.png")
            d_x = find_all_matches(300, 100, 450, 250, "assets/small_d.png")
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
            print(sequence)
            if len(sequence) != 0:

                for i in sequence:
                    pyd.press(i)
                playing = False
                time.sleep(5)
                pyd.keyDown("r")
                time.sleep(.5)
                pyd.keyUp("r")
                pyd.keyDown("r")
                time.sleep(.5)
                pyd.keyUp("r")
                time.sleep(1)
            else:
                if find_object(150, 100, 580, 240, image="assets/small_space.png"):
                    playing = False
