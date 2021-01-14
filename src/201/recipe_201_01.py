from datetime import time, datetime

t = datetime.strptime("12:15:05", "%H:%M:%S").time()
time_str = t.strftime("%H.%M.%S")
print(time_str)
