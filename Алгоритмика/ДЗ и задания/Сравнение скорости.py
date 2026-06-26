import random
import time


def bingo(data):
    max = len(data) - 1  # Индекс последнего
    nextValue = data[max]  # Последний элемент
    for i in range(max - 1, -1, -1):
        if data[i] > nextValue:
            nextValue = data[i]

    while max and data[max] == nextValue:
        max -= 1
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

def choice_sort(dataset):
    N = len(dataset)
    for a in range(N - 1):
        m = dataset[a]
        p = a
        for b in range(a + 1, N):
            if m < dataset[b]:
                m = dataset[b]
                p = b
        if p != a:
            t = dataset[a]
            dataset[a] = dataset[p]
            dataset[p] = t
    return dataset


data = [random.randint(1, 3000) for i in range(30000)]

start = time.time()
data = bingo(data)
print(time.time()-start)
print(data)
print('==============================')
start = time.time()
data = choice_sort(data)
print(time.time()-start)
print(data)