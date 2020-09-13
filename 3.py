month = input("Введите месяц как число от 1 до 12 ")
month = int(month) - 1
list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
print(list[month])
month = int(month) + 1
season = None
dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8]}
for i in dict.items():
    if month in i[1]:
        season = i[0]
if season == None:
    season = 'Осень'
print(season)