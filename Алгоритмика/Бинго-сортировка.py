data = [8, 7, 87, 87, 87, 87, 87, 85, 64, 534, 78, 87, 87, 87]

def bingo(data):
    # Первый проход
    max = len(data) - 1  # Индекс последнего
    nextValue = data[max]  # Последний элемент
    for i in range(max - 1, -1, -1):
        if data[i] > nextValue:
            nextValue = data[i]

    while max and data[max] == nextValue:
        max -= 1
    # Последующие проходы
    while max:
        value = nextValue
        nextValue = data[max]  # Последний элемент

        for i in range(max - 1, -1, -1):
            if data[i] == value:
                data[i], data[max] = data[max], data[i]
                # Меняем местами со счетчиком
                max -= 1  # сдвигаем счётчик влево

            elif data[i] > nextValue:
                nextValue = data[i]

        while max and data[max] == nextValue:
            max -= 1
    return data

print(bingo(data))

