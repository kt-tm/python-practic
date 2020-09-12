revenue = input("Введите значение прибыли ")
costs = input("Введите значение издержек ")
revenue = int(revenue)
costs = int(costs)
if revenue > costs and revenue > 0:
    print("Фирма работает прибыльно")
    rent = round((revenue - costs) * 100 / revenue, 2)
    print(f"Рентабельность = {rent}")
else:
    print("Фирма работает в убыток")