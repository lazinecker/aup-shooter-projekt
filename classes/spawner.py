class Spawner:
    def __init__(self, x_pos, y_pos, spawn_rate, hp, hp_max):
        self.xPos = x_pos
        self.yPos = y_pos
        self.spawnRate = spawn_rate
        self.hp = hp
        self.hpMax = hp_max

        self.hitbox = None

    def spawn_zombie(self):
        pass
