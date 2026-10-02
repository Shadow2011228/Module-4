import os
from database import *
from pytest import mark

class TestDB:
    def test_connection(self):
        assert database_file in os.listdir()

    @mark.parametrize(
        "attr",
        [
            'id', 'name', 'weight'
        ]
    )
    def test_taste_attributes(self, attr):
        assert hasattr(Tastes, attr)

    @mark.parametrize(
        "attr",
        [
            'id', 'name', 'cone', 'taste_id'
        ]
    )
    def test_icecream_attributes(self, attr):
        assert hasattr(IceCream, attr)
