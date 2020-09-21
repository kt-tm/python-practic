import os.path
# 1 задание
if os.path.isfile("1.txt") == True:
    print("Файл уже существует")
else:
    with open("1.txt", "w", encoding="utf-8") as my_file:
        while True:
            new_line = input("Введите строку для записи ")
            if new_line == '':
                break
            my_file.write(f"{new_line}\n")

# 2 задание
if os.path.isfile("1.txt") == False:
    print("Файла не существует")
else:
    my_file = open("1.txt", "r", encoding="utf-8")
    cnt_line = 0
    for i in my_file.readlines():
        cnt_line = cnt_line + 1
        print(f"В строке № {cnt_line} количество строк = {len(i.split())}")
    my_file.close()