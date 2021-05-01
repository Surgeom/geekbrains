import memory_profiler
import timeit
import random
from statistics import median


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


def gnome(arr):
    i, size = 1, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


@decor
def median1(ar):
    arr = gnome(ar)
    half = len(arr) // 2
    return (arr[half] + arr[~half]) / 2


@decor
def median2(ar):
    for x in ar:
        arr = ar[:]
        arr.pop(ar.index(x))
        m = [num for num in arr if num <= x]
        b = [num for num in arr if num > x]
        if len(m) == len(b):
            return x
    return None


@decor
def median3(ar):
    arr = ar[:]
    for i in range(len(ar) // 2):
        arr.pop(ar.index(max(arr)))
    return max(arr)

@decor
def median4(ar):
    return median(ar)


a = [random.randint(0, 50) for j in range(1001)]


print(median1(a))
print()
print(median2(a))
print()
print(median3(a))
print()
print(median4(a))
"""  statistics.median  самая быстрая бможно сказать встроенная так что на скорость хорошая,
 вариант с макс на втором месте так как на пол цикла меньше других и используется встроенная функция макс,
 2ая самая медленная так как каждый раз генерируются списки сложность на порядок выше """