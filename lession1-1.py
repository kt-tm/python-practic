from datetime import datetime as DT
current_datetime = DT.now()
dt_bith = input("Введите дату рождения ")
dt_bith = DT.strptime(dt_bith, '%d.%m.%Y')
age = current_datetime.year - dt_bith.year
print(f"Ваш возраст {age}")
