import random
import time


def insertion(data):
    N = len(data)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:data[j], data[j - 1] = data[j - 1], data[j]
            else:   break

    return data

data = [random.randint(1, 30000) for i in range(30000)]
data = list(set(data))

start = time.time()
data = insertion(data)
print(time.time()-start)
print(data)