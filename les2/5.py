my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент '))
len_mylist = len(my_list)

if new_el in my_list:
    # ind = len_mylist - my_list[::-1].index(new_el)
    ind = my_list.index(new_el) + my_list.count(new_el)
    my_list.insert(ind, new_el)
else:
    for x in my_list:
        if new_el > x:
            ind_to_insert = my_list.index(x)
            my_list.insert(ind_to_insert, new_el)
            break
        else:
            my_list.insert(len_mylist, new_el)
            break
print(my_list)
