import random
import time
races = {
  "эльф": (1.5, 1),
  "гном": (0.8, 1.2),
  "человек": (1, 1)
}
profs = {
  "лучник": (0.9, 2, 2),
  "щитоносец": (2, 0.6),
  "рыцарь": (1.2, 1.2)
}

def create_hero(name, race, prof):
    hp = 180
    dmg = 25
    hp *= races[race][0]
    hp *= profs[prof][0]
    dmg *= races[race][1]
    dmg *= profs[prof][1]
    hero = Player(name, round(hp,1), round(dmg,1))
    return hero

def create_enemy():
    hp=random.randint(100,200)
    dmg=random.randint(10,40)
    names=["Калыван", "Горыныч", "Баба Яга"]
    name = random.choice(names)
    enemy = Enemy(name, hp, dmg)
    return enemy

def fight(enemy):
    result = hero.attack(enemy)
    time.sleep(1)
    if result:
        enemy.attack(hero)
        time.sleep(1)
        fight(enemy) # Рекурсия - это особый цикл с помощью вызова функции внутри себя же
    # else:
    #     start()

# def start():
#     enemy=create_enemy()
#     print(f"Тебе встретился")
#     enemy.stats()
#     otvet = input("Нападать? да/нет\n->")
#     if otvet == "да":
#         print("Нападаем")
#         fight(enemy)
#     elif otvet == "нет":
#         print("Вы предпочли сбежать")
#         chance = random.randint(1,100)
#         time.sleep(1)
#         if chance < 40:
#             print("Вам повезло, вы сбежали")
#             time.sleep(1.5)
#             start()
#         else:
#             print("Вам не повезло, вы не смогли сбежать")
#             print("Бой продолжается")
#             time.sleep(2)
#             enemy.attack(hero)
#             fight(enemy)






class Player:
    def __init__(self, name, hp, damage): # def __init__(self) - это конструктор класса
        self.name = name  # self.name - это атрибут класса Enemy
        self.hp = hp  # - это тоже атрибут класса Enemy
        self.damage = damage  # - это тоже атрибут класса Enemy
        self.level = 1
        self.exp = 0
        self.heals = 0

    def attack(self, enemy): # - это создание метода attack для класса Enemy
        enemy.hp =(enemy.hp- self.damage)
        print(f'{self.name} атакует {enemy.name} и наносит {self.damage} dmg по {enemy.name}')

        if enemy.hp <= 0:
            print("Враг убит\n")
            self.exp+=enemy.xp
            self.hp += 50
            print(f"Вы получили {enemy.xp} опыта\n"
                  f"теперь у вас {self.exp} опыта\n"
                  f"вы выпили отвар теперь у вас {self.hp} здоровья")
            time.sleep(1.5)
            if self.exp >= 100:
                self.level += 1
                print(f"ПОЗДРАВЛЯЮ! Уровень повышен: {self.level}")
                time.sleep(1.5)
                self.exp = 0
                self.damage *= 1.2
                self.damage = round(self.damage,1)
                print(f"Ты стал сильнее! ⚔️: {self.damage}")
                time.sleep(1.5)
                Otvar=random.randint(1,100)
                if Otvar > 50:
                    print("Вы нашли лечебный отвар")
                    self.heals += 1
                    print(f"Теперь у вас их {self.heals}")


            return False
        else:
            print(f'И у него осталось {enemy.hp} хп\n')
            return True

    def stats(self):
        print(f"{self.name} характиристики:\n"
              f"здоровье {self.hp}\n"
              f"урон {self.damage}\n")

class Enemy:
    def __init__(self, name, hp, damage): # def __init__(self) - это конструктор класса
        self.name = name # self.name - это атрибут класса Enemy
        self.hp = hp # - это тоже атрибут класса Enemy
        self.damage = damage #- это тоже атрибут класса Enemy
        self.xp = round(self.hp*1.5,1)

                #self - это аргумент в который кладется переменная объекта класса
    def attack(self, hero): # - это создание метода attack для класса Enemy
        hero.hp = (hero.hp - self.damage)
        print(f'{self.name} атакует {hero.name} и наносит {self.damage} урона!')

        if hero.hp <= 0:
            print("Герой убит\n"
                  "Игра окончена!")
            exit(0)
        else:
            print(f'И у него осталось {hero.hp} хп\n')
            return True


    def stats(self):
        print(f"{self.name} характиристики:\n"
              f"здоровье {self.hp}\n"
              f"урон {self.damage}\n")

# name = input('Введите свое имя: ')
# race = ""
# prof = ""
#
# # name = 'Ahmad' # !
# # race = "гном" # !
# # prof = "рыцарь" # !
#
# while race not in tuple(races.keys()):
#     print (f"Bыбеpи расу: {tuple (races.keys())}")
#     race=input("->").lower()
# while prof not in tuple (profs.keys()):
#     print (f"Bыбеpи профессию: {tuple(profs.keys())}")
#     prof=input("->").lower()
#
#
# hero = create_hero(name, race, prof)
# print(f"Здравствуй, герой с именем {hero.name}!\n"
#         f"Твоё здоровье равно {hero.hp} XП. \n"
#         f"Твой урон равен {hero.damage} единицам.\n"
#         f"Желаю удачи в приключениях, странник! ^_+")

# start()