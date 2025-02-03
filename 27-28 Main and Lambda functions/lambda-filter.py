numbers = [1, 2, 3, 4, 5, 6]

is_even = lambda x: x % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

