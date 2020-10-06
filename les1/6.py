a, b = int(input('a=')), int(input('b='))
days = 1
while True:
    print(f'{days}-й день:{a}')
    days += 1
    # a += round(a / 10 , 2)
    a += float(f'{a / 10:.2f}')
    if a > b:
        print(f'{days}-й день:{a}')
        break
