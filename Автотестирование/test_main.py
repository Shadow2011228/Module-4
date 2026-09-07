from main import *


def test_perimeter_of_faces():
    assert perimeter_of_faces(0,0,0) == 0
    assert perimeter_of_faces(1,2,3) == 24

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

test_perimeter_of_faces()
test_avg_perimeter()
test_area_of_sides()
test_avg_area()
test_volume()