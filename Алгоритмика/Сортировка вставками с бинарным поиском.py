import random
import time


def insertion_binary(data):
    N = len(data)
    for i in range(1, N):
        key = data[i]
        lo, hi = 0, i

        while lo < hi:
            mid = (lo + hi) // 2
            if key < data[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        for j in range(i, lo, -1):
            data[j] = data[j - 1]

        data[lo] = key
    return data

data = [random.randint(1, 30000) for i in range(30000)]
data = list(set(data))

start = time.time()
data = insertion_binary(data)
print(data)
print(time.time()-start)
