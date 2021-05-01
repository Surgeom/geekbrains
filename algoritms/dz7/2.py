import operator
import random
import timeit


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr, compare=operator.lt):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        return merge(left, right, compare)


k = 10
for i in range(1, 5):
    a = [random.randint(0, 50) for j in range(k)]
    # print(a)
    print(timeit.timeit("merge_sort(a)[:]", globals=globals(), number=1000))
    # print(merge_sort((a[:])))
    k *= 10
