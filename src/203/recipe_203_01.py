import calendar
from datetime import datetime

now_dt = datetime.now()
result = calendar.isleap(now_dt.year)
print(result)
