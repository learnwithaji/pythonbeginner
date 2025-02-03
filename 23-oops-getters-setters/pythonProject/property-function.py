class AutoInsurance:
    def __init__(self, policy_number, premium):
        self._policy_number = policy_number
        self._premium = premium

    def get_premium(self):
        return "Rs."+str(self._premium)

    def set_premium(self, amount):
        if amount < 0:
            raise ValueError("Premium cannot be negative.")
        self._premium = amount

    premium = property(get_premium, set_premium)
auto_insurance = AutoInsurance("A12345", 1200)
print(auto_insurance.premium)

auto_insurance.premium = 1300
print(auto_insurance.premium)