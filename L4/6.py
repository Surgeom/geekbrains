from sys import argv
from itertools import count, cycle

some_arr = ['d', 30, -2]


def br(num, func):
    stop = 10
    arr = []
    for x in func(num):
        if x == stop: return arr
        arr.append(x)


def brk(sar, func):
    stop = 15
    arr = []
    i = 0
    for x in func(sar):
        arr.append(x)
        i += 1
        if i == stop: return arr


try:
    if argv[1] == 'a':
        if int(argv[2]) < 10:
            print(br(int(argv[2]), count))
        else:
            print('Введите число меньше 10')
    elif argv[1] == 'b':
        print(brk(some_arr, cycle))
except IndexError:
    print('неверный ввод начните заново')
except ValueError:
    print('неверный ввод начните заново')
