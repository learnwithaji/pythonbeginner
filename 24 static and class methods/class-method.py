class AutoInsurance:
    promotional_discount = 0

    def __init__(self, car_model, car_age):
        self.car_model = car_model
        self.car_age = car_age

    @classmethod
    def set_promotional_discount(cls, discount):
        cls.promotional_discount = discount

    def calculate_premium(self):
        base_premium = 500
        if self.car_age > 5:
            base_premium += 100
        return base_premium - AutoInsurance.promotional_discount

policy1 = AutoInsurance("Mahindra Scorpio", 6)
policy2 = AutoInsurance("Mahindra XUV", 2)

print(f"Policy 1 Premium: {policy1.calculate_premium()}")
print(f"Policy 2 Premium: {policy2.calculate_premium()}")

AutoInsurance.set_promotional_discount(50)
print(f"After Discount Policy 1 Premium: {policy1.calculate_premium()}")
print(f"After Discount Policy 2 Premium: {policy2.calculate_premium()}")

