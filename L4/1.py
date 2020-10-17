from sys import argv

try:
    hours = int(argv[1])
    salary_in_hour = int(argv[2])
    prize = int(argv[3])
    salary = (hours * salary_in_hour) + prize
    print(f'зарплата сотрудника состовляет {salary}')
except IndexError:
    print('неверный ввод начните заново')
except ValueError:
    print('неверный ввод начните заново')