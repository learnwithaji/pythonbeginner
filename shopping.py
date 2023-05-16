import shopping_cart

# Test the add_item function
shopping_cart.add_item("apple", 1)
assert shopping_cart.cart == {"apple": 1}

# Test the remove_item function
shopping_cart.remove_item("apple")
assert shopping_cart.cart == {}

# Test the calculate_total function
shopping_cart.add_item("apple", 1)
shopping_cart.add_item("banana", 2)
total = shopping_cart.calculate_total()
assert total == 2.5

# Test the apply_discount function
discounted_total = shopping_cart.apply_discount(total, 0.1)
assert discounted_total == 2.25

# Test the checkout function
shopping_cart.checkout()
assert shopping_cart.cart == {}
