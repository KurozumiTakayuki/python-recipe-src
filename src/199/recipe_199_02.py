from datetime import datetime, date, time, timedelta

# 2021/12/22のdate型を生成
d1 = date(2021, 12, 22)

# 2021/12/22 12:00:30のdatetime型を生成
dt1 = datetime(2021, 12, 22, 12, 00, 30)

# 100日分のtimedelta型を生成
delta = timedelta(days=100)

# 100日前の日付を計算
d2 = d1 - delta
dt2 = dt1 - delta

# 計算結果をprint出力
print(d2)
print(dt2)
