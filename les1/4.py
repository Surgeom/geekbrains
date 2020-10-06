num = int(input('Введите число '))
min_num = 9
while num > 0:
    x = num % 10
    if x < min_num:
        min_num = x
    num //= 10
print(min_num)
