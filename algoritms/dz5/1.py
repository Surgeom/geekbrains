from collections import namedtuple
"""


дз 6 сдам в течении 2ух дней ,прощу прощения за задержку ,очень извиняюсь




"""
n = int(input("введите число компаний"))
comps_tuple = namedtuple('Companies', 'name p1 p2 p3 p4')
dict_of_comp_avgp = {}
for i in range(n):
    company = comps_tuple(name=input("введите название компании "),
                          p1=int(input('введите прибыль за первый период')),
                          p2=int(input('введите прибыль за второй период')),
                          p3=int(input('введите прибыль за третий период')),
                          p4=int(input('введите прибыль за четвертый период'))
                          )
    dict_of_comp_avgp[company.name] = (company.p1 +
                                       company.p2 +
                                       company.p3 +
                                       company.p4) / 4

avg_p = sum(dict_of_comp_avgp.values()) / n

print(f'компании с прибылью выше средней: {",".join([k for k, v in dict_of_comp_avgp.items() if v > avg_p])}')
print()
print(f'компании с прибылью ниже средней: {",".join([k for k, v in dict_of_comp_avgp.items() if v < avg_p])}')
