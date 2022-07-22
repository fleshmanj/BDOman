import pydirectinput as pyd


class Camera:

    def __int__(self):
        self.self = self

    def turn_left(self):
        pyd.press("k")
        originx, originy = pyd.position()
        print(originx)
        pyd.mouseDown(button="right")
        print(pyd.position())
        pyd.move(-1155, 0)
        print(pyd.position())
        pyd.mouseUp(button="right")

    def turn_right(self):
        pyd.press("k")
        originx, originy = pyd.position()
        print(originx)
        pyd.mouseDown(button="right")
        print(pyd.position())
        pyd.move(1, 0)
        pyd.move(703, 0)
        print(pyd.position())
        pyd.mouseUp(button="right")

    def turn_around(self):
        self.turn_left()
        self.turn_left()

    def circle(self):
        self.turn_around()
        self.turn_around()