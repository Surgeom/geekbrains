time_in_sec = int(input('Введите число в секундах '))
hours = time_in_sec // 3600
minutes = (time_in_sec - hours * 3600) // 60
sec = (time_in_sec - hours * 3600) % 60  # ну или вычесть из time_in_sec часов *3600 и минут *60
print(f'{hours}:{minutes}:{sec}')
# print(f'{time_in_sec // 3600}:{(time_in_sec - hours * 3600) // 60}:{(time_in_sec - hours * 3600) % 60}')
