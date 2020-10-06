proceeds = int(input('Ввведите выручку '))
costs = int(input('Ввведите издержки '))
print()

pozitive_d = True if proceeds > costs else False
if pozitive_d:
    print('фирма работает в прибыль')
    print()

    profit = proceeds - costs
    profitability = float(f'{(profit / proceeds):.2f}')
    print('рентабельность = ' + str(profitability))
    print()

    employers_num = int(input('Введите кол-во сотрудников '))
    print()

    profit_for_one_emp = float(f'{(profit / employers_num):.2f}')
    print('Прибыль на одного сотрудника=' + str(profit_for_one_emp))
else:
    print('Фирма работает в убыток')
