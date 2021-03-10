import memory_profiler
import timeit
import random
import numpy as np

""""""


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


# для функций без аргументов
def decor2(funct):
    def wrapper():
        t1 = timeit.default_timer()
        rez = funct()
        time = timeit.default_timer() - t1
        memory_profiler.profile(funct).__call__()
        print(f'Время : {time}')
        return rez

    return wrapper


'''Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются 
элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. '''


@decor2
def smth1():
    arr = [random.randint(1, 100) for i in range(100000)]
    new_arr = []
    for i in range(0, len(arr), 2):
        try:
            new_arr.append(arr[i + 1])
            new_arr.append(arr[i])
        except IndexError:
            new_arr.append(arr[i])


smth1()


@decor2
def smth2():
    arr2 = [random.randint(1, 100) for i in range(100000)]
    last_num = None
    len_arr = len(arr2)

    if len_arr % 2 != 0:
        last_num = arr2.pop(-1)
        len_arr -= 1

    for i in range(0, len_arr, 2):
        arr2[i], arr2[i + 1] = arr2[i + 1], arr2[i]

    if last_num:
        arr2.append(last_num)


smth2()
'''в первом скрипте затрачивалось больше памяти так как создавался второй массив ,
 во втором скрипте убрал создание второго массива соответвенно расход памяти уменьшился'''

'''Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них.'''


@decor2
def rate():
    my_list = sorted([random.randint(1, 100) for i in range(100000)], reverse=True)
    new_el = 5
    len_mylist = len(my_list)

    if new_el in my_list:
        # ind = len_mylist - my_list[::-1].index(new_el)
        ind = my_list.index(new_el) + my_list.count(new_el)
        my_list.insert(ind, new_el)
    else:
        for x in my_list:
            if new_el > x:
                ind_to_insert = my_list.index(x)
                my_list.insert(ind_to_insert, new_el)
                break
            else:
                my_list.insert(len_mylist, new_el)
                break


rate()


@decor2
def rate2():
    my_list = sorted(np.random.randint(100, size=100000), reverse=True)
    new_el = 5
    len_mylist = len(my_list)

    if new_el in my_list:
        ind = len_mylist - my_list[::-1].index(new_el)
        my_list.insert(ind, new_el)
    else:
        for x in my_list:
            if new_el > x:
                ind_to_insert = my_list.index(x)
                my_list.insert(ind_to_insert, new_el)
                break
            else:
                my_list.insert(len_mylist, new_el)
                break


rate2()
''' в во втором варианте скорость быстрее так как numpy заточен под скорость ,
но памяти второй скрипт использует больше так же из за numpy'''
