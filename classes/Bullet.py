class Bullet:
    def __init__(self, sprite, xpos, ypos, range:float, radius, dmg:int):
        self.sprite = sprite
        self.xpos = xpos
        self.ypos = ypos
        self.range = range
        self.radius = radius
        self.dmg = dmg

    def move(self):
        pass
