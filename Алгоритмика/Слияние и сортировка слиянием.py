import random
import time


def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)
    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c

def split_and_merge_list(a):
    N = len(a) // 2
    a, b = a[:N], a[N:]
    if len(a) > 1:
        a = split_and_merge_list(a)
    if len(b) > 1:
        b = split_and_merge_list(b)

    return merge_list(a, b)



data = [random.randint(1, 30000) for i in range(3000000)]
data = list(set(data))

start = time.time()
data = split_and_merge_list(data)
print(data)
print(time.time()-start)
