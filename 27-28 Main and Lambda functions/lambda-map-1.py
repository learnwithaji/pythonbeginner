#5. simpleifed
policies = [
    {"pol_no" : "p1", "car_age":10,"premium":1000},
    {"pol_no" : "p2", "car_age":4,"premium":1200},
    {"pol_no" : "p3", "car_age":2,"premium":1100},
    {"pol_no" : "p4", "car_age":15,"premium":1500}
    ]
print(policies)
discounted_policies = list(map(
                                lambda policy:
                                        {"pol_no": policy["pol_no"],
                                         "car_age": policy["car_age"],
                                         "premium": policy["premium"]-100 if policy["car_age"]<=5 else policy["premium"]}
                                            ,policies))
print(discounted_policies)