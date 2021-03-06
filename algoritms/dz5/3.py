from collections import deque
from timeit import timeit

a = [x for x in range(1000)]
b = deque(a)
c = 154


def apend_to_lidst(num):
    a.append(num)


def apend_to_deque(num):
    b.append(num)


def apendleft_to_list(num):
    a.insert(0, num)


def apendleft_to_deque(num):
    b.appendleft(num)


def pop_list(num):
    a.pop()


def pop_deque(num):
    b.pop()


def pop_left_list(num):
    a.pop(0)


def pop_left_deque(num):
    b.popleft()


print(timeit('apend_to_lidst(c)', setup='from __main__ import apend_to_lidst, c',
             number=10000))
print(timeit('apend_to_deque(c)', setup='from __main__ import apend_to_deque, c',
             number=10000))
print()
print(timeit('apendleft_to_list(c)', setup='from __main__ import apendleft_to_list, c',
             number=10000))
print(timeit('apendleft_to_deque(c)', setup='from __main__ import apendleft_to_deque, c',
             number=10000))
print()
print(timeit('pop_list(c)', setup='from __main__ import pop_list, c',
             number=10000))
print(timeit('pop_deque(c)', setup='from __main__ import pop_deque, c',
             number=10000))
print()
print(timeit('pop_left_list(c)', setup='from __main__ import pop_left_list, c',
             number=10000))
print(timeit('pop_left_deque(c)', setup='from __main__ import pop_left_deque, c',
             number=10000))

''' При операции добавления и операции удаления элемента в конец списка/очереди скорость не сильно различается
но при операциях удаления и добавления в начало скорость выполнения этих операций значительней быстрее '''
