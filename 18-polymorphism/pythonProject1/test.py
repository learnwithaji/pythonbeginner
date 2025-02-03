for num in range(1, 500):
    num_str = str(num)
    num_digits = len(num_str)

    total_sum = 0
    for digit in num_str:
        total_sum += int(digit) ** num_digits

    if total_sum == num:
        print(total_sum)
