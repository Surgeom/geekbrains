def my_func(a, b, c):
    arr = [a, b, c]
    arr.remove(min(arr))
    return sum(arr)


print(my_func(int(input("Введите число 1 ")), int(input("Введите число 2 ")), int(input("Введите число 3 "))))
