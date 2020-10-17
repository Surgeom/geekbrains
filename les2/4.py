arr_of_words = input('Введите слова ').split()
for ind, word in enumerate(arr_of_words):
    print(ind + 1, word[:10])
