class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("Start way")
    def stop(self):
        print("Stop way")
    def turn(self, direction):
        print(f"Turn {direction}")
    def show_speed(self):
        print(f"The current speed is {self.speed}")
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print((f"The current speed is {self.speed}" if self.speed > 60 else "Speed exceeded!"))
class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    def show_speed(self):
        print((f"The current speed is {self.speed}" if self.speed > 40 else "Speed exceeded!"))
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
print('townCar')
townCar = TownCar(90, 'red', 'name', True)
townCar.go()
townCar.turn('left')
townCar.show_speed()
townCar.stop()
print('sportCar')
sportCar = SportCar(90, 'red', 'name')
sportCar.go()
sportCar.turn('right')
sportCar.show_speed()
sportCar.stop()
print('workCar')
workCar = WorkCar(30, 'red', 'name')
workCar.go()
workCar.turn('right')
workCar.show_speed()
workCar.stop()
print('policeCar')
policeCar = PoliceCar(90, 'red', 'name')
policeCar.go()
policeCar.turn('straight')
policeCar.show_speed()
policeCar.stop()