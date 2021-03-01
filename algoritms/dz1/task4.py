# var1
dict_of_users = {'user1': '123',
                 'user2': '154',
                 'user3': '456'}
active_users_arr = ['user1', 'user2']


def check_auth(login, password):
    if login in active_users_arr:
        return f'user with login {login} already activated'
    elif login not in dict_of_users.keys():
        return f'not {login} user account go to registration'
    elif dict_of_users[login] != password:
        return 'wrong password'
    else:
        active_users_arr.append(login)
        return "OK"


# O(1)
print(check_auth('user3', '456'))

# var2
dict_of_users2 = {'user1': [True, '123'],
                  'user2': [True, '154'],
                  'user3': [False, '456']}


def check_auth2(login, password):
    for k in dict_of_users2.keys():
        if k == login:
            if dict_of_users2[k][1] == password and dict_of_users2[k][0] == False:
                return 'OK'
            elif dict_of_users2[k][1] != password and dict_of_users2[k][0] == False:
                return 'wrong password'
            elif dict_of_users2[k][0]:
                return f'{login} user allready active'

    return f'not {login} user account go to registration'


# O(n)
print(check_auth2('user', '456'))
