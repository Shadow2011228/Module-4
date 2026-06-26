import random
import time


def quick_sort(data):
    if len(data) > 1:
        x = data[random.randint(0, len(data) - 1)]
        low = [u for u in data if u < x]
        eq = [u for u in data if u == x]
        hi = [u for u in data if u > x]
        data = quick_sort(low) + eq + quick_sort(hi)
    return data

data = [random.randint(1, 30000) for i in range(3000000)]
data = list(set(data))

start = time.time()
data = quick_sort(data)
print(data)
print(time.time()-start)
