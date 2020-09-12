a = input("Введите начальное растояние ")
b = input("Введите целевое растояние ")
a = float(a)
b = float(b)
cntDay = 0
while a < b:
    a = a * 1.1
    cntDay = cntDay + 1
print(cntDay)