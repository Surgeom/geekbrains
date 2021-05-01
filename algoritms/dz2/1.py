def calcul():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода):')
    if operation == "0":
        return 'bye'
    elif operation == "-" or operation == '+' or operation == '*' or operation == '/':
        num1 = int(input('Введите первое число'))
        num2 = int(input('Введите второе число'))
        if operation == '+':
            print(f' {num1 + num2}')
        elif operation == '-':
            print(f'{num1 - num2}')
        elif operation == '*':
            print(f'{num1 * num2}')
        elif operation == '/':
            try:
                print(f'{num1 / num2}')
            except ZeroDivisionError:
                print('Делить на 0 нельзя')
    else:
        print('неверный ввод')
    print(calcul())


print(calcul())
