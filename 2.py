# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
import random
d = [random.randint(0, 500) for i in range(10)]
y_new = [el for item, el in enumerate(d) if (item > 0 and el > d[item - 1])]
print("Old = " + str(d))
print("New = " + str(y_new))
