import time
from loguru import logger



class HowTime:
    speeds = {
        "Рыбе": 2.5,
        "Человеку": 4,
        "Велосипеду": 30,
        "Горилле": 34,
        "Слону": 40,
        "Лосю": 45,
        "Носорогу": 48,
        "Кенгуру": 56,
        "Собаке": 72,
        "Соколу": 80,
        "Лошади": 88,
        "Гепарду": 120,
        "Автомобилю": 200,
        "Мотоциклу": 350,
        "Истребителю": 3700
    }

    def __init__(self):
        self.distance = 0
        self.answer = ""

    def ask_distance(self):
        time.sleep(0.5)
        distance = input("Введи расстояние в метрах → ")
        if not distance.isnumeric():
            logger.warning("Внимание! Неожиданное поведение!")
            return False
        self.distance = float(distance)

        return True

    def min_to_hours(self, sec):
        sec = sec % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60
        temp = "%02d:%02d:%02d" % (hour, min, sec)
        return temp

    def math(self):
        for name, speed in self.speeds.items():
            t = (self.distance / 1000) / speed
            t *= 60 * 60
            t = self.min_to_hours(t)
            self.final(t, name)
        time.sleep(1)
        print(self.answer)

    def final(self, result: str, name: str):
        temp = f"Для прохождения {int(self.distance)} метров {name} понадобится {result} времени\n"
        self.answer += temp
        logger.info(temp)


if __name__ == '__main__':
    logger.success("Нашальника мы запустилися")
    hw = HowTime()
    good = hw.ask_distance()
    if good:
        hw.math()
    else:
        logger.error("Ошибка! Бим Бим Бам Бам")
