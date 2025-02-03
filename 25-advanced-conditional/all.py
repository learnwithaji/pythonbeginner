has_no_claims = False
is_premium_member = True
is_valid_policy = True

eligibility =  [has_no_claims, is_premium_member, is_valid_policy]

if all(eligibility):
    print("Eligible for premium renewal.")
else:
    print("Not eligible for premium renewal.")
