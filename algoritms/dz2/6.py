from random import randint

number = randint(1, 101)


def gues(num, n=10):
    if n == 0:
        return print('looose')
    else:
        user_num = int(input("введите число"))
        if user_num > num:
            print("меньше")
            n -= 1
            gues(num, n)
        elif user_num < num:
            print('больше')
            n -= 1
            gues(num, n)
        elif user_num == num:
            return print('win')


print(gues(number))
