class AutoInsurance:
    def __init__(self, car_model, car_age):
        self.car_model = car_model
        self.car_age = car_age

    def calculate_premium(self):
        base_premium = 500
        if self.car_age > 5:
            base_premium += 100
        return base_premium

policy1 = AutoInsurance("Mahindra Scorpio", 6)
premium = policy1.calculate_premium()
print(f"{policy1.car_model}, Insurance premium: {premium}")

policy2 = AutoInsurance("Mahindra XUV", 2)
premium = policy2.calculate_premium()
print(f"{policy2.car_model}, Insurance premium: {premium}")
