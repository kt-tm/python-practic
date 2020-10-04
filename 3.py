class Worker:
    def __init__(self, name, surname, position, inc_wage, inc_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": inc_wage, "bonus": inc_bonus}

class Position(Worker):
    def __init__(self, name, surname, position, inc_wage, inc_bonus):
        super().__init__(name, surname, position, inc_wage, inc_bonus)
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return float(self._income.get("wage")) + float(self._income.get("wage")) * (float(self._income.get("bonus"))/100)
a = Position('Иванов', 'Петр', 'Директор', '2000000', '10')
print(a.get_full_name())
print(a.get_total_income())