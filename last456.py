import datetime
from termcolor import colored, cprint
from abc import ABC, abstractmethod
# формат состояния на складе или в отделе
# {'Printer': {'l': 1}, 'Scanner': {}, 'Xerox': {'k': 1}}
# верхний уровень типы техники, нижний уровень модель и остаток

class Dept:
    def __init__(self, name):
        self.name = name
        self.goods = {"Printer": {}, "Scanner": {}, "Xerox": {}}
    @staticmethod
    def get_list_equip(self):
        return f"Отделение - {self.name} оснащено следующим образом: {self.goods}"

    def add_goods(self, *equip):
        for i in equip:
            d = self.goods[i.get_descipt[0]]
            try:
                cnt = d[i.get_descipt[1]]
                d = {i.get_descipt[1]: cnt + 1}
            except KeyError:
                d[i.get_descipt[1]] = 1
            finally:
                self.goods[i.get_descipt[0]] = d

    def del_goods(self, *equip):
        for i in equip:
            d = self.goods[i.get_descipt[0]]
            try:
                cnt = d[i.get_descipt[1]]
                if cnt - 1 == 0:
                    del d[i.get_descipt[1]]
                else:
                    d = {i.get_descipt[1]: cnt - 1}
                self.goods[i.get_descipt[0]] = d
                return True
            except KeyError:
                cprint(f"Товар отсутствует в отделении {self.name}.", 'red')
                return False

class Warehouse:
    def __init__(self, addr, square, rent):
        self.addr = addr
        self.square = square
        self.rent = rent
        self.goods = {"Printer": {}, "Scanner": {}, "Xerox": {}}

    def add_goods(self, *equip):
        for i in equip:
            d = self.goods[i.get_descipt[0]]
            try:
                cnt = d[i.get_descipt[1]]
                d = {i.get_descipt[1]: cnt + 1}
                self.goods[i.get_descipt[0]] = d
                print('Товар добавлен на склад')
            except KeyError:
                d[i.get_descipt[1]] = 1


    def sent_goods_to_dept(self, dept, *equip):
        print(f"Начинаем передачу товара в  {dept.name}.")
        for i in equip:
            d = self.goods[i.get_descipt[0]]
            try:
                cnt = d[i.get_descipt[1]]
                if cnt - 1 == 0:
                    del d[i.get_descipt[1]]
                else:
                    d = {i.get_descipt[1]: cnt - 1}
                self.goods[i.get_descipt[0]] = d
                dept.add_goods(i)
                print(f"Успешно выполена передача товара в отделение.")
            except KeyError:
                cprint('Товар отсутствует на складе! Передача товара в отделение невозможна.', 'red')

    def return_goods_from_dept(self, dept, *equip):
        print(f"Начинаем возврат товара из {dept.name}.")
        for i in equip:
            if dept.del_goods(i) == True:
                self.add_goods(i)

class OfficeEquipment(ABC):
    def __init__(self, type, maker, model, price, oper_period_year):
        self.type = type
        self.maker = maker
        self.model = model
        self.price = price
        self.dt_of_receipt = datetime.datetime.now()
        self.oper_period_year = oper_period_year
    @abstractmethod
    def get_descipt(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, maker, model, price, oper_period_year, is_color):
        super().__init__('Printer', maker, model, price, oper_period_year)
        self.is_color = is_color
    def __str__(self):
        return f"Printer = Производитель - {self.maker}, модель - {self.model}, дата поступления на склад - {self.dt_of_receipt}"
    @property
    def get_descipt(self):
        return [self.type, self.model]
    @classmethod
    def valid(cls, maker, model, price, oper_period_year, is_color):
        try:
            return cls(maker, model, round(float(price), 2), int(oper_period_year), is_color)
        except ValueError:
            cprint("Некорректно введены данные о цене или гарантии, необходимо повторить ввод", 'red')

