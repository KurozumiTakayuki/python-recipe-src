import pandas as pd
import numpy as np

data = {'name': ['Apple', 'Orange', 'Banana'], 'stock': [15, None, 20]}
df = pd.DataFrame(data)
df2 = df.replace(np.NaN, 0)
print(df2)
