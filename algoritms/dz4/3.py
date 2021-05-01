from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = 12345678910

for i in range(1, 4):
    print(f'func_{i}')
    print(timeit(f'revers_{i}(num)', setup=f'from __main__ import revers_{i}, num',
                 number=10000))
    print()
    run(f'revers_{i}(num)')

''' 3ья реалтзация самая эффективная так как не проходим список'''
