import math
class Cell:
    def __init__(self, cnt):
        if isinstance(cnt, int):
            self.cnt = cnt
        else:
            print("Необходимо целочисленное значение!")
    def __str__(self):
        return f"{self.cnt}"
    def __add__(self, other):
        return Cell(self.cnt + other.cnt)
    def __sub__(self, other):
        return Cell(int(math.fabs(self.cnt - other.cnt)))
    def __mul__(self, other):
        return Cell(self.cnt * other.cnt)
    def __truediv__(self, other):
        return Cell(math.floor(self.cnt / other.cnt))
    def make_order(self, row):
        if isinstance(row, int):
            return ('*' * self.cnt + '\n') * (row // self.cnt) + '*' * (row % self.cnt)
        else:
            return "Количество рядов должно быть целочисленным!"
        return 1


a = Cell(7)
b = Cell(2)

print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a / b)
print(a.make_order(17))