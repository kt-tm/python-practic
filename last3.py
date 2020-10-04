class TypeIncorrect(Exception):
    def __init__(self, txt):
        self.txt = txt

d = []
while True:
    try:
        new_d = input("Введите элементы массива, чтобы завершить заполнение введите stop ")
        if new_d == 'stop':
            break
        d.append(int(new_d))
    except ValueError:
        d.append(new_d)
try:
    for i in range(len(d)):
        if not isinstance(d[i], int):
            raise TypeIncorrect("Элементы массива могут быть только числами")
except TypeIncorrect as err:
    print(d)
    print(err)
else:
    print(d)
    print("Массив корректен")
