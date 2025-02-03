class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Paid ${amount:.2f} using Credit Card ending {self.card_number[-4:]}."

class Cash:
    def __init__(self, amount):
        self.amount = amount

    def pay(self, amount):
        if amount > self.amount:
            return "Insufficient cash to complete the payment."
        self.amount -= amount
        return f"Paid ${amount:.2f} using Cash. Remaining cash: ${self.amount:.2f}."

def process_payment(payment_method, amount):
    print(payment_method.pay(amount))

credit_card_payment = CreditCard("1234-5678-9012-3456")
cash_payment = Cash(50)

process_payment(credit_card_payment, 30)
process_payment(cash_payment, 20)
process_payment(cash_payment, 40)
