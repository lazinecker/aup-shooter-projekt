class Game:
    def __init__(self, game_map, window):
        self.map = game_map
        self.window = window
        self.bullets = []
        self.player = None
        self.melee_zombies = []
        self.ranged_zombies = []
        self.items = []
        self.spawners = []

    def handle_collision(self):
        pass

    def handle_input(self):
        pass

    def game_loop(self):
        pass
