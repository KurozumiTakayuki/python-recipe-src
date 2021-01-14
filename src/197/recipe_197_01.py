from datetime import date, datetime

# 文字列からdatetime型さらにdate型に変換
d = datetime.strptime("2021/10/12", "%Y/%m/%d").date()

# date型から文字列に変換
date_str = d.strftime("%Y-%m-%d")
print(date_str)
