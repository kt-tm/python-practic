class Matrix:
    def __init__(self, m):
        if isinstance(m,list):
            self.m = m
            self.y = len(m)
            self.x = 0
            pr_exit = False
            for i in range(self.y):
                if not isinstance(m[i],list):
                    print(type(m[i]))
                    print(m[i])
                    print("Объект не корректен")
                    break
                else:
                    for j in range(len(m[i])):
                        if not isinstance(m[i][j], int):
                            print("Элемент матрицы имеет некорректный тип данных")
                            pr_exit = True
                            break
                        else:
                            self.x = len(m[i]) if self.x < len(m[i]) else self.x
                if pr_exit:
                    break
            for i in range(self.y):
                while len(self.m[i]) < self.x:
                    self.m[i].append(0)
        else:
            print("Объект не корректен")

    def __str__(self):
        print_result = ""
        for i in range(self.y):
            for j in range(self.x):
                print_result = f"{print_result}\t{str(self.m[i][j])}"
            print_result = f"{print_result}\n"
        return print_result

    def __add__(self, other):
        if self.x != other.x or self.y != other.y:
            print('Матрицы имеют разную размерность!')
            return Matrix([])
        else:
            arr_y = []
            arr_x = []
            for i in range(self.y):
                for j in range(self.x):
                  arr_x.append(self.m[i][j] + other.m[i][j])
                arr_y.append(arr_x)
                arr_x = []
            return Matrix(arr_y)


a = Matrix([[1,2,10],[6,9]])
b = Matrix([[1,5,17],[6,9,89]])
print(a)
print(b)
print(a + b)
