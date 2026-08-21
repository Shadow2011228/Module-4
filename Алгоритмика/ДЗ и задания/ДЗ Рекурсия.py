import random
import time
from numba import njit

def fank1(N, nums=[]):
    if len(nums) < N:
        nums.append(random.randint(0,30))
        fank1(N, nums)
    return nums
# @njit
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
# @njit
def split_and_merge_list(a):
    N = len(a) // 2
    a, b = a[:N], a[N:]
    if len(a) > 1:
        a = split_and_merge_list(a)
    if len(b) > 1:
        b = split_and_merge_list(b)

    return merge_list(a, b)

print(fank1(10))

start = time.time()
nums = split_and_merge_list(fank1(50))
print(nums)
print(time.time()-start)
