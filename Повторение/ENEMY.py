import random


class Enemy:

    names = ["Гоблин", "Орк", "Скелет", "Зомби", "Дракон", "Призрак"]

    def __init__(self):
        self.name = random.choice(self.names)
        self.health = random.randint(50, 100)
        self.damage = random.randint(5, 20)

    def stats(self):
        print(f"Враг: {self.name} | Здоровье: {self.health} | Урон: {self.damage}")



enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

enemy1.stats()
enemy2.stats()
enemy3.stats()








