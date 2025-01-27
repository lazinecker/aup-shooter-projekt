class Monster:
    def __init__(self, hp, maxhp, xpos, ypos, speed):
        self.hp = hp
        self.maxhp = maxhp
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed

    def drop_item(self):
        pass


class RangedMonster(Monster):
    def __init__(self, hp, maxhp, xpos, ypos, speed, attack_range):
        super().__init__(hp, maxhp, xpos, ypos, speed)
        self.attack_range = attack_range

    def attack(self, target):
        print(f"RangedMonster greift {target.sprite} aus der Entfernung {self.attack_range} an!")


class MeleeMonster(Monster):
    def __init__(self, hp, maxhp, xpos, ypos, speed, damage):
        super().__init__(hp, maxhp, xpos, ypos, speed)
        self.damage = damage

    def attack(self, target):
        print(f"MeleeMonster greift {target} mit {self.damage} Schaden an!")
