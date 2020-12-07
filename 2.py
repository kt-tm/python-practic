list = input("Введите список ")
list = list.split()
l = len(list)
for i in range(l):
    if i % 2 == 1:
        p = list[i - 1]
        list[i - 1] = list[i]
        list[i] = p
print(list)