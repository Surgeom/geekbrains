import re


def find_num_sum(s):
    nums = re.findall(r'\d+', s)
    return sum(map(int, nums))


with open('text_6.txt', 'r') as file:
    ar_of_str = file.readlines()
    dict_of_les = dict(zip([x.split()[0] for x in ar_of_str], [find_num_sum(x) for x in ar_of_str]))
    print(dict_of_les)
