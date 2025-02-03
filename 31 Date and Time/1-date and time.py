import datetime
dt = datetime.datetime.now()
print("Current Date and Time:", dt)
print("Current Date and Time:", type(dt))

dt_format = dt.strftime("%m/%d/%Y %H:%M:%S")
print("Current Date and Time Formatted:", dt_format)