class Scanner(OfficeEquipment):
    def __init__(self, maker, model, price, oper_period_year, speed):
        super().__init__('Scanner', maker, model, price, oper_period_year)
        self.speed = speed
    def __str__(self):
        return f"Scanner = Производитель - {self.maker}, модель - {self.model}, дата поступления на склад - {self.dt_of_receipt}"
    @property
    def get_descipt(self):
        return [self.type, self.model]
    @classmethod
    def valid(cls, maker, model, price, oper_period_year, speed):
        try:
            return cls(maker, model, round(float(price), 2), int(oper_period_year), int(speed))
        except ValueError:
            cprint("Некорректно введены данные о цене, гарантии или скорости печати, необходимо повторить ввод", 'red')

class Xerox(OfficeEquipment):
    def __init__(self, maker, model, price, oper_period_year):
        super().__init__('Xerox', maker, model, price, oper_period_year)
    def __str__(self):
        return f"Xerox = Производитель - {self.maker}, модель - {self.model}, дата поступления на склад - {self.dt_of_receipt}"
    @property
    def get_descipt(self):
        return [self.type, self.model]
    @classmethod
    def valid(cls, maker, model, price, oper_period_year):
        try:
            return cls(maker, model, round(float(price), 2), int(oper_period_year))
        except ValueError:
            cprint("Некорректно введены данные о цене, необходимо повторить ввод", 'red')


warehouse1 = Warehouse("Варшавское шоссе, стр. 5", 500, 15000)
dept1 = Dept("Бухгалтерия")

print(("Заводим товары для дальнейшей работы. Начинаем с Принтера. "))
equip = []
print1 = None
scan1 = None
x1 = None
while print1 == None:
    maker = input("Введите производителя ")
    model = input("Введите модель принтера ")
    price = input("Введите стоимость принтера, пример 5800.45 ")
    oper_period_year = input("Введите гарантию принтера в годах, пример 3 ")
    is_color = input("Введите F если принтер является цветным, иначе любой другой символ ")
    print1 = Printer.valid(maker, model, price, oper_period_year, is_color)
    print(f"Принтер успешно заведен - {print1}")
equip.append(print1)
while scan1 == None:
    maker = input("Заводим сканер. Введите производителя ")
    model = input("Введите модель сканера ")
    price = input("Введите стоимость сканера, пример 5800.45 ")
    oper_period_year = input("Введите гарантию сканера в годах, пример 3 ")
    speed = input("Введите скорость печати, пример 1 ")
    scan1 = Scanner.valid(maker, model, price, oper_period_year, speed)
    print(f"Сканнер успешно заведен - {scan1}")
equip.append(scan1)
while x1 == None:
    maker = input("Заводим ксерокс. Введите производителя ")
    model = input("Введите модель ксерокса ")
    price = input("Введите стоимость ксерокса, пример 5800.45 ")
    oper_period_year = input("Введите гарантию ксерокса в годах, пример 3 ")
    x1 = Xerox.valid(maker, model, price, oper_period_year)
    print(f"Ксерокс успешно заведен - {scan1}")
equip.append(x1)
print(f"Состояние склада - {warehouse1.goods}")
w = True
while w:
    s = input("Введите любой символ для добавления данных товаров на склад, для завершения процесса введите - stop")
    if s == 'stop':
        break
    for i in equip:
        warehouse1.add_goods(i)
    print(f"Состояние склада - {warehouse1.goods}")
    while warehouse1.goods != []:
        try:
            num = int(input("Введите 0 для работы с принтером, 1 - со сканером, 2 - с ксероксом"))
            if num not in (0, 1, 2):
                cprint("Введено некорректное значение", 'red')
                continue
            oper = input("Введите символ 's' для отправки товаров в отделение, 'r' для возвращения на склад, а для завершения процесса введите - stop")
            if oper == 'stop':
                w = False
                break
            elif oper == 'r':
                warehouse1.return_goods_from_dept(dept1, equip[num])
                print(f"Текущее состояние на складе - {warehouse1.goods}")
                print(f"Текущее состояние в отделе - {dept1.goods}")
            elif oper == 's':
                warehouse1.sent_goods_to_dept(dept1, equip[num])
                print(f"Текущее состояние на складе - {warehouse1.goods}")
                print(f"Текущее состояние в отделе - {dept1.goods}")
            elif oper not in ('s', 'r'):
                cprint("Введено некорректное значение", 'red')
        except ValueError:
            cprint("Введено некорректное значение", 'red')
            continue


