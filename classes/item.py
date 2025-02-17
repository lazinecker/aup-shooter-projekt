class Item:
    def __init__(self, sprite, x_pos, y_pos):
        self.sprite = sprite
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.hitbox = None

    def apply_effect(self, player):
        pass
