class Engine:
    pass

class Wheels:
    def start(self):
        print("Wheels are rotating")

class Car(Engine, Wheels):
    pass

my_car = Car()
my_car.start()
