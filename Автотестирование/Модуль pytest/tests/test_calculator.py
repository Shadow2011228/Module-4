import pytest

from Calculator import Calculator
from pytest import mark
from contextlib import nullcontext as does_not_raise

class TestCalculation:
    @mark.parametrize('a, b, result, expectation', [ # Декоратор для указания и передачи аргументов для функции тестирования
        (2, 1, 2.0, does_not_raise()),    #\
        (2, -1, -2.0, does_not_raise()),  # } разлчиные связки аргументов для теста
        (-2, -1, 2.0, does_not_raise()),  #/
        (25, 5, 5.0, does_not_raise()),
        (10, 0, 0, pytest.raises(ZeroDivisionError)),
        ('hello', 3, 5, pytest.raises(ValueError)),
        (1, 'hello', 5, pytest.raises(ValueError)),
        ('hello', 'hello', 'hello', pytest.raises(ValueError)),
        (2, 1, 1, pytest.raises(AssertionError)),
        ('hello', 1, 'hello', pytest.raises(ValueError)),
    ])
    def test_division_valid(self, a, b, result, expectation): # Функция тестирования
        c = Calculator()
        with expectation:
            assert c.calc(f'{a} / {b}') == result # Тестируемая функция

    @mark.parametrize('a, b, result, expectation', [ # Декоратор для указания и передачи аргументов для функции тестирования
        (2, 1, 2, does_not_raise()),    #\
        (2, -1, -2, does_not_raise()),  # } разлчиные связки аргументов для теста
        (-2, -1, 2, does_not_raise()),  #/
        (25, 5, 125, does_not_raise()),
        ('hello', 3, 5, pytest.raises(ValueError)),
        (1, 'hello', 5, pytest.raises(ValueError)),
        ('hello', 'hello', 'hello', pytest.raises(ValueError)),
        (2, 1, 1, pytest.raises(AssertionError)),
        ('hello', 1, 'hello', pytest.raises(ValueError)),
    ])
    def test_mult_valid(self, a, b, result, expectation):  # Функция тестирования
        c = Calculator()
        with expectation:
            assert c.calc(f'{a} * {b}') == result

    @mark.parametrize('a, b, result, expectation', [ # Декоратор для указания и передачи аргументов для функции тестирования
        (2, 1, 1, does_not_raise()),    #\
        (2, -1, 3, does_not_raise()),  # } разлчиные связки аргументов для теста
        (2, 0, 2, does_not_raise()),  #/
        (-2, -1, -1, does_not_raise()),
        ('hello', 3, 5, pytest.raises(ValueError)),
        (1, 'hello', 5, pytest.raises(ValueError)),
        ('hello', 'hello', 'hello', pytest.raises(ValueError)),
        (2, 1, 2, pytest.raises(AssertionError)),
        ('hello', 1, 'hello', pytest.raises(ValueError)),
    ])
    def test_diff_valid(self, a, b, result, expectation):
        c = Calculator()
        with expectation:
            assert c.calc(f'{a} - {b}') == result

    @mark.parametrize('a, b, result, expectation', [ # Декоратор для указания и передачи аргументов для функции тестирования
        (1, 2, 3, does_not_raise()),  # \
        (1, -3, -2, does_not_raise()),  # } разлчиные связки аргументов для теста
        (1, 0, 1, does_not_raise()),  # /
        (-2, -3, -5, does_not_raise()),
        ('hello', 3, 5, pytest.raises(ValueError)),
        (1, 'hello', 5, pytest.raises(ValueError)),
        ('hello', 'hello', 'hello', pytest.raises(ValueError)),
        (2, 1, 1, pytest.raises(AssertionError)),
        ('hello', 1, 'hello', pytest.raises(ValueError)),
    ])
    def test_summ_valid(self, a, b, result, expectation):
        c = Calculator()
        with expectation:
            assert c.calc(f'{a} + {b}') == result


def test_input_valid():
    c = Calculator()
    assert c.calc("1 + 1"), [1, '+', 1]
    assert c.calc("-1 - 1"), [-1, '-', 1]
    assert c.calc("1 * -1"), [1, '*', -1]
    assert c.calc("-1 / -1"), [-1, '/', -1]

def test_raise_valid():
    c = Calculator()
    with pytest.raises(ZeroDivisionError):
        assert c.calc('10 / 0')
# def test_div(self):
#     app = Calculator()
#     self.assertEqual(app.calc("2 / 1"), 2.0)
#     self.assertEqual(app.calc("2 / -1"), -2.0)
#     with self.assertRaises(ZeroDivisionError):  # Метод для тестирования получаемых ошибок, работает в связке с with
#         app.calc("2 / 0")
#     self.assertEqual(app.calc("-2 / -1"), 2.0)