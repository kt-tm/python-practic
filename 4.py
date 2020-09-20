# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
import random
d = [random.randint(0, 500) for i in range(10)]
y_new = [el for el in d if d.count(el) == 1]
print("Old = " + str(d))
print("New = " + str(y_new))
