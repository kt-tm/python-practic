from sys import argv
sc_name, cnt_hour, rate_hour, proc_bonus = argv
salary = round(float(cnt_hour) * float(rate_hour) * (1 + float(proc_bonus)/100), 2)
print(salary)