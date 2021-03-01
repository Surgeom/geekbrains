from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 6, 1, 1, 1, 5, 5, 6, 7, 8, 9, 11, 2, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 4]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())


def func_3():
    dict_count_items = {array.count(x): x for x in set(array)}
    a = max(dict_count_items.keys())
    return f'Чаще всего встречается число {dict_count_items[a]}, ' \
           f'оно появилось в массиве {a} раз(а)'


print(func_3())

for i in range(1, 4):
    print(timeit(f'func_{i}', setup=f'from __main__ import func_{i}',
                 number=100000))
    print()


#