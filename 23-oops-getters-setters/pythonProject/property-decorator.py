class AutoInsurance:
    def __init__(self, policy_number, premium):
        self._policy_number = policy_number
        self._premium = premium

    @property
    def premium(self):
        return "Rs." + str(self._premium)

    @premium.setter
    def premium(self, amount):
        if amount < 0:
            raise ValueError("Premium cannot be negative.")
        self._premium = amount

auto_insurance = AutoInsurance("A12345", 1200)
print(auto_insurance.premium)

auto_insurance.premium = 1400
print(auto_insurance.premium)
