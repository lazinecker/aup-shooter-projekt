class Weapon:
    def __init__(self, reload_time: float):
        self.reload_time = reload_time
        self.last_shot_time = 0

    def shoot(self, x: float, y: float, x_dir: float, y_dir: float):
        pass
