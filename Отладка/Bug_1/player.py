import random

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.dmg = 10

    def attack(self, victim):
        victim.hp -= self.dmg
        victim.counter += 1
        print(f"Удар по {victim.name}! -{self.dmg}❤️.")
        if victim.hp <= 0:
            return False
        else:
            return True
