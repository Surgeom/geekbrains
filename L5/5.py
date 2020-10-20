from random import randint

with open('fifth.txt', 'w') as file:
    file.write(" ".join([str(randint(0, x)) for x in range(10)]))
with open('fifth.txt', 'r') as file:
    ar_of_str = file.readlines()
    print(sum(map(int, ar_of_str[0].split())))
