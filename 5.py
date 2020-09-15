s_in = 0
t_in = 0
pr_exec_func = True
def my_func1(s, total_sum_in = 0):
    global sum, total_sum
    sum = 0
    total_sum = total_sum_in
    for i in s.split():
        if i == 'q':
            total_sum = total_sum + sum
            return False
        try: i = int(i)
        except ValueError:
            continue
        sum = sum + int(i)
    total_sum = total_sum + sum
    return True

while pr_exec_func == True:
    s = input("Введите строку чисел разделенных пробелом, для завершения введите символ q ")
    pr_exec_func = my_func1(s, t_in)
    s_in = sum
    t_in = total_sum
    print(f"Сумма в строке = {s_in}, Общая сумма = {t_in}")








