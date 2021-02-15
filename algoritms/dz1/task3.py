d = {'1company': 3000,
     '2company': 5000,
     '3company': 1000,
     '4company': 500,
     '5company': 10000}
# var1
rezdict = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])[:3]}
# O(n logn)
print(rezdict)

# var2
arr_of_companies = []
n = 0
for k, v in sorted(d.items(), key=lambda x: x[1]):
    arr_of_companies.append(k)
    if len(arr_of_companies) >= 3:
        break
# O(n logn)
print(arr_of_companies)

# 1ый вариант быстрее так как генераторы быстрее