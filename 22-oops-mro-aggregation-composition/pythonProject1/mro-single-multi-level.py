class Animal:
    def sound(self):
        print("Animal makes a sound")

class Mammal(Animal):
    def sound(self):
        print("Mammal makes a sound")

class Dog(Mammal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()
