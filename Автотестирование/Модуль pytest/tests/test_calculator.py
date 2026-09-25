from Calculator import Calculator
from pytest import mark


@mark.parametrize('a, b, result', [ # Декоратор для указания и передачи аргументов для функции тестирования
    (2, 1, 2.0),    #\
    (2, -1, -2.0),  # } разлчиные связки аргументов для теста
    (-2, -1, 2.0),  #/
    (25, 5, 5.0)
])
def test_division_valid(a, b, result): # Функция тестирования
    c = Calculator()
    assert c.calc(f'{a} / {b}') == result # Тестируемая функция

@mark.parametrize('a, b, result', [ # Декоратор для указания и передачи аргументов для функции тестирования
    (2, 1, 2),    #\
    (2, -1, -2),  # } разлчиные связки аргументов для теста
    (-2, -1, 2),  #/
    (25, 5, 125)
])
def test_mult_valid(a, b, result):  # Функция тестирования
    c = Calculator()
    assert c.calc(f'{a} * {b}') == result

# def test_div(self):
#     app = Calculator()
#     self.assertEqual(app.calc("2 / 1"), 2.0)
#     self.assertEqual(app.calc("2 / -1"), -2.0)
#     with self.assertRaises(ZeroDivisionError):  # Метод для тестирования получаемых ошибок, работает в связке с with
#         app.calc("2 / 0")
#     self.assertEqual(app.calc("-2 / -1"), 2.0)