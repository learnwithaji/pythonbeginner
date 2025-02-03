class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Create an instance of Dog
dog = Dog()
dog.speak()  # This will call the overridden method in Dog
