number = int(input('Введите число'))


def reversenum(num, s=0):
    if len(str(num)) == 1:
        s = str(num)
        return s
    else:
        s = str(num % 10)
        num = num // 10
        return s + reversenum(num, s)


print(reversenum(number))
