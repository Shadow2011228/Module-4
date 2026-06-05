import random
import time

#               модуль random
num = random.randint(0, 10)  # Создает случайное число в диапазоне.

list = [1, 2, 3, 4, "ghjbdt", "", [12, 3, 4]]
rand_elem = random.choice(list) # Выбирает рандомный элемент чего-либо.

print('Рандомное число:', num)
print('Рандомный элемент:', rand_elem)

#               модуль time
print("Начало отсчета")
time.sleep(3) # Отсчитать до 3 секунд
print("Конец 3-ух секундного отсчета")
time.sleep(0.5) # Отсчитать до 3 секунд
print("Конец 0.5 сек отсчета")




