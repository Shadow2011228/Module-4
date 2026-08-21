import time
import random
from numba import njit


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

start = time.time()
data = fibonacci(35)
print(data)
print(time.time()-start)
