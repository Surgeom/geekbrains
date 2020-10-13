def my_func(x, y):
    # return x**y
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res


num1 = float(input('действительное положительное число ='))
num2 = int(input('целое отрицательное число = '))

if num2 < 0:
    print(my_func(num1, num2))
else:
    print('wrong input')
