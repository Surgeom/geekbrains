d = {'one': 'Один',
     'two': 'Два',
     'three': 'Три',
     'four': 'Четыре'}


def translation(s):
    for x in d:
        if x in s.lower():
            return s.lower().replace(x, d[x])


with open('text_4.txt', 'r') as file:
    arr_to_write = [translation(x) for x in file.readlines()]

with open('test_4.txt', 'w') as file:
    for x in arr_to_write:
        file.write(x)
