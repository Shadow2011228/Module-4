from main_figures import *
from pytest import mark

@mark.parametrize('a, b, c, result', [ # Декоратор для указания и передачи аргументов для функции тестирования
    (0,0,0,0),    #\
    (1,2,3,24)  # } разлчиные связки аргументов для теста
])
def test_perimeter_of_faces(a, b, c, result):
    assert perimeter_of_faces(a,b,c) == result
    # assert perimeter_of_faces(0,0,0) == 0
    # assert perimeter_of_faces(1,2,3) == 24

def test_avg_perimeter():
    assert avg_perimeter(12) == 2

def test_area_of_sides():
    assert area_of_sides(2,4,6) == 88
    assert area_of_sides(3,6,9) == 198

def test_avg_area():
    assert avg_area(12) == 2

def test_volume():
    assert volume(4,8,12) == 384
    assert volume(5,10,15) == 750

