policies = [
    {"pol_no" : "p1", "car_age":10,"premium":1000},
    {"pol_no" : "p2", "car_age":4,"premium":1200},
    {"pol_no" : "p3", "car_age":2,"premium":1100},
    {"pol_no" : "p4", "car_age":15,"premium":1500}
    ]
filtered_policies = list(filter(lambda policy:
                                policy["car_age"] <= 5,
                                policies))
print(filtered_policies)