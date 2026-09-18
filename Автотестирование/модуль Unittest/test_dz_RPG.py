from dz_RPG import *
import unittest


class RPGTest(unittest.TestCase): # Создаем класс наследник unittest.TestCase с названием тестируемого элемента
    def test_attacks(self):
        govnuk=create_hero("Кеша", "гном", "лучник")
        skot=create_enemy()
        self.assertEqual(govnuk.attack(skot), True)
        self.assertEqual(skot.attack(govnuk), True)
        skot.hp = 1
        self.assertEqual(govnuk.attack(skot), False)

if __name__ == '__main__':
    unittest.main() # Запуск тестов