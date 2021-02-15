with open('text_3.txt', 'r') as file:
    arr_of_str = file.readlines()
    emp_dict = dict(zip([x.split()[0] for x in arr_of_str], [x.split()[1] for x in arr_of_str]))
    emp_with_more_tw = [x for x in emp_dict if float(emp_dict[x]) > 20000]
    salary_sum = 0
    for v in emp_dict.values():
        salary_sum += float(v)

    print(
        f'Сотрудники с зарплатой выше 20к {" ,".join(emp_with_more_tw)}. '
        f'Cредняя зарплата = {salary_sum / len(emp_dict)}')
