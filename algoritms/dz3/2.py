import hashlib

password = 123
login = 'jack'
jacks_hash = hashlib.sha256(f'{login}'.encode() + f'{password}'.encode()).hexdigest()

user_login = input('введите логин')
user_pas = input('введите пароль')
user_hash = hashlib.sha256(f'{user_login}'.encode() + f'{user_pas}'.encode()).hexdigest()
if user_hash == jacks_hash:
    print('OK')
else:
    print('wrong pass')
