from database import *
from pytest import mark



class TestMain:

    @mark.parametrize(
        "name, size, taste_id"
    )
    def test_buy_icecream(self, name, size, taste_id):
        pass
