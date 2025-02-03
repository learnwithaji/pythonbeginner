from functools import reduce

values = [10, 30, 50, 20]
max_value = reduce(lambda x, y: x if x > y else y, values)
print("Maximum value:", max_value)
