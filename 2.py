def my_func(**kwargs):
    result = ''
    for i in kwargs.values():
        result = result + ', ' + str(i)
    return result[2:]

name = input("Введите имя пользователя ")
lname = input("Введите фамилию пользователя ")
year = int(input("Введите год рождения пользователя "))
city = input("Введите город проживания пользователя ")
email = input("Введите электронную почту пользователя ")
phone = input("Введите телефон пользователя ")

print("Данные пользователя: " + my_func(name = name, lname = lname, year = year, city = city, email = email, phone = phone))

