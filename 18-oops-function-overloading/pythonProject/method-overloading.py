class Calculator:
    def add(self, n1, n2, n3=0, n4=0):
        return n1 + n2 + n3 + n4

calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(10, 20, 30, 40))
