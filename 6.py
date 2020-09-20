from itertools import count, repeat
start = int(input("Введите стартовое число (менее 15) "))
d = []
d_repeat = []
for el in count(start):
    if el > 15:
        break
    else:
        d.append(el)
print(d)
for el in repeat(d, 4):
    d_repeat.extend(d)
print(d_repeat)