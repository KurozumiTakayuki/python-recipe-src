from datetime import datetime

# 現在時刻を取得
dt = datetime.now()

# datetime型から文字列に変換
datetime_str = dt.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)
