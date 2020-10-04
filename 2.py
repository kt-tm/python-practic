class Road:
    __weight = 25
    __thick = 5
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._result = round((Road.__thick * Road.__weight * self._length * self._width) / 1000, 2)
a = Road(879, 19)
print(f"Необходимая масса асфальта {a._result}")