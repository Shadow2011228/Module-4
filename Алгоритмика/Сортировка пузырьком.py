import random
import time

def bubble(data):
    N = len(data)
    for i in range(0,N-1):
        for j in range(0, N - 1 - i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


data = [random.randint(1, 30000) for i in range(30000)]
data = list(set(data))

start = time.time()
data = bubble(data)
print(time.time()-start)
print(data)