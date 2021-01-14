from datetime import datetime

# 文字列からdatetime型を生成
dt = datetime.strptime("2021/10/12 12:05:00", "%Y/%m/%d %H:%M:%S")

# datetime型から文字列に変換
datetime_str = dt.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)
