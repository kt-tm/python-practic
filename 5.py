class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Метод draw класса Stationery")
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Метод draw класса Pen")
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Метод draw класса Pencil")
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Метод draw класса Handle")
a_Stationery = Stationery('Ручка')
a_Stationery.draw()
a_Pen = Pen('Ручка')
a_Pen.draw()
a_Pencil = Pencil('Карандаш')
a_Pencil.draw()
a_Handle = Handle('Маркер')
a_Handle.draw()