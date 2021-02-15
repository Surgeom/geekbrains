with open('first.txt', 'w') as file:
    while True:
        txt_to_write = input('введите стр для записи в файл')
        if txt_to_write:
            file.write(txt_to_write+'\n')
        else:
            break
