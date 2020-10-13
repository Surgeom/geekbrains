def summa(arr):
    if 'q' in arr:
        arr = [int(x) for x in arr[:arr.index('q')] if x.isdigit()]
    else:
        arr = [int(x) for x in arr if x.isdigit()]
    return sum(arr)


res = 0
while True:
    string = input("введите строку чисел, разделенных пробелом (стоп слово =q) ").split()
    if 'q' in string:
        res += summa(string)
        print(res)
        break
    else:
        res += summa(string)
        print(res)
