l = [6, 5, 4, 3, 2, 1]


# O(n^2)
def min_value1(arr):
    for i in range(len(arr)):
        f = True
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                f = False
        if f:
            return arr[i]


print(min_value1(l))


# O(n)
def min_value2(arr):
    min_val = arr[0]
    for i in range(len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
    return min_val


print(min_value2(l))
