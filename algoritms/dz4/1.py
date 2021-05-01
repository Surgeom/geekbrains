from timeit import timeit
from functools import partial

arr = [x for x in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit(partial(func_1, arr)))


def func_2(nums):
    return [x for x in nums if x % 2 == 0]


print(timeit(partial(func_2, arr)))

# генерация  спискового включения  быстрее чем генерация с помощью  цикла с апенд
