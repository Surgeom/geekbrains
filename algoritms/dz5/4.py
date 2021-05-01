from timeit import timeit
from collections import OrderedDict

n_dict = {}
o_dict = OrderedDict()
n = 1000


def n_dict_insert(num):
    for i in range(num):
        n_dict[i] = i


def o_dict_insert(num):
    for i in range(num):
        o_dict[i] = i


def n_d_pop():
    for i in [x for x in n_dict.keys()]:
        n_dict.pop(i)


def o_d_pop():
    for i in [x for x in o_dict.keys()]:
        o_dict.pop(i)


print(timeit('n_dict_insert(n)', setup='from __main__ import n_dict_insert, n',
             number=10000))
print(timeit('o_dict_insert(n)', setup='from __main__ import o_dict_insert, n',
             number=10000))
print()

print(timeit('n_d_pop()', setup='from __main__ import n_d_pop',
             number=10000))
print(timeit('o_d_pop()', setup='from __main__ import o_d_pop',
             number=10000))

''' скорость операции  добавлениия в dict быстрее чем в Ordereddict 
, а при удалении элементов наоборот , начиная с версии 3,6 смысл ordereddict в доп функционале move_to_end '''
