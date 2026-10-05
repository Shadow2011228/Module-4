from database import *
from pytest import mark
from pytest import fixture
from main import create_ice_cream



class TestMain:

    @mark.parametrize(
        "name, size, taste_id",
        [
            ("Шоколадный заяц", "Большой", 3),
            ("Банана", "Маленький", 4),
            ("Обычное", "Средний", 1),
        ]
    )
    def test_buy_icecream(self, name, size, taste_id):
        pass

    @mark.parametrize(
        "name, size, taste_id",
        [
            ("Шоколадный заяц", "Большой", 3),
            ("Банана", "Маленький", 4),
            ("Обычное", "Средний", 1),
        ]
    )
    def test_icecream_attrs(self, name, size, taste_id):
        ice = create_ice_cream(name, size, taste_id)
        data = s.query(IceCream).all()
        assert ice in data

    def test_nums_of_ice(self, delete_ices):
        ices = [
            ("Шоколадный заяц", "Большой", 3),
            ("Банана", "Маленький", 4),
            ("Обычное", "Средний", 1),
        ]
        for icecream in ices:
            create_ice_cream(*icecream)
        data = s.query(IceCream).all()
        assert len(data) == len(ices)

@fixture
def delete_ices():
    s.query(IceCream).delete()
    s.commit()
