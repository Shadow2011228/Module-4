import random


words_pool = ["яблоко", "кот", "программирование", "дом", "солнце",
             "книга", "автомобиль", "город", "река", "компьютер",
             "стол", "небо", "школа", "институт", "работа", "улица"]


random_words = []
for _ in range(10):
    random_word = random.choice(words_pool)
    random_words.append(random_word)

print("Случайный список слов:", random_words)


shortest_word = random_words[0]

for word in random_words:
    if len(word) < len(shortest_word):
        shortest_word = word

print("Самое короткое слово в списке:", shortest_word)
print("Его длина:", len(shortest_word), "символов")