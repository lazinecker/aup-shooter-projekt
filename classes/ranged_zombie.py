class RangedZombie:
    def __init__(self, hp, max, x_pos, y_pos, speed, range):
        self.hp = hp
        self.max_hp = max
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.range = range
        self.hitbox = None

    def do_ranged_zombie_stuff(self):
        pass

    def drop_item(self):
        pass

    def drop_rate(self):
        pass