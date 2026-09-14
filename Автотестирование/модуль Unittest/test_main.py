import unittest
import main

class NameTest(unittest.TestCase): # Создаем класс наследник unittest.TestCase с названием тестируемого элемента
    def test_valid(self): # Для каждого исхода создаем метод тестирования с соответствующим названием
        self.assertEqual(main.check_login("John", phone='123123123'), True) # Вызываем методы тестирования

    def test_invalid(self):
        self.assertEqual(main.check_login("24567", phone='123123'), True)

def division(a: int, b: int):
    return a / b

class DivisionTest(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(division(4, 2), 2.0)

    def test_zero(self):
        with self.assertRaises(ZeroDivisionError): # Метод для тестирования получаемых ошибок, работает в связке с with
            division(1, 0)

    def test_string(self):
        with self.assertRaises(TypeError):
            division("пять", "шесть")

if __name__ == '__main__':
    unittest.main() # Запуск тестов