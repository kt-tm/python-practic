def my_func1(a, b):
    if b > 0:
        return "Введена некорректная степень"
    elif a == 0:
        return "Результат возведения 0 в отрицательную степень = бесконечность"
    return "1. Результат возведения {a} в степень {b} = " + str(round(a ** b, 3))

def my_func2(a, b):
    if b > 0:
        return "Введена некорректная степень"
    elif a == 0:
        return "Результат возведения 0 в отрицательную степень = бесконечность"
    result = 1
    for i in (range(abs(b))):
        result = result / a
    return "2. Результат возведения {a} в степень {b} = " + str(round(result, 3))

a = float(input("Введите основание "))
b = int(input("Введите отрицательную степень "))
print(my_func1(a, b))
print(my_func2(a, b))

