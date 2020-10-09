seasons = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], 'Осень': [9, 10, 11]}

pol_inp = int(input("введите месяц в виде числа от  от 1 до 12 "))
f = False

for x in seasons:
    if pol_inp in seasons[x]:
        print(f'{pol_inp}- это {x}')
        f = True

if not f:
    print("проверьте ввод")
