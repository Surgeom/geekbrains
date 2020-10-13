def my_func(x, y):
    # return x ** y
    if x >= 0 and y < 0:
        st = 1
        for i in range(abs(y)):
            st *= x
        return 1 / st
    else:
        print('ошиблшись в вводе начните заново')


num1 = float(input('Введите число действительное положительное число '))
num2 = int(input('Введите число целое отрицательное число '))

print(my_func(num1, num2))
