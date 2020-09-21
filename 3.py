import os.path
def fnc_get_file_stat(file_name):
    if os.path.isfile(file_name) == False:
        return "Файл не существует"
    sal_sum = 0
    fio_lst = ""
    cnt = 0
    try:
        with open(file_name, "r", encoding="utf-8") as file_open:
            for i in file_open:
                fio = i.split()[0]
                sal = float(i.split()[1])
                fio_lst = fio_lst + "\n" + fio if sal < 20000.00 else fio_lst
                sal_sum += sal
                cnt += 1
        return f"Средняя зарплата = {sal_sum / cnt}\nПеречень сотрудников зарабатывающих менее 20 ты. руб:{fio_lst}"
    except ZeroDivisionError:
        return "Файл не заполнен"

print(fnc_get_file_stat("text_3.txt"))