class Calculator:
    def add(self, *args):
        print(args)
        return sum(args)

calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(10, 20, 30, 40))
print(calc.add(10, 20, 30, 40, 50))
