import pandas as pd

s1 = pd.Series([10, 20, 30], index=["a", "b", "c"], dtype=pd.StringDtype())
print(s1.dtype)

s2 = pd.Series([10, 20, 30], index=["a", "b", "c"], dtype=str)
print(s2.dtype)
