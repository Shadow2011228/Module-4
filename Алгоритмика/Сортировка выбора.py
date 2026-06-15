import random
import time


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

data = [random.randint(1, 30000) for i in range(30000)]
# data = list(set(data))

start = time.time()
data = choice_sort(data)
print(time.time()-start)
print(data)