import pandas as pd
import numpy as np

s1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s1.dtype)

s2 = pd.Series([10, 20, 30], index=["a", "b", "c"], dtype=np.float64)
print(s2.dtype)