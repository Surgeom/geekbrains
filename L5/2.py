with open('first.txt', 'a') as file:
    while True:
        txt_to_write = input('введите стр для записи в файл')
        if txt_to_write:
            file.write(txt_to_write + '\n')
        else:
            break

with open('first.txt', 'r') as file:
    arr_of_str = file.readlines()
    count_lines = len(arr_of_str)
    arr_of_words_in_str = []
    for string in arr_of_str:
        arr_of_words_in_str.append(len([x for x in string.split()]))

    print(f'кол-во строк ={count_lines},кол-во строк в строках={arr_of_words_in_str}')
