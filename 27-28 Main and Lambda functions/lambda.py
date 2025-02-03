#1. basic - return function
add = lambda a, b: a + b
result = add(3, 4)
print(result)

#2. type
print(type(add))

#3. simplified - return result
result = (lambda a, b: a + b)(3, 4)
print(result)

#4. more simplified - inline
print((lambda x: x ** 2)(5))

#5. real life - complex
policies = [
    {"pol_no" : "p1", "car_age":10,"premium":1000},
    {"pol_no" : "p2", "car_age":4,"premium":1200},
    {"pol_no" : "p3", "car_age":2,"premium":1100},
    {"pol_no" : "p4", "car_age":15,"premium":1500}
    ]
calculate_discount = lambda policy: policy["premium"]-100 if policy["car_age"]<=5 else policy["premium"]
for p in policies:
    print(p["pol_no"], calculate_discount(p))

#to simplify this we need high order functions