class Animal:
    def sound(self):
        print("Animal makes a sound")

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Bat(Mammal, Bird):
    pass

bat = Bat()
bat.sound()
