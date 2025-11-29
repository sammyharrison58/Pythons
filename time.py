import datetime
import time as time_module

date = datetime.date(2025, 1, 11)
today = datetime.date.today()
time = datetime.time(12, 30, 45)
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

target_datetime = datetime.datetime(2026, 1, 1, 12, 30, 45)
current_datetime = datetime.datetime.now()
if target_datetime < current_datetime:
    print("The target date and time has already passed.")
else:
    delta = target_datetime - current_datetime
    print("Time remaining until target date and time:", delta)
print("Date:", date)
print("Today's Date:", today)
