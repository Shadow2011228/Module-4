import math

class Square:
    def __init__(self):
        self.operators = '+-*/'

    def sqr(self, data: str, triangle):

        if data == "Треуголник":
            return 0.5 * triangle[0] * triangle[1]

        elif data == "Ромб":
            return (triangle[0] * triangle[1]) / 2

        elif data == "Круг":
            return math.pi * (triangle ** 2)