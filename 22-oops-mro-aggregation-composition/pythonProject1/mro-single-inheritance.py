class Vehicle:
    def start(self):
        print("Starting the vehicle")

class Car(Vehicle):
    pass

my_car = Car()
my_car.start()
