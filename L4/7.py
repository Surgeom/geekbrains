from sys import argv


def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial


# если учитывать факториал от 0 == 1 то в range заменить начало с 1 на 2

try:
    for x in fact(int(argv[1])):
        print(x)
except IndexError:
    print('неверный ввод начните заново')
except ValueError:
    print('неверный ввод начните заново')
