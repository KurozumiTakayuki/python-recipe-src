import pandas as pd
import numpy as np

data = {'col1': [1, 2, 3], 'col2': [10, 20, 30]}
df = pd.DataFrame(data, index=[0, 1, 2])
df2 = df.astype({'col1': np.float64, 'col2': pd.StringDtype()})
print(df2.dtypes)
