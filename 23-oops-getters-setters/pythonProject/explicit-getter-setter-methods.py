class AutoInsurance:
    def __init__(self, policy_number, premium):
        self._policy_number = policy_number
        self._premium = premium

    def get_premium(self):
        return self._premium

    def set_premium(self, premium):
        if premium < 0:
            raise ValueError("Premium cannot be negative.")
        self._premium = premium

auto_insurance = AutoInsurance("A12345", 1200)
print(auto_insurance.get_premium())

auto_insurance.set_premium(1400)
print(auto_insurance.get_premium())
