class AutoInsurance:
    def __init__(self, policy_number, premium):
        self._policy_number = policy_number
        self._premium = premium

    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, amount):
        if amount < 500:
            raise ValueError("Premium must be at least Rs.500.")
        self._premium = amount

auto_insurance = AutoInsurance("A12345", 1200)
auto_insurance.premium = 400
