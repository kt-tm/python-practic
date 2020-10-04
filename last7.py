class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a}{self.b}*i" if self.b < 0 else f"{self.a}+{self.b}*i"
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return Complex(self.a * self.b - other.a * other.b, self.a * other.b + other.a * self.b)

complex1 = Complex(3, -5)
complex2 = Complex(6, 1)
print(f"({complex1}) + ({complex2}) = {complex1 + complex2}")
print(f"({complex1}) * ({complex2}) = {complex1 * complex2}")
