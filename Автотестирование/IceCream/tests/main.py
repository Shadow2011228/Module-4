from database import *


def create_ice_cream(name, cone, taste_id):
    taste = s.query(Tastes).filter_by(id=taste_id).first()  # Поиск вкуса
    if taste:
        if taste.weight > 0:
            # Проверка доступного веса начинки
            ice_cream = IceCream(name=name, cone=cone, taste_id=taste_id)
            s.add(ice_cream)
            taste.weight -= 0.1  # Вычитаем вес начинки из Tastes
            s.commit()
            return ice_cream
        else:
            raise TypeError("Недостаточно начинки")
    else:
        raise TypeError("Вкус не найден")

# if __name__ == '__main__':
#     create_ice_cream("Маленький шоколад", "Маленький", 3)
#     create_ice_cream("Клубника", "Средний", 1)
#     create_ice_cream("Банан", "Маленький", 2)
#     create_ice_cream("Шоколад", "Большой", 4)
#     create_ice_cream("Фисташка", "Маленький", 2)
#     create_ice_cream("Малина", "Средний", 1)
#     create_ice_cream("Банан-клубника", "Маленький", 1)
#     create_ice_cream("малина-банан", "Средний", 3)
#     create_ice_cream("Шоколад-клубника", "Большой", 1)
#     create_ice_cream("Шоколад-банан", "Большой", 2)
#     create_ice_cream("Малина-шоколад", "Маленький", 1)
