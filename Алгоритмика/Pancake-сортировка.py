# Блинная сортировка
import random
import time

def pancake(data):
    if len(data) > 1:
        for size in range(len(data), 1, -1):
            maxindex = max(range(size), key=data.__getitem__)
            if maxindex + 1 != size:
                if maxindex != 0:
                    data[:maxindex + 1] = reversed(data[:maxindex + 1])
                data[:size] = reversed(data[:size])
    return data

data = [random.randint(1, 30000) for i in range(30000)]
# data = list(set(data))

start = time.time()
data = pancake(data)
print(time.time()-start)
print(data)