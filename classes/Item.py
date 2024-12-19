class Item:
    def __init__(self, sprite, xpos, ypos):
        self.sprite = sprite
        self.xpos = xpos
        self.ypos = ypos

    def on_collect(self):
        print(f"Item {self.sprite} collected.")