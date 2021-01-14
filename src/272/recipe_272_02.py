import pandas as pd

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 上の続き
s["c"] = 100
s.d = 200
print(s)
