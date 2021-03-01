def time_func(f):
    import time

    def decor(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        print(f' Время выполнения: {end - start:.12f} секунд.')

    return decor


a = []
d = {}


@time_func
def arr_items(arr, n):
    for i in range(n):
        arr.append(i)


@time_func
def dict_items(dic, n):
    for i in range(n):
        dic[i] = i


arr_items(a, 10000)
dict_items(d, 10000)

# списки быстрее ,так как при заполнение словаря значений добавляется больше
print('добавление элемента')
print()


@time_func
def arr_item_apend(arr):
    arr.append(1)


@time_func
def dict_item_apend(d):
    d['new'] = 1


arr_item_apend(a)
dict_item_apend(d)
# при добавлении элемента в конец списки быстрее так как добавляется одно значение а не 2
print('удаление элемента')
print()


@time_func
def arr_items_rm(arr):
    arr.clear()


@time_func
def dict_items_rm(d):
    d.clear()


arr_items_rm(a)
dict_items_rm(d)

# так же как и добавление элементов
