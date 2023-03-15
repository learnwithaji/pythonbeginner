n = int(input("Enter the number of Fibonacci numbers to generate: "))

# initialize the first two numbers in the series
a, b = 0, 1

# print the first n numbers in the series
for i in range(n):
    print(a)
    a, b = b, a + b
