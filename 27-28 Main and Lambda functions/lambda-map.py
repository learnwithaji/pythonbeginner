celsius = [0, 10, 20, 30]

fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))
