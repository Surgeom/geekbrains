def users_data(**kwargs):
    return f'{" ".join([x for x in kwargs.values() if x != ""])}'


print(users_data(name=input('Введите имя'),
                 surname=input('Введите фамилию'),
                 birth_date=input('Введите дату рождения'),
                 city=input('Введите город '),
                 email=input('Введите email'),
                 phone_number=input('Введите номер телефона')
                 ))
