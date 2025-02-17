class Player:
    def __init__(self, hp, speed, sprite, xPos, yPos, maxHp, move):
        self.hp = hp
        self.speed = speed
        self.sprite = sprite
        self.xPos = xPos
        self.yPos = yPos
        self.maxHp = maxHp
        self.move = move

        self.hitbox = None
        self.weapon = None

    def move(self, x, y):
        pass

    def shoot(self):
        pass
