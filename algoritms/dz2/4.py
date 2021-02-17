n = int(input('ВВедите n'))

arr = []


def strick(n, fn=1):
    if n == 0:
        return 0
    if n == 1:
        arr.append(fn)
    else:
        arr.append(fn)
        fn = -(fn / 2)
        n -= 1
        strick(n, fn)
    return sum(arr)


print(strick(n))
