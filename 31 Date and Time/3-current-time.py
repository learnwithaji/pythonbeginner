import datetime
dt = datetime.datetime.now()
time_only = dt.time()
print("Time :", time_only.strftime("%H:%M:%S"))
print("Hour:", time_only.hour)
print("Minute:", time_only.minute)
print("Second:", time_only.second)
print("Microsecond:", time_only.microsecond)