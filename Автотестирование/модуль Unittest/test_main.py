import unittest
import main

class NameTest(unittest.TestCase): # Создаем класс наследник unittest.TestCase с названием тестируемого элемента
    def test_valid(self): # Для каждого исхода создаем метод тестирования с соответствующим названием
        self.assertEqual(main.check_login("John", phone='123123123'), True) # Вызываем методы тестирования

    def test_invalid(self):
        self.assertEqual(main.check_login("24567", phone='123123'), False)

if __name__ == '__main__':
    unittest.main() # Запуск тестов