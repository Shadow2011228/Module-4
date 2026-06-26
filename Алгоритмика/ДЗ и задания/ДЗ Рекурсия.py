import random


def fank1(N, nums=[]):
    if len(nums) < N:
        nums.append(random.randint(0,30))
        fank1(N, nums)
    return nums

print(fank1(50))