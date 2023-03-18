def calculate_discounted_price(price, discount_percentage, tax_percentage):
    # calculate discounted price
    discounted_price = price - (price * discount_percentage / 100)

    # calculate tax amount
    tax_amount = discounted_price * tax_percentage / 100

    # calculate final price
    final_price = discounted_price + tax_amount

    return final_price

price = 100
discount_percentage = 10
tax_percentage = 5

final_price = calculate_discounted_price(price, discount_percentage, tax_percentage)
print(final_price) # output: 94.5
