def def_func(a, b):
    try:
        c = round(a / b, 2)
        return f"Результат деления {a} на {b} = " + str(c)
    except ZeroDivisionError:
        return 'Ошибка при делении на ноль'

a = float(input("Введите делимое "))
b = float(input("Введите делитель "))
print(def_func(a, b))
