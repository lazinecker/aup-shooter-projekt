class Item:
    def __init__(self, sprite, xpos, ypos):
        self.sprite = sprite
        self.xpos = xpos
        self.ypos = ypos

    def on_collect(self):
        pass


class MedKit(Item):
    def __init__(self, sprite, xpos, ypos, heal_amount):
        super().__init__(sprite, xpos, ypos)
        self.heal_amount = heal_amount

    def on_collect(self, target):
        print(f"{target.sprite} hat {self.heal_amount} Gesundheit erhalten!")
        target.hp = min(target.maxhp, target.hp + self.heal_amount)
