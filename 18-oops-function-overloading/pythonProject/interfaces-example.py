from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, amount, recipient):
        pass

    @abstractmethod
    def refund_payment(self, transaction_id, amount):
        pass

class UPIPaymentGateway(PaymentGateway):
    def initiate_payment(self, amount, recipient):
        return f"UPI payment of ₹{amount} initiated to {recipient}."

    def refund_payment(self, transaction_id, amount):
        return f"Refund of ₹{amount} processed for transaction ID {transaction_id}."

class CardPaymentGateway(PaymentGateway):
    def initiate_payment(self, amount, card_details) :
        return f"Card payment of ₹{amount} initiated using card ending with {card_details}."

    def refund_payment(self, transaction_id, amount):
        return f"Refund of ₹{amount} processed for card transaction ID {transaction_id}."

def process_payment(gateway, amount, recipient):
    result = gateway.initiate_payment(amount, recipient)
    print(result)

upi_gateway = UPIPaymentGateway()
process_payment(upi_gateway, 500.00, "example@upi")

card_gateway = CardPaymentGateway()
process_payment(card_gateway, 1200.00, "1234567891011")
