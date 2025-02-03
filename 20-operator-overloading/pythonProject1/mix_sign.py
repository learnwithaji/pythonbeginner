class CustomString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return CustomString(self.value + str(other))
        elif isinstance(other, str):
            return CustomString(self.value + other)
        elif isinstance(other, CustomString):
            return CustomString(str(self.value) + str(other.value))
        else:
            return NotImplemented

    def __str__(self):
        return str(self.value)

t=CustomString("Number of Students: ")
n=100
result = t + n
print(result)


t=CustomString("Number of Students: ")
n="Hundred"
result = t + n
print(result)

t=CustomString("Average Mark: ")
m=77.5
result = t + m
print(result)

c1 = CustomString("Number of Students: ")
c2 = CustomString(100)
result = c1 + c2
print(result)