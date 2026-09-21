import unittest
import math
from Square import *

class SqrTest(unittest.TestCase):
    def test_Sqr_available(self):
        app = Square()
        try:
            app.sqr(data="Круг" ,triangle=1)
        except AttributeError:
            self.fail("Функции sqr не существует!")

    def test_Sqr_Triangle(self):
        app = Square()
        self.assertEqual(app.sqr(data="Треуголник" , triangle=(2,2)), 2)

    def test_Sqr_Rhombus(self):
        app = Square()
        self.assertEqual(app.sqr(data="Ромб" , triangle=(2,2)), 2)

    def test_Sqr_Circle(self):
        app = Square()
        self.assertEqual(app.sqr(data="Круг" , triangle=1), 3.141592653589793)
