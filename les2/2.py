arr = input('Введите элементы массива через пробел ').split()

arr = [int(x) for x in arr]
# arr = list(map(int, input('Введите элементы массива через пробел ').split()))
last_num = None
len_arr = len(arr)

if len_arr % 2 != 0:
    last_num = arr.pop(-1)
    len_arr -= 1

for i in range(0, len_arr, 2):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]

if last_num:
    arr.append(last_num)
print(arr)
