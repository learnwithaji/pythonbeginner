class AutoInsurance:
    def __init__(self, policy_number, premium):
        self.policy_number = policy_number
        self.premium = premium

auto_insurance = AutoInsurance("A12345", 1200)
print(auto_insurance.policy_number)
print(auto_insurance.premium)

auto_insurance.premium = 1300
print("Premium after change: ",auto_insurance.premium)