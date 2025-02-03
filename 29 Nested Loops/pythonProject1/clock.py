import time

while True:
    for hour in range(24):
        for minute in range(60):
            for second in range(60):
                print(f"\r{hour:02}:{minute:02}:{second:02}", end="")
                time.sleep(1)
