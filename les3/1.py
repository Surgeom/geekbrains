def divide(a, b):
    return round(a / b, 2)


num1 = int(input('Введите число 1 '))
num2 = int(input('Введите число 2 '))
if num2 == 0:
    print('на ноль делить нельзя')
else:
    print(divide(num1, num2))
