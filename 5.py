import random, os.path
d = [random.randint(0, 500) for i in range(10)]
if os.path.isfile("5.txt") == True:
    print("Файл уже существует")
else:
    file_open = open("5.txt", "w", encoding="utf-8")
    for i in d:
        file_open.write(f"{i} ")
    file_open.close()

sum = 0
file_open = open("5.txt", "r", encoding="utf-8")
for i in file_open.readline().split():
    sum += int(i)
file_open.close()
print(sum)
