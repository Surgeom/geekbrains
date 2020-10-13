def user_data(**kwargs):
    return f'{" ".join([x for x in kwargs.values() if x != ""])}'


print(user_data(name=input("name="),
                surname=input('surname='),
                date_of_birth=input('date of bitrh='),
                city=input('your city='),
                email=input('your email='),
                phone=input('your phone=')
                ))
