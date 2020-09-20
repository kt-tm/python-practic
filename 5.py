from functools import reduce
d = [i for i in range(100, 1001, 2)]
def func_multiplic(a, b):
    return a * b
print(reduce(func_multiplic, d))
