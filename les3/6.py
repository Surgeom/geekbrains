def int_func(word):
    f = True
    for symb in word:
        if ord(symb) < ord('a') or ord(symb) > ord('z'):
            f = False
    if f:
        return word.title()
    else:
        return word


string = input('введите слова разделенные пробелом ')

print(' '.join(map(int_func, string.split())))
