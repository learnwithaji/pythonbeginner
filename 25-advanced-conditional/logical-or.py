car_age = 1
#high risk limit 5 year

accident_count_last_year   = 2
#high risk limit 3

if car_age > 10 or accident_count_last_year > 1:
    print("High-risk premium.")
else:
    print("Standard premium.")