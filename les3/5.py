def summa(arr):
    if 'q' not in arr:
        return sum(map(int, arr))
    else:
        return sum(map(int, arr[:arr.index('q')]))


result = 0
while True:
    s = input("Введите строку чисел, разделенных пробелом (стоп символ = 'q')").split()
    if 'q' in s:
        result += summa(s)
        print(result)
        break
    else:
        result += summa(s)
        print(result)
