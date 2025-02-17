class Bullet:
    def __init__(self, sprite, x_pos, y_pos, bullet_range):
        self.sprite = sprite
        self.x = x_pos
        self.y = y_pos
        self.range = bullet_range

        self.hitbox = None

    def move(self):
        pass
