import unittest
from Calculator import Calculator

def division(a: int, b: int):
    return a / b

class CalcTest(unittest.TestCase):
    def test_calc_available(self):
        app = Calculator()
        try:
            app.calc("1 + 1")
        except AttributeError:
            self.fail("Функции calc не существует!")

    def test_summ(self):
        app = Calculator()
        self.assertEqual(app.calc("1 + 2"), 3)
        self.assertEqual(app.calc("1 + -3"), -2)
        self.assertEqual(app.calc("1 + 0"), 1)
        self.assertEqual(app.calc("-2 + -3"), -5)

    def test_diff(self):
        app = Calculator()
        self.assertEqual(app.calc("2 - 1"), 1)
        self.assertEqual(app.calc("2 - -1"), 3)
        self.assertEqual(app.calc("2 - 0"), 2)
        self.assertEqual(app.calc("-2 - -1"), -1)

    def test_mult(self):
        app = Calculator()
        self.assertEqual(app.calc("2 * 3"), 6)
        self.assertEqual(app.calc("2 * -3"), -6)
        self.assertEqual(app.calc("2 * 0"), 0)
        self.assertEqual(app.calc("-2 * -3"), 6)

    def test_div(self):
        app = Calculator()
        self.assertEqual(app.calc("2 / 1"), 2.0)
        self.assertEqual(app.calc("2 / -1"), -2.0)
        with self.assertRaises(ZeroDivisionError):  # Метод для тестирования получаемых ошибок, работает в связке с with
            app.calc("2 / 0")
        self.assertEqual(app.calc("-2 / -1"), 2.0)



