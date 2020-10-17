arr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([x for x in arr if x > arr[arr.index(x) - 1]][1:])

