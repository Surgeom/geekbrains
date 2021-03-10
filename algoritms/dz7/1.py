import memory_profiler
import timeit
import random


def decor(func):
    def wrapper(*args, **kwargs):
        t1 = timeit.default_timer()
        m1 = memory_profiler.memory_usage()
        rez = func(*args, **kwargs)
        time = timeit.default_timer() - t1
        m2 = memory_profiler.memory_usage()
        mem = m2[0] - m1[0]
        print(f'Время : {time}')
        print(f'Затраченная память :{mem}')
        return rez

    return wrapper


@decor
def bSort1(array):
    l = len(array)
    for i in range(l):
        for j in range(0, l - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


@decor
def bSort2(array):
    f = False
    l = len(array)
    for i in range(l - 1):
        if array[i] > array[i + 1]:
            f = True
            break
    if f:
        for i in range(l):
            for j in range(0, l - i - 1):
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


a = [random.randint(1, 100) for i in range(10000)]

bSort1(a[:])
bSort2(a[:])
'''доработка была по примеру ,помогла бы только если массив был сортирован уже ,
тогда бы сложность была бы на порядок меньше'''
