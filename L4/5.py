from functools import reduce
import operator

print(reduce(operator.mul, [x for x in list(range(100, 1001)) if x % 2 == 0]))