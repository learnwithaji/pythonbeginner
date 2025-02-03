from datetime import datetime
from pytz import timezone

time_zones = {
    "India": "Asia/Kolkata",
    "USA - New York": "America/New_York",
    "UAE": "Asia/Dubai",
    "Australia": "Australia/Sydney"
}

for place, zone in time_zones.items():
    tz = timezone(zone)
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    print(f"{place}: {current_time}")
