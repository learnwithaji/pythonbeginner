from datetime import datetime
current_time = datetime.now()
new_year = datetime(2026, 1, 1)

days_left = (new_year - current_time)
print("Days Left for New Year:", days_left)
print("Days:", days_left.days)
print("Seconds:", days_left.seconds)
print("Micro Seconds:", days_left.microseconds)