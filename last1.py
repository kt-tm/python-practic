class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def decomp_date(cls, str_date):
        year = int(str_date.split('-')[2])
        month = int(str_date.split('-')[1])
        day = int(str_date.split('-')[0])
        return Date(year, month, day)

    @staticmethod
    def validation(self):
        err = []
        if self.month > 12 or self.month < 1:
            err.append('Месяц должен быть от 1 и до 12!')
        if self.year > 2100 or self.year < 1900:
            err.append('Некорректен год.')
        if self.day < 1:
            err.append('День месяца не может быть меньше 1.')
        elif self.year % 4 == 0 and self.day > 29 and self.month == 2:
            err.append('День некорректен.')
        elif self.year % 4 > 0 and self.day > 28 and self.month == 2:
            err.append('День некорректен.')
        elif self.day > 30 and self.month in [4, 6, 9, 11]:
            err.append('День некорректен.')
        elif self.day > 31:
            err.append('День некорректен.')
        if len(err) == 0:
            return 'Дата корректна'
        else:
            return " ".join(err)


my_date = Date.decomp_date('29-02-2020')
print(Date.validation(my_date))
my_date_incor = Date.decomp_date('29-02-2019')
print(Date.validation(my_date_incor))