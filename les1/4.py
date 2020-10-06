num = int(input('Введите число '))
max_num = 0
while num > 0:
    x = num % 10
    if x > max_num:
        max_num = x
    num //= 10
print(max_num)
