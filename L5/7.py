import json

with open('text_7.txt', 'r') as file:
    ar_of_str = file.readlines()
    dict_of_firms = dict(zip([x.split()[0] for x in ar_of_str],
                             [int(x.split()[2]) - int(x.split()[3]) for x in ar_of_str]))
    plus = [dict_of_firms[x] for x in dict_of_firms if dict_of_firms[x] > 0]
    average_profit_dict = {"average_profit": round(sum(plus) / len(plus), 2)}
    data = [dict_of_firms, average_profit_dict]

with open('text_7.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
