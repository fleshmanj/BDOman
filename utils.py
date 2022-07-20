import pydirectinput as pyd


def show_mouse_position():
    currentpos = pyd.position()
    if currentpos != pyd.position():
        print(pyd.position())
