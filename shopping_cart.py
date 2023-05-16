# shopping_cart.py

def add_item(item, cart):
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = 1
    return cart


def remove_item(item, cart):
    if item in cart:
        if cart[item] > 1:
            cart[item] -= 1
        else:
            del cart[item]
    return cart


def view_cart(cart):
    if not cart:
        print("Your cart is empty!")
    else:
        for item, quantity in cart.items():
            print(f"{item}: {quantity}")


def calculate_total(cart, prices):
    total = 0
    for item, quantity in cart.items():
        if item in prices:
            total += prices[item] * quantity
    return total


def checkout(cart, prices):
    total = calculate_total(cart, prices)
    print(f"Your total is: ${total:.2f}")
