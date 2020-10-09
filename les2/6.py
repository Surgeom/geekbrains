count_product = int(input('Введите кол-во позиций товара '))
structure = []
keys_for_d = ['название', 'цена', 'кол-во', 'ед']
a_dict = dict.fromkeys(keys_for_d)
for x in a_dict:
    a_dict[x] = []
for i in range(0, count_product):
    structure.append((i + 1,
                      {keys_for_d[0]: input('Введите название товара '), keys_for_d[1]: input('цену '),
                       keys_for_d[2]: input('кол-во '),
                       keys_for_d[3]: input('ед ')}))

for i in range(count_product):
    for j in range(len(keys_for_d)):
        a_dict[keys_for_d[j]].append(structure[i][1][keys_for_d[j]])

print(a_dict)
