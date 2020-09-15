def my_func(*args):
    mn = min(args)
    result = sum(args) - min(args)
    return result

a = float(input("Введите первое значение "))
b = float(input("Введите второе значение "))
c = float(input("Введите третье значение "))
print("Сумма максимальных элементов = " + str(my_func(a, b, c)))

