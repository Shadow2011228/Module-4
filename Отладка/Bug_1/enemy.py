class Enemy:
    types = {
        "Слайм": (10, 3),
        "Призрак": (20, 6),
        "Скелет": (25, 10),
        "Король": (40, 15)
             }

    def __init__(self, key: float | int):
        key = int(key)
        names = tuple(self.types.keys())
        self.name = names[key % len(names)]
        self.hp = self.types[self.name][0]
        self.dmg = self.types[self.name][1]
        self.counter = 0

    def attack(self, victim):
        victim.hp -= self.dmg
        print(f"Удар по {victim.name}! -{self.dmg}❤️.")
        if victim.hp <= 0:
            return True
        else:
            return False




