import time
import enemy
import player

class Game:
    def __init__(self, player: player.Player):
        self.player = player
        self.enemies = []

    def create_enemy(self):
        timestamp = time.time()
        e = enemy.Enemy(timestamp)
        self.enemies.append(e)

    def post_kill(self, target: enemy.Enemy):
        key = self.enemies.index(target)
        self.enemies[key] = (target.name, target.counter)

    def analyze(self):
        def sort_key(e):
            return e[1]
        self.enemies = sorted(self.enemies, key=sort_key)
        minimal = self.enemies[0]
        maximal = self.enemies[-1]
        print(f"Самая лёгкая битва: для победы над {minimal[0]} тебе потребовалось {minimal[1]} удара")
        print(f"Самая сложная битва: для победы над {maximal[0]} тебе потребовалось {maximal[1]} удара")

    def start_fight(self):
        self.create_enemy()
        self.fight()

    def fight(self):
        loser = self.player.attack(self.enemies[-1])
        if loser:
            loser = self.enemies[-1].attack(self.player)
            if loser:
                print("Ты проиграл")
                self.post_kill(self.enemies[-1])
                self.analyze()
            else:
                self.fight()
        else:
            self.post_kill(self.enemies[-1])
            print(f"Ты победил врага {self.enemies[-1][0]}")
            self.player.hp += 10
            time.sleep(1)
            self.start_fight()



if __name__ == '__main__':
    player_name = input("Введи своё имя → ")
    p = player.Player(player_name)
    game = Game(p)
    game.start_fight()





















