class AutoInsurance:
    @staticmethod
    def validate_registration(registration_number):
        for char in registration_number:
            if not (char.isalnum() or char == '-' or char == ' '):
                return False
        return True

is_valid = AutoInsurance.validate_registration("KL-01 1234")
print(f"Registration valid: {is_valid}")

is_valid = AutoInsurance.validate_registration("KL-08 1234")
print(f"Registration valid: {is_valid}")