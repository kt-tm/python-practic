class ZeroDivider(Exception):
    def __init__(self, txt):
        self.txt = txt
try:
    a = int(input('Введите целое делимое '))
    b = int(input('Введите целое делитель '))
    if b == 0:
        raise ZeroDivider("Невозможно деление на ноль")
except ValueError:
    print('Введеные числа должны быть челыми!')
except ZeroDivider as err:
    print(err)
else:
    print(f"{round(a / b)}")

