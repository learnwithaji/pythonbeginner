frequent_customer = False
has_no_claims = False
car_age_under_5 = False

eligible=[frequent_customer, has_no_claims, car_age_under_5]
if any(eligible):
    print("Car is eligible for a discount on insurance.")
else:
    print("Car is not eligible for a discount on insurance.")
